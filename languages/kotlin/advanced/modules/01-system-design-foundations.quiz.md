# Kotlin Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a performance or reliability improvement and measure the impact.
C) Document decisions and constraints clearly for reviewers.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 2: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Implement a small feature tied to this module in an existing starter app.
B) Skipping input validation and assuming “happy path”.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 3: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Includes tests appropriate for the feature.
B) Use tooling to keep quality high: ktlint + detekt.
C) All work must be covered by build + tests + static analysis in CI.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 4: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 5: Which testing requirement must be satisfied before submission?
A) Making performance claims without measurements.
B) All work must be covered by build + tests + static analysis in CI.
C) Implement a small feature tied to this module in an existing starter app.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 6: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) All work must be covered by build + tests + static analysis in CI.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Add or update documentation (README notes or ADR-style notes).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 7: Which acceptance requirement most clearly blocks approval if missing?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Uses consistent style/formatting and passes the quality gate.
C) Add or update documentation (README notes or ADR-style notes).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 8: Your teammate says: tests assert implementation details instead of outcomes. Which common mistake is this?
A) Includes tests appropriate for the feature.
B) Deliverable runs locally with clear instructions.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 9: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 10: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Document decisions and constraints clearly for reviewers.
C) Write tests that prove correctness and prevent regressions.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
