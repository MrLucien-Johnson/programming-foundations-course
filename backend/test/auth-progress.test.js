const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");
const bcrypt = require("bcryptjs");

process.env.JWT_SECRET = "test-secret";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-test-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "*";

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { mergeProgress } = require("../src/routes/progress");
const { isArgon2Hash, isBcryptHash } = require("../src/passwords");

test("register and login round trip stores Argon2id hashes", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-test-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `learner-${Date.now()}@example.com`;
  const registered = await auth.register({
    email,
    password: "password123",
    displayName: "Alex",
  });
  assert.equal(registered.user.email, email);
  assert.ok(registered.token);
  assert.equal(registered.user.password_hash, undefined);

  const row = db.prepare("SELECT password_hash FROM users WHERE email = ?").get(email);
  assert.ok(isArgon2Hash(row.password_hash));
  assert.ok(!isBcryptHash(row.password_hash));
  assert.ok(!row.password_hash.includes("password123"));

  const loggedIn = await auth.login({ email, password: "password123" });
  assert.equal(loggedIn.user.id, registered.user.id);

  await assert.rejects(
    () => auth.login({ email, password: "wrong-password" }),
    /Invalid email or password/
  );

  db.close();
  fs.unlinkSync(dbPath);
});

test("legacy bcrypt hashes verify and upgrade to Argon2id on login", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-test-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `legacy-${Date.now()}@example.com`;
  const now = new Date().toISOString();
  const id = "legacy-user-id";
  db.prepare(
    `INSERT INTO users (id, email, display_name, password_hash, token_version, created_at, updated_at)
     VALUES (?, ?, '', ?, 0, ?, ?)`
  ).run(id, email, bcrypt.hashSync("password123", 10), now, now);

  const before = db.prepare("SELECT password_hash FROM users WHERE id = ?").get(id);
  assert.ok(isBcryptHash(before.password_hash));

  const loggedIn = await auth.login({ email, password: "password123" });
  assert.equal(loggedIn.user.id, id);

  const after = db.prepare("SELECT password_hash FROM users WHERE id = ?").get(id);
  assert.ok(isArgon2Hash(after.password_hash));

  const again = await auth.login({ email, password: "password123" });
  assert.equal(again.user.id, id);

  db.close();
  fs.unlinkSync(dbPath);
});

test("changePassword verifies current password, rotates hash, and invalidates old JWTs", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-test-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `changer-${Date.now()}@example.com`;
  const { user, token: oldToken } = await auth.register({
    email,
    password: "password123",
    displayName: "Changer",
  });

  await assert.rejects(
    () =>
      auth.changePassword(user.id, {
        currentPassword: "wrong-password",
        newPassword: "newpassword123",
      }),
    /Current password is incorrect/
  );

  await assert.rejects(
    () =>
      auth.changePassword(user.id, {
        currentPassword: "password123",
        newPassword: "short",
      }),
    (error) => error.name === "ZodError"
  );

  await assert.rejects(
    () =>
      auth.changePassword(user.id, {
        currentPassword: "password123",
        newPassword: "password123",
      }),
    /New password must be different/
  );

  const result = await auth.changePassword(user.id, {
    currentPassword: "password123",
    newPassword: "newpassword123",
  });
  assert.equal(result.user.id, user.id);
  assert.ok(result.token);
  assert.notEqual(result.token, oldToken);

  await assert.rejects(
    () => auth.login({ email, password: "password123" }),
    /Invalid email or password/
  );
  const loggedIn = await auth.login({ email, password: "newpassword123" });
  assert.equal(loggedIn.user.id, user.id);

  const hashRow = db.prepare("SELECT password_hash, token_version FROM users WHERE id = ?").get(user.id);
  assert.ok(isArgon2Hash(hashRow.password_hash));
  assert.equal(hashRow.token_version, 1);

  // Old JWT must fail requireAuth after password change.
  const req = { headers: { authorization: `Bearer ${oldToken}` } };
  const res = {
    statusCode: 200,
    body: null,
    status(code) {
      this.statusCode = code;
      return this;
    },
    json(payload) {
      this.body = payload;
      return this;
    },
  };
  await new Promise((resolve) => {
    auth.requireAuth(req, res, () => resolve("next"));
    // If auth fails it won't call next; settle shortly.
    setTimeout(() => resolve("timeout"), 20);
  });
  assert.equal(res.statusCode, 401);

  // Fresh token from changePassword works.
  const req2 = { headers: { authorization: `Bearer ${result.token}` } };
  let nextCalled = false;
  const res2 = {
    status() {
      return this;
    },
    json() {
      return this;
    },
  };
  await new Promise((resolve) => {
    auth.requireAuth(req2, res2, () => {
      nextCalled = true;
      resolve();
    });
  });
  assert.equal(nextCalled, true);
  assert.equal(req2.user.id, user.id);

  db.close();
  fs.unlinkSync(dbPath);
});

