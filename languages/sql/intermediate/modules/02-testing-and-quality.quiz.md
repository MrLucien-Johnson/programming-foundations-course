# SQL (PostgreSQL) Intermediate — Module 02: Testing and Quality Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add a performance or reliability improvement and measure the impact.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 2: Which Better upgrade most improves maintainability or reliability?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Deliverable runs locally with clear instructions.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 3: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
A) Explain the core concepts and tradeoffs for Testing and Quality.
B) Deliverable runs locally with clear instructions.
C) Document decisions and constraints clearly for reviewers.
D) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Your answer:** _______________

---

### Question 4: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Create a short write-up: what changed, why, and how you verified it.
B) All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 5: Which outcome represents a transferable software engineering skill?
A) Document decisions and constraints clearly for reviewers.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 6: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Shipping without an automated test run in CI.
B) Includes tests appropriate for the feature.
C) Implement a small feature tied to this module in an existing starter app.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 7: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
A) Skipping input validation and assuming “happy path”.
B) Explain the core concepts and tradeoffs for Testing and Quality.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 8: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Uses consistent style/formatting and passes the quality gate.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 9: Before sign-off, which acceptance criterion must be confirmed?
A) Document decisions and constraints clearly for reviewers.
B) Includes a short README section describing assumptions and tradeoffs.
C) Write tests that prove correctness and prevent regressions.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 10: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Implement a small feature tied to this module in an existing starter app.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Includes a short README section describing assumptions and tradeoffs.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
