# SQL (PostgreSQL) Advanced — Module 02: Architecture Patterns Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which Core action best reflects professional engineering practice in this situation?
A) Making performance claims without measurements.
B) Uses consistent style/formatting and passes the quality gate.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 2: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 3: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Add a performance or reliability improvement and measure the impact.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 4: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Skipping input validation and assuming “happy path”.
B) Add a performance or reliability improvement and measure the impact.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 5: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Add or update documentation (README notes or ADR-style notes).
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Shipping without an automated test run in CI.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 6: Which acceptance requirement protects review quality if enforced?
A) Uses consistent style/formatting and passes the quality gate.
B) Making performance claims without measurements.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 7: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Implement a small feature tied to this module in an existing starter app.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 8: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Skipping input validation and assuming “happy path”.
B) Explain the core concepts and tradeoffs for Architecture Patterns.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 9: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 10: Which outcome best captures the practical ability you should carry forward?
A) Add or update documentation (README notes or ADR-style notes).
B) Includes a short README section describing assumptions and tradeoffs.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
