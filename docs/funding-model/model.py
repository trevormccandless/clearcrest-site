#!/usr/bin/env python3
"""
ClearCrest / Fairway Filter — cash flow / funding / breakeven model.

Three scenarios:
  PHASED (rollout plan) — models docs/business-rollout-plan.md as written: founder-led sales
      through month 6, one commission rep added month 7, owner tapering to management. This is
      the scenario to trust for the real funding ask.
  BASE / CONSERVATIVE — an "aggressive multi-rep buildout" sensitivity check, built independently
      from industry research before the rollout plan existed. Answers a different question (what
      would faster/slower scaling than the rollout plan cost), not a competing recommendation.

See docs/funding-model/README.md for how these relate to each other.

Confidence tags on every assumption:
  [SOURCED]   directly from research, cited in ASSUMPTIONS.md
  [DERIVED]   computed/inferred from sourced ranges
  [PLAN]      taken directly from business-rollout-plan.md / marketing-content-plan.md — the
              founders' own stated targets, not third-party research.
  [ASSUMED]   no data found anywhere; a placeholder that needs validation.

Run: python3 model.py
"""

MONTHS = 24
RAMP_CURVE = [0.0, 0.25, 0.50, 0.75, 0.90, 1.00]  # [SOURCED] months 1-6 of a rep's own tenure
ANNUAL_ATTRITION = 0.50  # [SOURCED] 30-70%+ range; midpoint. Drives recruiting effort, not cash directly.


# ============================================================================
# PHASED (rollout plan) — the real scenario
# ============================================================================

def simulate_phased():
    # [PLAN] $7,500 avg ticket — matches both Trevor's rollout plan AND the independently
    #        researched BASE scenario below. Good cross-check.
    AVG_DEAL_SIZE = 7500
    GROSS_MARGIN_EQUIPMENT = 0.55   # [PLAN] phase-2 checkpoint: "gross margin >= 55% on equipment"
    GROSS_MARGIN_PLANS = 0.70       # [PLAN] phase-2 checkpoint: ">= 70% on plans"
    COMMISSION_RATE = 0.10          # [SOURCED] within the 4-12% researched range
    CLUBHOUSE_MONTHLY_PRICE = 55    # [PLAN] "300 members averaging $55/month"
    CLUBHOUSE_ATTACH = 0.65         # [PLAN] target 60-70%, midpoint

    # [PLAN] Phase 2: founder-led selling, target "100 tests and 30 installs" by month 6.
    # Ramping 4/6/9/11 = 30 cumulative by month 6. Zero commission cost — it's the owner's time.
    owner_closes = {1: 0, 2: 0, 3: 4, 4: 6, 5: 9, 6: 11}
    # [PLAN] Phase 3: owner "moves from selling to sales management" as the hired rep ramps up.
    for m in range(7, MONTHS + 1):
        owner_closes[m] = max(2, 8 - (m - 7))  # tapers 8->2 by month 13, holds at 2 (VIP/referral deals)

    # [PLAN] one commission-based in-home consultant, hired month 7, standard ramp curve.
    # [DERIVED] full-ramp closes/month = 6, cross-checked against the marketing plan's own KPI
    #           target ("20+ tests/month, 30% close" by month 6 -> ~6 closes/month), not just
    #           the generic industry inference used in BASE/CONSERVATIVE below.
    REP_FULL_RAMP_CLOSES = 6
    rep_hire_month = 7

    # [PLAN] one-time startup: Trevor's own stated "$75k-150k for a lean start" range, midpoint.
    ONE_TIME_STARTUP = 100000

    def overhead(month):
        # [PLAN] CRM (Housecall Pro-class), insurance, admin -- pre-hire vs. phase-3 payroll
        # (full-time lead installer + part-time dispatch coordinator) once the model is proven.
        base = 3500
        if month >= 7:
            base += 4500 + 2000  # lead installer + dispatch coordinator, per phase 3
        return base

    def marketing(month):
        # [PLAN] "$4,500-8,000/month" paid media guide from the marketing plan, ramped:
        # lighter pre-launch, full guide once phase 2 selling starts, a bit more once the rep
        # needs feeding leads too in phase 3.
        if month <= 2:
            return 3000
        if month <= 6:
            return 5000
        return 6500

    cash_cum = -ONE_TIME_STARTUP
    breakeven_month = None
    trough_month, trough_cash = 0, cash_cum
    active_customers = []
    rows = []

    rep_tenure = 0
    for month in range(1, MONTHS + 1):
        oc = owner_closes.get(month, 2)

        rep_closes = 0.0
        if month >= rep_hire_month:
            rep_tenure += 1
            ramp_idx = min(rep_tenure, 6) - 1
            rep_closes = REP_FULL_RAMP_CLOSES * RAMP_CURVE[ramp_idx]

        total_closes = oc + rep_closes
        revenue_owner = oc * AVG_DEAL_SIZE
        revenue_rep = rep_closes * AVG_DEAL_SIZE
        gross_profit = (revenue_owner + revenue_rep) * GROSS_MARGIN_EQUIPMENT
        commission_expense = revenue_rep * COMMISSION_RATE  # no commission on owner's own sales

        active_customers.extend([month] * round(total_closes))
        maint_revenue = sum(
            (CLUBHOUSE_MONTHLY_PRICE * CLUBHOUSE_ATTACH) * GROSS_MARGIN_PLANS
            for install_month in active_customers
            if month - install_month >= 1  # Clubhouse starts at install, not a 12mo lag
        )

        oh = overhead(month)
        mkt = marketing(month)
        net_cash_flow = gross_profit + maint_revenue - commission_expense - oh - mkt
        cash_cum += net_cash_flow

        if breakeven_month is None and net_cash_flow > 0:
            breakeven_month = month
        if cash_cum < trough_cash:
            trough_cash, trough_month = cash_cum, month

        rows.append(dict(month=month, headcount=(1 if month >= rep_hire_month else 0),
                          closes=round(total_closes, 1), revenue_new=round(revenue_owner + revenue_rep),
                          maint_revenue=round(maint_revenue), gross_profit=round(gross_profit),
                          commission_expense=round(commission_expense), overhead=oh, marketing=mkt,
                          net_cash_flow=round(net_cash_flow), cash_cum=round(cash_cum)))

    return rows, breakeven_month, trough_month, trough_cash


