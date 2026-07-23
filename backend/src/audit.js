const crypto = require("crypto");

/**
 * Records compliance-friendly audit events (who did what, when).
 * Failures are swallowed so auditing never breaks a user-facing action.
 */
function createAudit(db) {
  const insert = db.prepare(`
    INSERT INTO audit_events (id, org_id, actor_id, action, meta, created_at)
    VALUES (@id, @org_id, @actor_id, @action, @meta, @created_at)
  `);

  const listByOrg = db.prepare(`
    SELECT id, org_id, actor_id, action, meta, created_at
    FROM audit_events
    WHERE org_id = ?
    ORDER BY created_at DESC
    LIMIT ?
  `);

  function log({ orgId = null, actorId = null, action, meta = {} }) {
    try {
      insert.run({
        id: crypto.randomUUID(),
        org_id: orgId,
        actor_id: actorId,
        action: String(action || "unknown"),
        meta: JSON.stringify(meta || {}),
        created_at: new Date().toISOString(),
      });
    } catch {
      // Auditing must never block the primary operation.
    }
  }

  function recent(orgId, limit = 100) {
    return listByOrg.all(orgId, Math.min(Math.max(Number(limit) || 100, 1), 500)).map((row) => ({
      id: row.id,
      orgId: row.org_id,
      actorId: row.actor_id,
      action: row.action,
      meta: safeParse(row.meta),
      createdAt: row.created_at,
    }));
  }

  return { log, recent };
}

function safeParse(value) {
  try {
    return JSON.parse(value);
  } catch {
    return {};
  }
}

module.exports = { createAudit };
