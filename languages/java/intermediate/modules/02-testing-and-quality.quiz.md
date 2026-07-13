# Java Intermediate — Module 02: Testing and Quality Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Making performance claims without measurements.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 2: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
A) Create a short write-up: what changed, why, and how you verified it.
B) Includes tests appropriate for the feature.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 3: Which outcome best captures the practical ability you should carry forward?
A) Making performance claims without measurements.
B) Add or update documentation (README notes or ADR-style notes).
C) Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 4: Before sign-off, which acceptance criterion must be confirmed?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Deliverable runs locally with clear instructions.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Over-mocking (tests assert implementation details instead of outcomes).

**Your answer:** _______________

---

### Question 5: Before shipping, which Core action best reduces regression risk?
A) Implement a small feature tied to this module in an existing starter app.
B) Create a short write-up: what changed, why, and how you verified it.
C) Refactor one area for readability (without changing behavior) and prove it with tests.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 6: Which common mistake matches this scenario: tests assert implementation details instead of outcomes?
A) Write tests that prove correctness and prevent regressions.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Over-mocking (tests assert implementation details instead of outcomes).
D) All work must be covered by build + unit tests + slice/integration tests (Spring + DB) in CI.

**Your answer:** _______________

---

### Question 7: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Includes a short README section describing assumptions and tradeoffs.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Add or update documentation (README notes or ADR-style notes).
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 8: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
A) Add a performance or reliability improvement and measure the impact.
B) Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Add or update documentation (README notes or ADR-style notes).

**Your answer:** _______________

---

### Question 9: A production fix is urgent. Which Core action is still required before release?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Includes tests appropriate for the feature.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 10: Which acceptance criterion acts as a release gate for this module?
A) Shipping without an automated test run in CI.
B) If the module involves a database, tests must run against an isolated schema/database.
C) Includes tests appropriate for the feature.
D) Add at least 3 focused unit tests that cover normal cases and edge cases.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
