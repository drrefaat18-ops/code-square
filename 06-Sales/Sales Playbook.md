---
date: 2026-09-02
type: sales-playbook
tags:
  - sales
  - process
  - pipeline
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Sales Playbook — Code Square

## For future Claude

This is the **operating manual for how Code Square sells**. It is `proposed` (written 2026-09-02), not `stated` — today there is no sales process at all. Leads arrive on WhatsApp, Messenger, phone, and a website form that promises a 24-hour reply nobody owns, and nothing is logged anywhere.

Rules for editing this file:
- Never invent a price. Every number goes to `[[Pricing and Packaging]]` or stays `TBD`.
- Never invent a client name or a result. The only four projects that exist are in `[[Portfolio and Case Studies]]`.
- Every stage here must stay consistent with the offer ladder in `[[Foundation Brief]]` §6. If the founder changes the ladder, change this file the same day.
- The banned-phrases list in `[[Foundation Brief]]` §5 applies to every word a prospect hears.
- The sibling files are `[[Discovery Call Script]]`, `[[Objection Handling]]`, `[[Lead Intake and CRM]]`, `[[Outbound Prospecting Playbook]]`, `[[Qualification and Deal Review]]`.

---

## Part 0 — "How we sell" in five minutes (read this first)

> A new person joining Code Square reads only this box on day one. Everything below is the detail.

**What we sell.** Not "websites and apps". We sell **the system a business actually runs on** — and then we keep running it with them. The words on the website already say it: *مهندسو أنظمة* / Outsourced CTO. That is the promise. (`stated`, from `[[Foundation Brief]]` §1)

**Who we sell to.** One segment leads: **maritime, logistics and port services around Port Said and the Suez Canal** — shipping agencies, crewing/manning agents, freight forwarders, customs brokers. We already built one (Osama Sakr Manning Agency). Education runs in parallel because Techno Square is a live demo we own. Healthcare is one pilot, not a campaign. See `[[ICP - Ideal Customer Profiles]]`.

**How the sale is shaped.** Three rungs, never skipped, never reordered:

| Rung | Name | Price | What it is |
|---|---|---|---|
| 1 | **جلسة تشخيص** — Diagnostic Session | Free, 30–45 min | We diagnose the problem. They keep a one-page written output whether they buy or not. |
| 2 | **خريطة المشروع** — Blueprint | Fixed, `TBD` — see `[[Pricing and Packaging]]` | 1–2 weeks. Problem definition, user journey, feature priority, phased scope, fixed build quote. Fully creditable against the build. |
| 3 | **البناء والتشغيل** — Build & Run | `TBD` | Fixed-scope V1 → versions → monthly retainer. This is where the money is. |

**The one rule that matters most.** We never quote a build price from a conversation. Ever. A build quote comes out of a paid Blueprint. If someone demands a number before the Blueprint, we give a **range with a stated assumption** and we say plainly that the real number comes from the Blueprint. This single rule is what separates us from a freelancer and it is what stops us losing money on scope.

**What "good" looks like in a week.** 5 new qualified conversations. 3 Diagnostic Sessions held. 1 Blueprint sold. Every single lead in the tracker with a next action and a date. Nothing — nothing — sitting with no next step.

**The seven-word version:** نشخّص، نكتب الخريطة، نبني، ونفضل معاك.

---

## Part 1 — Vocabulary (define once, use everywhere)

The reader of this file is a pharmacist, not a salesperson. Terms below are used throughout the vault.

| Term | Plain meaning |
|---|---|
| **Lead** (عميل محتمل) | Anyone who contacted us or we contacted, who might one day pay. Not yet judged. |
| **Qualified lead** | A lead we have checked and believe could realistically buy: they have the problem, some money, and someone who can say yes. |
| **Pipeline** (خط الصفقات) | The list of all live deals, sorted by which stage they are in. |
| **Stage** (مرحلة) | Where a deal sits in the process. A deal is in exactly one stage at a time. |
| **Entry criteria** | The fact that must be true before a deal is allowed *into* a stage. |
| **Exit criteria** | The fact that must be true before a deal is allowed to *leave* the stage. No opinion, a fact. |
| **SLA** | Service Level Agreement — a promise about time. "We reply within 24 hours" is an SLA. Ours must be real, not decorative. |
| **Discovery** (تشخيص) | The conversation where we find out what is actually wrong. We listen; we do not pitch. |
| **Blueprint** (خريطة المشروع) | Our paid scoping engagement. Rung 2 of the ladder. |
| **Retainer** (عقد شهري) | A fixed monthly fee for ongoing support and iteration. |
| **Forecast** (التوقع) | Our honest estimate of how much money will actually close this month/quarter. |
| **Weighted value** | Deal value × probability. Used so the forecast is not fantasy. |
| **Disqualify** (استبعاد) | Deciding on purpose that a lead is not a fit and stopping work on it. This is a *good* outcome, not a failure. |
| **Handoff** | Passing a deal from one owner to another (marketing → sales, sales → delivery) with a written summary. |
| **Touch** | Any single attempt to contact someone — a message, a call, a visit. |

