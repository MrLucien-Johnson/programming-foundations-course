const crypto = require("crypto");
const jwt = require("jsonwebtoken");

/**
 * Free, standards-based OAuth 2.0 / OIDC for major providers.
 * Credentials come from env vars — never commit real client secrets.
 *
 * Supported: google, github, apple, microsoft
 */
const PROVIDERS = {
  google: {
    id: "google",
    label: "Google",
    authUrl: "https://accounts.google.com/o/oauth2/v2/auth",
    tokenUrl: "https://oauth2.googleapis.com/token",
    userInfoUrl: "https://openidconnect.googleapis.com/v1/userinfo",
    scopes: ["openid", "email", "profile"],
    clientIdEnv: "GOOGLE_CLIENT_ID",
    clientSecretEnv: "GOOGLE_CLIENT_SECRET",
  },
  github: {
    id: "github",
    label: "GitHub",
    authUrl: "https://github.com/login/oauth/authorize",
    tokenUrl: "https://github.com/login/oauth/access_token",
    userInfoUrl: "https://api.github.com/user",
    emailsUrl: "https://api.github.com/user/emails",
    scopes: ["read:user", "user:email"],
    clientIdEnv: "GITHUB_CLIENT_ID",
    clientSecretEnv: "GITHUB_CLIENT_SECRET",
  },
  microsoft: {
    id: "microsoft",
    label: "Microsoft",
    authUrl: "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
    tokenUrl: "https://login.microsoftonline.com/common/oauth2/v2.0/token",
    userInfoUrl: "https://graph.microsoft.com/oidc/userinfo",
    scopes: ["openid", "email", "profile"],
    clientIdEnv: "MICROSOFT_CLIENT_ID",
    clientSecretEnv: "MICROSOFT_CLIENT_SECRET",
  },
  apple: {
    id: "apple",
    label: "Apple",
    authUrl: "https://appleid.apple.com/auth/authorize",
    tokenUrl: "https://appleid.apple.com/auth/token",
    scopes: ["name", "email"],
    clientIdEnv: "APPLE_CLIENT_ID",
    // Apple uses a JWT client secret built from team/key/private key.
    teamIdEnv: "APPLE_TEAM_ID",
    keyIdEnv: "APPLE_KEY_ID",
    privateKeyEnv: "APPLE_PRIVATE_KEY",
    responseMode: "form_post",
  },
};

function readEnv(name) {
  const value = process.env[name];
  return value && String(value).trim() ? String(value).trim() : "";
}

function getProviderConfig(providerId) {
  const base = PROVIDERS[providerId];
  if (!base) return null;

  const clientId = readEnv(base.clientIdEnv);
  if (!clientId) return null;

  if (providerId === "apple") {
    const teamId = readEnv(base.teamIdEnv);
    const keyId = readEnv(base.keyIdEnv);
    const privateKey = normalizePem(readEnv(base.privateKeyEnv));
    if (!teamId || !keyId || !privateKey) return null;
    return { ...base, clientId, teamId, keyId, privateKey, configured: true };
  }

  const clientSecret = readEnv(base.clientSecretEnv);
  if (!clientSecret) return null;
  return { ...base, clientId, clientSecret, configured: true };
}

function normalizePem(value) {
  if (!value) return "";
  // Allow env vars with literal \n for multiline keys.
  return value.includes("-----BEGIN")
    ? value.replace(/\\n/g, "\n")
    : value;
}

function listConfiguredProviders() {
  return Object.keys(PROVIDERS)
    .map((id) => getProviderConfig(id))
    .filter(Boolean)
    .map((p) => ({ id: p.id, label: p.label }));
}

function buildAppleClientSecret(config) {
  const now = Math.floor(Date.now() / 1000);
  return jwt.sign(
    {
      iss: config.teamId,
      iat: now,
      exp: now + 60 * 50,
      aud: "https://appleid.apple.com",
      sub: config.clientId,
    },
    config.privateKey,
    {
      algorithm: "ES256",
      keyid: config.keyId,
    }
  );
}

