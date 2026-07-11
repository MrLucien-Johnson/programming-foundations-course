# TypeScript Advanced — Module 01: System Design Foundations Quiz Answers

## Question 1: Which acceptance criterion must be satisfied before submission?
**Answer: C** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 2: Your tests are blocked by lint/format/type errors are breaking CI. Which requirement should you enforce?
**Answer: B** - All work must be covered by typecheck + lint + unit tests + integration tests (HTTP + DB) in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Which step would keep the work within the Core scope?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 5: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
**Answer: C** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: You already met Core. Which action qualifies as a Better upgrade?
**Answer: B** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 7: Which improvement moves a Core submission to the Better tier?
**Answer: C** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which action pushes the work into Beast Mode?
**Answer: D** - Add a performance or reliability improvement and measure the impact.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 10: Which item is explicitly required in the acceptance criteria?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
