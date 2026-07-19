# AI — Module 01: System Design for LLM Apps Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: An LLM feature architecture diagram should show…
**Checks outcome 1:** Draw architecture and data flow for an LLM feature including failure modes.

A) Only the marketing funnel  
B) Request path, model/tools/retrieval, stores, and failure/fallback paths  
C) Office seating  
D) Font tokens  

**Your answer:** _______________

---

### Question 2: Listing failure modes early helps you…
**Checks outcome 1:** Draw architecture and data flow for an LLM feature including failure modes.

A) Skip fallbacks  
B) Attach mitigations before launch  
C) Avoid SLOs  
D) Delete evals  

**Your answer:** _______________

---

### Question 3: Queues in front of expensive model calls provide…
**Checks outcome 2:** Plan scaling with caches, queues, and backpressure for model/tool workloads.

A) Unlimited concurrency forever  
B) Smoothing and backpressure under bursty load  
C) Free quality  
D) Automatic citations  

**Your answer:** _______________

---

### Question 4: Without backpressure, a viral traffic spike tends to…
**Checks outcome 2:** Plan scaling with caches, queues, and backpressure for model/tool workloads.

A) Improve p99  
B) Overwhelm workers and blow cost/latency budgets  
C) Fix CAP  
D) Version prompts  

**Your answer:** _______________

---

### Question 5: An error budget for quality SLO means…
**Checks outcome 3:** Define latency/quality SLOs and error budgets for the feature.

A) Unlimited bad answers  
B) Allowed degradation before you must prioritize reliability work  
C) A cache TTL  
D) A threat ID  

**Your answer:** _______________

---

### Question 6: Latency SLO without a quality SLO risks…
**Checks outcome 3:** Define latency/quality SLOs and error budgets for the feature.

A) Balanced tradeoffs  
B) Optimizing speed while shipping junk answers  
C) Perfect RAG  
D) Free privacy  

**Your answer:** _______________

---

### Question 7: Backward-compatible prompt/schema migration means…
**Checks outcome 4:** Design prompt/schema migrations with backward compatibility.

A) Breaking all clients at once  
B) Old and new versions coexist safely during rollout  
C) Deleting version numbers  
D) Skipping dual-read  

**Your answer:** _______________

---

### Question 8: Changing a required JSON field name without a plan…
**Checks outcome 4:** Design prompt/schema migrations with backward compatibility.

A) Is invisible  
B) Breaks consumers mid-flight  
C) Improves SLOs automatically  
D) Is required for canaries  

**Your answer:** _______________

---

### Question 9: Privacy-by-design for prompts/outputs includes…
**Checks outcome 5:** Apply privacy-by-design (minimization, retention, access control).

A) Logging everything forever  
B) Minimization, retention limits, and access controls  
C) Public training on private tickets by default  
D) Disabling redaction  

**Your answer:** _______________

---

### Question 10: Access controls on retrieved docs matter because…
**Checks outcome 5:** Apply privacy-by-design (minimization, retention, access control).

A) RAG ignores permissions  
B) Otherwise users can read neighbors’ private content via the model  
C) Embeddings encrypt data  
D) SLOs replace ACLs  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **10/10 correct:** Excellent — you can apply this module's outcomes.
- **8-9 correct:** Strong — review the missed outcome(s).
- **0-7 correct:** Revisit the lessons for those outcomes, then retry.

---

**Good luck!** Check your answers when you are ready.
