# go / intermediate — Quiz Alignment Sheet

Codecademy-style mapping: each learning outcome is tested by at least one quiz item.

Track: `languages/go/intermediate/modules/`

## 01-dsa-practical

| Outcome | Quiz questions |
|---|---|
| LO1: Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff. | Q1, Q2, Q10 |
| LO2: Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem. | Q3, Q4 |
| LO3: Decide when the language's built-in sort/search is enough versus writing a custom approach. | Q5 |
| LO4: Apply memoization or an LRU cache when recomputation is the bottleneck. | Q6, Q7 |
| LO5: Measure a change with a micro-benchmark and explain when profiling is the better tool. | Q8, Q9 |

## 02-testing-and-quality

| Outcome | Quiz questions |
|---|---|
| LO1: Place tests on the test pyramid and choose what to mock versus what to hit for real. | Q1, Q2, Q9 |
| LO2: Write deterministic unit tests using fixtures/factories and meaningful assertions. | Q3, Q4 |
| LO3: Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process). | Q5, Q8 |
| LO4: Interpret coverage as a signal — not a substitute for strong assertions. | Q6 |
| LO5: Use lint, format, and typecheck as automated quality gates. | Q7, Q10, Q11 |

## 03-git-and-collaboration

| Outcome | Quiz questions |
|---|---|
| LO1: Use a clear branching strategy and write commits that explain why a change happened. | Q1, Q2, Q9 |
| LO2: Open and review pull requests using a practical checklist and actionable feedback. | Q3, Q4, Q10 |
| LO3: Resolve merge conflicts and rebase safely without rewriting shared history carelessly. | Q5, Q6 |
| LO4: Diagnose CI failures from logs and fix the underlying issue before merging. | Q7, Q8 |

## 04-apis-and-auth

| Outcome | Quiz questions |
|---|---|
| LO1: Design REST endpoints with clear resources, status codes, and pagination. | Q1, Q2, Q10 |
| LO2: Validate input and return consistent error envelopes for clients. | Q3, Q9 |
| LO3: Distinguish authentication from authorization and apply sessions/JWT/roles appropriately. | Q4, Q5, Q6 |
| LO4: Add basic rate limiting / abuse protections to sensitive endpoints. | Q7 |
| LO5: Document the API with OpenAPI (or equivalent) including examples. | Q8 |

## 05-databases

| Outcome | Quiz questions |
|---|---|
| LO1: Design schemas with constraints that protect data integrity. | Q1, Q2 |
| LO2: Write forward/backwards-safe migrations and apply them carefully. | Q3, Q9 |
| LO3: Use transactions and reason about basic isolation needs. | Q4, Q10 |
| LO4: Choose indexes and read query plans to fix slow queries. | Q5, Q6 |
| LO5: Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries). | Q7, Q8 |

## 06-security-basics

| Outcome | Quiz questions |
|---|---|
| LO1: Map real application risks to the OWASP Top 10 categories. | Q1, Q8 |
| LO2: Store and load secrets via config/secret managers — never commit them. | Q2, Q7 |
| LO3: Prevent injection using validation, encoding, and parameterized queries. | Q3, Q4, Q9 |
| LO4: Enforce authorization checks with least privilege on every sensitive action. | Q5, Q6, Q10 |

## 07-debugging-and-performance

| Outcome | Quiz questions |
|---|---|
| LO1: Follow a reproduce → isolate → fix debugging workflow with evidence. | Q1, Q2, Q8 |
| LO2: Use logging and basic tracing to locate failures in running systems. | Q3, Q7 |
| LO3: Profile CPU and memory to find real hotspots before optimizing. | Q4, Q5, Q10 |
| LO4: Improve database performance using slow-query analysis and indexes. | Q6, Q9 |

## 08-deployment-and-ci

| Outcome | Quiz questions |
|---|---|
| LO1: Separate environments and configuration (dev/stage/prod) without baking secrets into images. | Q1, Q2 |
| LO2: Use containers to make local and CI environments reproducible. | Q3, Q10 |
| LO3: Design CI pipelines with caching, matrices, and artifacts where they help. | Q4, Q5, Q6 |
| LO4: Deploy with health checks, safe migrations, and a rollback plan. | Q7, Q8, Q9 |

## core-concepts

| Outcome | Quiz questions |
|---|---|
| LO1: Model data idiomatically with clear types and boundaries. | Q1, Q5, Q8 |
| LO2: Handle errors in a way that is debuggable and safe for callers. | Q2, Q6, Q9 |
| LO3: Design modules that are testable without hidden global state. | Q3, Q4, Q7, Q10 |
