# Java Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: Which testing requirement is most relevant to this issue: feature tests fail when hitting real boundaries?
**Answer: A** - All work must be covered by build + unit tests + slice/integration tests (Spring + DB) in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: A production fix is urgent. Which Core action is still required before release?
**Answer: C** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 4: Your teammate says: a performance claim was made without benchmarks. Which common mistake is this?
**Answer: A** - Making performance claims without measurements.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 5: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: A** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 6: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: A** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 7: A hiring manager asks what you can now do confidently. Which outcome fits?
**Answer: D** - Explain the core concepts and tradeoffs for Observability and SLOs.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 8: Which acceptance criterion would a reviewer check first to approve the submission?
**Answer: A** - Includes tests appropriate for the feature.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: Which acceptance criterion acts as a release gate for this module?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
