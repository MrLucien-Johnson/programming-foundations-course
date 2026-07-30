require("dotenv").config();

const express = require("express");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const path = require("path");

const { openDatabase } = require("./db");
const { createAuth } = require("./auth");
const { createAudit } = require("./audit");
const { createOrgStore } = require("./orgs");
const { createCertificateStore } = require("./certificates");
const { createOAuthStore, listConfiguredProviders } = require("./oauth");
const { createAuthRouter } = require("./routes/auth");
const { createOAuthRouter } = require("./routes/oauth");
const { createProgressRouter } = require("./routes/progress");
const { createOrgsRouter } = require("./routes/orgs");
const { createQuizRouter } = require("./routes/quiz");
const { createCertificatesRouter } = require("./routes/certificates");
const { createAccountRouter } = require("./routes/account");

const PORT = Number(process.env.PORT || 8787);
const HOST = process.env.HOST || "0.0.0.0";
const JWT_SECRET = process.env.JWT_SECRET || "dev-only-change-me-before-production";
const DATABASE_PATH =
  process.env.DATABASE_PATH || path.join(__dirname, "..", "data", "pf.sqlite");
const PUBLIC_API_BASE = (
  process.env.PUBLIC_API_BASE ||
  process.env.RENDER_EXTERNAL_URL ||
  `http://127.0.0.1:${PORT}`
).replace(/\/$/, "");
const FRONTEND_DEFAULT_RETURN = (
  process.env.FRONTEND_DEFAULT_RETURN ||
  "http://127.0.0.1:5500/docs/account.html"
).trim();

if (process.env.NODE_ENV === "production") {
  if (!process.env.JWT_SECRET || JWT_SECRET.startsWith("dev-only") || JWT_SECRET.length < 32) {
    console.error(
      "Refusing to start: set JWT_SECRET in production to a random string of at least 32 characters."
    );
    process.exit(1);
  }
}

// On Free hosts without a mounted disk, prefer a writable relative path.
// Example: DATABASE_PATH=./data/pf.sqlite
// Warning: Free instances can wipe this file on restart/redeploy.

/** Strip quotes/whitespace and trailing slashes so env typos still match browsers. */
function normalizeOrigin(value) {
  if (value == null) return "";
  let origin = String(value).trim();
  if (
    (origin.startsWith('"') && origin.endsWith('"')) ||
    (origin.startsWith("'") && origin.endsWith("'"))
  ) {
    origin = origin.slice(1, -1).trim();
  }
  // Browsers never send a trailing slash on Origin; tolerate it in env values.
  if (origin !== "null" && origin !== "*") {
    origin = origin.replace(/\/+$/, "");
  }
  return origin;
}

const corsOrigins = (process.env.CORS_ORIGINS || "")
  .split(",")
  .map(normalizeOrigin)
  .filter(Boolean);

const db = openDatabase(DATABASE_PATH);
const audit = createAudit(db);
const orgStore = createOrgStore({ db, audit });
const certStore = createCertificateStore({ db, audit });
const oauthStore = createOAuthStore(db);
const auth = createAuth({
  db,
  jwtSecret: JWT_SECRET,
  oauthStore,
  // Claim any pending org invites addressed to this email on register/login.
  onAuthenticated: (user) => orgStore.attachInvites(user.id, user.email),
});

const app = express();
app.set("trust proxy", 1);
app.use(
  cors({
    origin(origin, callback) {
      // Allow non-browser clients and configured origins.
      // "null" is included for local file:// testing when listed in CORS_ORIGINS.
      const normalized = normalizeOrigin(origin);
      if (!normalized || corsOrigins.includes(normalized) || corsOrigins.includes("*")) {
        return callback(null, true);
      }
      return callback(new Error(`Origin not allowed: ${origin}`));
    },
    credentials: false,
  })
);
app.use(express.json({ limit: "256kb" }));

app.get("/api/health", (_req, res) => {
  res.json({
    ok: true,
    service: "programming-foundations-api",
    corsConfigured: corsOrigins.length > 0,
    corsOriginCount: corsOrigins.length,
    oauthProviders: listConfiguredProviders().map((p) => p.id),
  });
});

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 40,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "Too many auth attempts. Try again in a few minutes." },
});

app.use(
  "/api/auth/oauth",
  authLimiter,
  createOAuthRouter({
    auth,
    oauthStore,
    publicApiBase: PUBLIC_API_BASE,
    allowedReturnOrigins: corsOrigins,
    frontendDefaultReturn: FRONTEND_DEFAULT_RETURN,
  })
);
app.use("/api/auth", authLimiter, createAuthRouter(auth));
app.use("/api/progress", createProgressRouter({ db, requireAuth: auth.requireAuth }));
app.use("/api/quiz-attempts", createQuizRouter({ db, requireAuth: auth.requireAuth }));
app.use("/api/orgs", createOrgsRouter({ orgStore, requireAuth: auth.requireAuth }));
app.use("/api/certificates", createCertificatesRouter({ certStore, requireAuth: auth.requireAuth }));
app.use("/api/account", createAccountRouter({ db, requireAuth: auth.requireAuth, audit }));

app.use((err, _req, res, _next) => {
  if (err && /Origin not allowed/.test(err.message || "")) {
    return res.status(403).json({ error: "This site origin is not allowed by the API." });
  }
  console.error(err);
  return res.status(500).json({ error: "Unexpected server error." });
});

if (require.main === module) {
  app.listen(PORT, HOST, () => {
    const providers = listConfiguredProviders().map((p) => p.id);
    console.log(`Programming Foundations API listening on http://${HOST}:${PORT}`);
    console.log(
      providers.length
        ? `OAuth providers enabled: ${providers.join(", ")}`
        : "OAuth providers: none configured (email/password still works)"
    );
  });
}

module.exports = {
  app,
  db,
  auth,
  orgStore,
  certStore,
  audit,
  oauthStore,
  normalizeOrigin,
};
