# Go Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Skipping input validation and assuming “happy path”.
B) All work must be covered by gofmt + lint + tests in CI.
C) Add or update documentation (README notes or ADR-style notes).
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 2: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) All work must be covered by gofmt + lint + tests in CI.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 3: Which Better upgrade most improves maintainability or reliability?
A) Includes tests appropriate for the feature.
B) Implement a small feature tied to this module in an existing starter app.
C) Explain the core concepts and tradeoffs for Reliability and Resilience.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 4: Which acceptance requirement most clearly blocks approval if missing?
A) Deliverable runs locally with clear instructions.
B) Write tests that prove correctness and prevent regressions.
C) Add a performance or reliability improvement and measure the impact.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 5: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Shipping without an automated test run in CI.
B) Skipping input validation and assuming “happy path”.
C) Create a short write-up: what changed, why, and how you verified it.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 6: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Add or update documentation (README notes or ADR-style notes).
B) Write tests that prove correctness and prevent regressions.
C) Making performance claims without measurements.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 7: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Implement a small feature tied to this module in an existing starter app.
B) Add or update documentation (README notes or ADR-style notes).
C) Apply the concepts to a realistic codebase (not just toy examples).
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 8: A production fix is urgent. Which Core action is still required before release?
A) Explain the core concepts and tradeoffs for Reliability and Resilience.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Use tooling to keep quality high: gofmt + golangci-lint.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 9: Which acceptance requirement protects review quality if enforced?
A) Making performance claims without measurements.
B) Uses consistent style/formatting and passes the quality gate.
C) Add a performance or reliability improvement and measure the impact.
D) All work must be covered by gofmt + lint + tests in CI.

**Your answer:** _______________

---

### Question 10: Which Core action best reflects professional engineering practice in this situation?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Implement a small feature tied to this module in an existing starter app.
C) Document decisions and constraints clearly for reviewers.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
