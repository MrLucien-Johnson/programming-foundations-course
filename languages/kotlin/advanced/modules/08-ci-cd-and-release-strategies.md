# Kotlin Advanced — Module 08: CI/CD and Release Strategies

## Overview
Ship safely with progressive delivery, rollbacks, and versioning.

This module uses **JDK 21 + Kotlin**, **Gradle**, and **JUnit 5 + MockK**. When applicable, you’ll build or extend a small service using **Ktor (or Spring Boot) REST** and **PostgreSQL + migrations (Flyway) + Exposed (or JDBC)**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **CI/CD and Release Strategies**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: ktlint + detekt.
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **Kotlin**.
- Able to run a local project in this environment: **JDK 21 + Kotlin**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose + Testcontainers).

## Lessons
1) Release strategies: canary, blue/green, rolling (45 min)
2) Feature flags + config safety (35 min)
3) Database migrations in production (45 min)
4) Rollbacks, versioning, and changelogs (40 min)

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
Build a small, production-leaning feature or service slice that showcases **CI/CD and Release Strategies** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **build + tests + static analysis in CI**.
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