---

## Part 2 — The pipeline

Eight stages. A deal lives in exactly one. Movement is only allowed when the exit criteria are literally true.

```
0. Inbox      →  1. Contacted  →  2. Qualified  →  3. Diagnostic
   →  4. Blueprint Proposed  →  5. Blueprint Won  →  6. Build Proposed
   →  7. Closed Won / Closed Lost
```

### Stage 0 — الوارد · Inbox

| Field | Value |
|---|---|
| **Definition** | A message, call, form, or referral arrived. Nobody has answered yet. |
| **Entry criteria** | Any inbound contact exists, on any channel. |
| **Exit criteria** | Logged in the tracker **and** a human has replied. |
| **Owner** | `TBD` — the Response Owner (one named person, see Part 5) |
| **SLA** | **Website form: 24 hours, no exceptions** (this promise is already published — `stated`). WhatsApp/Messenger: **2 working hours**. Phone missed call: **same day**. Walk-in: immediate. |
| **What happens** | Log the lead (see `[[Lead Intake and CRM]]`), reply, ask the two routing questions, book the Diagnostic Session. |
| **Trap** | A lead sitting unanswered in a phone nobody owns. This is the single most expensive failure in the company today. |

### Stage 1 — تم التواصل · Contacted

| Field | Value |
|---|---|
| **Definition** | We replied. We do not yet know if they are a fit. |
| **Entry criteria** | Reply sent, lead record created with source and channel. |
| **Exit criteria** | Either (a) qualification questions answered → Stage 2, or (b) 7 touches completed with no reply → Closed Lost (reason: no response), or (c) clear disqualifier found → Closed Lost (reason: not a fit). |
| **Owner** | Response Owner |
| **SLA** | Follow-up cadence runs to touch 7 over 21 days. Cadence text is in `[[Lead Intake and CRM]]`. |
| **What happens** | Light qualification by message. We are trying to earn a 30-minute call, nothing more. |
| **Trap** | Trying to sell in WhatsApp. The goal of this stage is a booked call, not a quote. |

### Stage 2 — مؤهَّل · Qualified

| Field | Value |
|---|---|
| **Definition** | We believe they could buy, and a Diagnostic Session is booked with a date and time. |
| **Entry criteria** | We know: what business they are in, roughly what is broken, who we are talking to, and that a date is agreed. |
| **Exit criteria** | The Diagnostic Session actually happened. |
| **Owner** | The person who will run the session |
| **SLA** | Session held within **5 working days** of booking. Confirmation message the day before, at a set hour. |
| **What happens** | Pre-call research (Part 4 of `[[Outbound Prospecting Playbook]]`), confirmation message, prepare the note template from `[[Discovery Call Script]]`. |
| **Trap** | No-shows. A confirmation the day before cuts them roughly in half. Track your own no-show rate from week one. |

### Stage 3 — جلسة التشخيص · Diagnostic

| Field | Value |
|---|---|
| **Definition** | The free session has been held. We now know the real problem, its cost, and the constraints. |
| **Entry criteria** | Session completed, notes written into the lead record **the same day**. |
| **Exit criteria** | The one-page written diagnosis has been sent, **and** the prospect has either agreed to hear a Blueprint proposal or explicitly declined. |
| **Owner** | Session owner |
| **SLA** | One-page written output delivered within **48 hours** of the session. This is a promise we make on the call — keep it. |
| **What happens** | Diagnose (website / app / MVP / internal system — see `[[Discovery Call Script]]`), write the one-pager, recommend the next step. |
| **Trap** | Giving away a full solution design for free. The one-pager states *what* is wrong and *what direction* to take. It does not contain the architecture or the feature list. Those are the Blueprint. |

### Stage 4 — عرض الخريطة · Blueprint Proposed

| Field | Value |
|---|---|
| **Definition** | We have proposed the paid Blueprint with a price and a scope. |
| **Entry criteria** | A written Blueprint proposal has been sent. |
| **Exit criteria** | Signed/agreed → Stage 5, or refused → Closed Lost with a logged reason. |
| **Owner** | Session owner |
| **SLA** | Proposal sent within **3 working days** of the Diagnostic. Follow-up call booked *at the moment of sending*, never after. |
| **What happens** | Proposal review call. Objections handled per `[[Objection Handling]]`. |
| **Trap** | Emailing a proposal and waiting. A proposal with no scheduled review call is a proposal that dies quietly. |

