# Kotlin Advanced — Module 04: Performance and Profiling Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Why capture a baseline before optimizing?
**Checks outcome 1:** Establish performance baselines before changing code.

A) So you can claim victory without numbers  
B) To know whether a change actually improved latency/throughput  
C) Baselines are illegal in production  
D) To avoid writing tests  

**Your answer:** _______________

---

### Question 2: A good baseline includes…
**Checks outcome 1:** Establish performance baselines before changing code.

A) Only vibes from code review  
B) Workload definition plus measured latency/error/resource metrics  
C) A single untimed run on a laptop during a meeting  
D) Disabling monitoring  

**Your answer:** _______________

---

### Question 3: Load testing primarily answers…
**Checks outcome 2:** Run load tests and locate bottlenecks with evidence.

A) Whether the logo is centered  
B) How the system behaves under target/peak concurrency and data size  
C) Whether CAP is solved  
D) Whether commits explain why  

**Your answer:** _______________

---

### Question 4: CPU is idle but latency is high. Likely bottleneck class?
**Checks outcome 2:** Run load tests and locate bottlenecks with evidence.

A) Always the sorting algorithm  
B) I/O waits, locks, or external dependencies  
C) Too many unit tests  
D) Missing README badges  

**Your answer:** _______________

---

### Question 5: A slow filter on `user_id` with sequential scans suggests…
**Checks outcome 3:** Tune databases using indexes, query plans, and lock analysis.

A) Deleting the WHERE clause  
B) Adding/using an appropriate index and verifying the plan  
C) Buying a new laptop only  
D) Caching the entire internet  

**Your answer:** _______________

---

### Question 6: Lock contention shows up as…
**Checks outcome 3:** Tune databases using indexes, query plans, and lock analysis.

A) Faster writes always  
B) Sessions waiting on locks held by other transactions  
C) Free consistency  
D) Lower cardinality metrics  

**Your answer:** _______________

---

### Question 7: Cache-aside with TTL mainly risks…
**Checks outcome 4:** Choose cache invalidation strategies that match correctness needs.

A) Serving stale data until TTL/invalidation  
B) Never needing a database  
C) Guaranteed linearizability  
D) Automatic threat models  

**Your answer:** _______________

---

### Question 8: Write-through caching means…
**Checks outcome 4:** Choose cache invalidation strategies that match correctness needs.

A) Writes update cache and store together (sync path)  
B) Never writing to the store  
C) Only invalidating on Fridays  
D) Deleting keys randomly for fun  

**Your answer:** _______________

---

### Question 9: You found a hotspot function via profiler. Next step?
**Checks outcome 2:** Run load tests and locate bottlenecks with evidence.

A) Rewrite the whole monorepo  
B) Optimize that hotspot and re-measure against the baseline  
C) Disable the profiler forever  
D) Add random sleeps  

**Your answer:** _______________

---

### Question 10: Micro-optimizing before profiling is risky because…
**Checks outcome 1:** Establish performance baselines before changing code.

A) Profilers always lie  
B) You may optimize the wrong place while the real hotspot remains  
C) Baselines forbid improvements  
D) Load tests are illegal  

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
