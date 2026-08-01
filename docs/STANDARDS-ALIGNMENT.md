# Curriculum Standards Alignment

Internal reference for aligning Programming Foundations with UK exam boards and
chartered computing education standards. Public learner view: `docs/standards.html`.

## Sources (researched 2026-07-23)

| Body | Spec / framework | Relevance |
| --- | --- | --- |
| OCR | GCSE Computer Science J277 | Widely used; strong programming paper (02) |
| AQA | GCSE Computer Science 8525 | Algorithms + programming skills emphasis |
| Pearson Edexcel | GCSE Computer Science 1CP2 | Principles + on-screen computational thinking |
| NCCE / Teach Computing | 10-strand taxonomy + 12 pedagogical principles | National curriculum delivery standard |
| BCS | Chartered Institute for IT (via NCCE consortium) | Computing Quality Framework / teaching quality |

## OCR J277 Component 02 → our beginner path

| Spec topic | Course coverage | Status |
| --- | --- | --- |
| 2.1 Algorithms (design, search/sort awareness, trace) | Control flow + functions; project design steps | Partial — add explicit pseudocode / trace practice |
| 2.2 Programming fundamentals | Modules 2–5 (variables, operators, I/O, collections) | Strong |
| 2.3 Producing robust programs | Exercises + Task Tracker validation | Improving — project modules call out validation / testing |
| 2.4 Boolean logic | Module 3 logical operators | Strong — frame as Boolean logic explicitly |
| 2.5 Languages & IDEs | Module 1 setup | Strong |

## AQA / Edexcel shared programming skills

| Skill | Where we teach it |
| --- | --- |
| Sequence, selection, iteration | Modules 1–3 |
| Data types & structures | Modules 2, 5 |
| Subroutines / methods | Module 4 |
| File / persistent data (intro) | Task Tracker project |
| Testing & debugging | Exercises, debug challenges, quizzes |
| Computational thinking vocabulary | Standards page + module “why” sections |

## NCCE pedagogical principles → site UX

| Principle (sample) | Site / course action |
| --- | --- |
| Worked examples | Lesson code walkthroughs |
| PRIMM-style predict → run → modify | Mini playground challenges + exercises |
| Make concrete before abstract | Real-world scenarios in each module |
| Foster program comprehension | Quizzes check skills, not scavenger hunts |
| Clear, plain language | Plain English, Help page, large CTAs |

## Known gaps (prioritized)

1. **Algorithm design language** — short “design before code” blocks (pseudocode + trace tables) in Modules 3–4.
2. **Robust programs** — validation / try-except (Python) and guard clauses (C#) callouts in project modules; Python Task Tracker now includes a robust-programs checkpoint.
3. **Boolean logic naming** — add “Boolean logic” heading alias in control-flow modules.
4. **Data representation (stretch)** — optional appendix for binary/ASCII for GCSE-curious learners (noted on `standards.html`).
5. **Networks / systems theory** — out of scope for this programming track; link out on Standards page only.

## Acceptance for “exquisite alignment”

- Every beginner module maps to ≥1 exam-board programming skill on Standards page.
- Quizzes stay skill-tagged (`docs/QUIZ-ALIGNMENT-STANDARD.md`).
- Pedagogy matches NCCE: worked examples, practice, feedback, clear next step.
- No claim of official OCR/AQA/Edexcel/BCS accreditation unless separately certified.
