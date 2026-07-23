const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const os = require("os");
const path = require("path");
const crypto = require("crypto");

const { openDatabase } = require("../src/db");
const { createAuth } = require("../src/auth");
const { createAudit } = require("../src/audit");
const { createOrgStore, toCsv } = require("../src/orgs");
const { createCertificateStore } = require("../src/certificates");

// Org creation / admin role are allowlisted by email (fail-closed). Include the
// fixed test admin emails used below so existing org-flow tests keep passing.
process.env.ORG_CREATOR_EMAILS = "admin@example.com,teacher@example.com,solo@example.com,learner@example.com";

function freshDb() {
  const file = path.join(os.tmpdir(), `pf-org-${crypto.randomUUID()}.sqlite`);
  const db = openDatabase(file);
  return { db, file };
}

function makeUser(auth, email) {
  return auth.register({ email, password: "password123", displayName: email.split("@")[0] }).user;
}

test("org lifecycle: create, roles, invites, assignments", () => {
  const { db, file } = freshDb();
  const audit = createAudit(db);
  const orgStore = createOrgStore({ db, audit });
  const auth = createAuth({
    db,
    jwtSecret: "test",
    onAuthenticated: (u) => orgStore.attachInvites(u.id, u.email),
  });

  const admin = makeUser(auth, "admin@example.com");
  const learner = makeUser(auth, "learner@example.com");

  const org = orgStore.createOrg({ userId: admin.id, name: "Acme School" });
  assert.equal(org.role, "admin");
  assert.equal(org.plan, "free");

  // Creator sees org; learner does not yet.
  assert.equal(orgStore.listOrgsForUser(admin.id).length, 1);
  assert.equal(orgStore.listOrgsForUser(learner.id).length, 0);

  // Add existing user -> active immediately.
  const added = orgStore.addMember({ orgId: org.id, actorId: admin.id, email: "learner@example.com" });
  assert.equal(added.status, "active");
  assert.equal(orgStore.listOrgsForUser(learner.id).length, 1);

  // Duplicate add rejected.
  assert.throws(
    () => orgStore.addMember({ orgId: org.id, actorId: admin.id, email: "learner@example.com" }),
    /already a member/
  );

  // Learner cannot list members (admin only).
  assert.throws(() => orgStore.listMembers(org.id, learner.id), /Admin role required/);

  // Invite a not-yet-registered email -> pending until they register.
  const invited = orgStore.addMember({ orgId: org.id, actorId: admin.id, email: "new@example.com", role: "learner" });
  assert.equal(invited.status, "invited");

  const members = orgStore.listMembers(org.id, admin.id);
  assert.equal(members.length, 3);
  assert.ok(members.find((m) => m.email === "new@example.com" && m.status === "invited"));

  // Registering the invited email claims the membership.
  const claimed = makeUser(auth, "new@example.com");
  const claimedOrgs = orgStore.listOrgsForUser(claimed.id);
  assert.equal(claimedOrgs.length, 1);

  // Promote learner to admin, then guard the last admin.
  orgStore.updateMemberRole({ orgId: org.id, actorId: admin.id, targetUserId: learner.id, role: "admin" });
  const afterPromote = orgStore.listMembers(org.id, admin.id).find((m) => m.userId === learner.id);
  assert.equal(afterPromote.role, "admin");

  // Assign a path org-wide and to a specific member.
  orgStore.assignPath({ orgId: org.id, actorId: admin.id, courseName: "Python Course" });
  orgStore.assignPath({ orgId: org.id, actorId: admin.id, courseName: "AI Prompt Creation Course", userId: claimed.id });

  const claimedView = orgStore.listAssignments(org.id, claimed.id);
  // Sees org-wide + their own = 2
  assert.equal(claimedView.length, 2);
  const learnerAdminView = orgStore.listAssignments(org.id, learner.id);
  // learner is now admin -> sees all 2
  assert.equal(learnerAdminView.length, 2);

  // Plan (billing stub).
  const planned = orgStore.setPlan({ orgId: org.id, actorId: admin.id, plan: "school" });
  assert.equal(planned.plan, "school");
  assert.throws(() => orgStore.setPlan({ orgId: org.id, actorId: admin.id, plan: "gold" }), /Plan must be/);

  // Audit events recorded.
  const events = orgStore.getAuditEvents(org.id, admin.id, 100);
  assert.ok(events.length >= 4);
  assert.ok(events.find((e) => e.action === "org.create"));

  db.close();
  fs.unlinkSync(file);
});

test("last admin cannot be removed or demoted", () => {
  const { db, file } = freshDb();
  const orgStore = createOrgStore({ db, audit: createAudit(db) });
  const auth = createAuth({ db, jwtSecret: "test" });
  const admin = makeUser(auth, "solo@example.com");
  const org = orgStore.createOrg({ userId: admin.id, name: "Solo Org" });

  assert.throws(
    () => orgStore.updateMemberRole({ orgId: org.id, actorId: admin.id, targetUserId: admin.id, role: "learner" }),
    /at least one admin/
  );
  assert.throws(
    () => orgStore.removeMember({ orgId: org.id, actorId: admin.id, targetUserId: admin.id }),
    /last admin/
  );
  db.close();
  fs.unlinkSync(file);
});

