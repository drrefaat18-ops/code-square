---
date: 2026-09-02
type: process
tags:
  - delivery
  - process
  - methodology
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Delivery Process

## For future Claude

This turns Code Square's own **published** 4-phase methodology (التأسيس → المعمارية → الهندسة → الإطلاق والتطوير, `stated`, from the website) into an operating process people can actually run. The 4-phase model is `stated`; everything about gates, owners, durations and artifacts is `proposed` and dated 2026-09-02.

Two methodologies are published today and they conflict — the website's 4 phases and Facebook's 5 stages. Section 2 reconciles them and recommends which becomes canonical. Do not publish both again (`[[Foundation Brief]]` rule 6).

Team roster is **unknown**. Every "owner" below is a **function**, not a person. One person may own several. Never invent headcount.

---

## 1. Words defined before we start

Read this once. Everything else assumes it.

| Term | Plain meaning |
|---|---|
| **Scope** | The exact list of what we agreed to build. Anything not on the list is not being built. |
| **Artifact** | A file or document produced by a step — a written thing you can point at. Not a conversation. |
| **Exit gate** | A checkpoint. Work does not move to the next phase until the named conditions are true and someone signs. |
| **MVP** (Minimum Viable Product) | The smallest version of the product that a real user can actually use to get the real job done. Not a demo, not a half-thing. |
| **Version / increment** | One shippable slice of work. V1, V2, V3 — each one usable on its own. |
| **Change request (CR)** | A written request to add or alter scope after it was agreed. Costs time or money, or both. |
| **Risk register** | A list of things that could go wrong, who watches each one, and what we do if it happens. |
| **Escalation** | Pushing a stuck decision or problem up to someone with the authority to resolve it. |
| **Backlog** | The ordered queue of work not yet started. |
| **Staging environment** | A private copy of the system where we test before real users see it. |
| **Definition of Done** | The written conditions a piece of work must meet before we call it finished. See `[[Quality Standards and Handover]]`. |

---

## 2. Reconciling the two published methodologies

`stated` — both of these are already public.

| Website (4 phases, AR) | Facebook (5 stages) |
|---|---|
| ① التأسيس / Discovery | ① Discovery |
| — | ② User Analysis |
| ② المعمارية / Architecture | ③ UX/UI Design |
| ③ الهندسة / Engineering | ④ Development (Frontend/Backend) |
| ④ الإطلاق والتطوير / Launch & Iterate | ⑤ Testing & Launch |

**They are not two different processes. They are the same process cut at different points.** The Facebook version splits Discovery into two (Discovery + User Analysis), narrows Architecture to only its design half, and hides testing inside a launch stage. The website version is broader and includes the part that actually earns the money — التطوير, ongoing iteration after launch — which the Facebook version drops entirely.

**Recommendation (`proposed`): the website 4-phase model becomes canonical.** Reasons:

1. It already sits on the site all traffic will be driven to.
2. It is the only version that includes life *after* launch — where the retainer and the "Outsourced CTO" positioning live (`[[Foundation Brief]]` §3).
3. Four phases are easier for a client to hold in their head than five.
4. User research and UX/UI are not deleted — they become named **activities inside** Phase 1 and Phase 2 (below), so nothing already published on Facebook becomes a lie.

**Action:** retire the 5-stage graphic from future publishing. Do not delete the old post; simply stop reproducing it. When the process is next described publicly, describe the 4 phases and list user analysis and UX/UI as activities within them.

---

## 3. The four phases at a glance

| # | Phase | Objective in one line | Typical duration (`proposed`) | Ends with |
|---|---|---|---|---|
| 1 | **التأسيس — Discovery** | Understand the business and decide what is worth building | 1–2 weeks | Gate A — Scope Agreed |
| 2 | **المعمارية — Architecture** | Decide how it will be built and what it will look like | 1–3 weeks | Gate B — Design & Architecture Approved |
| 3 | **الهندسة — Engineering** | Build it, test it, prove it works | 4–12 weeks (varies widely) | Gate C — Ready to Launch |
| 4 | **الإطلاق والتطوير — Launch & Iterate** | Put it live, hand it over, keep improving it | Launch week + ongoing | Gate D — Accepted & Handed Over, then retainer |

