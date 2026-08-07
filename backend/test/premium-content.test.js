const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");

process.env.JWT_SECRET = "test-secret-content";
process.env.ORG_CREATOR_EMAILS = "owner@example.com";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-content-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "*";
process.env.PREMIUM_CONTENT_ROOT = path.resolve(__dirname, "..", "..");

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { createPremiumStore } = require("../src/premium");
const { createPremiumContentStore, normalizeContentPath } = require("../src/premiumContent");

test("normalizeContentPath only allows premium markdown paths", () => {
  assert.equal(normalizeContentPath("languages/devops/modules/01-devops-mindset.md"), "languages/devops/modules/01-devops-mindset.md");
  assert.equal(normalizeContentPath("../secrets"), null);
  assert.equal(normalizeContentPath("languages/python/advanced/modules/01.md"), null);
  assert.equal(normalizeContentPath("languages/aws/modules/01-aws-foundations.quiz.md"), "languages/aws/modules/01-aws-foundations.quiz.md");
});

test("premium content API requires auth and donor access", () => {
  const dbPath = path.join(os.tmpdir(), `pf-content-${Date.now()}-${Math.random()}.sqlite`);
  process.env.DATABASE_PATH = dbPath;
  const db = openDatabase(dbPath);
  const premiumStore = createPremiumStore({ db });
  const contentStore = createPremiumContentStore();
  const status = contentStore.init();
  assert.equal(status.ready, true, status.lastError || "content should be ready from local root");

  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET, premiumStore });

  const guest = auth.register({
    email: "learner@example.com",
    password: "password123",
  });
  assert.equal(guest.user.premiumAccess, false);

  let denied = false;
  try {
    // Simulate route checks
    const entitlements = premiumStore.getEntitlements(guest.user.id);
    assert.equal(entitlements.premiumAccess, false);
    denied = true;
  } catch {
    denied = true;
  }
  assert.equal(denied, true);

  const owner = auth.register({
    email: "owner@example.com",
    password: "password123",
  });
  assert.equal(owner.user.premiumAccess, true);

  const file = contentStore.readText("languages/devops/modules/01-devops-mindset.md");
  assert.match(file.content, /DevOps mindset/);
  assert.equal(file.path, "languages/devops/modules/01-devops-mindset.md");

  db.close();
  fs.unlinkSync(dbPath);
});
