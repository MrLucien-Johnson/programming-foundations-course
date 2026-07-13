# Java Intermediate — Module 02: Testing and Quality Quiz Answers

## Question 1: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
**Answer: C** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Which outcome best captures the practical ability you should carry forward?
**Answer: C** - Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 4: Before sign-off, which acceptance criterion must be confirmed?
**Answer: B** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: Before shipping, which Core action best reduces regression risk?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: Which common mistake matches this scenario: tests assert implementation details instead of outcomes?
**Answer: C** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: A** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 9: A production fix is urgent. Which Core action is still required before release?
**Answer: A** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: Which acceptance criterion acts as a release gate for this module?
**Answer: C** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
