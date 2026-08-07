# Compose & local environments

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Run app + dependency (e.g. DB) with Compose
- Use env files without committing secrets
- Match local topology loosely to staging

## Why this matters

Local parity reduces “works on my machine”. Compose is the fastest way to learn multi-service wiring before Kubernetes.

## Core ideas

1. **Declare services** — app, db, cache as code.
2. **Networks & volumes** — data that must survive restarts.
3. **.env for local only** — never commit real credentials.
4. **Healthchecks** — start order that waits for readiness.

## Worked example

### Lab: app + Postgres sketch

```yaml
services:
  api:
    build: .
    ports: ["3000:3000"]
    environment:
      DATABASE_URL: postgres://app:app@db:5432/app
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: app
      POSTGRES_USER: app
      POSTGRES_DB: app
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
      retries: 5
```

```bash
docker compose up --build
```


## Practice

1. Add Compose for app + one dependency.
2. Document how a new teammate starts the stack in under five commands.
3. Ensure `.env` is gitignored; provide `.env.example` with fake values.

## Common mistakes

- Committing real passwords in compose files
- Assuming Compose equals production Kubernetes
- No healthcheck so the API starts before the DB

## Stretch goal

Add a `mailhog` or similar stub service for local email.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
