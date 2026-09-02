---
date: 2026-09-02
type: checklist
tags:
  - delivery
  - kickoff
  - checklist
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Project Kickoff Checklist

## For future Claude

Run at the start of **every** project, without exception, including small ones and including internal M Tech Square group projects. This is Gate 0: it happens before Phase 1 Discovery work begins in `[[Delivery Process]]`.

All content here is `proposed` (2026-09-02) except where marked `stated`. Owners are **functions**, not people — the roster is unknown. Copy this file into the project folder and tick the boxes there; never tick them in this master copy.

The single most important design choice in this checklist: **the case-study permission conversation happens at kickoff, not at the end.** Asking a happy client at launch still fails half the time, because by then permission needs a legal review nobody planned for. Asking at kickoff, when goodwill is highest and the contract is already open, converts far better. This directly addresses the vault's biggest gap — four real projects and zero published outcomes (`[[Foundation Brief]]` §7).

---

## Terms used here

| Term | Plain meaning |
|---|---|
| **Point of contact (POC)** | The one person we talk to day to day. |
| **Decision-maker** | The one person who can say yes to money and scope. Sometimes the same person as the POC, often not. |
| **Credentials** | Usernames, passwords, API keys — anything that grants access to a system. |
| **Password manager** | An app that stores passwords encrypted and lets you share one safely without ever typing it into a chat. |
| **2FA** (two-factor authentication) | A second proof of identity, usually a code on your phone, on top of the password. |
| **Environment** | A running copy of the system. `Development` = where we build. `Staging` = private copy for testing. `Production` = the real one users touch. |
| **Case study** | A published write-up of the project: the problem, what we did, the result with a number. |

---

## Section 1 — Commercial (before anything else)

Nothing below this section starts until Section 1 is complete. Working before the deposit lands is the most expensive habit a small agency can have.

- [ ] Contract signed by both sides, with a copy stored in the project folder
- [ ] Contract includes: scope reference, payment milestones, change request process, warranty period, acceptance window, intellectual property ownership, termination terms
- [ ] Deposit invoice issued
- [ ] **Deposit received and confirmed in the bank** — not "promised", received
- [ ] Payment milestones written into the project plan with dates
- [ ] Client's legal/company name and tax details recorded correctly for invoicing
- [ ] Currency and payment method agreed (EGP / USD / SAR — relevant given Jeddah and Riyadh are `stated` service areas)
- [ ] Who at Code Square owns the commercial relationship: **TBD — assign**

---

## Section 2 — Scope and exclusions

- [ ] The in-scope list is written down and both sides have the same copy
- [ ] **The out-of-scope list is written down** — explicitly naming what we are NOT doing
- [ ] The V1 boundary is agreed: what ships first, what is deferred to V2
- [ ] Deliverables named one by one (not "a website" but "5 page templates, 1 admin dashboard, 1 booking flow")
- [ ] Assumptions written down (e.g. "client supplies all photography", "no data migration from the old system")
- [ ] Dependencies on the client listed with dates
- [ ] Both lists signed or confirmed in writing by the decision-maker

**Common exclusions worth naming explicitly, so they are never assumed:** content writing, translation, photography, data migration from an old system, third-party licence fees, ongoing hosting costs, SEO work, training beyond one session, support after the warranty period.

---

## Section 3 — Success metrics

The project cannot pass Gate A without this. See `[[Delivery Process]]` §4.

- [ ] 1–3 success metrics written down, each a number the client's business cares about
- [ ] Current baseline recorded for each metric — or `baseline unknown, will measure in week 1`
- [ ] The date when we will measure again is set (recommend 30 days after launch)
- [ ] Who provides the measurement data on the client side is named
- [ ] Both sides agreed in writing that these are the metrics

**Ask it in the client's language:** "Three months after this is live, what number will have changed for you? And what is that number today?"

If the client cannot answer, that is not a reason to skip it — it is the most valuable thing Discovery can produce.

---

## Section 4 — People

- [ ] **Client point of contact** named, with role, phone, and email
- [ ] **Client decision-maker** named, with role, phone, and email
- [ ] Backup contact named on the client side, for when the POC is unreachable
- [ ] Anyone else who must review or approve is named — and it is agreed that they give feedback *through* the POC, not directly to our team
- [ ] Code Square delivery owner: **TBD — assign**
- [ ] Code Square commercial owner: **TBD — assign**
- [ ] Named backup on the Code Square side for the delivery owner: **TBD — assign**

