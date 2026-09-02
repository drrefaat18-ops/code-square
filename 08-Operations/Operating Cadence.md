---
date: 2026-09-02
type: operations
tags:
  - operations
  - cadence
  - meetings
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Operating Cadence

## For future Claude

The rhythm of the company: which meetings happen, how often, who is in them, what goes in, what comes out, and where the notes live in this vault. Plus the annual calendar of things that expire — the category of failure that already cost the group publicly (`[[Website and Technical Audit]]`: expired TLS certificate).

All `proposed` (2026-09-02). All attendees are **functions**, not people — roster unknown, see `[[Org and Roles]]`.

**Scale this to the team you actually have.** If Code Square is two people, the daily standup is a five-minute message and the weekly reviews merge into one 45-minute meeting. Do not run a five-meeting week for a three-person company. What must survive at any size is: *someone looks at money monthly, someone looks at the pipeline weekly, someone looks at renewals annually.*

---

## 1. Terms

| Term | Plain meaning |
|---|---|
| **Cadence** | The fixed rhythm at which something recurs. Fixed beats "when we get a chance", because "when we get a chance" is never. |
| **Standup** | A short daily check where each person says what they did, what they will do, and what is blocking them. |
| **Pipeline** | All the potential deals currently in progress, and what stage each is at. |
| **Blocker** | Something stopping work that the person cannot resolve alone. |
| **Runway** | How many months the company can keep operating with the cash it has. |
| **Retrospective** | A look back at how the work went, in order to change something. |

---

## 2. The rhythm at a glance

| Cadence | Forum | Length | Question it answers |
|---|---|---|---|
| Daily | Standup | 10 min | What is blocked today? |
| Weekly | Commercial review | 30 min | Where is the next project coming from? |
| Weekly | Delivery review | 45 min | Will we deliver what we promised? |
| Monthly | Business review | 90 min | Are we healthy, and are we making money? |
| Quarterly | Planning | half day | Are we doing the right things at all? |
| Annually | Calendar review | 2 hours | What expires this year and who owns it? |

---

## 3. Daily standup

| | |
|---|---|
| **Purpose** | Surface blockers within a day of them appearing, not a week |
| **Attendees** | Everyone doing delivery work |
| **Length** | 10 minutes, standing or in a chat thread — a written standup is fine and often better |
| **Inputs** | The task board |
| **Agenda** | Each person: ① what I finished ② what I am doing today ③ what is blocking me |
| **Outputs** | A list of blockers, each with an owner and a resolution path |
| **Notes go to** | Nowhere. Standups are not minuted. Blockers go on the task board |

**Rules:** no problem-solving in the standup — take it offline with the two people who need to be there. No status theatre for the founder's benefit. If nobody ever says "blocked", the standup is not working; people are being polite.

---

## 4. Weekly commercial review

| | |
|---|---|
| **Purpose** | Keep the pipeline alive; nothing kills a young agency faster than finishing a project with nothing behind it |
| **Attendees** | Sales, Marketing, Account management, founder |
| **Length** | 30 minutes |
| **Inputs** | Enquiry log · pipeline list · last week's published content · `[[KPI Dashboard]]` marketing and sales rows |

### Agenda
| Min | Item |
|---|---|
| 0–5 | New enquiries this week — count, source, and whether every one was answered inside 24 hours |
| 5–15 | Pipeline walk: every open deal, its stage, next step, and next-step date. **Any deal with no next step is not a deal** |
| 15–20 | Deals won and lost, with the reason for each loss recorded |
| 20–25 | What we published, what it produced, what we publish next week |
| 25–30 | One action each for Marketing and Sales |

**Outputs:** updated pipeline · named next steps with dates · next week's publishing plan.
**Notes go to:** `09-Commercial/Weekly Commercial Review/YYYY-MM-DD.md` — `❓ NEEDS FROM FOUNDER:` confirm the folder.

---

## 5. Weekly delivery review

| | |
|---|---|
| **Purpose** | Catch slipping projects while a fix is still cheap |
| **Attendees** | Delivery owner, everyone building, QA function |
| **Length** | 45 minutes |
| **Inputs** | Project boards · risk registers · change logs · support ticket queue |

