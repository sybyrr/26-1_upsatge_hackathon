# trial.md — n8n 데모에서 얻은 설계 교훈

이 문서는 n8n으로 먼저 구현한 별도 데모(`n8n/workflow.json`)에서 얻은 설계 교훈과 실패 사례를 정리한 참고 자료다. Python 주력 코드와는 별개 구현이며, 같은 설계 원칙을 가져와 적용/미적용한 현황은 아래 1절에 정리한다.

## 0. 데모 목표

영어 원서 PDF → Upstage Document Parse 구조 분석 → Solar로 용어 추출 + 일관 번역 → 표/그림은 이미지로 보존 → 한국어 학습 노트(n8n은 Notion, Python은 DOCX/PDF) 생성.

## 1. 현재 적용 상태 (Python 주력 코드 기준)

기준 브랜치: `integrate-upstream` (사용자의 P1 작업 + upstream fork의 5개 commit 통합본).
main에 머지 전 검증 완료 상태. 자세한 통합 내역은 commit history 참고.

### ✅ 적용됨 (P0 + P1 + upstream)

**P0 — 기본 파이프라인**
- parse → glossary → 요소별 번역 → DOCX 재조립
- 표/수식/그림 이미지 보존 (Document Parse base64 + PDF crop, DOCX 직접 임베드)
- 이미지 자연 비율 유지 (픽셀→인치 환산, 강제 stretch 없음)
- header/footer/page-number drop, OCR garbage 휴리스틱, 80-char fingerprint 중복 감지
- LaTeX byte-perfect 보존 (`_protect_latex`/`_restore_latex`) — n8n에 없던 보강

**P1 — 사용자 선호 용어 + 메타데이터**
- `/translate`의 `preferred_terms` 폼 입력 + 자동 glossary 사용자 우선 merge
- `Glossary.preferred_keys`로 사용자 지정 항목 추적 (2-Pass 검토 후도 보존)
- `translation_meta` 수집: 카테고리·스킵 사유·이미지 보존·fallback·glossary·preferred 카운트
- summary JSON 출력 (`{job_id}_summary.json`) — stages별 결과, 출력 경로, warnings 포함
- 진행상황 UI + 선호 용어 textarea + 메타 그리드 + ★ 사용자 지정 마커

**upstream 통합으로 추가**
- **2-Pass glossary review** — glossary 추출 후 `awaiting_review` 단계에서 일시정지, 사용자가 UI에서 용어 추가·수정·삭제한 뒤 번역 재개 (`/jobs/{id}/glossary` POST 엔드포인트). `interactive=false`로 우회 가능
- **page-batched translation** — 같은 페이지의 paragraph/heading/list/caption을 `⟦Ek⟧` 마커로 묶어 ~3500자 단위 단일 호출 (Solar API 호출 10–30× 감소). 마커 누락 시 자동으로 per-element fallback
- **boilerplate 자동 감지** — 3+ 페이지에서 반복되는 짧은 텍스트(러닝 헤더, copyright 등)를 `pipeline/boilerplate.py`가 사전 감지해 번역 대상에서 제외
- **element-level parsed dumps** — `{job_id}_parsed.jsonl` (요소당 1줄, jq·grep용) + `{job_id}_parsed.md` (페이지 단위 사람 친화적 dump) 동시 생성
- **메타 코멘트 차단 강화** — `_META_PATTERNS` 리스트가 한·영 변형 모두 잡음 (`[정확한 번역]`, `However, to strictly...`, `(※ ...)` 등)

### 📋 미적용 (P2 또는 별도 데모로 유지)

- `layoutBlocks`/`textUnits`/`visualAssets` 명시적 분리 — 현재 `Element` 구조가 그 역할 동시 수행. Markdown/Notion exporter 도입 시점에 분리 예정
- Cloudinary 업로드 — DOCX는 base64 직접 임베드라 불필요. Notion exporter 추가 시 필요
- Notion 페이지 생성 — Python 측 미구현 (P2)
- Markdown exporter — P2
- n8n workflow ↔ Python 통합 — 의도적 분리 ([AGENTS.md](AGENTS.md))

### 🔜 다음에 할 일

