"""Element-aware translation with structure preservation.

원칙:
- 일반 텍스트 → 자연스러운 한국어
- 수식(equation) → LaTeX 그대로 유지 (텍스트 주변 설명만 번역 — 여기선 통째 보존)
- 표(table) → HTML 태그/속성/구조는 그대로, 내부 텍스트만 번역
- 그림(figure)/차트(chart) → 캡션 텍스트가 있으면 번역, 이미지 자체는 보존
- 용어집을 system 프롬프트에 박아 일관된 용어 사용
"""
from __future__ import annotations

import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Callable, Iterable

ProgressCb = Callable[[int, int], None]

from bs4 import BeautifulSoup, NavigableString

from .glossary import Glossary
from .parser import Element
from .solar import SolarClient

log = logging.getLogger(__name__)

SKIP_CATEGORIES = {"header", "footer", "footnote", "page_number"}
PASSTHROUGH_CATEGORIES = {"equation"}
TABLE_CATEGORIES = {"table"}

TRANSLATE_SYSTEM = (
    "You are a precise English→Korean translator for STEM university textbooks.\n\n"
    "ABSOLUTE RULES — violating any of these makes the output unusable:\n"
    "1. Output EXACTLY ONE translation. NEVER multiple drafts, variants, alternatives, "
    "or 'final versions'. Pick the single best Korean rendering and stop.\n"
    "2. NO commentary, NO meta-explanations, NO translator notes, NO markdown headings "
    "like '**최종 번역:**' or '**다음 번역:**'. Output the translation as plain prose only.\n"
    "3. NO horizontal rules ('---'), NO bullet lists explaining choices, NO parenthetical "
    "asides discussing terminology decisions. Just the translation.\n"
    "4. Preserve any LaTeX (\\$...\\$, \\$\\$...\\$\\$, \\\\(...\\\\), \\\\[...\\\\]) and placeholders "
    "like ⟦M0⟧ EXACTLY — byte for byte.\n"
    "5. Preserve inline code, identifiers, numbers, units, and equation references verbatim.\n"
    "6. Honor the supplied terminology mapping strictly.\n\n"
    "If the input is short, the output should be short too. If the input is one sentence, "
    "the output is one sentence."
)


@dataclass
class TranslatedElement:
    element: Element
    translated_text: str
    translated_html: str


def _user_prompt(glossary: Glossary, payload: str) -> list[dict[str, str]]:
    glossary_block = glossary.as_prompt_block()
    parts = []
    if glossary_block:
        parts.append(glossary_block)
    parts.append("Translate the following to Korean. Output translation only.")
    parts.append("---")
    parts.append(payload)
    parts.append("---")
    return [
        {"role": "system", "content": TRANSLATE_SYSTEM},
        {"role": "user", "content": "\n\n".join(parts)},
    ]


_LATEX_PATTERNS = [
    (re.compile(r"\$\$[^$]+?\$\$", re.DOTALL), "display_dollar"),
    (re.compile(r"\\\[[\s\S]+?\\\]"), "display_bracket"),
    (re.compile(r"\$[^$\n]+?\$"), "inline_dollar"),
    (re.compile(r"\\\([\s\S]+?\\\)"), "inline_paren"),
]


def _protect_latex(text: str) -> tuple[str, list[str]]:
    """Replace LaTeX runs with opaque placeholders so the LLM cannot mangle them."""
    saved: list[str] = []

    def _sub(m: re.Match) -> str:
        saved.append(m.group(0))
        return f"⟦M{len(saved)-1}⟧"

    for pattern, _name in _LATEX_PATTERNS:
        text = pattern.sub(_sub, text)
    return text, saved


def _restore_latex(text: str, saved: list[str]) -> str:
    for i, original in enumerate(saved):
        text = text.replace(f"⟦M{i}⟧", original)
    return text


