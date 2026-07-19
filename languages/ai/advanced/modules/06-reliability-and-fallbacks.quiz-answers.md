# AI — Module 06: Reliability and Fallbacks Quiz Answers

## Question 1: Model-down fallback might be…
**Answer: B** — Cached answer, smaller model, or human handoff

**Outcome 1:** Define fallbacks per top failure mode (model, retrieval, tools).

**Explanation:** Degrade explicitly per mode.

---

## Question 2: Empty retrieval fallback should…
**Answer: B** — Abstain/ask rather than fabricate

**Outcome 1:** Define fallbacks per top failure mode (model, retrieval, tools).

**Explanation:** No evidence → no invented answer.

---

## Question 3: Retry budgets on tool errors prevent…
**Answer: B** — Unbounded cost and delayed failure signals

**Outcome 2:** Set retry budgets and stop conditions for degraded paths.

**Explanation:** Bound recovery attempts.

---

## Question 4: Stop conditions in degraded mode…
**Answer: B** — Ensure the system does not thrash forever

**Outcome 2:** Set retry budgets and stop conditions for degraded paths.

**Explanation:** Know when to quit.

---

## Question 5: Failure injection in harnesses proves…
**Answer: B** — Fallbacks actually trigger and behave safely

**Outcome 3:** Failure-inject outages/timeouts in the harness.

**Explanation:** Test the dark paths.

---

## Question 6: Simulating timeouts without assertions…
**Answer: B** — Misses whether fallbacks ran correctly

**Outcome 3:** Failure-inject outages/timeouts in the harness.

**Explanation:** Inject and assert.

---

## Question 7: Human-in-the-loop queues need…
**Answer: B** — Clear routing, SLA, and escalation

**Outcome 4:** Specify degraded modes: abstain, ask, cached answer, human queue.

**Explanation:** Humans are a capacity-limited dependency.

---

## Question 8: Cached answers as degraded mode require…
**Answer: B** — Freshness/validity rules so wrong cache is not “reliability”

**Outcome 4:** Specify degraded modes: abstain, ask, cached answer, human queue.

**Explanation:** Stale cache can be worse than abstain.

---

## Question 9: Post-incident reviews should update…
**Answer: B** — Evals, guardrails, and runbooks to prevent repeats

**Outcome 5:** Run post-incident reviews that harden evals and guardrails.

**Explanation:** Convert pain into controls.

---

## Question 10: A fallback strategy tied to SLOs means…
**Answer: B** — You know when degraded mode is acceptable vs stop-the-line

**Outcome 5:** Run post-incident reviews that harden evals and guardrails.

**Explanation:** Budgets frame degradation choices.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
