# Python Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## 📝 Instructions

Answer these questions about what you learned. Try to answer from memory first!

## 🧪 Questions

### Question 1: The work passes Core. Which improvement most clearly raises quality for reviewers?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Shipping without an automated test run in CI.
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Your answer:** _______________

---

### Question 2: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
B) Add at least 3 focused unit tests that cover normal cases and edge cases.
C) If the module involves a database, tests must run against an isolated schema/database.
D) Document decisions and constraints clearly for reviewers.

**Your answer:** _______________

---

### Question 3: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
A) Create a short write-up: what changed, why, and how you verified it.
B) Tests must be deterministic (no flakes) and runnable by a reviewer.
C) Add at least 3 focused unit tests that cover normal cases and edge cases.
D) Making performance claims without measurements.

**Your answer:** _______________

---

### Question 4: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
A) Refactor one area for readability (without changing behavior) and prove it with tests.
B) Shipping without an automated test run in CI.
C) Write tests that prove correctness and prevent regressions.
D) Implement a small feature tied to this module in an existing starter app.

**Your answer:** _______________

---

### Question 5: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
A) Create a short write-up: what changed, why, and how you verified it.
B) Refactor one area for readability (without changing behavior) and prove it with tests.
C) Skipping input validation and assuming “happy path”.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 6: Which acceptance requirement most clearly blocks approval if missing?
A) Shipping without an automated test run in CI.
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).
C) Making performance claims without measurements.
D) Includes a short README section describing assumptions and tradeoffs.

**Your answer:** _______________

---

### Question 7: You're pressed for time but still need a safe release. Which Core action must remain?
A) Shipping without an automated test run in CI.
B) Add or update documentation (README notes or ADR-style notes).
C) Deliverable runs locally with clear instructions.
D) Refactor one area for readability (without changing behavior) and prove it with tests.

**Your answer:** _______________

---

### Question 8: Before sign-off, which acceptance criterion must be confirmed?
A) Shipping without an automated test run in CI.
B) Use tooling to keep quality high: ruff + black (or ruff format).
C) Apply the concepts to a realistic codebase (not just toy examples).
D) Uses consistent style/formatting and passes the quality gate.

**Your answer:** _______________

---

### Question 9: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
A) Create a short write-up: what changed, why, and how you verified it.
B) Includes a short README section describing assumptions and tradeoffs.
C) Includes tests appropriate for the feature.
D) Use tooling to keep quality high: ruff + black (or ruff format).

**Your answer:** _______________

---

### Question 10: Which outcome represents a transferable software engineering skill?
A) If the module involves a database, tests must run against an isolated schema/database.
B) Use tooling to keep quality high: ruff + black (or ruff format).
C) Includes a short README section describing assumptions and tradeoffs.
D) Includes tests appropriate for the feature.

**Your answer:** _______________

---

## ✅ Check Your Answers

Once you finish, check the answers file for explanations.

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You understand the module well. 🎉
- **8-9/10 correct:** Great work! Review the ones you missed.
- **0-7/10 correct:** Review the module and try again. 💪
