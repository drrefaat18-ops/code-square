---
date: 2026-09-02
type: operations
tags:
  - operations
  - kpi
  - metrics
  - code-square
ai-first: true
status: draft
owner: TBD
---

# KPI Dashboard

## For future Claude

The measurement system: what gets counted, how it is calculated, where the number comes from, who owns it, how often it is reviewed, and the target — which is `TBD — set after 90 days of baseline` for almost everything, because **Code Square has no measured baseline for anything except its Facebook engagement, and that baseline is 74 followers and 1–4 reactions a post** (`stated`).

**KPI** = key performance indicator: a number that tells you whether something is working, chosen in advance so you cannot pick a flattering one afterwards.

All `proposed` (2026-09-02). All owners are **functions** — roster unknown, see `[[Org and Roles]]`.

> **The rule that makes this file work: no target is invented today.** Measure for 90 days, then set a target from the real number. A target pulled out of the air is worse than no target — it is either trivially met or permanently missed, and either way it is ignored.

---

## 1. North-star metric

**One number that, if it goes up, means the company is genuinely healthier.**

> ### North star: **monthly recurring revenue (MRR) from retainers**
> The total of all monthly support and maintenance fees currently being paid.

**Why this one.** `[[Foundation Brief]]` §3 positions Code Square as an **Outsourced CTO** — the claim that a freelancer and a template shop cannot make. That claim is only true if clients stay. Retainer revenue is the number that proves it, and it is the one revenue type that does not reset to zero when a project ends. Project revenue is lumpy and hides the truth; MRR does not.

**Current value:** `TBD — measure`. It may well be zero today, and that is a legitimate starting point.

**Secondary north star while MRR is near zero: qualified enquiries per month.** At 74 followers and no conversion path, the immediate constraint is demand, not retention.

---

## 2. Marketing

| Metric | Definition | Formula | Source | Owner | Cadence | Target |
|---|---|---|---|---|---|---|
| **Reach** | People who saw our content | Platform figure | Facebook insights | Marketing — TBD | Weekly | `TBD — set after 90 days of baseline` |
| **Website sessions** | Visits to the site | Analytics figure | Google Analytics | Marketing — TBD | Weekly | `TBD` |
| **Qualified enquiries** | Enquiries from someone with a real project, a budget, and authority to proceed | Count | CRM sheet | Marketing — TBD | Weekly | `TBD` |
| **Enquiry rate** | Share of visitors who enquire | Enquiries ÷ sessions × 100 | Analytics + CRM | Marketing — TBD | Monthly | `TBD` |
| **Cost per qualified enquiry** | What one real enquiry costs us | Total marketing spend ÷ qualified enquiries | Finance + CRM | Marketing — TBD | Monthly | `TBD` |
| **Enquiries by source** | Which channel produced them | Count by source | CRM sheet | Marketing — TBD | Monthly | Know it, do not target it |

**Note on cost per qualified enquiry:** this is the number that decides whether to spend on ads. `[[Foundation Brief]]` §9 is explicit that no spend happens until the site is fixed — a broken TLS certificate and an uncrawlable site make every pound of ad spend a donation.

---

## 3. Sales

| Metric | Definition | Formula | Source | Owner | Cadence | Target |
|---|---|---|---|---|---|---|
| **First-response time** | How long until a human replies to an enquiry | Average hours from receipt to reply | CRM sheet | Sales — TBD | Weekly | **Under 24 hours** — the website already promises this (`stated`); it is the only target here that is already publicly committed |
| **Diagnostic sessions booked** | Free diagnostic sessions scheduled | Count | Calendar / CRM | Sales — TBD | Weekly | `TBD` |
| **Enquiry → session rate** | Share of enquiries that become a session | Sessions ÷ qualified enquiries × 100 | CRM | Sales — TBD | Monthly | `TBD` |
| **Proposals sent** | Count | Count | CRM | Sales — TBD | Monthly | `TBD` |
| **Win rate** | Share of proposals that become signed projects | Won ÷ (won + lost) × 100 | CRM | Sales — TBD | Monthly | `TBD`. Above ~70% usually means underpricing, not brilliance |
| **Average deal size** | Typical project value | Total won value ÷ number won | CRM + Finance | Sales — TBD | Monthly | `TBD` |
| **Sales cycle length** | Days from first contact to signed contract | Average of (signed date − first contact date) | CRM | Sales — TBD | Monthly | `TBD` |
| **Loss reasons** | Why we lost | Categorised count | CRM | Sales — TBD | Monthly | Not a target — a list to act on |

