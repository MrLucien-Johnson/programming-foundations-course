# Accounts & cross-device progress

The course site can run fully as a guest (local browser storage only).

To sync progress across devices:

1. Run the API in [`backend/`](backend/README.md)
2. Open the site and visit **Account**
3. Create an account or sign in

Progress that syncs:

- Lesson completions
- Quiz results
- Start Here checklist
- Module checklist ticks in the lesson viewer

Configuration:

- Frontend API URL: [`docs/config.js`](docs/config.js) (see `docs/config.example.js`)
- Backend secrets / CORS: [`backend/.env.example`](backend/.env.example)

Guest learning still works if the API is offline.
