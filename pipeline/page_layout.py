"""Sniff page size and margins from a source PDF so the output docx can
match the visual rhythm of the original textbook.

Strategy: open the first few pages with PyMuPDF, take the union bounding
box of all text blocks on each page, and use the medians across pages as
the inferred body region. Page numbers and running headers are filtered
out by clipping to the inner 80% of the page on each axis before
measuring — otherwise a "page 198" near the bottom edge would collapse
the bottom margin to nearly zero.

The returned dimensions are in inches (72 PDF points = 1 inch). Errors
during analysis are caught and surface as a None return — the caller
should treat that as "no auto-layout, fall back to env vars / defaults".
"""
from __future__ import annotations

import logging
import statistics
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

# Pages to inspect (more = more robust median, but slower).
DEFAULT_SAMPLE_PAGES = 5
# Trim the outer N% of each axis before computing block extents, so running
# headers / page numbers don't contaminate the margin estimate.
INNER_FRACTION = 0.85


@dataclass
class PageLayout:
    width_in: float
    height_in: float
    margin_left_in: float
    margin_right_in: float
    margin_top_in: float
    margin_bottom_in: float

    def as_dict(self) -> dict[str, float]:
        return {
            "width_in": self.width_in,
            "height_in": self.height_in,
            "margin_left_in": self.margin_left_in,
            "margin_right_in": self.margin_right_in,
            "margin_top_in": self.margin_top_in,
            "margin_bottom_in": self.margin_bottom_in,
        }


def detect(pdf_path: str | Path, *, sample_pages: int = DEFAULT_SAMPLE_PAGES) -> PageLayout | None:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        log.warning("page_layout: pymupdf not installed; skipping auto-detect")
        return None

    path = Path(pdf_path)
    if not path.exists():
        log.warning("page_layout: pdf not found at %s", path)
        return None

    try:
        doc = fitz.open(str(path))
    except Exception:
        log.exception("page_layout: failed to open %s", path)
        return None

    n = min(sample_pages, len(doc))
    if n == 0:
        doc.close()
        return None

    widths: list[float] = []
    heights: list[float] = []
    lefts: list[float] = []
    rights: list[float] = []
    tops: list[float] = []
    bots: list[float] = []

    try:
        for i in range(n):
            page = doc[i]
            w, h = page.rect.width, page.rect.height
            widths.append(w)
            heights.append(h)

            # Clip blocks to the inner region so page-edge headers/footers
            # don't dominate the margin estimate.
            inner_x0 = w * (1 - INNER_FRACTION) / 2
            inner_y0 = h * (1 - INNER_FRACTION) / 2
            inner_x1 = w - inner_x0
            inner_y1 = h - inner_y0

            try:
                blocks = page.get_text("blocks")
            except Exception:
                blocks = []

            xs0: list[float] = []
            ys0: list[float] = []
            xs1: list[float] = []
            ys1: list[float] = []
            for b in blocks:
                if len(b) < 4:
                    continue
                bx0, by0, bx1, by1 = b[0], b[1], b[2], b[3]
                # Reject blocks whose center sits outside the inner region.
                cx = (bx0 + bx1) / 2
                cy = (by0 + by1) / 2
                if not (inner_x0 <= cx <= inner_x1 and inner_y0 <= cy <= inner_y1):
                    continue
                xs0.append(bx0)
                ys0.append(by0)
                xs1.append(bx1)
                ys1.append(by1)

            if not xs0:
                continue
            lefts.append(min(xs0))
            rights.append(w - max(xs1))
            tops.append(min(ys0))
            bots.append(h - max(ys1))
    finally:
        doc.close()

    if not widths or not lefts:
        return None

    layout = PageLayout(
        width_in=statistics.median(widths) / 72.0,
        height_in=statistics.median(heights) / 72.0,
        margin_left_in=max(0.4, statistics.median(lefts) / 72.0),
        margin_right_in=max(0.4, statistics.median(rights) / 72.0),
        margin_top_in=max(0.4, statistics.median(tops) / 72.0),
        margin_bottom_in=max(0.4, statistics.median(bots) / 72.0),
    )
    log.info(
        "page_layout: %.2f x %.2f in, margins L=%.2f R=%.2f T=%.2f B=%.2f (sampled %d pages)",
        layout.width_in, layout.height_in,
        layout.margin_left_in, layout.margin_right_in,
        layout.margin_top_in, layout.margin_bottom_in,
        n,
    )
    return layout
