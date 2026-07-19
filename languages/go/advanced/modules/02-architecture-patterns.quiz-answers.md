# Go Advanced — Module 02: Architecture Patterns Quiz Answers

## Question 1: In hexagonal architecture, domain logic should depend on…
**Answer: B** — Ports (interfaces); adapters implement infrastructure outside

**Outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

**Explanation:** Ports/adapters keep the domain independent of frameworks.

---

## Question 2: Layered architecture usually forbids…
**Answer: B** — Lower layers depending upward on UI/controllers

**Outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

**Explanation:** Dependencies should point inward/downward, not from domain to UI.

---

## Question 3: A money amount with currency is best modeled as…
**Answer: B** — A value object enforcing valid combinations

**Outcome 2:** Model domain concepts with entities, value objects, and aggregates.

**Explanation:** Value objects capture immutable domain rules without identity.

---

## Question 4: An aggregate boundary mainly protects…
**Answer: B** — Consistency of a cluster of entities updated together

**Outcome 2:** Model domain concepts with entities, value objects, and aggregates.

**Explanation:** Aggregates define transactional consistency boundaries in DDD.

---

## Question 5: A saga is useful when…
**Answer: B** — A long process spans services and needs compensating steps on failure

**Outcome 3:** Design event-driven flows and sagas for multi-step business processes.

**Explanation:** Sagas coordinate distributed steps with compensations, not one giant DB TX.

---

## Question 6: Event-driven design primarily helps by…
**Answer: B** — Decoupling producers from consumers via facts that happened

**Outcome 3:** Design event-driven flows and sagas for multi-step business processes.

**Explanation:** Events decouple; delivery semantics still need careful design.

---

## Question 7: CQRS is often overkill when…
**Answer: A** — Read and write models are simple and change together

**Outcome 4:** Decide when CQRS helps — and when it adds unjustified complexity.

**Explanation:** CQRS adds dual models/complexity; use it when asymmetry justifies it.

---

## Question 8: A team adopts CQRS “for purity” on a CRUD admin tool. Risk?
**Answer: B** — Extra moving parts without a scaling/consistency payoff

**Outcome 4:** Decide when CQRS helps — and when it adds unjustified complexity.

**Explanation:** Patterns must earn their complexity against real constraints.

---

## Question 9: Clean architecture’s dependency rule says source code dependencies point…
**Answer: B** — Inward toward enterprise/domain policy

**Outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

**Explanation:** Inner policy must not depend on outer details.

---

## Question 10: Two entities that must stay consistent in one transaction likely belong…
**Answer: B** — In the same aggregate (or a carefully designed process)

**Outcome 2:** Model domain concepts with entities, value objects, and aggregates.

**Explanation:** Aggregate design follows consistency needs.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
