const express = require("express");

/** GDPR-friendly self-service: export my data, delete my account + premium grants. */
function createAccountRouter({ db, requireAuth, audit, premiumStore }) {
  const router = express.Router();
  router.use(requireAuth);

  const getUser = db.prepare(
    `SELECT id, email, display_name, created_at, totp_enabled, is_donor, donor_note FROM users WHERE id = ?`
  );
  const getProgress = db.prepare(`SELECT payload, updated_at FROM progress WHERE user_id = ?`);
  const getAttempts = db.prepare(
    `SELECT quiz_path, course_name, score, total, passed, created_at FROM quiz_attempts WHERE user_id = ?`
  );
  const getCerts = db.prepare(
    `SELECT verify_id, learner_name, course_name, issued_at FROM certificates WHERE user_id = ?`
  );
  const getMemberships = db.prepare(
    `SELECT m.role, m.status, m.created_at, o.id AS org_id, o.name AS org_name
     FROM memberships m JOIN orgs o ON o.id = m.org_id WHERE m.user_id = ?`
  );
  const deleteUser = db.prepare(`DELETE FROM users WHERE id = ?`);

  router.get("/export", (req, res) => {
    const uid = req.user.id;
    const user = getUser.get(uid);
    const progressRow = getProgress.get(uid);
    let progress = null;
    if (progressRow) {
      try {
        progress = JSON.parse(progressRow.payload);
      } catch {
        progress = null;
      }
    }
    const entitlements = premiumStore
      ? premiumStore.entitlementsForRow(user)
      : { premiumAccess: false, isDonor: false };
    return res.json({
      exportedAt: new Date().toISOString(),
      account: user
        ? {
            id: user.id,
            email: user.email,
            displayName: user.display_name,
            createdAt: user.created_at,
            totpEnabled: Number(user.totp_enabled) === 1,
            isDonor: !!entitlements.isDonor,
            premiumAccess: !!entitlements.premiumAccess,
          }
        : null,
      progress,
      quizAttempts: getAttempts.all(uid),
      certificates: getCerts.all(uid),
      memberships: getMemberships.all(uid),
    });
  });

  router.get("/entitlements", (req, res) => {
    if (!premiumStore) {
      return res.json({ premiumAccess: false, isDonor: false, allowlisted: false, reason: "unavailable" });
    }
    return res.json(premiumStore.getEntitlements(req.user.id));
  });

  router.post("/premium/grant", (req, res) => {
    try {
      if (!premiumStore) {
        return res.status(503).json({ error: "Premium access is not configured on this API." });
      }
      const email = req.body && req.body.email;
      const note = req.body && req.body.note;
      const result = premiumStore.grantDonor(req.user, email, note);
      return res.json({ ok: true, entitlements: result, email: String(email || "").trim().toLowerCase() });
    } catch (error) {
      return res.status(error.status || 500).json({ error: error.message || "Could not grant access." });
    }
  });

  router.post("/premium/revoke", (req, res) => {
    try {
      if (!premiumStore) {
        return res.status(503).json({ error: "Premium access is not configured on this API." });
      }
      const email = req.body && req.body.email;
      const result = premiumStore.revokeDonor(req.user, email);
      return res.json({ ok: true, entitlements: result, email: String(email || "").trim().toLowerCase() });
    } catch (error) {
      return res.status(error.status || 500).json({ error: error.message || "Could not revoke access." });
    }
  });

  router.delete("/", (req, res) => {
    const uid = req.user.id;
    // Foreign keys cascade progress, quiz_attempts, and memberships.
    deleteUser.run(uid);
    audit && audit.log({ actorId: uid, action: "account.delete", meta: {} });
    return res.json({ deleted: true });
  });

  return router;
}

module.exports = { createAccountRouter };
