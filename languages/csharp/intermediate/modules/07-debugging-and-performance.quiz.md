# C# Intermediate — Module 07: Debugging and Performance Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: What is the best first step when a bug is reported?
**Checks outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

A) Rewrite the whole app  
B) Reproduce it reliably with clear steps/inputs  
C) Delete logs so they stay clean  
D) Optimize unrelated code  

**Your answer:** _______________

---

### Question 2: After reproducing, what comes next in a solid workflow?
**Checks outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

A) Ship a random change  
B) Isolate the failing component/layer, then fix with a regression test  
C) Turn off monitoring  
D) Blame the reporter  

**Your answer:** _______________

---

### Question 3: Which log practice helps production debugging most?
**Checks outcome 2:** Use logging and basic tracing to locate failures in running systems.

A) Logging secrets and full card numbers  
B) Structured logs with request IDs and actionable context (no secrets)  
C) Printing nothing ever  
D) Only logging on the developer laptop  

**Your answer:** _______________

---

### Question 4: Why profile before micro-optimizing random functions?
**Checks outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

A) Profiling is slower than guessing wrong forever  
B) Evidence shows where time/memory actually go — intuition is often wrong  
C) Profilers delete bugs automatically  
D) Benchmarks are forbidden by the language  

**Your answer:** _______________

---

### Question 5: A memory profile shows unbounded growth on each request. Likely class of issue?
**Checks outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

A) A leak / unbounded cache / retaining references  
B) Perfect GC behavior  
C) Too many useful indexes  
D) Commit messages that are too clear  

**Your answer:** _______________

---

### Question 6: An endpoint is slow and DB time dominates. What should you inspect?
**Checks outcome 4:** Improve database performance using slow-query analysis and indexes.

A) Only the favicon  
B) Slow queries and whether indexes/plans match the filters  
C) The office thermostat  
D) Whether the README mentions SQL comments  

**Your answer:** _______________

---

### Question 7: Tracing across services primarily helps you…
**Checks outcome 2:** Use logging and basic tracing to locate failures in running systems.

A) See a request's path/latency across components  
B) Replace unit tests  
C) Avoid writing logs forever  
D) Encrypt disks by itself  

**Your answer:** _______________

---

### Question 8: Why add a regression test after fixing a bug?
**Checks outcome 1:** Follow a reproduce → isolate → fix debugging workflow with evidence.

A) To guarantee the same bug can return unnoticed  
B) To lock the fixed behavior so it cannot silently break again  
C) Because CI requires failing tests  
D) To increase flakiness  

**Your answer:** _______________

---

### Question 9: Adding an index on every column “just in case” is often bad because…
**Checks outcome 4:** Improve database performance using slow-query analysis and indexes.

A) Indexes are free  
B) Extra indexes slow writes and may never help reads  
C) SQL forbids more than one index  
D) Query plans ignore indexes always  

**Your answer:** _______________

---

### Question 10: A micro-benchmark says a function is 2% faster, but users still wait 5s. What next?
**Checks outcome 3:** Profile CPU and memory to find real hotspots before optimizing.

A) Stop measuring  
B) Profile the end-to-end path — the hotspot may be elsewhere (often I/O/DB)  
C) Optimize the function another 50 times blindly  
D) Disable logging of latency  

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
