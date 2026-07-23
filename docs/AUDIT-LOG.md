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

### 2026-07-23 — Audit heartbeat (loop failure diagnosis)

**Why the loop “didn’t run”**
- Background shell PID for the 15m loop exited after ~78s (`exit_code: unknown`) — killed/aborted before `Start-Sleep 900` finished.
- First `AGENT_LOOP_TICK_siteaudit` only emits *after* that sleep, so no wake ever reached the agent.

**This check**
- `python scripts/audit_routes.py` → 0 errors / 0 warnings (24 HTML pages).
- Working tree clean on `main` tracking `origin/main`.

**Action**
- Restart continuous loop at **5 minutes** so ticks are more likely to survive session churn; first audit already done this turn.

---

### 2026-07-23 — Audit tick (5m loop #1)

**Routes:** `audit_routes.py` → 0 errors / 0 warnings.

**Gap:** Help page had no in-body link to Standards (nav only).

**Fix:** Added Help card “Is this an official OCR / AQA / Edexcel course?” → `standards.html`; added `#pf-resume-host` on Help for resume CTA.

**Files:** `docs/help.html`, `docs/AUDIT-LOG.md`

**Revert tip:** restore `docs/help.html` from `0a710a2` (or prior commit on main).

**Route risk:** Low — additive copy/link only.

---

### 2026-07-23 — Manual audit run

**Routes:** `audit_routes.py` → 0 errors / 0 warnings (24 pages). Loop still alive (5m cadence).

**Gaps**
1. Courses + Start Here lacked `#pf-resume-host` (resume CTA never appeared there).
2. No in-body Standards links on those entry pages (nav only).

**Fixes**
- Added resume host + Standards note/CTA on `courses.html` and `start-here.html`.
- Prior Help Standards FAQ retained (uncommitted with this batch).

**Files:** `docs/courses.html`, `docs/start-here.html`, `docs/help.html`, `docs/AUDIT-LOG.md`

**Revert tip:** restore those three HTML files from `0a710a2`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #2)

**Routes:** 0 errors / 0 warnings.

**Gap:** Beginner course pages + certificate lacked `#pf-resume-host`.

**Fix:** Added resume host to `python-course.html`, `csharp-course.html`, `ai-course.html`, `certificate.html`.

**Revert tip:** restore those files from `0a710a2`.

**Route risk:** Low.

---

### 2026-07-23 — Manual audit run #2

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. Quiz viewer did not record last quiz; lesson/quiz/support/account lacked resume hosts.
2. Homepage had no Standards body CTA.

**Fixes**
- `quiz-viewer.html`: `#pf-resume-host` + `PF.setLastQuiz` on load
- Resume hosts: `course-viewer.html`, `support.html`, `account.html`
- Homepage Standards section → `standards.html`

**Revert tip:** restore listed files from `0a710a2` / prior good SHA.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #3)

**Routes:** 0 errors / 0 warnings.

**Gap:** All 9 advanced course pages + `promo.html` lacked `#pf-resume-host`.

**Fix:** Added resume host under `<main>` on those 10 pages.

**Revert tip:** restore `docs/*-advanced-course.html` and `docs/promo.html` from `0a710a2`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #4)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. `setLastQuiz` stored data but resume banner never offered quiz resume.
2. Module 4 Functions lacked exam-board “design before code” / subroutine framing.

**Fixes**
- `docs/site.js`: resume banner prefers newer last quiz; otherwise offers Last quiz link; export `getLastQuiz`.
- Cache-bust assets to `?v=ux11` across HTML pages.
- Python Module 4: pseudocode subroutine design block (OCR/AQA/Edexcel alignment).

**Revert tip:** restore `docs/site.js`, HTML cache versions, and `python-beginner-workbook/module-04-functions/README.md` from prior commit.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #5)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. C# Module 4 lacked matching subroutine design framing.
2. Robust-programs gap (OCR 2.3) still thin on Python Task Tracker.

**Fixes**
- C# Module 4: “Design before you code (subroutines)” block.
- Python Module 7: Robust programs checkpoint before checklist.
- `STANDARDS-ALIGNMENT.md`: status note updated for 2.3.

**Revert tip:** restore those three files from prior commit / `0a710a2` where applicable.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #6)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. C# Task Tracker lacked matching robust-programs checkpoint.
2. Python/C# course pages had no Standards body CTA.
3. Route auditor omitted `promo.html`.

**Fixes**
- C# Module 7: robust programs checkpoint.
- `python-course.html` / `csharp-course.html`: Standards note + button.
- `scripts/audit_routes.py`: add `promo.html` to primary routes.

