# Python Intermediate — Module 04: APIs and Auth Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A client successfully creates a new resource. Which status code is most appropriate?
**Checks outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

A) 500  
B) 201 Created  
C) 404 Not Found  
D) 401 Unauthorized  

**Your answer:** _______________

---

### Question 2: Why paginate list endpoints?
**Checks outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

A) To hide errors from clients  
B) To bound response size and keep latency predictable as data grows  
C) Because REST forbids returning more than one item ever  
D) To avoid using status codes  

**Your answer:** _______________

---

### Question 3: A client sends an invalid email format. What should the API do?
**Checks outcome 2:** Validate input and return consistent error envelopes for clients.

A) Store it anyway  
B) Reject with 4xx and a clear, consistent error body  
C) Return 200 with empty data and no message  
D) Crash the worker process  

**Your answer:** _______________

---

### Question 4: Authentication answers which question?
**Checks outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

A) What is this user allowed to do?  
B) Who is this user / is the identity proven?  
C) How fast is the database?  
D) Which CSS theme to use?  

**Your answer:** _______________

---

### Question 5: A logged-in user tries to delete another user's private document. Which check failed if they are blocked?
**Checks outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

A) Only DNS  
B) Authorization (AuthZ) / permissions  
C) Pagination  
D) OpenAPI formatting  

**Your answer:** _______________

---

### Question 6: JWTs are commonly used to…
**Checks outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

A) Replace HTTPS  
B) Carry a signed identity/claims token the API can verify without a server session store (depending on design)  
C) Encrypt the entire database at rest by themselves  
D) Format source code  

**Your answer:** _______________

---

### Question 7: Why rate-limit a login endpoint?
**Checks outcome 4:** Add basic rate limiting / abuse protections to sensitive endpoints.

A) To make UX worse for no reason  
B) To slow brute-force and abuse attempts  
C) Because HTTP forbids retries  
D) To increase 500 errors intentionally  

**Your answer:** _______________

---

### Question 8: What does OpenAPI documentation help API consumers do?
**Checks outcome 5:** Document the API with OpenAPI (or equivalent) including examples.

A) Guess endpoints from production outages only  
B) See routes, schemas, status codes, and examples in one contract  
C) Bypass authentication permanently  
D) Avoid writing any server code  

**Your answer:** _______________

---

### Question 9: Which error response style is more client-friendly?
**Checks outcome 2:** Validate input and return consistent error envelopes for clients.

A) Random HTML stack traces with no structure  
B) A consistent JSON envelope like `{ "error": { "code": "validation_error", "message": "..." } }`  
C) Empty 200 OK for failures  
D) Closing the TCP connection silently  

**Your answer:** _______________

---

### Question 10: `GET /users/{id}` when the user does not exist should typically return:
**Checks outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

A) 201 Created  
B) 404 Not Found  
C) 100 Continue forever  
D) 302 to a random site  

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
