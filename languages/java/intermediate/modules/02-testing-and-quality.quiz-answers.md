# Java Intermediate — Module 02: Testing and Quality Quiz Answers

## Question 1: On the test pyramid, which layer should usually be the largest (most numerous)?
**Answer: B** — Unit tests

**Outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

**Explanation:** Unit tests are fast and numerous; integration/E2E are fewer and slower.

---

## Question 2: You are unit-testing a pure pricing function. What should you usually avoid mocking?
**Answer: A** — The function's own arithmetic

**Outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

**Explanation:** Don't mock the behavior you are trying to prove. Mock slow/external boundaries, not the subject itself.

---

## Question 3: A test fails only when run after another test. What is the likely problem?
**Answer: B** — Shared mutable state — the suite is not deterministic/isolated

**Outcome 2:** Write deterministic unit tests using fixtures/factories and meaningful assertions.

**Explanation:** Order-dependent failures usually mean leaked global/DB/file state. Tests must isolate and reset fixtures.

---

## Question 4: Which assertion is stronger for `create_user(email)`?
**Answer: B** — `assert result.email == email and result.id is not None`

**Outcome 2:** Write deterministic unit tests using fixtures/factories and meaningful assertions.

**Explanation:** Meaningful assertions check observable outcomes, not merely “something happened.”

---

## Question 5: Which example is an integration test?
**Answer: B** — Hitting a real test database or HTTP endpoint and asserting the response

**Outcome 3:** Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process).

**Explanation:** Integration tests cross a real boundary (HTTP/DB/etc.), not just in-memory mocks of the unit.

---

## Question 6: Coverage reports 100%, but a bug still ships. What lesson fits?
**Answer: B** — Coverage without meaningful assertions can still miss behavior

**Outcome 4:** Interpret coverage as a signal — not a substitute for strong assertions.

**Explanation:** Coverage shows what ran, not whether you asserted the right outcomes.

---

## Question 7: Why run lint/format/typecheck in CI as quality gates?
**Answer: B** — To catch style, bug-prone patterns, and type issues before merge

**Outcome 5:** Use lint, format, and typecheck as automated quality gates.

**Explanation:** Automated gates keep a consistent baseline so humans review design and behavior.

---

## Question 8: Your feature writes to Postgres. Which test strategy best proves the boundary works?
**Answer: B** — An integration test against an isolated test schema/database

**Outcome 3:** Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process).

**Explanation:** DB behavior needs an isolated real (or close-to-real) boundary — not only mocks.

---

## Question 9: When is mocking an HTTP client appropriate in a unit test?
**Answer: B** — When the code under test calls an external service and you want a fast, deterministic unit test

**Outcome 1:** Place tests on the test pyramid and choose what to mock versus what to hit for real.

**Explanation:** Mock external I/O for unit speed/determinism; still keep some integration tests that hit real boundaries.

---

## Question 10: What is the main value of lint/format/typecheck gates in CI?
**Answer: B** — They catch style, bug-prone patterns, and type issues before merge

**Outcome 5:** Use lint, format, and typecheck as automated quality gates.

**Explanation:** Automated quality gates keep a consistent baseline so humans review design and behavior.

---

## Question 11: In this course's Java tooling, which command typically runs unit tests (Maven)?
**Answer: A** — `mvn test`

**Outcome 5:** Use lint, format, and typecheck as automated quality gates.

**Explanation:** `mvn test` (or the Gradle equivalent) is the standard unit-test gate.

---

## How Did You Do?

- **11/11 correct:** Excellent! You are ready to move on.
- **9-10 correct:** Great work — review the missed outcomes.
- **0-8 correct:** Revisit the module lessons, then try again.