### Agenda
| Min | Item |
|---|---|
| 0–10 | Project by project: on track / at risk / late, and **the reason** — "at risk" with no reason is not a status |
| 10–20 | Risk registers: any risk moved to High, any risk that occurred |
| 20–28 | Change requests raised, decided, and pending |
| 28–36 | Support tickets: open, ageing, SLA breaches, repeat issues |
| 36–42 | Client health: anyone gone quiet, anyone unhappy, anyone with a demo missed twice |
| 42–45 | Actions with owners |

**Outputs:** status per project · escalations raised · actions.
**Notes go to:** `07-Delivery/Weekly Delivery Review/YYYY-MM-DD.md`.

**Rule: a project reported "on track" three weeks running and then late in week four means the review is not honest.** Ask specifically what has *not* been demonstrated on staging yet.

---

## 6. Monthly business review

| | |
|---|---|
| **Purpose** | The only meeting where the whole company is looked at as a business |
| **Attendees** | Founder plus every function owner |
| **Length** | 90 minutes, in the first week of the month |
| **Inputs** | `[[KPI Dashboard]]` fully populated · monthly close from Finance · SLA report · project retrospectives |

### Agenda
| Min | Item | Decision it produces |
|---|---|---|
| 0–15 | Financials: revenue, costs, margin, cash on hand, **runway in months**, receivables overdue | Whether spending changes |
| 15–30 | Commercial: enquiries, qualified enquiries, proposals, win rate, average deal size | Where marketing effort goes |
| 30–45 | Delivery: projects delivered, on-time rate, scope-change rate, defects that escaped to production | What changes in the process |
| 45–55 | Support: ticket volume, SLA compliance, repeat issues | Whether the SLA is deliverable as written |
| 55–65 | Client health and retainer renewals due | Retention actions |
| 65–75 | People: capacity, utilisation, who is overloaded, hiring triggers from `[[Org and Roles]]` §8 | Whether to hire |
| 75–85 | The month's biggest lesson, and the one document we change because of it | A named document edit |
| 85–90 | Three priorities for next month | Written, with owners |

**Outputs:** updated KPI dashboard · three named priorities · at least one document changed.
**Notes go to:** `08-Operations/Monthly Business Review/YYYY-MM.md`.

**Rule: if a monthly review changes no document and sets no priority, it was a status meeting and should be shortened.**

---

## 7. Quarterly planning

| | |
|---|---|
| **Purpose** | Step back from execution and check direction |
| **Attendees** | Founder plus all function owners |
| **Length** | Half a day, off the tools |
| **Inputs** | Three monthly reviews · `[[Foundation Brief]]` · `[[Open Questions and Decisions Needed]]` · `[[KPI Dashboard]]` trends |

### Agenda
| Item | Purpose |
|---|---|
| Last quarter vs what we said we would do | Honest scoring, not a narrative |
| Beachhead check | Is the chosen segment producing enquiries? `[[Foundation Brief]]` §4 says pick one — has it been picked, and is it working? |
| Positioning and message check | Still true? Still differentiated? |
| Pricing review | Are we winning too easily (underpriced) or losing on price every time (mispositioned)? |
| Capacity and hiring | Against the triggers in `[[Org and Roles]]` §8 |
| **Re-read `[[Org and Roles]]`** | Fill in newly-known owners; re-check the single-points-of-failure register |
| Open questions | Close as many blockers as possible — this is the meeting where TBDs get decided |
| Next quarter: three goals | With a number against each |

**Outputs:** three quarterly goals · decisions recorded against open questions · updated foundation documents.
**Notes go to:** `08-Operations/Quarterly Planning/YYYY-Qn.md`.

---

## 8. Annual calendar of recurring obligations

**This is the highest-value table in this file.** Everything on it fails silently and expensively. Every owner is `TBD — assign`; assign them before anything else in this document.

### Always-on technical renewals

