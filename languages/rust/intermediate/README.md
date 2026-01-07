# Rust — Intermediate Curriculum

## Who this is for
Learners who finished the beginner track and can build small programs independently.

## Focus
Build job-ready foundations: testing, APIs, databases, security basics, and deployment. You’ll ship small, real projects with quality gates.

## Tooling expectations
- **Environment**: Rust stable (rustup)
- **Build/Packages**: Cargo
- **Testing**: cargo test
- **Lint/Format**: rustfmt + clippy
- **Web/API**: axum (or actix-web) REST + tokio
- **Database**: PostgreSQL + migrations (sqlx migrate) + SQLx
- **Containers**: Docker + docker-compose
- **CI**: GitHub Actions (fmt + clippy + test)

## How to use this curriculum
- Work through modules in order; each ends with a mini-project.
- Then complete the projects in `projects/` (two mini-projects + a capstone).
- Treat every deliverable like a PR: clear README, tests, and reproducible steps.

## Assessment (high level)
- **Meets**: runs locally, passes tests, clear documentation.
- **Exceeds**: strong design tradeoffs, resilient behavior, measured performance/quality improvements.
