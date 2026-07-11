# Go Intermediate — Module 05: Databases Quiz Answers

## Question 1: Which testing requirement should you apply given this issue: database tests are polluting shared data?
**Answer: C** - If the module involves a database, tests must run against an isolated schema/database.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 2: Which common mistake matches this scenario: bugs appear on unexpected inputs because validation was skipped?
**Answer: D** - Skipping input validation and assuming “happy path”.

**Explanation:** This is listed in the Common Mistakes section to avoid.

---

## Question 3: A reviewer denies approval due to one missing item. Which acceptance criterion is it?
**Answer: A** - Uses consistent style/formatting and passes the quality gate.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## Question 4: The work passes Core. Which improvement most clearly raises quality for reviewers?
**Answer: A** - Add an integration test that hits a real boundary (HTTP, database, file system, or process).

**Explanation:** This is explicitly listed in the Better exercises section.

---

## Question 5: Before shipping, which Core action best reduces regression risk?
**Answer: B** - Add at least 3 focused unit tests that cover normal cases and edge cases.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 6: In a real code review, which outcome best reflects the skill you should demonstrate?
**Answer: C** - Write tests that prove correctness and prevent regressions.

**Explanation:** This statement appears in the Learning Outcomes section.

---

## Question 7: A teammate asks how to make the change safe to merge. Which Core action is non-negotiable?
**Answer: B** - Implement a small feature tied to this module in an existing starter app.

**Explanation:** This action is listed under the Core exercises for the module.

---

## Question 8: Your tests are blocked by tests are flaky and fail intermittently. Which requirement should you enforce?
**Answer: A** - Tests must be deterministic (no flakes) and runnable by a reviewer.

**Explanation:** This requirement appears in the Testing Requirements section.

---

## Question 9: You have extra time to go beyond expectations. Which Beast Mode action best shows senior-level rigor?
**Answer: B** - Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).

**Explanation:** This action is part of the Beast Mode upgrades.

---

## Question 10: Before sign-off, which acceptance criterion must be confirmed?
**Answer: A** - Includes a short README section describing assumptions and tradeoffs.

**Explanation:** This requirement appears in the mini-project acceptance criteria.

---

## 🎯 How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9/10 correct:** Good work! Review the missed concepts.
- **0-7/10 correct:** Review the module and try again.
