# Python Advanced — Capstone: Capstone: Operable, Scalable System

## Overview
- **Goal**: Build a system that is deployable and operable: scalability plan, resilience patterns, observability, security hardening, and profiling evidence.
- **Expected effort**: 7–14 days

## Brief
Build the deliverable using idiomatic tools for **Python**:
- venv + pip (or uv/poetry)
- pytest
- FastAPI (or Flask) for REST APIs
- PostgreSQL + migrations (Alembic)

## Requirements
- All intermediate capstone requirements
- Scalability considerations (read/write paths, caching, bottlenecks)
- Reliability patterns (retries, timeouts, idempotency, rate limits)
- Observability (metrics/logging/tracing concepts + what you would instrument)
- Security hardening (threat model + mitigations)
- Performance profiling or load testing evidence

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
- python -m venv .venv; pip install -r requirements.txt; docker compose up -d; pytest; uvicorn app:app
