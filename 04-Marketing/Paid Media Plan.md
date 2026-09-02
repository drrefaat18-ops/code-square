---
date: 2026-09-02
type: paid-media-plan
tags:
  - marketing
  - paid-media
  - meta-ads
  - code-square
ai-first: true
status: draft
owner: TBD
confidence: proposed
---

# Paid Media Plan — Code Square

## For future Claude

**This is a gated plan, not a start-now plan.** Nothing in it executes until the gates in §1 are green. Written 2026-09-02 so that the moment the website is fixed, the team can execute without a planning delay — not so that anyone can start spending this week.

Monthly budget is **`TBD`** (blocker B7, `[[Open Questions and Decisions Needed]]`). The superseded plan proposed 10,000 EGP/month at a 70/30 split; that number is **not adopted** here. §6 gives the allocation *logic* and a worked example at an arbitrary budget `B` so the structure holds at any figure the founder sets.

The one thing that must not be lost in editing: **spend is judged on qualified enquiries, never on clicks, reach, CPM, or followers.** A campaign delivering cheap clicks and no qualified enquiries is a failing campaign, and it must be killed even though the dashboard looks green.

---

## 1. The gates

Paid media does not start until **all** of these are true. Not "mostly true".

### Gate 0 — the website (from `[[Foundation Brief]]` §9, Priority 0)

- [ ] **TLS certificate on `mtechsquare.com` renewed and valid.** Today it is expired (`stated`), so every visitor meets a full-page browser security warning. Sending paid traffic into that is buying strangers a reason to distrust the company.
- [ ] **SSR or prerender live** on `/code-square/`. Today the served HTML is an empty shell (`stated`) — search engines and AI engines see nothing, and slow client-side rendering on Egyptian mobile data means a meaningful share of paid clicks bounce before content appears.
- [ ] `sitemap.xml`, `robots.txt`, `llms.txt` present.
- [ ] Page-level `<title>` and `<meta description>` for Code Square. Today a shared ad link previews as "M Tech Square Group — Beyond Squares" (`stated`) — the ad and the landing page would carry different company names.
- [ ] Contact form verified to deliver, with a **named human** owning the inbox.
- [ ] Mobile load tested on a real 4G connection, not office wifi. The current bundle is ~7.5 MB (`stated`).

### Gate 1 — the funnel (from `[[Foundation Brief]]` §9, Priority 1–3)

- [ ] Four case studies published, at least two carrying a real client number.
- [ ] Diagnostic Session live, named, and bookable via a working link (`[[Offer Ladder]]`).
- [ ] Beachhead confirmed by the founder — ads cannot be targeted before the audience is chosen.
- [ ] Intake + CRM in place (a labelled WhatsApp list or a spreadsheet counts) and a named Responder with hours.
- [ ] Measurement stack live (§4).
- [ ] Organic proof exists that *some* post drove *some* enquiry. Paying to amplify a message that has never once worked organically is paying to find out faster that it does not work.

> **If a founder asks to "just try a small boost" before these are green, the answer is no, and the reason is §2.** A small boost is not a small experiment; it is a small purchase of traffic into a broken door, and it produces a misleading negative result that discourages spending later when it would actually work.

---

## 2. Why the gate is absolute

Trace one paid click today:

ad → click → browser security warning → (most leave) → blank shell while 7.5 MB loads → (more leave) → a page whose title says another company's name → no bookable next step → a WhatsApp number with no greeting and no owner.

Six failure points, none of which more budget fixes. The certificate renewal and the prerender step cost a fraction of one month's media budget and multiply the return on every pound after them. Ads are an amplifier; an amplifier attached to nothing outputs nothing, loudly.

---

## 3. What paid media is actually for here

Not brand awareness. Not followers. At Code Square's size, paid media has exactly three jobs:

