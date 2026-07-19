# AI — Module 06: Reliability and Fallbacks Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Model-down fallback might be…
**Checks outcome 1:** Define fallbacks per top failure mode (model, retrieval, tools).

A) Hang the UI forever  
B) Cached answer, smaller model, or human handoff  
C) Disable all monitoring  
D) Invent success  

**Your answer:** _______________

---

### Question 2: Empty retrieval fallback should…
**Checks outcome 1:** Define fallbacks per top failure mode (model, retrieval, tools).

A) Hallucinate confidently  
B) Abstain/ask rather than fabricate  
C) Call admin tools  
D) Raise budgets infinitely  

**Your answer:** _______________

---

### Question 3: Retry budgets on tool errors prevent…
**Checks outcome 2:** Set retry budgets and stop conditions for degraded paths.

A) All outages  
B) Unbounded cost and delayed failure signals  
C) Human queues  
D) Cached answers  

**Your answer:** _______________

---

### Question 4: Stop conditions in degraded mode…
**Checks outcome 2:** Set retry budgets and stop conditions for degraded paths.

A) Are optional flair  
B) Ensure the system does not thrash forever  
C) Forbid abstention  
D) Delete runbooks  

**Your answer:** _______________

---

### Question 5: Failure injection in harnesses proves…
**Checks outcome 3:** Failure-inject outages/timeouts in the harness.

A) Only happy paths  
B) Fallbacks actually trigger and behave safely  
C) SLOs are unnecessary  
D) Caches never expire  

**Your answer:** _______________

---

### Question 6: Simulating timeouts without assertions…
**Checks outcome 3:** Failure-inject outages/timeouts in the harness.

A) Fully validates resilience  
B) Misses whether fallbacks ran correctly  
C) Replaces IR  
D) Fixes drift  

**Your answer:** _______________

---

### Question 7: Human-in-the-loop queues need…
**Checks outcome 4:** Specify degraded modes: abstain, ask, cached answer, human queue.

A) No SLA  
B) Clear routing, SLA, and escalation  
C) Automatic approval of all risks  
D) Secret-only tickets  

**Your answer:** _______________

---

### Question 8: Cached answers as degraded mode require…
**Checks outcome 4:** Specify degraded modes: abstain, ask, cached answer, human queue.

A) Ignoring staleness forever  
B) Freshness/validity rules so wrong cache is not “reliability”  
C) No version keys  
D) Disabling abstain  

**Your answer:** _______________

---

### Question 9: Post-incident reviews should update…
**Checks outcome 5:** Run post-incident reviews that harden evals and guardrails.

A) Nothing if users calmed down  
B) Evals, guardrails, and runbooks to prevent repeats  
C) Only the logo  
D) Temperature defaults randomly  

**Your answer:** _______________

---

### Question 10: A fallback strategy tied to SLOs means…
**Checks outcome 5:** Run post-incident reviews that harden evals and guardrails.

A) Fallbacks are aesthetic  
B) You know when degraded mode is acceptable vs stop-the-line  
C) Retries are unlimited  
D) Shadow evals are banned  

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
