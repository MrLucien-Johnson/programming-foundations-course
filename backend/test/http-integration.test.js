const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");
const crypto = require("crypto");

process.env.JWT_SECRET = "http-test-secret";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-http-${crypto.randomUUID()}.sqlite`);
process.env.CORS_ORIGINS = "*";

const { app } = require("../src/server");

let server;
let base;

test.before(async () => {
  await new Promise((resolve) => {
    server = app.listen(0, "127.0.0.1", resolve);
  });
  const { port } = server.address();
  base = `http://127.0.0.1:${port}`;
});

test.after(() => {
  server && server.close();
  try {
    fs.unlinkSync(process.env.DATABASE_PATH);
  } catch {
    /* ignore */
  }
});

async function api(pathname, { method = "GET", token, body } = {}) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers.Authorization = `Bearer ${token}`;
  const res = await fetch(`${base}${pathname}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let json;
  try {
    json = text ? JSON.parse(text) : {};
  } catch {
    json = { raw: text };
  }
  return { status: res.status, json, text, res };
}

test("full org-grade HTTP flow", async () => {
  const health = await api("/api/health");
  assert.equal(health.status, 200);
  assert.equal(health.json.ok, true);

  const email = `owner-${Date.now()}@example.com`;
  const reg = await api("/api/auth/register", {
    method: "POST",
    body: { email, password: "password123", displayName: "Owner" },
  });
  assert.equal(reg.status, 201);
  const token = reg.json.token;
  assert.ok(token);

  // Create org.
  const created = await api("/api/orgs", { method: "POST", token, body: { name: "HTTP Academy" } });
  assert.equal(created.status, 201);
  const orgId = created.json.org.id;
  assert.equal(created.json.org.role, "admin");

  // Invite a member.
  const invite = await api(`/api/orgs/${orgId}/members`, {
    method: "POST",
    token,
    body: { email: "invitee@example.com", role: "learner" },
  });
  assert.equal(invite.status, 201);
  assert.equal(invite.json.member.status, "invited");

  // Assign a path.
  const assign = await api(`/api/orgs/${orgId}/assignments`, {
    method: "POST",
    token,
    body: { courseName: "Python Course" },
  });
  assert.equal(assign.status, 201);

  // Log a quiz attempt then check analytics reflects it.
  const attempt = await api("/api/quiz-attempts", {
    method: "POST",
    token,
    body: { quizPath: "python/q1.md", courseName: "Python Course", score: 8, total: 10 },
  });
  assert.equal(attempt.status, 201);

  const analytics = await api(`/api/orgs/${orgId}/analytics`, { token });
  assert.equal(analytics.status, 200);
  assert.equal(analytics.json.analytics.quizAttempts, 1);
  assert.equal(analytics.json.analytics.assignments, 1);

  // Roster CSV.
  const roster = await api(`/api/orgs/${orgId}/roster.csv`, { token });
  assert.equal(roster.status, 200);
  assert.match(roster.text, /Email,Name,Role/);

  // Certificate issue + public verify (no token).
  const cert = await api("/api/certificates", {
    method: "POST",
    token,
    body: { learnerName: "Owner Person", courseName: "Python Course" },
  });
  assert.equal(cert.status, 201);
  const verifyId = cert.json.certificate.verifyId;
  const verify = await api(`/api/certificates/verify/${verifyId}`);
  assert.equal(verify.status, 200);
  assert.equal(verify.json.valid, true);

  // Account export.
  const exported = await api("/api/account/export", { token });
  assert.equal(exported.status, 200);
  assert.equal(exported.json.account.email, email);
  assert.equal(exported.json.certificates.length, 1);
  assert.equal(exported.json.quizAttempts.length, 1);

  // Non-member cannot read org.
  const other = await api("/api/auth/register", {
    method: "POST",
    body: { email: `other-${Date.now()}@example.com`, password: "password123" },
  });
  const forbidden = await api(`/api/orgs/${orgId}/members`, { token: other.json.token });
  assert.equal(forbidden.status, 403);

  // Delete account.
  const del = await api("/api/account", { method: "DELETE", token });
  assert.equal(del.status, 200);
  const afterDelete = await api("/api/auth/me", { token });
  assert.equal(afterDelete.status, 401);
});
