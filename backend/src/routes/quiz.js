const express = require("express");
const crypto = require("crypto");
const { z } = require("zod");

const attemptSchema = z.object({
  quizPath: z.string().trim().min(1).max(400),
  courseName: z.string().trim().max(200).optional().default(""),
  score: z.number().int().min(0).max(1000),
  total: z.number().int().min(0).max(1000),
  passed: z.boolean().optional(),
});

/** Durable, server-side quiz attempt log — the source of truth for gradebooks. */
function createQuizRouter({ db, requireAuth }) {
  const router = express.Router();
  const insert = db.prepare(`
    INSERT INTO quiz_attempts (id, user_id, quiz_path, course_name, score, total, passed, created_at)
    VALUES (@id, @user_id, @quiz_path, @course_name, @score, @total, @passed, @created_at)
  `);
  const listForUser = db.prepare(
    `SELECT quiz_path, course_name, score, total, passed, created_at
     FROM quiz_attempts WHERE user_id = ? ORDER BY created_at DESC LIMIT 500`
  );

  router.use(requireAuth);

  router.get("/", (req, res) => {
    const attempts = listForUser.all(req.user.id).map((a) => ({
      quizPath: a.quiz_path,
      courseName: a.course_name,
      score: a.score,
      total: a.total,
      passed: !!a.passed,
      at: a.created_at,
    }));
    return res.json({ attempts });
  });

  router.post("/", (req, res) => {
    try {
      const data = attemptSchema.parse(req.body || {});
      const passed =
        typeof data.passed === "boolean"
          ? data.passed
          : data.total > 0 && data.score / data.total >= 0.7;
      insert.run({
        id: crypto.randomUUID(),
        user_id: req.user.id,
        quiz_path: data.quizPath,
        course_name: data.courseName || "",
        score: data.score,
        total: data.total,
        passed: passed ? 1 : 0,
        created_at: new Date().toISOString(),
      });
      return res.status(201).json({ ok: true });
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({ error: "Invalid quiz attempt payload." });
      }
      console.error(error);
      return res.status(500).json({ error: "Could not record quiz attempt." });
    }
  });

  return router;
}

module.exports = { createQuizRouter };
