# Java Advanced — Module 07: Observability and SLOs Quiz Answers

## Question 1: An SLI is…
**Answer: B** — A quantitative measure of user-visible reliability (e.g., success rate)

**Outcome 1:** Define SLIs/SLOs and manage error budgets for a service.

**Explanation:** SLIs measure experience; SLOs set targets on those measures.

---

## Question 2: An error budget is…
**Answer: B** — Allowed unreliability derived from the SLO before you must slow feature work

**Outcome 1:** Define SLIs/SLOs and manage error budgets for a service.

**Explanation:** Budgets balance velocity vs reliability.

---

## Question 3: RED metrics stand for…
**Answer: B** — Rate, Errors, Duration

**Outcome 2:** Apply RED/USE metrics while avoiding high-cardinality label explosions.

**Explanation:** RED is a common request-centric metric set.

---

## Question 4: High-cardinality labels (user_id on every metric) typically cause…
**Answer: B** — Metric store explosion and useless dashboards

**Outcome 2:** Apply RED/USE metrics while avoiding high-cardinality label explosions.

**Explanation:** Keep label cardinality bounded.

---

## Question 5: Trace context propagation lets you…
**Answer: A** — See one request across service spans

**Outcome 3:** Propagate trace context across services to diagnose latency.

**Explanation:** Propagation stitches spans into one distributed trace.

---

## Question 6: A span without parent linkage in a deep call chain usually means…
**Answer: B** — Broken context propagation at a boundary

**Outcome 3:** Propagate trace context across services to diagnose latency.

**Explanation:** Missing parents break end-to-end latency diagnosis.

---

## Question 7: A good alert is…
**Answer: B** — Tied to user impact / SLO burn and actionable for humans

**Outcome 4:** Design alerts that are actionable and kind to on-call.

**Explanation:** Alert on symptoms that need human action.

---

## Question 8: Pager fatigue usually comes from…
**Answer: B** — Noisy, non-actionable alerts that train people to ignore pages

**Outcome 4:** Design alerts that are actionable and kind to on-call.

**Explanation:** Hygiene: fewer, better alerts.

---

## Question 9: Burning the error budget quickly should trigger…
**Answer: B** — Prioritizing reliability fixes over risky feature launches

**Outcome 1:** Define SLIs/SLOs and manage error budgets for a service.

**Explanation:** Budgets are decision tools, not vanity charts.

---

## Question 10: USE metrics focus on…
**Answer: A** — Utilization, Saturation, Errors for resources

**Outcome 2:** Apply RED/USE metrics while avoiding high-cardinality label explosions.

**Explanation:** USE complements RED for resource-centric views.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
