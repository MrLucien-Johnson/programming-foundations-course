# Systems and Design (Advanced) Quiz Answers

## Question 1: A scalable design doc should state…
**Answer: B** — Expected load, bottlenecks, and how the design handles them

**Outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

**Explanation:** Scale claims need load assumptions and bottleneck thinking.

---

## Question 2: Vertical scaling alone becomes a problem when…
**Answer: A** — A single machine’s limits or cost ceiling are hit

**Outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

**Explanation:** Eventually you need horizontal strategies.

---

## Question 3: Recording rejected alternatives in an ADR helps reviewers…
**Answer: B** — Understand why this option won given constraints

**Outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

**Explanation:** Tradeoff docs preserve decision rationale.

---

## Question 4: “We picked eventual consistency” without saying why is weak because…
**Answer: B** — Reviewers cannot judge fitness without constraints and failure modes

**Outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

**Explanation:** Name the constraint that forced the tradeoff.

---

## Question 5: If the design hinges on a cache hit rate, verification should include…
**Answer: B** — A load or rehearsal that measures hit rate under realistic keys

**Outcome 3:** Define verification (tests, load checks, or probes) that match the design risks.

**Explanation:** Validate the risky assumptions, not only happy-path code.

---

## Question 6: A design that adds many new failure domains should plan…
**Answer: B** — Health checks, SLOs, and failure drills for those domains

**Outcome 3:** Define verification (tests, load checks, or probes) that match the design risks.

**Explanation:** New complexity needs operable verification.

---

## Question 7: Sharding by user_id helps when…
**Answer: A** — Traffic and data grow beyond one node fairly evenly by user

**Outcome 1:** Design a service for expected scale with explicit bottlenecks and mitigations.

**Explanation:** Key choice must match access patterns — cross-shard ops stay hard.

---

## Question 8: A good tradeoff write-up compares options on…
**Answer: B** — Cost, complexity, consistency, and operability against requirements

**Outcome 2:** Document architecture tradeoffs and rejected alternatives clearly.

**Explanation:** Tradeoffs are multi-dimensional against real constraints.

---

## How Did You Do?

- **8/8 correct:** Excellent! You are ready to move on.
- **6-7 correct:** Great work — review the missed outcomes.
- **0-5 correct:** Revisit the module lessons, then try again.
