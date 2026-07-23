const express = require("express");
const { toCsv } = require("../orgs");

function sendError(res, error) {
  const status = error && error.status ? error.status : 500;
  if (status >= 500) console.error(error);
  return res.status(status).json({ error: (error && error.message) || "Request failed." });
}

function createOrgsRouter({ orgStore, requireAuth }) {
  const router = express.Router();
  router.use(requireAuth);

  router.get("/", (req, res) => {
    try {
      return res.json({ orgs: orgStore.listOrgsForUser(req.user.id) });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.post("/", (req, res) => {
    try {
      const org = orgStore.createOrg({ userId: req.user.id, name: (req.body || {}).name });
      return res.status(201).json({ org });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id", (req, res) => {
    try {
      const { org, membership } = orgStore.requireMembership(req.params.id, req.user.id);
      return res.json({
        org: {
          id: org.id,
          name: org.name,
          plan: org.plan,
          createdAt: org.created_at,
          role: membership.role,
        },
      });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.patch("/:id", (req, res) => {
    try {
      const result = orgStore.setPlan({
        orgId: req.params.id,
        actorId: req.user.id,
        plan: (req.body || {}).plan,
      });
      return res.json(result);
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/members", (req, res) => {
    try {
      return res.json({ members: orgStore.listMembers(req.params.id, req.user.id) });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.post("/:id/members", (req, res) => {
    try {
      const body = req.body || {};
      const member = orgStore.addMember({
        orgId: req.params.id,
        actorId: req.user.id,
        email: body.email,
        role: body.role || "learner",
      });
      return res.status(201).json({ member });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.patch("/:id/members/:userId", (req, res) => {
    try {
      const result = orgStore.updateMemberRole({
        orgId: req.params.id,
        actorId: req.user.id,
        targetUserId: req.params.userId,
        role: (req.body || {}).role,
      });
      return res.json(result);
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.delete("/:id/members/:userId", (req, res) => {
    try {
      const result = orgStore.removeMember({
        orgId: req.params.id,
        actorId: req.user.id,
        targetUserId: req.params.userId,
      });
      return res.json(result);
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/assignments", (req, res) => {
    try {
      return res.json({ assignments: orgStore.listAssignments(req.params.id, req.user.id) });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.post("/:id/assignments", (req, res) => {
    try {
      const body = req.body || {};
      const assignment = orgStore.assignPath({
        orgId: req.params.id,
        actorId: req.user.id,
        courseName: body.courseName,
        userId: body.userId || null,
      });
      return res.status(201).json({ assignment });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/analytics", (req, res) => {
    try {
      return res.json({ analytics: orgStore.analytics(req.params.id, req.user.id) });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/audit", (req, res) => {
    try {
      const events = orgStore.getAuditEvents(req.params.id, req.user.id, req.query.limit);
      return res.json({ events });
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/roster.csv", (req, res) => {
    try {
      const rows = orgStore.rosterRows(req.params.id, req.user.id);
      const csv = toCsv(rows, [
        { key: "email", label: "Email" },
        { key: "displayName", label: "Name" },
        { key: "role", label: "Role" },
        { key: "status", label: "Status" },
        { key: "completions", label: "Modules completed" },
        { key: "lastActive", label: "Last active" },
        { key: "joinedAt", label: "Joined" },
      ]);
      res.setHeader("Content-Type", "text/csv; charset=utf-8");
      res.setHeader("Content-Disposition", `attachment; filename="roster-${req.params.id}.csv"`);
      return res.send(csv);
    } catch (error) {
      return sendError(res, error);
    }
  });

  router.get("/:id/gradebook.csv", (req, res) => {
    try {
      const rows = orgStore.gradebookRows(req.params.id, req.user.id);
      const csv = toCsv(rows, [
        { key: "email", label: "Email" },
        { key: "displayName", label: "Name" },
        { key: "courseName", label: "Course" },
        { key: "quizPath", label: "Quiz" },
        { key: "score", label: "Score" },
        { key: "total", label: "Total" },
        { key: "passed", label: "Passed" },
        { key: "attemptedAt", label: "Attempted at" },
      ]);
      res.setHeader("Content-Type", "text/csv; charset=utf-8");
      res.setHeader("Content-Disposition", `attachment; filename="gradebook-${req.params.id}.csv"`);
      return res.send(csv);
    } catch (error) {
      return sendError(res, error);
    }
  });

  return router;
}

module.exports = { createOrgsRouter };
