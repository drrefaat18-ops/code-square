---
date: 2026-09-02
type: pricing-architecture
tags:
  - offers
  - pricing
  - packaging
  - margin
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Pricing and Packaging — Code Square

## For future Claude

**This file contains no Code Square prices, and that is deliberate.**

`[[Foundation Brief]]` §6 and §10 state that real pricing is undecided and that only the founder may set it. Inventing a number here would fabricate a company fact, which `[[Foundation Brief]]` §0.1 forbids outright. So this file provides the **architecture and the decision framework**: which pricing model to use for which service, how to derive a floor and a ceiling, how to structure retainers, payment terms, deposits, change requests, currency, and discounts — with every actual figure written as `TBD — founder must set`.

Rules for editing:
- **Never fill in a Code Square price without the founder saying it.** If the founder sets one, replace the `TBD` and change the label from `TBD` to `stated`.
- **External benchmark ranges are allowed** with a source URL and a date, and must always be labelled `researched — external benchmark, NOT Code Square's price`. They inform a decision; they are never a quote.
- The `$19 / $49 / $99` on the SaaS infographic is **mockup art**. §11 exists solely to prevent it ever being quoted.
- Terminology is defined in the `[[Service Catalog]]` §12 glossary; the pricing-specific terms are defined inline here.

---

## 1. The three-number frame — how any price gets decided

Every price sits between a floor and a ceiling, checked against the market.

```
        VALUE CEILING  ────────── what the client gains (§3)
              ▲                    above this, nobody buys
              │
        ┌─────┴─────┐
        │ THE BAND  │  ← the price lives here, positioned by
        │           │    confidence, proof, and demand
        └─────┬─────┘
              │
         COST FLOOR  ─────────── what delivery costs + target margin (§2)
              ▼                   below this, Code Square loses money
                                  while looking busy

     MARKET REFERENCE (§4) tells you where in the band a buyer
     expects to land — it is a sanity check, never the method.
```

**The failure modes, both fatal:**
- **Price below the floor** → the busiest year of the company's life ends with no money. This is how agencies die: not from no work, from unprofitable work.
- **Price at the floor when the ceiling is far above** → the company subsidises its clients and never accumulates the capital to hire, market, or survive a slow quarter.

`[[Foundation Brief]]` §2 Layer 3 notes Code Square has genuinely uncopyable assets (maritime software, a live education platform, a pharmacist founder). **Assets like those belong near the ceiling, not the floor.** Pricing at the floor with those assets in hand is the most expensive mistake available here.

---

## 2. The cost floor — derive it before quoting anything

### 2.1 The fully-loaded day rate

Never price from a salary. Price from a **fully-loaded, utilisation-adjusted day rate**, which is always much higher than a salary divided by working days — and the gap is where agencies quietly go bankrupt.

**Step 1 — annual cost of one delivery person**

| Line | Value |
|---|---|
| Gross salary | `TBD — founder must set` |
| Employer taxes, insurance, statutory costs | `TBD` |
| Equipment, amortised | `TBD` |
| Software, licences, cloud, tools per head | `TBD` |
| Share of rent, internet, utilities, admin | `TBD` |
| Training and recruitment | `TBD` |
| **A = total annual cost per delivery head** | `TBD` |

**Step 2 — billable days per year (the number everyone gets wrong)**

| Line | Illustrative arithmetic |
|---|---|
| Calendar days | 365 |
| − weekends | ≈ 261 remaining |
| − public holidays (Egypt) | `TBD` — count them |
| − annual leave | `TBD` |
| − sick and contingency | `TBD` |
| **= available working days** | `TBD` |
| × **utilisation rate** | **60–70% realistic for a small agency** |
| **B = billable days per year** | `TBD` |

> **Utilisation is the number that destroys naive pricing.** A developer does not bill 250 days. Between sales support, internal work, admin, rework, and gaps between projects, 60–70% is the honest figure for a small agency; new agencies often run below 50%. If you price assuming 100% billability, you have quietly discounted yourself by 30–40% before the first negotiation. **Use 60% until Code Square has 12 months of real timesheet data.**

**Step 3 — the floor**

```
Direct cost per billable day     = A ÷ B
Overhead-loaded cost per day     = (A ÷ B) × (1 + overhead %)
                                   overhead % = non-delivery costs
                                   (founder time, sales, marketing,
                                   accounting, unbilled admin)
                                   ÷ total delivery cost      = TBD

COST FLOOR DAY RATE = overhead-loaded cost per day
                    ÷ (1 − target gross margin)

Target gross margin for a services business: 40–55% proposed
Below 30% there is no capacity to invest, hire, or survive a bad quarter.
```

**Every one of A, B, overhead %, and target margin is `TBD — founder must set`.** Until they exist, Code Square is not pricing — it is guessing. This is decision #1 in `[[Open Questions and Decisions Needed]]`.

