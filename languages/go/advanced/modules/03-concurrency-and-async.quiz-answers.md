# Go Advanced — Module 03: Concurrency and Async Quiz Answers

## Question 1: Two threads increment the same counter without synchronization. Result?
**Answer: B** — A race: lost updates are possible

**Outcome 1:** Identify race conditions and choose safe synchronization or ownership patterns.

**Explanation:** Unsycned shared mutable state races; use atomics/locks/ownership.

---

## Question 2: Which approach often prevents races better than sprinkling locks everywhere?
**Answer: B** — Owning data per task/actor and communicating by messages

**Outcome 1:** Identify race conditions and choose safe synchronization or ownership patterns.

**Explanation:** Isolation/ownership removes shared-mutation races at the design level.

---

## Question 3: An unbounded in-memory queue under load typically causes…
**Answer: B** — Memory growth and eventual collapse

**Outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

**Explanation:** Bound queues; apply backpressure or drop/shed load deliberately.

---

## Question 4: Backpressure means…
**Answer: B** — Consumers/signals slow or block producers when buffers fill

**Outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

**Explanation:** Backpressure protects the system by limiting in-flight work.

---

## Question 5: Why set timeouts on outbound calls?
**Answer: B** — To bound wait time when dependencies hang

**Outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

**Explanation:** Timeouts stop hung dependencies from holding resources forever.

---

## Question 6: Structured concurrency encourages…
**Answer: B** — Parent scopes that cancel/wait for child tasks cleanly

**Outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

**Explanation:** Parents own lifetimes so cancellation and errors propagate predictably.

---

## Question 7: “Exactly-once delivery” across unreliable networks is…
**Answer: B** — Effectively achieved via idempotent processing of at-least-once deliveries

**Outcome 4:** Design for at-least-once delivery and idempotent handlers — not mythical exactly-once.

**Explanation:** Networks duplicate; make handlers idempotent and dedupe.

---

## Question 8: An idempotency key on a payment create endpoint helps when…
**Answer: A** — The client retries after a timeout and might double-charge

**Outcome 4:** Design for at-least-once delivery and idempotent handlers — not mythical exactly-once.

**Explanation:** Retries + side effects need dedupe via idempotency keys.

---

## Question 9: A worker pool of size N with a bounded queue of size M is full. A good policy is…
**Answer: B** — Reject, block, or shed load with a clear signal

**Outcome 2:** Apply backpressure with bounded queues so producers cannot overwhelm consumers.

**Explanation:** Saturation needs an explicit policy — not unbounded growth.

---

## Question 10: A cancelled request should ideally…
**Answer: B** — Propagate cancellation so downstream work stops promptly

**Outcome 3:** Use timeouts, cancellation, and structured concurrency to bound work lifetimes.

**Explanation:** Cancellation frees resources and protects dependencies.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
