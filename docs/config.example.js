/**
 * Runtime config for the Programming Foundations site.
 * Copy values into config.js after you deploy the API.
 */
(function () {
  const isLocalHost =
    location.hostname === "localhost" ||
    location.hostname === "127.0.0.1" ||
    location.hostname === "";

  const productionApiBaseUrl = "https://YOUR-SERVICE.onrender.com";

  window.PF_CONFIG = {
    apiBaseUrl: isLocalHost ? "http://localhost:8787" : productionApiBaseUrl,
    // Free donation link (Ko-fi, PayPal.Me, Buy Me a Coffee, or GitHub Sponsors)
    donateUrl: "",
    donateLabel: "Donate",
  };
})();
