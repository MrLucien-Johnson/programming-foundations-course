# SQL (PostgreSQL) Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which Better upgrade most improves maintainability or reliability?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Includes tests appropriate for the feature.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 2: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Create a short write-up: what changed, why, and how you verified it.
B) Uses consistent style/formatting and passes the quality gate.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 3: Which outcome represents a transferable software engineering skill?
A) Add or update documentation (README notes or ADR-style notes).
B) Write tests that prove correctness and prevent regressions.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 4: Before shipping, which Core action best reduces regression risk?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Includes tests appropriate for the feature.
C) Explain the core concepts and tradeoffs for Observability and SLOs.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 5: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Includes tests appropriate for the feature.
B) Explain the core concepts and tradeoffs for Observability and SLOs.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 6: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
A) Add or update documentation (README notes or ADR-style notes).
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 7: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
A) Includes tests appropriate for the feature.
B) Add a performance or reliability improvement and measure the impact.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 8: Which acceptance criterion would a reviewer check first to approve the submission?
A) Add or update documentation (README notes or ADR-style notes).
B) Includes a short README section describing assumptions and tradeoffs.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 9: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Uses consistent style/formatting and passes the quality gate.
C) Add or update documentation (README notes or ADR-style notes).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 10: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Uses consistent style/formatting and passes the quality gate.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Implement a small feature tied to this module in an existing starter app.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
