# Rust Advanced — Module 02: Architecture Patterns Quiz Answers

## Question 1: Which testing requirement must be satisfied before submission?
**Answer: A** - All work must be covered by fmt + clippy + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which task is explicitly listed as a Beast Mode upgrade?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 3: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Which enhancement is a Better-level upgrade (not Beast Mode)?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: Which acceptance criterion must be satisfied before submission?
**Answer: D** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: You already met Core. Which action qualifies as a Better upgrade?
**Answer: A** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 8: A reviewer approves the mini-project when which condition is met?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: This happened during review: bugs appear on unexpected inputs because validation was skipped. Which mistake is it?
**Answer: C** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 10: You're preparing a submission and need to meet the Core bar. Which action is required?
**Answer: B** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
