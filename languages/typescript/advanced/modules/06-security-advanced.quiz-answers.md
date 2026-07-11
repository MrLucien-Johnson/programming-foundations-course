# TypeScript Advanced — Module 06: Security (Advanced) Quiz Answers

## Question 1: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
**Answer: C** - All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: B** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 5: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: Your teammate says: tests assert implementation details instead of outcomes. Which common mistake is this?
**Answer: B** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: Before sign-off, which acceptance criterion must be confirmed?
**Answer: D** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: C** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which outcome best captures the practical ability you should carry forward?
**Answer: C** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 10: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: A** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
