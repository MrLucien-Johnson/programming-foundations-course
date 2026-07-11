# Kotlin Intermediate — Module 04: APIs and Auth Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Skipping input validation and assuming “happy path”.
B) Deliverable runs locally with clear instructions.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 2: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
A) All work must be covered by build + tests + static analysis in CI.
B) Skipping input validation and assuming “happy path”.
C) Document decisions and constraints clearly for reviewers.
D) Add a performance or reliability improvement and measure the impact.

**Your answer:** _______________

---

### Question 3: You're pressed for time but still need a safe release. Which Core action must remain?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Implement a small feature tied to this module in an existing starter app.
C) Add a performance or reliability improvement and measure the impact.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 4: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Uses consistent style/formatting and passes the quality gate.
C) Use tooling to keep quality high: ktlint + detekt.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 5: Which acceptance criterion would a reviewer check first to approve the submission?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Deliverable runs locally with clear instructions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 6: Which Better upgrade most improves maintainability or reliability?
A) Over-mocking (tests assert implementation details instead of outcomes).
B) Implement a small feature tied to this module in an existing starter app.
C) Skipping input validation and assuming “happy path”.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 7: Which acceptance criterion acts as a release gate for this module?
A) Uses consistent style/formatting and passes the quality gate.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) All work must be covered by build + tests + static analysis in CI.

**Your answer:** _______________

---

### Question 8: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Use tooling to keep quality high: ktlint + detekt.
B) Add a performance or reliability improvement and measure the impact.
C) Skipping input validation and assuming “happy path”.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 9: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Apply the concepts to a realistic codebase (not just toy examples).
C) Use tooling to keep quality high: ktlint + detekt.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 10: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Shipping without an automated test run in CI.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
