# Accounts & cross-device progress

The course site can run fully as a guest (local browser storage only).

## Local tryout

1. Run the API in [`backend/`](../backend/README.md)
2. Open the site and visit **Account**
3. Create an account or sign in

## Production open beta

Follow the step-by-step guide:

→ **[OPEN-BETA-DEPLOY.md](OPEN-BETA-DEPLOY.md)**

That covers Render deploy, disk, CORS, and pointing `config.js` at your live API.

## What syncs

- Lesson completions
- Quiz results
- Start Here checklist
- Module checklist ticks in the lesson viewer

## Configuration

- Frontend API URL: [`config.js`](config.js) (see `config.example.js`)
- Backend secrets / CORS: [`../backend/.env.example`](../backend/.env.example)

Guest learning still works if the API is offline.