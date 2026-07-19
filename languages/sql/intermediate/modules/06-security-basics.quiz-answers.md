# SQL (PostgreSQL) Intermediate — Module 06: Security Basics Quiz Answers

## Question 1: Broken access control in OWASP terms is closest to…
**Answer: A** — Users performing actions outside their permissions

**Outcome 1:** Map real application risks to the OWASP Top 10 categories.

**Explanation:** Access control failures let users act beyond their authorization.

---

## Question 2: Where should a production database password live?
**Answer: B** — In environment/config or a secret manager, not in source control

**Outcome 2:** Store and load secrets via config/secret managers — never commit them.

**Explanation:** Secrets belong in env/secret stores — never in git.

---

## Question 3: Which query style best prevents SQL injection?
**Answer: B** — Parameterized queries / bound parameters

**Outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

**Explanation:** Parameter binding keeps data from being interpreted as SQL code.

---

## Question 4: Showing user-provided HTML in a page without encoding risks…
**Answer: A** — XSS (cross-site scripting)

**Outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

**Explanation:** Unencoded output enables XSS — validate/encode appropriately.

---

## Question 5: Least privilege means…
**Answer: B** — Grant only the permissions required for a role/task — nothing more

**Outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

**Explanation:** Least privilege limits blast radius when accounts or tokens leak.

---

## Question 6: After AuthN succeeds, what must still happen before deleting a billing record?
**Answer: B** — An AuthZ check that this identity may delete that record

**Outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

**Explanation:** Authentication ≠ authorization. Sensitive actions need explicit AuthZ.

---

## Question 7: A secret was accidentally committed. Best immediate response?
**Answer: B** — Rotate/revoke the secret, remove it from the tree, and treat history as compromised

**Outcome 2:** Store and load secrets via config/secret managers — never commit them.

**Explanation:** Assume exposure: rotate, purge from future commits, and audit usage.

---

## Question 8: Why map bugs to OWASP categories during review?
**Answer: B** — To prioritize fixes using a shared language for common web risks

**Outcome 1:** Map real application risks to the OWASP Top 10 categories.

**Explanation:** OWASP gives a practical taxonomy for common vulnerabilities.

---

## Question 9: Server-side validation is still required when the UI already validates because…
**Answer: A** — Clients can be bypassed; the server is the trust boundary

**Outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

**Explanation:** Never trust the client. Validate again on the server.

---

## Question 10: A background worker token can drop production tables. What principle is violated?
**Answer: A** — Least privilege

**Outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

**Explanation:** Over-privileged tokens violate least privilege and are dangerous if leaked.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
