# Core Concepts (Intermediate) Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Why prefer clear data models/types at module boundaries?
**Checks outcome 1:** Model data idiomatically with clear types and boundaries.

A) To make invalid states harder and intent obvious to callers  
B) Because maps/dicts are illegal  
C) To slow imports on purpose  
D) To avoid writing tests  

**Your answer:** _______________

---

### Question 2: Which error-handling approach is usually better for libraries?
**Checks outcome 2:** Handle errors in a way that is debuggable and safe for callers.

A) Swallow all exceptions and return `None` silently  
B) Raise specific errors (or return structured results) that callers can handle  
C) Call `sys.exit` on every validation failure  
D) Print secrets into logs when failing  

**Your answer:** _______________

---

### Question 3: Hidden global mutable state makes tests hard because…
**Checks outcome 3:** Design modules that are testable without hidden global state.

A) Tests become order-dependent and hard to isolate  
B) The test runner cannot import modules  
C) Functions become pure automatically  
D) Types disappear  

**Your answer:** _______________

---

### Question 4: Which design is easier to unit test?
**Checks outcome 3:** Design modules that are testable without hidden global state.

A) A function that reads a hard-coded production database URL from a global  
B) A function that accepts a repository/connection as a parameter  
C) A module that writes files to random paths with no seams  
D) Code that only runs inside a hidden import side effect  

**Your answer:** _______________

---

### Question 5: Using a typed model / schema object for an API payload mainly helps by…
**Checks outcome 1:** Model data idiomatically with clear types and boundaries.

A) Documenting fields and validating shape early  
B) Removing the need for HTTP status codes  
C) Replacing authentication  
D) Making Big-O irrelevant  

**Your answer:** _______________

---

### Question 6: When logging an error, you should avoid…
**Checks outcome 2:** Handle errors in a way that is debuggable and safe for callers.

A) Including a request ID  
B) Including secrets or raw passwords  
C) Including the error type  
D) Including a short human message  

**Your answer:** _______________

---

### Question 7: A module imports and mutates a process-wide cache at import time. Risk?
**Checks outcome 3:** Design modules that are testable without hidden global state.

A) Easier parallel testing  
B) Surprising side effects and brittle tests  
C) Guaranteed purity  
D) Automatic rollbacks  

**Your answer:** _______________

---

### Question 8: “Make invalid states unrepresentable” is closest to which practice?
**Checks outcome 1:** Model data idiomatically with clear types and boundaries.

A) Using types/models so illegal combinations cannot be constructed easily  
B) Storing everything as untyped `Any` blobs  
C) Parsing JSON with `eval`  
D) Skipping validation because the UI is trusted  

**Your answer:** _______________

---

### Question 9: A caller must distinguish “not found” from “permission denied.” What should your API/module do?
**Checks outcome 2:** Handle errors in a way that is debuggable and safe for callers.

A) Use one generic `Exception` with no details  
B) Signal distinct error types/codes for each case  
C) Return `False` for both  
D) Exit the process  

**Your answer:** _______________

---

### Question 10: Why keep “pure” logic separate from I/O in a module?
**Checks outcome 3:** Design modules that are testable without hidden global state.

A) So business rules can be unit-tested without a database or network  
B) Because I/O is illegal in all languages  
C) To prevent using functions  
D) To force all code into one file  

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