# ============================================================================
# BASE / CONSERVATIVE — aggressive multi-rep sensitivity check (pre-existing model)
# ============================================================================

def make_scenario(name, *, avg_deal_size, gross_margin, commission_rate,
                   full_ramp_closes, hiring_plan, overhead_base, overhead_mgmt_threshold,
                   overhead_mgmt_cost, marketing_base, marketing_per_rep, one_time_startup):
    return dict(name=name, avg_deal_size=avg_deal_size, gross_margin=gross_margin,
                commission_rate=commission_rate, full_ramp_closes=full_ramp_closes,
                hiring_plan=hiring_plan, overhead_base=overhead_base,
                overhead_mgmt_threshold=overhead_mgmt_threshold, overhead_mgmt_cost=overhead_mgmt_cost,
                marketing_base=marketing_base, marketing_per_rep=marketing_per_rep,
                one_time_startup=one_time_startup)


def hiring_plan_base():
    plan = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 6, 9: 7, 10: 8, 11: 8, 12: 8}
    for m in range(13, MONTHS + 1):
        plan[m] = 8
    return plan


def hiring_plan_conservative():
    plan = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5, 11: 5, 12: 5}
    for m in range(13, MONTHS + 1):
        plan[m] = 6
    return plan


SCENARIOS = [
    make_scenario("BASE (aggressive multi-rep, research midpoints)",
        avg_deal_size=7500, gross_margin=0.55, commission_rate=0.10,
        full_ramp_closes=6, hiring_plan=hiring_plan_base(),
        overhead_base=6000, overhead_mgmt_threshold=5, overhead_mgmt_cost=2500,
        marketing_base=4000, marketing_per_rep=600, one_time_startup=25000),
    make_scenario("CONSERVATIVE (aggressive multi-rep, unproven brand/channel)",
        avg_deal_size=6500, gross_margin=0.50, commission_rate=0.10,
        full_ramp_closes=3, hiring_plan=hiring_plan_conservative(),
        overhead_base=8000, overhead_mgmt_threshold=4, overhead_mgmt_cost=3000,
        marketing_base=5000, marketing_per_rep=900, one_time_startup=35000),
]

