# SQL (PostgreSQL) Intermediate — Module 08: Deployment and CI Quiz Answers

## Question 1: A reviewer asks for stronger engineering discipline. Which Better action fits?
**Answer: B** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 3: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Which outcome represents a transferable software engineering skill?
**Answer: C** - Explain the core concepts and tradeoffs for Deployment and CI.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 5: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
**Answer: D** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: B** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: Which acceptance criterion acts as a release gate for this module?
**Answer: A** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Your tests are blocked because tests are flaky and fail intermittently. Which requirement should you enforce?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 10: Which acceptance requirement protects review quality if enforced?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
