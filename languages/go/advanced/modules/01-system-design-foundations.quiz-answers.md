# Go Advanced — Module 01: System Design Foundations Quiz Answers

## Question 1: A stakeholder says “make it scale.” What should you produce first?
**Answer: B** — Measurable requirements, hard constraints, and rough capacity estimates

**Outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

**Explanation:** Requirements and estimates bound the design; “scale” alone is not a design input.

---

## Question 2: Which estimate is most useful early in a design?
**Answer: B** — Order-of-magnitude QPS, storage, and payload size

**Outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

**Explanation:** Rough capacity estimates drive caching, sharding, and hardware choices.

---

## Question 3: Read-heavy traffic with mostly identical responses. First lever?
**Answer: B** — A cache in front of the origin with a clear TTL/invalidation story

**Outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

**Explanation:** Caching cuts origin load for hot reads when invalidation is planned.

---

## Question 4: Why partition (shard) a growing dataset?
**Answer: B** — To keep each node’s data and query load within capacity

**Outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

**Explanation:** Partitions spread data and load; they also add operational complexity.

---

## Question 5: CAP “partition tolerance” in practice means…
**Answer: B** — The system keeps operating despite network splits between nodes

**Outcome 3:** Apply CAP/consistency tradeoffs to pick a consistency model for a use case.

**Explanation:** Real distributed systems must tolerate partitions; you then trade C vs A.

---

## Question 6: A bank ledger needs strong correctness across accounts. Prefer…
**Answer: B** — Strong consistency (or ACID transactions) for money movement

**Outcome 3:** Apply CAP/consistency tradeoffs to pick a consistency model for a use case.

**Explanation:** Financial correctness usually needs strong consistency, not pure eventual.

---

## Question 7: When are queues/streams a better fit than sync request/response?
**Answer: B** — When work is bursty, long-running, or must fan out asynchronously

**Outcome 4:** Design async workflows with queues or streams when synchronous request paths are insufficient.

**Explanation:** Async pipelines absorb spikes and decouple producers from slow consumers.

---

## Question 8: A stream consumer crashes mid-batch. What design concern appears?
**Answer: B** — At-least-once delivery and idempotent processing

**Outcome 4:** Design async workflows with queues or streams when synchronous request paths are insufficient.

**Explanation:** Async systems retry; handlers must tolerate duplicates.

---

## Question 9: A load balancer’s primary job is to…
**Answer: B** — Distribute traffic across healthy instances

**Outcome 2:** Choose caching, load balancing, and data partitioning approaches for a given load pattern.

**Explanation:** LBs spread load and route away from unhealthy nodes.

---

## Question 10: Which constraint most changes a chatty mobile API design?
**Answer: B** — Bandwidth, battery, and high latency on poor networks

**Outcome 1:** Turn vague product goals into requirements, constraints, and rough capacity estimates.

**Explanation:** Mobile constraints push toward fewer round-trips and smaller payloads.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
