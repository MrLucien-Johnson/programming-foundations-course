const express = require("express");

/** GDPR-friendly self-service: export my data, delete my account. */
function createAccountRouter({ db, requireAuth, audit }) {
  const router = express.Router();
  router.use(requireAuth);

  const getUser = db.prepare(
    `SELECT id, email, display_name, created_at, totp_enabled FROM users WHERE id = ?`
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
    return res.json({
      exportedAt: new Date().toISOString(),
      account: user
        ? {
            id: user.id,
            email: user.email,
            displayName: user.display_name,
            createdAt: user.created_at,
            totpEnabled: Number(user.totp_enabled) === 1,
          }
        : null,
      progress,
      quizAttempts: getAttempts.all(uid),
      certificates: getCerts.all(uid),
      memberships: getMemberships.all(uid),
    });
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
