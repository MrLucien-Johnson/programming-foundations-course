# SQL (PostgreSQL) Intermediate — Module 07: Debugging and Performance Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) Create a short write-up: what changed, why, and how you verified it.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Document decisions and constraints clearly for reviewers.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 2: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add or update documentation (README notes or ADR-style notes).
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 3: Which acceptance criterion acts as a release gate for this module?
A) Shipping without an automated test run in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 4: Which outcome best captures the practical ability you should carry forward?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add or update documentation (README notes or ADR-style notes).
C) Document decisions and constraints clearly for reviewers.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 5: Which Better upgrade most improves maintainability or reliability?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Includes a short README section describing assumptions and tradeoffs.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 6: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Implement a small feature tied to this module in an existing starter app.
B) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Explain the core concepts and tradeoffs for Debugging and Performance.

**Your answer:** _______________

---

### Question 7: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Deliverable runs locally with clear instructions.
B) Implement a small feature tied to this module in an existing starter app.
C) Add a performance or reliability improvement and measure the impact.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 8: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Deliverable runs locally with clear instructions.
C) Create a short write-up: what changed, why, and how you verified it.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 9: Which Core action would a senior engineer insist on before approving the change?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Add a performance or reliability improvement and measure the impact.
C) Add or update documentation (README notes or ADR-style notes).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 10: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Deliverable runs locally with clear instructions.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Create a short write-up: what changed, why, and how you verified it.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
