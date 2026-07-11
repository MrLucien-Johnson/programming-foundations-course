# SQL (PostgreSQL) Intermediate — Module 07: Debugging and Performance Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: You already met Core. Which action qualifies as a Better upgrade?
A) Deliverable runs locally with clear instructions.
B) Implement a small feature tied to this module in an existing starter app.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 2: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add or update documentation (README notes or ADR-style notes).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 3: Which step would keep the work within the Core scope?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Write tests that prove correctness and prevent regressions.
C) Implement a small feature tied to this module in an existing starter app.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 4: Which step is explicitly called out as Better work?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Explain the core concepts and tradeoffs for Debugging and Performance.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 5: A reviewer approves the mini-project when which condition is met?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Includes a short README section describing assumptions and tradeoffs.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 6: This happened during review: a performance claim was made without benchmarks. Which mistake is it?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Write tests that prove correctness and prevent regressions.
C) Making performance claims without measurements.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 7: Which requirement is part of the mini-project acceptance criteria?
A) Deliverable runs locally with clear instructions.
B) Skipping input validation and assuming “happy path”.
C) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 8: To reach Beast Mode, which improvement should you choose?
A) Add a performance or reliability improvement and measure the impact.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 9: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Add or update documentation (README notes or ADR-style notes).
B) If the module involves a database, tests must run against an isolated schema/database.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 10: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Document decisions and constraints clearly for reviewers.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
