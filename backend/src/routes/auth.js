const express = require("express");
const { ZodError } = require("zod");

function createAuthRouter(auth) {
  const router = express.Router();

  router.post("/register", async (req, res) => {
    try {
      const result = await auth.register(req.body || {});
      return res.status(201).json(result);
    } catch (error) {
      return sendAuthError(res, error);
    }
  });

  router.post("/login", async (req, res) => {
    try {
      const result = await auth.login(req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(res, error);
    }
  });

  router.get("/me", auth.requireAuth, (req, res) => {
    return res.json({ user: req.user });
  });

  // Rotates the password hash (Argon2id) and bumps token_version so other
  // devices' JWTs stop working. Response includes a fresh token for this session.
  router.post("/change-password", auth.requireAuth, async (req, res) => {
    try {
      const result = await auth.changePassword(req.user.id, req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(
        res,
        error,
        "Check your current and new password (new password must be at least 8 characters)."
      );
    }
  });

  return router;
}

function sendAuthError(res, error, zodMessage) {
  if (error instanceof ZodError) {
    return res.status(400).json({
      error: zodMessage || "Check your email and password (password must be at least 8 characters).",
      details: error.issues.map((issue) => issue.message),
    });
  }
  const status = error.status || 500;
  return res.status(status).json({ error: error.message || "Request failed." });
}

module.exports = { createAuthRouter };