### Stage 5 — الخريطة قيد التنفيذ · Blueprint Won

| Field | Value |
|---|---|
| **Definition** | Blueprint paid and being delivered. **This is our first revenue event.** |
| **Entry criteria** | Payment terms agreed per `[[Pricing and Packaging]]`, kickoff scheduled. |
| **Exit criteria** | Blueprint document delivered, including a fixed build quote. |
| **Owner** | Delivery owner (`TBD`) with sales staying in the room |
| **SLA** | 1–2 weeks, as promised at sale. Late delivery here poisons the build sale. |
| **What happens** | Discovery workshops, user journey, feature priority, phased scope, fixed quote. |
| **Trap** | Letting sales disappear during delivery. The person who sold it presents the build quote. |

### Stage 6 — عرض البناء · Build Proposed

| Field | Value |
|---|---|
| **Definition** | The fixed build quote is on the table. |
| **Entry criteria** | Blueprint delivered and presented in a live meeting — never sent cold. |
| **Exit criteria** | Signed → Closed Won, or refused → Closed Lost with reason. |
| **Owner** | Session owner |
| **SLA** | Decision chased to a **yes or a no within 21 days**. After that, one honest closing message (the "should I close your file?" message in `[[Lead Intake and CRM]]`), then Closed Lost with a 6-month re-engagement reminder. |
| **What happens** | Negotiation on scope and phasing — **not on price with the same scope**. If the budget is smaller, the phase gets smaller. |
| **Trap** | Discounting to close. Cut scope, never rate. A discount now becomes the expected rate forever. |

### Stage 7 — Closed Won / Closed Lost

- **Closed Won:** signed. Handoff to delivery within 2 working days with the written handoff pack (Part 5). Ask for the case-study permission **at signature**, not at launch — see `[[Portfolio and Case Studies]]`.
- **Closed Lost:** a reason from the fixed list is mandatory (Part 7). Re-engagement reminder set for **+6 months**. A lost deal with no logged reason is a lesson thrown in the bin.

---

## Part 3 — Stage-to-forecast mapping

Probability numbers are `proposed` starting values. Replace them with your own real conversion data after 20 closed deals — until then they are an educated guess, and should be labelled as such in any report.

| Stage | Probability | Counts in forecast as | Notes |
|---|---|---|---|
| 0 Inbox | 0% | Not in forecast | |
| 1 Contacted | 5% | Not in forecast | Too early to be real |
| 2 Qualified | 10% | Not in forecast | |
| 3 Diagnostic held | 25% | **Pipeline** | First point the deal is real |
| 4 Blueprint proposed | 40% | **Pipeline** | |
| 5 Blueprint won | 60% | **Commit** — Blueprint revenue is *booked*, build revenue is 60% | Two separate lines |
| 6 Build proposed | 70% | **Commit** | |
| 7 Closed Won | 100% | **Booked** | |

**Three forecast lines, reported weekly:**
- **Booked** — money already contracted. Certain.
- **Commit** — deals we will personally stand behind closing this period.
- **Pipeline** — everything else, weighted.

**Never** report the raw sum of all open deals as "the pipeline is worth X". It is not. Report the weighted number and say it is weighted.

---

## Part 4 — Ownership map

Roles, not people. In a 2–3 person team one person wears several hats — that is fine, as long as every hat has exactly one head.

| Role | Owns | Must not |
|---|---|---|
| **Response Owner** | The inbox promise. Every channel checked at set times. Every lead logged. Stages 0–1. | Improvise pricing. |
| **Diagnostic Owner** | Running the free session, the one-pager, the Blueprint proposal. Stages 2–4. | Skip the written output. |
| **Delivery Owner** | Blueprint execution and the build. Stages 5+. | Agree new scope without the Diagnostic Owner. |
| **Pipeline Owner** | The weekly review, the forecast, data hygiene. | Let a deal sit with no next action. |

**Escalation:** any deal above the "large" threshold in `[[Pricing and Packaging]]` (`TBD`), any deal with a signed contract from the client's side, and any Gulf deal → founder reviews before commitment.

---

## Part 5 — Handoffs

A handoff without a written artifact is not a handoff.

### Marketing → Sales
Triggered when a lead arrives from any campaign or post.
**Required:** source, channel, exact UTM or post reference, the verbatim first message, timestamp.
**Rule:** marketing never promises a price or a timeline in a comment or a DM. Marketing books the Diagnostic Session, full stop.

### Sales → Delivery (Blueprint)
Within 2 working days of the Blueprint being won.
**Required pack:** the Diagnostic notes, the one-pager sent, what was promised verbatim, the constraints (budget band, deadline, decision process), who the champion is, who the sceptic is, and anything we explicitly said we would *not* do.
**Rule:** the Diagnostic Owner attends the kickoff. No cold throw-overs.

