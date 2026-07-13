# SQL (PostgreSQL) Intermediate — Module 05: Databases Quiz Answers

## Question 1: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 3: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: C** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: Before sign-off, which acceptance criterion must be confirmed?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
**Answer: C** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: This happened during review: CI has no automated test run before release. Which mistake is it?
**Answer: A** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: C** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: Which outcome best captures the practical ability you should carry forward?
**Answer: B** - Apply the concepts to a realistic codebase (not just toy examples).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 9: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: C** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
