const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");
const crypto = require("crypto");

process.env.JWT_SECRET = "oauth-test-secret-at-least-32-chars!!";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-oauth-${crypto.randomUUID()}.sqlite`);
process.env.CORS_ORIGINS = "http://127.0.0.1:5500,http://localhost:5500";
process.env.PUBLIC_API_BASE = "http://127.0.0.1:9";
process.env.FRONTEND_DEFAULT_RETURN = "http://127.0.0.1:5500/docs/account.html";

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { createOAuthStore, isSafeReturnTo, listConfiguredProviders } = require("../src/oauth");
const { app } = require("../src/server");

test("no OAuth providers configured by default", () => {
  assert.deepEqual(listConfiguredProviders(), []);
});

test("isSafeReturnTo allows CORS origins and localhost", () => {
  const allowed = ["https://example.github.io", "http://127.0.0.1:5500"];
  assert.equal(isSafeReturnTo("https://example.github.io/docs/account.html", allowed), true);
  assert.equal(isSafeReturnTo("http://127.0.0.1:5500/docs/account.html", allowed), true);
  assert.equal(isSafeReturnTo("http://localhost:8080/docs/account.html", allowed), true);
  assert.equal(isSafeReturnTo("https://evil.example/phish", allowed), false);
  assert.equal(isSafeReturnTo("javascript:alert(1)", allowed), false);
});

test("OAuth upsert creates user, links by email, and preserves progress", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-oauth-store-${crypto.randomUUID()}.sqlite`);
  const db = openDatabase(dbPath);
  const oauthStore = createOAuthStore(db);
  const auth = createAuth({ db, jwtSecret: "test-secret", oauthStore });

  const registered = await auth.register({
    email: "learner@example.com",
    password: "password123",
    displayName: "Learner",
  });

  db.prepare(
    `INSERT INTO progress (user_id, payload, updated_at) VALUES (?, ?, ?)`
  ).run(
    registered.user.id,
    JSON.stringify({
      completions: ["kept.md"],
      quizCompletions: {},
      startSteps: {},
      moduleProgress: {},
    }),
    new Date().toISOString()
  );

  const linked = oauthStore.upsertOAuthUser({
    provider: "google",
    providerUserId: "google-sub-123",
    email: "learner@example.com",
    displayName: "Learner G",
  });
  assert.equal(linked.id, registered.user.id);
  assert.deepEqual(oauthStore.providersForUser(linked.id), ["google"]);

  const progress = db.prepare(`SELECT payload FROM progress WHERE user_id = ?`).get(linked.id);
  assert.deepEqual(JSON.parse(progress.payload).completions, ["kept.md"]);

  // Same provider id signs back into the same user.
  const again = oauthStore.upsertOAuthUser({
    provider: "google",
    providerUserId: "google-sub-123",
    email: "learner@example.com",
    displayName: "Learner G",
  });
  assert.equal(again.id, registered.user.id);

  // Fresh social-only user (no password).
  const social = oauthStore.upsertOAuthUser({
    provider: "github",
    providerUserId: "gh-99",
    email: "social@example.com",
    displayName: "Social",
  });
  assert.ok(social.id);
  await assert.rejects(
    () => auth.login({ email: "social@example.com", password: "password123" }),
    /no password/i
  );

  const code = oauthStore.issueLoginCode(social.id);
  const consumed = oauthStore.consumeLoginCode(code);
  assert.equal(consumed.id, social.id);
  assert.equal(oauthStore.consumeLoginCode(code), null);

  const session = auth.sessionForUser(social);
  assert.ok(session.token);
  assert.equal(session.user.hasPassword, false);
  assert.deepEqual(session.user.providers, ["github"]);

  db.close();
  fs.unlinkSync(dbPath);
});

test("HTTP oauth providers + exchange endpoints", async () => {
  const server = await new Promise((resolve) => {
    const s = app.listen(0, "127.0.0.1", () => resolve(s));
  });
  const { port } = server.address();
  const base = `http://127.0.0.1:${port}`;

  const providersRes = await fetch(`${base}/api/auth/oauth/providers`);
  assert.equal(providersRes.status, 200);
  const providersJson = await providersRes.json();
  assert.deepEqual(providersJson.providers, []);

  const health = await fetch(`${base}/api/health`);
  const healthJson = await health.json();
  assert.deepEqual(healthJson.oauthProviders, []);

  // Exchange with bogus code fails.
  const bad = await fetch(`${base}/api/auth/oauth/exchange`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code: "nope" }),
  });
  assert.equal(bad.status, 401);

  // Unconfigured provider start returns 503 JSON.
  const start = await fetch(
    `${base}/api/auth/oauth/google?return_to=${encodeURIComponent("http://127.0.0.1:5500/docs/account.html")}`,
    { redirect: "manual" }
  );
  assert.equal(start.status, 503);

  server.close();
});