1. **Reach the specific local buyer organic cannot reach.** 74 followers means organic reach is effectively zero outside a tiny circle. Meta's geo + interest targeting is the only affordable way to put a case study in front of a port-services owner in Port Said who has never heard of the company.
2. **Retarget the people the case studies already warmed.** Once real traffic exists, the highest-return spend in the account is showing the Diagnostic Session offer to people who already read a case study.
3. **Buy learning speed.** Which pain resonates, which case study converts, which headline gets a reply — organic at this audience size produces too little data to answer that in under a year.

---

## 4. The measurement stack (build this BEFORE spending)

Without this, spend cannot be judged and the plan's core rule — judge on qualified enquiries — is unenforceable.

| # | Item | Why | Owner |
|---|---|---|---|
| 1 | **Meta Pixel installed sitewide** | Builds retargeting audiences and website-custom-audiences. Install it in week 1 even though ads are months away — audiences need time to accumulate | dev |
| 2 | **Conversions API (CAPI)** | Browser-side pixel loses a large share of events to iOS tracking prevention and ad blockers. Server-side CAPI recovers them. Without it, Meta optimises on partial data | dev |
| 3 | **Events defined and firing** | See the event table below | dev + P |
| 4 | **GA4 or Plausible** | Independent check on Meta's self-reported numbers. Never grade a channel solely on its own homework | dev |
| 5 | **UTM convention** | See below. Non-negotiable and enforced | P |
| 6 | **Lead form fallback** | See §4.3 | P |
| 7 | **CRM field: "how did you hear about us"** | The only source of truth that survives every tracking break. Ask it in every Diagnostic Session | F |

### 4.1 Events

| Event | Trigger | Standard/custom |
|---|---|---|
| `PageView` | Any page | Standard |
| `ViewContent` | A case-study page opened | Standard |
| `CaseStudyRead` | 60% scroll or 45s on a case-study page | Custom — the real interest signal |
| `Contact` | WhatsApp link clicked | Standard |
| `Lead` | Contact form submitted, or lead form completed | Standard — **the optimisation event** |
| `Schedule` | Diagnostic Session booked | Standard |
| `QualifiedLead` | Marked qualified in the CRM, sent back to Meta as an offline conversion | Custom — **the real success event** |

`QualifiedLead` is what closes the loop between the ad account and reality. Until offline conversions are uploaded, Meta is optimising for form-fillers, and form-fillers include every "how much for a logo" enquiry.

### 4.2 UTM convention

```
utm_source   = facebook | instagram | linkedin | whatsapp | email | offline
utm_medium   = paid | organic | referral | outreach
utm_campaign = <objective>-<segment>-<yyyymm>     e.g. diagnostic-maritime-202612
utm_content  = <creative-id>                       e.g. osamasakr-number-v1
utm_term     = <audience>                          e.g. geo-portsaid-interest-shipping
```
Lowercase, hyphens, no spaces, no Arabic in UTMs. One typo splits a campaign into two rows in the report and quietly ruins the analysis.

### 4.3 The lead-form fallback

Because the site is the weakest link, the **first campaigns should not depend on it**. Use Meta **Instant Forms** (a form that opens inside Facebook and never leaves the app):

- Removes the landing page from the funnel entirely — no cert, no load time, no bounce.
- Much higher completion rate on mobile in Egypt.
- **Cost:** lead quality drops, because filling a form inside Facebook takes no effort. Counter it with (a) 3–5 qualifying questions, not name/phone alone, (b) an intro screen that states plainly who this is for, (c) a "higher intent" form setting where available.
- **Mandatory:** every lead-form submission gets a WhatsApp message **within 15 minutes**. Instant-form leads go cold faster than any other kind. A lead answered the next morning is usually a lead lost.

Qualifying questions to put on the form:
1. نوع نشاط الشركة؟ (ملاحة/توكيلات · توظيف بحري · شحن وتخليص · تعليم · غير كده)
2. الشغل اللي عايز تظبطه بيتعمل إزاي دلوقتي؟ (إكسيل · ورق · واتساب · نظام موجود)
3. كام واحد هيستخدم النظام؟
4. عايز تبدأ امتى؟

