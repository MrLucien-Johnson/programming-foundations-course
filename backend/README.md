# Programming Foundations API

Accounts and cross-device progress sync for the static course site in `/docs`.

## Features

- Email + password accounts (JWT sessions, 30 days)
- Progress sync for lesson completions, quiz results, Start Here steps, and module checklists
- SQLite storage (simple to run locally; swap the file for a persistent volume in production)
- CORS allow-list for your published site origin

## Quick start

```bash
cd backend
cp .env.example .env
npm install
npm run dev
```

API listens on `http://localhost:8787` by default.

Health check:

```bash
curl http://localhost:8787/api/health
```

## Frontend wiring

1. Copy `docs/config.example.js` to `docs/config.js` (already gitignored pattern via example).
2. Set:

```js
window.PF_CONFIG = {
  apiBaseUrl: "http://localhost:8787",
};
```

3. Open the site (Live Server / static host) and visit **Account**.

When signed in, progress writes sync to the API. Guest mode still uses localStorage only.

## API

| Method | Path | Auth | Body |
|--------|------|------|------|
| GET | `/api/health` | no | — |
| POST | `/api/auth/register` | no | `{ email, password, displayName? }` |
| POST | `/api/auth/login` | no | `{ email, password }` |
| GET | `/api/auth/me` | Bearer | — |
| GET | `/api/progress` | Bearer | — |
| PUT | `/api/progress` | Bearer | progress JSON |

Progress payload shape:

```json
{
  "completions": ["python-beginner-workbook/module-01-setup/README.md"],
  "quizCompletions": {
    "…/quiz.md": { "score": 8, "total": 10, "passed": true, "at": "ISO-8601" }
  },
  "startSteps": { "open-online": true },
  "moduleProgress": { "module-progress:…": { } },
  "updatedAt": "ISO-8601"
}
```

## Production checklist

1. Set a strong `JWT_SECRET`.
2. Set `CORS_ORIGINS` to your real site origin(s), e.g. `https://yourname.github.io`.
3. Persist `DATABASE_PATH` on a volume.
4. Put TLS in front (Railway, Render, Fly.io, Cloudflare Tunnel, nginx, etc.).
5. Point `docs/config.js` `apiBaseUrl` at the public API URL.

## Deploy notes (Render / Railway / Fly)

- Root directory: `backend`
- Start command: `npm start`
- Environment variables: copy from `.env.example`
- Attach a persistent disk for the SQLite file, **or** migrate later to Postgres if traffic grows

## Tests

```bash
cd backend
npm test
```
