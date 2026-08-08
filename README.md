# ClearCrest Water & Air — Website & Brand Repo

Whole-home water softening, PFAS filtration, and air purification for Utah homeowners.
Brand: **ClearCrest** (ClearCrest Water & Air LLC). Domain: **clearcresthome.com** (hosted on external server; the `/site` files here are the deployable artifact).

## Repo map
- `/` root: the deployable static site (index.html, locations/, AEO files, legal, 404)
- `/assets`: logo system + Kip the Kingfisher mascot (SVG)
- `/docs`: marketing plan, rollout plan, target-market & site strategy, design system spec
- `/tools`: page generator, validator, and the homepage base template

## How the site is built
Single-file React pages (React.createElement, no build step) on the Fusion design system
(`docs/fusion-design-system-1.md`): Outfit font, BRAND tokens, gradient headings, trust marquee,
tabbed systems, 3-step booking wizard, AEO layer (JSON-LD, extraction copy, llms.txt,
ai-agents.json, /for-agents).

Location pages are generated, never hand-edited:
```
cd tools && python3 generate_site_cc.py   # reads clearcrest-home.html, writes ../site tree
node validate-cc.js <page.html>            # syntax, SSR @1280/375, schema, FAQ parity, no phone
```
To add a market: add one config block in `generate_site_cc.py`, regenerate, validate, push.

## Brand quick reference
- Colors: blue #0A78C0, green #8AC838, dark #0F172A (full tokens in design system doc)
- Signature: "The ClearCrest Home Report" (letter-grade inspection card)
- Membership: CrestCare (Essential $29 / Complete $59 / Concierge $99, all "from" pricing)
- Mascot: Kip the Kingfisher ("kingfishers only live where the water is clean")
- Voice rules: no em dashes in body copy; never "leverage/seamless/robust"; prices always "from"

## Launch TODOs
- [ ] Web3Forms access key into `WEB3FORMS_KEY` (index.html + all location pages) so the wizard emails submissions
- [ ] Replace 3 sample reviews (marked TODO) with real ones
- [ ] Privacy policy: legal review + effective date
- [ ] No phone number anywhere by design; contact is schedule@/hello@clearcresthome.com (ImprovMX → owner Gmail)
- [ ] HubSpot portal/form IDs when CRM is stood up (upgrade path already wired in wizard)
