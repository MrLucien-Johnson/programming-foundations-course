# Go Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: A** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 2: Your tests are blocked by lint/format/type errors are breaking CI. Which requirement should you enforce?
**Answer: C** - All work must be covered by gofmt + lint + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Your project passes review only if which condition is true?
**Answer: C** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: Which acceptance criterion must be satisfied before submission?
**Answer: D** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
**Answer: D** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: Which action qualifies as a Beast Mode stretch?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 7: To earn a Better evaluation, which action should you add?
**Answer: C** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 9: A reviewer checks the Core checklist. Which action should they see?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