| Item | Frequency | Alert before | Owner |
|---|---|---|---|
| **TLS certificate — all Code Square and client domains** | Per certificate (often 90 days) | **30 days, plus auto-renew enabled** | TBD — assign |
| **Domain registrations** | Annual | 60 days, plus auto-renew enabled | TBD — assign |
| Hosting and server subscriptions | Monthly or annual | 30 days | TBD — assign |
| Apple Developer account | Annual | 30 days | TBD — assign |
| Google Play developer account | One-off, verify status annually | — | TBD — assign |
| Third-party API and service plans (maps, payments, email, SMS) | Varies | 30 days | TBD — assign |
| Software subscriptions and tool licences | Monthly or annual | 30 days | TBD — assign |
| **Backup restore test** | Quarterly | — | TBD — assign |
| **Access review** — who still has access to what | Quarterly | — | TBD — assign |
| Security and dependency update sweep | Monthly | — | TBD — assign |

### Business and legal — Egypt

`❓ NEEDS FROM FOUNDER:` the vault does not know the legal entity, its registration type, or its tax obligations. **Confirm each row with an accountant before relying on it.** Dates and frequencies below are placeholders to be replaced, not advice.

| Item | Frequency | Owner | Status |
|---|---|---|---|
| Commercial registration renewal | `TBD` | TBD — assign | ❓ confirm |
| Tax card / tax registration | `TBD` | TBD — assign | ❓ confirm |
| VAT returns, if registered | `TBD` — commonly monthly | TBD — assign | ❓ confirm |
| Annual income tax return | Annual | TBD — assign | ❓ confirm |
| Payroll tax and social insurance filings, if there are employees | `TBD` — commonly monthly | TBD — assign | ❓ confirm |
| Professional or industry licences | `TBD` | TBD — assign | ❓ confirm |
| Insurance renewals (if any) | Annual | TBD — assign | ❓ confirm |
| Bank account and signatory review | Annual | TBD — assign | ❓ confirm |
| Client contract renewals | Per contract | TBD — assign | — |
| Retainer renewals | Per client, 30-day reminder | TBD — assign | — |
| Supplier and freelancer agreements | Annual | TBD — assign | — |

### Internal, calendarised

| Item | When | Owner |
|---|---|---|
| Quarterly planning | Q1–Q4, first week | TBD — assign |
| Annual review of every document in this vault | January | TBD — assign |
| Egyptian public holiday list published to clients | January | TBD — assign |
| Ramadan working hours published to clients | Before Ramadan | TBD — assign |
| Pricing review | Annual, in quarterly planning | TBD — assign |
| Continuity register review (`[[Org and Roles]]` §6) | Quarterly | TBD — assign |

**How to run this table:** every row becomes a recurring calendar entry with a named person and a reminder, in one shared calendar. Not a note, not a memory, not this file. A file nobody opens is not a control.

---

## 9. Where notes live

| Forum | Location |
|---|---|
| Standup | Not minuted — blockers go to the task board |
| Weekly commercial review | `09-Commercial/Weekly Commercial Review/YYYY-MM-DD.md` |
| Weekly delivery review | `07-Delivery/Weekly Delivery Review/YYYY-MM-DD.md` |
| Monthly business review | `08-Operations/Monthly Business Review/YYYY-MM.md` |
| Quarterly planning | `08-Operations/Quarterly Planning/YYYY-Qn.md` |
| Project retrospectives | In the project folder |
| Decisions with lasting effect | `[[Open Questions and Decisions Needed]]`, then into the relevant document |

`❓ NEEDS FROM FOUNDER:` confirm these folder names match the vault's actual structure.

**Every meeting note uses the same four headings:** Decisions · Actions (owner + date) · Risks · Open questions. Nothing else. Long minutes are not read, and a decision buried in prose is a decision nobody can find.

---

## 10. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | How many people are there — which of these meetings makes sense? | The whole cadence |
| 2 | What are the actual Egyptian legal and tax obligations for this entity? | §8, penalty exposure |
| 3 | Which shared calendar holds the renewals? | `[[Tools Stack]]` |
| 4 | Who owns the renewal calendar? | The most preventable failure category |
| 5 | Do the folder paths in §9 exist? | Where notes go |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Org and Roles]] · [[KPI Dashboard]] · [[Tools Stack]] · [[Delivery Process]] · [[Support and Maintenance SLA]] · [[Quality Standards and Handover]] · [[Foundation Brief]] · [[Website and Technical Audit]]
