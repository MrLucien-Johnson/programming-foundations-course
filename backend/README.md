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

## Who can create an organisation / be an admin?

Creating an organisation (and holding the `admin` membership role in general —
including being invited or promoted to admin) is restricted to an allowlist of
emails set via `ORG_CREATOR_EMAILS` (comma-separated, case-insensitive). This
is **fail-closed**: if the variable is unset or empty, no one can create an
org or hold the admin role, even in local dev. Everyone can still register,
sign in, learn, and be invited/added as a `learner`.

Set your own email so you can create your first org:

```bash
ORG_CREATOR_EMAILS=you@example.com
```

Do not commit real email addresses — set this in your local `.env` (already
gitignored) and in your host's environment variables (e.g. the Render
dashboard) instead.

## Production checklist

1. Set a strong `JWT_SECRET`.
2. Set `CORS_ORIGINS` to your real site origin(s), e.g. `https://yourname.github.io`.
3. Set `ORG_CREATOR_EMAILS` to your own email (see above) — required to create an org.
4. Persist `DATABASE_PATH` on a volume (`/data/pf.sqlite` on Render).
5. Put TLS in front (Render/Railway/Fly provide HTTPS).
6. Point `docs/config.js` `productionApiBaseUrl` at the public API URL.

Open-beta walkthrough: [`docs/OPEN-BETA-DEPLOY.md`](../docs/OPEN-BETA-DEPLOY.md)

## Deploy notes (Render)

- Blueprint file: [`render.yaml`](../render.yaml) at repo root
- Root directory: `backend`
- Start command: `npm start`
- Use **Starter** + disk mount `/data` (Free instances lose SQLite on restart)
- Set `CORS_ORIGINS` in the Render dashboard after first deploy

## Tests

```bash
cd backend
npm test
```
