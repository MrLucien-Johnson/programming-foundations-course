const crypto = require("crypto");

const ROLES = ["admin", "learner"];

function httpError(message, status) {
  const err = new Error(message);
  err.status = status;
  return err;
}

function normalizeEmail(value) {
  return String(value || "").trim().toLowerCase();
}

/**
 * Data access + rules for organisations, memberships, roles, and assignments.
 * Kept framework-free so it can be unit tested directly (see auth.js pattern).
 */
function createOrgStore({ db, audit }) {
  const now = () => new Date().toISOString();

  const insertOrg = db.prepare(`
    INSERT INTO orgs (id, name, plan, created_by, created_at, updated_at)
    VALUES (@id, @name, @plan, @created_by, @created_at, @updated_at)
  `);
  const insertMembership = db.prepare(`
    INSERT INTO memberships (id, org_id, user_id, invited_email, role, status, created_at, updated_at)
    VALUES (@id, @org_id, @user_id, @invited_email, @role, @status, @created_at, @updated_at)
  `);
  const getOrg = db.prepare(`SELECT * FROM orgs WHERE id = ?`);
  const getMembership = db.prepare(
    `SELECT * FROM memberships WHERE org_id = ? AND user_id = ?`
  );
  const getMembershipByEmail = db.prepare(
    `SELECT * FROM memberships WHERE org_id = ? AND invited_email = ?`
  );
  const listMembershipsForUser = db.prepare(
    `SELECT * FROM memberships WHERE user_id = ? ORDER BY created_at ASC`
  );
  const listMembershipsForOrg = db.prepare(
    `SELECT * FROM memberships WHERE org_id = ? ORDER BY created_at ASC`
  );
  const countAdmins = db.prepare(
    `SELECT COUNT(*) AS n FROM memberships WHERE org_id = ? AND role = 'admin' AND status = 'active'`
  );
  const findUserByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findUserById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const getProgressRow = db.prepare(
    `SELECT payload, updated_at FROM progress WHERE user_id = ?`
  );

  const insertAssignment = db.prepare(`
    INSERT INTO path_assignments (id, org_id, user_id, course_name, assigned_by, created_at)
    VALUES (@id, @org_id, @user_id, @course_name, @assigned_by, @created_at)
  `);
  const listAssignmentsForOrg = db.prepare(
    `SELECT * FROM path_assignments WHERE org_id = ? ORDER BY created_at ASC`
  );
  const listQuizAttemptsForUser = db.prepare(
    `SELECT * FROM quiz_attempts WHERE user_id = ? ORDER BY created_at ASC`
  );

  function publicOrg(row, role) {
    return {
      id: row.id,
      name: row.name,
      plan: row.plan,
      createdAt: row.created_at,
      ...(role ? { role } : {}),
    };
  }

  function requireMembership(orgId, userId) {
    const org = getOrg.get(orgId);
    if (!org) throw httpError("Organisation not found.", 404);
    const membership = getMembership.get(orgId, userId);
    if (!membership || membership.status !== "active") {
      throw httpError("You are not a member of this organisation.", 403);
    }
    return { org, membership };
  }

  function requireAdmin(orgId, userId) {
    const { org, membership } = requireMembership(orgId, userId);
    if (membership.role !== "admin") {
      throw httpError("Admin role required for this action.", 403);
    }
    return { org, membership };
  }

  function createOrg({ userId, name }) {
    const trimmed = String(name || "").trim();
    if (trimmed.length < 2 || trimmed.length > 120) {
      throw httpError("Organisation name must be 2–120 characters.", 400);
    }
    const ts = now();
    const org = {
      id: crypto.randomUUID(),
      name: trimmed,
      plan: "free",
      created_by: userId,
      created_at: ts,
      updated_at: ts,
    };
    insertOrg.run(org);
    insertMembership.run({
      id: crypto.randomUUID(),
      org_id: org.id,
      user_id: userId,
      invited_email: null,
      role: "admin",
      status: "active",
      created_at: ts,
      updated_at: ts,
    });
    audit && audit.log({ orgId: org.id, actorId: userId, action: "org.create", meta: { name: trimmed } });
    return publicOrg(org, "admin");
  }

  function listOrgsForUser(userId) {
    return listMembershipsForUser
      .all(userId)
      .filter((m) => m.status === "active")
      .map((m) => {
        const org = getOrg.get(m.org_id);
        return org ? publicOrg(org, m.role) : null;
      })
      .filter(Boolean);
  }

  function progressSummary(userId) {
    const row = getProgressRow.get(userId);
    if (!row) return { completions: 0, updatedAt: null };
    try {
      const payload = JSON.parse(row.payload);
      return {
        completions: Array.isArray(payload.completions) ? payload.completions.length : 0,
        updatedAt: row.updated_at,
      };
    } catch {
      return { completions: 0, updatedAt: row.updated_at };
    }
  }

  function listMembers(orgId, actorId) {
    requireAdmin(orgId, actorId);
    return listMembershipsForOrg.all(orgId).map((m) => {
      const user = m.user_id ? findUserById.get(m.user_id) : null;
      const summary = m.user_id ? progressSummary(m.user_id) : { completions: 0, updatedAt: null };
      return {
        membershipId: m.id,
        userId: m.user_id,
        email: user ? user.email : m.invited_email,
        displayName: user ? user.display_name : "",
        role: m.role,
        status: m.status,
        joinedAt: m.created_at,
        completions: summary.completions,
        lastActive: summary.updatedAt,
      };
    });
  }

  function addMember({ orgId, actorId, email, role = "learner" }) {
    requireAdmin(orgId, actorId);
    const cleanEmail = normalizeEmail(email);
    if (!cleanEmail || !cleanEmail.includes("@")) {
      throw httpError("A valid email is required to add a member.", 400);
    }
    if (!ROLES.includes(role)) throw httpError("Role must be admin or learner.", 400);

    const existingUser = findUserByEmail.get(cleanEmail);
    if (existingUser) {
      const already = getMembership.get(orgId, existingUser.id);
      if (already) throw httpError("That person is already a member.", 409);
      const ts = now();
      insertMembership.run({
        id: crypto.randomUUID(),
        org_id: orgId,
        user_id: existingUser.id,
        invited_email: null,
        role,
        status: "active",
        created_at: ts,
        updated_at: ts,
      });
      audit && audit.log({ orgId, actorId, action: "member.add", meta: { email: cleanEmail, role, status: "active" } });
      return { email: cleanEmail, role, status: "active", userId: existingUser.id };
    }

    const pending = getMembershipByEmail.get(orgId, cleanEmail);
    if (pending) throw httpError("That email is already invited.", 409);
    const ts = now();
    insertMembership.run({
      id: crypto.randomUUID(),
      org_id: orgId,
      user_id: null,
      invited_email: cleanEmail,
      role,
      status: "invited",
      created_at: ts,
      updated_at: ts,
    });
    audit && audit.log({ orgId, actorId, action: "member.invite", meta: { email: cleanEmail, role } });
    return { email: cleanEmail, role, status: "invited", userId: null };
  }

  function updateMemberRole({ orgId, actorId, targetUserId, role }) {
    requireAdmin(orgId, actorId);
    if (!ROLES.includes(role)) throw httpError("Role must be admin or learner.", 400);
    const target = getMembership.get(orgId, targetUserId);
    if (!target) throw httpError("Member not found.", 404);
    if (target.role === "admin" && role !== "admin" && countAdmins.get(orgId).n <= 1) {
      throw httpError("An organisation must keep at least one admin.", 400);
    }
    db.prepare(
      `UPDATE memberships SET role = ?, updated_at = ? WHERE id = ?`
    ).run(role, now(), target.id);
    audit && audit.log({ orgId, actorId, action: "member.role", meta: { targetUserId, role } });
    return { userId: targetUserId, role };
  }

  function removeMember({ orgId, actorId, targetUserId }) {
    requireAdmin(orgId, actorId);
    const target = getMembership.get(orgId, targetUserId);
    if (!target) throw httpError("Member not found.", 404);
    if (target.role === "admin" && countAdmins.get(orgId).n <= 1) {
      throw httpError("You cannot remove the last admin.", 400);
    }
    db.prepare(`DELETE FROM memberships WHERE id = ?`).run(target.id);
    audit && audit.log({ orgId, actorId, action: "member.remove", meta: { targetUserId } });
    return { removed: true };
  }

  /** Claims any pending email invites for a newly registered / signing-in user. */
  function attachInvites(userId, email) {
    const cleanEmail = normalizeEmail(email);
    if (!cleanEmail) return 0;
    const pending = db
      .prepare(`SELECT * FROM memberships WHERE invited_email = ? AND user_id IS NULL`)
      .all(cleanEmail);
    let claimed = 0;
    for (const m of pending) {
      const already = getMembership.get(m.org_id, userId);
      if (already) {
        db.prepare(`DELETE FROM memberships WHERE id = ?`).run(m.id);
        continue;
      }
      db.prepare(
        `UPDATE memberships SET user_id = ?, invited_email = NULL, status = 'active', updated_at = ? WHERE id = ?`
      ).run(userId, now(), m.id);
      audit && audit.log({ orgId: m.org_id, actorId: userId, action: "member.join", meta: { email: cleanEmail } });
      claimed += 1;
    }
    return claimed;
  }

  function assignPath({ orgId, actorId, courseName, userId = null }) {
    requireAdmin(orgId, actorId);
    const clean = String(courseName || "").trim();
    if (!clean) throw httpError("A course name is required to assign a path.", 400);
    if (userId) {
      const target = getMembership.get(orgId, userId);
      if (!target || target.status !== "active") {
        throw httpError("Assign to an active member of this organisation.", 400);
      }
    }
    const row = {
      id: crypto.randomUUID(),
      org_id: orgId,
      user_id: userId,
      course_name: clean,
      assigned_by: actorId,
      created_at: now(),
    };
    insertAssignment.run(row);
    audit && audit.log({ orgId, actorId, action: "path.assign", meta: { courseName: clean, userId } });
    return {
      id: row.id,
      courseName: clean,
      userId,
      scope: userId ? "member" : "org",
      createdAt: row.created_at,
    };
  }

  /** Assignments visible to a member: org-wide plus their own. Admins see all. */
  function listAssignments(orgId, userId) {
    const { membership } = requireMembership(orgId, userId);
    const all = listAssignmentsForOrg.all(orgId);
    const visible =
      membership.role === "admin"
        ? all
        : all.filter((a) => a.user_id === null || a.user_id === userId);
    return visible.map((a) => ({
      id: a.id,
      courseName: a.course_name,
      userId: a.user_id,
      scope: a.user_id ? "member" : "org",
      createdAt: a.created_at,
    }));
  }

  function setPlan({ orgId, actorId, plan }) {
    requireAdmin(orgId, actorId);
    const allowed = ["free", "team", "school", "enterprise"];
    const clean = String(plan || "").trim().toLowerCase();
    if (!allowed.includes(clean)) {
      throw httpError(`Plan must be one of: ${allowed.join(", ")}.`, 400);
    }
    db.prepare(`UPDATE orgs SET plan = ?, updated_at = ? WHERE id = ?`).run(clean, now(), orgId);
    audit && audit.log({ orgId, actorId, action: "org.plan", meta: { plan: clean } });
    return { plan: clean };
  }

  function analytics(orgId, actorId) {
    requireAdmin(orgId, actorId);
    const members = listMembershipsForOrg.all(orgId);
    const active = members.filter((m) => m.status === "active" && m.user_id);
    let totalCompletions = 0;
    let totalAttempts = 0;
    let passedAttempts = 0;
    for (const m of active) {
      totalCompletions += progressSummary(m.user_id).completions;
      const attempts = listQuizAttemptsForUser.all(m.user_id);
      totalAttempts += attempts.length;
      passedAttempts += attempts.filter((a) => a.passed).length;
    }
    return {
      members: members.length,
      activeMembers: active.length,
      invited: members.filter((m) => m.status === "invited").length,
      admins: members.filter((m) => m.role === "admin").length,
      assignments: listAssignmentsForOrg.all(orgId).length,
      totalCompletions,
      quizAttempts: totalAttempts,
      quizPassRate: totalAttempts ? Math.round((passedAttempts / totalAttempts) * 100) : 0,
    };
  }

  function rosterRows(orgId, actorId) {
    requireAdmin(orgId, actorId);
    return listMembers(orgId, actorId).map((m) => ({
      email: m.email || "",
      displayName: m.displayName || "",
      role: m.role,
      status: m.status,
      completions: m.completions,
      lastActive: m.lastActive || "",
      joinedAt: m.joinedAt,
    }));
  }

  function gradebookRows(orgId, actorId) {
    requireAdmin(orgId, actorId);
    const members = listMembershipsForOrg.all(orgId).filter((m) => m.user_id);
    const rows = [];
    for (const m of members) {
      const user = findUserById.get(m.user_id);
      const attempts = listQuizAttemptsForUser.all(m.user_id);
      for (const a of attempts) {
        rows.push({
          email: user ? user.email : "",
          displayName: user ? user.display_name : "",
          courseName: a.course_name || "",
          quizPath: a.quiz_path,
          score: a.score,
          total: a.total,
          passed: a.passed ? "yes" : "no",
          attemptedAt: a.created_at,
        });
      }
    }
    return rows;
  }

  function getAuditEvents(orgId, actorId, limit) {
    requireAdmin(orgId, actorId);
    return audit ? audit.recent(orgId, limit) : [];
  }

  return {
    ROLES,
    createOrg,
    listOrgsForUser,
    requireMembership,
    requireAdmin,
    listMembers,
    addMember,
    updateMemberRole,
    removeMember,
    attachInvites,
    assignPath,
    listAssignments,
    setPlan,
    analytics,
    rosterRows,
    gradebookRows,
    getAuditEvents,
  };
}

function toCsv(rows, columns) {
  const escape = (value) => {
    const s = value == null ? "" : String(value);
    if (/[",\n\r]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
    return s;
  };
  const header = columns.map((c) => escape(c.label)).join(",");
  const body = rows
    .map((row) => columns.map((c) => escape(row[c.key])).join(","))
    .join("\r\n");
  return body ? `${header}\r\n${body}\r\n` : `${header}\r\n`;
}

module.exports = { createOrgStore, toCsv, ROLES };
