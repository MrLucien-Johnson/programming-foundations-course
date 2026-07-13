# C# Advanced — Module 04: Performance and Profiling Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which acceptance criterion acts as a release gate for this module?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 2: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Skipping input validation and assuming “happy path”.
B) Write tests that prove correctness and prevent regressions.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Use tooling to keep quality high: dotnet format + analyzers.

**Your answer:** _______________

---

### Question 3: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
A) Document decisions and constraints clearly for reviewers.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 4: Which testing requirement would you verify in CI before approving the change?
A) All work must be covered by build + tests + analyzers in CI.
B) Skipping input validation and assuming “happy path”.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 5: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Includes tests appropriate for the feature.
B) Making performance claims without measurements.
C) Skipping input validation and assuming “happy path”.
D) Use tooling to keep quality high: dotnet format + analyzers.

**Your answer:** _______________

---

### Question 6: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
A) Skipping input validation and assuming “happy path”.
B) Explain the core concepts and tradeoffs for Performance and Profiling.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 7: You're pressed for time but still need a safe release. Which Core action must remain?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 8: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add or update documentation (README notes or ADR-style notes).
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 9: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Deliverable runs locally with clear instructions.
B) Add a performance or reliability improvement and measure the impact.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 10: Which Core action best reflects professional engineering practice in this situation?
A) Includes tests appropriate for the feature.
B) Shipping without an automated test run in CI.
C) Add or update documentation (README notes or ADR-style notes).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
