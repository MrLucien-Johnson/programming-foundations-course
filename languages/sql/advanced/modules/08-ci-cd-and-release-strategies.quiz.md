# SQL (PostgreSQL) Advanced — Module 08: CI/CD and Release Strategies Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which common mistake matches this scenario: CI has no automated test run before release?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Shipping without an automated test run in CI.
D) Explain the core concepts and tradeoffs for CI/CD and Release Strategies.

**Your answer:** _______________

---

### Question 2: Which Core action best reflects professional engineering practice in this situation?
A) Create a short write-up: what changed, why, and how you verified it.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Making performance claims without measurements.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 3: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Explain the core concepts and tradeoffs for CI/CD and Release Strategies.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 4: A production fix is urgent. Which Core action is still required before release?
A) Write tests that prove correctness and prevent regressions.
B) Skipping input validation and assuming “happy path”.
C) Explain the core concepts and tradeoffs for CI/CD and Release Strategies.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 5: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Uses consistent style/formatting and passes the quality gate.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 6: Production validation failed because tests are flaky and fail intermittently. Which testing requirement would have prevented it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Deliverable runs locally with clear instructions.
C) Making performance claims without measurements.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 7: Which acceptance requirement protects review quality if enforced?
A) Shipping without an automated test run in CI.
B) Includes tests appropriate for the feature.
C) Skipping input validation and assuming “happy path”.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 8: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Write tests that prove correctness and prevent regressions.
B) Deliverable runs locally with clear instructions.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 9: Which outcome best captures the practical ability you should carry forward?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Shipping without an automated test run in CI.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 10: A reviewer asks for stronger engineering discipline. Which Better action fits?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Implement a small feature tied to this module in an existing starter app.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
