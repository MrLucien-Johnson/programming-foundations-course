# SQL (PostgreSQL) Intermediate — Module 02: Testing and Quality Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 2: You already met Core. Which action qualifies as a Better upgrade?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Skipping input validation and assuming “happy path”.
C) Write tests that prove correctness and prevent regressions.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 3: Which item is explicitly required in the acceptance criteria?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Explain the core concepts and tradeoffs for Testing and Quality.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 4: Which option is listed under Better work for this module?
A) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 5: Which common mistake matches this scenario: tests assert implementation details instead of outcomes?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 6: Which acceptance criterion must be satisfied before submission?
A) Shipping without an automated test run in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Implement a small feature tied to this module in an existing starter app.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 7: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Shipping without an automated test run in CI.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 8: A reviewer checks the Core checklist. Which action should they see?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 9: Which option represents a Beast Mode enhancement?
A) Document decisions and constraints clearly for reviewers.
B) Add a performance or reliability improvement and measure the impact.
C) Write tests that prove correctness and prevent regressions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 10: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
A) Skipping input validation and assuming “happy path”.
B) Add or update documentation (README notes or ADR-style notes).
C) Explain the core concepts and tradeoffs for Testing and Quality.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
