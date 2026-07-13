# TypeScript Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your tests are blocked because database tests are polluting shared data. Which requirement should you enforce?
A) Making performance claims without measurements.
B) Write tests that prove correctness and prevent regressions.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Explain the core concepts and tradeoffs for Reliability and Resilience.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion acts as a release gate for this module?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Includes a short README section describing assumptions and tradeoffs.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 3: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 4: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Deliverable runs locally with clear instructions.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 5: Which outcome best captures the practical ability you should carry forward?
A) Explain the core concepts and tradeoffs for Reliability and Resilience.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Deliverable runs locally with clear instructions.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 6: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Implement a small feature tied to this module in an existing starter app.
B) Add or update documentation (README notes or ADR-style notes).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 7: A reviewer asks for stronger engineering discipline. Which Better action fits?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Create a short write-up: what changed, why, and how you verified it.
C) Document decisions and constraints clearly for reviewers.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 8: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
A) Skipping input validation and assuming “happy path”.
B) Includes tests appropriate for the feature.
C) Explain the core concepts and tradeoffs for Reliability and Resilience.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 9: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Implement a small feature tied to this module in an existing starter app.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 10: You're pressed for time but still need a safe release. Which Core action must remain?
A) Includes a short README section describing assumptions and tradeoffs.
B) Implement a small feature tied to this module in an existing starter app.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
