const crypto = require("crypto");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { z } = require("zod");
const { authenticator } = require("otplib");
const QRCode = require("qrcode");

const emailSchema = z.string().trim().email().max(254);
const passwordSchema = z.string().min(8).max(128);
const nameSchema = z.string().trim().max(80).optional().default("");
const totpCodeSchema = z
  .string()
  .trim()
  .regex(/^[0-9A-Za-z-]{6,14}$/, "Enter a 6-digit authenticator code or a backup code.");

const ISSUER = "Programming Foundations";
const BACKUP_CODE_COUNT = 8;

function createAuth({ db, jwtSecret, onAuthenticated }) {
  const notifyAuthenticated = (user) => {
    if (typeof onAuthenticated === "function") {
      try {
        onAuthenticated(user);
      } catch {
        // Post-auth hooks (e.g. claiming invites) must not block sign-in.
      }
    }
  };

  const encKey = crypto.createHash("sha256").update(`pf-totp:${jwtSecret}`).digest();

  const insertUser = db.prepare(`
    INSERT INTO users (id, email, display_name, password_hash, created_at, updated_at,
      totp_enabled, totp_secret_enc, totp_pending_enc, totp_backup_hashes)
    VALUES (@id, @email, @display_name, @password_hash, @created_at, @updated_at,
      0, NULL, NULL, NULL)
  `);

  const findByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const updatePasswordHash = db.prepare(`
    UPDATE users SET password_hash = @password_hash, updated_at = @updated_at WHERE id = @id
  `);
  const updateTotpPending = db.prepare(`
    UPDATE users SET totp_pending_enc = @totp_pending_enc, updated_at = @updated_at WHERE id = @id
  `);
  const enableTotp = db.prepare(`
    UPDATE users SET
      totp_enabled = 1,
      totp_secret_enc = @totp_secret_enc,
      totp_pending_enc = NULL,
      totp_backup_hashes = @totp_backup_hashes,
      updated_at = @updated_at
    WHERE id = @id
  `);
  const disableTotpStmt = db.prepare(`
    UPDATE users SET
      totp_enabled = 0,
      totp_secret_enc = NULL,
      totp_pending_enc = NULL,
      totp_backup_hashes = NULL,
      updated_at = @updated_at
    WHERE id = @id
  `);
  const updateBackupHashes = db.prepare(`
    UPDATE users SET totp_backup_hashes = @totp_backup_hashes, updated_at = @updated_at WHERE id = @id
  `);

  const registerSchema = z.object({
    email: emailSchema,
    password: passwordSchema,
    displayName: nameSchema,
  });

  const loginSchema = z.object({
    email: emailSchema,
    password: z.string().min(1).max(128),
  });

  const changePasswordSchema = z.object({
    currentPassword: z.string().min(1).max(128),
    newPassword: passwordSchema,
  });

  const loginTotpSchema = z.object({
    totpToken: z.string().min(10).max(2048),
    code: totpCodeSchema,
  });

  const confirmTotpSchema = z.object({
    code: z.string().trim().regex(/^[0-9]{6}$/, "Enter the 6-digit code from your authenticator app."),
  });

  const disableTotpSchema = z.object({
    password: z.string().min(1).max(128),
    code: totpCodeSchema,
  });

  function encryptSecret(plain) {
    const iv = crypto.randomBytes(12);
    const cipher = crypto.createCipheriv("aes-256-gcm", encKey, iv);
    const encrypted = Buffer.concat([cipher.update(String(plain), "utf8"), cipher.final()]);
    const tag = cipher.getAuthTag();
    return `${iv.toString("base64url")}.${tag.toString("base64url")}.${encrypted.toString("base64url")}`;
  }

  function decryptSecret(payload) {
    if (!payload) return null;
    const [ivB64, tagB64, dataB64] = String(payload).split(".");
    if (!ivB64 || !tagB64 || !dataB64) return null;
    const decipher = crypto.createDecipheriv(
      "aes-256-gcm",
      encKey,
      Buffer.from(ivB64, "base64url")
    );
    decipher.setAuthTag(Buffer.from(tagB64, "base64url"));
    const plain = Buffer.concat([
      decipher.update(Buffer.from(dataB64, "base64url")),
      decipher.final(),
    ]);
    return plain.toString("utf8");
  }

  function publicUser(row) {
    return {
      id: row.id,
      email: row.email,
      displayName: row.display_name || "",
      createdAt: row.created_at,
      totpEnabled: Number(row.totp_enabled) === 1,
    };
  }

  function signToken(user) {
    return jwt.sign(
      { sub: user.id, email: user.email },
      jwtSecret,
      { expiresIn: "30d" }
    );
  }

  function signTotpChallenge(user) {
    return jwt.sign(
      { sub: user.id, email: user.email, purpose: "totp-login" },
      jwtSecret,
      { expiresIn: "5m" }
    );
  }

  function parseBackupHashes(row) {
    if (!row.totp_backup_hashes) return [];
    try {
      const parsed = JSON.parse(row.totp_backup_hashes);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  function generateBackupCodes() {
    const codes = [];
    for (let i = 0; i < BACKUP_CODE_COUNT; i += 1) {
      const raw = crypto.randomBytes(4).toString("hex").toUpperCase();
      codes.push(`${raw.slice(0, 4)}-${raw.slice(4)}`);
    }
    return codes;
  }

  function normalizeCode(code) {
    return String(code || "")
      .trim()
      .replace(/\s+/g, "")
      .toUpperCase();
  }

  function verifyTotpOrBackup(row, code) {
    const secret = decryptSecret(row.totp_secret_enc);
    const cleaned = String(code || "").trim().replace(/\s+/g, "");
    if (secret && /^[0-9]{6}$/.test(cleaned)) {
      if (authenticator.check(cleaned, secret)) {
        return { ok: true, usedBackup: false };
      }
    }
    const normalized = normalizeCode(cleaned);
    const hashes = parseBackupHashes(row);
    for (let i = 0; i < hashes.length; i += 1) {
      if (bcrypt.compareSync(normalized, hashes[i])) {
        const next = hashes.slice();
        next.splice(i, 1);
        updateBackupHashes.run({
          id: row.id,
          totp_backup_hashes: JSON.stringify(next),
          updated_at: new Date().toISOString(),
        });
        return { ok: true, usedBackup: true, remainingBackupCodes: next.length };
      }
    }
    return { ok: false };
  }

  function register(input) {
    const data = registerSchema.parse(input);
    const email = data.email.toLowerCase();
    if (findByEmail.get(email)) {
      const err = new Error("An account with that email already exists.");
      err.status = 409;
      throw err;
    }

    const now = new Date().toISOString();
    const user = {
      id: crypto.randomUUID(),
      email,
      display_name: data.displayName || "",
      password_hash: bcrypt.hashSync(data.password, 10),
      created_at: now,
      updated_at: now,
    };
    insertUser.run(user);
    const pub = publicUser({ ...user, totp_enabled: 0 });
    notifyAuthenticated(pub);
    return { token: signToken(user), user: pub };
  }

  function login(input) {
    const data = loginSchema.parse(input);
    const email = data.email.toLowerCase();
    const row = findByEmail.get(email);
    if (!row || !bcrypt.compareSync(data.password, row.password_hash)) {
      const err = new Error("Invalid email or password.");
      err.status = 401;
      throw err;
    }
    const pub = publicUser(row);
    if (Number(row.totp_enabled) === 1 && row.totp_secret_enc) {
      return {
        requiresTotp: true,
        totpToken: signTotpChallenge(row),
        user: { email: pub.email, displayName: pub.displayName, totpEnabled: true },
      };
    }
    notifyAuthenticated(pub);
    return { token: signToken(row), user: pub };
  }

  function loginWithTotp(input) {
    const data = loginTotpSchema.parse(input);
    let payload;
    try {
      payload = jwt.verify(data.totpToken, jwtSecret);
    } catch {
      const err = new Error("Your 2FA step expired. Sign in again with your password.");
      err.status = 401;
      throw err;
    }
    if (payload.purpose !== "totp-login" || !payload.sub) {
      const err = new Error("Invalid 2FA session. Sign in again.");
      err.status = 401;
      throw err;
    }
    const row = findById.get(payload.sub);
    if (!row || Number(row.totp_enabled) !== 1) {
      const err = new Error("Two-factor authentication is not enabled for this account.");
      err.status = 400;
      throw err;
    }
    const check = verifyTotpOrBackup(row, data.code);
    if (!check.ok) {
      const err = new Error("Invalid authenticator or backup code.");
      err.status = 401;
      throw err;
    }
    const fresh = findById.get(row.id);
    const pub = publicUser(fresh);
    notifyAuthenticated(pub);
    return {
      token: signToken(fresh),
      user: pub,
      usedBackup: !!check.usedBackup,
      remainingBackupCodes: check.remainingBackupCodes,
    };
  }

  /**
   * Verifies the caller's current password before rotating to a new hash.
   * JWTs already issued stay valid until they expire (no server-side revocation
   * list yet) — see routes/auth.js for the user-facing caveat.
   */
  function changePassword(userId, input) {
    const data = changePasswordSchema.parse(input);
    const row = findById.get(userId);
    if (!row) {
      const err = new Error("Sign in required.");
      err.status = 401;
      throw err;
    }
    if (!bcrypt.compareSync(data.currentPassword, row.password_hash)) {
      const err = new Error("Current password is incorrect.");
      err.status = 401;
      throw err;
    }
    if (bcrypt.compareSync(data.newPassword, row.password_hash)) {
      const err = new Error("New password must be different from your current password.");
      err.status = 400;
      throw err;
    }
    updatePasswordHash.run({
      id: userId,
      password_hash: bcrypt.hashSync(data.newPassword, 10),
      updated_at: new Date().toISOString(),
    });
    return publicUser(row);
  }

  async function beginTotpSetup(userId) {
    const row = findById.get(userId);
    if (!row) {
      const err = new Error("Sign in required.");
      err.status = 401;
      throw err;
    }
    if (Number(row.totp_enabled) === 1) {
      const err = new Error("Two-factor authentication is already enabled.");
      err.status = 400;
      throw err;
    }
    const secret = authenticator.generateSecret();
    const otpauthUrl = authenticator.keyuri(row.email, ISSUER, secret);
    updateTotpPending.run({
      id: row.id,
      totp_pending_enc: encryptSecret(secret),
      updated_at: new Date().toISOString(),
    });
    const qrDataUrl = await QRCode.toDataURL(otpauthUrl, {
      errorCorrectionLevel: "M",
      margin: 1,
      width: 220,
    });
    return {
      secret,
      otpauthUrl,
      qrDataUrl,
      issuer: ISSUER,
      account: row.email,
    };
  }

  function confirmTotpSetup(userId, input) {
    const data = confirmTotpSchema.parse(input);
    const row = findById.get(userId);
    if (!row) {
      const err = new Error("Sign in required.");
      err.status = 401;
      throw err;
    }
    if (Number(row.totp_enabled) === 1) {
      const err = new Error("Two-factor authentication is already enabled.");
      err.status = 400;
      throw err;
    }
    const pending = decryptSecret(row.totp_pending_enc);
    if (!pending) {
      const err = new Error("Start 2FA setup first, then enter the code from your app.");
      err.status = 400;
      throw err;
    }
    if (!authenticator.check(data.code, pending)) {
      const err = new Error("That code did not match. Check your authenticator app and try again.");
      err.status = 400;
      throw err;
    }
    const backupCodes = generateBackupCodes();
    const hashes = backupCodes.map((code) => bcrypt.hashSync(normalizeCode(code), 10));
    enableTotp.run({
      id: row.id,
      totp_secret_enc: encryptSecret(pending),
      totp_backup_hashes: JSON.stringify(hashes),
      updated_at: new Date().toISOString(),
    });
    const fresh = findById.get(row.id);
    return {
      user: publicUser(fresh),
      backupCodes,
      message:
        "Two-factor authentication is on. Save these backup codes somewhere safe — they are shown once.",
    };
  }

  function disableTotp(userId, input) {
    const data = disableTotpSchema.parse(input);
    const row = findById.get(userId);
    if (!row) {
      const err = new Error("Sign in required.");
      err.status = 401;
      throw err;
    }
    if (Number(row.totp_enabled) !== 1) {
      const err = new Error("Two-factor authentication is not enabled.");
      err.status = 400;
      throw err;
    }
    if (!bcrypt.compareSync(data.password, row.password_hash)) {
      const err = new Error("Password is incorrect.");
      err.status = 401;
      throw err;
    }
    const check = verifyTotpOrBackup(row, data.code);
    if (!check.ok) {
      const err = new Error("Invalid authenticator or backup code.");
      err.status = 401;
      throw err;
    }
    disableTotpStmt.run({
      id: row.id,
      updated_at: new Date().toISOString(),
    });
    return { user: publicUser(findById.get(row.id)) };
  }

  function requireAuth(req, res, next) {
    const header = req.headers.authorization || "";
    const match = header.match(/^Bearer\s+(.+)$/i);
    if (!match) {
      return res.status(401).json({ error: "Sign in required." });
    }
    try {
      const payload = jwt.verify(match[1], jwtSecret);
      if (payload.purpose === "totp-login") {
        return res.status(401).json({ error: "Complete two-factor authentication to continue." });
      }
      const row = findById.get(payload.sub);
      if (!row) {
        return res.status(401).json({ error: "Sign in required." });
      }
      req.user = publicUser(row);
      return next();
    } catch {
      return res.status(401).json({ error: "Session expired. Please sign in again." });
    }
  }

  return {
    register,
    login,
    loginWithTotp,
    changePassword,
    beginTotpSetup,
    confirmTotpSetup,
    disableTotp,
    requireAuth,
    publicUser,
  };
}

module.exports = { createAuth };