Keep the lead form as the fallback even after the site is fixed — run it as a parallel test against a landing-page campaign and let the *qualified* cost decide, not the raw lead cost.

---

## 5. Campaign structure for a small budget

**The governing constraint:** small budgets fragment badly. Meta's delivery system needs roughly 50 optimisation events per ad set per week to leave the learning phase. At a small budget with a high-value B2B offer, that number is unreachable on `Lead` events, and completely unreachable on `QualifiedLead`.

Three consequences that shape everything below:

1. **Few ad sets.** Two or three at most. Ten ad sets at a small budget means ten ad sets that never learn.
2. **Optimise for the highest-volume event that still correlates with the outcome** — `Contact` or `Lead`, not `QualifiedLead` — and use `QualifiedLead` for *judging*, not for optimising.
3. **Do not use automated scaling rules.** At this volume they react to noise.

### 5.1 Structure

```
CAMPAIGN 1 — Proof (objective: Traffic or Engagement)   ~25% of budget
  └ Ad set 1.1  Cold · geo Port Said + Damietta + Suez + Ismailia · interests: shipping/logistics/import-export
        Creatives: case-study hero, the number card, the client quote card

CAMPAIGN 2 — Enquiry (objective: Leads)                 ~50% of budget
  └ Ad set 2.1  Cold · same geo + interests · optimise for Lead
  └ Ad set 2.2  Lookalike 1% of the CRM/enquirer list  [ONLY once the source list is 300+]

CAMPAIGN 3 — Retargeting (objective: Leads)             ~25% of budget
  └ Ad set 3.1  Website visitors 30d + CaseStudyRead + video 50% viewers + page engagers 90d
        Creatives: the Diagnostic Session offer, the FAQ carousel, the objection post
```

**Sequencing note:** Campaign 3 has nobody in its audiences on day one. **Run Campaign 1 alone for the first 3–4 weeks** to fill the retargeting pools, then switch Campaign 3 on. Turning on retargeting with an empty audience is the most common way a small account wastes its first month — and it is why the old plan's 70/30 services/retargeting split is rejected: 30% of the budget aimed at an audience that does not exist yet.

**Campaign 2 ad set 2.2** stays off until the source audience is large enough for a lookalike to be meaningful. A lookalike built from 40 people is a lookalike of noise.

### 5.2 The Port Said / Suez geo angle

This is the highest-leverage targeting decision available and it is specific to this company.

- Interest targeting for "shipping agencies" is weak in Egypt — the categories are broad and full of enthusiasts rather than owners.
- **Geography does the qualifying instead.** Port Said, Damietta, Suez, and Ismailia are port cities where a disproportionate share of business owners are *in* port services. A 20 km radius around Port Said port is a far purer B2B audience than any interest stack.
- Layer, don't stack narrowly: geo (tight) + broad business-owner behaviours + age 30–60. Then let the creative do the qualifying — an ad whose first line says **"لو عندك وكالة ملاحية أو توكيلات في بورسعيد"** filters harder than any targeting setting, because the wrong person scrolls past and costs nothing.
- **Cost advantage:** these are small, cheap ad markets. CPMs in Port Said are far below Cairo.
- **Local proof compounds:** an ad naming a Port Said manning agency, shown to Port Said business owners, may reach people who know the client personally. That is the single strongest ad this company can run.
- Add an **exclusion** for job titles and interests indicating students, job seekers, and freelancers — otherwise a software ad in Egypt fills with CV enquiries.

---

## 6. Budget allocation

**Monthly budget = `TBD`.** Founder decision, blocker B7. What follows is structure, expressed as shares of a budget `B`, so it holds at any figure.

### 6.1 Allocation logic