ANNUAL_MAINT_PRICE = 350  # [SOURCED] synthesized $250-500/yr range -- used only by BASE/CONSERVATIVE
MAINT_ATTACH_RATE = 0.65


def simulate(sc):
    rep_tenures = []
    active_customers = []
    cash_cum = -sc["one_time_startup"]
    breakeven_month = None
    trough_month, trough_cash = 0, cash_cum
    rows = []

    for month in range(1, MONTHS + 1):
        target_hc = sc["hiring_plan"][month]
        aged = [min(t + 1, 6) for t in rep_tenures]
        new_hires = max(0, target_hc - len(aged))
        rep_tenures = (aged + [1] * new_hires)[:target_hc]

        closes = sum(sc["full_ramp_closes"] * RAMP_CURVE[min(t, 6) - 1] for t in rep_tenures)

        revenue_new = closes * sc["avg_deal_size"]
        gross_profit = revenue_new * sc["gross_margin"]
        commission_expense = revenue_new * sc["commission_rate"]

        active_customers.extend([month] * round(closes))
        maint_revenue = sum((ANNUAL_MAINT_PRICE * MAINT_ATTACH_RATE) / 12
                             for install_month in active_customers if month - install_month >= 12)

        overhead = sc["overhead_base"] + (sc["overhead_mgmt_cost"] if target_hc >= sc["overhead_mgmt_threshold"] else 0)
        marketing = sc["marketing_base"] + sc["marketing_per_rep"] * target_hc

        net_cash_flow = (gross_profit + maint_revenue) - commission_expense - overhead - marketing
        cash_cum += net_cash_flow

        if breakeven_month is None and net_cash_flow > 0:
            breakeven_month = month
        if cash_cum < trough_cash:
            trough_cash, trough_month = cash_cum, month

        rows.append(dict(month=month, headcount=target_hc, closes=round(closes, 1),
                          revenue_new=round(revenue_new), maint_revenue=round(maint_revenue),
                          gross_profit=round(gross_profit), commission_expense=round(commission_expense),
                          overhead=overhead, marketing=marketing,
                          net_cash_flow=round(net_cash_flow), cash_cum=round(cash_cum)))

    return rows, breakeven_month, trough_month, trough_cash


def print_run(name, rows, breakeven_month, trough_month, trough_cash):
    print(f"\n{'='*100}\nSCENARIO: {name}\n{'='*100}")
    print(f"{'Mo':>3} {'HC':>3} {'Closes':>7} {'NewRev':>8} {'MaintRev':>9} {'GP':>8} {'Comm':>7} {'OH':>6} {'Mktg':>6} {'NetCF':>8} {'CumCash':>10}")
    for r in rows:
        print(f"{r['month']:>3} {r['headcount']:>3} {r['closes']:>7} {r['revenue_new']:>8} {r['maint_revenue']:>9} "
              f"{r['gross_profit']:>8} {r['commission_expense']:>7} {r['overhead']:>6} {r['marketing']:>6} "
              f"{r['net_cash_flow']:>8} {r['cash_cum']:>10}")
    print()
    print(f"Monthly cash-flow breakeven: month {breakeven_month}" if breakeven_month else "Breakeven NOT reached in 24mo window")
    print(f"Cash trough: month {trough_month}, cumulative cash position ${trough_cash:,.0f}")
    print(f"=> Funding ask (trough + 25% buffer): ${abs(trough_cash) * 1.25:,.0f}")


if __name__ == "__main__":
    results = []

    rows, be, tm, tc = simulate_phased()
    print_run("PHASED (rollout plan -- trust this one)", rows, be, tm, tc)
    results.append(("PHASED (rollout plan)", be, tc))

    for sc in SCENARIOS:
        rows, be, tm, tc = simulate(sc)
        print_run(sc["name"], rows, be, tm, tc)
        results.append((sc["name"], be, tc))

    print(f"\n{'='*100}\nSUMMARY\n{'='*100}")
    for name, be, trough in results:
        be_str = f"month {be}" if be else "not reached in 24mo"
        print(f"{name}: breakeven {be_str}, funding ask ${abs(trough)*1.25:,.0f}")
