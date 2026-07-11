# SQL (PostgreSQL) Intermediate — Module 04: APIs and Auth Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which acceptance requirement protects review quality if enforced?
A) Create a short write-up: what changed, why, and how you verified it.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Uses consistent style/formatting and passes the quality gate.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 2: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Shipping without an automated test run in CI.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 3: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Add a performance or reliability improvement and measure the impact.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 4: A production fix is urgent. Which Core action is still required before release?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Making performance claims without measurements.
C) Add a performance or reliability improvement and measure the impact.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 5: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Making performance claims without measurements.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 6: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Implement a small feature tied to this module in an existing starter app.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 7: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
A) Includes a short README section describing assumptions and tradeoffs.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Skipping input validation and assuming “happy path”.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 8: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 9: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Implement a small feature tied to this module in an existing starter app.
B) Includes a short README section describing assumptions and tradeoffs.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 10: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Apply the concepts to a realistic codebase (not just toy examples).
C) Making performance claims without measurements.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
