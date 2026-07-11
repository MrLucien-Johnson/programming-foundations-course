# SQL (PostgreSQL) Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
A) Includes tests appropriate for the feature.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Add or update documentation (README notes or ADR-style notes).
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 2: A reviewer checks the Core checklist. Which action should they see?
A) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
B) Implement a small feature tied to this module in an existing starter app.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 3: Your teammate says: CI has no automated test run before release. Which common mistake is this?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Explain the core concepts and tradeoffs for Reliability and Resilience.
C) Shipping without an automated test run in CI.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 4: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add a performance or reliability improvement and measure the impact.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 5: Which enhancement is a Better-level upgrade (not Beast Mode)?
A) Skipping input validation and assuming “happy path”.
B) Document decisions and constraints clearly for reviewers.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Explain the core concepts and tradeoffs for Reliability and Resilience.

**Your answer:** _______________

---

### Question 6: Your tests are blocked by tests are flaky and fail intermittently. Which requirement should you enforce?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Implement a small feature tied to this module in an existing starter app.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 7: Which acceptance criterion must be satisfied before submission?
A) Deliverable runs locally with clear instructions.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 8: Which improvement moves a Core submission to the Better tier?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
C) Document decisions and constraints clearly for reviewers.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 9: Which requirement is part of the mini-project acceptance criteria?
A) Includes a short README section describing assumptions and tradeoffs.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 10: Which action pushes the work into Beast Mode?
A) Write tests that prove correctness and prevent regressions.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Add a performance or reliability improvement and measure the impact.
D) Making performance claims without measurements.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
