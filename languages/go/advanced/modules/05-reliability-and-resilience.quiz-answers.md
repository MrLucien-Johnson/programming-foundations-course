# Go Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 2: Production validation failed because lint/format/type errors are breaking CI. Which testing requirement would have prevented it?
**Answer: B** - All work must be covered by gofmt + lint + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: Which Better upgrade most improves maintainability or reliability?
**Answer: D** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 4: Which acceptance requirement most clearly blocks approval if missing?
**Answer: A** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: Which Beast Mode action most clearly demonstrates advanced engineering judgment?
**Answer: C** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 6: A hiring manager asks what you can now do confidently. Which outcome fits?
**Answer: B** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 7: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 8: A production fix is urgent. Which Core action is still required before release?
**Answer: B** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 9: Which acceptance requirement protects review quality if enforced?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: Which Core action best reflects professional engineering practice in this situation?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
