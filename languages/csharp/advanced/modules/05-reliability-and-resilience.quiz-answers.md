# C# Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: C** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: C** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: This happened during review: a performance claim was made without benchmarks. Which mistake is it?
**Answer: D** - Making performance claims without measurements.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: Which option represents a Beast Mode enhancement?
**Answer: C** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: Which acceptance criterion must be satisfied before submission?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: To earn a Better evaluation, which action should you add?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 10: Which item is explicitly required in the acceptance criteria?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
