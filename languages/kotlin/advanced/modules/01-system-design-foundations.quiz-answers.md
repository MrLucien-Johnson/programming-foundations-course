# Kotlin Advanced — Module 01: System Design Foundations Quiz Answers

## Question 1: Which testing requirement is most relevant to this issue: database tests are polluting shared data?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: D** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 3: Your project passes review only if which condition is true?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: Which requirement belongs in the testing checklist for this module?
**Answer: A** - All work must be covered by build + tests + static analysis in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
**Answer: D** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: Which action pushes the work into Beast Mode?
**Answer: A** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 7: Which task best matches the Core expectations for this module?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 8: Which step would keep the work within the Core scope?
**Answer: C** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which acceptance criterion must be satisfied before submission?
**Answer: B** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: Which improvement moves a Core submission to the Better tier?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
