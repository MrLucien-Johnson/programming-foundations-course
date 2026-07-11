# Java Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement is most relevant to this issue: feature tests fail when hitting real boundaries?
A) All work must be covered by build + unit tests + slice/integration tests (Spring + DB) in CI.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Explain the core concepts and tradeoffs for Observability and SLOs.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 2: A production fix is urgent. Which Core action is still required before release?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Implement a small feature tied to this module in an existing starter app.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Skipping input validation and assuming “happy path”.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 4: Your teammate says: a performance claim was made without benchmarks. Which common mistake is this?
A) Making performance claims without measurements.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 5: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Write tests that prove correctness and prevent regressions.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 6: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Add or update documentation (README notes or ADR-style notes).
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Includes tests appropriate for the feature.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 7: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Making performance claims without measurements.
D) Explain the core concepts and tradeoffs for Observability and SLOs.

**Your answer:** _______________

---

### Question 8: Which acceptance criterion would a reviewer check first to approve the submission?
A) Includes tests appropriate for the feature.
B) Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).
C) Add or update documentation (README notes or ADR-style notes).
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 9: Which acceptance criterion acts as a release gate for this module?
A) Uses consistent style/formatting and passes the quality gate.
B) Add or update documentation (README notes or ADR-style notes).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Explain the core concepts and tradeoffs for Observability and SLOs.

**Your answer:** _______________

---

### Question 10: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
