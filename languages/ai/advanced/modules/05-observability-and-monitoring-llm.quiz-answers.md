# AI — Module 05: Observability and Monitoring for LLM Apps Quiz Answers

## Question 1: LLM SLIs often include…
**Answer: B** — Success/groundedness proxies, safety hits, latency, cost

**Outcome 1:** Define SLIs/SLOs for quality, safety, cost, and latency.

**Explanation:** User-visible and operational signals together.

---

## Question 2: Mapping SLOs to metrics ensures…
**Answer: B** — Error budgets and alerts attach to real targets

**Outcome 1:** Define SLIs/SLOs for quality, safety, cost, and latency.

**Explanation:** SLOs without metrics are slogans.

---

## Question 3: Alert thresholds should be…
**Answer: B** — Tied to user impact / budget burn and actionable

**Outcome 2:** Design dashboards and alert thresholds operators can act on.

**Explanation:** Hygiene beats noise.

---

## Question 4: A dashboard without owners…
**Answer: B** — Tends to rot; assign responders per signal

**Outcome 2:** Design dashboards and alert thresholds operators can act on.

**Explanation:** Observability needs operational ownership.

---

## Question 5: Tracing retrieval → generation → tools shows…
**Answer: B** — Where latency and failures occur in the LLM pipeline

**Outcome 3:** Trace multi-step LLM flows (retrieval, generation, tools).

**Explanation:** Spans localize bottlenecks.

---

## Question 6: Missing trace context between retrieval and generation…
**Answer: B** — Breaks end-to-end latency diagnosis

**Outcome 3:** Trace multi-step LLM flows (retrieval, generation, tools).

**Explanation:** Propagate context across steps.

---

## Question 7: Privacy-safe quality sampling means…
**Answer: B** — Redacting/minimizing content while still scoring subsets

**Outcome 4:** Sample quality safely (privacy-preserving) with escalation paths.

**Explanation:** Learn quality without leaking.

---

## Question 8: Escalation for quality drop should be documented so…
**Answer: B** — Responders know when to flag/rollback/page specialists

**Outcome 4:** Sample quality safely (privacy-preserving) with escalation paths.

**Explanation:** Playbooks attach to signals.

---

## Question 9: Continuous canary eval…
**Answer: B** — Detects live regressions early on a small cohort

**Outcome 5:** Run continuous canary evaluation in production.

**Explanation:** Always-on progressive checking.

---

## Question 10: Monitoring must verify fallbacks because…
**Answer: B** — Broken fallbacks can silently degrade UX or safety

**Outcome 5:** Run continuous canary evaluation in production.

**Explanation:** Watch the safety nets too.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
