# Java Advanced — Module 05: Reliability and Resilience Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Retrying immediately forever without jitter tends to…
**Checks outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

A) Heal dependencies gently  
B) Create synchronized retry storms that worsen outages  
C) Guarantee exactly-once  
D) Reduce error budgets automatically  

**Your answer:** _______________

---

### Question 2: A timeout without a retry budget means…
**Checks outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

A) You may still hammer a sick dependency indefinitely via client loops  
B) Reliability is solved  
C) CAP is fixed  
D) Caches never expire  

**Your answer:** _______________

---

### Question 3: A circuit breaker opens when…
**Checks outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

A) Error rates/latency cross a threshold, failing fast instead of calling the dependency  
B) The logo changes  
C) CI is green  
D) A single log line appears  

**Your answer:** _______________

---

### Question 4: Bulkheads help by…
**Checks outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

A) Sharing one thread pool for all workloads  
B) Isolating resources so one failure domain cannot exhaust another  
C) Removing rate limits  
D) Disabling AuthZ  

**Your answer:** _______________

---

### Question 5: Idempotency keys are most critical for…
**Checks outcome 3:** Use idempotency keys and dedupe to make retried writes safe.

A) Read-only GETs with no side effects  
B) Create/payment operations that clients may retry  
C) Static asset caching only  
D) Choosing font families  

**Your answer:** _______________

---

### Question 6: Deduping consumer messages by event ID prevents…
**Checks outcome 3:** Use idempotency keys and dedupe to make retried writes safe.

A) All network partitions  
B) Double-applying the same business effect after redelivery  
C) The need for schemas  
D) On-call rotations  

**Your answer:** _______________

---

### Question 7: A runbook should primarily contain…
**Checks outcome 4:** Write and follow runbooks for common incident classes.

A) Only motivational quotes  
B) Detection signals, mitigation steps, owners, and escalation paths  
C) Unrelated architecture trivia  
D) Passwords in plaintext  

**Your answer:** _______________

---

### Question 8: During an incident, the first reliability move is often…
**Checks outcome 4:** Write and follow runbooks for common incident classes.

A) Rewrite the platform  
B) Mitigate user impact (rollback, feature flag, degrade) then diagnose  
C) Delete metrics  
D) Disable communication  

**Your answer:** _______________

---

### Question 9: Rate limiting a dependency client protects…
**Checks outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

A) Only the marketing site fonts  
B) Both your service and the dependency from overload  
C) Nothing if retries exist  
D) Only disk encryption  

**Your answer:** _______________

---

### Question 10: Which retry policy is safest for non-idempotent POSTs without keys?
**Checks outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

A) Blind unlimited retries  
B) Fail clearly / get an idempotency key before retrying side effects  
C) Retry every microsecond  
D) Retry only on 200 OK  

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
