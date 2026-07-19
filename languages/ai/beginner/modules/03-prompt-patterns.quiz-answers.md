# AI — Module 03: Prompt Patterns Quiz Answers

## Question 1: Extraction prompts should define…
**Answer: B** — Field names, types, and allowed empties

**Outcome 1:** Design extraction prompts that emit valid structured fields.

**Explanation:** Schemas make extraction evaluable.

---

## Question 2: Free text → JSON is brittle unless you…
**Answer: B** — Specify schema and validate outputs

**Outcome 1:** Design extraction prompts that emit valid structured fields.

**Explanation:** Validation closes the loop.

---

## Question 3: A required-field checklist tells the model…
**Answer: B** — Which fields must be present and what to do if absent

**Outcome 2:** Specify required-field checklists and missing-data behavior.

**Explanation:** Missing-data policy is part of the contract.

---

## Question 4: If account ID is missing, a good pattern is…
**Answer: B** — Leave null/omit per schema and flag incompleteness

**Outcome 2:** Specify required-field checklists and missing-data behavior.

**Explanation:** Explicit incomplete beats fake completeness.

---

## Question 5: A repair prompt should…
**Answer: B** — Fix invalid JSON/structure without changing meaning

**Outcome 3:** Add a review/repair pass that fixes structure without inventing facts.

**Explanation:** Repair ≠ rewrite content.

---

## Question 6: A second review pass is useful to…
**Answer: B** — Flag missing fields or contradictions before finalizing

**Outcome 3:** Add a review/repair pass that fixes structure without inventing facts.

**Explanation:** Review catches structural and consistency issues.

---

## Question 7: An error taxonomy helps iteration by…
**Answer: B** — Focusing fixes on the largest failure categories first

**Outcome 4:** Build an error taxonomy and track reductions across iterations.

**Explanation:** Categorize → prioritize → fix.

---

## Question 8: Tracking “invalid JSON” vs “wrong urgency” separately matters because…
**Answer: A** — They need different mitigations

**Outcome 4:** Build an error taxonomy and track reductions across iterations.

**Explanation:** Different failures need different prompt/tool fixes.

---

## Question 9: Few-shots for sarcasm/multiple issues help because…
**Answer: B** — They demonstrate judgment on hard cases the base rules under-specify

**Outcome 5:** Cover tricky cases with targeted few-shot examples.

**Explanation:** Hard cases need demonstrated patterns.

---

## Question 10: Measuring % valid JSON on a fixed set proves…
**Answer: B** — Structural compliance of the extraction pattern

**Outcome 1:** Design extraction prompts that emit valid structured fields.

**Explanation:** Validity rate is a core extraction metric.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
