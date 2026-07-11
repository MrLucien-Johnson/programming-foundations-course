# Rust Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: B** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 2: A reviewer says, 'Good start.' Which Better upgrade should you add next?
**Answer: C** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 3: Which testing requirement would prevent a reviewer from rejecting the submission?
**Answer: C** - All work must be covered by fmt + clippy + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Which outcome represents a transferable software engineering skill?
**Answer: D** - Use tooling to keep quality high: rustfmt + clippy.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 5: Your tests are blocked because database tests are polluting shared data. Which requirement should you enforce?
**Answer: A** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: A reviewer reports: CI has no automated test run before release. Which mistake does this reflect?
**Answer: D** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 8: Before sign-off, which acceptance criterion must be confirmed?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Which Core action best reflects professional engineering practice in this situation?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 10: A PR introduces new behavior. Which Core action is the minimum expected before review?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
