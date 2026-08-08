# Funding Model — how this relates to `business-rollout-plan.md`

This folder was built independently (by Aron, before seeing Trevor's `business-rollout-plan.md`,
`marketing-content-plan.md`, and `target-markets-site-strategy.md`) from industry research into
water treatment / air filtration unit economics, commission-based field sales, and golf-course
community market sizing. It converged on real numbers close to Trevor's — **$7,500 average
ticket, independently arrived at the same figure**; 55%/70% gross margin split, matching
Trevor's phase-2 checkpoints — which is a good cross-check that the two efforts agree.

**Where it diverges, explicitly:**

`business-rollout-plan.md` is founder-led-first: the owner sells personally through month 6
(phase 2 proof-of-model), and hiring is one commission-based in-home consultant starting around
month 7-18 (phase 3), building toward a semi-absentee model on a $1,000/month debt-service
comfort level. That's the real, capital-constrained baseline plan.

The original model in this folder (`model.py`, scenarios `BASE` and `CONSERVATIVE`) was built
before that context existed, from generic industry benchmarks alone, and assumed scaling to
**8 commission reps by month 10** — a much faster, larger buildout than the rollout plan
describes. It isn't wrong on its own terms (the per-rep unit economics are the same numbers
Trevor's plan uses), but it answers a different question: not "what does Trevor's actual phased
plan cost," but "what would an aggressive multi-rep commission buildout cost, and would it reach
breakeven faster."

**Added a third scenario, `PHASED (rollout plan)`,** that actually models
`business-rollout-plan.md` as written: founder-led sales ramping to ~30 installs by month 6 (no
commission cost — it's the owner's own time), then one commission rep added at month 7 on the
standard ramp curve, with the owner's personal selling tapering as they shift to sales
management per phase 3. This is the scenario to trust for the real funding ask;
`BASE`/`CONSERVATIVE` are left in as an "what if we scaled faster/slower than the rollout plan"
sensitivity check, not competing recommendations.

**One thing worth resolving at the founder level, not something I resolved myself:** the docs in
this repo call the brand "Fairway Filter" with mascot "Finn the Fairway Falcon" throughout
(`business-rollout-plan.md`, `marketing-content-plan.md`, `target-markets-site-strategy.md`),
but the live site (`index.html`, `ai-agents.json`, `llms.txt`, `README.md`) uses "ClearCrest
Water & Air" with mascot "Kip the Kingfisher." Both are fully fleshed-out brand systems, not
placeholders — this reads like an in-progress rebrand where the docs weren't updated to match
the final site, or vice versa. Whichever is current, the other should be updated to match before
this goes to print/production anywhere (business cards, van wraps, the plush mascot order in the
marketing plan) — flagging rather than silently picking one.

See `ASSUMPTIONS.md` for the full sourced/derived/assumed breakdown with citations, and run
`python3 model.py` for the actual month-by-month numbers across all three scenarios.
