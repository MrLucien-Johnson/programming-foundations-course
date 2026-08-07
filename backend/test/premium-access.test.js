const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");

process.env.JWT_SECRET = "test-secret-premium";
process.env.ORG_CREATOR_EMAILS = "owner@example.com";
process.env.PREMIUM_ACCESS_EMAILS = "mentor@example.com";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-premium-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "*";

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { createPremiumStore } = require("../src/premium");

test("premium allowlist and donor grant unlock access", () => {
  const dbPath = path.join(os.tmpdir(), `pf-premium-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const premiumStore = createPremiumStore({ db });
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET, premiumStore });

  const owner = auth.register({
    email: "owner@example.com",
    password: "password123",
    displayName: "Owner",
  });
  assert.equal(owner.user.premiumAccess, true);
  assert.equal(owner.user.canManagePremium, true);

  const learner = auth.register({
    email: "learner@example.com",
    password: "password123",
    displayName: "Learner",
  });
  assert.equal(learner.user.premiumAccess, false);

  const granted = premiumStore.grantDonor(owner.user, "learner@example.com", "Thanks for donating");
  assert.equal(granted.premiumAccess, true);
  assert.equal(granted.isDonor, true);

  const refreshed = auth.login({ email: "learner@example.com", password: "password123" });
  assert.equal(refreshed.user.premiumAccess, true);
  assert.equal(refreshed.user.isDonor, true);

  const mentor = auth.register({
    email: "mentor@example.com",
    password: "password123",
  });
  assert.equal(mentor.user.premiumAccess, true);

  premiumStore.revokeDonor(owner.user, "learner@example.com");
  const after = auth.login({ email: "learner@example.com", password: "password123" });
  assert.equal(after.user.premiumAccess, false);

  db.close();
  fs.unlinkSync(dbPath);
});