### 2.2 The founder's own time is not free

The most common small-agency accounting error. The founder's hours on sales, Diagnostics, Blueprints, project management, and client management are a **real cost** and must sit in the overhead figure. Excluding them makes every project look profitable and makes the company's actual cash position inexplicable.

**Diagnostic Sessions are a marketing cost, not free.** At 20 sessions a month, the founder is spending 15+ hours plus write-up time. That belongs in the customer-acquisition-cost line and it is why §3 of `[[Offer Ladder]]` puts a hard 45-minute stop on the session.

### 2.3 The floor is a floor

No project is priced below the cost floor. Not for a logo, not for a "foot in the door", not for a promised second project. The second project arrives at the same discounted price or does not arrive. **The only acceptable below-floor exception** is a deliberate, capped, written-down investment — see §10.3.

---

## 3. The value ceiling — what the work is worth to the client

Cost sets what Code Square can afford to charge. **Value sets what the client can afford to pay.** They are unrelated numbers, and the ceiling is usually far above the floor.

### 3.1 The calculation

`[[Offer Ladder]]` §3 question block C exists to produce these inputs. Ask them and write down the answers.

```
Annual value to the client =
      hours saved per week × 52 × the loaded cost of that person's hour
    + errors avoided per year × cost per error
    + revenue enabled (faster quotes, more bookings, less leakage)
    + cost removed (licences retired, headcount not hired, paper eliminated)
    − the client's ongoing running costs of the new system
```

**Worked structure** — using segment A (maritime/logistics), the beachhead. All inputs are illustrative placeholders, not Code Square or client facts:

| Input | Placeholder |
|---|---|
| Clerks doing manual crew paperwork | `{{n}}` |
| Hours per week each on re-typing | `{{h}}` |
| Loaded cost per hour | `{{c}} EGP` |
| Annual labour value released | `n × h × 52 × c` |
| Placements lost per year to slow/incorrect paperwork | `{{p}}` |
| Margin per placement | `{{m}}` |
| Annual revenue value | `p × m` |
| **Total annual value** | sum |

### 3.2 The value capture ratio

Code Square charges a **fraction** of the value created — the client must clearly win, or the deal has no second year.

| Market situation | Capture as % of first-year value created | Where Code Square sits |
|---|---|---|
| New market, no real alternative | 30–50% | Segment C (healthcare) — founder's domain, no local competitor with the fluency |
| Differentiated, credible proof | 25–40% | **Segment A (maritime) — this is the target zone.** Osama Sakr is a direct reference |
| Competitive market | 10–25% | Segment B (education), general web work |
| Commodity | 5–15% | Marketing websites — **do not compete here** |

**Rule of thumb:** if the system pays for itself in under 12 months of the value it creates, most B2B buyers say yes. Under 6 months and you have almost certainly priced below the ceiling.

### 3.3 Say the value out loud

Value pricing only works if the client *sees* the value. Every proposal states, in the client's own numbers from the Diagnostic:

> "Your team currently spends {{x}} hours a week on {{task}}. At {{rate}}, that is {{annual}} EGP a year. This system removes most of it in {{months}} months."

Charging value-based prices while presenting a feature list is how a strong price loses to a weak one. See `[[Proposal and SOW Template]]` §2.

---

## 4. Market reference band — external benchmarks only

> 🔴 **Everything in this section is `researched` external market data about *other companies*. None of it is Code Square's price, cost, or rate. It is a sanity check on where the floor and ceiling fall relative to the market, and nothing else.**

### 4.1 Agency day/hour rates, Egypt

