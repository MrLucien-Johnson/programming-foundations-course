# Python Intermediate — Module 06: Security Basics Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Add or update documentation (README notes or ADR-style notes).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 2: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Making performance claims without measurements.
B) Deliverable runs locally with clear instructions.
C) Shipping without an automated test run in CI.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 3: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
A) All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.
B) Making performance claims without measurements.
C) Document decisions and constraints clearly for reviewers.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 4: Which acceptance criterion acts as a release gate for this module?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Includes a short README section describing assumptions and tradeoffs.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 5: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Add a performance or reliability improvement and measure the impact.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Includes tests appropriate for the feature.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 6: You're pressed for time but still need a safe release. Which Core action must remain?
A) Implement a small feature tied to this module in an existing starter app.
B) Making performance claims without measurements.
C) Includes a short README section describing assumptions and tradeoffs.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 7: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Add or update documentation (README notes or ADR-style notes).
B) Use tooling to keep quality high: ruff + black (or ruff format).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 8: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Includes a short README section describing assumptions and tradeoffs.
B) Making performance claims without measurements.
C) Add a performance or reliability improvement and measure the impact.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 9: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Add a performance or reliability improvement and measure the impact.
B) All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.
C) Document decisions and constraints clearly for reviewers.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 10: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
A) Add or update documentation (README notes or ADR-style notes).
B) Shipping without an automated test run in CI.
C) Deliverable runs locally with clear instructions.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
