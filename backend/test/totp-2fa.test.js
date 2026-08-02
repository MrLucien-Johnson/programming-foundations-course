const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { authenticator } = require("otplib");

process.env.JWT_SECRET = "test-secret-for-totp";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-totp-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "*";

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");

test("totp setup, confirm, login challenge, backup code, and disable", async () => {
  const dbPath = path.join(os.tmpdir(), `pf-totp-${Date.now()}-${Math.random()}.sqlite`);
  const db = openDatabase(dbPath);
  const auth = createAuth({ db, jwtSecret: process.env.JWT_SECRET });
  const email = `totp-${Date.now()}@example.com`;
  const password = "password123";

  const registered = auth.register({ email, password, displayName: "Totp User" });
  assert.equal(registered.user.totpEnabled, false);

  const setup = await auth.beginTotpSetup(registered.user.id);
  assert.ok(setup.secret);
  assert.ok(setup.otpauthUrl.includes("otpauth://"));
  assert.ok(setup.qrDataUrl.startsWith("data:image/"));

  const code = authenticator.generate(setup.secret);
  const confirmed = auth.confirmTotpSetup(registered.user.id, { code });
  assert.equal(confirmed.user.totpEnabled, true);
  assert.equal(confirmed.backupCodes.length, 8);

  const challenged = auth.login({ email, password });
  assert.equal(challenged.requiresTotp, true);
  assert.ok(challenged.totpToken);
  assert.equal(challenged.token, undefined);

  const bad = () => auth.loginWithTotp({ totpToken: challenged.totpToken, code: "000000" });
  assert.throws(bad, /Invalid authenticator or backup code/);

  const liveCode = authenticator.generate(setup.secret);
  const signedIn = auth.loginWithTotp({
    totpToken: challenged.totpToken,
    code: liveCode,
  });
  assert.ok(signedIn.token);
  assert.equal(signedIn.user.totpEnabled, true);

  const challenged2 = auth.login({ email, password });
  const backup = confirmed.backupCodes[0];
  const viaBackup = auth.loginWithTotp({
    totpToken: challenged2.totpToken,
    code: backup,
  });
  assert.ok(viaBackup.token);
  assert.equal(viaBackup.usedBackup, true);
  assert.equal(viaBackup.remainingBackupCodes, 7);

  const liveCode2 = authenticator.generate(setup.secret);
  const disabled = auth.disableTotp(registered.user.id, {
    password,
    code: liveCode2,
  });
  assert.equal(disabled.user.totpEnabled, false);

  const plainLogin = auth.login({ email, password });
  assert.ok(plainLogin.token);
  assert.equal(plainLogin.requiresTotp, undefined);

  db.close();
  fs.unlinkSync(dbPath);
});
