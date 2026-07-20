/**
 * Runtime config for the Programming Foundations site.
 *
 * For open beta / production:
 * 1. Deploy backend (see docs/OPEN-BETA-DEPLOY.md)
 * 2. Set productionApiBaseUrl to your HTTPS API URL
 * 3. Set CORS_ORIGINS on the API to your GitHub Pages origin
 */
(function () {
  const isLocalHost =
    location.hostname === "localhost" ||
    location.hostname === "127.0.0.1" ||
    location.hostname === "";

  // ← Replace this after Render deploy (no trailing slash)
  const productionApiBaseUrl = "https://YOUR-SERVICE.onrender.com";

  window.PF_CONFIG = {
    apiBaseUrl: isLocalHost ? "http://localhost:8787" : productionApiBaseUrl,
  };
})();
