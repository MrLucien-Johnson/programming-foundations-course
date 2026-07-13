# C# Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement would prevent a reviewer from rejecting the submission?
A) All work must be covered by build + tests + analyzers in CI.
B) Includes a short README section describing assumptions and tradeoffs.
C) Shipping without an automated test run in CI.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 2: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
A) Apply the concepts to a realistic codebase (not just toy examples).
B) Skipping input validation and assuming “happy path”.
C) Includes a short README section describing assumptions and tradeoffs.
D) All work must be covered by build + tests + analyzers in CI.

**Your answer:** _______________

---

### Question 3: Which acceptance criterion acts as a release gate for this module?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Uses consistent style/formatting and passes the quality gate.
C) Skipping input validation and assuming “happy path”.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 4: Your tests are blocked because tests are flaky and fail intermittently. Which requirement should you enforce?
A) Tests must be deterministic (no flakes) and runnable by a reviewer.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 5: A reviewer says, 'Good start.' Which Better upgrade should you add next?
A) Use tooling to keep quality high: dotnet format + analyzers.
B) Add or update documentation (README notes or ADR-style notes).
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 6: Before sign-off, which acceptance criterion must be confirmed?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Skipping input validation and assuming “happy path”.
C) Includes tests appropriate for the feature.
D) Write tests that prove correctness and prevent regressions.

**Your answer:** _______________

---

### Question 7: A hiring manager asks what you can now do confidently. Which outcome fits?
A) Create a short write-up: what changed, why, and how you verified it.
B) Document decisions and constraints clearly for reviewers.
C) Skipping input validation and assuming “happy path”.
D) All work must be covered by build + tests + analyzers in CI.

**Your answer:** _______________

---

### Question 8: A production fix is urgent. Which Core action is still required before release?
A) Uses consistent style/formatting and passes the quality gate.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Implement a small feature tied to this module in an existing starter app.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 9: A PR introduces new behavior. Which Core action is the minimum expected before review?
A) Explain the core concepts and tradeoffs for Reliability and Resilience.
B) Add or update documentation (README notes or ADR-style notes).
C) Includes tests appropriate for the feature.
D) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Your answer:** _______________

---

### Question 10: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Write tests that prove correctness and prevent regressions.
B) Includes a short README section describing assumptions and tradeoffs.
C) Create a short write-up: what changed, why, and how you verified it.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
