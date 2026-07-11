# Rust Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
**Answer: D** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 5: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: D** - Apply the concepts to a realistic codebase (not just toy examples).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 6: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
**Answer: C** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: Before sign-off, which acceptance criterion must be confirmed?
**Answer: C** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Which Core action best reflects professional engineering practice in this situation?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
**Answer: D** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
