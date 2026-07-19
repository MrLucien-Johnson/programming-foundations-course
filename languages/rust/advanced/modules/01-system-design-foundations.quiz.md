# Rust Advanced — Module 01: System Design Foundations Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A stakeholder says “make it scale.” What should you produce first?
**Checks outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

A) A production deploy with no written constraints  
B) Measurable requirements, hard constraints, and rough capacity estimates  
C) A choice of logo colors  
D) Only a list of frameworks you like  

**Your answer:** _______________

---

### Question 2: Which estimate is most useful early in a design?
**Checks outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

A) Exact microsecond latency of every function  
B) Order-of-magnitude QPS, storage, and payload size  
C) The CEO’s favorite database brand  
D) How many linters the repo has  

**Your answer:** _______________

---

### Question 3: Read-heavy traffic with mostly identical responses. First lever?
**Checks outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

A) Replicate writes to every client browser  
B) A cache in front of the origin with a clear TTL/invalidation story  
C) Disable the load balancer  
D) Store everything in one giant unsorted file  

**Your answer:** _______________

---

### Question 4: Why partition (shard) a growing dataset?
**Checks outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

A) To make CAP irrelevant  
B) To keep each node’s data and query load within capacity  
C) Because load balancers cannot distribute connections  
D) To avoid writing indexes forever  

**Your answer:** _______________

---

### Question 5: CAP “partition tolerance” in practice means…
**Checks outcome 3:** Apply CAP/consistency tradeoffs to pick a consistency model for a use case.

A) You never need retries  
B) The system keeps operating despite network splits between nodes  
C) All writes are free  
D) Caches never expire  

**Your answer:** _______________

---

### Question 6: A bank ledger needs strong correctness across accounts. Prefer…
**Checks outcome 3:** Apply CAP/consistency tradeoffs to pick a consistency model for a use case.

A) Eventual consistency with no conflict handling  
B) Strong consistency (or ACID transactions) for money movement  
C) Best-effort UDP without acks  
D) Client-side-only validation  

**Your answer:** _______________

---

### Question 7: When are queues/streams a better fit than sync request/response?
**Checks outcome 4:** Design async workflows with queues or streams when synchronous request paths are insufficient.

A) For every static CSS file  
B) When work is bursty, long-running, or must fan out asynchronously  
C) When you want to avoid all observability  
D) When CAP says consistency is free  

**Your answer:** _______________

---

### Question 8: A stream consumer crashes mid-batch. What design concern appears?
**Checks outcome 4:** Design async workflows with queues or streams when synchronous request paths are insufficient.

A) Only CSS theming  
B) At-least-once delivery and idempotent processing  
C) Whether OpenAPI fonts are pretty  
D) Deleting the partition key forever  

**Your answer:** _______________

---

### Question 9: A load balancer’s primary job is to…
**Checks outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

A) Encrypt backups by itself  
B) Distribute traffic across healthy instances  
C) Replace the database schema  
D) Write ADRs automatically  

**Your answer:** _______________

---

### Question 10: Which constraint most changes a chatty mobile API design?
**Checks outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

A) The office snack budget  
B) Bandwidth, battery, and high latency on poor networks  
C) Whether CI uses matrices  
D) The number of README badges  

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
