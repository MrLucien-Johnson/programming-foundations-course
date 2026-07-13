# Python Advanced — Module 04: Performance and Profiling Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Before sign-off, which acceptance criterion must be confirmed?
A) Includes tests appropriate for the feature.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion would a reviewer check first to approve the submission?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Making performance claims without measurements.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Deliverable runs locally with clear instructions.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 4: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Write tests that prove correctness and prevent regressions.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Deliverable runs locally with clear instructions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 5: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Add a performance or reliability improvement and measure the impact.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 6: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Explain the core concepts and tradeoffs for Performance and Profiling.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 7: Which Core action would a senior engineer insist on before approving the change?
A) Deliverable runs locally with clear instructions.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 8: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Apply the concepts to a realistic codebase (not just toy examples).
C) Create a short write-up: what changed, why, and how you verified it.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 9: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Implement a small feature tied to this module in an existing starter app.
B) Deliverable runs locally with clear instructions.
C) Create a short write-up: what changed, why, and how you verified it.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 10: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Implement a small feature tied to this module in an existing starter app.
C) Skipping input validation and assuming “happy path”.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
