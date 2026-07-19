# AI — Module 02: RAG: Advanced Retrieval Quiz Answers

## Question 1: Separating hit-rate from groundedness tells you…
**Answer: B** — Whether misses are retrieval or generation problems

**Outcome 1:** Evaluate retrieval with hit-rate, groundedness, and abstention metrics.

**Explanation:** Split metrics guide fixes.

---

## Question 2: High abstention with high hit-rate may mean…
**Answer: B** — Over-strict grounding or poor evidence use in generation

**Outcome 1:** Evaluate retrieval with hit-rate, groundedness, and abstention metrics.

**Explanation:** Interpret metric pairs, not single numbers.

---

## Question 3: Comparing two chunking strategies requires…
**Answer: B** — The same question set and recorded metrics

**Outcome 2:** Compare chunking strategies with measured tradeoffs.

**Explanation:** Controlled A/B on retrieval units.

---

## Question 4: Huge chunks often hurt because…
**Answer: B** — Irrelevant text dilutes retrieval and context windows

**Outcome 2:** Compare chunking strategies with measured tradeoffs.

**Explanation:** Chunk size is a relevance/context tradeoff.

---

## Question 5: Reranking helps when…
**Answer: B** — Top-n candidates need relevance reordering before generation

**Outcome 3:** Add reranking and quantify lift on a fixed question set.

**Explanation:** Rerank refines candidate lists.

---

## Question 6: Measure rerank lift by…
**Answer: B** — Diffing metrics on a fixed question set with/without rerank

**Outcome 3:** Add reranking and quantify lift on a fixed question set.

**Explanation:** Hold the set constant.

---

## Question 7: ACL-aware retrieval means…
**Answer: B** — Only retrieve documents the caller is allowed to see

**Outcome 4:** Enforce access-control-aware retrieval to prevent leakage.

**Explanation:** Filter at retrieval time, not after generation.

---

## Question 8: Leakage across permissions is a…
**Answer: B** — Security/privacy incident class for RAG

**Outcome 4:** Enforce access-control-aware retrieval to prevent leakage.

**Explanation:** Treat cross-tenant retrieval as a breach path.

---

## Question 9: Freshness tests verify…
**Answer: B** — Newly added docs become retrievable within an agreed window

**Outcome 5:** Test freshness so new docs become retrievable within a target window.

**Explanation:** Index lag is a product bug for many domains.

---

## Question 10: Groundedness scoring checks…
**Answer: A** — Whether claims are supported by retrieved evidence

**Outcome 1:** Evaluate retrieval with hit-rate, groundedness, and abstention metrics.

**Explanation:** Groundedness is evidence alignment.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
