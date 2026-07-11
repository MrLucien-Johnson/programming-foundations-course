# SQL (PostgreSQL) Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: A** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 3: Which outcome represents a transferable software engineering skill?
**Answer: B** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 4: Before shipping, which Core action best reduces regression risk?
**Answer: A** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 5: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
**Answer: A** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 6: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
**Answer: C** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 7: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
**Answer: D** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 8: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: C** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
