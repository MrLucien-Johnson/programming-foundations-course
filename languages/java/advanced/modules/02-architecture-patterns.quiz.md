# Java Advanced — Module 02: Architecture Patterns Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: In hexagonal architecture, domain logic should depend on…
**Checks outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

A) Concrete HTTP frameworks and SQL drivers directly  
B) Ports (interfaces); adapters implement infrastructure outside  
C) Global mutable singletons only  
D) The presentation layer’s CSS  

**Your answer:** _______________

---

### Question 2: Layered architecture usually forbids…
**Checks outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

A) Having a UI at all  
B) Lower layers depending upward on UI/controllers  
C) Using a database  
D) Writing tests  

**Your answer:** _______________

---

### Question 3: A money amount with currency is best modeled as…
**Checks outcome 2:** Model domain concepts with entities, value objects, and aggregates.

A) Two unrelated ints with no rules  
B) A value object enforcing valid combinations  
C) A UI color picker  
D) A thread ID  

**Your answer:** _______________

---

### Question 4: An aggregate boundary mainly protects…
**Checks outcome 2:** Model domain concepts with entities, value objects, and aggregates.

A) CSS specificity  
B) Consistency of a cluster of entities updated together  
C) DNS TTLs  
D) Lint rule names  

**Your answer:** _______________

---

### Question 5: A saga is useful when…
**Checks outcome 3:** Design event-driven flows and sagas for multi-step business processes.

A) A single local ACID transaction covers the whole business process  
B) A long process spans services and needs compensating steps on failure  
C) You only render static HTML  
D) You want to avoid all failure handling  

**Your answer:** _______________

---

### Question 6: Event-driven design primarily helps by…
**Checks outcome 3:** Design event-driven flows and sagas for multi-step business processes.

A) Deleting all APIs  
B) Decoupling producers from consumers via facts that happened  
C) Guaranteeing exactly-once everywhere for free  
D) Removing the need for schemas  

**Your answer:** _______________

---

### Question 7: CQRS is often overkill when…
**Checks outcome 4:** Decide when CQRS helps — and when it adds unjustified complexity.

A) Read and write models are simple and change together  
B) You already have extreme read/write asymmetry and scaling pain  
C) You need separate optimized projections proven by load  
D) Audit projections are a hard requirement  

**Your answer:** _______________

---

### Question 8: A team adopts CQRS “for purity” on a CRUD admin tool. Risk?
**Checks outcome 4:** Decide when CQRS helps — and when it adds unjustified complexity.

A) Too little ceremony  
B) Extra moving parts without a scaling/consistency payoff  
C) Automatic CAP compliance  
D) Free idempotency  

**Your answer:** _______________

---

### Question 9: Clean architecture’s dependency rule says source code dependencies point…
**Checks outcome 1:** Compare layered, hexagonal, and clean architecture and place dependencies correctly.

A) Outward toward frameworks  
B) Inward toward enterprise/domain policy  
C) Only sideways between random packages  
D) Nowhere — cycles are encouraged  

**Your answer:** _______________

---

### Question 10: Two entities that must stay consistent in one transaction likely belong…
**Checks outcome 2:** Model domain concepts with entities, value objects, and aggregates.

A) In separate aggregates with no coordination  
B) In the same aggregate (or a carefully designed process)  
C) Only in the CDN  
D) In client localStorage exclusively  

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
