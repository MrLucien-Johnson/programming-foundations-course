# Go Advanced — Module 08: CI/CD and Release Strategies Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: You're pressed for time but still need a safe release. Which Core action must remain?
A) All work must be covered by gofmt + lint + tests in CI.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 2: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Deliverable runs locally with clear instructions.
B) Includes tests appropriate for the feature.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 3: Which testing requirement is most relevant to this issue: lint/format/type errors are breaking CI?
A) All work must be covered by gofmt + lint + tests in CI.
B) Includes a short README section describing assumptions and tradeoffs.
C) Making performance claims without measurements.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 4: Which Core action would a senior engineer insist on before approving the change?
A) Implement a small feature tied to this module in an existing starter app.
B) Uses consistent style/formatting and passes the quality gate.
C) Making performance claims without measurements.
D) Use tooling to keep quality high: gofmt + golangci-lint.

**Your answer:** _______________

---

### Question 5: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) Add a performance or reliability improvement and measure the impact.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 6: Before sign-off, which acceptance criterion must be confirmed?
A) Includes a short README section describing assumptions and tradeoffs.
B) Apply the concepts to a realistic codebase (not just toy examples).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 7: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Implement a small feature tied to this module in an existing starter app.
B) All work must be covered by gofmt + lint + tests in CI.
C) Includes tests appropriate for the feature.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 8: Which outcome best captures the practical ability you should carry forward?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Uses consistent style/formatting and passes the quality gate.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 9: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Making performance claims without measurements.
B) Includes tests appropriate for the feature.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) All work must be covered by gofmt + lint + tests in CI.

**Your answer:** _______________

---

### Question 10: Your teammate says: CI has no automated test run before release. Which common mistake is this?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Write tests that prove correctness and prevent regressions.
C) Shipping without an automated test run in CI.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
