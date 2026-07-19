# Go Intermediate — Module 04: APIs and Auth Quiz Answers

## Question 1: A client successfully creates a new resource. Which status code is most appropriate?
**Answer: B** — 201 Created

**Outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

**Explanation:** 201 indicates a resource was created. 500 is server error; 404 missing; 401 auth failure.

---

## Question 2: Why paginate list endpoints?
**Answer: B** — To bound response size and keep latency predictable as data grows

**Outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

**Explanation:** Pagination protects performance and usability for large collections.

---

## Question 3: A client sends an invalid email format. What should the API do?
**Answer: B** — Reject with 4xx and a clear, consistent error body

**Outcome 2:** Validate input and return consistent error envelopes for clients.

**Explanation:** Validate input and return a predictable error envelope clients can handle.

---

## Question 4: Authentication answers which question?
**Answer: B** — Who is this user / is the identity proven?

**Outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

**Explanation:** AuthN = identity. AuthZ = permissions/roles after identity is known.

---

## Question 5: A logged-in user tries to delete another user's private document. Which check failed if they are blocked?
**Answer: B** — Authorization (AuthZ) / permissions

**Outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

**Explanation:** They may be authenticated but not authorized for that resource action.

---

## Question 6: JWTs are commonly used to…
**Answer: B** — Carry a signed identity/claims token the API can verify without a server session store (depending on design)

**Outcome 3:** Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.

**Explanation:** JWTs are a common AuthN token format; they do not replace transport security or AuthZ design.

---

## Question 7: Why rate-limit a login endpoint?
**Answer: B** — To slow brute-force and abuse attempts

**Outcome 4:** Add basic rate limiting / abuse protections to sensitive endpoints.

**Explanation:** Rate limits are a basic abuse protection on sensitive endpoints.

---

## Question 8: What does OpenAPI documentation help API consumers do?
**Answer: B** — See routes, schemas, status codes, and examples in one contract

**Outcome 5:** Document the API with OpenAPI (or equivalent) including examples.

**Explanation:** OpenAPI is the machine/human-readable contract for the API surface.

---

## Question 9: Which error response style is more client-friendly?
**Answer: B** — A consistent JSON envelope like `{ "error": { "code": "validation_error", "message": "..." } }`

**Outcome 2:** Validate input and return consistent error envelopes for clients.

**Explanation:** Consistent envelopes let clients branch on `code` and show `message` safely.

---

## Question 10: `GET /users/{id}` when the user does not exist should typically return:
**Answer: B** — 404 Not Found

**Outcome 1:** Design REST endpoints with clear resources, status codes, and pagination.

**Explanation:** Missing resources map to 404 in common REST practice.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
