# SQL (PostgreSQL) Advanced — Module 03: Concurrency and Async Quiz Answers

## Question 1: A reviewer flags lint/format/type errors are breaking CI. Which testing requirement resolves it?
**Answer: B** - All work must be covered by migrations apply cleanly + pgTAP + SQL linting in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which acceptance criterion must be satisfied before submission?
**Answer: D** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 3: Which task is explicitly listed as a Beast Mode upgrade?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: A** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: A reviewer checks the Core checklist. Which action should they see?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: Your project passes review only if which condition is true?
**Answer: D** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: Your teammate says: bugs appear on unexpected inputs because validation was skipped. Which common mistake is this?
**Answer: B** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 9: Which testing requirement should you apply given this issue: database tests are polluting shared data?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 10: Which option is listed under Better work for this module?
**Answer: C** - Refactor one area for readability (without changing behavior) and prove it with tests.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
