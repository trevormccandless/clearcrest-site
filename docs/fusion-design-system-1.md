# Fusion CPA Website Design & Build System
## Portable Reference for New Claude Projects

**Source of truth:** fusion-homepage-v23-final.html is the canonical design system. Components are extracted from it directly, never recreated from memory. When porting to a new project, upload that file (or the equivalent reference page) as the component source.

**Last verified:** August 2026

---

## 1. Tech Stack

- Single-file HTML with embedded React (functional components + hooks)
- Pre-compiled JSX via `React.createElement` (no build step, no bundler)
- Google Font: **Outfit**, weights 300-800
- No external CSS framework. Inline styles only.
- Forms submit via HubSpot Forms API (`/submissions/v3/integration/submit/{portalId}/{formId}`). No iframes.
- HubSpot portal ID hardcoded: `50477734`. Each page declares:
  ```javascript
  const HUBSPOT_FORM_ID = "your-form-id-here"; // TODO: Replace with form ID for this page
  ```

---

## 2. Brand Color Tokens

```javascript
const BRAND = {
  blue: "#0A78C0", blueDark: "#065A90", green: "#8AC838",
  red: "#F03020", redLight: "#FF5040", yellow: "#F5A623", yellowMuted: "#E8D800",
  white: "#FFFFFF", offWhite: "#F7F8FA", greyBg: "#F0F2F5",
  grey: "#64748B", greyLight: "#94A3B8", greyBorder: "#E2E8F0",
  dark: "#0F172A", darkSoft: "#1E293B"
};
```

The discovery wizard code aliases this as `var B = BRAND;` and references `B.blue`, `B.dark`, etc. Keep the alias if reusing wizard code.

**Signature gradients:**
- Primary CTA / accents: `linear-gradient(135deg, BRAND.blue, BRAND.green)`
- Dark blocks / closing CTA: `linear-gradient(135deg, BRAND.dark, BRAND.blueDark)`

---

## 3. Typography

| Element | Spec |
|---|---|
| Section labels | 12px, uppercase, weight 600, letter-spacing 0.14em, color BRAND.blue |
| Section headings | `clamp(28px, 3.5vw, 40px)`, weight 800, letter-spacing -0.03em, color BRAND.dark |
| Heading key phrases | Gradient text: `linear-gradient(135deg, blue, green)` + `WebkitBackgroundClip: "text"` + `WebkitTextFillColor: "transparent"` |
| Body | 14-17px, line-height 1.6-1.8, color BRAND.grey |
| All text | `fontFamily: "'Outfit', sans-serif"` |

---

## 4. Component Patterns

- **Section label unit:** 40px x 2px gradient bar (blue to green) + uppercase label text
- **Cards:** border-radius 18-20px, `1px solid BRAND.greyBorder`, hover `translateY(-5px)` + colored box-shadow
- **Color accent bars:** 4-5px gradient strip across card tops
- **CTAs:** border-radius 10px, gradient background, 15px weight 600, trailing right-arrow character
- **Tab selectors:** pill-style, offWhite container; active tab = white bg + shadow + colored indicator
- **Hover transitions:** `cubic-bezier(0.16, 1, 0.3, 1)`, 0.3-0.45s
- **Background decoration:** subtle radial-gradient circles, absolute positioned, low-opacity brand colors
- **Trust signals:** animated counters (IntersectionObserver), star ratings, overlapping team photo stacks, certification badges, review cards
- **Trust marquee:** scrolling credential strip directly below hero

**Prohibited pattern:** simple dark-box-with-button closing CTA. The closing CTA is always the full dark gradient header + inline 3-step wizard (see Section 7).

---

## 5. Layout

- Max content width: 1100px (some sections 1200px), centered
- Section padding: 80-100px vertical, 48px horizontal (desktop)
- Card gaps: 16-18px
- Dark CTA blocks: dark gradient, border-radius 20-28px

### Animations (`@keyframes` defined in page styles)

`fadeIn, fadeSlideUp, fadeSlideRight, expandBar, expandWidth, pulse, marquee, float, ringRotate` — plus `scaleIn` and `slideUp` (required by the wizard).

---

## 6. Responsive System

**Breakpoints:** mobile < 768px, tablet 768-1023px, desktop >= 1024px.

**Required hook on every page:**

