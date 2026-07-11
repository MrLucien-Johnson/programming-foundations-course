# SQL (PostgreSQL) Advanced — Module 02: Architecture Patterns Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Skipping input validation and assuming “happy path”.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 2: Which requirement is part of the mini-project acceptance criteria?
A) Shipping without an automated test run in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 3: A reviewer approves the mini-project when which condition is met?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Deliverable runs locally with clear instructions.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 4: You already met Core. Which action qualifies as a Better upgrade?
A) Add a performance or reliability improvement and measure the impact.
B) Document decisions and constraints clearly for reviewers.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 5: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Create a short write-up: what changed, why, and how you verified it.
B) Write tests that prove correctness and prevent regressions.
C) Shipping without an automated test run in CI.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 6: Which task best matches the Core expectations for this module?
A) Making performance claims without measurements.
B) Uses consistent style/formatting and passes the quality gate.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 7: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Explain the core concepts and tradeoffs for Architecture Patterns.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Shipping without an automated test run in CI.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 8: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Add or update documentation (README notes or ADR-style notes).
B) Includes a short README section describing assumptions and tradeoffs.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 9: Which improvement moves a Core submission to the Better tier?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 10: Which action pushes the work into Beast Mode?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) If the module involves a database, tests must run against an isolated schema/database.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
