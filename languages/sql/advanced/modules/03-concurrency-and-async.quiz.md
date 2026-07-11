# SQL (PostgreSQL) Advanced — Module 03: Concurrency and Async Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
A) Add a performance or reliability improvement and measure the impact.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Uses consistent style/formatting and passes the quality gate.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion must be satisfied before submission?
A) Skipping input validation and assuming “happy path”.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Write tests that prove correctness and prevent regressions.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 3: Which task is explicitly listed as a Beast Mode upgrade?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Shipping without an automated test run in CI.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Skipping input validation and assuming “happy path”.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 5: A reviewer checks the Core checklist. Which action should they see?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Implement a small feature tied to this module in an existing starter app.
C) Document decisions and constraints clearly for reviewers.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 6: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add or update documentation (README notes or ADR-style notes).
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 7: Your project passes review only if which condition is true?
A) Add a performance or reliability improvement and measure the impact.
B) Document decisions and constraints clearly for reviewers.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 8: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Skipping input validation and assuming “happy path”.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 9: Which testing requirement should you apply given this issue: database tests are polluting shared data?
A) Uses consistent style/formatting and passes the quality gate.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Create a short write-up: what changed, why, and how you verified it.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 10: Which option is listed under Better work for this module?
A) Write tests that prove correctness and prevent regressions.
B) Shipping without an automated test run in CI.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
