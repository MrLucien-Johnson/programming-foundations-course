# Rust Advanced — Module 04: Performance and Profiling Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which acceptance requirement protects review quality if enforced?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Includes tests appropriate for the feature.
C) All work must be covered by fmt + clippy + tests in CI.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 2: Which testing requirement should be verified in CI for this module?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) All work must be covered by fmt + clippy + tests in CI.
C) Uses consistent style/formatting and passes the quality gate.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 3: Which acceptance criterion would a reviewer check first to approve the submission?
A) Write tests that prove correctness and prevent regressions.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Includes a short README section describing assumptions and tradeoffs.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 4: Which Better upgrade most improves maintainability or reliability?
A) Create a short write-up: what changed, why, and how you verified it.
B) Uses consistent style/formatting and passes the quality gate.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) All work must be covered by fmt + clippy + tests in CI.

**Your answer:** _______________

---

### Question 5: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
A) Skipping input validation and assuming “happy path”.
B) Uses consistent style/formatting and passes the quality gate.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) All work must be covered by fmt + clippy + tests in CI.

**Your answer:** _______________

---

### Question 6: Which testing requirement should you apply given this issue: database tests are polluting shared data?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Shipping without an automated test run in CI.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 7: Which Core action best reflects professional engineering practice in this situation?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Create a short write-up: what changed, why, and how you verified it.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 8: Which outcome best captures the practical ability you should carry forward?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Skipping input validation and assuming “happy path”.
C) Explain the core concepts and tradeoffs for Performance and Profiling.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 9: Which Core action would a senior engineer insist on before approving the change?
A) Shipping without an automated test run in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Use tooling to keep quality high: rustfmt + clippy.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 10: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Add or update documentation (README notes or ADR-style notes).
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
