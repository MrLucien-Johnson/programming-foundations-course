# Go — Intermediate Curriculum

## Who this is for
Learners who finished the beginner track and can build small programs independently.

## Focus
Build job-ready foundations: testing, APIs, databases, security basics, and deployment. You’ll ship small, real projects with quality gates.

## Tooling expectations
- **Environment**: Go 1.22+
- **Build/Packages**: go mod
- **Testing**: testing + httptest
- **Lint/Format**: gofmt + golangci-lint
- **Web/API**: net/http (or chi/gin) REST
- **Database**: PostgreSQL + migrations (goose) + database/sql (or sqlc)
- **Containers**: Docker + docker-compose
- **CI**: GitHub Actions (lint + test)

## How to use this curriculum
- Work through modules in order; each ends with a mini-project.
- Then complete the projects in `projects/` (two mini-projects + a capstone).
- Treat every deliverable like a PR: clear README, tests, and reproducible steps.

## Assessment (high level)
- **Meets**: runs locally, passes tests, clear documentation.
- **Exceeds**: strong design tradeoffs, resilient behavior, measured performance/quality improvements.
