# Python Advanced — Module 08: CI/CD and Release Strategies Quiz Answers

## Question 1: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: A** - Use tooling to keep quality high: ruff + black (or ruff format).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 2: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Your tests are blocked by tests are flaky and fail intermittently. Which requirement should you enforce?
**Answer: D** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: A** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 6: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
**Answer: C** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 7: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 8: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 9: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: B** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 10: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
