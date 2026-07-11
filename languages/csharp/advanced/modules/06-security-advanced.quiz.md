# C# Advanced — Module 06: Security (Advanced) Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: You're pressed for time but still need a safe release. Which Core action must remain?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) All work must be covered by build + tests + analyzers in CI.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 2: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Over-mocking (tests assert implementation details instead of outcomes).
D) Use tooling to keep quality high: dotnet format + analyzers.

**Your answer:** _______________

---

### Question 3: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Write tests that prove correctness and prevent regressions.
C) Add a performance or reliability improvement and measure the impact.
D) Explain the core concepts and tradeoffs for Security (Advanced).

**Your answer:** _______________

---

### Question 4: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Includes a short README section describing assumptions and tradeoffs.
B) Shipping without an automated test run in CI.
C) All work must be covered by build + tests + analyzers in CI.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 5: Which testing requirement must be satisfied before submission?
A) Use tooling to keep quality high: dotnet format + analyzers.
B) Includes tests appropriate for the feature.
C) All work must be covered by build + tests + analyzers in CI.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 6: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Skipping input validation and assuming “happy path”.
B) Implement a small feature tied to this module in an existing starter app.
C) Includes tests appropriate for the feature.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 7: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Skipping input validation and assuming “happy path”.
C) Add a performance or reliability improvement and measure the impact.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 8: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Includes tests appropriate for the feature.
C) Add or update documentation (README notes or ADR-style notes).
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 9: Which acceptance requirement protects review quality if enforced?
A) Document decisions and constraints clearly for reviewers.
B) Explain the core concepts and tradeoffs for Security (Advanced).
C) Uses consistent style/formatting and passes the quality gate.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 10: Which Better upgrade most improves maintainability or reliability?
A) Uses consistent style/formatting and passes the quality gate.
B) Use tooling to keep quality high: dotnet format + analyzers.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
