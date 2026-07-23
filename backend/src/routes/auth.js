const express = require("express");
const { ZodError } = require("zod");

function createAuthRouter(auth) {
  const router = express.Router();

  router.post("/register", (req, res) => {
    try {
      const result = auth.register(req.body || {});
      return res.status(201).json(result);
    } catch (error) {
      return sendAuthError(res, error);
    }
  });

  router.post("/login", (req, res) => {
    try {
      const result = auth.login(req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(res, error);
    }
  });

  router.get("/me", auth.requireAuth, (req, res) => {
    return res.json({ user: req.user });
  });

  // Rotates the password hash only; existing JWTs stay valid until they expire
  // (no server-side session/token revocation yet), so this does not sign the
  // user out of other devices.
  router.post("/change-password", auth.requireAuth, (req, res) => {
    try {
      const result = auth.changePassword(req.user.id, req.body || {});
      return res.json({ user: result });
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
