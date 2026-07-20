require("dotenv").config();

const express = require("express");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const path = require("path");

const { openDatabase } = require("./db");
const { createAuth } = require("./auth");
const { createAuthRouter } = require("./routes/auth");
const { createProgressRouter } = require("./routes/progress");

const PORT = Number(process.env.PORT || 8787);
const HOST = process.env.HOST || "0.0.0.0";
const JWT_SECRET = process.env.JWT_SECRET || "dev-only-change-me-before-production";
const DATABASE_PATH =
  process.env.DATABASE_PATH || path.join(__dirname, "..", "data", "pf.sqlite");

if (process.env.NODE_ENV === "production" && JWT_SECRET.startsWith("dev-only")) {
  console.error("Refusing to start: set JWT_SECRET in production.");
  process.exit(1);
}

const corsOrigins = (process.env.CORS_ORIGINS || "")
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean);

const db = openDatabase(DATABASE_PATH);
const auth = createAuth({ db, jwtSecret: JWT_SECRET });

const app = express();
app.set("trust proxy", 1);
app.use(
  cors({
    origin(origin, callback) {
      // Allow non-browser clients and configured origins.
      // "null" is included for local file:// testing when listed in CORS_ORIGINS.
      if (!origin || corsOrigins.includes(origin) || corsOrigins.includes("*")) {
        return callback(null, true);
      }
      return callback(new Error(`Origin not allowed: ${origin}`));
    },
    credentials: false,
  })
);
app.use(express.json({ limit: "256kb" }));

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, service: "programming-foundations-api" });
});

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 40,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "Too many auth attempts. Try again in a few minutes." },
});

app.use("/api/auth", authLimiter, createAuthRouter(auth));
app.use("/api/progress", createProgressRouter({ db, requireAuth: auth.requireAuth }));

app.use((err, _req, res, _next) => {
  if (err && /Origin not allowed/.test(err.message || "")) {
    return res.status(403).json({ error: "This site origin is not allowed by the API." });
  }
  console.error(err);
  return res.status(500).json({ error: "Unexpected server error." });
});

if (require.main === module) {
  app.listen(PORT, HOST, () => {
    console.log(`Programming Foundations API listening on http://${HOST}:${PORT}`);
  });
}

module.exports = { app, db, auth };
