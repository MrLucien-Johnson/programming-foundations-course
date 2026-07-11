# Go Advanced — Module 03: Concurrency and Async Quiz Answers

## Question 1: Which Better upgrade most improves maintainability or reliability?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: Your teammate says: tests assert implementation details instead of outcomes. Which common mistake is this?
**Answer: A** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 3: Which Core action would a senior engineer insist on before approving the change?
**Answer: C** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: C** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: C** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 7: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: C** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
**Answer: A** - All work must be covered by gofmt + lint + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 9: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: C** - Explain the core concepts and tradeoffs for Concurrency and Async.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
