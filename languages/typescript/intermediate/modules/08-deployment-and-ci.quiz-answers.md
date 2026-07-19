# TypeScript Intermediate — Module 08: Deployment and CI Quiz Answers

## Question 1: Why keep production config/secrets out of the container image?
**Answer: B** — Images get copied widely — secrets belong in env/secret injection at runtime

**Outcome 1:** Separate environments and configuration (dev/stage/prod) without baking secrets into images.

**Explanation:** Build once; inject config/secrets per environment at run time.

---

## Question 2: Dev and prod should differ mainly by…
**Answer: B** — Configuration/data — not “works on my machine” snowflake setups

**Outcome 1:** Separate environments and configuration (dev/stage/prod) without baking secrets into images.

**Explanation:** Environment parity + config separation reduces deploy surprises.

---

## Question 3: Containers help CI/local work by…
**Answer: B** — Packaging dependencies so runs are more reproducible across machines

**Outcome 2:** Use containers to make local and CI environments reproducible.

**Explanation:** Containers shrink “works on my machine” gaps.

---

## Question 4: Why cache dependencies in CI?
**Answer: B** — To speed pipelines by reusing downloaded packages between runs

**Outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

**Explanation:** Caching cuts install time; still invalidate when locks change.

---

## Question 5: A CI matrix is useful when you need to…
**Answer: A** — Run the same checks across versions/platforms (e.g., 3.11 and 3.12)

**Outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

**Explanation:** Matrices fan out jobs across dimensions you care about.

---

## Question 6: CI artifacts are typically used to…
**Answer: A** — Publish build outputs (wheels, images metadata, coverage reports) for later jobs/humans

**Outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

**Explanation:** Artifacts pass outputs between jobs or retain reports.

---

## Question 7: What is a health check for in deployment?
**Answer: B** — Letting the platform know whether the new instance is ready to receive traffic

**Outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

**Explanation:** Health checks gate traffic until the service is actually ready.

---

## Question 8: Before a migration that might fail in production, you should have…
**Answer: B** — A tested forward path and a rollback/mitigation plan

**Outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

**Explanation:** Safe deploys pair migrations with rollback thinking.

---

## Question 9: A bad deploy is live. What does a rollback plan enable?
**Answer: A** — Faster return to a known-good version while you diagnose

**Outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

**Explanation:** Rollback limits user impact when a release is bad.

---

## Question 10: Why run the same container image in CI tests and staging when possible?
**Answer: B** — To test what you actually ship

**Outcome 2:** Use containers to make local and CI environments reproducible.

**Explanation:** Testing the shippable artifact catches packaging mistakes early.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