| Principle | Consequence |
|---|---|
| Production is the constraint before reach | Months 1–2 spend goes to assets, not media (`[[Marketing Strategy]]` §8) |
| Retargeting needs an audience first | Month 1 of spend = Campaign 1 only; retargeting from month 2 |
| Small budgets must not fragment | Max 2–3 active ad sets |
| Media spend is a test budget until proven | No increase without a qualified-enquiry result |
| Reserve for opportunity | Hold ~10% unallocated |

### 6.2 Phased split of `B`

| Phase | Campaign 1 (Proof) | Campaign 2 (Enquiry) | Campaign 3 (Retarget) | Reserve |
|---|---|---|---|---|
| **Month 1 of spend** (fill the pools) | 60% | 30% | 0% | 10% |
| **Month 2** | 30% | 45% | 15% | 10% |
| **Month 3+** (steady state) | 25% | 45% | 20% | 10% |

### 6.3 Minimum viable daily spend

Below a floor, an ad set delivers so erratically that the data is unreadable and the money is wasted anyway. `proposed` rule: **no ad set runs below the equivalent of ~2× the expected cost per click per day**, and no ad set runs for fewer than 7 continuous days before being judged. If `B` divided by the planned ad sets falls below that floor, **run fewer ad sets**, not smaller ones.

### 6.4 What the money must not buy

- Page likes or follower campaigns. Explicitly banned — see `[[Marketing Strategy]]` §9.
- Boosted posts chosen by which post already got likes. Boosting is a blunt instrument with no ad-set control; use the Ads Manager.
- Any campaign whose success metric is reach, CPM, or video views.

---

## 7. Creative testing framework

**Test one variable at a time.** Small budgets cannot resolve a multi-variable test — the result is noise dressed as a finding.

### The hierarchy — test in this order, because impact runs in this order

1. **Offer** — is the Diagnostic Session the right hook, or is the case-study PDF a better first ask?
2. **Angle / pain** — certificate expiry vs scattered records vs manual reporting vs slow quoting.
3. **Hook line** — the first line of the caption. Biggest single lever after the angle.
4. **Format** — number card vs carousel vs 60s screen video vs founder-to-camera.
5. **Creative details** — colour, crop, layout. Test last, and only if 1–4 are settled.

### Rules

- **One idea per creative, maximum 15 words on the image** (`[[Foundation Brief]]` §8). Meta's delivery penalises text-heavy images, and the existing 8-bullet infographics are unreadable in a phone feed. Detail lives in the caption.
- 3–4 creatives per ad set. More than that and none gets enough delivery to be judged.
- Minimum 7 days or ~1,000 impressions per creative before any judgement.
- Kill on **cost per qualified enquiry**, never on CTR. A high-CTR creative that attracts students is worse than a low-CTR creative that attracts three agency owners.
- Every creative gets a `utm_content` ID so the CRM can trace a signed client back to the exact image.
- **Refresh on frequency, not on boredom.** In a small geo audience, frequency climbs fast; when frequency passes ~3.0 and results decline, rotate. Do not rotate because the team is tired of a creative that is still working.

### Starting creative set

| ID | Creative | Angle |
|---|---|---|
| `osamasakr-number-v1` | The number card | Result proof |
| `osamasakr-problem-v1` | "وكالة توظيف بحري بتشتغل على إكسيل وواتساب" | Pain recognition |
| `diagnostic-offer-v1` | "جلسة تشخيص مجانية، ٣٠ دقيقة، وبتخرج منها بورقة مكتوبة" | Offer |
| `founder-pov-v1` | Founder to camera, 45s, Arabic subtitles | Trust |
| `local-callout-v1` | "لو عندك وكالة ملاحية أو توكيلات في بورسعيد" | Self-selection |

Copy for all five is in `[[Content Templates and Hooks]]`. Banned phrases apply to paid creative exactly as to organic (`[[Foundation Brief]]` §5).

---

## 8. Decision rules — scale, hold, or kill

