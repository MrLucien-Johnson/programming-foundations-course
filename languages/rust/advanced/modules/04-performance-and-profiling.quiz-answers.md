# Rust Advanced — Module 04: Performance and Profiling Quiz Answers

## Question 1: Which acceptance requirement protects review quality if enforced?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 2: Which testing requirement would prevent a reviewer from rejecting the submission?
**Answer: B** - All work must be covered by fmt + clippy + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: C** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: C** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: Which testing requirement should you apply given this issue: database tests are polluting shared data?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 7: Which Core action best reflects professional engineering practice in this situation?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 8: Which outcome best captures the practical ability you should carry forward?
**Answer: C** - Explain the core concepts and tradeoffs for Performance and Profiling.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 9: Which Core action would a senior engineer insist on before approving the change?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
