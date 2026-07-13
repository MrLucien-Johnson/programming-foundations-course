# Rust Intermediate — Module 07: Debugging and Performance Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Explain the core concepts and tradeoffs for Debugging and Performance.
B) Skipping input validation and assuming “happy path”.
C) Making performance claims without measurements.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion acts as a release gate for this module?
A) Deliverable runs locally with clear instructions.
B) Implement a small feature tied to this module in an existing starter app.
C) Create a short write-up: what changed, why, and how you verified it.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 3: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Write tests that prove correctness and prevent regressions.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 4: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) All work must be covered by fmt + clippy + tests in CI.
B) Shipping without an automated test run in CI.
C) Implement a small feature tied to this module in an existing starter app.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 5: Which acceptance requirement protects review quality if enforced?
A) Add a performance or reliability improvement and measure the impact.
B) Skipping input validation and assuming “happy path”.
C) Includes a short README section describing assumptions and tradeoffs.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 6: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Implement a small feature tied to this module in an existing starter app.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 7: Which common mistake matches this scenario: tests assert implementation details instead of outcomes?
A) Write tests that prove correctness and prevent regressions.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 8: Which outcome best captures the practical ability you should carry forward?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 9: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Uses consistent style/formatting and passes the quality gate.
B) Use tooling to keep quality high: rustfmt + clippy.
C) Add or update documentation (README notes or ADR-style notes).
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 10: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
A) Deliverable runs locally with clear instructions.
B) Skipping input validation and assuming “happy path”.
C) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
