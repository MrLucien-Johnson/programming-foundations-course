const crypto = require("crypto");

function httpError(message, status) {
  const err = new Error(message);
  err.status = status;
  return err;
}

/** Short, human-friendly, hard-to-guess verification code, e.g. PF-7QK2-9ZAM. */
function makeVerifyId() {
  const alphabet = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
  const pick = () =>
    Array.from({ length: 4 }, () => alphabet[crypto.randomInt(0, alphabet.length)]).join("");
  return `PF-${pick()}-${pick()}`;
}

function createCertificateStore({ db, audit }) {
  const insert = db.prepare(`
    INSERT INTO certificates (id, verify_id, user_id, learner_name, course_name, issued_at, revoked)
    VALUES (@id, @verify_id, @user_id, @learner_name, @course_name, @issued_at, 0)
  `);
  const byVerifyId = db.prepare(`SELECT * FROM certificates WHERE verify_id = ?`);
  const byUser = db.prepare(
    `SELECT * FROM certificates WHERE user_id = ? ORDER BY issued_at DESC`
  );

  function issue({ userId, learnerName, courseName }) {
    const name = String(learnerName || "").trim();
    const course = String(courseName || "").trim();
    if (name.length < 2 || name.length > 120) {
      throw httpError("Enter the learner name (2–120 characters).", 400);
    }
    if (!course) throw httpError("A course name is required.", 400);

    let verifyId = makeVerifyId();
    for (let i = 0; i < 5 && byVerifyId.get(verifyId); i += 1) {
      verifyId = makeVerifyId();
    }
    const row = {
      id: crypto.randomUUID(),
      verify_id: verifyId,
      user_id: userId || null,
      learner_name: name,
      course_name: course,
      issued_at: new Date().toISOString(),
    };
    insert.run(row);
    audit && audit.log({ actorId: userId, action: "certificate.issue", meta: { verifyId, courseName: course } });
    return publicCert(row);
  }

  function verify(verifyId) {
    const row = byVerifyId.get(String(verifyId || "").trim().toUpperCase());
    if (!row || row.revoked) return { valid: false };
    return { valid: true, certificate: publicCert(row) };
  }

  function listForUser(userId) {
    return byUser.all(userId).map(publicCert);
  }

  function publicCert(row) {
    return {
      verifyId: row.verify_id,
      learnerName: row.learner_name,
      courseName: row.course_name,
      issuedAt: row.issued_at,
    };
  }

  return { issue, verify, listForUser };
}

module.exports = { createCertificateStore, makeVerifyId };