| Benchmark | Figure | Source | Retrieved |
|---|---|---|---|
| Established Egyptian agency, blended | $20–35 /hr | [matrixmindsit.com](https://www.matrixmindsit.com/en/blog/software-development-rates-egypt-2026) | 2026-09-02 |
| Junior developer | $15–20 /hr | same | 2026-09-02 |
| Senior engineer | $40–50 /hr | same | 2026-09-02 |
| Egypt offshore range | $20–35 /hr | [thescalers.com](https://thescalers.com/offshore-software-development-rates-by-country/) | 2026-09-02 |
| Egypt blended agency pricing | $25–35 /hr | [aalpha.net](https://www.aalpha.net/articles/offshore-software-development-hourly-rates/) | 2026-09-02 |
| Africa region, all outsourcing | $25–65 /hr | [upstackstudio.com](https://upstackstudio.com/blog/offshore-software-development-rate-by-country/) | 2026-09-02 |

### 4.2 Gulf rates — the strategic point

Code Square already lists **Jeddah and Riyadh** as service areas (`[[2026-09-02 - Facebook Page Evidence]]`).

| Benchmark | Figure | Source | Retrieved |
|---|---|---|---|
| Saudi/UAE, offshore vendor rates | $25–49 /hr | [apptunix.com](https://www.apptunix.com/blog/offshore-software-development-rates/) | 2026-09-02 |
| Saudi Arabia, higher-end vendor rates | $55–95 /hr | [aalpha.net](https://www.aalpha.net/articles/offshore-software-development-hourly-rates/) | 2026-09-02 |
| Saudi Arabia, **established local agency** | SAR 350–600+ /hr | [neologix.sa](https://neologix.sa/blogs/software-development-cost-saudi-arabia/) | 2026-09-02 |
| Saudi Arabia, offshore/nearshore teams | SAR 83–150 /hr | same | 2026-09-02 |
| UAE, offshore | $60–100 /hr | [apptunix.ae](https://www.apptunix.ae/blog/software-development-cost-in-uae-vs-saudi-arabia/) | 2026-09-02 |
| Middle East & Africa, full spread | $20–120+ /hr | [fixnhour.com](https://fixnhour.com/blog/it-outsourcing-rates-by-country) | 2026-09-02 |

**The strategic implication `proposed`:** the *same work*, delivered by the *same team*, sells into Riyadh or Jeddah at a materially higher rate than into Port Said. That gap is the single largest available margin improvement in the company and it requires no new capability — only English/MSA collateral, a Gulf-credible web presence, and a channel. `[[Foundation Brief]]` §9 Priority 0 (TLS, SSR, meta) is the precondition: no Gulf enterprise buyer proceeds past a browser security warning.

**Caveats on all of the above.** These are self-published vendor marketing numbers, not audited surveys. Ranges are wide, definitions of "blended" vary, and none of them describe the Port Said local market — where budgets are lower and the competition is freelancers and template shops. Use them as a compass, not a map. **Code Square's own actual observed competitor quotes, once collected, override every row here.** Collecting them is a task in `[[Open Questions and Decisions Needed]]`.

### 4.3 What to actually collect

Market data Code Square owns beats anything in §4.1–4.2:
- Every quote a prospect mentions they received elsewhere — record vendor, scope, and number.
- Every lost deal: the winning price and *why* (price is often the stated reason and rarely the real one).
- Every won deal: what the client said about the price.
- Competitor published pricing where it exists.

Six months of that is worth more than every URL above.

---

## 5. Pricing models — which one, when, and what it risks

### 5.1 The five models

| Model | How it works | Best for | **Risk to Code Square** | Risk to client |
|---|---|---|---|---|
| **Fixed price** | One agreed total for one agreed scope | Well-defined work after a Blueprint: V1 builds, design sprints, the Blueprint itself | **High.** Every hour of overrun comes out of Code Square's margin. Requires disciplined scope control and a real change-request process (§8) | Low. Certainty |
| **Time & materials (T&M)** | Bill actual days at a day rate | Genuinely unknowable scope: integrations, R&D, exploratory AI, inherited systems | **Low** for Code Square | **High.** No ceiling. Clients resist it, and they are not wrong to |
| **Retainer** | Fixed monthly fee for ongoing capacity and support | Post-launch, long relationships, the Outsourced CTO position | **Low–medium.** Predictable revenue; risk is scope creep inside the retainer | Low |
| **Equity / revenue share** | Payment partly or wholly in ownership or a cut of revenue | Almost nothing, at this stage | **Very high.** See §5.3 | Low — it is cheap for them, which is precisely the problem |
| **Hybrid** | Fixed for the defined part, T&M for the unknown part, retainer after | **Most real projects** | Medium, and *managed* | Medium — and explainable |

### 5.2 Hybrid is the default answer

Almost every real engagement has a knowable part and an unknowable part. Pricing both the same way means either Code Square eats the risk (all fixed) or the client does (all T&M). Split it:

```
Blueprint            → FIXED (small, bounded, credited)
V1 core build        → FIXED (scope is now known — that is what the Blueprint bought)
Third-party
  integrations       → T&M, or fixed only after a paid feasibility week
Post-launch          → RETAINER
New features later   → FIXED per change request, or drawn from retainer hours
```

This is defensible to a client in one sentence: *"We fix the price on what we can define, and we bill honestly for what neither of us can define yet — instead of padding the whole number to cover the unknown."*

### 5.3 Equity and revenue share — the standing answer is no

A founder with no cash will offer equity. It is flattering and it is usually a trap.

| Why it is dangerous | |
|---|---|
| Cash-flow mismatch | Salaries are paid monthly in cash; equity pays in years, or never |
| Valuation asymmetry | The client values their idea at millions; the market usually values it at zero |
| Prioritisation | Equity clients demand paying-client attention while paying nothing |
| Dilution and control | Multiple equity deals fragment attention and create governance chaos |
| Positioning damage | An agency that takes equity is signalling it cannot fill its calendar with cash work |

**Rule `proposed`:** default no. Consider **only** if *all* of: (a) the cash portion covers the full cost floor with zero margin, so equity is upside and never subsidy; (b) the client has an operating business with existing revenue, not just an idea; (c) Code Square has spare, genuinely idle capacity; (d) a lawyer papers it; (e) the position is capped so this never exceeds `TBD`% of annual capacity.

**Revenue share** is the better version of the same instinct: cost floor covered in cash, plus a percentage of revenue the system generates, capped at a multiple of the fixed price. Consider it only where revenue is directly attributable and measurable in a system Code Square built.

### 5.4 Recommended default model per service line

| Service (`[[Service Catalog]]`) | Default model | Why |
|---|---|---|
| 1 — Mobile Applications | Fixed, **after a Blueprint** | Scope is definable; store submission is the only wildcard |
| 2 — Web & Platform | Fixed, **after a Blueprint** | The core business. Best-understood work |
| 3 — Custom SaaS | **Hybrid, phased.** Fixed per phase, re-quoted between phases | Too large and too uncertain to fix in one number. Never one lump |
| 4 — AI & Automation | Automation: **fixed** (small, provable). AI/RAG: **T&M or fixed pilot then re-quote** | AI output quality cannot be guaranteed in advance; do not fixed-price an unknown accuracy target |
| 5 — UI/UX Design | **Fixed, per screen count** | Screen count is a clean, defensible unit |
| 6 — System Integration (IoT) | **T&M**, or fixed only after a paid feasibility week | Highest-risk line in the catalog. The dependency is a third party Code Square does not control |
| 7 — Support & Maintenance | **Retainer** | The whole point |

### 5.5 The three rungs

| Rung (`[[Offer Ladder]]`) | Model | Price |
|---|---|---|
| جلسة تشخيص / Diagnostic | Free — a marketing cost, budgeted as one | Free |
| خريطة المشروع / Blueprint | Fixed, 100% up front | `TBD — founder must set` |
| البناء والتشغيل / Build & Run | Fixed V1 → retainer | `TBD — founder must set` |

### 5.6 Setting the Blueprint price — the framework

The Blueprint price is the single most leveraged number in the company: it gates the whole funnel. Four constraints:

| Constraint | Test |
|---|---|
| **Floor** | ≥ (Blueprint days × cost-floor day rate). It is 1–2 weeks of 1–2 people plus founder time — cost it honestly |
| **Ceiling** | Low enough that a qualified buyer approves it without a committee, a board, or a procurement process. It must feel like a decision, not a purchase |
| **Ratio** | `proposed` **5–12% of the expected build price.** Below 5% it does not cover the work; above 15% it becomes a second buying decision and the funnel stalls |
| **Signal** | Not so cheap it reads as worthless. A free-feeling price attracts unqualified buyers, which is the exact problem the rung exists to solve |

`TBD — founder must set`, using the four constraints above.

### 5.7 The credit mechanic — how "credited against the build" works

The Blueprint fee is **100% credited against the build**, subject to written rules. Without rules it becomes a permanent discount.

| Rule | Position `proposed` |
|---|---|
| Credit amount | **100%** of the Blueprint fee |
| Applied to | The **first invoice** of the build (the deposit), not spread across milestones — the client feels it immediately |
| **Validity window** | Build must start within **60 days** of Blueprint delivery. After that the credit lapses, because the analysis has aged and re-work is real |
| Minimum build size | Credit applies only to builds at or above `TBD — founder must set`. Otherwise a tiny build is delivered essentially free |
| Transferable? | **No.** Same client, same project |
| Stackable with discounts? | **No.** The credit *is* the concession. See §10.1 |
| If the client walks away | They keep the document. No refund. That is the deal, and it must be stated in the SOW |
| If Code Square declines the build | **Full refund of the Blueprint fee.** If Code Square concludes it cannot or should not build it, it does not keep the money |

**The margin trap to watch.** The Blueprint is credited, so **the build quote must be priced as if the Blueprint had been free.** If the founder mentally discounts the build because "they already paid for the Blueprint," Code Square delivers 1–2 weeks of senior work for nothing. **The build price is derived from build scope only.** Say it in the proposal: "Build: {{X}}. Less Blueprint credit: −{{Y}}. Total: {{X−Y}}." The client sees the concession; the price integrity survives.

---

## 6. Retainer tiers — structure

Recurring revenue is the strategic prize (`[[Service Catalog]]` §8). The structure, not the prices:

### 6.1 Three tiers

| | **أساسي / Essential** | **نشط / Active** | **شريك تقني / Partner (Outsourced CTO)** |
|---|---|---|---|
| Promise | Keep it alive and safe | Keep it alive and keep improving it | Your technology function |
| Monthly price | `TBD` | `TBD` | `TBD` |
| Uptime monitoring | ✅ | ✅ | ✅ |
| Security patching | ✅ | ✅ | ✅ |
| Backup verification | Monthly | Weekly | Weekly + restore test |
| Defect fixes | ✅ | ✅ | ✅ |
| **Included change hours** | Minimal (`TBD`) | Meaningful (`TBD`) | Substantial (`TBD`) |
| Response target | S1 `TBD` | Faster | Fastest |
| Support hours | Business hours | Business hours | Extended `TBD` |
| Monthly report | ✅ | ✅ | ✅ |
| Roadmap review | Annual | Quarterly | **Monthly** |
| Named engineer | ❌ | ❌ | ✅ |
| Priority in the build queue | ❌ | ✅ | ✅ |
| Discount on new projects | ❌ | `TBD`% | `TBD`% |

### 6.2 Design rules for the tiers

| Rule | Why |
|---|---|
| **Included hours do not roll over** | Rollover creates an unfunded liability — a client banking 6 months of hours then demanding them in one week. State "use it or lose it" plainly at signature |
| **Price the tiers on capacity, not on cost of incidents** | The client is buying reserved availability. That reservation has a cost whether or not they use it |
| **Essential must still clear the cost floor** | A retainer priced below the cost of monitoring and patching it is a monthly donation |
| **Partner tier is the positioning tier** | This is where "Outsourced CTO" (website differentiator #7) is *delivered*. Price it like a fractional executive, not like hosting support |
| **Anchor with three, sell the middle** | Essential exists partly to make Active look correct. This is deliberate choice architecture, and it is honest as long as all three tiers are genuinely deliverable |
| **Annual prepay discount** | `TBD`% — recommend 8–12%. Buys cash certainty and cuts churn |
| **Minimum term 3 months, 30 days' notice** | Prevents the one-month emergency subscription |
| **Annual escalation clause** | `TBD`% or CPI-linked. **Non-optional in Egypt** — see §9. Without it, inflation silently converts a good retainer into a loss over 24 months |

### 6.3 Overage

Hours beyond the tier are billed at the **standard day rate with no retainer discount**, or the client upgrades tier. Never absorb overage silently — a retainer that quietly delivers 3× its hours has become the least profitable work in the company while looking like the most stable.

---

## 7. Payment terms, milestones, and deposits

Cash flow kills more small agencies than bad pricing. A profitable project paid 90 days late can still bankrupt the company.

### 7.1 Standard schedule `proposed`

| Engagement | Schedule |
|---|---|
| **Diagnostic** | Free |
| **Blueprint** | **100% before start** |
| **Fixed-price build** | **Deposit `TBD`% (recommend 40–50%) before any work** → milestone payments against signed acceptance → final `TBD`% (recommend 10–20%) on acceptance |
| **T&M** | Monthly in arrears, net `TBD` days (recommend 14). Advance against an escrow/float for new clients |
| **Retainer** | **Monthly in advance**, standing order or auto-debit |
| **Change requests** | Per the CR, following the parent project's terms |

### 7.2 Deposit policy — non-negotiable

| Rule | Position |
|---|---|
| **No work begins before the deposit clears.** Not "the PO is approved," not "it is with accounts." Cleared funds | A deposit is the only real evidence of commitment |
| Deposit is **non-refundable** once work starts | It covers scheduling, team allocation, and the work already done |
| Existing clients in good standing | May reduce to `TBD`% at the founder's discretion, in writing |
| **New clients: never waive** | The prospect most insistent on waiving the deposit is the one most likely to not pay at all. Treat the request as a qualification signal |

### 7.3 Milestones

Each milestone must be **binary** — demonstrable, acceptance-tested, and signed. Never "50% complete"; percentage complete is an opinion and it is always 90% for the last third of a project.

| Rule | Why |
|---|---|
| Tie every milestone to a **demo of working software** | The only honest progress signal |
| No milestone larger than `TBD`% of the total (recommend ≤ 25%) | Limits exposure if the client stops paying |
| Milestones no more than 4 weeks apart | Longer gaps mean lending the client money |
| **Final payment ≤ 20%** | A large final payment becomes the client's negotiating lever at the worst possible moment |

### 7.4 Late payment

| Term | Position `proposed` |
|---|---|
| Payment terms | Net `TBD` days (recommend 14 for SMEs) |
| Reminder cadence | Day 1 after due, day 7, day 14 |
| Late fee | `TBD`% per month, stated in the SOW. Charge it or remove the clause; an unenforced clause teaches the client the deadline is decorative |
| **Work stops** at `TBD` days overdue (recommend 15) | Written notice first. Stated in the SOW so it is never a surprise |
| Retainer suspension | At `TBD` days overdue — **but never stop security patching or backups without written notice.** Never hold a client's live system hostage; it is unethical, it is reputationally fatal in a small city, and it may be unlawful |
| **IP transfers on final payment only** | The strongest, cleanest lever available. §12 |

---

## 8. Scope change and change requests

**Scope creep is the largest single source of margin loss in a fixed-price agency**, and it is almost never one big request. It is fifteen small ones, each individually too small to argue about.

### 8.1 The process

```
Client requests something not in the signed scope
        ↓
Say: "Good idea — that's outside the current scope.
      I'll send you a change request today."     ← NEVER "sure, no problem"
        ↓
Written CR: what, why, effort in days, price,
            schedule impact, expiry
        ↓
Client signs                              Client declines
        ↓                                         ↓
Added to scope. Timeline formally moves.  Logged to the V2 backlog.
Invoiced per terms.                       Original scope proceeds unchanged.
```

### 8.2 Rules

| Rule | Why |
|---|---|
| **Every change is written. No verbal scope. Ever.** | The single highest-value discipline in the whole document |
| **"That's a great idea for V2"** is the standard response | Preserves the relationship *and* the margin. Neither a no nor a free yes |
| A CR states **schedule impact**, not only price | Clients accept cost far more readily than delay; hiding the delay guarantees a fight later |
| **Small changes are still changes** | Track and *show* them. "We've absorbed 6 small requests, roughly 4 days. Here's CR-007 for the rest." Visible generosity is worth something; invisible generosity is worth nothing |
| **Absorbed-change budget** | Allow `TBD` days of goodwill per project (recommend ≤ 3% of project days). Log every one. When exhausted, everything is a CR |
| CRs are priced at **standard rates**, no project discount | The discount bought the original scope |
| CRs **expire** in 14 days | Prevents a client banking approvals and springing them late |
| A CR that pushes the project past `TBD`% of original scope | Triggers a **full re-plan and re-quote**, not another CR. Death by a thousand CRs is still death |

### 8.3 The client-caused-delay clause

| Trigger | Consequence |
|---|---|
| Client misses the 3-working-day feedback SLA | Timeline moves day for day. **Notify in writing the day it happens**, not at the end |
| Delay exceeds `TBD` days (recommend 15) cumulative | Project may be paused; **re-mobilisation fee** of `TBD` applies |
| Third-party access not provided by the agreed date | Same treatment |

Without this clause, a client who takes three weeks on every review still expects the original delivery date, and Code Square absorbs the cost of a delay it did not cause. `[[Scoping and Estimation Guide]]` trap #4.

---

## 9. Currency — EGP vs USD/SAR, and who carries the risk

Code Square sells in **Egypt** (EGP) and lists **Jeddah and Riyadh** (SAR/USD). This is a pricing decision, not an accounting detail.

### 9.1 The exposure

Egyptian costs are in EGP and the EGP has a documented history of sharp devaluation. Two distinct risks:

| Risk | Effect |
|---|---|
| **Devaluation risk** on a long EGP fixed-price project | A 6-month project quoted in EGP can lose real margin before delivery if the currency moves |
| **Cost inflation risk** | Salaries, cloud (USD-denominated), tools, and equipment all rise. Cloud and SaaS tooling are billed in USD *today* — a devaluation raises Code Square's costs immediately, in EGP |

**The second is the sharper one and it is routinely missed.** A large part of a software agency's cost base is already dollar-denominated even when every client pays in EGP.

### 9.2 Policy `proposed`

| Client | Quote in | Who bears currency risk | Mechanism |
|---|---|---|---|
| Egyptian, project **< 3 months** | **EGP**, fixed | Code Square | Short enough to absorb. Quote validity **30 days** |
| Egyptian, project **> 3 months** | **EGP** with an **FX adjustment clause** | Shared | If USD/EGP moves more than `TBD`% (recommend 10%) between signature and a milestone, the remaining milestones are adjusted by the excess. **Symmetric — it must cut both ways, or it is not a fair clause and clients will refuse it** |
| Egyptian, USD-denominated costs | Pass through **at cost**, billed in USD or at the day's rate | Client | Cloud, licences, API fees are the client's accounts anyway (`[[Service Catalog]]` §9) |
| **Gulf (KSA/UAE)** | **USD or SAR** | Client | Never quote a Gulf client in EGP. It reads as low-cost-vendor positioning and it hands Code Square the entire currency exposure for free |
| Retainers, all currencies | **Annual escalation clause**, `TBD`% or CPI-linked | Shared | Mandatory in Egypt. §6.2 |

### 9.3 The strategic move

Per §4.2, the same work sells for materially more in SAR/USD than in EGP. **Every USD or SAR contract is simultaneously a higher price and a natural hedge against the company's dollar-denominated cost base.**

**Recommendation `proposed`:** set an explicit target for hard-currency revenue as a share of total — `TBD`%, recommend building toward 30%+ within 18 months. That single target does more for the company's financial resilience than any pricing tactic in this document. It requires: TLS fixed, SSR shipped, English/MSA collateral, Gulf-credible case studies, and a Gulf channel. `[[Foundation Brief]]` §9.

### 9.4 Practical rules

- **Quote validity: 30 days.** Not 90. State it on every proposal.
- Bank charges and transfer fees: **client's cost**, stated in the SOW.
- International wires: confirm which side absorbs correspondent-bank fees (they are real and they surprise people).
- Never accept payment in a currency Code Square cannot receive without loss.
- Record the exchange rate used, and its date, on every cross-currency quote.

---

## 10. Discount policy and when to walk away

### 10.1 The governance table `proposed`

| Discount | Approval | Acceptable justification |
|---|---|---|
| **0%** | — | **The default. Most deals should close here.** |
| 1–10% | Founder | Full prepayment, multi-project commitment signed at the same time, or a flagship reference client with **written** case-study and metric rights |
| 10–20% | Founder, written justification filed | A genuine strategic account: opens the beachhead segment, or is the first paid healthcare pilot creating the missing reference (`[[Foundation Brief]]` §7.3) |
| **>20%** | **Do not.** Restructure the scope instead | There is no justification. If the price is 20%+ too high for this client, the *scope* is wrong, not the price |

**Every discount must have:** a written reason, an expiry date, a named condition it is contingent on (and it is withdrawn if the condition fails), and a record in `[[Lead Intake and CRM]]`. **A discount granted with no expiry becomes the price.**

### 10.2 Give these before giving price

Ranked by cost to Code Square. Exhaust the list before touching the number.

| Concession | Cost to Code Square |
|---|---|
| Extended payment terms / more milestones | Cash-flow only. **Try this first — it is what most "price" objections actually are** |
| Reduce scope to fit the budget (phase it) | **Zero. This is the correct answer to almost every price objection** |
| Extra retainer months at the same rate | Low, and it deepens the relationship |
| Additional training or onboarding sessions | Low |
| A free small add-on with a named value | Low, and it preserves the headline price |
| Faster start date | Zero, if capacity exists |
| Referral or case-study credit | Zero, and it is genuinely valuable |
| **Cutting the price** | **Direct margin. Last resort, never first.** |

> **The scope answer, in one sentence:** *"I can't reduce the price for this scope — but I can absolutely build you a smaller first version that fits your budget, and we add the rest once it's earning."* This keeps the price integrity, keeps the client, and produces a better project. It is also exactly the MVP argument Code Square already publishes on Facebook.

### 10.3 The one below-floor exception

A below-floor price is permitted **only** as a written, capped investment — for example the first healthcare pilot needed to create a reference that does not yet exist (`[[Foundation Brief]]` §7.3). Conditions, all mandatory:
- The gap is recorded as a **marketing cost**, not disguised as a profitable project.
- The client signs case-study rights, named-logo rights, a filmed testimonial, and **the metrics**.
- The discount is explicitly one-time, stated in the SOW, with the standard price named beside it.
- **A hard cap:** no more than `TBD` such engagements per year (recommend 1–2). Beyond that it is not a strategy, it is a habit.

### 10.4 When to walk away

Walking away is a pricing decision. These are the signals — any two together should end the conversation.

| Signal | What it predicts |
|---|---|
| Refuses a deposit | Will not pay at the end either |
| Refuses to pay for the Blueprint but wants a fixed quote | Wants free analysis |
| "This is simple, it should be cheap" | Has not understood the work and will dispute every hour |
| Fixed price + open scope, and will not move on either | A guaranteed loss. The only two ways to lose are both present |
| Demands >20% off before negotiating scope | Buying on price alone; will leave for anyone 10% cheaper |
| "There's much more work after this" as the reason for a low price | The mythical second project. It arrives at the discounted price or not at all |
| No identifiable decision-maker | Endless approval loops, unpaid |
| Burned a previous agency and blames them entirely | Sometimes true. Often the pattern repeats. Ask hard questions |
| Wants to own Code Square's internal tools and libraries | Misunderstands what is being bought. See §12 |
| Asks for work to start before contract or deposit | Boundary test on day one |
| The project is outside the `[[Service Catalog]]` | Refer it out. Referrals return |
| A gut feeling that this will be painful | **Trust it.** It is pattern recognition, and it is usually right |

> **The best deals a small agency makes are the ones it does not make.** One bad client consumes the capacity of three good ones, and the loss never appears in a report — it appears as a year with lots of work and no money.

---

## 11. 🔴 The $19 / $49 / $99 warning

**The SaaS service infographic posted on Facebook contains a mockup screenshot showing subscription tiers priced at $19, $49, and $99 per month.**

| Fact | |
|---|---|
| What it is | **Placeholder art inside a fake product screenshot**, used to illustrate that Code Square builds subscription systems |
| What it is not | Code Square's prices. A client's prices. A benchmark. A starting point. Anything at all |
| Evidence | `[[2026-09-02 - Facebook Page Evidence]]`, service pillar 3: *"Mockup showed sample tiers $19 / $49 / $99 per month — **this is placeholder art, NOT Code Square's real pricing.** Do not treat as a price list."* |
| Confirmed by | `[[Foundation Brief]]` §6: *"The `$19/$49/$99` on the SaaS infographic is mockup art and must never be quoted."* |

**Rules:**
1. **Never quote these numbers to anyone, in any currency, in any context.**
2. Never paste that infographic into a proposal, a deck, or a WhatsApp reply to a pricing question.
3. If a prospect references them — *"I saw your prices are $19 a month"* — correct it immediately and warmly: **"That's a design mockup showing the kind of subscription system we build for clients, not our own pricing. Let's talk about what you actually need and I'll give you a real number."**
4. **Action required:** either add a visible "mockup / نموذج توضيحي" watermark to the creative, or retire it. Today it is an unpriced, uncontrolled price signal published by the company to the public. Tracked in `[[Open Questions and Decisions Needed]]`.

**Why this matters more than it looks.** A published number, even a fake one, anchors every negotiation that follows. A prospect who has seen "$19/month" will experience any real quote as expensive, regardless of value. Anchoring is the strongest effect in pricing psychology and this one is currently working against the company for free.

**Related unknown:** the website's contact form has a **budget dropdown whose bands were not recoverable from the code** (`[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`). Those bands are also a published price signal, and nobody currently knows what they say. **Check them.** If the lowest band is very low, it is filtering *for* the wrong buyer.

---

## 12. IP, data, and payment — the commercial link

| Position `proposed` | |
|---|---|
| **Custom code and deliverables** | Transfer to the client **on receipt of final payment**. Not on delivery, not on acceptance — on payment |
| **Code Square's pre-existing tools, libraries, and internal frameworks** | Remain Code Square's, licensed to the client perpetually, non-exclusively, for use within the delivered system. **Never sell these outright.** They are the reason project #5 is faster than project #1, and selling them sells the company's compounding advantage |
| **Client data** | The client's, always. Exportable in a standard format on request, at no charge, at any time |
| **Third-party components** | Under their own licences, disclosed in the SOW |
| **Portfolio rights** | Code Square may name and show the work unless the client opts out **in the SOW** (`[[Service Catalog]]` §9) |
| **Metrics** | The client agrees at signature to share before/after numbers for a case study. A deliverable, not a favour |

Full clause wording in `[[Proposal and SOW Template]]` §10.

---

## 13. What the founder must decide — the blocking list

Nothing in this vault's commercial layer can execute until these exist. In order:

| # | Decision | Blocks | §  |
|---|---|---|---|
| 1 | **Fully-loaded cost per delivery day** (A, B, overhead %, target margin) | **Everything.** No floor = no pricing | §2 |
| 2 | Standard day rate | Every quote, T&M, CR, overage | §2 |
| 3 | Blueprint price | The entire funnel (`[[Offer Ladder]]` rung 2) | §5.6 |
| 4 | Minimum project size | Which leads to accept at all | §5.7 |
| 5 | Three retainer prices + included hours | 80% attach target | §6 |
| 6 | Deposit % and payment terms | Cash flow | §7 |
| 7 | FX threshold and escalation % | Long projects, all retainers | §9 |
| 8 | Discount ceiling and approver | Margin discipline | §10 |
| 9 | Whether the $19/$49/$99 creative is watermarked or retired | Live public price signal | §11 |
| 10 | What the website budget dropdown bands actually say | Live public price signal | §11 |

All ten go to `[[Open Questions and Decisions Needed]]`.

---

## 14. Review cadence

Pricing is never finished.

| Cadence | Review |
|---|---|
| **Every project** | Actual days vs estimate. Feed into `[[Scoping and Estimation Guide]]` |
| **Monthly** | Realised margin per project. Discount depth granted. Absorbed (unbilled) change days |
| **Quarterly** | Win rate by price band. Retainer churn. Overage patterns. Competitor quotes observed |
| **Annually** | Rebuild the cost floor from actual costs. Apply retainer escalation. Reprice the catalog |
| **On trigger** | EGP moves >10% · a key cost rises sharply · win rate exceeds 80% (**priced too low**) or falls below 25% (priced wrong, or targeting wrong) |

> **A win rate above 80% is not good news.** It means the price is below what the market would have paid. A healthy fixed-price agency wins somewhere around 40–60% of qualified proposals. Losing deals on price sometimes is the evidence that the price is right.

---

## Related

[[Foundation Brief]] · [[Service Catalog]] · [[Offer Ladder]] · [[Proposal and SOW Template]] · [[Scoping and Estimation Guide]] · [[ICP - Ideal Customer Profiles]] · [[Sales Playbook]] · [[Delivery Process]] · [[Lead Intake and CRM]] · [[Open Questions and Decisions Needed]] · [[2026-09-02 - Facebook Page Evidence]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]