### Sales → Delivery (Build)
At Closed Won.
**Required pack:** signed scope, phase plan, payment schedule, named client-side owner, the success metric agreed with the client, plus the case-study permission status.
**Rule:** anything promised verbally that is not in the scope document gets written down at handoff or it does not exist.

### Delivery → Sales (expansion)
At every project milestone and at go-live.
**Required:** what changed for the client, ideally with a number. That number is both a retainer trigger and the proof asset `[[Portfolio and Case Studies]]` is starving for.

---

## Part 6 — The weekly rhythm

Small team, so keep it short and immovable.

| When | What | Duration | Output |
|---|---|---|---|
| **Every working day, 09:30** | Channel sweep: WhatsApp, Messenger, form inbox, phone log. Everything logged, everything answered. | 15 min | Zero unanswered leads |
| **Every working day, 16:30** | Second sweep. Nothing goes overnight unanswered. | 10 min | Same |
| **Sunday, 10:00** | **Pipeline review.** Every deal in Stage 2+ read aloud: stage, next action, date, blocker. Deals with no next action are either given one or closed. | 45 min | Updated tracker, forecast |
| **Sunday, 11:00** | **Prospecting block.** Outbound list built and worked. See `[[Outbound Prospecting Playbook]]`. | 90 min | Weekly activity targets hit |
| **Wednesday, 10:00** | **Deal review.** Deep review of the 3 biggest live deals only. See `[[Qualification and Deal Review]]`. | 30 min | Named risk + action per deal |
| **Last Thursday of month** | **Win/loss review.** Every deal closed that month, won or lost, reviewed against the template in `[[Qualification and Deal Review]]`. | 45 min | Logged reasons, one process change |

**Weekly activity targets** (`proposed`, first 90 days):

| Metric | Target |
|---|---|
| New qualified conversations | 5 |
| Diagnostic Sessions held | 3 |
| Blueprint proposals sent | 1–2 |
| Blueprints won | 1 |
| Outbound first-touches | 20 |
| In-person visits (Port Said) | 3 |
| Leads with no next action | **0** |

Activity is the only thing fully under our control in month one. Track activity weekly, outcomes monthly.

---

## Part 7 — Closed Lost reasons (fixed list — pick one, no free text)

1. No response after full cadence
2. No budget now
3. Budget exists but below our minimum
4. Chose a freelancer / cheaper vendor
5. Chose a template / off-the-shelf product (Wix, Odoo, ready-made system)
6. Chose another agency
7. Decided to build internally
8. Timing — real project, wrong quarter (→ re-engagement date is mandatory)
9. Not a fit — we disqualified them
10. Went silent after proposal
11. Lost to internal politics / decision-maker changed
12. Project cancelled entirely

Every Closed Lost also records: the stage it died in, what we would do differently, and a re-engagement date.

---

## Part 8 — The rules that do not bend

1. **The 24-hour website SLA is real or it comes off the website.** A published promise nobody owns is worse than no promise. Assign the owner this week. (`[[Foundation Brief]]` §9, Priority 0)
2. **No build price without a Blueprint.** Ranges with stated assumptions only.
3. **Every lead is logged, on every channel, the moment it arrives.** An unlogged lead does not exist.
4. **Every deal has a next action with a date.** Always. This is the pipeline review's only real test.
5. **Cut scope, never rate.**
6. **Disqualify early and say so kindly.** A bad-fit client closed is a refund and a bad review waiting to happen.
7. **Never say a banned phrase.** `[[Foundation Brief]]` §5. No أقوى فريق, no أفضل شركة, no 99.9% uptime, no SLA guarantee unless a real SLA document exists.
8. **Never name a client we do not have written permission to name.** Today that is two internal projects freely, and El Shoush + Osama Sakr **only once permission is on file**.
9. **Everything promised verbally gets written down the same day** — in the lead record and, at signature, in the scope.

---

## Open questions blocking this playbook

Move these to `[[Open Questions and Decisions Needed]]`:
- Who is the Response Owner, by name?
- Real pricing for the Blueprint and the build. Minimum project size.
- The website form's budget dropdown bands — unknown, and they shape every conversation.
- Do we have written case-study permission from El Shoush and Osama Sakr?
- Is the founder full-time on sales, and how many hours a week?
- Which methodology is canonical (site's 4-phase vs Facebook's 5-stage)? Sales must quote one.

## Related
[[Foundation Brief]] · [[ICP - Ideal Customer Profiles]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Portfolio and Case Studies]] · [[Discovery Call Script]] · [[Objection Handling]] · [[Lead Intake and CRM]] · [[Outbound Prospecting Playbook]] · [[Qualification and Deal Review]] · [[Open Questions and Decisions Needed]]
