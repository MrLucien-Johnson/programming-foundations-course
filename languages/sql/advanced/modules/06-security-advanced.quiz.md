# SQL (PostgreSQL) Advanced — Module 06: Security (Advanced) Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which outcome best captures the practical ability you should carry forward?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Includes a short README section describing assumptions and tradeoffs.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 2: Your tests are blocked by lint/format/type errors are breaking CI. Which requirement should you enforce?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 3: Which acceptance requirement most clearly blocks approval if missing?
A) Add or update documentation (README notes or ADR-style notes).
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Includes a short README section describing assumptions and tradeoffs.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 4: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Shipping without an automated test run in CI.
C) Write tests that prove correctness and prevent regressions.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 5: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Explain the core concepts and tradeoffs for Security (Advanced).
B) Apply the concepts to a realistic codebase (not just toy examples).
C) Over-mocking (tests assert implementation details instead of outcomes).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 6: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Implement a small feature tied to this module in an existing starter app.
B) Includes tests appropriate for the feature.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 7: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Uses consistent style/formatting and passes the quality gate.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 8: A production fix is urgent. Which Core action is still required before release?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Add or update documentation (README notes or ADR-style notes).
C) Document decisions and constraints clearly for reviewers.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 9: Which common mistake matches this scenario: a performance claim was made without benchmarks?
A) Making performance claims without measurements.
B) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
C) Explain the core concepts and tradeoffs for Security (Advanced).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 10: Which Better action best demonstrates stronger engineering discipline?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Create a short write-up: what changed, why, and how you verified it.
C) Making performance claims without measurements.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
