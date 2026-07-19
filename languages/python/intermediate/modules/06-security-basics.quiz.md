# Python Intermediate — Module 06: Security Basics Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Broken access control in OWASP terms is closest to…
**Checks outcome 1:** Map real application risks to the OWASP Top 10 categories.

A) Users performing actions outside their permissions  
B) Using a slow CSS animation  
C) Having too many unit tests  
D) Formatting code with the linter  

**Your answer:** _______________

---

### Question 2: Where should a production database password live?
**Checks outcome 2:** Store and load secrets via config/secret managers — never commit them.

A) Committed in the repo as `password.txt`  
B) In environment/config or a secret manager, not in source control  
C) Hard-coded in a public frontend bundle  
D) In a screenshot in the PR  

**Your answer:** _______________

---

### Question 3: Which query style best prevents SQL injection?
**Checks outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

A) String-concatenating raw user input into SQL  
B) Parameterized queries / bound parameters  
C) Disabling the database firewall only  
D) Lowercasing the input and hoping  

**Your answer:** _______________

---

### Question 4: Showing user-provided HTML in a page without encoding risks…
**Checks outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

A) XSS (cross-site scripting)  
B) Faster CSS  
C) Automatic indexing  
D) Stronger passwords  

**Your answer:** _______________

---

### Question 5: Least privilege means…
**Checks outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

A) Every user is admin for convenience  
B) Grant only the permissions required for a role/task — nothing more  
C) Disable AuthZ after login  
D) Share one service account everywhere including CI screenshots  

**Your answer:** _______________

---

### Question 6: After AuthN succeeds, what must still happen before deleting a billing record?
**Checks outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

A) Nothing — login is enough for all actions  
B) An AuthZ check that this identity may delete that record  
C) A CSS theme switch  
D) Disabling HTTPS  

**Your answer:** _______________

---

### Question 7: A secret was accidentally committed. Best immediate response?
**Checks outcome 2:** Store and load secrets via config/secret managers — never commit them.

A) Leave it; git history is private forever on the internet  
B) Rotate/revoke the secret, remove it from the tree, and treat history as compromised  
C) Rename the variable only  
D) Add more comments  

**Your answer:** _______________

---

### Question 8: Why map bugs to OWASP categories during review?
**Checks outcome 1:** Map real application risks to the OWASP Top 10 categories.

A) To sound fancy without changing code  
B) To prioritize fixes using a shared language for common web risks  
C) Because OWASP replaces tests  
D) To avoid writing error messages  

**Your answer:** _______________

---

### Question 9: Server-side validation is still required when the UI already validates because…
**Checks outcome 3:** Prevent injection using validation, encoding, and parameterized queries.

A) Clients can be bypassed; the server is the trust boundary  
B) Browsers cannot send HTTP  
C) Databases reject all input automatically  
D) OpenAPI makes validation unnecessary  

**Your answer:** _______________

---

### Question 10: A background worker token can drop production tables. What principle is violated?
**Checks outcome 4:** Enforce authorization checks with least privilege on every sensitive action.

A) Least privilege  
B) Pagination  
C) Big-O notation  
D) Semantic versioning only  

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