```javascript
function useWindowSize() {
  const [size, setSize] = React.useState({ width: window.innerWidth, height: window.innerHeight });
  React.useEffect(() => {
    const handle = () => setSize({ width: window.innerWidth, height: window.innerHeight });
    window.addEventListener('resize', handle);
    return () => window.removeEventListener('resize', handle);
  }, []);
  return size;
}
```

| Element | Desktop | Tablet | Mobile |
|---|---|---|---|
| Section padding | 80px 48px | 60px 32px | 48px 20px |
| Multi-column layouts | Row / grid | 2-col wrap | Single column |
| Hero (text + graphic) | Side-by-side | Stack, graphic scaled | Stack, graphic hidden |
| Cards | 3-4 columns | 2 columns | Single column |
| CTA button rows | Row, gap 14 | Row | Column, full-width |
| Wizard date step | Row, 52%/48% | Row | Column, stacked |
| Form grids | 2 columns | 2 columns | Single column |
| Touch targets | — | — | Min 44px height |
| Min font sizes | — | — | Body 14px, labels 12px, buttons 14px |

Nav hides below 768px, replaced by logo-only header. No horizontal overflow at any breakpoint.

---

## 7. Discovery Wizard (Closing CTA Component)

The old CalendarEmbed (single-step calendar + name/email form) is fully retired. Every page closes with the **3-Step Discovery Wizard** (`MainForm`) inside a dark gradient header wrapper.

**Step 1 (Your Needs):** service selection via checkbox cards (Tax, Bookkeeping, Controller, Family Advisory). Tax triggers Personal/Business/Both drill-down; Personal triggers SMLLC + filing status questions; Business triggers entity, revenue, software, start-date fields. Bookkeeping and Controller are mutually exclusive.

**Step 2 (Pick a Time):** next-10-weekday date picker (computed dynamically via `getWeekdays()` — no hardcoded month constants) + time slots; right panel shows live selection summary.

**Step 3 (Confirm):** name, email, phone, goals textarea, "How did you hear about us?" pill selector with referral tracking.

**Routing logic (`deriveRoute()`):** Susan (SB) for NetSuite accounting; Danielle (DP) for everything else; Tommy added to every call.

**Submission:** all fields compile into a structured HubSpot message field with routing headers.

**Wizard data arrays:** `SOFTWARE, REVENUE, ENTITIES, INDUSTRY_OPTIONS, FILING_STATUS, HEARD_OPTIONS, MONTH_NAMES, NOW, TIME_SLOTS`. Use `INDUSTRY_OPTIONS` (not `INDUSTRIES`) to avoid collision with other section data.

**Helper functions:** `deriveRoute(), getWeekdays(), submitHS(), inpS(), Pills(), RevPicker(), SubPanel(), Steps(), PersonalQuestions(), BusinessQuestions()`.

**Deployment:** standalone `/discovery-call/` page + inline at the bottom of homepage, every service page, and every industry page (same `#calendar` anchor). Nav "Schedule a Call" and all "Book a Call" buttons link to `/discovery-call/`.

Below the wizard: contact line with clickable phone + email and reassurance text ("No long-term contracts · No pressure · Free consultation").

---

## 8. Nav & Footer (extract from homepage v23, never rebuild)

**Nav:** 7 NavDropdown menus (Tax Services, Accounting, Software, Industries, Advisory & CFO, About Us, Locations) + "Schedule a Call" button linking to `/discovery-call/`. Base64 PNG logo (~8,410 chars, stored at `/home/claude/logo_base64.txt` during builds).

**Footer:** 5 columns (Tax Services, Accounting, Software, Advisory & CFO + Company, Locations with addresses). Credential badges (AICPA, EOS/Traction, NetSuite Certified). Regional phones. info@fusiontaxes.com. Social icons (LinkedIn, X, YouTube, Instagram, Facebook). Privacy Policy + Sitemap + "For AI Agents" links. Logo in white via `filter: brightness(0) invert(1)`.

**Trust marquee entries:** AICPA Member, GA Society of CPAs, PR Society of CPAs, UHNW Institute, QuickBooks Pro Advisor, Ramp Partner, NetSuite Certified, EOS / Traction, Entrepreneurs' Organization.

**Logo alt text (only place an em dash is permitted):** "Fusion CPA — Tax, Outsourced Accounting, and Advisory"

---

## 9. Page Templates

