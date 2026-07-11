# SQL (PostgreSQL) Intermediate — Module 08: Deployment and CI Quiz Answers

## Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: D** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A reviewer checks the Core checklist. Which action should they see?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 3: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: D** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: Which option is listed under Better work for this module?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 6: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
**Answer: B** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 7: Which option represents a Beast Mode enhancement?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 8: Your project passes review only if which condition is true?
**Answer: C** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: This happened during review: CI has no automated test run before release. Which mistake is it?
**Answer: C** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 10: Which acceptance criterion must be satisfied before submission?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
