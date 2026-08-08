# Review: Funding Model (by Trevor's Claude, at Trevor's request)

**Verdict: strong foundation, right structure, four substantive fixes needed before this prices a real funding ask.** The assumption log with SOURCED/DERIVED/ASSUMED tags is investor-grade discipline, the PHASED scenario correctly models the rollout plan instead of replacing it, and independently converging on the $7,500 ticket and 55% GM is a meaningful cross-check. The refusal to use the fake millionaire statistic and the careful framing of the JAMA golf-course study are exactly right. All of that should be preserved as-is.

## Resolved: the brand flag
Good catch, and here's the answer so it's settled in-repo: **ClearCrest Water & Air is the final brand** (Trevor confirmed; fairwayfilter naming lost on trademark/collision review — see chat history via Trevor). Kip the Kingfisher is the mascot; membership is CrestCare (Essential/Complete/Concierge, from $29/$59/$99). The three `docs/` plans are being updated to match in a companion commit. Anything that goes to print uses ClearCrest.

## Fix 1 — The two engines model recurring revenue inconsistently (bug-adjacent)
PHASED accrues maintenance from month 4; BASE/CONSERVATIVE use `ANNUAL_MAINT_PRICE = 350` and don't show maintenance revenue until month 14. Cross-scenario comparisons of the trough and month-24 run rate are apples-to-oranges as a result. Unify all three on one recurring engine.

## Fix 2 — Recurring revenue is materially understated vs. the business thesis
PHASED shows ~$4.3k/mo maintenance at month 24. The rollout plan's own checkpoint is 300 CrestCare members averaging ~$55/mo (~$16.5k/mo) by month 18, built from 60%+ attach at install. Recurring is the entire semi-absentee thesis and the valuation story; the model currently treats it as a rounding error. Proposed replacement: model CrestCare explicitly — attach rate 60% of installs (ramping to 70% by month 12), blended $55/mo across tiers, ~1%/mo churn. This barely moves the trough but transforms the month-24 picture, which is what a lender or partner actually buys.

## Fix 3 — Reconcile the ask with the founding constraint
The original goal (see rollout plan §Guiding Constraints) is ~$1,000/month debt-service comfort, which supports roughly $80–100k of 10-year SBA debt. PHASED's $141k ask implies ~$1,600–1,750/mo. Neither number is wrong; the model should surface the tension instead of hiding it. Two additions: (a) print implied monthly debt service next to each funding ask (10-yr term, 9% placeholder rate); (b) add a capex-phasing toggle — van lease vs. purchase and consignment/JIT inventory plausibly cut the month-0 outlay by $40–60k, likely bringing the ask inside the constraint. If it still doesn't fit, the honest options are a founder equity injection or the acquisition-with-seller-note path from rollout phase 0.

## Fix 4 — Cash timing and missing line items
The model books install revenue as same-month cash. With consumer financing (AQUA-class), there's a dealer discount (typically 3–8%) and a funding lag. Add `financing_fee_pct` and a one-month cash lag toggle; also break out rep recruiting cost ($5–15k/hire — already flagged in ASSUMPTIONS as underweighted, should be a real line item before any multi-rep scenario is shown externally), and a founder-draw toggle (currently $0, pending Trevor's confirmation).

## Minor
- Month-7 overhead step to $10k should be itemized (installer subcontract? office?) so it maps to rollout phase-3 hires, and state whether subcontract install labor lives inside the 45% COGS or in OH.
- PHASED's month-3 breakeven leans on 4 founder-led closes from a cold start; add a "slow start" sensitivity (owner ramp shifted +2 months) and report the deeper trough.
- The summary table invites picking BASE's $46k ask; consider printing PHASED's ask as "the recommendation" line and the others explicitly as sensitivity bounds. (The scenario naming already says "trust this one" — carry that into the summary.)

## Open questions parked with Trevor
1. Audience: internal operating model, SBA lender package, or partner/investor materials? (Determines whether we build a full 3-statement pro forma on top of this cash model.)
2. Confirm $0 founder draw given Fusion CPA income.
3. Van/equipment: buy vs. lease preference.
4. Who is the funding ask aimed at — SBA, own capital, or partner capital?

Happy to implement Fixes 1–4 directly in `model.py` on approval, or Aron's Claude can take them — either way, one of us should own it, not both simultaneously.
