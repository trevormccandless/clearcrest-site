# Assumption Log

Every number in `model.py` and `BUSINESS-PLAN.md` is tagged by confidence. Read this before
trusting or presenting any figure externally.

- **[SOURCED]** — directly from a cited source, see links below.
- **[DERIVED]** — computed/inferred from sourced ranges (e.g. backing into COGS from a markup multiple).
- **[ASSUMED]** — no data found anywhere in research. A placeholder. **Do not use in an actual
  funding ask or investor conversation without validating it first** — the validation step is
  listed next to each one.

## Pricing

| Assumption | Value used | Confidence | Source / validation needed |
|---|---|---|---|
| Whole-house RO installed price | $5,000–$12,000 range; blended into $7,500 avg deal size across water/air/bundle | [SOURCED] range / [ASSUMED] blend | [Bob Vila](https://www.bobvila.com/articles/whole-house-reverse-osmosis-system-cost/), [HomeGuide](https://homeguide.com/costs/reverse-osmosis-system-cost). Sources disagree 2-3x — validate with 3 actual supplier/installer quotes before quoting to investors. |
| Premium whole-home air filtration installed price | $3,000–$6,000 range | [SOURCED] (Angi avg $2,610 general pop; premium tier inferred, not directly cited) | [Angi](https://www.angi.com/articles/whole-house-air-purifier-cost.htm), [HomeGuide](https://homeguide.com/costs/whole-house-air-purifier-cost) |
| Annual maintenance/certification plan | $350/yr | [SOURCED] synthesized from $250–500/yr comps | [Coopers Water](https://cooperswater.com/membership/whole-home-maintenance-program/), Culligan Platinum plan $150-300/yr comps. **No competitor sells a named "annual certification" product — this is white space, priced by analogy, not benchmarked directly.** |

## Cost structure

| Assumption | Value used | Confidence | Source / validation needed |
|---|---|---|---|
| Water gross margin | 55% (blend) | [SOURCED, CONFLICTING] one source cites ~70% GM, another implies ~55-60% GM from a 40-45% COGS figure | [FinancialModelsLab](https://financialmodelslab.com/blogs/kpi-metrics/whole-house-water-filtration). **Get real supplier quotes before trusting this.** |
| Air/HVAC gross margin | 50% (blend) | [SOURCED] HVAC industry 35-45% typical, 50-55% target; IAQ add-ons called out as higher-margin but no exact % | [Sera.tech](https://sera.tech/blog/hvac-profit-margin-calculator), [ServiceTitan](https://www.servicetitan.com/blog/hvac-profit-margins) |
| Blended gross margin (model) | 55% base / 50% conservative | [ASSUMED] blend of the two above | Validate once product mix (water-only vs air-only vs bundle) is real, not assumed 50/50 |

## Sales commission & hiring

| Assumption | Value used | Confidence | Source / validation needed |
|---|---|---|---|
| Commission rate | 10% of contract value | [SOURCED] range 4-8% company-lead / 8-12% self-gen (solar, water treatment comps) | [Everstage](https://www.everstage.com/sales-commission/solar-sales-commission), [Sequifi](https://blog.sequifi.com/solar-sales-commission/), [Salesman Connect](https://salesmanconnect.com/sales-salary/water-treatment) |
| Ramp curve (% of full quota by month of tenure) | 0/25/50/75/90/100% over 6 months | [SOURCED] | [RepCard](https://repcard.com/blog/30-60-90-day-sales-plan), [ORM-Tech](https://orm-tech.com/glossary/quota-ramp-schedule/) |
| **Full-ramp closes/rep/month** | BASE: 6, CONSERVATIVE: 3 | **[ASSUMED] — explicitly flagged by research as not found anywhere.** Backed into from close-rate comps (35-45% water treatment, 20-35% D2D general) × an assumed appointment volume, not a direct benchmark. | **This is the single highest-leverage number in the whole model and the least sourced. Validate ASAP with a small pilot (1-2 reps, 90 days) before scaling hiring or pricing a real funding round on it.** |
| Annual attrition | 50% | [SOURCED] range 30-70%+ in D2D home services | [SPOTIO](https://spotio.com/blog/door-to-door-sales-recruiting/) |
| Cost to recruit/onboard one rep | $5,000-$15,000 (not yet built into model as a line item — currently implicit in marketing/overhead) | [SOURCED] | [SPOTIO](https://spotio.com/blog/door-to-door-sales-recruiting/). **Should be broken out as its own line if hiring pace increases — currently underweighted in the model.** |

## Overhead & marketing

| Assumption | Value used | Confidence |
|---|---|---|
| Base monthly overhead (software, insurance, admin) | $6,000 (BASE) / $8,000 (CONSERVATIVE) | **[ASSUMED] — not researched at all.** Get real insurance quotes (general liability + install liability) and software costs before trusting this. |
| Marketing/lead-gen spend | $4,000 + $600/rep (BASE) / $5,000 + $900/rep (CONSERVATIVE) | **[ASSUMED] — not researched.** This is the second-highest-leverage unresearched number: it directly funds whether the "full-ramp closes/rep/month" assumption is achievable at all. |
| One-time startup cost | $25,000 (BASE) / $35,000 (CONSERVATIVE) | [ASSUMED] entity/legal, demo units, CRM setup, initial marketing collateral, insurance setup |
| Founder draw | $0 assumed | **[ASSUMED] — confirm with Aron/Trevor whether either needs to draw income, which would materially raise the funding ask.** |

## Market / thesis validation (from the golf-course market-sizing research)

- **Confirmed, well-sourced**: Florida has 2x the residential-golf-community density of the next
  closest state (California); ~3,200 US golf facilities have a residential component. Home price
  premiums for golf-course proximity run 15-30% (multiple sources, NAR/NGF/academic). [NGF/MIGCSA](https://www.migcsa.org/content.aspx?page_id=5&club_id=544808&item_id=106256)
- **Confirmed, real science, needs careful framing**: Mayo Clinic/Barrow Neurological Institute,
  *JAMA Network Open*, May 2025 — living within 1 mile of a golf course associated with adjusted
  OR 2.26 (95% CI 1.09-4.70) for Parkinson's vs. >6 miles away, in a single-county (Olmsted
  County, MN) case-control study. **This is an association in one geography with wide confidence
  intervals — not causal, not nationally representative. Do not market it as "golf courses cause
  Parkinson's."** [PubMed](https://pubmed.ncbi.nlm.nih.gov/40338549/), [Parkinson's Foundation](https://www.parkinson.org/blog/science-news/golf-courses)
- **Gap, explicitly not found**: no rigorous "% of US millionaires who live on/near a golf course"
  statistic exists. The founders' framing is directionally supported by adjacent data (income
  premiums, golf participation rate among the wealthy, Naples FL's outlier millionaire density)
  but should not cite a specific percentage that doesn't exist in any source.
- **Confirmed white space**: no dedicated golf-community-focused water or air filtration company
  was found in a direct search. This is the strongest, most verifiable part of the thesis.

## Benchmark company: Culligan

Full profile in `BUSINESS-PLAN.md`. Key figures used, with confidence:
- Franchise total investment $130K-$814K, franchise fee ~$0-$38.5K, royalty 1-2% of sales —
  **[SOURCED but internally conflicting across FDD-aggregator sites** — pull the actual current
  FDD Item 5/6/7 before using these numbers in any real comparison.
- Annual "Platinum"/"Privilege" service plan (28-point inspection) — closest real-world analog
  to the proposed "annual certification" product. [culligan.com/platinum](https://www.culligan.com/platinum)
- Field rep comp: base $34-50K + commission, avg total comp ~$116K, top performers $200K+ —
  [SOURCED] from Indeed/Glassdoor/ZipRecruiter aggregated data, not Culligan corporate disclosure.
