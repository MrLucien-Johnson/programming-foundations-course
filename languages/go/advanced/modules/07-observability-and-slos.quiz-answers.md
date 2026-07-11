# Go Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: To earn a Better evaluation, which action should you add?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
**Answer: C** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 4: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: A reviewer checks the Core checklist. Which action should they see?
**Answer: A** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: Which acceptance criterion must be satisfied before submission?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: Which task is explicitly listed as a Beast Mode upgrade?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: Which item is explicitly required in the acceptance criteria?
**Answer: D** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Which improvement moves a Core submission to the Better tier?
**Answer: B** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 10: Which task best matches the Core expectations for this module?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