function callbackUrl(publicApiBase, providerId) {
  return `${publicApiBase.replace(/\/$/, "")}/api/auth/oauth/${providerId}/callback`;
}

function buildAuthorizeUrl({ providerId, publicApiBase, state }) {
  const config = getProviderConfig(providerId);
  if (!config) {
    const err = new Error(`Sign-in with ${providerId} is not configured.`);
    err.status = 503;
    throw err;
  }

  const redirectUri = callbackUrl(publicApiBase, providerId);
  const params = new URLSearchParams({
    client_id: config.clientId,
    redirect_uri: redirectUri,
    response_type: "code",
    state,
    scope: config.scopes.join(" "),
  });

  if (config.responseMode) {
    params.set("response_mode", config.responseMode);
  }
  if (providerId === "google" || providerId === "microsoft") {
    params.set("access_type", "online");
    params.set("prompt", "select_account");
  }
  if (providerId === "github") {
    // GitHub ignores unused params; keep URL clean.
    params.delete("access_type");
    params.delete("prompt");
  }

  return `${config.authUrl}?${params.toString()}`;
}

async function exchangeCodeForProfile({ providerId, code, publicApiBase }) {
  const config = getProviderConfig(providerId);
  if (!config) {
    const err = new Error(`Sign-in with ${providerId} is not configured.`);
    err.status = 503;
    throw err;
  }

  const redirectUri = callbackUrl(publicApiBase, providerId);
  const clientSecret =
    providerId === "apple" ? buildAppleClientSecret(config) : config.clientSecret;

  const body = new URLSearchParams({
    client_id: config.clientId,
    client_secret: clientSecret,
    code,
    grant_type: "authorization_code",
    redirect_uri: redirectUri,
  });

  const tokenRes = await fetch(config.tokenUrl, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });
  const tokenJson = await tokenRes.json().catch(() => ({}));
  if (!tokenRes.ok || !tokenJson.access_token) {
    const detail = tokenJson.error_description || tokenJson.error || "token exchange failed";
    const err = new Error(`Could not complete ${config.label} sign-in (${detail}).`);
    err.status = 502;
    throw err;
  }

  if (providerId === "apple") {
    return profileFromApple(tokenJson);
  }
  if (providerId === "github") {
    return profileFromGitHub(tokenJson.access_token);
  }
  return profileFromUserInfo(config, tokenJson.access_token);
}

