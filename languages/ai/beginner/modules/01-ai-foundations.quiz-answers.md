# AI — Module 01: AI Foundations Quiz Answers

## Question 1: A stakeholder says “summarize tickets better.” First deliverable?
**Answer: B** — A clear goal, constraints, and success criteria

**Outcome 1:** Translate a vague request into goal, constraints, and success criteria.

**Explanation:** Vague asks become buildable only after goals and success criteria.

---

## Question 2: Success criteria should be…
**Answer: B** — Observable checks you can score on examples

**Outcome 1:** Translate a vague request into goal, constraints, and success criteria.

**Explanation:** If you cannot score it, you cannot iterate.

---

## Question 3: A solid task spec includes…
**Answer: B** — Inputs, outputs, constraints, and do-not-do / failure modes

**Outcome 2:** Write a one-page task spec with inputs, outputs, and failure modes.

**Explanation:** Specs make prompts repeatable across people and runs.

---

## Question 4: Why list failure modes in the spec?
**Answer: B** — So the system has planned behavior for empty/ambiguous/sensitive input

**Outcome 2:** Write a one-page task spec with inputs, outputs, and failure modes.

**Explanation:** Failure modes drive fallbacks and tests.

---

## Question 5: An eval set should include…
**Answer: B** — Good, bad, and ambiguous cases

**Outcome 3:** Build a small eval set covering good, bad, and ambiguous cases.

**Explanation:** Coverage of messiness finds regressions early.

---

## Question 6: Why keep a fixed eval set across iterations?
**Answer: A** — So scores are comparable over time

**Outcome 3:** Build a small eval set covering good, bad, and ambiguous cases.

**Explanation:** Comparable runs prove whether a change helped.

---

## Question 7: A grounding rule (“only use provided text”) mainly reduces…
**Answer: B** — Invented facts not in the source

**Outcome 4:** Add grounding/fallback rules and measure their effect on failures.

**Explanation:** Grounding targets hallucination against the given context.

---

## Question 8: Low-quality input with missing fields — good fallback?
**Answer: B** — Ask a clarifying question or return insufficient-info

**Outcome 4:** Add grounding/fallback rules and measure their effect on failures.

**Explanation:** Fallbacks beat confident fabrication.

---

## Question 9: An iteration log should record…
**Answer: B** — What changed, scores, and what improved/worsened

**Outcome 5:** Version prompt/spec changes with an iteration log.

**Explanation:** Versioned notes make improvements explainable.

---

## Question 10: Changing prompt, temperature, and examples all at once is bad because…
**Answer: B** — You cannot tell which change caused the score delta

**Outcome 5:** Version prompt/spec changes with an iteration log.

**Explanation:** Isolate variables when iterating.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
