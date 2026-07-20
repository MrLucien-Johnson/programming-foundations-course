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

  return router;
}

function sendAuthError(res, error) {
  if (error instanceof ZodError) {
    return res.status(400).json({
      error: "Check your email and password (password must be at least 8 characters).",
      details: error.issues.map((issue) => issue.message),
    });
  }
  const status = error.status || 500;
  return res.status(status).json({ error: error.message || "Request failed." });
}

module.exports = { createAuthRouter };