test("quiz attempts feed analytics and gradebook", () => {
  const { db, file } = freshDb();
  const orgStore = createOrgStore({ db, audit: createAudit(db) });
  const auth = createAuth({ db, jwtSecret: "test" });
  const admin = makeUser(auth, "teacher@example.com");
  const org = orgStore.createOrg({ userId: admin.id, name: "Analytics Org" });
  const student = makeUser(auth, "student@example.com");
  orgStore.addMember({ orgId: org.id, actorId: admin.id, email: "student@example.com" });

  const insert = db.prepare(`
    INSERT INTO quiz_attempts (id, user_id, quiz_path, course_name, score, total, passed, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `);
  insert.run(crypto.randomUUID(), student.id, "python/q1.md", "Python Course", 9, 10, 1, new Date().toISOString());
  insert.run(crypto.randomUUID(), student.id, "python/q2.md", "Python Course", 4, 10, 0, new Date().toISOString());

  const stats = orgStore.analytics(org.id, admin.id);
  assert.equal(stats.quizAttempts, 2);
  assert.equal(stats.quizPassRate, 50);
  assert.equal(stats.activeMembers, 2);

  const gradebook = orgStore.gradebookRows(org.id, admin.id);
  assert.equal(gradebook.length, 2);
  const csv = toCsv(gradebook, [
    { key: "email", label: "Email" },
    { key: "score", label: "Score" },
  ]);
  assert.match(csv, /Email,Score/);
  assert.match(csv, /student@example.com,9/);

  db.close();
  fs.unlinkSync(file);
});

test("certificates issue and publicly verify", () => {
  const { db, file } = freshDb();
  const certStore = createCertificateStore({ db, audit: createAudit(db) });
  const auth = createAuth({ db, jwtSecret: "test" });
  const user = makeUser(auth, "grad@example.com");

  const cert = certStore.issue({ userId: user.id, learnerName: "Ada Lovelace", courseName: "Python Course" });
  assert.match(cert.verifyId, /^PF-[A-Z0-9]{4}-[A-Z0-9]{4}$/);

  const good = certStore.verify(cert.verifyId);
  assert.equal(good.valid, true);
  assert.equal(good.certificate.learnerName, "Ada Lovelace");

  // Case-insensitive lookup, and unknown codes are invalid.
  assert.equal(certStore.verify(cert.verifyId.toLowerCase()).valid, true);
  assert.equal(certStore.verify("PF-0000-0000").valid, false);

  assert.throws(() => certStore.issue({ userId: user.id, learnerName: "x", courseName: "Python" }), /learner name/);

  const mine = certStore.listForUser(user.id);
  assert.equal(mine.length, 1);

  db.close();
  fs.unlinkSync(file);
});

test("org creation is restricted to the ORG_CREATOR_EMAILS allowlist", () => {
  const { db, file } = freshDb();
  const orgStore = createOrgStore({ db, audit: createAudit(db) });
  const auth = createAuth({ db, jwtSecret: "test" });

  const original = process.env.ORG_CREATOR_EMAILS;
  try {
    process.env.ORG_CREATOR_EMAILS = "owner@example.com";

    const outsider = makeUser(auth, "outsider@example.com");
    assert.throws(
      () => orgStore.createOrg({ userId: outsider.id, name: "Rogue Org" }),
      /approved platform admins/
    );

    const owner = makeUser(auth, "owner@example.com");
    const org = orgStore.createOrg({ userId: owner.id, name: "Owner Org" });
    assert.equal(org.role, "admin");

    // Unset/empty allowlist fails closed — no one can create an org.
    process.env.ORG_CREATOR_EMAILS = "";
    assert.throws(
      () => orgStore.createOrg({ userId: owner.id, name: "Another Org" }),
      /approved platform admins/
    );
  } finally {
    process.env.ORG_CREATOR_EMAILS = original;
  }
  db.close();
  fs.unlinkSync(file);
});

test("promoting or adding a member as admin is restricted to the allowlist", () => {
  const { db, file } = freshDb();
  const orgStore = createOrgStore({ db, audit: createAudit(db) });
  const auth = createAuth({ db, jwtSecret: "test" });

  const original = process.env.ORG_CREATOR_EMAILS;
  try {
    process.env.ORG_CREATOR_EMAILS = "owner@example.com";
    const owner = makeUser(auth, "owner@example.com");
    const org = orgStore.createOrg({ userId: owner.id, name: "Gate Org" });

    const learner = makeUser(auth, "learner2@example.com");
    orgStore.addMember({ orgId: org.id, actorId: owner.id, email: learner.email, role: "learner" });

    // Non-allowlisted learner cannot be promoted to admin.
    assert.throws(
      () => orgStore.updateMemberRole({ orgId: org.id, actorId: owner.id, targetUserId: learner.id, role: "admin" }),
      /approved platform admins/
    );

    // Non-allowlisted email cannot be added directly as admin either.
    assert.throws(
      () => orgStore.addMember({ orgId: org.id, actorId: owner.id, email: "new-admin@example.com", role: "admin" }),
      /approved platform admins/
    );

    // Allowlisted second admin can be added and promoted.
    process.env.ORG_CREATOR_EMAILS = "owner@example.com,second-admin@example.com";
    const added = orgStore.addMember({ orgId: org.id, actorId: owner.id, email: "second-admin@example.com", role: "admin" });
    assert.equal(added.role, "admin");
  } finally {
    process.env.ORG_CREATOR_EMAILS = original;
  }
  db.close();
  fs.unlinkSync(file);
});

test("toCsv escapes quotes, commas, and newlines", () => {
  const csv = toCsv(
    [{ a: 'Say "hi"', b: "one,two", c: "line1\nline2" }],
    [
      { key: "a", label: "A" },
      { key: "b", label: "B" },
      { key: "c", label: "C" },
    ]
  );
  assert.match(csv, /"Say ""hi"""/);
  assert.match(csv, /"one,two"/);
  assert.match(csv, /"line1\nline2"/);
});
