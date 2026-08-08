# ClearCrest — Target Markets & Location Site Strategy
*Top states, metros, and ICPs, and the site architecture they drive · August 2026*

## 1. The Targeting Model

ClearCrest wins where four conditions stack: (1) very hard water (10.5+ gpg by USGS definition, ideally 15+), (2) golf and master-planned community density, (3) affluent, growing homeowner populations, and (4) an air quality burden (inversions, dust, or wildfire smoke) that makes the air+water bundle sell itself. A fifth filter, competitive intensity, breaks ties: markets already saturated by strong Culligan/Kinetico dealers or air+water pure-plays score lower.

Roughly 85% of U.S. homes have some hard water, but the extreme markets cluster in the Southwest, Mountain West, Texas, and parts of the Midwest, driven by limestone geology and arid-climate evaporation concentrating minerals in river-fed supplies (the Colorado River system feeding Las Vegas and Phoenix, the Edwards Aquifer under San Antonio).

## 2. Top 10 States (ranked)

1. **Utah** — Home base. Nearly the entire state tests very hard (15–30+ gpg in most metros), winter inversions are a nationally known air problem, and Wasatch Front/Washington County growth keeps producing new master-planned and golf communities. Establish dominance here before anything else.
2. **Arizona** — The highest golf course density per capita in America (~9.8 per 100k residents), 12–22+ gpg Colorado/Salt River water, dust storms and the Phoenix "brown cloud," and a massive affluent retiree base. The single best expansion state.
3. **Nevada** — Las Vegas averages ~16 gpg off Lake Mead. Summerlin, Henderson, and Lake Las Vegas are dense with golf communities, and virtually every home needs softening.
4. **Texas** — San Antonio (Edwards Aquifer, 15–20 gpg) and the Austin Hill Country corridor combine extreme hardness with explosive growth in master-planned golf communities (Kissing Tree class developments).
5. **Florida** — The most golf courses in the nation (1,250+), with over 60% sitting inside HOA-governed master-planned communities; Southwest Florida groundwater is hard and PFAS awareness is high. Naples has the most golf holes per capita of any U.S. community.
6. **California (desert)** — The Coachella Valley (Palm Desert, La Quinta, Indian Wells) is wall-to-wall golf communities on hard Colorado River water; treat as a metro play, not a state play.
7. **Colorado** — Front Range hardness is moderate-to-hard rather than extreme, but wildfire smoke, affluence, and golf communities (Castle Pines corridor) make the air side of the bundle unusually strong.
8. **Idaho** — Boise/Eagle is one of the fastest-growing affluent metros in the West, with hard water, wildfire smoke summers, and new golf/master-planned developments; competition is thin.
9. **Indiana** — Indianapolis tests 12–20 gpg, among the hardest big-city water in America; golf-lifestyle density is lower, so this is a hardness-led rather than lifestyle-led market (Carmel/Zionsville are the wedge).
10. **Minnesota** — Minneapolis–St. Paul is a perennial hardest-water metro with among the highest golf participation rates in the country; strong seasonal business with a heavy softener-replacement installed base.

## 3. Top 10 Metros/Cities (site build order)

| # | Metro | Hardness | Anchor golf communities | Air story | Note |
|---|---|---|---|---|---|
| 1 | Park City / Heber Valley, UT | 12–28+ gpg | Promontory, Glenwild, Tuhaye, Red Ledges | Wildfire smoke | Cleanest premium beachhead; weakest specialist coverage |
| 2 | Eagle Mountain / Saratoga Springs, UT | 18–30+ gpg | The Ranches, SilverLake | Inversions, dust | Highest hardness; contest NuSoft's content moat |
| 3 | South Jordan / Daybreak, UT | 14–26+ gpg | Daybreak, Glenmoor | Worst inversion zone | Density play; referral engine market |
| 4 | Lehi / North Utah County, UT | 15–28+ gpg | Traverse Mountain, Alpine, Highland | Inversions, lake dust | Silicon Slopes income; Element's home turf |
| 5 | St. George / Washington County, UT | 15–26+ gpg | Entrada, SunRiver, Coral Canyon | Desert dust, smoke | Utah's golf capital; phase 4 market from the rollout plan |
| 6 | Scottsdale / North Phoenix, AZ | 12–22+ gpg | DC Ranch, Silverleaf, Troon, Desert Mountain | Dust, brown cloud | First out-of-state market; template built |
| 7 | Las Vegas — Summerlin / Henderson, NV | ~16 gpg | Summerlin, Anthem, Lake Las Vegas | Dust | Universal softener need |
| 8 | San Antonio — Hill Country, TX | 15–20 gpg | Dominion, Cordillera Ranch | Cedar allergens | Edwards Aquifer story writes itself |
| 9 | Naples / Bonita Springs, FL | Hard + PFAS salience | 90+ courses; most golf holes per capita in U.S. | Humidity/mold (UV story) | Highest ICP density anywhere |
| 10 | Palm Desert / La Quinta, CA | Hard Colorado River water | PGA West, Indian Wells corridor | Dust | Seasonal residents fit Concierge plan |

