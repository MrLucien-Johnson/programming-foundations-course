const express = require("express");

/**
 * Authenticated donor-course content.
 * Lessons/quizzes are read from a private checkout (or local root) — never from
 * public raw.githubusercontent.com in the browser for premium paths.
 */
function createContentRouter({ requireAuth, premiumStore, contentStore }) {
  const router = express.Router();
  router.use(requireAuth);

  router.get("/status", (req, res) => {
    const entitlements = premiumStore
      ? premiumStore.getEntitlements(req.user.id)
      : { premiumAccess: false };
    return res.json({
      entitlements,
      content: contentStore ? contentStore.status() : { ready: false },
    });
  });

  router.get("/", (req, res) => {
    try {
      if (!premiumStore || !contentStore) {
        return res.status(503).json({ error: "Premium content API is not configured." });
      }
      const entitlements = premiumStore.getEntitlements(req.user.id);
      if (!entitlements.premiumAccess) {
        return res.status(403).json({
          error:
            "Donor / allowlisted account required. Ask the owner to grant your email after a donation.",
        });
      }
      const relPath = req.query.path;
      const file = contentStore.readText(relPath);
      res.setHeader("Cache-Control", "private, no-store");
      return res.json(file);
    } catch (error) {
      return res.status(error.status || 500).json({ error: error.message || "Could not load content." });
    }
  });

  return router;
}

module.exports = { createContentRouter };
