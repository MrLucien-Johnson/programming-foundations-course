# Kotlin Intermediate — Module 05: Databases Quiz Answers

## Question 1: You need emails to be unique per user. Where should that rule live primarily?
**Answer: B** — As a database unique constraint (and validated in the app)

**Outcome 1:** Design schemas with constraints that protect data integrity.

**Explanation:** Integrity constraints in the DB enforce rules even if app code misses a check.

---

## Question 2: A foreign key constraint helps by…
**Answer: B** — Preventing orphan rows that reference missing parents

**Outcome 1:** Design schemas with constraints that protect data integrity.

**Explanation:** FKs preserve referential integrity between tables.

---

## Question 3: What makes a migration safer to ship?
**Answer: B** — A reviewed migration that is expandable/rollback-aware and tested on a copy first

**Outcome 2:** Write forward/backwards-safe migrations and apply them carefully.

**Explanation:** Migrations should be reviewed, tested, and have a safety/rollback story.

---

## Question 4: Why wrap multi-step money transfers in a transaction?
**Answer: A** — So partial updates cannot leave balances inconsistent if a step fails

**Outcome 3:** Use transactions and reason about basic isolation needs.

**Explanation:** Transactions commit all-or-nothing for a unit of work.

---

## Question 5: A query filters frequently on `orders.user_id` and is slow. First database lever?
**Answer: A** — Add an appropriate index on `user_id` (and verify with the query plan)

**Outcome 4:** Choose indexes and read query plans to fix slow queries.

**Explanation:** Indexes + EXPLAIN/query plans are the core performance tools in this module.

---

## Question 6: What does reading a query plan help you see?
**Answer: B** — Whether the database uses indexes, scans, joins, and costly steps

**Outcome 4:** Choose indexes and read query plans to fix slow queries.

**Explanation:** Plans show how the engine executes SQL so you can fix real bottlenecks.

---

## Question 7: What is the N+1 query problem?
**Answer: B** — Running one query, then one extra query per returned row (often via lazy ORM loads)

**Outcome 5:** Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries).

**Explanation:** N+1 is a classic ORM pitfall — fix with joins/eager loading/batch queries.

---

## Question 8: An ORM call loads an entire table into memory without a limit. Risk?
**Answer: B** — Unbounded queries can exhaust memory and crush latency

**Outcome 5:** Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries).

**Explanation:** Always bound list queries (pagination/limits) in real systems.

---

## Question 9: Why prefer expandable migrations over rewrite-in-place of historical migration files already applied?
**Answer: A** — History already applied in other environments will diverge and break deploys

**Outcome 2:** Write forward/backwards-safe migrations and apply them carefully.

**Explanation:** Applied migrations are history; change forward with new migrations.

---

## Question 10: Isolation levels mainly trade off between…
**Answer: B** — Consistency vs concurrency anomalies/performance

**Outcome 3:** Use transactions and reason about basic isolation needs.

**Explanation:** Stronger isolation reduces anomalies but can reduce throughput; pick what the use case needs.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
