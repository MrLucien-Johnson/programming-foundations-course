# Swift Advanced — Module 03: Concurrency and Async Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Two threads increment the same counter without synchronization. Result?
**Checks outcome 1:** Identify race conditions and choose safe synchronization or ownership patterns.

A) Always perfectly accurate counts  
B) A race: lost updates are possible  
C) Automatic database indexing  
D) CAP becoming irrelevant  

**Your answer:** _______________

---

### Question 2: Which approach often prevents races better than sprinkling locks everywhere?
**Checks outcome 1:** Identify race conditions and choose safe synchronization or ownership patterns.

A) Sharing more mutable globals  
B) Owning data per task/actor and communicating by messages  
C) Disabling tests  
D) Sleeping randomly longer  

**Your answer:** _______________

---

### Question 3: An unbounded in-memory queue under load typically causes…
**Checks outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

A) Perfect backpressure  
B) Memory growth and eventual collapse  
C) Faster GC forever  
D) Stronger consistency  

**Your answer:** _______________

---

### Question 4: Backpressure means…
**Checks outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

A) Producers keep sending at full speed no matter what  
B) Consumers/signals slow or block producers when buffers fill  
C) Deleting metrics  
D) Turning off timeouts  

**Your answer:** _______________

---

### Question 5: Why set timeouts on outbound calls?
**Checks outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

A) To guarantee success  
B) To bound wait time when dependencies hang  
C) Because retries are illegal  
D) To increase cardinality of every metric  

**Your answer:** _______________

---

### Question 6: Structured concurrency encourages…
**Checks outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

A) Fire-and-forget tasks with no parent ownership  
B) Parent scopes that cancel/wait for child tasks cleanly  
C) Ignoring cancellation forever  
D) Sharing one global mutable list for all jobs  

**Your answer:** _______________

---

### Question 7: “Exactly-once delivery” across unreliable networks is…
**Checks outcome 4:** Design for at-least-once delivery and idempotent handlers — not mythical exactly-once.

A) Trivial if you enable a checkbox  
B) Effectively achieved via idempotent processing of at-least-once deliveries  
C) Guaranteed by UDP  
D) Unnecessary if you use JSON  

**Your answer:** _______________

---

### Question 8: An idempotency key on a payment create endpoint helps when…
**Checks outcome 4:** Design for at-least-once delivery and idempotent handlers — not mythical exactly-once.

A) The client retries after a timeout and might double-charge  
B) You want to skip AuthZ  
C) Caches should never expire  
D) You delete audit logs  

**Your answer:** _______________

---

### Question 9: A worker pool of size N with a bounded queue of size M is full. A good policy is…
**Checks outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

A) Allocate infinite threads silently  
B) Reject, block, or shed load with a clear signal  
C) Drop ACLs  
D) Disable health checks  

**Your answer:** _______________

---

### Question 10: A cancelled request should ideally…
**Checks outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

A) Keep running forever consuming CPU/DB  
B) Propagate cancellation so downstream work stops promptly  
C) Delete the database schema  
D) Raise cardinality of user-id labels  

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
