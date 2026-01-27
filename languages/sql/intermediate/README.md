# SQL (PostgreSQL) — Intermediate Curriculum

## Who this is for
Learners who finished the beginner track and can build small programs independently.

## Focus
Build job-ready foundations: testing, APIs, databases, security basics, and deployment. You’ll ship small, real projects with quality gates.

## Tooling expectations
- **Environment**: PostgreSQL 15+ (local via Docker)
- **Build/Packages**: psql + migrations tool (Sqitch/Flyway/Liquibase) + SQL formatter (sqlfluff)
- **Testing**: pgTAP (or migration + query validation scripts)
- **Lint/Format**: sqlfluff (lint + fix) + consistent naming conventions
- **Web/API**: Interface layer via views/functions + (optional) PostgREST
- **Database**: PostgreSQL schemas, roles, RLS, indexes, EXPLAIN
- **Containers**: Docker + docker-compose to run Postgres
- **CI**: GitHub Actions (migrate + pgTAP + sqlfluff)

## How to use this curriculum
- Work through modules in order; each ends with a mini-project.
- Then complete the projects in `projects/` (two mini-projects + a capstone).
- Treat every deliverable like a PR: clear README, tests, and reproducible steps.

## Assessment (high level)
- **Meets**: runs locally, passes tests, clear documentation.
- **Exceeds**: strong design tradeoffs, resilient behavior, measured performance/quality improvements.