test("progress persists across reopen for the same user account", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-test-progress-${Date.now()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `persist-${Date.now()}@example.com`;
  const { user, token } = await auth.register({
    email,
    password: "password123",
    displayName: "Persister",
  });

  const upsert = db.prepare(`
    INSERT INTO progress (user_id, payload, updated_at)
    VALUES (@user_id, @payload, @updated_at)
    ON CONFLICT(user_id) DO UPDATE SET
      payload = excluded.payload,
      updated_at = excluded.updated_at
  `);
  const payload = {
    completions: ["python/module-01.md"],
    quizCompletions: {
      "python/q1.md": { score: 9, total: 10, passed: true, at: "2026-07-30T00:00:00.000Z" },
    },
    startSteps: { "open-online": true },
    moduleProgress: {},
    updatedAt: "2026-07-30T00:00:00.000Z",
  };
  upsert.run({
    user_id: user.id,
    payload: JSON.stringify(payload),
    updated_at: payload.updatedAt,
  });
  db.close();

  const db2 = openDatabase(dbPath);
  const auth2 = createAuth({ db: db2, jwtSecret: process.env.JWT_SECRET });
  const loggedIn = await auth2.login({ email, password: "password123" });
  assert.equal(loggedIn.user.id, user.id);
  assert.ok(loggedIn.token);
  assert.notEqual(token, undefined);

  const row = db2.prepare("SELECT payload FROM progress WHERE user_id = ?").get(user.id);
  assert.ok(row);
  const stored = JSON.parse(row.payload);
  assert.deepEqual(stored.completions, ["python/module-01.md"]);
  assert.equal(stored.quizCompletions["python/q1.md"].score, 9);
  assert.equal(stored.startSteps["open-online"], true);

  db2.close();
  fs.unlinkSync(dbPath);
});

test("mergeProgress unions completions and keeps true start steps", () => {
  const merged = mergeProgress(
    {
      completions: ["a.md"],
      quizCompletions: {
        "q1.md": { score: 8, total: 10, passed: true, at: "2026-01-02T00:00:00.000Z" },
      },
      startSteps: { "open-online": true },
      moduleProgress: {},
    },
    {
      completions: ["b.md"],
      quizCompletions: {
        "q1.md": { score: 5, total: 10, passed: false, at: "2026-01-01T00:00:00.000Z" },
      },
      startSteps: { "choose-course": true, "open-online": false },
      moduleProgress: { "module-progress:a.md": { outcomes: {} } },
    }
  );

  assert.deepEqual(new Set(merged.completions), new Set(["a.md", "b.md"]));
  assert.equal(merged.quizCompletions["q1.md"].score, 8);
  assert.equal(merged.startSteps["open-online"], true);
  assert.equal(merged.startSteps["choose-course"], true);
  assert.ok(merged.moduleProgress["module-progress:a.md"]);
});
