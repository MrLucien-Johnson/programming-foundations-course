const express = require("express");

function createCertificatesRouter({ certStore, requireAuth }) {
  const router = express.Router();

  // Public verification — no auth so anyone (an employer, school) can check a code.
  router.get("/verify/:verifyId", (req, res) => {
    return res.json(certStore.verify(req.params.verifyId));
  });

  router.get("/", requireAuth, (req, res) => {
    return res.json({ certificates: certStore.listForUser(req.user.id) });
  });

  router.post("/", requireAuth, (req, res) => {
    try {
      const body = req.body || {};
      const certificate = certStore.issue({
        userId: req.user.id,
        learnerName: body.learnerName,
        courseName: body.courseName,
      });
      return res.status(201).json({ certificate });
    } catch (error) {
      const status = error && error.status ? error.status : 500;
      if (status >= 500) console.error(error);
      return res.status(status).json({ error: (error && error.message) || "Could not issue certificate." });
    }
  });

  return router;
}

module.exports = { createCertificatesRouter };
