# Site Audit Log

Living log of audits and live fixes. Each entry includes a **revert tip** so major route
disturbances can be undone quickly.

## Baseline

| Field | Value |
| --- | --- |
| Started | 2026-07-23 |
| Pre-audit HEAD | `f94d2f9` (Softens 3D bevel texture) |
| Git tag (create after first commit) | `audit-baseline-2026-07-23` |
| Safe revert | `git checkout audit-baseline-2026-07-23 -- docs/` or restore listed files from that tag |

**Do not delete this file** while continuous auditing is active.

---

## How to revert

1. Identify the entry that caused the issue (file list below).
2. Restore those files from the baseline tag or from the previous good commit:
   ```bash
   git checkout audit-baseline-2026-07-23 -- docs/index.html docs/site.js
   ```
3. Or restore the entire docs folder:
   ```bash
   git checkout audit-baseline-2026-07-23 -- docs/
   ```
4. Re-run `python scripts/audit_routes.py` to confirm primary routes are healthy.

Primary routes that must stay healthy: `index.html`, `start-here.html`, `courses.html`,
`help.html`, `python-course.html`, `csharp-course.html`, `ai-course.html`,
`course-viewer.html`, `quiz-viewer.html`, `certificate.html`, `tracks.html` (redirect).

---

## Entries

### 2026-07-23 — Audit Round 1 (research + engagement foundation)

**Research sources**
- OCR GCSE Computer Science J277 (esp. Component 02: algorithms, programming fundamentals, robust programs, Boolean logic, languages/IDEs)
- AQA GCSE Computer Science 8525 (algorithms, programming, data representation, networks, cyber security)
- Pearson Edexcel GCSE Computer Science 1CP2 (principles + on-screen computational thinking)
- NCCE / Teach Computing Curriculum (10-strand taxonomy; 12 pedagogical principles)
- BCS, The Chartered Institute for IT (Computing Quality Framework / chartered teaching standards via NCCE consortium)

**Findings**
1. Homepage has interactive widgets but no “resume learning” path for returning learners (progress exists in localStorage but is invisible on Home).
2. Nav has no active-state feedback; Certificate and Standards are discoverability gaps.
3. Help page is thin vs beginner friction (ZIP, Module 1, quizzes, progress reset).
4. Beginner modules cover programming fundamentals well; explicit mapping to exam-board topics (algorithms design, Boolean logic framing, robust programs / validation) was not surfaced to learners.
5. No automated route integrity check for the static site.

**Changes**
- Added `docs/site.js` — shared resume CTA, active nav, last-lesson memory.
- Added `docs/standards.html` — public curriculum alignment (OCR/AQA/Edexcel/NCCE/BCS).
- Added `docs/STANDARDS-ALIGNMENT.md` — internal mapping + gap plan.
- Added `scripts/audit_routes.py` — route/file integrity checker.
- Wired resume banner + site.js into key pages; expanded Help; linked Standards from Courses/nav.
- Course viewer records last viewed lesson for resume.
- CSS: resume bar, active nav, FAQ, standards chips (`styles.css?v=audit1`).

**Files touched**
- `docs/site.js` (new)
- `docs/standards.html` (new)
- `docs/STANDARDS-ALIGNMENT.md` (new)
- `docs/AUDIT-LOG.md` (this file)
- `docs/styles.css`
- `docs/index.html`
- `docs/courses.html`
- `docs/start-here.html`
- `docs/help.html`
- `docs/python-course.html`
- `docs/csharp-course.html`
- `docs/ai-course.html`
- `docs/course-viewer.html`
- `docs/quiz-viewer.html`
- `docs/certificate.html`
- `scripts/audit_routes.py` (new)

**Revert tip:** restore listed files from `audit-baseline-2026-07-23` or `f94d2f9`.

**Route risk:** Low — additive pages/scripts; existing hrefs preserved; `tracks.html` redirect unchanged.

---

### 2026-07-23 — Audit Round 2 (nav consistency + algorithm habit)

**Findings**
1. Advanced course pages lacked Standards nav link (discoverability gap).
2. Boolean logic was taught but not named in exam-board language on C# Module 3.
3. Algorithm “design before code” habit (OCR/AQA expectation) was implicit only.

**Changes**
- Added Standards link + cache-bust on all `*-advanced-course.html` pages (fixed a brief bad newline during batch edit — verified clean).
- Python Module 3: pseudocode “Design before you code” block.
- C# Module 3: Boolean logic framing.
- Playground toolbar wraps challenge chips cleanly on small screens.

**Files touched**
- `docs/*-advanced-course.html` (9 files)
- `python-beginner-workbook/module-03-control-flow/README.md`
- `csharp-beginner-workbook/module-03-control-flow/README.md`
- `docs/styles.css`

**Revert tip:** `git checkout audit-baseline-2026-07-23 -- docs/` then re-apply Round 1 only if needed; or restore the listed files from HEAD~n after commit.

**Route risk:** Low after nav fix verification. Run `python scripts/audit_routes.py`.

---

### 2026-07-23 — Audit Round 3 (playground + continuous loop)

**Changes**
- Homepage playground: Ctrl/Cmd+Enter runs code (faster practice loop).
- Armed continuous audit loop every 15 minutes (sentinel `AGENT_LOOP_TICK_siteaudit`).
- Baseline tag: `audit-baseline-2026-07-23` → commit `f94d2f9`.

**Revert tip:** restore `docs/index.html` from baseline if playground JS misbehaves; kill loop PID if continuous auditing should stop.

**Route risk:** None — additive keydown handler only.

---

### 2026-07-23 — Rebase onto remote main (accounts / support / promo)

**Context**
Remote main had advanced (accounts API, Support, shared `site.js` header, promo assets). Rebase conflicts resolved by keeping remote site shell and merging audit features into it.

**Merged into remote architecture**
- `Standards` nav link in shared `NAV_LINKS`
- Resume banner + last-lesson memory + playground challenge chips in `docs/site.js`
- `docs/standards.html` updated to `data-pf-header` / `config.js` pattern
- Module 3 Boolean / algorithm framing retained
- Route auditor updated for Support + Account pages

**Revert tip:** `git checkout audit-baseline-2026-07-23 -- docs/` only restores pre-accounts docs; prefer reverting this commit SHA after push if needed.

---
