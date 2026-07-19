# AI — Module 07: Cost, Latency, and Ops Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A budget without an enforcement action is…
**Checks outcome 1:** Set cost/latency budgets and enforce them in workflows.

A) A complete control  
B) Just a hope — define fallback when exceeded  
C) A cache key  
D) An SLO replacement  

**Your answer:** _______________

---

### Question 2: When a latency budget is exceeded, a workflow might…
**Checks outcome 1:** Set cost/latency budgets and enforce them in workflows.

A) Hang forever  
B) Fallback to a cheaper/faster path or abstain  
C) Disable monitoring  
D) Delete caches  

**Your answer:** _______________

---

### Question 3: Cache keys for LLM calls should usually include…
**Checks outcome 2:** Design cache keys and reuse strategies that preserve correctness.

A) Only the user id  
B) Prompt version + normalized inputs that determine the output  
C) Wall-clock seconds always  
D) Random UUID each time  

**Your answer:** _______________

---

### Question 4: Caching answers without prompt version in the key risks…
**Checks outcome 2:** Design cache keys and reuse strategies that preserve correctness.

A) Perfect invalidation  
B) Serving stale answers after a prompt change  
C) Lower latency forever safely  
D) Free evals  

**Your answer:** _______________

---

### Question 5: Early exit on low confidence trades…
**Checks outcome 3:** Add early-exit/abstain rules when confidence is low.

A) Nothing  
B) Some coverage for lower cost/risk of bad answers  
C) Away all safety  
D) Monitoring for silence  

**Your answer:** _______________

---

### Question 6: Context trimming in RAG helps latency/cost by…
**Checks outcome 3:** Add early-exit/abstain rules when confidence is low.

A) Sending more tokens always  
B) Keeping only necessary retrieved evidence  
C) Removing citations forever  
D) Disabling abstention  

**Your answer:** _______________

---

### Question 7: Ops dashboards for LLM features should show…
**Checks outcome 4:** Monitor quality, cost, and latency with actionable alerts.

A) Only marketing NPS  
B) Quality proxies, cost, latency, and error/fallback rates  
C) Nothing after launch  
D) Raw prompts with secrets  

**Your answer:** _______________

---

### Question 8: An alert on cost spike should be…
**Checks outcome 4:** Monitor quality, cost, and latency with actionable alerts.

A) Ignored  
B) Actionable: check canaries, caches, runaway agents  
C) Paged every DEBUG log  
D) Secret-only  

**Your answer:** _______________

---

### Question 9: Prompt canaries reduce risk by…
**Checks outcome 5:** Plan canary/rollback for prompt and model version changes.

A) Shipping to 100% first  
B) Exposing a new prompt version to a small cohort while watching metrics  
C) Skipping eval gates  
D) Disabling rollback  

**Your answer:** _______________

---

### Question 10: Rollback criteria for prompt releases should be predefined so…
**Checks outcome 5:** Plan canary/rollback for prompt and model version changes.

A) Debates happen during an outage  
B) You revert quickly on quality/cost/safety regressions  
C) Canaries never end  
D) Caches ignore versions  

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