Durations are **placeholders until three real projects have been measured**. Record actual dates on every project and replace these numbers after project #3. Never quote a duration to a client from this table — quote it from the Blueprint (see `[[Pricing and Packaging]]`).

---

## 4. Phase 1 — التأسيس (Discovery)

**Objective:** understand the client's business well enough to say what should be built, what should not, and roughly what it costs. If we cannot say that at the end, the phase is not finished.

**Owner:** Product/Discovery function. **Supported by:** Sales (context from the deal), Design.

### Activities
- Kickoff meeting — run `[[Project Kickoff Checklist]]` in full.
- Business walk-through: how does money actually move through this business today?
- Current-state map: what does the client do manually right now, step by step, who does it, how long does it take, where does it go wrong?
- **User analysis** (this is where the Facebook "User Analysis" stage lives): who are the actual user types, what is each one trying to get done, what do they use today?
- Problem statement written down in one paragraph and agreed.
- Success metrics defined — see below.
- Feature list drafted, then cut into Must / Should / Could / Won't.
- Constraint capture: budget, deadline, existing systems that must be integrated, legal or regulatory limits.
- Risk register started.

### Success metrics rule
A project without a written success metric cannot pass Gate A. It must be a number the *client's business* cares about, not a technical one. Examples in Code Square's actual verticals:

| Vertical | Bad metric | Good metric |
|---|---|---|
| Maritime / crewing | "the system works" | "crew placement paperwork drops from 3 days to same-day" |
| Education | "the app is live" | "enrolments completed online rise from 0% to 60% of intake" |
| Healthcare | "nice interface" | "dispensing errors logged per month falls below X" |

### Inputs required
Client time (see obligations), access to the people who actually do the work, existing documents, screenshots of current tools, sample data.

### Outputs / artifacts
- `Discovery Notes` — the raw record
- `Current-State Process Map` — the manual workflow as it exists today
- `User Types & Jobs` — one page
- `Problem Statement` — one paragraph, agreed in writing
- `Success Metrics` — 1–3 numbers with a baseline
- `Scope Sheet` — in-scope list **and an explicit out-of-scope list**
- `Risk Register v1`
- `Indicative Budget & Timeline`

The out-of-scope list is not optional. Most scope disputes are about things nobody ever wrote down as excluded.

### Client obligations in this phase
- Name a single **point of contact** and a single **decision-maker** (may be the same person) — `[[Project Kickoff Checklist]]`.
- Make the people who do the work available for the current-state walk-through.
- Answer questions within the agreed response window.
- Sign off on the Problem Statement and Scope Sheet.

### Gate A — Scope Agreed
Cannot proceed until **all** are true:
- [ ] Problem statement written and signed by the client decision-maker
- [ ] Success metrics written with a baseline number (or "baseline unknown — will measure in week 1")
- [ ] In-scope and out-of-scope lists both written and signed
- [ ] Budget band and timeline accepted in writing
- [ ] Commercial terms in place: contract signed, deposit received (see `[[Project Kickoff Checklist]]`)
- [ ] Risk register has at least the top 5 risks with owners

**Gate A is signed by:** the client decision-maker + the Code Square delivery owner.

---

## 5. Phase 2 — المعمارية (Architecture)

**Objective:** decide *how* it gets built — both the structure under the hood and the experience on the surface — so that Engineering is execution, not invention.

**Owner:** Architecture/Technical function. **Supported by:** Design (UX/UI), Product.

### Activities
- System architecture: what the parts are, how data flows, what gets stored where.
- Technology decisions written down with the reason (an "architecture decision record" — one short entry per decision: what we chose, what we rejected, why).
- Integration plan: every external system it must talk to, and confirmation that the integration is actually possible. **Test the API before committing to it** — this is the most common source of mid-project surprises.
- Data model: what entities exist, what fields, what rules.
- **UX/UI design** (this is where the Facebook "UX/UI Design" stage lives): user flows → wireframes → visual design → clickable prototype.
- Security and access design: who can see what, how people log in.
- Hosting and environment plan: where it lives, staging vs production, backups.
- Version plan: how the scope is sliced into V1 / V2 / V3 (see §8).
- Firm estimate and schedule replacing the indicative one.

