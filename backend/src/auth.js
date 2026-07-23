const crypto = require("crypto");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { z } = require("zod");

const emailSchema = z.string().trim().email().max(254);
const passwordSchema = z.string().min(8).max(128);
const nameSchema = z.string().trim().max(80).optional().default("");

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
  const insertUser = db.prepare(`
    INSERT INTO users (id, email, display_name, password_hash, created_at, updated_at)
    VALUES (@id, @email, @display_name, @password_hash, @created_at, @updated_at)
  `);

  const findByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const updatePasswordHash = db.prepare(`
    UPDATE users SET password_hash = @password_hash, updated_at = @updated_at WHERE id = @id
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

  function publicUser(row) {
    return {
      id: row.id,
      email: row.email,
      displayName: row.display_name || "",
      createdAt: row.created_at,
    };
  }

  function signToken(user) {
    return jwt.sign(
      { sub: user.id, email: user.email },
      jwtSecret,
      { expiresIn: "30d" }
    );
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
    notifyAuthenticated(publicUser(user));
    const token = signToken(user);
    return { token, user: publicUser(user) };
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
    notifyAuthenticated(publicUser(row));
    return { token: signToken(row), user: publicUser(row) };
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
      req.user = publicUser(row);
      return next();
    } catch {
      return res.status(401).json({ error: "Session expired. Please sign in again." });
    }
  }

  return { register, login, changePassword, requireAuth, publicUser };
}

module.exports = { createAuth };
