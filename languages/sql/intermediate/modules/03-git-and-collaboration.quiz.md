# SQL (PostgreSQL) Intermediate — Module 03: Git and Collaboration Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Implement a small feature tied to this module in an existing starter app.
C) Includes tests appropriate for the feature.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 2: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 3: You're pressed for time but still need a safe release. Which Core action must remain?
A) Add or update documentation (README notes or ADR-style notes).
B) Includes a short README section describing assumptions and tradeoffs.
C) Includes tests appropriate for the feature.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 4: Which acceptance criterion would a reviewer check first to approve the submission?
A) Uses consistent style/formatting and passes the quality gate.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 5: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 6: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
A) Add or update documentation (README notes or ADR-style notes).
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Making performance claims without measurements.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 7: This happened during review: a performance claim was made without benchmarks. Which mistake is it?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Making performance claims without measurements.
C) Implement a small feature tied to this module in an existing starter app.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 8: Which outcome represents a transferable software engineering skill?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Document decisions and constraints clearly for reviewers.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 9: Which acceptance requirement most clearly blocks approval if missing?
A) Write tests that prove correctness and prevent regressions.
B) Implement a small feature tied to this module in an existing starter app.
C) Deliverable runs locally with clear instructions.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 10: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Explain the core concepts and tradeoffs for Git and Collaboration.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Making performance claims without measurements.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
