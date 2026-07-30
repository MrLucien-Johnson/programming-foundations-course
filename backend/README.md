# Programming Foundations API

Accounts and cross-device progress sync for the static course site in `/docs`.

## Features

- Email + password accounts (JWT sessions, 30 days)
- Passwords hashed with Argon2id (OWASP-recommended); legacy bcrypt hashes upgrade on next login
- Password changes invalidate other sessions (token version bump)
- Progress sync for lesson completions, quiz results, Start Here steps, and module checklists
- SQLite storage (simple to run locally; swap the file for a persistent volume in production)
- CORS allow-list for your published site origin

Social sign-in (Google / Apple / GitHub / Microsoft) is implemented in the API for a later iteration; the site UI currently shows email/password only.

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
| POST | `/api/auth/change-password` | Bearer | `{ currentPassword, newPassword }` → `{ user, token }` |
| GET | `/api/auth/oauth/providers` | no | configured social providers |
| GET | `/api/auth/oauth/:provider` | no | starts OAuth (`return_to` query) |
| GET/POST | `/api/auth/oauth/:provider/callback` | no | provider redirect |
| POST | `/api/auth/oauth/exchange` | no | `{ code }` → `{ token, user }` |
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

## Social sign-in (optional)

Email/password always works. To offer one-click Google / GitHub / Microsoft / Apple:

1. Create a free OAuth app at the provider.
2. Set the callback URL to `{PUBLIC_API_BASE}/api/auth/oauth/{provider}/callback`.
3. Put the client id/secret in env (see `.env.example`). Never commit secrets.
4. Set `CORS_ORIGINS` to your site origin and `PUBLIC_API_BASE` to the public API URL.
5. Restart the API — `/api/health` lists enabled `oauthProviders`, and the Account page shows matching buttons.

Apple Sign In also needs `APPLE_TEAM_ID`, `APPLE_KEY_ID`, and `APPLE_PRIVATE_KEY` (PEM). Linking is by email: if a learner already registered with that email, the social login attaches to the same account and keeps their progress.

## Production checklist

1. Set a strong `JWT_SECRET` (at least 32 random characters).
2. Set `CORS_ORIGINS` to your real site origin(s), e.g. `https://yourname.github.io`.
3. Set `ORG_CREATOR_EMAILS` to your own email (see above) — required to create an org.
4. Persist `DATABASE_PATH` on a volume (`/data/pf.sqlite` on Render).
5. Put TLS in front (Render/Railway/Fly provide HTTPS).
6. Point `docs/config.js` `productionApiBaseUrl` at the public API URL.
7. (Optional) Configure social OAuth env vars and `PUBLIC_API_BASE` / `FRONTEND_DEFAULT_RETURN`.

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
