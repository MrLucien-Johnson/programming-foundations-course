# AI — Module 03: Evals at Scale Quiz Answers

## Question 1: A scalable eval runner should log…
**Answer: B** — Dataset, prompt, scorer versions plus budgets/retries

**Outcome 1:** Design batch eval runners with retries, budgets, and reproducibility.

**Explanation:** Reproducibility at scale needs provenance.

---

## Question 2: Batching evals primarily helps…
**Answer: B** — Throughput and cost control for large sets

**Outcome 1:** Design batch eval runners with retries, budgets, and reproducibility.

**Explanation:** Scale the mechanics, not just the set size.

---

## Question 3: Stratified sampling matters because…
**Answer: B** — Overall averages can hide regressions in a segment

**Outcome 2:** Detect quality drift with stratified sampling and cadence.

**Explanation:** Segments reveal localized failures.

---

## Question 4: A drift metric without a cadence is weak because…
**Answer: B** — You will not notice slow quality decay in time

**Outcome 2:** Detect quality drift with stratified sampling and cadence.

**Explanation:** Schedule the checks.

---

## Question 5: Stop-the-line criteria should be…
**Answer: B** — Predeclared thresholds that halt releases

**Outcome 3:** Define stop-the-line criteria for regressions.

**Explanation:** Gates need prior agreement.

---

## Question 6: A sudden schema-validity collapse should…
**Answer: B** — Trip stop-the-line and rollback/investigate

**Outcome 3:** Define stop-the-line criteria for regressions.

**Explanation:** Hard quality cliffs are release blockers.

---

## Question 7: Shadow eval on live traffic must be…
**Answer: B** — Privacy-safe (minimize/redact) and non-user-impacting

**Outcome 4:** Run privacy-safe shadow evaluation on live traffic.

**Explanation:** Observe without exposing users or PII.

---

## Question 8: Shadow scoring a new prompt helps you…
**Answer: B** — Estimate live impact before progressive delivery

**Outcome 4:** Run privacy-safe shadow evaluation on live traffic.

**Explanation:** Bridge offline and online confidence.

---

## Question 9: Rater calibration reduces…
**Answer: B** — Inconsistent human scores that muddy drift signals

**Outcome 5:** Operate human labeling with calibration across raters.

**Explanation:** Humans need shared standards.

---

## Question 10: A labeling workflow should include…
**Answer: B** — Guidelines, examples, and periodic agreement checks

**Outcome 5:** Operate human labeling with calibration across raters.

**Explanation:** Process quality → label quality.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
