# AI — Module 01: System Design for LLM Apps Quiz Answers

## Question 1: An LLM feature architecture diagram should show…
**Answer: B** — Request path, model/tools/retrieval, stores, and failure/fallback paths

**Outcome 1:** Draw architecture and data flow for an LLM feature including failure modes.

**Explanation:** Design for the real runtime and its failures.

---

## Question 2: Listing failure modes early helps you…
**Answer: B** — Attach mitigations before launch

**Outcome 1:** Draw architecture and data flow for an LLM feature including failure modes.

**Explanation:** Failure modes drive resilience design.

---

## Question 3: Queues in front of expensive model calls provide…
**Answer: B** — Smoothing and backpressure under bursty load

**Outcome 2:** Plan scaling with caches, queues, and backpressure for model/tool workloads.

**Explanation:** Absorb spikes; protect downstream.

---

## Question 4: Without backpressure, a viral traffic spike tends to…
**Answer: B** — Overwhelm workers and blow cost/latency budgets

**Outcome 2:** Plan scaling with caches, queues, and backpressure for model/tool workloads.

**Explanation:** Unbounded admission is a reliability bug.

---

## Question 5: An error budget for quality SLO means…
**Answer: B** — Allowed degradation before you must prioritize reliability work

**Outcome 3:** Define latency/quality SLOs and error budgets for the feature.

**Explanation:** Budgets govern ship vs fix decisions.

---

## Question 6: Latency SLO without a quality SLO risks…
**Answer: B** — Optimizing speed while shipping junk answers

**Outcome 3:** Define latency/quality SLOs and error budgets for the feature.

**Explanation:** Measure both dimensions users care about.

---

## Question 7: Backward-compatible prompt/schema migration means…
**Answer: B** — Old and new versions coexist safely during rollout

**Outcome 4:** Design prompt/schema migrations with backward compatibility.

**Explanation:** Compatibility windows prevent cutover outages.

---

## Question 8: Changing a required JSON field name without a plan…
**Answer: B** — Breaks consumers mid-flight

**Outcome 4:** Design prompt/schema migrations with backward compatibility.

**Explanation:** Treat schema like an API.

---

## Question 9: Privacy-by-design for prompts/outputs includes…
**Answer: B** — Minimization, retention limits, and access controls

**Outcome 5:** Apply privacy-by-design (minimization, retention, access control).

**Explanation:** Collect less, keep less, restrict access.

---

## Question 10: Access controls on retrieved docs matter because…
**Answer: B** — Otherwise users can read neighbors’ private content via the model

**Outcome 5:** Apply privacy-by-design (minimization, retention, access control).

**Explanation:** Retrieval must enforce authorization.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
