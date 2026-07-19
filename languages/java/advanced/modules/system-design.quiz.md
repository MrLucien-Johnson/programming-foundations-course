# Systems and Design (Advanced) Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A scalable design doc should state…
**Checks outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

A) Only the framework fashion of the week  
B) Expected load, bottlenecks, and how the design handles them  
C) No numbers at all  
D) Secrets in plaintext  

**Your answer:** _______________

---

### Question 2: Vertical scaling alone becomes a problem when…
**Checks outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

A) A single machine’s limits or cost ceiling are hit  
B) You add read replicas thoughtfully  
C) You cache hot keys  
D) You use a load balancer  

**Your answer:** _______________

---

### Question 3: Recording rejected alternatives in an ADR helps reviewers…
**Checks outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

A) Re-litigate the same debates forever  
B) Understand why this option won given constraints  
C) Skip reading the design  
D) Avoid tests  

**Your answer:** _______________

---

### Question 4: “We picked eventual consistency” without saying why is weak because…
**Checks outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

A) Eventual consistency is illegal  
B) Reviewers cannot judge fitness without constraints and failure modes  
C) CAP forbids documentation  
D) Queues cannot be mentioned  

**Your answer:** _______________

---

### Question 5: If the design hinges on a cache hit rate, verification should include…
**Checks outcome 3:** Define verification (tests, load checks, or probes) that match the design risks.

A) Only a unit test of string concat  
B) A load or rehearsal that measures hit rate under realistic keys  
C) Deleting metrics  
D) A logo review  

**Your answer:** _______________

---

### Question 6: A design that adds many new failure domains should plan…
**Checks outcome 3:** Define verification (tests, load checks, or probes) that match the design risks.

A) No probes or alerts  
B) Health checks, SLOs, and failure drills for those domains  
C) Only manual SSH forever  
D) Skipping runbooks  

**Your answer:** _______________

---

### Question 7: Sharding by user_id helps when…
**Checks outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

A) Traffic and data grow beyond one node fairly evenly by user  
B) You never read data  
C) CAP is optional  
D) You want cross-shard transactions for free  

**Your answer:** _______________

---

### Question 8: A good tradeoff write-up compares options on…
**Checks outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

A) Only aesthetics  
B) Cost, complexity, consistency, and operability against requirements  
C) Twitter likes  
D) Variable names alone  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **8/8 correct:** Excellent — you can apply this module's outcomes.
- **6-7 correct:** Strong — review the missed outcome(s).
- **0-5 correct:** Revisit the lessons for those outcomes, then retry.

---

**Good luck!** Check your answers when you are ready.
