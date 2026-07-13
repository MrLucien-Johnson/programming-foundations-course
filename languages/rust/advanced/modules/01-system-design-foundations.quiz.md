# Rust Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Document decisions and constraints clearly for reviewers.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 2: Which acceptance requirement most clearly blocks approval if missing?
A) Explain the core concepts and tradeoffs for System Design Foundations.
B) Includes a short README section describing assumptions and tradeoffs.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 3: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
A) Add a performance or reliability improvement and measure the impact.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Making performance claims without measurements.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 4: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Includes tests appropriate for the feature.
B) Making performance claims without measurements.
C) Write tests that prove correctness and prevent regressions.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 5: Before shipping, which Core action best reduces regression risk?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Add or update documentation (README notes or ADR-style notes).
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 6: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Making performance claims without measurements.
B) Create a short write-up: what changed, why, and how you verified it.
C) Deliverable runs locally with clear instructions.
D) Tests must be deterministic (no flakes) and runnable by a reviewer.

**Your answer:** _______________

---

### Question 7: Which acceptance criterion would a reviewer check first to approve the submission?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Use tooling to keep quality high: rustfmt + clippy.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 8: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
A) Shipping without an automated test run in CI.
B) Write tests that prove correctness and prevent regressions.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 9: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
A) Includes tests appropriate for the feature.
B) Shipping without an automated test run in CI.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 10: Which outcome best captures the practical ability you should carry forward?
A) Write tests that prove correctness and prevent regressions.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) All work must be covered by fmt + clippy + tests in CI.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
