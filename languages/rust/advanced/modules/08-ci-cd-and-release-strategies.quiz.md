# Rust Advanced — Module 08: CI/CD and Release Strategies Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Create a short write-up: what changed, why, and how you verified it.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 2: Which acceptance criterion acts as a release gate for this module?
A) All work must be covered by fmt + clippy + tests in CI.
B) Uses consistent style/formatting and passes the quality gate.
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Use tooling to keep quality high: rustfmt + clippy.

**Your answer:** _______________

---

### Question 3: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Implement a small feature tied to this module in an existing starter app.
C) Includes a short README section describing assumptions and tradeoffs.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 4: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Document decisions and constraints clearly for reviewers.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 5: Which outcome best captures the practical ability you should carry forward?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 6: You're pressed for time but still need a safe release. Which Core action must remain?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Implement a small feature tied to this module in an existing starter app.
C) Shipping without an automated test run in CI.
D) Apply the concepts to a realistic codebase (not just toy examples).

**Your answer:** _______________

---

### Question 7: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Add or update documentation (README notes or ADR-style notes).
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Uses consistent style/formatting and passes the quality gate.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 8: Which testing requirement should be verified in CI for this module?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) All work must be covered by fmt + clippy + tests in CI.
C) Implement a small feature tied to this module in an existing starter app.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 9: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Document decisions and constraints clearly for reviewers.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Includes tests appropriate for the feature.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

### Question 10: Which acceptance requirement most clearly blocks approval if missing?
A) Add a performance or reliability improvement and measure the impact.
B) Includes tests appropriate for the feature.
C) Explain the core concepts and tradeoffs for CI/CD and Release Strategies.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
