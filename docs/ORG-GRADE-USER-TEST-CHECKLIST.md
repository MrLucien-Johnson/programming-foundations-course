# Org-Grade Roadmap — User Test Checklist

This covers the Phase 1–3 org-grade features added on the `test/org-grade-phases` branch.
Nothing here breaks guest / self-serve learning — that path keeps working with no account.

## 0. Run it locally

**Backend (Express + SQLite):**

```bash
cd backend
npm install
npm test        # should show 9 passing tests
npm run dev     # starts API on http://localhost:8787
```

Leave the API running in one terminal.

**Frontend (static site):** the site talks to `http://localhost:8787` automatically when opened
from `localhost`/`127.0.0.1` (see `docs/config.js`). Serve `docs/` with any static server, e.g.:

```bash
cd docs
python -m http.server 5173
```

Then open http://127.0.0.1:5173/ (open via a server, not `file://`, so `fetch` works).

Quick API smoke test (optional):

```bash
curl http://localhost:8787/api/health
```

---

## 1. Phase 1 — Trust (accounts, orgs, roles, assignments, durable quiz log)

- [ ] **Guest still works:** In a fresh browser, complete a module and take a quiz without signing in. Progress persists on reload.
- [ ] **Create account:** Go to **Account**, create an account, confirm you’re signed in.
- [ ] **Create an org:** Go to **Teams**, create an organisation. You become **admin**.
- [ ] **Add an existing user:** Register a second account (second browser/incognito). Back as admin, add that email — status shows **active** immediately.
- [ ] **Invite a new email:** Add an email that has NOT registered — status shows **invited**. Register that email; it should auto-join the org (check the members list).
- [ ] **Roles:** Promote a learner to admin and back. Confirm you **cannot demote/remove the last admin** (error shown).
- [ ] **Assign paths:** Assign a course org-wide and a course to a single member. Confirm they appear under “Assigned paths”.
- [ ] **Durable quiz log:** While signed in, take a quiz in **Courses → a quiz**. It’s recorded server-side (verified next in the gradebook).

## 2. Phase 2 — Operate (roster, gradebook, dashboards, verifiable certs)

- [ ] **Analytics lite:** On the org page, the analytics line shows members, assignments, completions, quiz attempts, and pass rate.
- [ ] **Roster CSV:** Click **Download roster CSV** — opens a CSV with email, name, role, status, modules completed.
- [ ] **Gradebook CSV:** Click **Download gradebook CSV** — includes the quiz attempt(s) you made while signed in.
- [ ] **Verifiable certificate:** Go to **certificate.html**, complete a course’s modules, enter your name, then **Issue verifiable certificate**. Note the code (e.g. `PF-XXXX-XXXX`).
- [ ] **Public verify:** Open **verify.html**, paste the code (or use the verify link). It should show **Valid certificate**. A random code shows **Not found**.

## 3. Phase 3 — Buy (analytics, billing stub, audit, privacy/DPA, persona templates)

- [ ] **Billing stub (plan):** On the org page, change the plan (Free/Team/School/Enterprise) and save. Reload — the plan persists.
- [ ] **Audit log:** The “Recent activity” panel lists actions (org.create, member.add, path.assign, etc.).
- [ ] **Persona templates:** Use the “Assign … path” buttons to bulk-assign a persona’s recommended courses; confirm they appear in assignments.
- [ ] **Privacy page:** Open **privacy.html**. Signed in, click **Export my data (JSON)** — downloads your account, progress, quiz attempts, certificates, memberships.
- [ ] **Delete account:** (Use a throwaway account) Click **Delete my account**, confirm. You’re signed out and `/api/auth/me` returns unauthorized. Guest progress in the browser is retained.

---

## What shipped (honest status)

- **Phase 1:** DONE — orgs/memberships/roles schema, org+member+role+assignment APIs, invite-on-register, server-side quiz attempt log, Teams admin UI, audit logging. SQLite durability already provided by the Render disk mount (`render.yaml`).
- **Phase 2:** DONE — roster CSV, gradebook CSV, analytics-lite endpoint + dashboard, verifiable certificates with public verify page.
- **Phase 3:** MOSTLY DONE — analytics-lite, billing **stub** (plan field only; no Stripe by design), audit log endpoint + UI, privacy/DPA page, self-service data export + account deletion, persona→path templates. Deferred: full payment provider integration, per-seat billing enforcement.

## New/changed API endpoints

- `POST/GET /api/orgs`, `GET/PATCH /api/orgs/:id`
- `GET/POST /api/orgs/:id/members`, `PATCH/DELETE /api/orgs/:id/members/:userId`
- `GET/POST /api/orgs/:id/assignments`
- `GET /api/orgs/:id/analytics`, `GET /api/orgs/:id/audit`
- `GET /api/orgs/:id/roster.csv`, `GET /api/orgs/:id/gradebook.csv`
- `GET/POST /api/quiz-attempts`
- `POST/GET /api/certificates`, `GET /api/certificates/verify/:verifyId` (public)
- `GET /api/account/export`, `DELETE /api/account`

## Automated tests

`cd backend && npm test` → 9 passing (auth round-trip, progress merge, CORS normalize,
org lifecycle/roles/invites/assignments, last-admin guard, analytics+gradebook, certificate
issue/verify, CSV escaping, and a full HTTP integration flow).
