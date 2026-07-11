# Go Advanced — Module 07: Observability and SLOs

## Overview
Instrument systems and run them with SLO-based operations.

This module uses **Go 1.22+**, **go mod**, and **testing + httptest**. When applicable, you’ll build or extend a small service using **net/http (or chi/gin) REST** and **PostgreSQL + migrations (goose) + database/sql (or sqlc)**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **Observability and SLOs**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: gofmt + golangci-lint.
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **Go**.
- Able to run a local project in this environment: **Go 1.22+**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose).

## Lessons
1) SLIs/SLOs and error budgets (45 min)
2) Metrics: RED/USE and cardinality pitfalls (45 min)
3) Tracing: spans, context propagation (45 min)
4) Alerting strategy + on-call hygiene (35 min)

## Guided Walkthrough

Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/go/advanced/starter-pack` into a new working folder.
2. Review the module goals and plan how you will monitor, alert, and set service objectives.
3. Define SLIs and SLO targets for one critical path.
4. Add logs/metrics for visibility.
5. Document alert thresholds and escalation steps.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/go/advanced/starter-pack` for a clean baseline.

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
Build a small, production-leaning feature or service slice that showcases **Observability and SLOs** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **gofmt + lint + tests in CI**.
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
- Run: `go test ./...`
- Run: `golangci-lint run`
- Run: `gofmt -w .`

## Common Mistakes
- Shipping without an automated test run in CI.
- Over-mocking (tests assert implementation details instead of outcomes).
- Skipping input validation and assuming “happy path”.
- Making performance claims without measurements.

## Stretch Resources


- SRE workbook: https://sre.google/workbook/
- OpenTelemetry: https://opentelemetry.io/docs/

