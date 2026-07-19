# Core Concepts (Intermediate) Quiz Answers

## Question 1: Why prefer clear data models/types at module boundaries?
**Answer: A** — To make invalid states harder and intent obvious to callers

**Outcome 1:** Model data idiomatically with clear types and boundaries.

**Explanation:** Idiomatic modeling documents contracts and catches mistakes earlier.

---

## Question 2: Which error-handling approach is usually better for libraries?
**Answer: B** — Raise specific errors (or return structured results) that callers can handle

**Outcome 2:** Handle errors in a way that is debuggable and safe for callers.

**Explanation:** Callers need actionable, specific failure modes — not silent `None` or process death.

---

## Question 3: Hidden global mutable state makes tests hard because…
**Answer: A** — Tests become order-dependent and hard to isolate

**Outcome 3:** Design modules that are testable without hidden global state.

**Explanation:** Inject dependencies and keep modules pure/testable where possible.

---

## Question 4: Which design is easier to unit test?
**Answer: B** — A function that accepts a repository/connection as a parameter

**Outcome 3:** Design modules that are testable without hidden global state.

**Explanation:** Dependency injection creates a seam for fakes/fakes doubles in tests.

---

## Question 5: Using a typed model / schema object for an API payload mainly helps by…
**Answer: A** — Documenting fields and validating shape early

**Outcome 1:** Model data idiomatically with clear types and boundaries.

**Explanation:** Structured models clarify and enforce the data contract.

---

## Question 6: When logging an error, you should avoid…
**Answer: B** — Including secrets or raw passwords

**Outcome 2:** Handle errors in a way that is debuggable and safe for callers.

**Explanation:** Debuggability must not leak secrets.

---

## Question 7: A module imports and mutates a process-wide cache at import time. Risk?
**Answer: B** — Surprising side effects and brittle tests

**Outcome 3:** Design modules that are testable without hidden global state.

**Explanation:** Import-time side effects hurt testability and predictability.

---

## Question 8: “Make invalid states unrepresentable” is closest to which practice?
**Answer: A** — Using types/models so illegal combinations cannot be constructed easily

**Outcome 1:** Model data idiomatically with clear types and boundaries.

**Explanation:** Good models encode legal states in the type/shape itself.

---

## Question 9: A caller must distinguish “not found” from “permission denied.” What should your API/module do?
**Answer: B** — Signal distinct error types/codes for each case

**Outcome 2:** Handle errors in a way that is debuggable and safe for callers.

**Explanation:** Distinct errors let callers branch correctly.

---

## Question 10: Why keep “pure” logic separate from I/O in a module?
**Answer: A** — So business rules can be unit-tested without a database or network

**Outcome 3:** Design modules that are testable without hidden global state.

**Explanation:** Separating pure logic from I/O is core testable design.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
