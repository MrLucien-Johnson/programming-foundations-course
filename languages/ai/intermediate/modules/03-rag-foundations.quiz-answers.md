# AI — Module 03: RAG Foundations Quiz Answers

## Question 1: Chunking strategy matters because…
**Answer: B** — It affects what can be retrieved and cited

**Outcome 1:** Chunk documents and attach metadata for retrieval.

**Explanation:** Chunks are the retrieval unit.

---

## Question 2: Useful metadata often includes…
**Answer: B** — Doc type, version, and access tags

**Outcome 1:** Chunk documents and attach metadata for retrieval.

**Explanation:** Metadata enables filters and governance.

---

## Question 3: Grounded answering requires…
**Answer: B** — Using retrieved context and citing supporting excerpts

**Outcome 2:** Answer only from retrieved context with citations.

**Explanation:** Citations make grounding checkable.

---

## Question 4: “No evidence → abstain” mainly reduces…
**Answer: B** — Unsupported claims

**Outcome 2:** Answer only from retrieved context with citations.

**Explanation:** Abstention is an anti-hallucination control.

---

## Question 5: If retrieval returns empty, generation should…
**Answer: B** — Abstain or ask — not fabricate

**Outcome 3:** Abstain when evidence is missing and measure hallucination drop.

**Explanation:** Empty retrieval is a retrieval failure, not a writing prompt.

---

## Question 6: Tracking retrieval vs generation failures separately helps because…
**Answer: B** — Wrong mitigations waste effort (index vs prompt)

**Outcome 4:** Separate retrieval failures from generation failures in evals.

**Explanation:** Split metrics target the right layer.

---

## Question 7: A wrong answer with perfect citations to irrelevant chunks is usually…
**Answer: B** — A retrieval relevance problem (and/or ranking)

**Outcome 4:** Separate retrieval failures from generation failures in evals.

**Explanation:** Bad evidence in → grounded-but-wrong out.

---

## Question 8: Query rewriting can improve…
**Answer: B** — Retrieval hit-rate on a fixed question set

**Outcome 5:** Improve hit-rate with query rewriting and simple offline metrics.

**Explanation:** Better queries → better candidates.

---

## Question 9: Precision@k as a proxy evaluates…
**Answer: B** — Whether top-k retrieved chunks are relevant

**Outcome 5:** Improve hit-rate with query rewriting and simple offline metrics.

**Explanation:** Offline retrieval metrics guide indexing/chunking.

---

## Question 10: Why cite excerpts rather than say “according to docs”?
**Answer: B** — They let humans verify the claim against evidence

**Outcome 2:** Answer only from retrieved context with citations.

**Explanation:** Verifiability is the point of grounding.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
