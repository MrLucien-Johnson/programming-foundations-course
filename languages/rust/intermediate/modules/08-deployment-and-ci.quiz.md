# Rust Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## Instructions

Answer these questions about what you've learned. Try to answer from memory first!

## Questions

### Question 1: You need to run the test suite. Which command should you use?
A) Use tooling to keep quality high: rustfmt + clippy.  
B) `cargo test`  
C) Document decisions and constraints clearly for reviewers.  
D) `cargo clippy`  

**Your answer:** _______________

---

### Question 2: You need to run lint checks. Which command should you use?
A) Over-mocking (tests assert implementation details instead of outcomes).  
B) `cargo clippy`  
C) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.  
D) Environments + configuration (35 min)  

**Your answer:** _______________

---

### Question 3: You need to format the code. Which command should you use?
A) If the module involves a database, tests must run against an isolated schema/database.  
B) `cargo fmt`  
C) `cargo clippy`  
D) Containerize, configure, and deploy with automated CI checks.  

**Your answer:** _______________

---

### Question 4: Which action best satisfies the Core requirements?
A) Implement a small feature tied to this module in an existing starter app.  
B) Making performance claims without measurements.  
C) Document rollback steps and environment variables.  
D) Run: `cargo test`  

**Your answer:** _______________

---

### Question 5: Which action upgrades the work to the Better level?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  
B) Review the module goals and plan how you will ship safely with automation.  
C) Treat every request as safe without review.  
D) Skipping input validation and assuming “happy path”.  

**Your answer:** _______________

---

### Question 6: Which action qualifies as a Beast Mode upgrade?
A) Add a performance or reliability improvement and **measure** the impact.  
B) Shipping without an automated test run in CI.  
C) Explain the core concepts and tradeoffs for **Deployment and CI**.  
D) Containerize, configure, and deploy with automated CI checks.  

**Your answer:** _______________

---

### Question 7: Before submitting, which verification step must you complete?
A) Containerize, configure, and deploy with automated CI checks.  
B) Write tests that prove correctness and prevent regressions.  
C) Run the module tests and confirm they pass.  
D) Ship changes without documentation.  

**Your answer:** _______________

---

### Question 8: Which testing requirement must be satisfied to pass?
A) Document decisions and constraints clearly for reviewers.  
B) All work must be covered by **fmt + clippy + tests in CI**.  
C) Update the README with setup, run, and test commands.  
D) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).  

**Your answer:** _______________

---

### Question 9: Which option would be a common mistake to avoid?
A) Shipping without an automated test run in CI.  
B) Update the README with setup, run, and test commands.  
C) Write tests that prove correctness and prevent regressions.  
D) Add a performance or reliability improvement and **measure** the impact.  

**Your answer:** _______________

---

### Question 10: A reviewer asks what capability you demonstrated. Which outcome matches?
A) Verify the primary feature works with normal and edge-case inputs.  
B) Add at least **3 focused unit tests** that cover normal cases and edge cases.  
C) Document decisions in a short README section (assumptions, tradeoffs, next steps).  
D) Explain the core concepts and tradeoffs for **Deployment and CI**.  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **10/10 correct:** Excellent! You understand the module well.
- **8-9 correct:** Great work! Review what you missed.
- **0-7 correct:** Review the module and try again.

---

**Good luck!** Check your answers when you are ready.