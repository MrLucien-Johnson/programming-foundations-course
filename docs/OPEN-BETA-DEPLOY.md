# Open beta: turn on accounts in production

Your course site can stay on **GitHub Pages**. Accounts need a small **HTTPS API** next to it. Guest learning keeps working even if the API is down.

## What you need (about 20 minutes)

1. Merge the accounts PR into `main` (and the usability PR if it is not merged yet)
2. Deploy the API on Render (free web service + cheap disk)
3. Point `docs/config.js` at that API URL
4. Set CORS to your live site origin
5. Smoke-test Account on the live site

---

## Step 1 — Merge code

Merge these into `main` (order does not matter much if accounts already includes usability):

- Usability PR (if still open)
- Accounts/backend PR

GitHub Pages will publish from `docs/` after `main` updates.

---

## Step 2 — Deploy the API on Render

### Create the service

1. Go to [https://render.com](https://render.com) and sign in with GitHub
2. **New → Blueprint** (or Web Service) and select `programming-foundations-course`
3. If using Blueprint, Render reads [`render.yaml`](../render.yaml)
4. If creating manually:
   - **Root directory:** `backend`
   - **Runtime:** Node
   - **Build command:** `npm install`
   - **Start command:** `npm start`
   - **Instance:** Free is fine for open beta

### Add a persistent disk (important)

Free Render disks wipe on restart unless you attach storage.

1. In the service → **Disks**
2. Add a disk:
   - **Name:** `pf-data`
   - **Mount path:** `/data`
   - **Size:** 1 GB is enough for beta

### Environment variables

| Key | Value |
|-----|--------|
| `NODE_ENV` | `production` |
| `PORT` | `8787` (or leave Render’s default and set `PORT` to what Render injects — our server reads `PORT`) |
| `JWT_SECRET` | long random string (e.g. `openssl rand -hex 32`) |
| `DATABASE_PATH` | `/data/pf.sqlite` |
| `CORS_ORIGINS` | your live site origin(s), comma-separated |

Examples for `CORS_ORIGINS`:

```text
https://mrlucien-johnson.github.io
https://mrlucien-johnson.github.io,https://www.yourdomain.com
```

Use the exact origin learners open in the browser (no trailing slash, include `https://`).

### Deploy

Click **Deploy**. When it finishes, open:

```text
https://YOUR-SERVICE.onrender.com/api/health
```

You should see: `{"ok":true,"service":"programming-foundations-api"}`.

Copy the service URL (no path). That is your API base URL.

---

## Step 3 — Point the website at the API

Edit [`docs/config.js`](config.js):

```js
window.PF_CONFIG = {
  // Local development
  // apiBaseUrl: "http://localhost:8787",

  // Production (Render / Railway / Fly)
  apiBaseUrl: "https://YOUR-SERVICE.onrender.com",
};
```

Or keep the auto-detect version already in the repo: set `productionApiBaseUrl` to your Render URL.

Commit and push to `main` so GitHub Pages picks it up.

---

## Step 4 — Live smoke test

1. Open the live site → **Account**
2. Create a test account
3. Mark a lesson complete
4. Open a private window (or another device) → sign in
5. Confirm progress is there
6. Sign out and confirm guest mode still works

If Account says it cannot reach the API:

- Check `/api/health` on the API URL
- Confirm `CORS_ORIGINS` matches the site origin exactly
- Confirm the site uses `https://…` for `apiBaseUrl` (never `http://` on a GitHub Pages site)

---

## Step 5 — Soft-launch messaging

Tell beta learners:

> You can learn as a guest. Create a free Account if you want progress to follow you on another device.

Link them to `account.html`.

---

## Ops checklist for open beta

- [ ] API health URL bookmarked
- [ ] `JWT_SECRET` stored in a password manager
- [ ] Disk mounted at `/data`
- [ ] CORS includes every live origin you use
- [ ] Test account created and verified on a second device
- [ ] Instagram/help reply ready for “progress disappeared” → point to Account

## Cost expectation

- GitHub Pages: free
- Render free web service: free (spins down when idle; first request may be slow)
- Render disk: usually a few dollars/month — worth it so beta progress is not wiped on restart

## If Render free spin-down is annoying

Upgrade the web service to a tiny always-on plan, or move the same `backend/` folder to Railway/Fly with a volume. The app code does not need to change—only env vars and `config.js`.
