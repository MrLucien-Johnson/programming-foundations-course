# Python Advanced — Module 08: CI/CD and Release Strategies Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Use tooling to keep quality high: ruff + black (or ruff format).
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 2: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Includes tests appropriate for the feature.
C) Create a short write-up: what changed, why, and how you verified it.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 3: Your tests are blocked because tests are flaky and fail intermittently. Which requirement should you enforce?
A) Deliverable runs locally with clear instructions.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Add a performance or reliability improvement and measure the impact.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 4: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Includes a short README section describing assumptions and tradeoffs.
C) Add or update documentation (README notes or ADR-style notes).
D) Use tooling to keep quality high: ruff + black (or ruff format).

**Your answer:** _______________

---

### Question 5: Which acceptance criterion would a reviewer check first to approve the submission?
A) Deliverable runs locally with clear instructions.
B) Explain the core concepts and tradeoffs for CI/CD and Release Strategies.
C) Add or update documentation (README notes or ADR-style notes).
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 6: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
A) Deliverable runs locally with clear instructions.
B) Use tooling to keep quality high: ruff + black (or ruff format).
C) Shipping without an automated test run in CI.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 7: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Includes tests appropriate for the feature.
B) Create a short write-up: what changed, why, and how you verified it.
C) Add a performance or reliability improvement and measure the impact.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 8: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Add or update documentation (README notes or ADR-style notes).
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 9: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Add a performance or reliability improvement and measure the impact.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 10: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Create a short write-up: what changed, why, and how you verified it.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
