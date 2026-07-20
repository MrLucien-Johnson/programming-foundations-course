const express = require("express");
const { z } = require("zod");

const emptyProgress = () => ({
  completions: [],
  quizCompletions: {},
  startSteps: {},
  moduleProgress: {},
  updatedAt: null,
});

const progressSchema = z.object({
  completions: z.array(z.string()).default([]),
  quizCompletions: z.record(z.any()).default({}),
  startSteps: z.record(z.boolean()).default({}),
  moduleProgress: z.record(z.any()).default({}),
  updatedAt: z.string().nullable().optional(),
});

function createProgressRouter({ db, requireAuth }) {
  const router = express.Router();
  const getProgress = db.prepare(`SELECT payload, updated_at FROM progress WHERE user_id = ?`);
  const upsertProgress = db.prepare(`
    INSERT INTO progress (user_id, payload, updated_at)
    VALUES (@user_id, @payload, @updated_at)
    ON CONFLICT(user_id) DO UPDATE SET
      payload = excluded.payload,
      updated_at = excluded.updated_at
  `);

  router.use(requireAuth);

  router.get("/", (req, res) => {
    const row = getProgress.get(req.user.id);
    if (!row) {
      return res.json({ progress: emptyProgress() });
    }
    try {
      const progress = JSON.parse(row.payload);
      progress.updatedAt = row.updated_at;
      return res.json({ progress });
    } catch {
      return res.json({ progress: emptyProgress() });
    }
  });

  router.put("/", (req, res) => {
    try {
      const parsed = progressSchema.parse(req.body || {});
      const now = new Date().toISOString();
      const progress = {
        completions: [...new Set(parsed.completions.filter(Boolean))],
        quizCompletions: parsed.quizCompletions || {},
        startSteps: parsed.startSteps || {},
        moduleProgress: parsed.moduleProgress || {},
        updatedAt: now,
      };
      upsertProgress.run({
        user_id: req.user.id,
        payload: JSON.stringify(progress),
        updated_at: now,
      });
      return res.json({ progress });
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({ error: "Invalid progress payload." });
      }
      return res.status(500).json({ error: "Could not save progress." });
    }
  });

  return router;
}

function mergeProgress(localProgress, remoteProgress) {
  const local = normalize(localProgress);
  const remote = normalize(remoteProgress);

  const completions = [...new Set([...(local.completions || []), ...(remote.completions || [])])];

  const quizCompletions = { ...(remote.quizCompletions || {}) };
  for (const [key, value] of Object.entries(local.quizCompletions || {})) {
    const remoteValue = quizCompletions[key];
    if (!remoteValue) {
      quizCompletions[key] = value;
      continue;
    }
    const localAt = Date.parse(value.at || 0) || 0;
    const remoteAt = Date.parse(remoteValue.at || 0) || 0;
    quizCompletions[key] = localAt >= remoteAt ? value : remoteValue;
  }

  const startSteps = {
    ...(remote.startSteps || {}),
    ...(local.startSteps || {}),
  };
  // Once a step is true on either side, keep it true
  for (const key of new Set([
    ...Object.keys(remote.startSteps || {}),
    ...Object.keys(local.startSteps || {}),
  ])) {
    startSteps[key] = !!(local.startSteps?.[key] || remote.startSteps?.[key]);
  }

  const moduleProgress = {
    ...(remote.moduleProgress || {}),
    ...(local.moduleProgress || {}),
  };

  return {
    completions,
    quizCompletions,
    startSteps,
    moduleProgress,
    updatedAt: new Date().toISOString(),
  };
}

function normalize(progress) {
  if (!progress || typeof progress !== "object") return emptyProgress();
  return {
    completions: Array.isArray(progress.completions) ? progress.completions : [],
    quizCompletions:
      progress.quizCompletions && typeof progress.quizCompletions === "object"
        ? progress.quizCompletions
        : {},
    startSteps:
      progress.startSteps && typeof progress.startSteps === "object" ? progress.startSteps : {},
    moduleProgress:
      progress.moduleProgress && typeof progress.moduleProgress === "object"
        ? progress.moduleProgress
        : {},
    updatedAt: progress.updatedAt || null,
  };
}

module.exports = { createProgressRouter, mergeProgress, emptyProgress };
