# TypeScript Advanced — Module 01: System Design Foundations

## Overview
Reason about scalability, data, and tradeoffs under constraints.

This module uses **Node.js LTS**, **npm (or pnpm), TypeScript compiler (tsc)**, and **Vitest (or Jest)**. When applicable, you’ll build or extend a small service using **Fastify (or Express) for REST APIs** and **PostgreSQL + migrations (Prisma or Knex)**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **System Design Foundations**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: ESLint + Prettier.
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **TypeScript**.
- Able to run a local project in this environment: **Node.js LTS**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose for local Postgres).

## Lessons
1) Requirements → constraints → estimates (60 min)
2) Caching, load balancing, and data partitions (60 min)
3) Consistency models + CAP in practice (55 min)
4) Queues, streams, and asynchronous workflows (55 min)

## Exercises
### Core
- Implement a small feature tied to this module in an existing starter app.
- Add at least **3 focused unit tests** that cover normal cases and edge cases.
- Add or update documentation (README notes or ADR-style notes).

### Better
- Add an integration test that hits a real boundary (HTTP, database, file system, or process).
- Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.
- Refactor one area for readability (without changing behavior) and prove it with tests.

### Beast Mode
- Add a performance or reliability improvement and **measure** the impact.
- Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).
- Create a short write-up: what changed, why, and how you verified it.

## Mini-Project
### Brief
Build a small, production-leaning feature or service slice that showcases **System Design Foundations** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **typecheck + lint + unit tests + integration tests (HTTP + DB) in CI**.
- Tests must be deterministic (no flakes) and runnable by a reviewer.
- If the module involves a database, tests must run against an isolated schema/database.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Feature works and handles common cases | Handles edge cases and failure modes with tests |
| Test quality | Tests pass and are readable | Strong boundaries, good fixtures, meaningful assertions |
| Code quality | Lint/format clean, clear naming | Clean architecture choices with justified tradeoffs |
| Documentation | Setup + usage documented | Includes rationale, diagrams, or ADR-style notes |

## Common Mistakes
- Shipping without an automated test run in CI.
- Over-mocking (tests assert implementation details instead of outcomes).
- Skipping input validation and assuming “happy path”.
- Making performance claims without measurements.

## Stretch Resources
- (Add links to official docs, talks, and reference implementations.)
- (Add 1–2 curated articles that deepen understanding.)
