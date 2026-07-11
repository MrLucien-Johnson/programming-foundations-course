# Rust Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Write tests that prove correctness and prevent regressions.
B) Create a short write-up: what changed, why, and how you verified it.
C) Making performance claims without measurements.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 2: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Making performance claims without measurements.
B) Skipping input validation and assuming “happy path”.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 3: Which testing requirement would prevent a reviewer from rejecting the submission?
A) Create a short write-up: what changed, why, and how you verified it.
B) Implement a small feature tied to this module in an existing starter app.
C) All work must be covered by fmt + clippy + tests in CI.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 4: Which outcome represents a transferable software engineering skill?
A) Includes a short README section describing assumptions and tradeoffs.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Use tooling to keep quality high: rustfmt + clippy.

**Your answer:** _______________

---

### Question 5: Your tests are blocked because database tests are polluting shared data. Which requirement should you enforce?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Use tooling to keep quality high: rustfmt + clippy.

**Your answer:** _______________

---

### Question 6: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Uses consistent style/formatting and passes the quality gate.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 7: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Uses consistent style/formatting and passes the quality gate.
C) Create a short write-up: what changed, why, and how you verified it.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 8: Before sign-off, which acceptance criterion must be confirmed?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Includes tests appropriate for the feature.
C) Add or update documentation (README notes or ADR-style notes).
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 9: Which Core action best reflects professional engineering practice in this situation?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Uses consistent style/formatting and passes the quality gate.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 10: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Implement a small feature tied to this module in an existing starter app.
B) Deliverable runs locally with clear instructions.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
