# Python Advanced — Module 06: Security (Advanced) Quiz Answers

## Question 1: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: A** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 2: Which acceptance requirement protects review quality if enforced?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 4: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 5: Which testing requirement should you apply given this issue: lint/format/type errors are breaking CI?
**Answer: B** - All work must be covered by ruff/format + unit tests + integration tests (HTTP + DB) in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: Which acceptance requirement most clearly blocks approval if missing?
**Answer: B** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 8: This happened during review: a performance claim was made without benchmarks. Which mistake is it?
**Answer: D** - Making performance claims without measurements.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 9: A hiring manager asks what you can now do confidently. Which outcome fits?
**Answer: A** - Explain the core concepts and tradeoffs for Security (Advanced).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 10: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
