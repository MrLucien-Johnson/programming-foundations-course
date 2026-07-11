# Kotlin Advanced — Module 08: CI/CD and Release Strategies Quiz Answers

## Question 1: Your tests are blocked by database tests are polluting shared data. Which requirement should you enforce?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A hiring manager asks what you can now do confidently. Which outcome fits?
**Answer: C** - Use tooling to keep quality high: ktlint + detekt.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 3: Which requirement belongs in the testing checklist for this module?
**Answer: D** - All work must be covered by build + tests + static analysis in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 5: A reviewer says, 'Good start.' Which Better upgrade should you add next?
**Answer: B** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 6: Which Core action would a senior engineer insist on before approving the change?
**Answer: D** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: Your teammate says: CI has no automated test run before release. Which common mistake is this?
**Answer: D** - Shipping without an automated test run in CI.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 9: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 10: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: A** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
