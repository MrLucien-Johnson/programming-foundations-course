# Rust Intermediate — Module 06: Security Basics Quiz Answers

## Question 1: Before shipping, which Core action best reduces regression risk?
**Answer: D** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 2: A reviewer flags database tests are polluting shared data. Which testing requirement resolves it?
**Answer: B** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: A reviewer wants better maintainability or reliability. Which upgrade should you choose?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 4: Which Core action would a senior engineer insist on before approving the change?
**Answer: C** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 5: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: D** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 6: Which outcome represents a transferable software engineering skill?
**Answer: B** - Explain the core concepts and tradeoffs for Security Basics.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 7: Which testing requirement would you verify in CI before approving the change?
**Answer: A** - All work must be covered by fmt + clippy + tests in CI.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 8: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
**Answer: A** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 9: A reviewer is ready to approve once one missing requirement is fixed. Which requirement is it?
**Answer: A** - Deliverable runs locally with clear instructions.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 10: Which acceptance criterion acts as a release gate for this module?
**Answer: C** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
