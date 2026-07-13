# Go Advanced — Module 03: Concurrency and Async Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Includes tests appropriate for the feature.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 2: Your teammate says: tests assert implementation details instead of outcomes. Which common mistake is this?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Write tests that prove correctness and prevent regressions.
C) Uses consistent style/formatting and passes the quality gate.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 3: Which Core action would a senior engineer insist on before approving the change?
A) Includes tests appropriate for the feature.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Add or update documentation (README notes or ADR-style notes).
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 4: Your tests are blocked because database tests are polluting shared data. Which requirement should you enforce?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Explain the core concepts and tradeoffs for Concurrency and Async.
C) Use tooling to keep quality high: gofmt + golangci-lint.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 5: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Write tests that prove correctness and prevent regressions.
B) Use tooling to keep quality high: gofmt + golangci-lint.
C) Implement a small feature tied to this module in an existing starter app.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 6: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Use tooling to keep quality high: gofmt + golangci-lint.
C) Create a short write-up: what changed, why, and how you verified it.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 7: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Skipping input validation and assuming “happy path”.
C) Includes a short README section describing assumptions and tradeoffs.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 8: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
A) All work must be covered by gofmt + lint + tests in CI.
B) Add or update documentation (README notes or ADR-style notes).
C) Add a performance or reliability improvement and measure the impact.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 9: Which acceptance criterion acts as a release gate for this module?
A) Shipping without an automated test run in CI.
B) Deliverable runs locally with clear instructions.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 10: In a real code review, which outcome best reflects the skill you should demonstrate?
A) All work must be covered by gofmt + lint + tests in CI.
B) Skipping input validation and assuming “happy path”.
C) Explain the core concepts and tradeoffs for Concurrency and Async.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
