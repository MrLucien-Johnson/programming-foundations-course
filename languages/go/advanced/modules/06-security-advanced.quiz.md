# Go Advanced — Module 06: Security (Advanced) Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Before sign-off, which acceptance criterion must be confirmed?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Deliverable runs locally with clear instructions.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 2: Which acceptance criterion acts as a release gate for this module?
A) Includes a short README section describing assumptions and tradeoffs.
B) Add or update documentation (README notes or ADR-style notes).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 3: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 4: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Includes a short README section describing assumptions and tradeoffs.
C) Create a short write-up: what changed, why, and how you verified it.
D) Explain the core concepts and tradeoffs for Security (Advanced).

**Your answer:** _______________

---

### Question 5: Your teammate says: CI has no automated test run before release. Which common mistake is this?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Uses consistent style/formatting and passes the quality gate.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 6: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Skipping input validation and assuming “happy path”.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Uses consistent style/formatting and passes the quality gate.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 7: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Skipping input validation and assuming “happy path”.
C) Create a short write-up: what changed, why, and how you verified it.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 8: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) All work must be covered by gofmt + lint + tests in CI.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Use tooling to keep quality high: gofmt + golangci-lint.

**Your answer:** _______________

---

### Question 9: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
A) Shipping without an automated test run in CI.
B) Includes a short README section describing assumptions and tradeoffs.
C) Deliverable runs locally with clear instructions.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 10: Which Core action best reflects professional engineering practice in this situation?
A) Add a performance or reliability improvement and measure the impact.
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