---

## 4. Delivery

| Metric | Definition | Formula | Source | Owner | Cadence | Target |
|---|---|---|---|---|---|---|
| **On-time delivery** | Projects launched by the date agreed at Gate B | On-time ÷ delivered × 100 | Project records | Delivery — TBD | Monthly | `TBD` |
| **Schedule variance** | How far off we were | (Actual days − planned days) ÷ planned days × 100 | Project records | Delivery — TBD | Per project | `TBD` |
| **Scope-change rate** | How much scope moved after Gate A | Value of approved change requests ÷ original scope value × 100 | Change log | Delivery — TBD | Per project | Investigate above 20% (`[[Delivery Process]]` §9) |
| **Defect escape rate** | Bugs the client found that we should have caught | Defects reported in the first 30 days ÷ features delivered | Ticket log | QA — TBD | Per project | `TBD` |
| **Estimate accuracy** | Estimated hours vs actual | Actual ÷ estimated | Time records | Delivery — TBD | Per project | `TBD` |
| **Client satisfaction** | One question at the 30-day review: *"How likely are you to recommend us, 0–10?"* | Average | Post-launch review | Account mgmt — TBD | Per project | `TBD` |
| **Case studies published** | Written up and live | Count | Website | Marketing — TBD | Monthly | **1 per delivered project.** Currently 4 real projects, 0 published (`stated`) — this is the vault's single biggest proof gap |

---

## 5. Financial

| Metric | Definition | Formula | Source | Owner | Cadence | Target |
|---|---|---|---|---|---|---|
| **Revenue** | Money invoiced this month | Sum of invoices | Accounting | Finance — TBD | Monthly | `TBD` |
| **MRR (north star)** | Recurring retainer revenue | Sum of active monthly retainers | Accounting | Finance — TBD | Monthly | `TBD` |
| **Recurring share** | How much of revenue is predictable | MRR ÷ total monthly revenue × 100 | Accounting | Finance — TBD | Monthly | `TBD`. Higher is a more stable company |
| **Gross margin** | What is left after the direct cost of delivering | (Revenue − direct delivery cost) ÷ revenue × 100 | Accounting + time records | Finance — TBD | Monthly | `TBD` |
| **Utilisation** | Share of working hours spent on paid client work | Billable hours ÷ available hours × 100 | Time records | Delivery — TBD | Monthly | `TBD`. 100% is a warning sign, not a triumph — it means no time for sales, learning, or the company itself |
| **Cash on hand** | Money in the bank today | Bank balance | Bank | Finance — TBD | **Weekly** | — |
| **Cash runway** | Months of survival at current burn | Cash ÷ average monthly costs | Accounting | Finance — TBD | Monthly | Never below 3 months |
| **Receivables overdue** | Money owed past its due date | Sum of overdue invoices | Accounting | Finance — TBD | Weekly | Zero |

> **Cash on hand and runway are the only two metrics reviewed weekly rather than monthly.** Profitable companies die of cash, not of profit.

---

## 6. Support

| Metric | Definition | Formula | Source | Owner | Cadence | Target |
|---|---|---|---|---|---|---|
| **Ticket volume** | Tickets opened | Count | Ticket system | Support — TBD | Weekly | Not a target — rising volume may mean growth or may mean poor quality; read it with defect escape rate |
| **Tickets by severity** | S1–S4 split | Count by severity | Ticket system | Support — TBD | Weekly | S1 count should trend to zero |
| **SLA compliance — response** | Share answered within target | Met ÷ total × 100 | Ticket system | Support — TBD | Monthly | `TBD — set after 90 days`, then honestly reported |
| **SLA compliance — resolution** | Share resolved within target | Met ÷ total × 100 | Ticket system | Support — TBD | Monthly | `TBD` |
| **Uptime** | Availability of each client system | Monitoring tool figure | UptimeRobot | DevOps — TBD | Monthly | **Do not publish a figure until 90 days are measured** — see `[[Support and Maintenance SLA]]` |
| **Repeat issues** | Same problem recurring | Count of tickets sharing a root cause | Ticket system | Support — TBD | Monthly | Each one gets a permanent fix, not a repeated patch |
| **Retainer retention** | Share of retainers renewed | Renewed ÷ due for renewal × 100 | CRM + Accounting | Account mgmt — TBD | Quarterly | `TBD` |

---

## 7. Vanity metrics — the warning

