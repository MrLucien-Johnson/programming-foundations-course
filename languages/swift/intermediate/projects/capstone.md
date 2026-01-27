# Swift Intermediate — Capstone: Capstone: Production-Ready Service

## Overview
- **Goal**: Build a small production-leaning service with auth, database, tests, and deployable instructions.
- **Expected effort**: 4–7 days

## Brief
Build the deliverable using idiomatic tools for **Swift**:
- Swift Package Manager (swift build)
- XCTest (swift test)
- Vapor (server-side Swift) for REST APIs
- PostgreSQL + migrations (Fluent)

## Requirements
- Authentication (login + protected endpoints)
- Database usage (schema + migrations)
- API or interface layer (HTTP endpoints or equivalent)
- Tests (unit + at least one integration test)
- Runnable/deployable instructions
- Logging or basic monitoring notes

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
- swift test; docker compose up -d; swift run
