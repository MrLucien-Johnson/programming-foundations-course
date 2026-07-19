# Swift Advanced — Module 04: Performance and Profiling Quiz Answers

## Question 1: Why capture a baseline before optimizing?
**Answer: B** — To know whether a change actually improved latency/throughput

**Outcome 1:** Establish performance baselines before changing code.

**Explanation:** Without a baseline you cannot prove improvement.

---

## Question 2: A good baseline includes…
**Answer: B** — Workload definition plus measured latency/error/resource metrics

**Outcome 1:** Establish performance baselines before changing code.

**Explanation:** Baselines need a defined load and recorded metrics.

---

## Question 3: Load testing primarily answers…
**Answer: B** — How the system behaves under target/peak concurrency and data size

**Outcome 2:** Run load tests and locate bottlenecks with evidence.

**Explanation:** Load tests reveal bottlenecks under realistic pressure.

---

## Question 4: CPU is idle but latency is high. Likely bottleneck class?
**Answer: B** — I/O waits, locks, or external dependencies

**Outcome 2:** Run load tests and locate bottlenecks with evidence.

**Explanation:** Idle CPU with high latency often means waiting on I/O or locks.

---

## Question 5: A slow filter on `user_id` with sequential scans suggests…
**Answer: B** — Adding/using an appropriate index and verifying the plan

**Outcome 3:** Tune databases using indexes, query plans, and lock analysis.

**Explanation:** Indexes + plans are the primary DB performance tools.

---

## Question 6: Lock contention shows up as…
**Answer: B** — Sessions waiting on locks held by other transactions

**Outcome 3:** Tune databases using indexes, query plans, and lock analysis.

**Explanation:** Contended locks serialize work and inflate latency.

---

## Question 7: Cache-aside with TTL mainly risks…
**Answer: A** — Serving stale data until TTL/invalidation

**Outcome 4:** Choose cache invalidation strategies that match correctness needs.

**Explanation:** TTLs trade freshness for simplicity; invalidate when correctness demands.

---

## Question 8: Write-through caching means…
**Answer: A** — Writes update cache and store together (sync path)

**Outcome 4:** Choose cache invalidation strategies that match correctness needs.

**Explanation:** Write-through keeps cache warmer at the cost of write latency.

---

## Question 9: You found a hotspot function via profiler. Next step?
**Answer: B** — Optimize that hotspot and re-measure against the baseline

**Outcome 2:** Run load tests and locate bottlenecks with evidence.

**Explanation:** Measure → change → re-measure the same scenario.

---

## Question 10: Micro-optimizing before profiling is risky because…
**Answer: B** — You may optimize the wrong place while the real hotspot remains

**Outcome 1:** Establish performance baselines before changing code.

**Explanation:** Evidence first; intuition about hotspots is often wrong.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