### Service / Industry Page Section Order (current, supersedes older specs)

| # | Component | Purpose |
|---|---|---|
| — | Navigation | |
| — | TrustMarquee | Credential strip |
| 1 | HeroSection (with ActivityStrip) | Hook |
| 2 | PainSection | Feel understood |
| 3 | CrossLinksSection (Industries) | See yourself |
| 4 | ReviewsSection | Trust |
| 5 | StageNavigator (tier-priced pages only) | Find your level |
| 6 | TabbedFiling | Understand |
| 7 | ServiceCards | Full picture |
| 8 | ProcessSection | Clear path (Stabilize / Strategize / Scale) |
| 9 | FAQSection | Overcome objections |
| 10 | InsightsSection | Productive exit for warm-but-not-ready visitors |
| 11 | BundleBanner (service pages only) | Incentivize |
| 12 | CTASection (dark header + MainForm wizard) | Act |
| — | ExtractionSection | AI agent content |
| — | Section13 Footer | |

**Key ordering rule:** Insights sits BEFORE the BundleBanner and CTA, not after. Nobody scrolls past a booking form to find reading material.

### Other templates
- **Industry pages:** same structure but NO bundle banner — only a secondary text link to `/pricing-structure/`. Include Platform Ecosystem row and Sub-Market Grid (4-12 cards; omit grid if fewer than 4 have published content; no placeholder # links).
- **Ad landing pages:** logo-only header, no nav; hero matching ad copy; 2-3 pain points; 3 benefit cards; 1-2 reviews; badges/counters; wizard or link to `/discovery-call/`; minimal footer with firm name, phone, both emails. Optional modal (max-width ~500px desktop, full-width mobile).
- **Location pages:** Atlanta page is the base. Local content (not city-name swaps), local industries, local phone, LocalBusiness schema with geo coordinates.

---

## 10. AI Agent / AEO Layer

**Core principle:** every page must be fully evaluable by an AI agent in isolation. The 5-Question Paste Test: from the raw HTML alone, an agent must be able to answer (1) what company is this, (2) what service does this page cover, (3) who is it for, (4) is it credible, (5) how do I engage and what does it cost to start.

### Schema (JSON-LD on every page)
- **AccountingService** node (name, url, telephone, email, areaServed, knowsAbout customized per page, all office locations, sameAs)
- **Two ContactPoint nodes:** customer service (phone + info@fusiontaxes.com) AND new client inquiries (discovery@fusiontaxes.com + /contact)
- By page type: Service + FAQPage (min 3 Qs) + BreadcrumbList (service/industry); LocalBusiness + geo (location); Article (blog); Person (any named team member); Review (any testimonial)
- FAQ questions written the way a real person asks an AI; answers standalone with phone + URL where natural

### Extraction copy (every service/location/landing page)
Two paragraphs answering two DIFFERENT questions: (1) what does the firm do for this audience/service, (2) what does the engagement look like / why choose them. Rules: say "Fusion CPA" (never only "we") at least once per paragraph; include phone, discovery@ email, and/or URL; be specific (steps, timelines, deliverables); at least one paragraph in the lower half of the page near the CTA.

### Agent-facing sentence (every page, third person, standalone-extractable)
"Fusion CPA provides [SERVICE] for [AUDIENCE] across all 50 states, operating from offices in Atlanta, GA, Puerto Rico, and Utah — email discovery@fusiontaxes.com, visit fusiontaxes.com, or call 404-955-7338 to schedule a free discovery call."

### Meta descriptions
Under 160 chars, written as a direct answer preview (services + audience + contact), never a tagline.

### Discovery assets + three-way sync rule (non-negotiable)
1. `/.well-known/ai-agents.json` — static JSON manifest (org identity, contacts, locations, services, industries, credentials, stats, engagement model, agent instructions)
2. `/for-agents` — single-file HTML authority page consolidating everything an agent needs
3. Individual page schema + extraction copy

All three must always agree. Any change to services, locations, credentials, contact info, phones, emails, stats, or pricing updates all three. Every page footer links "For AI Agents."

### Email rules
- info@fusiontaxes.com: only visible email in body copy, footer of every page, site-wide schema
- discovery@fusiontaxes.com: schema ContactPoint + readable text near CTAs on service/landing pages
- Never obfuscate either email. No "[at]/[dot]", no images, no JS-only rendering. Clean HTML text.
- Personal firstname@ addresses never appear on public pages.

---

## 11. Content Standards Carried Into Every Build

- Tax always positioned first: "tax preparation, tax planning, outsourced accounting, and CFO advisory." Entity pages name actual filings (1120-S, Form 1065).
- Audience: "high-achieving individuals and families" / "business owners and high-achieving individuals." "High-net-worth" never stands alone.
- Firm stats, always consistent: 20+ years, 2K+ businesses, 5.0 Google rating, 100+ reviews, 40+ states served.
- No em dashes in body copy (brand lockup only).
- Prohibited terms: "IRS-defensible," "state registration," "nexus audit," "leverage," "seamless," "robust," "fungible," fixed advisory frequency, "US-Based Team," "Medicare" in healthcare descriptions.
- Reviews weave team names mid-sentence or at the end, never as the opener.
- Prices always "from" / "starting at," always identify QuickBooks vs NetSuite track, ranges not absolutes.
- Bundle naming: "Bookkeeping" and "Controller" in pills, never "Accounting."

### Current pricing anchors (as of July 2026 — supersedes all earlier figures)
- Bundle tiers: Growth 10% / Scale 12% / Full Stack 15% ("Bundle and save 10-15%")
- Growth-Focused CFO floor: $3,000-$3,999/mo
- QB Full Stack: $3,493/mo (individual $4,109, save $616)
- NS Full Stack: $11,427/mo (individual $13,444, save $2,017)
- Bundle cards show percentage badge AND dollar savings
- Placement: homepage Section 11 (3 individual cards + dark gradient Bundle & Save banner + View Full Pricing CTA); service pages (banner between services section and closing CTA); industry pages (text link to /pricing-structure/ only); ad landing pages (optional text link only)

Note: a March 2026 addendum shows 15/18/20% tiers and "Save up to 20%." The July 2026 pricing update reverted/confirmed 10/12/15%. If both documents travel to the new project, the July 2026 figures above win.

---

## 12. Build & Validation Workflow (the "logic" side)

1. **Python assembly, never bash heredoc,** for writing all files (heredoc introduces formatting artifacts in long files).
2. **Single-source content generation:** visible page content and JSON-LD schema are generated from one config object so they cannot drift.
3. **FAQ schema parity:** the FAQPage mainEntity array is regenerated from the visible FAQ array after every edit, using a string-aware bracket walker (never naive regex).
4. **Validation pipeline per page:**
   - `vm.Script` (Node.js) syntax check
   - Headless `react-dom/server` render at 1280px
   - Repeat render at 375px
   - Spot-check rendered HTML for key strings (firm name, phones, both emails, agent sentence)
   - `json.loads` every JSON-LD block
5. **Three-way sync check** before delivery: does this change require updating ai-agents.json and /for-agents?
6. Components copied verbatim from the reference homepage file, never re-approximated.
7. WordPress MCP connector is scoped to blog posts only (Elementor is incompatible with the REST API); page builds go through SiteCare.

---

## 13. Per-Page Delivery Checklist (condensed)

**Design/tech:** single-file HTML + React; BRAND tokens; nav + footer match v23 exactly; useWindowSize present; viewport meta; HUBSPOT_FORM_ID const + TODO; hero CTA + closing wizard both present; trust marquee; scaleIn/slideUp keyframes; `B = BRAND` alias if wizard code present; no INDUSTRIES variable collision.

**Responsive:** padding scales; grids collapse; hero stacks; 44px touch targets; no text below 12px mobile; no horizontal overflow.

**SEO:** one H1 with primary keyword; meta title < 60 chars; meta description < 160 chars as answer preview; slug recommendation; 2-3 inbound + 2-3 outbound internal links, descriptive anchors, no placeholder # links.

**Content:** tax-first positioning; audience language; filing + compliance in scope; consistent stats; two extraction paragraphs (different questions); credential line matches location; no prohibited terms.

**AEO:** AccountingService schema; two ContactPoint nodes; page-type schema (Service/FAQPage/BreadcrumbList/LocalBusiness/Person/Review as applicable); agent-facing sentence; neither email obfuscated; passes 5-Question Paste Test; footer "For AI Agents" link; sync update flagged if identity data changed.

**Images:** descriptive alt text everywhere; badges use full credential names; team photos identify name/credentials/title; every trust signal exists as readable HTML text.
