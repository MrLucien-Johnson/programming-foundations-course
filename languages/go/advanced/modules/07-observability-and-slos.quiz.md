# Go Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Shipping without an automated test run in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 2: Which acceptance requirement most clearly blocks approval if missing?
A) Write tests that prove correctness and prevent regressions.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Includes tests appropriate for the feature.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 3: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) If the module involves a database, tests must run against an isolated schema/database.
C) Shipping without an automated test run in CI.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 4: CI is failing because lint/format/type errors are breaking CI. Which testing requirement addresses this?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Skipping input validation and assuming “happy path”.
C) All work must be covered by gofmt + lint + tests in CI.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 5: Which Core action best reflects professional engineering practice in this situation?
A) Shipping without an automated test run in CI.
B) Implement a small feature tied to this module in an existing starter app.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Explain the core concepts and tradeoffs for Observability and SLOs.

**Your answer:** _______________

---

### Question 6: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add a performance or reliability improvement and measure the impact.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 7: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Includes a short README section describing assumptions and tradeoffs.
B) Write tests that prove correctness and prevent regressions.
C) Making performance claims without measurements.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 8: This happened during review: CI has no automated test run before release. Which mistake is it?
A) All work must be covered by gofmt + lint + tests in CI.
B) Document decisions and constraints clearly for reviewers.
C) Deliverable runs locally with clear instructions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 9: Which Better upgrade most improves maintainability or reliability?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Includes a short README section describing assumptions and tradeoffs.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 10: Which outcome best captures the practical ability you should carry forward?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Skipping input validation and assuming “happy path”.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
