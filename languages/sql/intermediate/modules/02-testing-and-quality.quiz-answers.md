# SQL (PostgreSQL) Intermediate — Module 02: Testing and Quality Quiz Answers

## Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which Better upgrade most improves maintainability or reliability?
**Answer: A** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 3: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
**Answer: D** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: A** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 5: Which outcome represents a transferable software engineering skill?
**Answer: A** - Document decisions and constraints clearly for reviewers.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 6: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 8: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Before sign-off, which acceptance criterion must be confirmed?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
