# Java Advanced — Module 01: System Design Foundations Quiz Answers

## Question 1: Which Better action best demonstrates stronger engineering discipline?
**Answer: C** - Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: If you wanted to stretch the module into production readiness, which Beast Mode action fits?
**Answer: B** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 3: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 4: Production validation failed because feature tests fail when hitting real boundaries. Which testing requirement would have prevented it?
**Answer: D** - All work must be covered by build + unit tests + slice/integration tests (Spring + DB) in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 5: CI is failing because tests are flaky and fail intermittently. Which testing requirement addresses this?
**Answer: C** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 6: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: Before sign-off, which acceptance criterion must be confirmed?
**Answer: B** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 8: Which acceptance criterion acts as a release gate for this module?
**Answer: B** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: D** - Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 10: This happened during review: tests assert implementation details instead of outcomes. Which mistake is it?
**Answer: D** - Over-mocking (tests assert implementation details instead of outcomes).

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
