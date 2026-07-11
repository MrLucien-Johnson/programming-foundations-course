# SQL (PostgreSQL) Intermediate — Module 07: Debugging and Performance Quiz Answers

## Question 1: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
**Answer: C** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 3: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: Which outcome best captures the practical ability you should carry forward?
**Answer: C** - Document decisions and constraints clearly for reviewers.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 5: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 6: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: C** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
**Answer: A** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 9: Which Core action would a senior engineer insist on before approving the change?
**Answer: C** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: A** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
