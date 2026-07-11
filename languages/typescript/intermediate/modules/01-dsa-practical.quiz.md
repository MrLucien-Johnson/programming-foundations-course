# TypeScript Intermediate — Module 01: DSA (Practical) Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Includes tests appropriate for the feature.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 2: Which common mistake matches this scenario: CI has no automated test run before release?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 3: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Uses consistent style/formatting and passes the quality gate.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 4: Which Better action best demonstrates stronger engineering discipline?
A) Add or update documentation (README notes or ADR-style notes).
B) Uses consistent style/formatting and passes the quality gate.
C) Includes a short README section describing assumptions and tradeoffs.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 5: Which Core action best reflects professional engineering practice in this situation?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Document decisions and constraints clearly for reviewers.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 6: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Add or update documentation (README notes or ADR-style notes).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Your answer:** _______________

---

### Question 7: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Implement a small feature tied to this module in an existing starter app.
B) Includes tests appropriate for the feature.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Use tooling to keep quality high: ESLint + Prettier.

**Your answer:** _______________

---

### Question 8: Before sign-off, which acceptance criterion must be confirmed?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 9: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Create a short write-up: what changed, why, and how you verified it.
B) Implement a small feature tied to this module in an existing starter app.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Your answer:** _______________

---

### Question 10: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Deliverable runs locally with clear instructions.
B) Write tests that prove correctness and prevent regressions.
C) Skipping input validation and assuming “happy path”.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
