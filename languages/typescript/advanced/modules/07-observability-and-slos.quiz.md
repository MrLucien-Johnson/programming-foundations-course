# TypeScript Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A production fix is urgent. Which Core action is still required before release?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.
C) Explain the core concepts and tradeoffs for Observability and SLOs.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion would a reviewer check first to approve the submission?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Apply the concepts to a realistic codebase (not just toy examples).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 3: Which acceptance requirement protects review quality if enforced?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Includes tests appropriate for the feature.
C) Add a performance or reliability improvement and measure the impact.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 4: Production validation failed because tests are flaky and fail intermittently. Which testing requirement would have prevented it?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Shipping without an automated test run in CI.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 5: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Deliverable runs locally with clear instructions.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Write tests that prove correctness and prevent regressions.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 6: In a real code review, which outcome best reflects the skill you should demonstrate?
A) Implement a small feature tied to this module in an existing starter app.
B) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.
C) Write tests that prove correctness and prevent regressions.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 7: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
A) Skipping input validation and assuming “happy path”.
B) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.
C) Includes tests appropriate for the feature.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 8: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Add or update documentation (README notes or ADR-style notes).
B) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 9: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Skipping input validation and assuming “happy path”.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 10: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Implement a small feature tied to this module in an existing starter app.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
