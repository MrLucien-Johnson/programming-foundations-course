# SQL (PostgreSQL) Intermediate — Module 04: APIs and Auth Quiz Answers

## Question 1: Which acceptance requirement protects review quality if enforced?
**Answer: C** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 2: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 3: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: D** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: A production fix is urgent. Which Core action is still required before release?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 5: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
**Answer: D** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 6: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 7: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
**Answer: C** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 8: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: C** - Use tooling to keep quality high: sqlfluff (lint + fix) + consistent naming conventions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 10: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
