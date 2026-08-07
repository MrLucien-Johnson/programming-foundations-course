const crypto = require("crypto");

function normalizeEmail(value) {
  return String(value || "").trim().toLowerCase();
}

function parseEmailList(raw) {
  return String(raw || "")
    .split(",")
    .map(normalizeEmail)
    .filter(Boolean);
}

/**
 * Emails that always unlock donor/premium courses.
 * Combines ORG_CREATOR_EMAILS (site owner) + PREMIUM_ACCESS_EMAILS (extra allowlist).
 * Fail-closed for the allowlist itself; donors still get access via users.is_donor.
 */
function premiumAllowlist() {
  return [
    ...new Set([
      ...parseEmailList(process.env.ORG_CREATOR_EMAILS),
      ...parseEmailList(process.env.PREMIUM_ACCESS_EMAILS),
    ]),
  ];
}

function isPremiumAllowlistedEmail(email) {
  const clean = normalizeEmail(email);
  if (!clean) return false;
  return premiumAllowlist().includes(clean);
}

function createPremiumStore({ db, audit }) {
  const findByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const setDonor = db.prepare(
    `UPDATE users SET is_donor = @is_donor, donor_note = @donor_note, updated_at = @updated_at WHERE id = @id`
  );

  function entitlementsForRow(row) {
    if (!row) {
      return {
        premiumAccess: false,
        isDonor: false,
        allowlisted: false,
        reason: "signed-out",
      };
    }
    const allowlisted = isPremiumAllowlistedEmail(row.email);
    const isDonor = Number(row.is_donor) === 1;
    return {
      premiumAccess: allowlisted || isDonor,
      isDonor,
      allowlisted,
      reason: allowlisted ? "allowlist" : isDonor ? "donor" : "none",
    };
  }

  function getEntitlements(userId) {
    const row = findById.get(userId);
    return entitlementsForRow(row);
  }

  function canManagePremium(actorEmail) {
    return isPremiumAllowlistedEmail(actorEmail);
  }

  function grantDonor(actor, targetEmail, note) {
    if (!canManagePremium(actor.email)) {
      const err = new Error("Only the site owner / allowlisted admins can grant donor access.");
      err.status = 403;
      throw err;
    }
    const email = normalizeEmail(targetEmail);
    if (!email) {
      const err = new Error("Enter an email address to grant.");
      err.status = 400;
      throw err;
    }
    const row = findByEmail.get(email);
    if (!row) {
      const err = new Error(
        "That email does not have an account yet. Ask them to create a free account first, then grant again."
      );
      err.status = 404;
      throw err;
    }
    setDonor.run({
      id: row.id,
      is_donor: 1,
      donor_note: String(note || "Granted by site owner").slice(0, 200),
      updated_at: new Date().toISOString(),
    });
    if (audit) {
      audit.log({
        actorId: actor.id,
        action: "premium.grant_donor",
        meta: { targetEmail: email, targetUserId: row.id },
      });
    }
    return entitlementsForRow(findById.get(row.id));
  }

  function revokeDonor(actor, targetEmail) {
    if (!canManagePremium(actor.email)) {
      const err = new Error("Only the site owner / allowlisted admins can revoke donor access.");
      err.status = 403;
      throw err;
    }
    const email = normalizeEmail(targetEmail);
    const row = findByEmail.get(email);
    if (!row) {
      const err = new Error("No account found for that email.");
      err.status = 404;
      throw err;
    }
    setDonor.run({
      id: row.id,
      is_donor: 0,
      donor_note: "",
      updated_at: new Date().toISOString(),
    });
    if (audit) {
      audit.log({
        actorId: actor.id,
        action: "premium.revoke_donor",
        meta: { targetEmail: email, targetUserId: row.id },
      });
    }
    return entitlementsForRow(findById.get(row.id));
  }

  return {
    getEntitlements,
    grantDonor,
    revokeDonor,
    canManagePremium,
    entitlementsForRow,
  };
}

module.exports = {
  createPremiumStore,
  isPremiumAllowlistedEmail,
  premiumAllowlist,
  normalizeEmail,
};
