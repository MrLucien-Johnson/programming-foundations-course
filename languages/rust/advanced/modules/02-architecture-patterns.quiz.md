# Rust Advanced — Module 02: Architecture Patterns Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement must be satisfied before submission?
A) All work must be covered by fmt + clippy + tests in CI.
B) Add or update documentation (README notes or ADR-style notes).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 2: Which task is explicitly listed as a Beast Mode upgrade?
A) Skipping input validation and assuming “happy path”.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 3: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Use tooling to keep quality high: rustfmt + clippy.
B) Implement a small feature tied to this module in an existing starter app.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Making performance claims without measurements.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 5: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Implement a small feature tied to this module in an existing starter app.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 6: Which acceptance criterion must be satisfied before submission?
A) Skipping input validation and assuming “happy path”.
B) Add or update documentation (README notes or ADR-style notes).
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 7: You already met Core. Which action qualifies as a Better upgrade?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Making performance claims without measurements.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 8: A reviewer approves the mini-project when which condition is met?
A) Uses consistent style/formatting and passes the quality gate.
B) Shipping without an automated test run in CI.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 9: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
A) Deliverable runs locally with clear instructions.
B) Use tooling to keep quality high: rustfmt + clippy.
C) Skipping input validation and assuming “happy path”.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 10: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Skipping input validation and assuming “happy path”.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Uses consistent style/formatting and passes the quality gate.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
