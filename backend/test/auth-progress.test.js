const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");

process.env.JWT_SECRET = "test-secret";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-test-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "*";

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { mergeProgress } = require("../src/routes/progress");

test("register and login round trip", () => {
  const db = openDatabase(process.env.DATABASE_PATH);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `learner-${Date.now()}@example.com`;
  const registered = auth.register({
    email,
    password: "password123",
    displayName: "Alex",
  });
  assert.equal(registered.user.email, email);
  assert.ok(registered.token);

  const loggedIn = auth.login({ email, password: "password123" });
  assert.equal(loggedIn.user.id, registered.user.id);

  assert.throws(
    () => auth.login({ email, password: "wrong-password" }),
    /Invalid email or password/
  );

  db.close();
  fs.unlinkSync(process.env.DATABASE_PATH);
});

test("changePassword verifies current password and rotates the hash", () => {
  const dbPath = path.join(os.tmpdir(), `pf-test-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `changer-${Date.now()}@example.com`;
  const { user } = auth.register({ email, password: "password123", displayName: "Changer" });

  assert.throws(
    () => auth.changePassword(user.id, { currentPassword: "wrong-password", newPassword: "newpassword123" }),
    /Current password is incorrect/
  );

  assert.throws(
    () => auth.changePassword(user.id, { currentPassword: "password123", newPassword: "short" }),
    (error) => error.name === "ZodError"
  );

  assert.throws(
    () => auth.changePassword(user.id, { currentPassword: "password123", newPassword: "password123" }),
    /New password must be different/
  );

  const result = auth.changePassword(user.id, {
    currentPassword: "password123",
    newPassword: "newpassword123",
  });
  assert.equal(result.id, user.id);

  assert.throws(
    () => auth.login({ email, password: "password123" }),
    /Invalid email or password/
  );
  const loggedIn = auth.login({ email, password: "newpassword123" });
  assert.equal(loggedIn.user.id, user.id);

  db.close();
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
