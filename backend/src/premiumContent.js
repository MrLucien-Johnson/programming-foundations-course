const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const PREMIUM_PATH_PREFIXES = [
  "languages/devops/",
  "languages/aws/",
  "languages/azure/",
  "languages/gcp/",
  "languages/kubernetes/",
  "languages/terraform/",
];

function normalizeContentPath(raw) {
  const clean = String(raw || "")
    .replace(/\\/g, "/")
    .replace(/^\/+/, "")
    .trim();
  if (!clean || clean.includes("\0")) return null;
  const parts = clean.split("/");
  if (parts.some((p) => p === ".." || p === "")) return null;
  if (!PREMIUM_PATH_PREFIXES.some((prefix) => clean.startsWith(prefix))) return null;
  if (!/\.(md|txt|markdown)$/i.test(clean)) return null;
  return clean;
}

function repoRootFromHere() {
  return path.resolve(__dirname, "..", "..");
}

function defaultLocalRoot() {
  if (process.env.PREMIUM_CONTENT_ROOT) {
    return path.resolve(process.env.PREMIUM_CONTENT_ROOT);
  }
  return repoRootFromHere();
}

function gitCheckoutDir() {
  return path.resolve(
    process.env.PREMIUM_CONTENT_DIR ||
      path.join(process.env.DATABASE_PATH ? path.dirname(process.env.DATABASE_PATH) : path.join(__dirname, "..", "data"), "premium-content")
  );
}

function createPremiumContentStore({ audit } = {}) {
  let mode = "local";
  let root = defaultLocalRoot();
  let lastError = null;
  let ready = false;

  function resolveOnDisk(relPath) {
    const safe = normalizeContentPath(relPath);
    if (!safe) {
      const err = new Error("That content path is not allowed.");
      err.status = 400;
      throw err;
    }
    const full = path.resolve(root, safe);
    const rootResolved = path.resolve(root);
    if (!full.startsWith(rootResolved + path.sep) && full !== rootResolved) {
      const err = new Error("Invalid content path.");
      err.status = 400;
      throw err;
    }
    return { safe, full };
  }

  function readText(relPath) {
    if (!ready) {
      const err = new Error(
        "Premium content is not ready on this server yet. The owner needs to connect the private content repo (or local content root)."
      );
      err.status = 503;
      throw err;
    }
    const { safe, full } = resolveOnDisk(relPath);
    if (!fs.existsSync(full) || !fs.statSync(full).isFile()) {
      const err = new Error("Content not found.");
      err.status = 404;
      throw err;
    }
    return {
      path: safe,
      content: fs.readFileSync(full, "utf8"),
      contentType: "text/markdown; charset=utf-8",
    };
  }

  function status() {
    return {
      ready,
      mode,
      root,
      lastError,
      prefixes: PREMIUM_PATH_PREFIXES,
    };
  }

  function markLocalReady() {
    mode = "local";
    root = defaultLocalRoot();
    const probe = path.join(root, "languages", "devops");
    ready = fs.existsSync(probe);
    lastError = ready
      ? null
      : `Local premium content not found under ${probe}. Set PREMIUM_CONTENT_GIT_URL or PREMIUM_CONTENT_ROOT.`;
    return status();
  }

  function runGit(args, cwd) {
    const result = spawnSync("git", args, {
      cwd,
      encoding: "utf8",
      env: process.env,
    });
    if (result.status !== 0) {
      const msg = (result.stderr || result.stdout || "git failed").trim();
      const err = new Error(msg);
      err.status = 500;
      throw err;
    }
    return result.stdout || "";
  }

  function authenticatedRemote(url, token) {
    // https://x-access-token:TOKEN@github.com/org/repo.git
    try {
      const parsed = new URL(url);
      if (parsed.protocol !== "https:") {
        throw new Error("PREMIUM_CONTENT_GIT_URL must be an https Git URL.");
      }
      parsed.username = "x-access-token";
      parsed.password = token;
      return parsed.toString();
    } catch (error) {
      const err = new Error(error.message || "Invalid PREMIUM_CONTENT_GIT_URL.");
      err.status = 500;
      throw err;
    }
  }

  function syncFromGit() {
    const url = String(process.env.PREMIUM_CONTENT_GIT_URL || "").trim();
    const token = String(process.env.PREMIUM_CONTENT_GIT_TOKEN || "").trim();
    if (!url || !token) {
      return markLocalReady();
    }

    mode = "git";
    const dir = gitCheckoutDir();
    fs.mkdirSync(path.dirname(dir), { recursive: true });
    const remote = authenticatedRemote(url, token);

    try {
      if (fs.existsSync(path.join(dir, ".git"))) {
        runGit(["remote", "set-url", "origin", remote], dir);
        runGit(["fetch", "--depth", "1", "origin"], dir);
        // Prefer main, fall back to master / default HEAD
        try {
          runGit(["checkout", "-B", "main", "origin/main"], dir);
        } catch {
          try {
            runGit(["checkout", "-B", "master", "origin/master"], dir);
          } catch {
            runGit(["checkout", "FETCH_HEAD"], dir);
          }
        }
        runGit(["reset", "--hard", "FETCH_HEAD"], dir);
      } else {
        if (fs.existsSync(dir)) {
          fs.rmSync(dir, { recursive: true, force: true });
        }
        runGit(["clone", "--depth", "1", remote, dir], path.dirname(dir));
      }

      root = dir;
      const probe = path.join(root, "languages", "devops");
      ready = fs.existsSync(probe);
      lastError = ready
        ? null
        : "Private premium repo cloned, but languages/devops was not found. Push the donor course tree into that repo.";
      if (audit && ready) {
        audit.log({
          actorId: null,
          action: "premium_content.synced",
          meta: { mode: "git", root },
        });
      }
    } catch (error) {
      ready = false;
      lastError = error.message || "Could not sync private premium content.";
      // Fall back to local public tree so owner can still develop / soft-migrate.
      const local = markLocalReady();
      if (local.ready) {
        lastError = `Git sync failed (${error.message}); serving local fallback content.`;
      }
    }
    return status();
  }

  function init() {
    return syncFromGit();
  }

  return {
    init,
    syncFromGit,
    readText,
    status,
    normalizeContentPath,
  };
}

module.exports = {
  createPremiumContentStore,
  normalizeContentPath,
  PREMIUM_PATH_PREFIXES,
};
