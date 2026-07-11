# C# Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: You already met Core. Which action qualifies as a Better upgrade?
A) Skipping input validation and assuming “happy path”.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 2: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Shipping without an automated test run in CI.
C) Implement a small feature tied to this module in an existing starter app.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 3: You're preparing a submission and need to meet the Core bar. Which action is required?
A) Includes a short README section describing assumptions and tradeoffs.
B) Create a short write-up: what changed, why, and how you verified it.
C) Implement a small feature tied to this module in an existing starter app.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 4: Which acceptance criterion must be satisfied before submission?
A) Shipping without an automated test run in CI.
B) Includes a short README section describing assumptions and tradeoffs.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Use tooling to keep quality high: dotnet format + analyzers.

**Your answer:** _______________

---

### Question 5: Which common mistake matches this scenario: CI has no automated test run before release?
A) Includes tests appropriate for the feature.
B) Shipping without an automated test run in CI.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 6: Which action qualifies as a Beast Mode stretch?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Deliverable runs locally with clear instructions.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 7: A reviewer approves the mini-project when which condition is met?
A) Includes tests appropriate for the feature.
B) Write tests that prove correctness and prevent regressions.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 8: Which option is listed under Better work for this module?
A) Add a performance or reliability improvement and measure the impact.
B) Explain the core concepts and tradeoffs for Deployment and CI.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 9: Which step would keep the work within the Core scope?
A) Shipping without an automated test run in CI.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Write tests that prove correctness and prevent regressions.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 10: Which requirement belongs in the testing checklist for this module?
A) Implement a small feature tied to this module in an existing starter app.
B) All work must be covered by build + tests + analyzers in CI.
C) Explain the core concepts and tradeoffs for Deployment and CI.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
