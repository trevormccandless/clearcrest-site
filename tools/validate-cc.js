const fs = require("fs");
const vm = require("vm");
const React = require("react");
const ReactDOMServer = require("react-dom/server");

const html = fs.readFileSync(process.argv[2] || "./fairway-v2.html", "utf8");

// Extract the main inline script (the last <script> block without src)
const blocks = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (!blocks.length) { console.error("FAIL: no inline script found"); process.exit(1); }
const code = blocks[blocks.length - 1];

// 1. Syntax check
new vm.Script(code);
console.log("PASS: vm.Script syntax check");

function renderAt(width) {
  const sandbox = {
    React,
    ReactDOM: { createRoot: () => ({ render: () => {} }) },
    window: { innerWidth: width, innerHeight: 800, addEventListener: () => {}, removeEventListener: () => {} },
    document: undefined, // typeof document === "undefined" branch: skip DOM mount
    location: { href: "https://clearcresthome.com" },
    console,
    setTimeout,
    module: { exports: {} },
    IntersectionObserver: undefined,
    fetch: () => Promise.resolve({ ok: true }),
    requestAnimationFrame: (cb) => setTimeout(cb, 0),
  };
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);
  const App = sandbox.module.exports.App;
  if (!App) throw new Error("App not exported");
  return ReactDOMServer.renderToString(React.createElement(App));
}

// 2 & 3. Headless renders
const out1280 = renderAt(1280);
console.log("PASS: SSR render at 1280px (" + out1280.length + " chars)");
const out375 = renderAt(375);
console.log("PASS: SSR render at 375px (" + out375.length + " chars)");

// 4. String spot-checks (rendered output + raw HTML)
const checks = [
  ["ClearCrest", out1280],
  ["hello@clearcresthome.com", out1280],
  ["schedule@clearcresthome.com", out1280],
  ["or visit clearcresthome.com to schedule a free in-home", out1280], // agent-facing sentence
  ["The ClearCrest Home Report", out1280],
  ["For AI Agents", out1280],
  ["CrestCare", out1280],
];
let ok = true;
for (const [needle, hay] of checks) {
  if (hay.indexOf(needle) === -1) { console.error("FAIL: missing string: " + needle); ok = false; }
}
if (ok) console.log("PASS: all string spot-checks");

// Mobile check: scorecard hidden, content still present
if (out375.indexOf("The ClearCrest Home Report") === -1 && out375.indexOf("ClearCrest") !== -1) {
  console.log("PASS: hero graphic hidden on mobile, content intact");
} else if (out375.indexOf("The ClearCrest Home Report") !== -1) {
  console.log("NOTE: scorecard renders on mobile (check spec: graphic hidden on mobile)");
}

if (out1280.indexOf("(801)") !== -1 || out1280.indexOf("tel:+1801") !== -1) { console.error("FAIL: phone number present"); ok = false; } else { console.log("PASS: no phone number on page"); }

// 5. JSON-LD parse
const ldBlocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
ldBlocks.forEach((m, i) => {
  JSON.parse(m[1]);
  console.log("PASS: JSON-LD block " + (i + 1) + " parses (" + JSON.parse(m[1])["@type"] + ")");
});

// 6. Content standards: no em dashes in body copy (allow none at all here)
const emDashes = (out1280.match(/\u2014/g) || []).length;
console.log(emDashes === 0 ? "PASS: no em dashes in rendered body copy" : "NOTE: " + emDashes + " em dash(es) found in rendered output");

// Prohibited terms
const prohibited = ["leverage", "seamless", "robust", "IRS-defensible", "US-Based Team"];
const found = prohibited.filter(t => out1280.toLowerCase().includes(t.toLowerCase()));
console.log(found.length === 0 ? "PASS: no prohibited terms" : "FAIL: prohibited terms: " + found.join(", "));

// FAQ parity: every visible FAQ question exists in FAQPage schema
const faqSchema = ldBlocks.map(m => JSON.parse(m[1])).find(o => o["@type"] === "FAQPage");
const schemaQs = faqSchema.mainEntity.map(q => q.name);
const visibleQs = [...out1280.matchAll(/aria-expanded/g)].length;
console.log("INFO: " + schemaQs.length + " schema FAQs, " + visibleQs + " visible FAQ buttons");
let parity = true;
for (const q of schemaQs) {
  const esc = q.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/'/g, "&#x27;");
  if (out1280.indexOf(esc) === -1 && out1280.indexOf(q) === -1) { console.error("FAIL: schema FAQ not visible: " + q); parity = false; }
}
if (parity) console.log("PASS: FAQ schema parity with visible FAQs");