### Inputs required
All Phase 1 artifacts. Client brand assets. Access credentials for any system to be integrated — handled per the security rule in `[[Project Kickoff Checklist]]`, never in plain text over WhatsApp.

### Outputs / artifacts
- `System Architecture Diagram`
- `Architecture Decision Records`
- `Data Model`
- `Integration Plan` (each integration marked *verified* or *unverified*)
- `Wireframes` → `Visual Designs` → `Clickable Prototype`
- `Environment & Hosting Plan`
- `Version Plan (V1/V2/V3)`
- `Firm Estimate & Schedule`
- `Risk Register v2`

### Client obligations
- Review and approve the prototype within the agreed window. **Design approval is a hard dependency** — engineering does not start on an unapproved screen.
- Provide brand assets, content, and real sample data.
- Provide or authorise credentials for integrations.
- Nominate who signs off design — the named decision-maker, not a committee.

### Gate B — Design & Architecture Approved
- [ ] Clickable prototype reviewed and approved in writing by the decision-maker
- [ ] Architecture diagram and data model reviewed internally
- [ ] Every integration marked *verified* — or explicitly moved out of V1
- [ ] Version plan agreed: what is in V1, what is deferred
- [ ] Firm estimate accepted; any gap to the Phase 1 indicative number raised and resolved *now*, not later
- [ ] Environments provisioned, or the plan to provision them dated and owned

---

## 6. Phase 3 — الهندسة (Engineering)

**Objective:** build V1 to the standard in `[[Quality Standards and Handover]]`, with the client seeing progress continuously rather than at the end.

**Owner:** Engineering function (frontend / backend / DevOps). **Supported by:** QA, Product.

### Activities
- Work broken into small items in a backlog, each with a written acceptance condition.
- Work runs in **fixed cycles** — one week recommended, two weeks maximum. Every cycle ends with something demonstrable on staging.
- **Weekly client demo + written progress note.** Non-negotiable. The largest single cause of a failed handover is a client who first sees the product in month three.
- Code review before anything is merged.
- Testing as work is completed, not saved for the end. The Facebook 5-stage model's biggest weakness is implying testing is a phase at the end — it is not.
- Risk register reviewed weekly.
- Change requests handled per §9.

### Inputs required
Approved designs, provisioned environments, content and assets from the client, verified integration access.

### Outputs / artifacts
- Working software on staging, updated every cycle
- `Weekly Progress Note` — what shipped, what is next, what is blocked, what decisions we need from you
- Test records
- Updated backlog
- Draft technical documentation, written as we go and never at the end

### Client obligations
- Attend or watch the weekly demo. Absence is a project risk; after two consecutive missed demos it is escalated.
- Answer blocking questions within the agreed response window — an unanswered question stops work, and stopped work still burns calendar time.
- Deliver content and assets on the agreed dates.
- Send no new requirements informally. Everything new goes through the change request in §9.

### Gate C — Ready to Launch
- [ ] All V1 scope items meet the feature-level Definition of Done (`[[Quality Standards and Handover]]`)
- [ ] Full pre-launch checklist passed — including **TLS certificate valid and auto-renewing**
- [ ] Client has tested it themselves on staging and confirmed in writing
- [ ] Known defects listed, each classified *fix before launch* or *accepted, fix later*
- [ ] Backups, monitoring, and error alerting live
- [ ] Handover pack drafted
- [ ] The payment milestone due at this stage is settled

---

## 7. Phase 4 — الإطلاق والتطوير (Launch & Iterate)

**Objective:** go live safely, transfer ownership properly, then keep improving. This phase never really ends — it becomes the retainer.

**Owner:** DevOps/Engineering for launch; Account Management for what follows.

### Activities — launch week
- Deploy to production at an agreed low-traffic time. Never on a Thursday afternoon, never the day before a holiday.
- Verify on production: run the pre-launch checklist again against the live system.
- Watch for 48 hours with error monitoring on and a named person actually assigned to look at it.
- Admin training session with the client's team.
- Hand over the handover pack and transfer credentials properly.