async function profileFromUserInfo(config, accessToken) {
  const res = await fetch(config.userInfoUrl, {
    headers: { Authorization: `Bearer ${accessToken}`, Accept: "application/json" },
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const err = new Error(`Could not load ${config.label} profile.`);
    err.status = 502;
    throw err;
  }
  const email = String(data.email || "").trim().toLowerCase();
  if (!email) {
    const err = new Error(`${config.label} did not share an email address. Allow email access and try again.`);
    err.status = 400;
    throw err;
  }
  return {
    providerUserId: String(data.sub || data.id || email),
    email,
    displayName: String(data.name || data.given_name || "").trim().slice(0, 80),
    emailVerified: data.email_verified !== false,
  };
}

async function profileFromGitHub(accessToken) {
  const headers = {
    Authorization: `Bearer ${accessToken}`,
    Accept: "application/vnd.github+json",
    "User-Agent": "programming-foundations-api",
  };
  const userRes = await fetch(PROVIDERS.github.userInfoUrl, { headers });
  const user = await userRes.json().catch(() => ({}));
  if (!userRes.ok || !user.id) {
    const err = new Error("Could not load GitHub profile.");
    err.status = 502;
    throw err;
  }

  let email = String(user.email || "").trim().toLowerCase();
  if (!email) {
    const emailsRes = await fetch(PROVIDERS.github.emailsUrl, { headers });
    const emails = await emailsRes.json().catch(() => []);
    if (Array.isArray(emails)) {
      const primary =
        emails.find((e) => e.primary && e.verified) ||
        emails.find((e) => e.verified) ||
        emails[0];
      email = String(primary?.email || "").trim().toLowerCase();
    }
  }
  if (!email) {
    const err = new Error("GitHub did not share an email address. Make a public/verified email available and try again.");
    err.status = 400;
    throw err;
  }

  return {
    providerUserId: String(user.id),
    email,
    displayName: String(user.name || user.login || "").trim().slice(0, 80),
    emailVerified: true,
  };
}

function profileFromApple(tokenJson) {
  const idToken = tokenJson.id_token;
  if (!idToken) {
    const err = new Error("Apple did not return an ID token.");
    err.status = 502;
    throw err;
  }
  // Apple's id_token is signed by Apple; we decode claims after successful token exchange.
  const payload = jwt.decode(idToken);
  if (!payload || !payload.sub) {
    const err = new Error("Could not read Apple identity token.");
    err.status = 502;
    throw err;
  }
  const email = String(payload.email || "").trim().toLowerCase();
  if (!email) {
    const err = new Error(
      "Apple did not share an email. Use “Share My Email” (or an existing linked account) and try again."
    );
    err.status = 400;
    throw err;
  }
  return {
    providerUserId: String(payload.sub),
    email,
    displayName: "",
    emailVerified: payload.email_verified !== "false" && payload.email_verified !== false,
  };
}

function createOAuthStore(db) {
  db.exec(`
    CREATE TABLE IF NOT EXISTS oauth_accounts (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      provider TEXT NOT NULL,
      provider_user_id TEXT NOT NULL,
      created_at TEXT NOT NULL,
      UNIQUE(provider, provider_user_id)
    );
    CREATE INDEX IF NOT EXISTS idx_oauth_user ON oauth_accounts(user_id);

    CREATE TABLE IF NOT EXISTS oauth_states (
      state TEXT PRIMARY KEY,
      return_to TEXT NOT NULL,
      created_at TEXT NOT NULL,
      expires_at TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS oauth_codes (
      code TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      created_at TEXT NOT NULL,
      expires_at TEXT NOT NULL
    );
  `);

  const insertState = db.prepare(`
    INSERT INTO oauth_states (state, return_to, created_at, expires_at)
    VALUES (@state, @return_to, @created_at, @expires_at)
  `);
  const takeState = db.prepare(`SELECT * FROM oauth_states WHERE state = ?`);
  const deleteState = db.prepare(`DELETE FROM oauth_states WHERE state = ?`);
  const purgeStates = db.prepare(`DELETE FROM oauth_states WHERE expires_at < ?`);

  const insertCode = db.prepare(`
    INSERT INTO oauth_codes (code, user_id, created_at, expires_at)
    VALUES (@code, @user_id, @created_at, @expires_at)
  `);
  const takeCode = db.prepare(`SELECT * FROM oauth_codes WHERE code = ?`);
  const deleteCode = db.prepare(`DELETE FROM oauth_codes WHERE code = ?`);
  const purgeCodes = db.prepare(`DELETE FROM oauth_codes WHERE expires_at < ?`);

  const findOAuth = db.prepare(
    `SELECT * FROM oauth_accounts WHERE provider = ? AND provider_user_id = ?`
  );
  const findOAuthByUser = db.prepare(
    `SELECT provider FROM oauth_accounts WHERE user_id = ? ORDER BY provider`
  );
  const insertOAuth = db.prepare(`
    INSERT INTO oauth_accounts (id, user_id, provider, provider_user_id, created_at)
    VALUES (@id, @user_id, @provider, @provider_user_id, @created_at)
  `);
  const findUserByEmail = db.prepare(`SELECT * FROM users WHERE email = ?`);
  const findUserById = db.prepare(`SELECT * FROM users WHERE id = ?`);
  const insertUser = db.prepare(`
    INSERT INTO users (id, email, display_name, password_hash, token_version, created_at, updated_at)
    VALUES (@id, @email, @display_name, '', 0, @created_at, @updated_at)
  `);
  const touchUser = db.prepare(`UPDATE users SET updated_at = ? WHERE id = ?`);

  function createState(returnTo) {
    purgeStates.run(new Date().toISOString());
    const state = crypto.randomBytes(24).toString("hex");
    const now = new Date();
    const expires = new Date(now.getTime() + 10 * 60 * 1000);
    insertState.run({
      state,
      return_to: returnTo,
      created_at: now.toISOString(),
      expires_at: expires.toISOString(),
    });
    return state;
  }

  function consumeState(state) {
    purgeStates.run(new Date().toISOString());
    const row = takeState.get(state);
    if (!row) return null;
    deleteState.run(state);
    if (new Date(row.expires_at).getTime() < Date.now()) return null;
    return row;
  }

  function issueLoginCode(userId) {
    purgeCodes.run(new Date().toISOString());
    const code = crypto.randomBytes(24).toString("hex");
    const now = new Date();
    const expires = new Date(now.getTime() + 2 * 60 * 1000);
    insertCode.run({
      code,
      user_id: userId,
      created_at: now.toISOString(),
      expires_at: expires.toISOString(),
    });
    return code;
  }

  function consumeLoginCode(code) {
    purgeCodes.run(new Date().toISOString());
    const row = takeCode.get(code);
    if (!row) return null;
    deleteCode.run(code);
    if (new Date(row.expires_at).getTime() < Date.now()) return null;
    return findUserById.get(row.user_id) || null;
  }

  function upsertOAuthUser({ provider, providerUserId, email, displayName, onAuthenticated }) {
    const existingLink = findOAuth.get(provider, providerUserId);
    if (existingLink) {
      const user = findUserById.get(existingLink.user_id);
      if (!user) {
        const err = new Error("Linked account is missing. Contact support or create a new account.");
        err.status = 500;
        throw err;
      }
      touchUser.run(new Date().toISOString(), user.id);
      if (typeof onAuthenticated === "function") {
        try {
          onAuthenticated({
            id: user.id,
            email: user.email,
            displayName: user.display_name || "",
            createdAt: user.created_at,
          });
        } catch {
          /* ignore */
        }
      }
      return user;
    }

    const normalizedEmail = String(email || "").trim().toLowerCase();
    let user = findUserByEmail.get(normalizedEmail);
    const now = new Date().toISOString();
    if (!user) {
      user = {
        id: crypto.randomUUID(),
        email: normalizedEmail,
        display_name: displayName || "",
        created_at: now,
        updated_at: now,
      };
      insertUser.run(user);
      user = findUserById.get(user.id);
    } else if (displayName && !user.display_name) {
      db.prepare(`UPDATE users SET display_name = ?, updated_at = ? WHERE id = ?`).run(
        displayName,
        now,
        user.id
      );
      user = findUserById.get(user.id);
    }

    insertOAuth.run({
      id: crypto.randomUUID(),
      user_id: user.id,
      provider,
      provider_user_id: providerUserId,
      created_at: now,
    });

    if (typeof onAuthenticated === "function") {
      try {
        onAuthenticated({
          id: user.id,
          email: user.email,
          displayName: user.display_name || "",
          createdAt: user.created_at,
        });
      } catch {
        /* ignore */
      }
    }
    return user;
  }

  function providersForUser(userId) {
    return findOAuthByUser.all(userId).map((r) => r.provider);
  }

  return {
    createState,
    consumeState,
    issueLoginCode,
    consumeLoginCode,
    upsertOAuthUser,
    providersForUser,
  };
}

function isSafeReturnTo(returnTo, allowedOrigins) {
  if (!returnTo || typeof returnTo !== "string") return false;
  let url;
  try {
    url = new URL(returnTo);
  } catch {
    return false;
  }
  if (url.protocol !== "https:" && url.protocol !== "http:") return false;
  // Allow localhost for local testing.
  if (url.hostname === "localhost" || url.hostname === "127.0.0.1") return true;
  const origin = `${url.protocol}//${url.host}`;
  return allowedOrigins.includes(origin) || allowedOrigins.includes("*");
}

module.exports = {
  PROVIDERS,
  listConfiguredProviders,
  getProviderConfig,
  buildAuthorizeUrl,
  exchangeCodeForProfile,
  createOAuthStore,
  callbackUrl,
  isSafeReturnTo,
};
