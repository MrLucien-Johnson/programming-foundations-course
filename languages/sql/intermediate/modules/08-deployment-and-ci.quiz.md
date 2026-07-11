# SQL (PostgreSQL) Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 2: A reviewer checks the Core checklist. Which action should they see?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Add a performance or reliability improvement and measure the impact.
C) Document decisions and constraints clearly for reviewers.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 3: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Write tests that prove correctness and prevent regressions.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Shipping without an automated test run in CI.
C) Uses consistent style/formatting and passes the quality gate.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 5: Which option is listed under Better work for this module?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Skipping input validation and assuming “happy path”.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 6: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Includes a short README section describing assumptions and tradeoffs.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 7: Which option represents a Beast Mode enhancement?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Includes a short README section describing assumptions and tradeoffs.
C) Shipping without an automated test run in CI.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 8: Your project passes review only if which condition is true?
A) Making performance claims without measurements.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Includes a short README section describing assumptions and tradeoffs.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 9: This happened during review: CI has no automated test run before release. Which mistake is it?
A) Includes tests appropriate for the feature.
B) Deliverable runs locally with clear instructions.
C) Shipping without an automated test run in CI.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 10: Which acceptance criterion must be satisfied before submission?
A) Uses consistent style/formatting and passes the quality gate.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
