# SQL (PostgreSQL) Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which step would keep the work within the Core scope?
A) Write tests that prove correctness and prevent regressions.
B) Uses consistent style/formatting and passes the quality gate.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 2: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Includes tests appropriate for the feature.
B) Shipping without an automated test run in CI.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 3: To satisfy the Core requirements, which step must be included?
A) Implement a small feature tied to this module in an existing starter app.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Create a short write-up: what changed, why, and how you verified it.
D) Explain the core concepts and tradeoffs for System Design Foundations.

**Your answer:** _______________

---

### Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
A) Deliverable runs locally with clear instructions.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Document decisions and constraints clearly for reviewers.
D) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.

**Your answer:** _______________

---

### Question 5: Which requirement is part of the mini-project acceptance criteria?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Implement a small feature tied to this module in an existing starter app.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 6: A reviewer approves the mini-project when which condition is met?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Includes a short README section describing assumptions and tradeoffs.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 7: You already met Core. Which action qualifies as a Better upgrade?
A) Deliverable runs locally with clear instructions.
B) Add a performance or reliability improvement and measure the impact.
C) Making performance claims without measurements.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 8: This happened during review: CI has no automated test run before release. Which mistake is it?
A) Shipping without an automated test run in CI.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Includes a short README section describing assumptions and tradeoffs.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 9: Which option represents a Beast Mode enhancement?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Includes tests appropriate for the feature.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 10: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
A) Create a short write-up: what changed, why, and how you verified it.
B) Skipping input validation and assuming “happy path”.
C) Uses consistent style/formatting and passes the quality gate.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
