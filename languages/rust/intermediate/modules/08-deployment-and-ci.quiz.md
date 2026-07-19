# Rust Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Why keep production config/secrets out of the container image?
**Checks outcome 1:** Separate environments and configuration (dev/stage/prod) without baking secrets into images.

A) Images are never stored anywhere  
B) Images get copied widely — secrets belong in env/secret injection at runtime  
C) Kubernetes forbids environment variables  
D) Config never changes between environments  

**Your answer:** _______________

---

### Question 2: Dev and prod should differ mainly by…
**Checks outcome 1:** Separate environments and configuration (dev/stage/prod) without baking secrets into images.

A) Completely different undocumented codepaths with no parity  
B) Configuration/data — not “works on my machine” snowflake setups  
C) Disabling HTTPS only in prod  
D) Skipping tests only in prod  

**Your answer:** _______________

---

### Question 3: Containers help CI/local work by…
**Checks outcome 2:** Use containers to make local and CI environments reproducible.

A) Guaranteeing marketing copy is correct  
B) Packaging dependencies so runs are more reproducible across machines  
C) Removing the need for tests  
D) Making rollbacks impossible  

**Your answer:** _______________

---

### Question 4: Why cache dependencies in CI?
**Checks outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

A) To hide failing tests  
B) To speed pipelines by reusing downloaded packages between runs  
C) To avoid ever updating libraries  
D) To store production secrets in the cache  

**Your answer:** _______________

---

### Question 5: A CI matrix is useful when you need to…
**Checks outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

A) Run the same checks across versions/platforms (e.g., 3.11 and 3.12)  
B) Deploy on every keystroke to production  
C) Skip linting forever  
D) Store passwords in artifacts  

**Your answer:** _______________

---

### Question 6: CI artifacts are typically used to…
**Checks outcome 3:** Design CI pipelines with caching, matrices, and artifacts where they help.

A) Publish build outputs (wheels, images metadata, coverage reports) for later jobs/humans  
B) Replace git remotes  
C) Bypass code review  
D) Disable health checks  

**Your answer:** _______________

---

### Question 7: What is a health check for in deployment?
**Checks outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

A) A cosmetic README badge only  
B) Letting the platform know whether the new instance is ready to receive traffic  
C) Deleting the database nightly  
D) Formatting source files  

**Your answer:** _______________

---

### Question 8: Before a migration that might fail in production, you should have…
**Checks outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

A) No plan  
B) A tested forward path and a rollback/mitigation plan  
C) Only a screenshot of local success  
D) Force-push to main during peak traffic  

**Your answer:** _______________

---

### Question 9: A bad deploy is live. What does a rollback plan enable?
**Checks outcome 4:** Deploy with health checks, safe migrations, and a rollback plan.

A) Faster return to a known-good version while you diagnose  
B) Permanent data corruption as a feature  
C) Skipping blameless review forever  
D) Turning off monitoring  

**Your answer:** _______________

---

### Question 10: Why run the same container image in CI tests and staging when possible?
**Checks outcome 2:** Use containers to make local and CI environments reproducible.

A) To maximize environment drift  
B) To test what you actually ship  
C) Because registries reject tags  
D) To avoid writing Dockerfiles with any base image  

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
