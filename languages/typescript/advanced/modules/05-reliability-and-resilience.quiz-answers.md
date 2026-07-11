# TypeScript Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A reviewer approves the mini-project when which condition is met?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: You already met Core. Which action qualifies as a Better upgrade?
**Answer: C** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
**Answer: A** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: Which action qualifies as a Beast Mode stretch?
**Answer: D** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 7: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: C** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: Which testing requirement should you apply given this issue: tests are flaky and fail intermittently?
**Answer: B** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 9: Which requirement is part of the mini-project acceptance criteria?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: A reviewer checks the Core checklist. Which action should they see?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
