# Java Advanced — Module 02: Architecture Patterns Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 2: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Explain the core concepts and tradeoffs for Architecture Patterns.
B) Shipping without an automated test run in CI.
C) Deliverable runs locally with clear instructions.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Shipping without an automated test run in CI.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 4: A reviewer flags feature tests fail when hitting real boundaries. Which testing requirement resolves it?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) All work must be covered by build + unit tests + slice/integration tests (Spring + DB) in CI.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 5: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Create a short write-up: what changed, why, and how you verified it.
C) Shipping without an automated test run in CI.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 6: Your tests are blocked because tests are flaky and fail intermittently. Which requirement should you enforce?
A) Uses consistent style/formatting and passes the quality gate.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Explain the core concepts and tradeoffs for Architecture Patterns.

**Your answer:** _______________

---

### Question 7: A production fix is urgent. Which Core action is still required before release?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Includes a short README section describing assumptions and tradeoffs.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 8: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Add a performance or reliability improvement and measure the impact.
B) Includes tests appropriate for the feature.
C) Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 9: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Document decisions and constraints clearly for reviewers.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 10: Which acceptance requirement most clearly blocks approval if missing?
A) Uses consistent style/formatting and passes the quality gate.
B) Explain the core concepts and tradeoffs for Architecture Patterns.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
