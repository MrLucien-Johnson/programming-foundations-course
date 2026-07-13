# Rust Intermediate — Module 06: Security Basics Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Before shipping, which Core action best reduces regression risk?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) All work must be covered by fmt + clippy + tests in CI.
C) Use tooling to keep quality high: rustfmt + clippy.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 2: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Skipping input validation and assuming “happy path”.
C) Making performance claims without measurements.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 4: Which Core action would a senior engineer insist on before approving the change?
A) Document decisions and constraints clearly for reviewers.
B) Shipping without an automated test run in CI.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 5: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) All work must be covered by fmt + clippy + tests in CI.
B) Skipping input validation and assuming “happy path”.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Create a short write-up: what changed, why, and how you verified it.

**Your answer:** _______________

---

### Question 6: Which outcome represents a transferable software engineering skill?
A) Making performance claims without measurements.
B) Explain the core concepts and tradeoffs for Security Basics.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) All work must be covered by fmt + clippy + tests in CI.

**Your answer:** _______________

---

### Question 7: Which testing requirement would you verify in CI before approving the change?
A) All work must be covered by fmt + clippy + tests in CI.
B) Document decisions and constraints clearly for reviewers.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 8: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
A) Skipping input validation and assuming “happy path”.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 9: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
A) Deliverable runs locally with clear instructions.
B) Explain the core concepts and tradeoffs for Security Basics.
C) All work must be covered by fmt + clippy + tests in CI.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 10: Which acceptance criterion acts as a release gate for this module?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Uses consistent style/formatting and passes the quality gate.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
