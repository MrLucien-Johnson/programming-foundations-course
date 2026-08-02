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

  router.post("/login/totp", (req, res) => {
    try {
      const result = auth.loginWithTotp(req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(
        res,
        error,
        "Enter a valid 6-digit authenticator code or a backup code."
      );
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

  router.post("/totp/setup", auth.requireAuth, async (req, res) => {
    try {
      const result = await auth.beginTotpSetup(req.user.id);
      return res.json(result);
    } catch (error) {
      return sendAuthError(res, error);
    }
  });

  router.post("/totp/confirm", auth.requireAuth, (req, res) => {
    try {
      const result = auth.confirmTotpSetup(req.user.id, req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(res, error, "Enter the 6-digit code from your authenticator app.");
    }
  });

  router.post("/totp/disable", auth.requireAuth, (req, res) => {
    try {
      const result = auth.disableTotp(req.user.id, req.body || {});
      return res.json(result);
    } catch (error) {
      return sendAuthError(
        res,
        error,
        "Enter your password and a valid authenticator or backup code."
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
