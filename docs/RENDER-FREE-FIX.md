# Fix your live Render Free service

Your service URL is:

`https://programming101.onrender.com`

The site is already on GitHub Pages:

`https://mrlucien-johnson.github.io/programming-foundations-course/`

Right now the API URL times out, which usually means the service is **crashing on boot**, pointed at the wrong folder, or the build command has a typo.

## Do this in the Render dashboard

### 1) Settings → Build & Deploy

| Setting | Value |
|--------|--------|
| Runtime | **Node** (not Go) |
| Root Directory | `backend` |
| Build Command | `npm install` (all lowercase — `Npm` will fail) |
| Start Command | `npm start` |

If Root Directory is empty, Render tries to start the whole repo and the API never comes up.

### 2) Environment

| Key | Value |
|-----|--------|
| `NODE_ENV` | `production` |
| `JWT_SECRET` | a long random string (create one; do not leave blank) |
| `DATABASE_PATH` | `./data/pf.sqlite` |
| `CORS_ORIGINS` | `https://mrlucien-johnson.github.io` |

Important for **Free**:
- Do **not** use `/data/pf.sqlite` unless you attached a disk
- Free has no durable disk, so account data can reset on restart
- That is OK for a temporary beta smoke test, not for keeping learner progress long-term

### 3) Manual Deploy

Use **Manual Deploy → Clear build cache & deploy**.

### 4) Logs

Open **Logs**. You want to see:

```text
Programming Foundations API listening on http://0.0.0.0:...
```

If you see `Refusing to start: set JWT_SECRET`, add `JWT_SECRET`.
If you see errors about `/data`, switch `DATABASE_PATH` to `./data/pf.sqlite`.

### 5) Health check

After deploy finishes, open:

`https://programming101.onrender.com/api/health`

Expected:

```json
{"ok":true,"service":"programming-foundations-api"}
```

First request on Free can take ~30–60s while it wakes up.

## Then wire the website

`docs/config.js` should use `https://programming101.onrender.com`. After that is on `main`, open:

`https://mrlucien-johnson.github.io/programming-foundations-course/account.html`

Create a test account.

## For real open beta (recommended next)

Upgrade this service to **Starter + disk**:
- Disk mount: `/data`
- `DATABASE_PATH=/data/pf.sqlite`

Otherwise Free restarts will wipe accounts.
