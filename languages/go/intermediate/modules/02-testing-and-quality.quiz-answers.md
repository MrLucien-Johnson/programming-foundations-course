# Go Intermediate — Module 02: Testing and Quality Quiz Answers

## Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which common mistake matches this scenario: a performance claim was made without benchmarks?
**Answer: C** - Making performance claims without measurements.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 3: Which action pushes the work into Beast Mode?
**Answer: D** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 4: Which improvement moves a Core submission to the Better tier?
**Answer: A** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: Which testing requirement is most relevant to this issue: lint/format/type errors are breaking CI?
**Answer: A** - All work must be covered by gofmt + lint + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 7: Which requirement is part of the mini-project acceptance criteria?
**Answer: A** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which acceptance criterion must be satisfied before submission?
**Answer: D** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: A reviewer checks the Core checklist. Which action should they see?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