Judged **weekly**, on a rolling 7-day window, against **cost per qualified enquiry (CPQE)** as marked in the CRM. Set the CPQE benchmark once the first ten enquiries exist; before then, run and observe without acting on noise.

| Signal | Decision |
|---|---|
| CPQE at or below benchmark, 7+ days, 3+ qualified enquiries | **Scale** — increase budget by no more than 20–30% per week. Larger jumps reset the learning phase and typically make performance worse before it recovers |
| CPQE within ~1.5× benchmark | **Hold.** Change creative, not budget |
| CPQE above ~2× benchmark after 7 days and 1,000+ impressions | **Kill the ad set.** Do not "give it another week" — that is how a small budget is spent on hope |
| Leads arriving but none qualified | **Targeting or creative problem, not a budget problem.** Tighten the geo, add exclusions, make the first line of the copy more exclusionary. Never fix this by spending more |
| Cheap clicks, no enquiries | **Kill.** This is the seductive failure — the dashboard looks healthy. Clicks are not the product |
| Qualified enquiries arriving faster than they can be answered within 24h | **Pause spend.** Capacity is the binding constraint. Unanswered enquiries destroy more value than the ads create |
| Frequency > 3.0 with declining results | Rotate creative; if it persists, widen the geo before increasing budget |
| Any month with zero qualified enquiries from paid | **Stop all spend.** Return to organic and outreach, re-examine the offer, restart only with a changed hypothesis |

**Two standing rules:**
- **Never change more than one thing per week per ad set.** Otherwise nothing that happens can be attributed.
- **The founder, not the platform, decides what "qualified" means.** Meta will happily optimise toward whoever fills forms most readily.

---

## 9. Beyond Meta — when, and only when

| Channel | When it earns budget |
|---|---|
| **Google Search ads** | Only after the site renders server-side and converts. Intent-based search volume for "نظام إدارة وكالة ملاحية" in Egypt is likely small — but small and high-intent beats large and vague. Test with a tiny budget on exact-match terms once organic search proves any demand exists |
| **LinkedIn ads** | Expensive per click, and correct only when the target is Gulf enterprise or larger shipping companies — i.e. when geography stops being the acquisition mechanism (`[[Marketing Strategy]]` §5.1). Not in the first 6 months |
| **Instagram-only campaigns** | No. Instagram runs as a placement inside Meta campaigns, not as its own line |
| **TikTok** | No. See `[[Marketing Strategy]]` §9 |

---

## 10. Pre-launch checklist

Run this on the day spend is proposed. Any unchecked box means do not launch.

- [ ] All Gate 0 items green
- [ ] All Gate 1 items green
- [ ] Business Manager, ad account, and payment method set up and verified
- [ ] Pixel firing, verified in Events Manager
- [ ] Conversions API live
- [ ] All seven events firing correctly
- [ ] Domain verified in Business Manager
- [ ] Aggregated Event Measurement configured, `Lead` prioritised
- [ ] UTM convention documented and applied to every ad link
- [ ] Lead-form fallback built with the four qualifying questions
- [ ] Responder assigned, hours defined, 15-minute lead-form SLA agreed
- [ ] CRM ready with a "how did you hear about us" field and a qualified/unqualified flag
- [ ] Monthly budget set by the founder (blocker B7) and a hard account spending limit configured
- [ ] Benchmark CPQE agreed, or an explicit "observe first, no decisions for 14 days" period declared
- [ ] Creative set approved through Gate A and Gate C (`[[Content System]]` §5) — no banned phrases, one idea per creative, ≤15 words on image
- [ ] A written kill rule the founder has agreed to **in advance**, so a losing campaign is not defended emotionally later

## Related
[[Foundation Brief]] · [[Marketing Strategy]] · [[Content System]] · [[Social Media Playbook]] · [[Editorial Calendar - First 90 Days]] · [[Content Templates and Hooks]] · [[Offer Ladder]] · [[ICP - Ideal Customer Profiles]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]]
