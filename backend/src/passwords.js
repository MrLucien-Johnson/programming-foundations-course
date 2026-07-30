/**
 * Password hashing — OWASP Password Storage Cheat Sheet:
 * prefer Argon2id; keep bcrypt verify for hashes created before this upgrade.
 *
 * Stored formats:
 * - Argon2id: native `$argon2id$…` strings from the argon2 package
 * - Legacy bcrypt: `$2a$` / `$2b$` / `$2y$` from bcryptjs
 */
const argon2 = require("argon2");
const bcrypt = require("bcryptjs");

/** OWASP-aligned Argon2id parameters (memory in KiB). */
const ARGON2_OPTIONS = {
  type: argon2.argon2id,
  memoryCost: 65536, // 64 MiB
  timeCost: 3,
  parallelism: 1,
};

/** Dummy bcrypt hash so missing-user logins still pay a comparable cost. */
const DUMMY_BCRYPT_HASH = bcrypt.hashSync("timing-dummy-not-a-real-password", 10);

function isBcryptHash(hash) {
  return typeof hash === "string" && /^\$2[aby]\$/.test(hash);
}

function isArgon2Hash(hash) {
  return typeof hash === "string" && hash.startsWith("$argon2");
}

async function hashPassword(password) {
  return argon2.hash(password, ARGON2_OPTIONS);
}

/**
 * Verifies a password against a stored hash.
 * Returns { ok, needsRehash } — needsRehash is true for legacy bcrypt or weaker params.
 */
async function verifyPassword(password, storedHash) {
  if (!storedHash || typeof storedHash !== "string") {
    await bcrypt.compare(password, DUMMY_BCRYPT_HASH);
    return { ok: false, needsRehash: false };
  }

  if (isArgon2Hash(storedHash)) {
    try {
      const ok = await argon2.verify(storedHash, password);
      const needsRehash = ok && argon2.needsRehash(storedHash, ARGON2_OPTIONS);
      return { ok, needsRehash: !!needsRehash };
    } catch {
      return { ok: false, needsRehash: false };
    }
  }

  if (isBcryptHash(storedHash)) {
    const ok = bcrypt.compareSync(password, storedHash);
    // Successful bcrypt login should upgrade to Argon2id on next write.
    return { ok, needsRehash: ok };
  }

  // Unknown algorithm — still burn time, then fail closed.
  await bcrypt.compare(password, DUMMY_BCRYPT_HASH);
  return { ok: false, needsRehash: false };
}

/** Constant-ish cost when no user row exists (mitigates email enumeration timing). */
async function burnVerifyCost(password) {
  await bcrypt.compare(password || "", DUMMY_BCRYPT_HASH);
}

module.exports = {
  hashPassword,
  verifyPassword,
  burnVerifyCost,
  isBcryptHash,
  isArgon2Hash,
  ARGON2_OPTIONS,
};
