# TypeScript Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: A production fix is urgent. Which Core action is still required before release?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 2: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: D** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: Which acceptance requirement protects review quality if enforced?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: Production validation failed because tests are flaky and fail intermittently. Which testing requirement would have prevented it?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: C** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 7: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 8: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: A** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: B** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 10: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
