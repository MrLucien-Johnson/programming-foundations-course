# TypeScript Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: Your tests are blocked because database tests are polluting shared data. Which requirement should you enforce?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: B** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: C** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 5: Which outcome best captures the practical ability you should carry forward?
**Answer: A** - Explain the core concepts and tradeoffs for Reliability and Resilience.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 6: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: D** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: A reviewer asks for stronger engineering discipline. Which Better action fits?
**Answer: A** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 9: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 10: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