### Activities — iterate
- Warranty period, 30 days recommended (`proposed`): defects in delivered V1 scope fixed at no charge. Scope is the V1 scope sheet; new ideas are not defects.
- Post-launch review at 30 days: did the success metric move? See `[[Quality Standards and Handover]]`.
- Move to the `[[Support and Maintenance SLA]]` retainer.
- V2 planning, drawn from the deferred list and from what real usage revealed.

### Client obligations
- Attend the admin training and nominate who will be trained.
- Accept or reject against the written acceptance criteria within the agreed window — 10 working days recommended, with silence past the window counting as acceptance. This must be in the contract.
- Sign the case-study permission agreed at kickoff (see `[[Project Kickoff Checklist]]` — this is exactly why we ask at the start, not now).
- Take over ownership of accounts and pay for their own hosting and services from the agreed date.

### Gate D — Accepted & Handed Over
- [ ] Signed client acceptance
- [ ] Credentials transferred; Code Square temporary access removed or documented
- [ ] Handover pack delivered
- [ ] Admin training completed
- [ ] Final invoice issued
- [ ] Retainer agreed, or explicitly declined in writing
- [ ] Internal retrospective held (§11) and case-study material captured

---

## 8. How work is broken into versions

`proposed`. This is a commercial position as much as a technical one, and it is already publicly stated on Facebook ("ابدأ بـ Landing Page أو MVP وشحن على مراحل").

**Rule: no project ships as one giant delivery.** Break every build into versions.

| Slice | What it is | Rule |
|---|---|---|
| **V1 / MVP** | The smallest thing a real user can do the real job with, end to end | Ships in ≤ 12 weeks. If V1 cannot ship in 12 weeks, V1 is too big — cut it. |
| **V2** | The next most valuable slice, chosen *after* seeing V1 used | Planned from real usage, not from the original wishlist |
| **V3+** | Ongoing improvement | Lives in the retainer |

**How to cut V1:** take the Must list from Discovery and ask of each item, "if this were missing, could a user still complete the whole job start to finish?" If yes, it is not V1. The Facebook booking-app example already says this publicly: 80% of users needed only search + book + confirm.

**Why this matters commercially:** a smaller V1 means an earlier launch, an earlier real success metric, an earlier case study, and an earlier retainer. A six-month V1 means six months with no proof and a client whose enthusiasm has run out.

---

## 9. Change request process

`proposed`. Nothing protects a fixed-price project except this.

**The rule: after Gate A, every change to scope is written down before it is worked on. No exceptions, including "small" ones.**

### The form — keep it to one screen

| Field | |
|---|---|
| CR number | CR-`<project>`-`<nn>` |
| Requested by | |
| Date | |
| What is being asked for | Plain description |
| Why | The business reason |
| Impact on cost | Amount, or "none" |
| Impact on schedule | Days added, or "none" |
| Impact on other work | What gets pushed back |
| Options | ① Do it now, at the cost and time above ② Defer to V2 ③ Swap — do it now and remove something of equal size from V1 ④ Decline |
| Decision | |
| Decided by | Client decision-maker |
| Date decided | |

### Rules
1. Work does not start on a CR until it is decided in writing. "Just start, we will sort the paperwork later" is how projects lose money.
2. **Option ③ (swap) is offered every time.** It lets a client change their mind without a budget conversation, and it keeps V1 shippable.
3. Small changes are not free — they are *cheap*. Track them anyway. Ten untracked "quick" changes are a month.
4. A rejected CR is not a lost opportunity; it goes on the V2 list, which is next quarter's revenue.
5. If CRs exceed **20% of the original scope value**, stop and re-plan the project instead of continuing to bolt things on.
6. Log every CR in a `Change Log` on the project. It is also the evidence when a client later asks why the project ran long.

---

## 10. Risk register practice

`proposed`. Started in Phase 1, reviewed weekly, never archived until Gate D.

| Field | |
|---|---|
| Risk | What could go wrong, stated as a specific event |
| Likelihood | Low / Medium / High |
| Impact | Low / Medium / High |
| Level | High if either Likelihood or Impact is High |
| Mitigation | What we do *now* to make it less likely |
| Contingency | What we do *if it happens anyway* |
| Owner | The function watching it |
| Status | Open / Mitigated / Occurred / Closed |

