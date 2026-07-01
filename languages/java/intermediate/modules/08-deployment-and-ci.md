# Java Intermediate — Module 08: Deployment and CI

## Overview
Containerize, configure, and deploy with automated CI checks.

This module uses **Java 21 LTS**, **Maven (or Gradle)**, and **JUnit 5 + Mockito**. When applicable, you’ll build or extend a small service using **Spring Boot REST** and **PostgreSQL + migrations (Flyway) + JPA/Hibernate**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **Deployment and CI**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: Spotless + Checkstyle (or Error Prone).
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **Java**.
- Able to run a local project in this environment: **Java 21 LTS**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose + Testcontainers).

## Lessons
1) Environments + configuration (35 min)
2) Containers for local dev and CI (45 min)
3) CI pipelines: caching, matrices, artifacts (45 min)
4) Deployments: health checks + migrations + rollback plan (45 min)

## Guided Walkthrough

Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/java/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will ship safely with automation.
3. Create a deployment checklist (build, test, release).
4. Add a CI workflow or script that runs tests automatically.
5. Document rollback steps and environment variables.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/java/intermediate/starter-pack` for a clean baseline.

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
Build a small, production-leaning feature or service slice that showcases **Deployment and CI** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **build + unit tests + slice/integration tests (Spring + DB) in CI**.
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
- Run: `javac Main.java && java Main`

## Common Mistakes
- Shipping without an automated test run in CI.
- Over-mocking (tests assert implementation details instead of outcomes).
- Skipping input validation and assuming “happy path”.
- Making performance claims without measurements.

## Stretch Resources


- GitHub Actions: https://docs.github.com/en/actions
- CI/CD overview: https://martinfowler.com/articles/continuousIntegration.html

