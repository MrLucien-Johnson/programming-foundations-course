# Go Intermediate — Module 02: Testing and Quality Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: On the test pyramid, which layer should usually be the largest (most numerous)?
**Checks outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

A) Manual-only exploratory tests  
B) Unit tests  
C) Full production canaries only  
D) UI screenshot tests for every line of code  

**Your answer:** _______________

---

### Question 2: You are unit-testing a pure pricing function. What should you usually avoid mocking?
**Checks outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

A) The function's own arithmetic  
B) An external payment HTTP API used by a different module  
C) A clock if the function under test does not use time  
D) Nothing — mock every name in scope  

**Your answer:** _______________

---

### Question 3: A test fails only when run after another test. What is the likely problem?
**Checks outcome 2:** Write deterministic unit tests using fixtures/factories and meaningful assertions.

A) The assertion is too meaningful  
B) Shared mutable state — the suite is not deterministic/isolated  
C) Coverage is above 90%  
D) The linter is too strict  

**Your answer:** _______________

---

### Question 4: Which assertion is stronger for `create_user(email)`?
**Checks outcome 2:** Write deterministic unit tests using fixtures/factories and meaningful assertions.

A) `assert result is not None`  
B) `assert result.email == email and result.id is not None`  
C) `assert True`  
D) `assert result` with no further checks  

**Your answer:** _______________

---

### Question 5: Which example is an integration test?
**Checks outcome 3:** Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process).

A) Calling a pure function with mocked everything including its own logic  
B) Hitting a real test database or HTTP endpoint and asserting the response  
C) Reading the source code without running it  
D) Running the formatter alone  

**Your answer:** _______________

---

### Question 6: Coverage reports 100%, but a bug still ships. What lesson fits?
**Checks outcome 4:** Interpret coverage as a signal — not a substitute for strong assertions.

A) Coverage guarantees correctness  
B) Coverage without meaningful assertions can still miss behavior  
C) You should delete all unit tests  
D) Only E2E tests ever matter  

**Your answer:** _______________

---

### Question 7: Why run lint/format/typecheck in CI as quality gates?
**Checks outcome 5:** Use lint, format, and typecheck as automated quality gates.

A) To replace unit tests entirely  
B) To catch style, bug-prone patterns, and type issues before merge  
C) To slow developers with no signal  
D) Only to generate prettier README screenshots  

**Your answer:** _______________

---

### Question 8: Your feature writes to Postgres. Which test strategy best proves the boundary works?
**Checks outcome 3:** Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process).

A) Mock the DB away and never talk to SQL  
B) An integration test against an isolated test schema/database  
C) Print SQL in a comment and skip running it  
D) Only type-check the ORM models  

**Your answer:** _______________

---

### Question 9: When is mocking an HTTP client appropriate in a unit test?
**Checks outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

A) Never  
B) When the code under test calls an external service and you want a fast, deterministic unit test  
C) When you want to avoid asserting anything  
D) When replacing the test runner itself  

**Your answer:** _______________

---

### Question 10: What is the main value of lint/format/typecheck gates in CI?
**Checks outcome 5:** Use lint, format, and typecheck as automated quality gates.

A) They replace all unit and integration tests  
B) They catch style, bug-prone patterns, and type issues before merge  
C) They exist only to slow developers with no signal  
D) They only generate prettier README screenshots  

**Your answer:** _______________

---

### Question 11: In this course's Go tooling, which command runs the test suite?
**Checks outcome 5:** Use lint, format, and typecheck as automated quality gates.

A) `go test ./...`  
B) `go fmt ./...`  
C) `git push --force`  
D) `docker system prune`  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **11/11 correct:** Excellent — you can apply this module's outcomes.
- **9-10 correct:** Strong — review the missed outcome(s).
- **0-8 correct:** Revisit the lessons for those outcomes, then retry.

---

**Good luck!** Check your answers when you are ready.
