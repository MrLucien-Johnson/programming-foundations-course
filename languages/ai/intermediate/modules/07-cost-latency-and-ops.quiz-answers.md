# AI — Module 07: Cost, Latency, and Ops Quiz Answers

## Question 1: A budget without an enforcement action is…
**Answer: B** — Just a hope — define fallback when exceeded

**Outcome 1:** Set cost/latency budgets and enforce them in workflows.

**Explanation:** Budgets need tripwires and fallbacks.

---

## Question 2: When a latency budget is exceeded, a workflow might…
**Answer: B** — Fallback to a cheaper/faster path or abstain

**Outcome 1:** Set cost/latency budgets and enforce them in workflows.

**Explanation:** Degrade deliberately.

---

## Question 3: Cache keys for LLM calls should usually include…
**Answer: B** — Prompt version + normalized inputs that determine the output

**Outcome 2:** Design cache keys and reuse strategies that preserve correctness.

**Explanation:** Keys must match semantic inputs.

---

## Question 4: Caching answers without prompt version in the key risks…
**Answer: B** — Serving stale answers after a prompt change

**Outcome 2:** Design cache keys and reuse strategies that preserve correctness.

**Explanation:** Version the cache namespace.

---

## Question 5: Early exit on low confidence trades…
**Answer: B** — Some coverage for lower cost/risk of bad answers

**Outcome 3:** Add early-exit/abstain rules when confidence is low.

**Explanation:** Abstain/ask can be the cheapest correct action.

---

## Question 6: Context trimming in RAG helps latency/cost by…
**Answer: B** — Keeping only necessary retrieved evidence

**Outcome 3:** Add early-exit/abstain rules when confidence is low.

**Explanation:** Less context → less spend if relevance holds.

---

## Question 7: Ops dashboards for LLM features should show…
**Answer: B** — Quality proxies, cost, latency, and error/fallback rates

**Outcome 4:** Monitor quality, cost, and latency with actionable alerts.

**Explanation:** Triangulate quality and spend.

---

## Question 8: An alert on cost spike should be…
**Answer: B** — Actionable: check canaries, caches, runaway agents

**Outcome 4:** Monitor quality, cost, and latency with actionable alerts.

**Explanation:** Tie alerts to operator playbooks.

---

## Question 9: Prompt canaries reduce risk by…
**Answer: B** — Exposing a new prompt version to a small cohort while watching metrics

**Outcome 5:** Plan canary/rollback for prompt and model version changes.

**Explanation:** Progressive delivery for prompts.

---

## Question 10: Rollback criteria for prompt releases should be predefined so…
**Answer: B** — You revert quickly on quality/cost/safety regressions

**Outcome 5:** Plan canary/rollback for prompt and model version changes.

**Explanation:** Decide thresholds before the fire.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
