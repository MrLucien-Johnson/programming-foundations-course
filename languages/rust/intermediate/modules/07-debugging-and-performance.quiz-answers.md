# Rust Intermediate — Module 07: Debugging and Performance Quiz Answers

## Question 1: What is the best first step when a bug is reported?
**Answer: B** — Reproduce it reliably with clear steps/inputs

**Outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

**Explanation:** If you cannot reproduce, you cannot verify a fix.

---

## Question 2: After reproducing, what comes next in a solid workflow?
**Answer: B** — Isolate the failing component/layer, then fix with a regression test

**Outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

**Explanation:** Reproduce → isolate → fix (and lock with a test).

---

## Question 3: Which log practice helps production debugging most?
**Answer: B** — Structured logs with request IDs and actionable context (no secrets)

**Outcome 2:** Use logging and basic tracing to locate failures in running systems.

**Explanation:** Structured, correlatable logs (minus secrets) make tracing failures possible.

---

## Question 4: Why profile before micro-optimizing random functions?
**Answer: B** — Evidence shows where time/memory actually go — intuition is often wrong

**Outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

**Explanation:** Measure first; optimize the real hotspot.

---

## Question 5: A memory profile shows unbounded growth on each request. Likely class of issue?
**Answer: A** — A leak / unbounded cache / retaining references

**Outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

**Explanation:** Rising memory usually means retained objects, caches without bounds, or leaks.

---

## Question 6: An endpoint is slow and DB time dominates. What should you inspect?
**Answer: B** — Slow queries and whether indexes/plans match the filters

**Outcome 4:** Improve database performance using slow-query analysis and indexes.

**Explanation:** DB-bound latency is attacked with query analysis and indexing.

---

## Question 7: Tracing across services primarily helps you…
**Answer: A** — See a request's path/latency across components

**Outcome 2:** Use logging and basic tracing to locate failures in running systems.

**Explanation:** Traces show where a request spends time across boundaries.

---

## Question 8: Why add a regression test after fixing a bug?
**Answer: B** — To lock the fixed behavior so it cannot silently break again

**Outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

**Explanation:** Regression tests are the durable part of isolate → fix.

---

## Question 9: Adding an index on every column “just in case” is often bad because…
**Answer: B** — Extra indexes slow writes and may never help reads

**Outcome 4:** Improve database performance using slow-query analysis and indexes.

**Explanation:** Index with intent from measured slow queries/plans.

---

## Question 10: A micro-benchmark says a function is 2% faster, but users still wait 5s. What next?
**Answer: B** — Profile the end-to-end path — the hotspot may be elsewhere (often I/O/DB)

**Outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

**Explanation:** Local wins can miss the real end-to-end bottleneck.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
