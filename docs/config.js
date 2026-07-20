/**
 * Runtime config for the Programming Foundations site.
 *
 * Production API: https://programming101.onrender.com
 * Live site origin (for CORS): https://mrlucien-johnson.github.io
 *
 * Donations (free to set up — pick one and paste the public URL):
 *   Ko-fi:           https://ko-fi.com/YOUR_PAGE
 *   PayPal.Me:       https://paypal.me/YOUR_NAME
 *   Buy Me a Coffee: https://www.buymeacoffee.com/YOUR_PAGE
 *   GitHub Sponsors: https://github.com/sponsors/YOUR_USERNAME  (enable in GitHub settings first)
 */
(function () {
  const isLocalHost =
    location.hostname === "localhost" ||
    location.hostname === "127.0.0.1" ||
    location.hostname === "";

  const productionApiBaseUrl = "https://programming101.onrender.com";

  window.PF_CONFIG = {
    apiBaseUrl: isLocalHost ? "http://localhost:8787" : productionApiBaseUrl,
    // Paste your public donate link here when ready (leave "" until then).
    donateUrl: "",
    donateLabel: "Donate",
  };
})();
