# C# Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: A reviewer says, 'Good start.' Which Better upgrade should you add next?
**Answer: A** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: Which outcome best captures the practical ability you should carry forward?
**Answer: A** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 3: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: D** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 4: Which acceptance criterion acts as a release gate for this module?
**Answer: A** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
**Answer: B** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 7: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: C** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: Before shipping, which Core action best reduces regression risk?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 10: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