**The last box is a continuity control, not paperwork.** A project with exactly one person who knows anything about it is one illness away from stalling. See `[[Org and Roles]]`.

---

## Section 5 — Communication

- [ ] Primary channel agreed and written down (recommend one channel, not four)
- [ ] Escalation channel agreed — a phone call to a named person, not a group chat
- [ ] **Our response time to the client** committed: `TBD — set` (recommend: same working day for messages, 2 working days for anything requiring a decision or estimate)
- [ ] **Client's response time to us** committed: `TBD — set` (recommend 2 working days) — and the client understands that a late answer moves the schedule
- [ ] Working days and hours agreed on both sides, including how Fridays, weekends, and Ramadan hours are handled
- [ ] Weekly demo day and time booked as a recurring calendar invite for the whole project
- [ ] Weekly written progress note agreed: what it contains, who sends it, which day
- [ ] Agreed that requirements arriving informally (a WhatsApp voice note, a corridor conversation) are captured as change requests, not silently built
- [ ] Language of working communication agreed — Arabic, English, or both

---

## Section 6 — Access and credentials

**Security rule, non-negotiable:**

> **Credentials are never sent in plain text — not on WhatsApp, not in Messenger, not by email, not in a screenshot, not in a voice note.**
> They go through a password manager share, or the client creates an account for us themselves and we never see their personal password.
> If a credential does arrive in a chat, it is treated as compromised: use it once to change itself, then rotate it, and delete the message.

Why this matters here specifically: a company selling digital trust cannot ask clients to paste passwords into WhatsApp. It is also the most likely route to a real incident, because chat history is backed up to phones, laptops, and cloud accounts that nobody is auditing.

- [ ] Password manager vault created for this client, shared with the delivery team only
- [ ] Client shown how to share credentials into it (a 3-minute walkthrough, done live on the kickoff call)
- [ ] Domain registrar access — obtained, or confirmed to stay with the client
- [ ] DNS access — obtained or confirmed
- [ ] Hosting / server access
- [ ] Existing website or system admin access
- [ ] Database access, if migrating
- [ ] Third-party service accounts: payment gateway, email sending, SMS, maps, analytics
- [ ] Social media accounts, if in scope
- [ ] App store accounts (Apple Developer, Google Play), if a mobile app is in scope — **these take days to set up and are a classic launch-week delay**
- [ ] For every credential: recorded whose account it is and whether it transfers to the client at handover
- [ ] **2FA enabled** on every account we touch
- [ ] Agreed date on which Code Square access will be removed after handover
- [ ] Where credentials that must be shared with the client at handover will be delivered (password manager, never chat)

---

## Section 7 — Content and assets

Late content is the most common non-technical cause of a missed launch date. Name dates now.

- [ ] Logo files in vector format (`.svg` or `.ai`), not a screenshot
- [ ] Brand colours and fonts, or confirmation that Code Square defines them
- [ ] Photography — supplied, to be sourced, or to be shot; and who pays
- [ ] Written content per page or screen — who writes it, in which languages, by what date
- [ ] Translations — who provides them; **machine translation is not acceptable** (`[[Foundation Brief]]` rule 3)
- [ ] Legal text: privacy policy, terms of service, refund policy — who supplies, who reviews
- [ ] Existing data to be imported: format, volume, quality checked with a real sample
- [ ] Every content item has an owner and a due date on the project plan
- [ ] Agreed what happens if content is late: we launch with placeholders in a marked section, or the date moves — decided **now**, not in launch week

---

## Section 8 — Environments and setup

- [ ] Project folder created in the agreed location, with a standard structure
- [ ] Code repository created, with access granted to the delivery team
- [ ] Project board / task tracker created, with the backlog seeded
- [ ] Development environment set up and confirmed working by a second person
- [ ] Staging environment planned, with a date
- [ ] Production hosting decided: who owns the account, who pays, what it costs monthly
- [ ] Domain decided: who owns it, when it renews, **auto-renew on**
- [ ] TLS certificate approach decided and **auto-renewal confirmed** — see `[[Quality Standards and Handover]]`
- [ ] Backup approach decided: what is backed up, how often, where to, and who verifies a restore works
- [ ] Error monitoring and analytics decided (installed later, decided now)

