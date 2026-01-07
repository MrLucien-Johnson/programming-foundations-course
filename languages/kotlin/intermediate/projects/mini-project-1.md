# Kotlin Intermediate — Mini Project 1: Task API (CRUD + tests)

## Overview
- **Goal**: Build a small REST API for tasks with validation and tests.
- **Expected effort**: 1–2 days

## Brief
Build the deliverable using idiomatic tools for **Kotlin**:
- Gradle
- JUnit 5 + MockK
- Ktor (or Spring Boot) REST
- PostgreSQL + migrations (Flyway) + Exposed (or JDBC)

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
- ./gradlew test; docker compose up -d; ./gradlew run
