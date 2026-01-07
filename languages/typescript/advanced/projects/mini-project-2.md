# TypeScript Advanced — Mini Project 2: Async Worker + Idempotency

## Overview
- **Goal**: Add an async pipeline (queue/worker) with idempotency, retries, and observability basics.
- **Expected effort**: 2–3 days

## Brief
Build the deliverable using idiomatic tools for **TypeScript**:
- npm (or pnpm), TypeScript compiler (tsc)
- Vitest (or Jest)
- Fastify (or Express) for REST APIs
- PostgreSQL + migrations (Prisma or Knex)

## Requirements
- Clear README with setup + run steps
- Tests for core behavior
- Consistent style and quality gates

## Acceptance Criteria
- Runs locally with reproducible steps.
- Includes a minimal but meaningful test suite.
- Includes clear API/interface documentation (routes, queries, or function contracts).
- Uses consistent formatting and passes CI-style checks.

## Testing Requirements
- Automated tests must run via a single command documented in the README.
- Include at least one test that crosses a boundary (HTTP↔DB, query plan check, worker↔DB, etc.).

## Deliverables
- `README.md` with setup/run/test instructions.
- Source code and/or SQL migrations/scripts.
- A short write-up: what you built, tradeoffs, and how you verified it.

## Suggested Run Commands
- npm install; docker compose up -d; npm test; npm run dev