## 4. Ideal Customer Profiles

**ICP 1 — The Fairway Family (primary, ~60% of revenue target).** Ages 35–60, household income $150k+, home value $700k+, living in a golf or master-planned community. Health-conscious (PFAS, kids' allergies), time-poor, convenience buyers who join memberships everywhere else in their lives. Triggers: new build move-in, dead tankless heater, a neighbor's referral, a bad inversion week. Buys the bundle; attaches to Member tier.

**ICP 2 — The Lock-and-Leave Owner (premium, ~25%).** Ages 55+, primary or second home in Park City, St. George, Scottsdale, or Naples. Away for weeks at a time; wants monitored, maintained, transferable protection and same-day emergency response. Highest tickets, lowest price sensitivity, natural Concierge-tier member. Reached through HOAs, property managers, and club pro shops rather than Google.

**ICP 3 — The New-Build Buyer (pipeline, ~15%).** Buying in a growth community (Eagle Mountain, Daybreak, Cedar Valley). Water is at its worst, budgets are stretched, financing matters. Reached through builder and realtor partnerships; converts on the free test at move-in and grows into higher tiers over time.

**Secondary — HOA & light commercial.** CrestCares, pro shops, and HOA common facilities in the same communities; small revenue, outsized visibility and referral value.

## 5. Site Architecture (hub and spoke)

The site mirrors the targeting model in four layers, all generated from one config so content, schema, and the AI-agent layer never drift:

**Layer 1 — Brand homepage** (built): national positioning, systems, CrestCare plan, wizard.
**Layer 2 — State hubs** (`/utah/`, `/arizona/`): the state's water and air story, metro links, state licensing/credential language. Target keywords: "water softener utah", "pfas filter utah".
**Layer 3 — Metro/city pages** (built, 7 pages): localized hardness data, hero, scorecard, FAQs, LocalBusiness schema with geo coordinates, and local extraction copy. Target keywords: "water softener park city", "water softener cost eagle mountain", "whole house air purifier scottsdale".
**Layer 4 — Community pages** (the moat): one page per named golf community ("Water Softening in Promontory", "Daybreak Water Hardness Guide"). Nobody in this market builds at the community level; these are low-volume, near-zero-competition, extremely high-intent pages that also flatter the HOA/club partnership channel. Build once installs exist there, so each page can carry a real neighbor review and photos.

Supporting content clusters per metro (from the marketing plan's blog cadence): a "[City] water hardness: we tested it" data post, a PFAS-in-[city] explainer, and a cost-of-ownership post. Each cluster interlinks hub → metro → community and feeds the metro page's authority.

**Build order:** Utah metros 1–5 live at launch; Scottsdale page ships dark as the expansion template and goes live with phase 4/5 of the rollout plan; remaining metros follow acquisition or expansion decisions. Every page ships with the three-way AEO sync (page schema + ai-agents.json + /for-agents) updated in the same commit.

## 6. Measurement

Per metro page, track monthly: non-brand organic impressions and clicks for "[city] water softener" terms, wizard starts and completions, booked tests attributed to the page, and cost per booked test versus paid channels. A metro page earning 5+ booked tests/month justifies building its Layer 4 community pages; below 2/month after six months, the market gets demoted in the build order.
