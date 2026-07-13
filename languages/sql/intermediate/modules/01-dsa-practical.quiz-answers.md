# SQL (PostgreSQL) Intermediate — Module 01: DSA (Practical) Quiz Answers

## Question 1: Production validation failed because tests are flaky and fail intermittently. Which testing requirement would have prevented it?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
**Answer: A** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 3: Which acceptance criterion acts as a release gate for this module?
**Answer: C** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: A production fix is urgent. Which Core action is still required before release?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: Which outcome best captures the practical ability you should carry forward?
**Answer: D** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 7: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
**Answer: C** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: C** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Which Core action would a senior engineer insist on before approving the change?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: A reviewer says, 'Good start.' Which Better upgrade should you add next?
**Answer: B** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
