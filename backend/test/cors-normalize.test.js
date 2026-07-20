const test = require("node:test");
const assert = require("node:assert/strict");
const path = require("path");
const os = require("os");

process.env.JWT_SECRET = "test-secret";
process.env.DATABASE_PATH = path.join(os.tmpdir(), `pf-cors-test-${Date.now()}.sqlite`);
process.env.CORS_ORIGINS = "https://mrlucien-johnson.github.io/, \"https://example.com\"";

const { normalizeOrigin } = require("../src/server");

test("normalizeOrigin strips trailing slashes and quotes", () => {
  assert.equal(
    normalizeOrigin("https://mrlucien-johnson.github.io/"),
    "https://mrlucien-johnson.github.io"
  );
  assert.equal(
    normalizeOrigin(" https://mrlucien-johnson.github.io "),
    "https://mrlucien-johnson.github.io"
  );
  assert.equal(
    normalizeOrigin('"https://mrlucien-johnson.github.io/"'),
    "https://mrlucien-johnson.github.io"
  );
  assert.equal(normalizeOrigin("'https://example.com'"), "https://example.com");
  assert.equal(normalizeOrigin("*"), "*");
  assert.equal(normalizeOrigin("null"), "null");
});
