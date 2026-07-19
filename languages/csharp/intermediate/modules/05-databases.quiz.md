# C# Intermediate — Module 05: Databases Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: You need emails to be unique per user. Where should that rule live primarily?
**Checks outcome 1:** Design schemas with constraints that protect data integrity.

A) Only in a comment in the README  
B) As a database unique constraint (and validated in the app)  
C) Only in the UI's placeholder text  
D) In a spreadsheet outside the repo  

**Your answer:** _______________

---

### Question 2: A foreign key constraint helps by…
**Checks outcome 1:** Design schemas with constraints that protect data integrity.

A) Speeding up CSS  
B) Preventing orphan rows that reference missing parents  
C) Removing the need for indexes forever  
D) Encrypting backups automatically  

**Your answer:** _______________

---

### Question 3: What makes a migration safer to ship?
**Checks outcome 2:** Write forward/backwards-safe migrations and apply them carefully.

A) Editing production data by hand with no script  
B) A reviewed migration that is expandable/rollback-aware and tested on a copy first  
C) Dropping columns in peak traffic without a plan  
D) Storing the SQL only in chat history  

**Your answer:** _______________

---

### Question 4: Why wrap multi-step money transfers in a transaction?
**Checks outcome 3:** Use transactions and reason about basic isolation needs.

A) So partial updates cannot leave balances inconsistent if a step fails  
B) Because SQL forbids single statements  
C) To disable foreign keys  
D) To skip indexes  

**Your answer:** _______________

---

### Question 5: A query filters frequently on `orders.user_id` and is slow. First database lever?
**Checks outcome 4:** Choose indexes and read query plans to fix slow queries.

A) Add an appropriate index on `user_id` (and verify with the query plan)  
B) Buy a new laptop for the developer  
C) Remove the WHERE clause  
D) Store all orders in a single JSON file  

**Your answer:** _______________

---

### Question 6: What does reading a query plan help you see?
**Checks outcome 4:** Choose indexes and read query plans to fix slow queries.

A) Only the author's favorite color  
B) Whether the database uses indexes, scans, joins, and costly steps  
C) The editor color theme  
D) Git blame for the migration file  

**Your answer:** _______________

---

### Question 7: What is the N+1 query problem?
**Checks outcome 5:** Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries).

A) Using one query total for the whole app  
B) Running one query, then one extra query per returned row (often via lazy ORM loads)  
C) Having exactly eleven tables  
D) A migration with eleven steps  

**Your answer:** _______________

---

### Question 8: An ORM call loads an entire table into memory without a limit. Risk?
**Checks outcome 5:** Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries).

A) None — memory is infinite  
B) Unbounded queries can exhaust memory and crush latency  
C) It improves indexes automatically  
D) It deletes constraints  

**Your answer:** _______________

---

### Question 9: Why prefer expandable migrations over rewrite-in-place of historical migration files already applied?
**Checks outcome 2:** Write forward/backwards-safe migrations and apply them carefully.

A) History already applied in other environments will diverge and break deploys  
B) Git cannot store SQL  
C) Databases ignore schemas  
D) Rollback is illegal in SQL  

**Your answer:** _______________

---

### Question 10: Isolation levels mainly trade off between…
**Checks outcome 3:** Use transactions and reason about basic isolation needs.

A) Font size and line height  
B) Consistency vs concurrency anomalies/performance  
C) IPv4 and IPv6  
D) JWT and sessions only  

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
