# Python Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: D** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 2: CI is failing because database tests are polluting shared data. Which testing requirement addresses this?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 3: A reviewer flags tests are flaky and fail intermittently. Which testing requirement resolves it?
**Answer: B** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 4: Your team wants to reduce risk quickly. Which Core action gives the biggest safety gain?
**Answer: D** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 5: A reviewer reports: bugs appear on unexpected inputs because validation was skipped. Which mistake does this reflect?
**Answer: C** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 6: Which acceptance requirement most clearly blocks approval if missing?
**Answer: D** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 7: You're pressed for time but still need a safe release. Which Core action must remain?
**Answer: B** - Add or update documentation (README notes or ADR-style notes).

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 8: Before sign-off, which acceptance criterion must be confirmed?
**Answer: D** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 9: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: A** - Create a short write-up: what changed, why, and how you verified it.

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 10: Which outcome represents a transferable software engineering skill?
**Answer: B** - Use tooling to keep quality high: ruff + black (or ruff format).

**Explanation:** This statement appears in the Learning Outcomes section.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
