const crypto = require("crypto");
const jwt = require("jsonwebtoken");
const { z } = require("zod");
const { hashPassword, verifyPassword, burnVerifyCost } = require("./passwords");

const emailSchema = z.string().trim().email().max(254);
// OWASP: minimum 8 characters; allow long passphrases up to 128.
const passwordSchema = z
  .string()
  .min(8, "Password must be at least 8 characters.")
  .max(128, "Password must be at most 128 characters.");
const nameSchema = z.string().trim().max(80).optional().default("");

function createAuth({ db, jwtSecret, onAuthenticated, oauthStore }) {
  const notifyAuthenticated = (user) => {
    if (typeof onAuthenticated === "function") {
      try {
        onAuthenticated(user);
      } catch {
        // Post-auth hooks (e.g. claiming invites) must not block sign-in.
      }
    }
  };

  const insertUser = db.prepare(`
    INSERT INTO users (id, email, display_name, password_hash, token_version, created_at, updated_at)
    VALUES (@id, @email, @display_name, @password_hash, @token_version, @created_at, @updated_at)
  `);

  const findByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const updatePasswordHash = db.prepare(`
    UPDATE users
    SET password_hash = @password_hash,
        token_version = @token_version,
        updated_at = @updated_at
    WHERE id = @id
  `);
  const updatePasswordHashOnly = db.prepare(`
    UPDATE users
    SET password_hash = @password_hash, updated_at = @updated_at
    WHERE id = @id
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
    currentPassword: z.string().max(128).optional().default(""),
    newPassword: passwordSchema,
  });

  function hasPasswordHash(row) {
    return !!(row && row.password_hash && String(row.password_hash).length > 0);
  }

  function publicUser(row) {
    const providers =
      oauthStore && typeof oauthStore.providersForUser === "function"
        ? oauthStore.providersForUser(row.id)
        : [];
    return {
      id: row.id,
      email: row.email,
      displayName: row.display_name || "",
      createdAt: row.created_at,
      hasPassword: hasPasswordHash(row),
      providers,
    };
  }

  function signToken(user) {
    const tokenVersion = Number(user.token_version) || 0;
    return jwt.sign(
      { sub: user.id, email: user.email, tv: tokenVersion },
      jwtSecret,
      { expiresIn: "30d" }
    );
  }

  function sessionForUser(row) {
    notifyAuthenticated(publicUser(row));
    return { token: signToken(row), user: publicUser(row) };
  }

  async function register(input) {
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
      password_hash: await hashPassword(data.password),
      token_version: 0,
      created_at: now,
      updated_at: now,
    };
    insertUser.run(user);
    return sessionForUser(user);
  }

  async function login(input) {
    const data = loginSchema.parse(input);
    const email = data.email.toLowerCase();
    const row = findByEmail.get(email);
    if (!row) {
      await burnVerifyCost(data.password);
      const err = new Error("Invalid email or password.");
      err.status = 401;
      throw err;
    }

    if (!hasPasswordHash(row)) {
      await burnVerifyCost(data.password);
      const providers =
        oauthStore && typeof oauthStore.providersForUser === "function"
          ? oauthStore.providersForUser(row.id)
          : [];
      const hint = providers.length
        ? ` Continue with ${providers.map((p) => p[0].toUpperCase() + p.slice(1)).join(", ")}.`
        : " Use social sign-in for this account.";
      const err = new Error(`This account has no password.${hint}`);
      err.status = 401;
      throw err;
    }

    const { ok, needsRehash } = await verifyPassword(data.password, row.password_hash);
    if (!ok) {
      const err = new Error("Invalid email or password.");
      err.status = 401;
      throw err;
    }

    if (needsRehash) {
      try {
        updatePasswordHashOnly.run({
          id: row.id,
          password_hash: await hashPassword(data.password),
          updated_at: new Date().toISOString(),
        });
      } catch {
        // Rehash is best-effort; login still succeeds with the verified password.
      }
    }

    return sessionForUser(row);
  }

  /**
   * Verifies the caller's current password, rotates to a new Argon2id hash,
   * and bumps token_version so previously issued JWTs stop working.
   * Returns a fresh token for the current device.
   */
  async function changePassword(userId, input) {
    const data = changePasswordSchema.parse(input);
    const row = findById.get(userId);
    if (!row) {
      const err = new Error("Sign in required.");
      err.status = 401;
      throw err;
    }

    if (!hasPasswordHash(row)) {
      // OAuth-only account with an authenticated session may set a password.
      const nextVersion = (Number(row.token_version) || 0) + 1;
      const updated = {
        id: userId,
        password_hash: await hashPassword(data.newPassword),
        token_version: nextVersion,
        updated_at: new Date().toISOString(),
      };
      updatePasswordHash.run(updated);
      const userForToken = {
        ...row,
        token_version: nextVersion,
        password_hash: updated.password_hash,
      };
      return {
        user: publicUser(userForToken),
        token: signToken(userForToken),
      };
    }

    if (!data.currentPassword) {
      const err = new Error("Current password is required.");
      err.status = 400;
      throw err;
    }

    const current = await verifyPassword(data.currentPassword, row.password_hash);
    if (!current.ok) {
      const err = new Error("Current password is incorrect.");
      err.status = 401;
      throw err;
    }

    const sameAsNew = await verifyPassword(data.newPassword, row.password_hash);
    if (sameAsNew.ok) {
      const err = new Error("New password must be different from your current password.");
      err.status = 400;
      throw err;
    }

    const nextVersion = (Number(row.token_version) || 0) + 1;
    const updated = {
      id: userId,
      password_hash: await hashPassword(data.newPassword),
      token_version: nextVersion,
      updated_at: new Date().toISOString(),
    };
    updatePasswordHash.run(updated);

    const userForToken = { ...row, token_version: nextVersion, password_hash: updated.password_hash };
    return {
      user: publicUser(userForToken),
      token: signToken(userForToken),
    };
  }

  function requireAuth(req, res, next) {
    const header = req.headers.authorization || "";
    const match = header.match(/^Bearer\s+(.+)$/i);
    if (!match) {
      return res.status(401).json({ error: "Sign in required." });
    }
    try {
      const payload = jwt.verify(match[1], jwtSecret);
      const row = findById.get(payload.sub);
      if (!row) {
        return res.status(401).json({ error: "Sign in required." });
      }
      const expectedTv = Number(row.token_version) || 0;
      const tokenTv = payload.tv == null ? 0 : Number(payload.tv);
      if (!Number.isFinite(tokenTv) || tokenTv !== expectedTv) {
        return res.status(401).json({ error: "Session expired. Please sign in again." });
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
    changePassword,
    requireAuth,
    publicUser,
    sessionForUser,
    onAuthenticatedHook: notifyAuthenticated,
  };
}

module.exports = { createAuth };
