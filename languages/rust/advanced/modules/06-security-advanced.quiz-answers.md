# Rust Advanced — Module 06: Security (Advanced) Quiz Answers

## Question 1: A reviewer reports: tests assert implementation details instead of outcomes. Which mistake does this reflect?
**Answer: A** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 2: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
**Answer: C** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: You already met Core. Which action qualifies as a Better upgrade?
**Answer: A** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 4: Which acceptance criterion must be satisfied before submission?
**Answer: D** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: A reviewer approves the mini-project when which condition is met?
**Answer: D** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 6: A reviewer checks the Core checklist. Which action should they see?
**Answer: A** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 8: Which step is explicitly called out as Better work?
**Answer: A** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 9: Which action pushes the work into Beast Mode?
**Answer: D** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 10: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: A** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
