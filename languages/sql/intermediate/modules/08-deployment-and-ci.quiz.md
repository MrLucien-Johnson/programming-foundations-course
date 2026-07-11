# SQL (PostgreSQL) Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer asks for stronger engineering discipline. Which Better action fits?
A) Add a performance or reliability improvement and measure the impact.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Includes tests appropriate for the feature.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 2: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Uses consistent style/formatting and passes the quality gate.
B) Create a short write-up: what changed, why, and how you verified it.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 3: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Deliverable runs locally with clear instructions.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 4: Which outcome represents a transferable software engineering skill?
A) Deliverable runs locally with clear instructions.
B) Uses consistent style/formatting and passes the quality gate.
C) Explain the core concepts and tradeoffs for Deployment and CI.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 5: You're pressed for time but still need a safe release. Which Core action must remain?
A) Making performance claims without measurements.
B) Implement a small feature tied to this module in an existing starter app.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 6: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Write tests that prove correctness and prevent regressions.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 7: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Includes tests appropriate for the feature.
B) Add a performance or reliability improvement and measure the impact.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 8: Which acceptance criterion acts as a release gate for this module?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 9: Your tests are blocked because tests are flaky and fail intermittently. Which requirement should you enforce?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Add a performance or reliability improvement and measure the impact.
C) Document decisions and constraints clearly for reviewers.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 10: Which acceptance requirement protects review quality if enforced?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Includes tests appropriate for the feature.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
