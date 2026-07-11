# Rust Advanced — Module 01: System Design Foundations Quiz Answers

## Question 1: Which Better upgrade most improves maintainability or reliability?
**Answer: B** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: Which acceptance requirement most clearly blocks approval if missing?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: Production validation failed because database tests are polluting shared data. Which testing requirement would have prevented it?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Which testing requirement is most relevant to this issue: tests are flaky and fail intermittently?
**Answer: D** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: Before shipping, which Core action best reduces regression risk?
**Answer: C** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: B** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 7: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: D** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
**Answer: B** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 10: Which outcome best captures the practical ability you should carry forward?
**Answer: A** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