- `integrate-upstream` 브랜치를 main에 commit + merge (사용자 검토 후)
- 실제 PDF로 LIVE 모드 회귀 테스트 (작은 영어 textbook PDF 1개)
- 영상 시연 준비: n8n workflow.json의 `Webhook` 노드를 `Form Trigger`로 교체 (워크플로우 자체에서 UI 제공)
- P2 우선순위 확정 후 Markdown exporter 작업 착수

### n8n workflow.json 자체

- 현재 `Webhook` 노드 진입 (binary PDF POST, 자체 UI 없음)
- 영상 시연용 UI가 필요하면 `Webhook` → `On form submission` (Form Trigger)로 교체

## 2. 핵심 설계 교훈

### 2.1 레이아웃은 코드가 보존, LLM은 텍스트만 번역

풀 HTML을 Solar에 통째로 넘겨 "구조 유지한 채 번역"을 시키면 블록 누락, 표 깨짐, `<figure>` HTML 누출, 페이지 헤더 반복 같은 문제가 발생한다. 코드가 블록 순서/타입을 보존하고, Solar에는 번역할 텍스트 단위만 보내야 한다.

### 2.2 표/그림은 이미지 우선

복잡한 표의 HTML grid는 신뢰할 수 없다 (예: confusion matrix가 셀 몇 개로 합쳐짐). Document Parse가 base64를 주면 이미지로 보존, 못 주면 텍스트 표/callout으로 fallback. Document Parse 요청에 `base64_encoding=['figure','chart','table']`을 반드시 전달.

### 2.3 긴 문서는 응답 truncation에 주의

13페이지 linear algebra PDF에서 Solar 응답 JSON이 중간에 잘렸음. n8n과 Python 모두 batch 분할로 회피한다 — Python에서는 같은 페이지 요소들을 `⟦Ek⟧` 마커로 묶어 ~3500자 단위로 보내고, 누락된 마커는 per-element로 재시도 (`_translate_page_chunk`).

## 3. 실패 사례 & 해결

| 문제 | 원인 | 해결 |
|---|---|---|
| Upstage API 인증 오류 | 헤더 수동 중복 / 자격 증명 종류 혼동 | Generic Credential → Bearer Auth 사용, `Authorization` 수동 중복 금지 |
| n8n Raw body가 `=[object Object]`로 깨짐 | `={{ ... }}` 접두 `=` 포함 | `Code` 노드에서 `JSON.stringify()`로 빌드 후 `{{ $json.bodyJson }}` (앞 `=` 제거) |
| Glossary JSON parse 실패 | Solar가 array 대신 인접 object 반환 | parser가 `[...]`, `{terms:[...]}`, `{...}{...}` 모두 허용 |
| 본문 누락/요약 | 전체 문서 단일 번역 호출에서 LLM이 스킵 | layoutBlocks/textUnits 분리, textUnits만 번역 |
| 페이지 번호/러닝 헤더가 본문에 섞임 | header/footer 블록을 본문 취급 | layout policy에서 drop (Python: `SKIP_CATEGORIES`) |
| 표가 markdown으로 깨짐 | OCR 셀 정렬 어긋남 | base64 image-first 보존 |
| 그림/차트가 이미지로 안 나옴 | base64 없이 좌표만 받음 | `base64_encoding` 요청 옵션 추가 |
| 긴 PDF 응답 JSON truncation | 단일 호출 토큰 한계 | batch 분할 또는 요소별 병렬 |

## 4. n8n workflow 사용 시 필요한 환경변수

```
UPSTAGE_API_KEY       # Bearer 토큰만 (접두 "Bearer " 없이)
NOTION_API_KEY        # Bearer 토큰만
NOTION_PARENT_PAGE_ID
CLOUDINARY_CLOUD_NAME
CLOUDINARY_UNSIGNED_UPLOAD_PRESET   # form-data로 전달, Bearer 아님
```

Python 코드는 위 중 `UPSTAGE_API_KEY`만 필수.

## 5. 한 줄 요약

n8n 데모는 Document Parse + Solar 번역 + Cloudinary 이미지 호스팅 + Notion 페이지 생성까지를 low-code로 이어붙인 별도 워크플로우이고, 같은 설계 원칙을 Python FastAPI 코드에 옮겨 DOCX/PDF 산출물로 확장한 것이 현재 주력 구현이다.
