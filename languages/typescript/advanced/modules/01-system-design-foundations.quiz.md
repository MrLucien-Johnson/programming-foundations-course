# TypeScript Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which common mistake matches this scenario: tests assert implementation details instead of outcomes?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Includes a short README section describing assumptions and tradeoffs.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 2: Which acceptance requirement protects review quality if enforced?
A) Create a short write-up: what changed, why, and how you verified it.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Includes a short README section describing assumptions and tradeoffs.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 3: Your tests are blocked because lint/format/type errors are breaking CI. Which requirement should you enforce?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Add a performance or reliability improvement and measure the impact.
D) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Your answer:** _______________

---

### Question 4: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add a performance or reliability improvement and measure the impact.
B) Explain the core concepts and tradeoffs for System Design Foundations.
C) Implement a small feature tied to this module in an existing starter app.
D) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Your answer:** _______________

---

### Question 5: A reviewer asks for stronger engineering discipline. Which Better action fits?
A) Deliverable runs locally with clear instructions.
B) Making performance claims without measurements.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 6: Which testing requirement should you apply given this issue: database tests are polluting shared data?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Use tooling to keep quality high: ESLint + Prettier.

**Your answer:** _______________

---

### Question 7: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Use tooling to keep quality high: ESLint + Prettier.
C) Add a performance or reliability improvement and measure the impact.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 8: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Add a performance or reliability improvement and measure the impact.
B) Write tests that prove correctness and prevent regressions.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 9: Which Core action best reflects professional engineering practice in this situation?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Document decisions and constraints clearly for reviewers.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 10: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Includes a short README section describing assumptions and tradeoffs.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
