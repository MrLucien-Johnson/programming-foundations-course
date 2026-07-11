# SQL (PostgreSQL) Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Before shipping, which Core action best reduces regression risk?
A) Includes tests appropriate for the feature.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Add or update documentation (README notes or ADR-style notes).
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 2: You're pressed for time but still need a safe release. Which Core action must remain?
A) Document decisions and constraints clearly for reviewers.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 3: Which outcome represents a transferable software engineering skill?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Document decisions and constraints clearly for reviewers.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 4: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Skipping input validation and assuming “happy path”.
B) Add a performance or reliability improvement and measure the impact.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Explain the core concepts and tradeoffs for Reliability and Resilience.

**Your answer:** _______________

---

### Question 5: Which Better upgrade most improves maintainability or reliability?
A) Skipping input validation and assuming “happy path”.
B) Document decisions and constraints clearly for reviewers.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Explain the core concepts and tradeoffs for Reliability and Resilience.

**Your answer:** _______________

---

### Question 6: Production validation failed because tests are flaky and fail intermittently. Which testing requirement would have prevented it?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Implement a small feature tied to this module in an existing starter app.
C) Shipping without an automated test run in CI.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 7: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Deliverable runs locally with clear instructions.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 8: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Add a performance or reliability improvement and measure the impact.
B) Write tests that prove correctness and prevent regressions.
C) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 9: CI is failing because lint/format/type errors are breaking CI. Which testing requirement addresses this?
A) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
B) Implement a small feature tied to this module in an existing starter app.
C) Uses consistent style/formatting and passes the quality gate.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 10: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Includes a short README section describing assumptions and tradeoffs.
D) Explain the core concepts and tradeoffs for Reliability and Resilience.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
