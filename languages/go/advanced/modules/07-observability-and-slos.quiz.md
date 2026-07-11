# Go Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: To earn a Better evaluation, which action should you add?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Includes tests appropriate for the feature.
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 2: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
A) Uses consistent style/formatting and passes the quality gate.
B) Over-mocking (tests assert implementation details instead of outcomes).
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Skipping input validation and assuming “happy path”.

**Your answer:** _______________

---

### Question 3: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
A) Skipping input validation and assuming “happy path”.
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) Add a performance or reliability improvement and measure the impact.
D) If the module involves a database, tests must run against an isolated schema/database.

**Your answer:** _______________

---

### Question 4: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Making performance claims without measurements.
C) Use tooling to keep quality high: gofmt + golangci-lint.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

### Question 5: A reviewer checks the Core checklist. Which action should they see?
A) Add at least 3 focused unit tests that cover normal cases and edge cases.
B) Use tooling to keep quality high: gofmt + golangci-lint.
C) Tests must be deterministic (no flakes) and runnable by a reviewer.
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 6: Which acceptance criterion must be satisfied before submission?
A) Uses consistent style/formatting and passes the quality gate.
B) Skipping input validation and assuming “happy path”.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Shipping without an automated test run in CI.

**Your answer:** _______________

---

### Question 7: Which task is explicitly listed as a Beast Mode upgrade?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
B) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
C) Shipping without an automated test run in CI.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

### Question 8: Which item is explicitly required in the acceptance criteria?
A) All work must be covered by gofmt + lint + tests in CI.
B) Create a short write-up: what changed, why, and how you verified it.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Deliverable runs locally with clear instructions.

**Your answer:** _______________

---

### Question 9: Which improvement moves a Core submission to the Better tier?
A) Explain the core concepts and tradeoffs for Observability and SLOs.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) If the module involves a database, tests must run against an isolated schema/database.
D) Use tooling to keep quality high: gofmt + golangci-lint.

**Your answer:** _______________

---

### Question 10: Which task best matches the Core expectations for this module?
A) Implement a small feature tied to this module in an existing starter app.
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
C) Create a short write-up: what changed, why, and how you verified it.
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
