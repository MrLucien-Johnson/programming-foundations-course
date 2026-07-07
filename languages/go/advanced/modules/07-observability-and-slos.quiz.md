# Go Advanced — Module 07: Observability and SLOs Quiz: Test Your Understanding

## Instructions

Answer these questions about what you've learned. Try to answer from memory first!

## Questions

### Question 1: You need to run the test suite. Which command should you use?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  
B) Jump to the next module without verifying results.  
C) Instrument systems and run them with SLO-based operations.  
D) `go test ./...`  

**Your answer:** _______________

---

### Question 2: You need to run lint checks. Which command should you use?
A) Run: `golangci-lint run`  
B) `golangci-lint run`  
C) All work must be covered by **gofmt + lint + tests in CI**.  
D) `go test ./...`  

**Your answer:** _______________

---

### Question 3: You need to format the code. Which command should you use?
A) `gofmt -w .`  
B) Alerting strategy + on-call hygiene (35 min)  
C) Run: `golangci-lint run`  
D) Run: `go test ./...`  

**Your answer:** _______________

---

### Question 4: Which action best satisfies the Core requirements?
A) Copy the starter pack from `languages/go/advanced/starter-pack` into a new working folder.  
B) Implement a small feature tied to this module in an existing starter app.  
C) Skipping input validation and assuming “happy path”.  
D) If the module involves a database, tests must run against an isolated schema/database.  

**Your answer:** _______________

---

### Question 5: Which action upgrades the work to the Better level?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).  
B) Metrics: RED/USE and cardinality pitfalls (45 min)  
C) Making performance claims without measurements.  
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  

**Your answer:** _______________

---

### Question 6: Which action qualifies as a Beast Mode upgrade?
A) Refactor one area for readability (without changing behavior) and prove it with tests.  
B) Add a performance or reliability improvement and **measure** the impact.  
C) Change multiple variables at once so you cannot compare outcomes.  
D) Over-mocking (tests assert implementation details instead of outcomes).  

**Your answer:** _______________

---

### Question 7: Before submitting, which verification step must you complete?
A) Run the module tests and confirm they pass.  
B) Ship changes without documentation.  
C) Document decisions in a short README section (assumptions, tradeoffs, next steps).  
D) Use tooling to keep quality high: gofmt + golangci-lint.  

**Your answer:** _______________

---

### Question 8: Which testing requirement must be satisfied to pass?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.  
B) Jump to the next module without verifying results.  
C) All work must be covered by **gofmt + lint + tests in CI**.  
D) Ignore error handling for edge cases.  

**Your answer:** _______________

---

### Question 9: Which option would be a common mistake to avoid?
A) Update the README with setup, run, and test commands.  
B) Define SLIs and SLO targets for one critical path.  
C) Run: `gofmt -w .`  
D) Shipping without an automated test run in CI.  

**Your answer:** _______________

---

### Question 10: A reviewer asks what capability you demonstrated. Which outcome matches?
A) Shipping without an automated test run in CI.  
B) Tracing: spans, context propagation (45 min)  
C) Explain the core concepts and tradeoffs for **Observability and SLOs**.  
D) Define SLIs and SLO targets for one critical path.  

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