> **A vanity metric is a number that goes up without the business getting better.**

| Vanity metric | Why it misleads | Measure instead |
|---|---|---|
| **Followers** | 74 followers and zero enquiries is the current position (`stated`). Ten thousand followers who never buy is the same position, louder | Qualified enquiries |
| **Likes and reactions** | Costs the liker nothing and predicts nothing | Enquiries by source |
| **Impressions / reach alone** | Being seen is not being chosen | Enquiry rate from that channel |
| **Number of posts published** | Effort, not outcome. Content output is already high and demand is already zero — more of it changes nothing | Enquiries per published piece |
| **Website hits** | Traffic to a page with no offer converts nobody | Sessions that reach the diagnostic-session booking |
| **Hours worked** | Rewards slowness | Utilisation and margin |
| **Lines of code / features shipped** | Rewards building the wrong thing | Client success metric movement |
| **Revenue with no margin** | A busy company losing money on every project | Gross margin |

**The test:** if the number went up 10× tomorrow, would the company be meaningfully better off? If not, it is a vanity metric. Do not put it on the scorecard, and do not celebrate it.

---

## 8. Weekly one-page scorecard

One page. Reviewed in the weekly reviews (`[[Operating Cadence]]`). If it does not fit on one page, it is not a scorecard.

```
CODE SQUARE — WEEKLY SCORECARD
Week ending: ____________          Prepared by: ____________

MONEY
  Cash on hand                 ________     Runway (months)  ________
  Invoiced this week           ________     Overdue          ________
  MRR (north star)             ________     vs last month    ________

DEMAND
  Qualified enquiries          ____ (last week ____)
  Avg first-response time      ____ hrs   [target: under 24]
  Diagnostic sessions booked   ____
  Proposals out                ____        Value ________
  Won ____   Lost ____   Reason for each loss: ______________________

DELIVERY
  Project            Status        Next milestone   Date    Risk
  _________________  on/at risk/late  ____________  ____    ______
  _________________  on/at risk/late  ____________  ____    ______
  Change requests raised ____   decided ____   pending ____

SUPPORT
  Tickets open ____  S1 ____ S2 ____ S3 ____ S4 ____
  SLA breaches this week ____   Ageing over 7 days ____
  Uptime incidents ____

RENEWALS DUE IN 30 DAYS
  ______________________________________________  Owner ________

TOP 3 RISKS THIS WEEK
  1. ____________________________________  Owner ________
  2. ____________________________________  Owner ________
  3. ____________________________________  Owner ________

THE ONE THING that must happen next week:
  ______________________________________________________________
```

**Rules:** filled in before the meeting, not during it. Blank cells stay blank rather than being guessed — a blank is honest data about what is not being measured. Kept as `08-Operations/Scorecards/YYYY-MM-DD.md`.

---

## 9. Building the baseline — the first 90 days

Nothing in this file works without measurement starting. In order:

- [ ] **Week 1** — start the CRM sheet: every enquiry, its source, and the response time. This alone gives four metrics
- [ ] **Week 1** — uptime monitoring on all Code Square and client sites
- [ ] **Week 1** — Google Analytics and Search Console on the website
- [ ] **Week 2** — a cash sheet: money in, money out, cash on hand, updated weekly
- [ ] **Week 2** — a ticket record, even if it is a sheet
- [ ] **Week 3** — record estimated vs actual hours on the current project
- [ ] **Week 4** — first weekly scorecard, with blanks left blank
- [ ] **Day 90** — the quarterly planning session sets the first real targets, from real numbers

**Until day 90, the honest answer to "how are we doing?" is "we are measuring".** That is a much better answer than a made-up target.

---

## 10. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | Is MRR the right north star, or should it be qualified enquiries until demand exists? | Focus |
| 2 | What is the current cash position and monthly cost base? | Runway, every financial metric |
| 3 | Is anyone recording time worked? | Utilisation, margin, estimate accuracy |
| 4 | What counts as a *qualified* enquiry for Code Square specifically? | The definition underneath half this file |
| 5 | Who owns the scorecard each week? | Whether it ever gets filled in |
| 6 | Where do scorecards live in the vault? | §8 |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Operating Cadence]] · [[Org and Roles]] · [[Tools Stack]] · [[Delivery Process]] · [[Support and Maintenance SLA]] · [[Quality Standards and Handover]] · [[Sales Playbook]] · [[Pricing and Packaging]] · [[Foundation Brief]]