def _translate_text(solar: SolarClient, glossary: Glossary, text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    protected, saved = _protect_latex(text)
    out = solar.chat(messages=_user_prompt(glossary, protected), temperature=0.0)
    out = _clean_model_output(out)
    out = _restore_latex(out, saved)
    return glossary.apply(out)


_BAD_HEADER_RE = re.compile(
    r"(?m)^\s*\*{0,2}\s*(?:다음|최종|초안|대안|변경된|개선된|수정된|두\s*번째|또\s*다른)\s*[^\n]{0,40}번역[^\n]{0,30}\*{0,2}\s*[:：].*$"
)
_HR_RE = re.compile(r"(?m)^\s*-{3,}\s*$")


def _clean_model_output(out: str) -> str:
    """Strip the kinds of meta-commentary Solar likes to add despite the system prompt:
    multi-variant headers ('**최종 번역:**'), horizontal rules, parenthetical translator
    notes at the very end, leading/trailing fence markers."""
    out = out.strip()
    out = re.sub(r"^---\s*", "", out)
    out = re.sub(r"\s*---$", "", out)
    out = _BAD_HEADER_RE.sub("", out)
    out = _HR_RE.sub("", out)
    # If the model produced multiple variants separated by blank lines + header markers,
    # keep only the LAST chunk after the last variant header (usually the most polished).
    parts = re.split(r"\n\s*\n", out)
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) > 1:
        # If a part looks like translator commentary (starts with "(" and ends with ")"
        # AND mentions translation), drop it.
        parts = [
            p for p in parts
            if not (p.startswith("(") and p.endswith(")") and ("번역" in p or "translation" in p.lower()))
        ]
        out = "\n\n".join(parts) if parts else out
    return out.strip()


def _translate_table_html(solar: SolarClient, glossary: Glossary, html: str) -> str:
    """Walk the HTML tree and translate only NavigableString text nodes."""
    if not html.strip():
        return html
    soup = BeautifulSoup(html, "lxml")
    targets: list[NavigableString] = []
    for node in soup.descendants:
        if isinstance(node, NavigableString):
            s = str(node)
            if s.strip() and not s.strip().isdigit():
                targets.append(node)

    for node in targets:
        original = str(node)
        translated = _translate_text(solar, glossary, original)
        if translated:
            node.replace_with(translated)

    body = soup.body
    if body is not None:
        return body.decode_contents()
    return str(soup)


def _translate_one(
    solar: SolarClient, glossary: Glossary, elem: Element
) -> TranslatedElement:
    cat = elem.category.lower()
    if cat in SKIP_CATEGORIES or cat in PASSTHROUGH_CATEGORIES:
        return TranslatedElement(elem, elem.text, elem.html)
    if cat in TABLE_CATEGORIES:
        try:
            new_html = _translate_table_html(solar, glossary, elem.html)
        except Exception:
            log.exception("table translate failed; keeping original")
            new_html = elem.html
        return TranslatedElement(elem, elem.text, new_html)
    try:
        translated = _translate_text(solar, glossary, elem.text or elem.markdown)
    except Exception:
        log.exception("text translate failed; keeping original")
        translated = elem.text
    return TranslatedElement(elem, translated, elem.html)


def translate_elements(
    solar: SolarClient,
    glossary: Glossary,
    elements: Iterable[Element],
    *,
    on_progress: ProgressCb | None = None,
) -> list[TranslatedElement]:
    items = list(elements)
    total = len(items)
    try:
        workers = max(1, int(os.environ.get("TRANSLATE_WORKERS", "5")))
    except ValueError:
        workers = 5

    if on_progress:
        on_progress(0, total)

    if workers == 1 or total <= 1:
        out: list[TranslatedElement] = []
        for i, e in enumerate(items, 1):
            out.append(_translate_one(solar, glossary, e))
            if on_progress:
                on_progress(i, total)
        return out

    results: list[TranslatedElement | None] = [None] * total
    log_every = max(1, total // 20)  # ~5% increments
    completed = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {
            ex.submit(_translate_one, solar, glossary, elem): idx
            for idx, elem in enumerate(items)
        }
        for fut in as_completed(futures):
            idx = futures[fut]
            try:
                results[idx] = fut.result()
            except Exception:
                log.exception("worker failed for element %d; keeping original", idx)
                e = items[idx]
                results[idx] = TranslatedElement(e, e.text, e.html)
            completed += 1
            if on_progress:
                on_progress(completed, total)
            if completed % log_every == 0 or completed == total:
                log.info("translated %d/%d elements (workers=%d)", completed, total, workers)

    return [r for r in results if r is not None]
