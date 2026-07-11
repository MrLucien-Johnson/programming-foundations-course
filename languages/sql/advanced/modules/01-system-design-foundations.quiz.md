# SQL (PostgreSQL) Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Before shipping, which Core action best reduces regression risk?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Shipping without an automated test run in CI.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 2: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
A) Includes tests appropriate for the feature.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 3: Which outcome best captures the practical ability you should carry forward?
A) Explain the core concepts and tradeoffs for System Design Foundations.
B) Includes a short README section describing assumptions and tradeoffs.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 4: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
A) Includes tests appropriate for the feature.
B) Skipping input validation and assuming “happy path”.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 5: Which acceptance criterion acts as a release gate for this module?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Implement a small feature tied to this module in an existing starter app.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 6: Which Better upgrade most improves maintainability or reliability?
A) Deliverable runs locally with clear instructions.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Document decisions and constraints clearly for reviewers.
D) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.

**Your answer:** _______________

---

### Question 7: Which Core action best reflects professional engineering practice in this situation?
A) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
B) Explain the core concepts and tradeoffs for System Design Foundations.
C) Create a short write-up: what changed, why, and how you verified it.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 8: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Add a performance or reliability improvement and measure the impact.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 9: Which acceptance requirement most clearly blocks approval if missing?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Uses consistent style/formatting and passes the quality gate.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 10: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
