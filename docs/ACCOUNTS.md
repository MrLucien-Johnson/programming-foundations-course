# Accounts & cross-device progress

The course site can run fully as a guest (local browser storage only).

**Free hosting note:** On Render Free (no paid disk), cloud accounts can be wiped when the
service restarts. Guest progress on the learner’s device remains the reliable default.
Donations via [Support](support.html) are how we plan to fund durable hosting later.

## Local tryout

1. Run the API in [`backend/`](../backend/README.md)
2. Open the site and visit **Account**
3. Create an account or sign in

## Production open beta

Follow the step-by-step guide:

→ **[OPEN-BETA-DEPLOY.md](OPEN-BETA-DEPLOY.md)**

That covers Render deploy, disk, CORS, and pointing `config.js` at your live API.

If you stay on Free for now: keep guest mode front-and-centre, and treat cloud sync as best-effort.

## Donations

Set `donateUrl` in [`config.js`](config.js) to a free provider link (Ko-fi, PayPal.Me, Buy Me a Coffee, or GitHub Sponsors). The Support page and donate buttons pick it up automatically.

## What syncs

- Lesson completions
- Quiz results
- Start Here checklist
- Module checklist ticks in the lesson viewer

## Configuration

- Frontend API URL: [`config.js`](config.js) (see `config.example.js`)
- Backend secrets / CORS: [`../backend/.env.example`](../backend/.env.example)

Guest learning still works if the API is offline.