**Revert tip:** restore those files from prior commit.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #7)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. Help “Reset progress” left resume keys (`pf-last-lesson` / `pf-last-quiz`), so Continue banners could linger.
2. AI course page had no Standards / foundations cross-link.

**Fixes**
- `resetAllProgress` clears last lesson/quiz and remounts resume banner; cache `site.js?v=ux12`.
- `ai-course.html`: Standards + Python cross-links.

**Revert tip:** restore `docs/site.js` and `docs/ai-course.html` from prior commit.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #8)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. Help reset copy still omitted resume/Continue memory.
2. Standards page did not state out-of-scope theory (data representation stretch from alignment plan).

**Fixes**
- `help.html`: reset description includes Continue memory.
- `standards.html`: “Out of scope / optional stretch” section; alignment doc note updated.

**Revert tip:** restore `docs/help.html`, `docs/standards.html`, `docs/STANDARDS-ALIGNMENT.md`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #9)

**Routes:** 0 errors / 0 warnings.

**Gaps**
1. Many pages still on `styles.css?v=ux11` while JS was `ux12` (stale CSS risk for resume/standards styles).
2. Help lacked a dedicated Continue-banner FAQ.

**Fixes**
- Bump stylesheet cache to `?v=ux12` across docs HTML.
- Help card: “How do I continue where I left off?”

**Revert tip:** restore `docs/*.html` cache strings / help card from prior commit.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #10)

**Routes:** 0 errors / 0 warnings. No conflict markers. Cache versions consistent (`ux12`).

**Gaps**
1. Certificate footer lacked Standards link.
2. Route auditor did not require `config.js` (used by shared header/auth).

**Fixes**
- Certificate footer: Standards map link.
- `audit_routes.py`: add `config.js` to primary routes.

**Note:** Large uncommitted audit batch still local (~31 files). Commit/push when ready.

**Revert tip:** restore `docs/certificate.html` and `scripts/audit_routes.py`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #11)

**Routes:** 0 errors / 0 warnings. `config.js` + `tracks.html` present.

**Gap:** Support footer had Instagram only — weak path back into learning/standards.

**Fix:** Support footer links to Standards map + Help.

**Status:** Engagement/standards pass is in diminishing-returns territory; remaining value is mostly commit of local batch.

**Revert tip:** restore `docs/support.html`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #12)

**Routes:** 0 errors / 0 warnings.

**Gap:** Promo page footer only linked Support — weak return path after watching ads.

**Fix:** Promo footer adds Courses + Start Here links. Account footer adds Courses + Help.

**Revert tip:** restore `docs/promo.html`.

**Route risk:** Low.

---

### 2026-07-23 — Audit tick (5m loop #13)

**Routes:** 0 errors / 0 warnings.

**Findings:** No new actionable engagement/route gaps. Resume hosts present on 23 content pages; `tracks.html` redirect healthy; primary assets present.

**Changes:** None (verification-only).

**Note:** Local uncommitted audit batch still pending commit/push.

---

### 2026-07-23 — Audit tick (5m loop #14)

**Routes:** 0 errors / 0 warnings (24 HTML pages).

**Findings:** Verification-only — no new actionable gaps. Loop still healthy.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #15)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — site remains healthy; no new fixes.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #16)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #17)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — site remains healthy.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #18)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #19)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — site remains healthy.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #20)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #21)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — site remains healthy while org-grade planning runs in parallel.

**Changes:** None.

---

### 2026-07-23 — Feature: org persona picker (home-first)

**Need:** Learners (mostly at home) choose Schools & colleges, Corporate L&D, or Self-serve / SaaS as primary framing.

**Shipped**
- `PF.PERSONAS` + localStorage `pf-org-persona` in `docs/site.js`
- Picker on Home, Start Here, Account (`#pf-persona-host`)
- Persona-aware Standards note + course matcher tip
- Help FAQ; CSS persona cards; cache `ux13`
- Roadmap canvas updated

**Revert tip:** restore `docs/site.js`, listed HTML, `docs/styles.css` from prior commit.

**Route risk:** Low — additive UI.

---

### 2026-07-23 — Audit tick (5m loop #22)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only after persona + org-grade planning merge. Site healthy.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #23)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 — Audit tick (5m loop #24)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only — site remains healthy.

**Changes:** None.

---

### 2026-07-23 - Audit tick (5m loop #25)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only - 0 route errors.

**Changes:** None.

---

### 2026-07-23 - Audit tick (5m loop #26)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only - no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 - Audit tick (5m loop #27)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only - no new actionable gaps.

**Changes:** None.

---

### 2026-07-23 - Audit tick (5m loop #28)

**Routes:** 0 errors / 0 warnings.

**Findings:** Verification-only - no new actionable gaps.

**Changes:** None.

---