---

## Section 9 — The case-study permission conversation

**Do this at kickoff. Do not defer it.**

Rationale to say out loud to the client: we want to write up what we build together, and it is far easier to agree the rules now than to negotiate after launch. The client also gets something — a published case study is free marketing for *them*, and they get approval rights over every word.

- [ ] Case-study permission raised in the kickoff meeting
- [ ] Permission level agreed, one of:
  - **Full** — name, logo, screenshots, numbers, quote
  - **Partial** — name and logo, no numbers
  - **Anonymous** — "a crewing agency in Port Said", screenshots blurred, numbers included
  - **None** — nothing published (record the reason; ask again at the 30-day review)
- [ ] Agreed which numbers may be published, and where they will come from
- [ ] Agreed that the client sees and approves the draft before anything goes live
- [ ] Agreed that a short testimonial (written or filmed) is requested at the 30-day post-launch review, not at handover
- [ ] Permission clause added to the contract, or a one-page permission form signed separately
- [ ] Screenshot and logo usage rights specified
- [ ] Calendar reminder set for the 30-day review, where the case study is actually produced

**If the answer is "none":** accept it gracefully, record it, and still capture the internal write-up for the team. The internal projects (M Tech Square site, Techno Square platform) need no permission at all and should be published first while external permissions are pending — `[[Foundation Brief]]` §7.

---

## Section 10 — Risk and continuity

- [ ] Risk register created with at least the 5 starter risks from `[[Delivery Process]]` §10
- [ ] An owner assigned to each risk
- [ ] Client informed of the top 3 risks and what we are doing about each — this is trust-building, not weakness
- [ ] Confirmed no part of this project depends on exactly one person with no backup and nothing written down

---

## Section 11 — The kickoff meeting itself

**Length:** 90 minutes. **Attendees:** client POC + decision-maker; Code Square delivery owner + commercial owner + whoever will actually do the design and build work.

**Prepare before the meeting:** signed contract, confirmed deposit, this checklist, the scope sheet draft, a blank risk register, the password manager vault already created.

### Agenda

| Min | Item | Outcome |
|---|---|---|
| 0–10 | Introductions and roles | Everyone knows who does what and who decides |
| 10–20 | Why this project exists, in the client's own words | The problem statement, drafted live on screen |
| 20–35 | Scope walk-through — in and **out** | Both lists confirmed |
| 35–45 | Success metrics: what number changes, and what is it today | Metrics + baselines written down |
| 45–55 | How we work: phases, gates, weekly demo, change requests | Client understands that new ideas are welcome *and* go through a CR |
| 55–65 | Communication: channels, response times, working hours | Committed both ways |
| 65–75 | Access, credentials, and the security rule; content and asset dates | Vault set up live; dates on the plan |
| 75–85 | **Case-study permission** | Permission level agreed |
| 85–90 | Top risks, next steps, who does what by when | Written actions with owners and dates |

### After the meeting
- [ ] Written summary sent within 1 working day: decisions, actions, owners, dates
- [ ] Client confirms the summary in writing — this confirmation is the project's foundation document
- [ ] Project plan updated with all dates gathered
- [ ] Weekly demo invite sent for the full duration of the project
- [ ] Discovery work begins — `[[Delivery Process]]` Phase 1

---

## Section 12 — Kickoff sign-off

| Item | Confirmed by | Date |
|---|---|---|
| Sections 1–11 complete | Code Square delivery owner — TBD | |
| Client agrees the written summary | Client decision-maker | |
| Gate 0 passed, Discovery may start | Both | |

If any box in Sections 1, 2, 3, 4, or 6 is unticked, **the project does not start.** Everything else can trail by a few days; those five cannot.

## Related
[[Delivery Process]] · [[Quality Standards and Handover]] · [[Support and Maintenance SLA]] · [[Org and Roles]] · [[Tools Stack]] · [[Sales Playbook]] · [[Pricing and Packaging]] · [[Service Catalog]] · [[Foundation Brief]]
