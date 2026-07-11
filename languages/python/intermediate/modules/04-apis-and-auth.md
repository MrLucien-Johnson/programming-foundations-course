# Python Intermediate — Module 04: APIs and Auth

## Overview
Design and secure REST APIs with authentication and authorization.

This module uses **Python 3.12+**, **venv + pip (or uv/poetry)**, and **pytest**. When applicable, you’ll build or extend a small service using **FastAPI (or Flask) for REST APIs** and **PostgreSQL + migrations (Alembic)**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **APIs and Auth**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: ruff + black (or ruff format).
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **Python**.
- Able to run a local project in this environment: **Python 3.12+**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose for local Postgres).

## Lessons
1) REST: resources, status codes, pagination (45 min)
2) Input validation + error envelopes (40 min)
3) AuthN vs AuthZ: sessions/JWT + roles (45 min)
4) Rate limiting + basic abuse protections (35 min)
5) API docs: OpenAPI + examples (35 min)

## Guided Walkthrough

Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/python/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will design and secure API endpoints.
3. Define request/response contracts with example payloads.
4. Implement one authenticated endpoint and validate error cases.
5. Add logging and status code verification.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/python/intermediate/starter-pack` for a clean baseline.

Inside the pack:
- A minimal project scaffold.
- A sample entry point you can expand.
- A place to add tests and notes.

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
Build a small, production-leaning feature or service slice that showcases **APIs and Auth** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **ruff/format + unit tests + integration tests (HTTP + DB) in CI**.
- Tests must be deterministic (no flakes) and runnable by a reviewer.
- If the module involves a database, tests must run against an isolated schema/database.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Feature works and handles common cases | Handles edge cases and failure modes with tests |
| Test quality | Tests pass and are readable | Strong boundaries, good fixtures, meaningful assertions |
| Code quality | Lint/format clean, clear naming | Clean architecture choices with justified tradeoffs |
| Documentation | Setup + usage documented | Includes rationale, diagrams, or ADR-style notes |

## Verification Checklist

Before moving on, confirm the following:

- Run the module tests and confirm they pass.
- Verify the primary feature works with normal and edge-case inputs.
- Update the README with setup, run, and test commands.
- Run: `python -m pytest`
- Run: `ruff check .`
- Run: `ruff format .`

## Common Mistakes
- Shipping without an automated test run in CI.
- Over-mocking (tests assert implementation details instead of outcomes).
- Skipping input validation and assuming “happy path”.
- Making performance claims without measurements.

## Stretch Resources


- HTTP overview: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- OAuth 2.0 intro: https://oauth.net/2/

