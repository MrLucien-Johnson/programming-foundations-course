# AI — Module 02: Structured Outputs and Schemas Quiz Answers

## Question 1: A ticket schema should define…
**Answer: B** — Fields like category, summary, urgency, actions — with types

**Outcome 1:** Design schemas for task outputs with required and optional fields.

**Explanation:** Schemas encode the product contract.

---

## Question 2: Optional vs required fields matter because…
**Answer: B** — They change pass/fail and missing-data behavior

**Outcome 1:** Design schemas for task outputs with required and optional fields.

**Explanation:** Requirements drive validation.

---

## Question 3: Measuring JSON validity + required-field completeness tells you…
**Answer: B** — Structural quality of structured outputs

**Outcome 2:** Validate outputs and measure validity/completeness on a dataset.

**Explanation:** These are core structured-output metrics.

---

## Question 4: A 30-case dataset is useful to…
**Answer: B** — Estimate validity rates beyond anecdotes

**Outcome 2:** Validate outputs and measure validity/completeness on a dataset.

**Explanation:** Sample size beats one lucky example.

---

## Question 5: Repair must not…
**Answer: B** — Invent missing business facts to satisfy the schema

**Outcome 3:** Add capped repair passes that fix structure without new facts.

**Explanation:** Repair is structural, not creative.

---

## Question 6: Capping repair attempts prevents…
**Answer: B** — Unbounded cost loops on hopeless outputs

**Outcome 3:** Add capped repair passes that fix structure without new facts.

**Explanation:** Budgets apply to repair too.

---

## Question 7: Schema versioning helps when…
**Answer: B** — Producers/consumers evolve without silent breakages

**Outcome 4:** Version schemas and plan migrations for breaking changes.

**Explanation:** Versions + migrations keep contracts coherent.

---

## Question 8: A breaking field rename should include…
**Answer: B** — A migration plan and dual-read period if needed

**Outcome 4:** Version schemas and plan migrations for breaking changes.

**Explanation:** Treat schema breaks like API breaks.

---

## Question 9: Strict mode fails validation — best response?
**Answer: B** — Fallback: error, abstain, or safe partial per policy

**Outcome 5:** Fail closed with a fallback when strict validation fails.

**Explanation:** Fail closed with an explicit fallback.

---

## Question 10: Red-team “extra fields / injected instructions” tests…
**Answer: B** — Whether validators and prompts reject schema abuse

**Outcome 5:** Fail closed with a fallback when strict validation fails.

**Explanation:** Structured outputs need adversarial coverage too.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