### Starter risks that apply to nearly every Code Square project

| Risk | Mitigation | Contingency | Owner |
|---|---|---|---|
| Client point-of-contact goes silent | Response window agreed at kickoff; weekly written note creates a record | Escalate to decision-maker after 3 working days; formally pause the project and notify that the schedule is moving | Account Management — TBD |
| A third-party integration does not work as documented | Verify every integration in Phase 2 before committing | Move it out of V1; deliver a manual workaround | Engineering — TBD |
| Client content and assets arrive late | Named dates at kickoff; placeholder content used so the build is not blocked | Launch with placeholders in a clearly marked section | Product — TBD |
| Scope creeps informally | Change request process, enforced from day one | Stop, run the CR backlog, re-baseline | Delivery owner — TBD |
| **One person holds all knowledge of the project** | Everything written into shared artifacts; no verbal-only decisions | Reconstruct from artifacts — which only works if the artifacts exist | Delivery owner — TBD |
| Payment milestone missed | Milestones tied to gates in the contract | Pause work at the gate, in writing, before continuing | Finance — TBD |
| Hosting, domain, or TLS certificate expires mid-project | Auto-renew on; renewal dates in the annual calendar (`[[Operating Cadence]]`) | The group has already lived this failure — see `[[Website and Technical Audit]]` | DevOps — TBD |

---

## 11. Escalation path

`proposed`. An escalation is not a complaint; it is a routing rule so a stuck thing gets unstuck fast.

| Level | Trigger | Who acts | Response target |
|---|---|---|---|
| **0 — Normal** | Ordinary question or blocker | Project team ↔ client point of contact | Within the agreed response window |
| **1 — Blocked** | Work has stopped and cannot restart without a decision | Delivery owner raises it to the client decision-maker, in writing | Same working day |
| **2 — At risk** | The schedule, budget, or success metric is now threatened | Delivery owner + Code Square leadership meet the client decision-maker | Within 2 working days |
| **3 — Escalated** | Relationship, payment, or contract dispute | Code Square leadership ↔ client leadership | Within 5 working days |

### Rules
- Escalate **early and quietly**. The bad version is escalating late and loudly.
- Every escalation is written: what is stuck, what it costs per day, the options, the decision needed, the deadline for that decision.
- Internal escalation exists too. Any team member may raise a project to the delivery owner at any time without asking permission. Say this out loud to the team — people who are new or junior default to waiting.
- Nothing is escalated in a group chat. Escalation goes to a named person.

---

## 12. Retrospective (internal, after every project)

30 minutes, held after Gate D, written down in the project folder. Four questions only:

1. What did we estimate, and what did it actually take?
2. What surprised us, and could a Phase 1 or Phase 2 question have caught it?
3. Which artifact did we skip, and what did skipping it cost?
4. What one change do we make to this file before the next project?

If a retrospective does not change a document, the process never improves and the same mistake is repeated at full price.

---

## 13. Open questions — must be answered by the founder

| # | Question | Blocks |
|---|---|---|
| 1 | Who owns each delivery function today? | Everything in this file |
| 2 | Do we accept the 4-phase model as canonical and retire the 5-stage graphic? | Public communication |
| 3 | What are the real payment milestones — deposit %, at Gate B, at Gate C, on acceptance? | Contract, cash flow |
| 4 | What is the standard warranty period? (30 days proposed) | Contract, `[[Support and Maintenance SLA]]` |
| 5 | What is the standard client response window? (2 working days proposed) | Kickoff, escalation |
| 6 | Is there a written contract template at all, and who reviewed it legally? | Every project |
| 7 | Where do project artifacts live? | `[[Tools Stack]]` |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Foundation Brief]] · [[Project Kickoff Checklist]] · [[Quality Standards and Handover]] · [[Support and Maintenance SLA]] · [[Org and Roles]] · [[Tools Stack]] · [[Operating Cadence]] · [[KPI Dashboard]] · [[Sales Playbook]] · [[Service Catalog]] · [[Pricing and Packaging]] · [[Website and Technical Audit]]
