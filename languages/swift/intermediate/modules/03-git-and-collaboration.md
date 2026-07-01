# Swift Intermediate — Module 03: Git and Collaboration

## Overview
Collaborate safely using branching, PRs, and reviews.

This module uses **Swift 5.10+ (SwiftPM)**, **Swift Package Manager (swift build)**, and **XCTest (swift test)**. When applicable, you’ll build or extend a small service using **Vapor (server-side Swift) for REST APIs** and **PostgreSQL + migrations (Fluent)**.

## Learning Outcomes
- Explain the core concepts and tradeoffs for **Git and Collaboration**.
- Apply the concepts to a realistic codebase (not just toy examples).
- Write tests that prove correctness and prevent regressions.
- Use tooling to keep quality high: SwiftFormat + SwiftLint.
- Document decisions and constraints clearly for reviewers.

## Prerequisites
- Comfortable with the course’s beginner material in **Swift**.
- Able to run a local project in this environment: **Swift 5.10+ (SwiftPM)**.
- Basic CLI literacy (running tests, reading logs).
- For modules that involve data: a local **PostgreSQL** instance (recommended via Docker + docker-compose for Postgres).

## Lessons
1) Branching strategies + commit hygiene (40 min)
2) PRs: review checklists and feedback loops (40 min)
3) Conflicts and rebasing safely (45 min)
4) Working with CI failures (30 min)

## Guided Walkthrough

Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/swift/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will work in branches, reviews, and clean history.
3. Create a feature branch, commit in small increments, and open a PR description.
4. Resolve one simulated conflict by rebasing or merging safely.
5. Write a changelog entry that summarises the work.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/swift/intermediate/starter-pack` for a clean baseline.

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
Build a small, production-leaning feature or service slice that showcases **Git and Collaboration** in a way you could explain in a code review.

### Acceptance Criteria
- Deliverable runs locally with clear instructions.
- Includes tests appropriate for the feature.
- Uses consistent style/formatting and passes the quality gate.
- Includes a short README section describing assumptions and tradeoffs.

## Testing Requirements
- All work must be covered by **build + tests + lint/format in CI**.
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
- Run: `swift main.swift`

## Common Mistakes
- Shipping without an automated test run in CI.
- Over-mocking (tests assert implementation details instead of outcomes).
- Skipping input validation and assuming “happy path”.
- Making performance claims without measurements.

## Stretch Resources


- Pro Git book: https://git-scm.com/book/en/v2
- GitHub flow: https://docs.github.com/en/get-started/quickstart/github-flow

