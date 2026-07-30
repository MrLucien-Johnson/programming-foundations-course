const express = require("express");
const {
  listConfiguredProviders,
  buildAuthorizeUrl,
  exchangeCodeForProfile,
  isSafeReturnTo,
  PROVIDERS,
} = require("../oauth");

function createOAuthRouter({
  auth,
  oauthStore,
  publicApiBase,
  allowedReturnOrigins,
  frontendDefaultReturn,
}) {
  const router = express.Router();

  router.get("/providers", (_req, res) => {
    return res.json({ providers: listConfiguredProviders() });
  });

  router.get("/:provider", (req, res) => {
    const provider = String(req.params.provider || "").toLowerCase();
    if (!PROVIDERS[provider]) {
      return res.status(404).json({ error: "Unknown sign-in provider." });
    }

    const returnTo = String(req.query.return_to || frontendDefaultReturn || "").trim();
    if (!isSafeReturnTo(returnTo, allowedReturnOrigins)) {
      return res.status(400).json({
        error:
          "Invalid return_to URL. Use your published site origin (listed in CORS_ORIGINS) or localhost.",
      });
    }

    try {
      const state = oauthStore.createState(returnTo);
      const url = buildAuthorizeUrl({
        providerId: provider,
        publicApiBase,
        state,
      });
      return res.redirect(302, url);
    } catch (error) {
      const status = error.status || 500;
      return res.status(status).json({ error: error.message || "Could not start social sign-in." });
    }
  });

  async function handleCallback(req, res) {
    const provider = String(req.params.provider || "").toLowerCase();
    const code = String((req.body && req.body.code) || req.query.code || "");
    const state = String((req.body && req.body.state) || req.query.state || "");
    const oauthError = String((req.body && req.body.error) || req.query.error || "");

    const stateRow = state ? oauthStore.consumeState(state) : null;
    const returnTo = stateRow?.return_to || frontendDefaultReturn || "";

    const failRedirect = (message) => {
      if (!returnTo) {
        return res.status(400).json({ error: message });
      }
      const url = new URL(returnTo);
      url.searchParams.set("oauth_error", message);
      return res.redirect(302, url.toString());
    };

    if (oauthError) {
      return failRedirect(`Sign-in was cancelled or denied (${oauthError}).`);
    }
    if (!PROVIDERS[provider]) {
      return failRedirect("Unknown sign-in provider.");
    }
    if (!stateRow) {
      return failRedirect("Sign-in session expired. Please try again.");
    }
    if (!code) {
      return failRedirect("Missing authorization code from the provider.");
    }

    try {
      const profile = await exchangeCodeForProfile({
        providerId: provider,
        code,
        publicApiBase,
      });
      // Apple may send the user's name only on the first authorization (form_post body).
      if (provider === "apple" && req.body && req.body.user) {
        try {
          const appleUser = typeof req.body.user === "string" ? JSON.parse(req.body.user) : req.body.user;
          const name = [appleUser?.name?.firstName, appleUser?.name?.lastName]
            .filter(Boolean)
            .join(" ")
            .trim();
          if (name && !profile.displayName) profile.displayName = name.slice(0, 80);
        } catch {
          /* ignore malformed Apple user payload */
        }
      }

      const userRow = oauthStore.upsertOAuthUser({
        provider,
        providerUserId: profile.providerUserId,
        email: profile.email,
        displayName: profile.displayName,
        onAuthenticated: auth.onAuthenticatedHook,
      });

      const loginCode = oauthStore.issueLoginCode(userRow.id);
      const url = new URL(returnTo);
      url.searchParams.delete("oauth_error");
      url.searchParams.set("oauth_code", loginCode);
      return res.redirect(302, url.toString());
    } catch (error) {
      return failRedirect(error.message || "Social sign-in failed.");
    }
  }

  router.get("/:provider/callback", (req, res) => {
    handleCallback(req, res);
  });

  // Apple uses response_mode=form_post.
  router.post(
    "/:provider/callback",
    express.urlencoded({ extended: false }),
    (req, res) => {
      handleCallback(req, res);
    }
  );

  router.post("/exchange", async (req, res) => {
    try {
      const code = String((req.body && req.body.code) || "").trim();
      if (!code) {
        return res.status(400).json({ error: "Missing oauth_code." });
      }
      const row = oauthStore.consumeLoginCode(code);
      if (!row) {
        return res.status(401).json({ error: "Sign-in code expired. Please try again." });
      }
      const result = auth.sessionForUser(row);
      return res.json(result);
    } catch (error) {
      const status = error.status || 500;
      return res.status(status).json({ error: error.message || "Could not complete sign-in." });
    }
  });

  return router;
}

module.exports = { createOAuthRouter };
