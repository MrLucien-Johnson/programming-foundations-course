/**
 * Runtime config for the Programming Foundations site.
 *
 * Production API: https://programming-foundations-course.onrender.com
 * Live site origin (for CORS): https://mrlucien-johnson.github.io
 */
(function () {
  const isLocalHost =
    location.hostname === "localhost" ||
    location.hostname === "127.0.0.1" ||
    location.hostname === "";

  const productionApiBaseUrl = "https://programming-foundations-course.onrender.com";

  window.PF_CONFIG = {
    apiBaseUrl: isLocalHost ? "http://localhost:8787" : productionApiBaseUrl,
  };
})();
