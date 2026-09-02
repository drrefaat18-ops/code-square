---
date: 2026-09-02
type: operations
tags:
  - operations
  - org
  - roles
  - raci
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Org and Roles

## For future Claude

**The team roster is unknown.** Nobody has told this vault how many people work at Code Square, what they do, or how much time they have. So this file does **not** describe a team. It describes the **functions that must be owned** for the company to operate — a list of jobs that need a name against them, not a list of people.

One person can own several functions. That is normal and expected in a young company. What is not survivable is a function that **nobody** owns, because unowned functions do not fail loudly — they fail silently, months later, as a missed renewal, an unanswered enquiry, or an unpaid invoice.

Everywhere a person's name belongs, this file says `❓ NEEDS FROM FOUNDER:`. **Do not invent names, headcount, salaries, or capacity.** This unblocks blocker B5 by defining the structure; only the founder can fill the names in.

---

## How to use this file

1. Read the function list.
2. Against each function, write **one name**. Not two, not "the team".
3. Where the same name appears many times, that is fine — but §7 tells you which combinations are dangerous.
4. Where no name can be written, that function is **uncovered**. Mark it, and decide: accept the risk consciously, or make it someone's job today.
5. Re-read this file every quarter in the quarterly planning session — `[[Operating Cadence]]`.

**Rule: an owner is one named person, not a department and not "whoever is free".** Shared ownership is no ownership.

---

## 1. Terms

| Term | Plain meaning |
|---|---|
| **Function** | A job that must get done, described independently of who does it. |
| **Owner** | The single named person accountable for that function. They may not do all the work; they are answerable for it. |
| **Handoff** | The moment work passes from one function to another, and the thing that gets passed. |
| **RACI** | A grid saying, for each step: who **R**esponsible does it, who is **A**ccountable for the outcome, who is **C**onsulted, who is **I**nformed. |
| **Single point of failure** | Something that stops working if one specific person is unavailable. |
| **Utilisation** | The share of someone's working hours spent on paid client work. |
| **Bus factor** | How many people would have to disappear before the company cannot operate. If it is 1, that is the biggest risk on the list. |

---

## 2. The commercial functions

### 2.1 Marketing
**Purpose:** create demand, so the sales function has people to talk to.
**Responsibilities:** content and publishing on Facebook and the website · brand consistency (colours, voice, claims) · case studies · SEO and AI-engine visibility · running any paid spend · lead capture working end to end.
**Decisions it owns:** what gets published and when · which channel gets effort · creative direction within the brand system.
**Decisions it does NOT own:** positioning and pricing (founder) · what is claimed about clients (needs client permission).
**Hands off:** a qualified enquiry → Sales, with the source, the message, and any context captured.
**Minimum viable version:** publish one thing a week that points at one offer with one call to action. Nothing else. Sporadic high-volume posting with no offer is what produced 74 followers and zero enquiries (`stated`).
**❓ NEEDS FROM FOUNDER:** owner name.

### 2.2 Sales
**Purpose:** turn enquiries into signed, correctly-scoped, correctly-priced projects.
**Responsibilities:** responding to every enquiry inside the promised window · qualifying · running the diagnostic session · writing proposals · negotiating · closing · getting the contract signed and the deposit in · keeping the pipeline record current.
**Decisions it owns:** whether to pursue a lead · how to sequence a deal · what to include in a proposal within agreed pricing.
**Decisions it does NOT own:** discounting below the floor · accepting scope the delivery function has not sized · payment terms outside the standard.
**Hands off:** a won deal → Delivery, via the kickoff, carrying the scope, the promises made verbally, and the client context. **Every promise made during a sale must be written into the handoff.** Undocumented sales promises are the most common cause of a disputed project.
**Minimum viable version:** an inbox with a named owner, a response inside 24 hours (the site already promises this — `stated`), and a written record of every enquiry.
**❓ NEEDS FROM FOUNDER:** owner name. **Also: who owns the 24-hour website form SLA today?** This is currently an unowned public promise.

### 2.3 Account management
**Purpose:** keep existing clients, and grow them. Cheaper than finding new ones and the source of recurring revenue.
**Responsibilities:** the relationship after handover · retainer renewals · spotting V2 and expansion work · collecting testimonials and case-study material · being the escalation point.
**Decisions it owns:** how to handle a dissatisfied client · when to escalate to the founder.
**Hands off:** an expansion opportunity → Sales · a support issue → Support.
**Minimum viable version:** a calendar reminder to contact every past client once a quarter, and a note of what was said.
**❓ NEEDS FROM FOUNDER:** owner name.

---

## 3. The delivery functions

### 3.1 Product / Discovery
**Purpose:** work out what should be built before anyone builds it. This is where projects are saved or lost — the Facebook post already says it publicly: failure happens before the code (`stated`).
**Responsibilities:** discovery sessions · current-state mapping · user analysis · scope and out-of-scope lists · success metrics · prioritisation into V1/V2 · change requests · the weekly client demo.
**Decisions it owns:** what is in V1 · how a change request is presented · when to stop and re-plan.
**Hands off:** an approved scope → Design and Architecture.
**Minimum viable version:** run `[[Project Kickoff Checklist]]` and produce a written scope sheet with an explicit exclusions list. Nothing else in the toolkit matters as much.
**❓ NEEDS FROM FOUNDER:** owner name.

### 3.2 Design (UI/UX)
**Purpose:** make it usable and make it look like the company that claims Awwwards-tier work (`stated` — a claim that needs a standard behind it, see `[[Quality Standards and Handover]]`).
**Responsibilities:** user flows · wireframes · visual design · clickable prototype · design system and component consistency · Arabic and English layouts including right-to-left · accessibility basics.
**Decisions it owns:** visual and interaction choices within the brand system.
**Hands off:** approved designs → Frontend, with states specified (loading, empty, error, long text).
**Minimum viable version:** wireframes plus one styled screen approved by the client before any code is written.
**❓ NEEDS FROM FOUNDER:** owner name.

### 3.3 Frontend engineering
**Purpose:** build what the user touches.
**Responsibilities:** implementing designs · responsive and mobile-first behaviour · Arabic/English and right-to-left correctness · performance on slow connections · accessibility basics · browser testing.
**Hands off:** finished features → QA; integration needs → Backend.
**Minimum viable version:** one person who can take a design to a working, mobile-correct screen.
**❓ NEEDS FROM FOUNDER:** owner name.

### 3.4 Backend engineering
**Purpose:** build the part that holds the data and the rules.
**Responsibilities:** data model · business logic · APIs · authentication and permissions · third-party integrations · data validation · performance of queries.
**Decisions it owns:** technical implementation choices within the agreed architecture.
**Hands off:** APIs → Frontend, documented; deployment needs → DevOps.
**Minimum viable version:** one person who owns the data model and the rules, and writes them down.
**❓ NEEDS FROM FOUNDER:** owner name.

### 3.5 QA (quality assurance)
**Purpose:** find the problems before the client does. **This function exists whether or not there is a QA person** — if it is unassigned it defaults to the client, which is the most expensive place to find a defect.
**Responsibilities:** testing against the acceptance criteria · the pre-launch checklist in `[[Quality Standards and Handover]]` · cross-browser and mobile testing · regression checks · recording defects.
**Decisions it owns:** whether something meets the Definition of Done · defect severity.
**Minimum viable version:** **a different person than the one who built it** runs the pre-launch checklist. Not a QA hire — just not the author. People cannot see their own blind spots.
**❓ NEEDS FROM FOUNDER:** owner name.

### 3.6 DevOps / infrastructure
**Purpose:** keep things running and deployable, and prevent the failures nobody notices until they are catastrophic.
**Responsibilities:** hosting and environments · deployment · **TLS certificates and auto-renewal** · domains and renewals · backups **and tested restores** · uptime and error monitoring · security patching · incident response.
**Decisions it owns:** hosting choices within budget · deployment timing · when to roll back.
**Minimum viable version:** one person who knows where everything is hosted, holds the renewal calendar, and receives the alerts.
> This is the function whose absence already cost the group publicly: the expired TLS certificate on `mtechsquare.com` (`stated`, `[[Website and Technical Audit]]`). **If only one function gets an owner this week, make it this one.**
**❓ NEEDS FROM FOUNDER:** owner name.

---

## 4. The business functions

### 4.1 Finance
**Responsibilities:** invoicing · chasing payment · paying suppliers and salaries · recording expenses · monthly close · cash-flow forecast · pricing inputs and margin tracking · tax filings.
**Decisions it owns:** when to chase, when to pause work for non-payment (with the delivery owner).
**Minimum viable version:** a spreadsheet with money in, money out, and cash on hand, updated weekly. **A young company does not die of bad strategy; it dies of running out of cash while profitable on paper.**
**❓ NEEDS FROM FOUNDER:** owner name.

### 4.2 Admin and operations
**Responsibilities:** the annual calendar of renewals, licences, and filings · document and file organisation · tool subscriptions and who has access · access reviews · meeting notes landing in the vault.
**Minimum viable version:** one calendar, one file location, one list of subscriptions.
**❓ NEEDS FROM FOUNDER:** owner name.

### 4.3 Legal and contracts
**Responsibilities:** the contract template · client contracts and amendments · intellectual property terms · case-study permissions · privacy policy and terms of service (the site links to both — **confirm they have content**, `stated` concern) · supplier agreements.
**Decisions it owns:** whether a client's contract changes are acceptable.
**Minimum viable version:** one lawyer-reviewed contract template used every time, with a change request clause and an acceptance clause.
**❓ NEEDS FROM FOUNDER:** owner name, and whether any legal review has happened at all.

### 4.4 People / HR
**Responsibilities:** hiring · onboarding · contracts for staff and freelancers · capacity planning · training · retention.
**Minimum viable version:** a written onboarding checklist so a new person is productive in days, and a note of who knows what — which is also the continuity register in §6.
**❓ NEEDS FROM FOUNDER:** owner name.

---

## 5. RACI for the five recurring processes

**R** = does the work · **A** = accountable, one per row · **C** = consulted before · **I** = told after.

Every cell below is `TBD — assign`. Fill them in with the founder before this file is useful.

### 5.1 A new lead arrives

| Step | R | A | C | I |
|---|---|---|---|---|
| Enquiry received and logged | TBD — assign | TBD — assign | — | TBD — assign |
| First response within 24h | TBD — assign | TBD — assign | — | — |
| Qualification | TBD — assign | TBD — assign | TBD — assign (Delivery) | — |
| Diagnostic session run | TBD — assign | TBD — assign | TBD — assign | — |
| Proposal written and priced | TBD — assign | TBD — assign | TBD — assign (Delivery, Finance) | — |
| Contract sent and signed | TBD — assign | TBD — assign | TBD — assign (Legal) | TBD — assign |
| Deposit confirmed | TBD — assign | TBD — assign | — | TBD — assign |
| Lost deal recorded with reason | TBD — assign | TBD — assign | — | TBD — assign |

### 5.2 A new project starts

| Step | R | A | C | I |
|---|---|---|---|---|
| Sales → Delivery handoff | TBD — assign | TBD — assign | TBD — assign | — |
| Kickoff checklist run | TBD — assign | TBD — assign | — | TBD — assign |
| Discovery and scope sheet | TBD — assign | TBD — assign | TBD — assign | — |
| Gate A sign-off | TBD — assign | TBD — assign | TBD — assign (client) | TBD — assign |
| Architecture and design | TBD — assign | TBD — assign | TBD — assign | — |
| Gate B sign-off | TBD — assign | TBD — assign | TBD — assign (client) | TBD — assign |
| Build and weekly demos | TBD — assign | TBD — assign | — | TBD — assign |
| Change requests decided | TBD — assign | TBD — assign | TBD — assign (Finance) | TBD — assign |
| Pre-launch checklist | TBD — assign | TBD — assign | — | TBD — assign |
| Launch and handover | TBD — assign | TBD — assign | TBD — assign | TBD — assign |
| Acceptance and final invoice | TBD — assign | TBD — assign | — | TBD — assign |

### 5.3 A support ticket arrives

| Step | R | A | C | I |
|---|---|---|---|---|
| Ticket logged | TBD — assign | TBD — assign | — | — |
| Severity assigned | TBD — assign | TBD — assign | — | TBD — assign |
| Client acknowledged within target | TBD — assign | TBD — assign | — | — |
| Fixed or worked around | TBD — assign | TBD — assign | — | TBD — assign |
| S1 hourly updates | TBD — assign | TBD — assign | — | TBD — assign |
| Billable work quoted before doing it | TBD — assign | TBD — assign | TBD — assign (Finance) | — |
| Monthly SLA report sent | TBD — assign | TBD — assign | — | TBD — assign |

### 5.4 A case study is produced

| Step | R | A | C | I |
|---|---|---|---|---|
| Permission agreed **at kickoff** | TBD — assign | TBD — assign | TBD — assign (Legal) | TBD — assign |
| Numbers collected at 30-day review | TBD — assign | TBD — assign | TBD — assign (client) | — |
| Testimonial requested | TBD — assign | TBD — assign | — | — |
| Draft written within 5 working days | TBD — assign | TBD — assign | TBD — assign (Delivery) | — |
| Client approves the draft | TBD — assign | TBD — assign | TBD — assign (client) | — |
| Published to site and social | TBD — assign | TBD — assign | — | TBD — assign |

### 5.5 Monthly close

| Step | R | A | C | I |
|---|---|---|---|---|
| All invoices issued | TBD — assign | TBD — assign | — | — |
| Receivables chased | TBD — assign | TBD — assign | — | TBD — assign |
| Expenses recorded | TBD — assign | TBD — assign | — | — |
| Cash position and runway updated | TBD — assign | TBD — assign | — | TBD — assign |
| KPI dashboard updated | TBD — assign | TBD — assign | TBD — assign | TBD — assign |
| Monthly business review held | TBD — assign | TBD — assign | — | TBD — assign |
| Renewals due next month checked | TBD — assign | TBD — assign | — | TBD — assign |

---

## 6. Single points of failure — the continuity register

Fill this in honestly. It is the most useful table in this file.

| # | Thing | Who is the only person who can do it | Written down? | Backup | Action |
|---|---|---|---|---|---|
| 1 | Deploying to production | ❓ NEEDS FROM FOUNDER | | TBD | Write a runbook, train a second person |
| 2 | Domain and hosting account access | ❓ NEEDS FROM FOUNDER | | TBD | Put in a shared password manager vault |
| 3 | TLS certificate renewal | ❓ NEEDS FROM FOUNDER | | TBD | Automate, then alert 30 days out |
| 4 | Client relationships | ❓ NEEDS FROM FOUNDER | | TBD | Every client has a named backup contact |
| 5 | The bank account and payments | ❓ NEEDS FROM FOUNDER | | TBD | Second signatory or documented process |
| 6 | Knowledge of each live client system | ❓ NEEDS FROM FOUNDER | | TBD | Handover pack per project, kept current |
| 7 | The code repositories | ❓ NEEDS FROM FOUNDER | | TBD | Organisation account, not a personal one |
| 8 | Facebook page and website admin access | ❓ NEEDS FROM FOUNDER | | TBD | Two admins minimum |

**Rule:** any row where the answer is one person and "written down?" is no is an active risk, not a theoretical one. Fix the two cheapest rows this month.

---

## 7. Which hats can safely be worn by one person

Because a small company must combine roles, this matters more than the org chart.

| Combination | Verdict |
|---|---|
| Marketing + Sales | Fine, and common |
| Sales + Account management | Fine |
| Product/Discovery + Design | Fine, often better |
| Frontend + Backend | Fine |
| Backend + DevOps | Fine |
| Finance + Admin | Fine |
| **Builder + QA on the same work** | ⚠️ Avoid. Nobody proofreads their own work well. If unavoidable, use the written checklist and do it a day later, not the same evening |
| **Sales + Delivery estimating, unchecked** | ⚠️ Risky. The person who wants the deal should not be the only one sizing it. A second opinion on every estimate, even a 10-minute one |
| **Finance + the person who approves their own spending** | ⚠️ Basic control. Someone else sees the numbers monthly, even informally |
| **Everything, one person** | This is a real situation, not a failure — but then §6 must be filled in and written down, because the bus factor is 1 |

---

## 8. Hiring order and the trigger for each

`proposed`. **Hire against a trigger, never against optimism.** The trigger is what tells you the hire pays for itself.

| # | Hire | Trigger — hire when this is true | Why this order |
|---|---|---|---|
| 1 | **Delivery / project owner** (product + QA + client comms) | Two or more projects running at once, or a client complains about communication | The founder cannot both sell and run delivery. This is the first thing to break |
| 2 | **Engineer** (whichever of frontend/backend is the bottleneck) | Work is being turned down, or promised dates are being missed on capacity alone — not on scope | Only after delivery is organised; adding builders to a disorganised process makes it slower, not faster |
| 3 | **Marketing / content** | The offer and the case studies exist, and the constraint is publishing volume, not message quality | Hiring this before the message is fixed just publishes the wrong thing faster |
| 4 | **Support** | Ticket volume regularly breaks SLA targets, or support is interrupting build work more than a few hours a week | Support interrupting engineers is the hidden cost most companies never measure |
| 5 | **Second engineer / specialist** | A named skill gap is blocking work that has already been sold | — |
| 6 | **Finance / admin, part-time or outsourced** | Invoicing or filings are late, or the founder spends more than half a day a week on admin | Outsource this before employing it |

### Before any hire, in order
1. **Can the work be removed?** Ten one-off proposals that are never won are not a hiring case.
2. **Can it be automated or templated?** A proposal template beats a proposal writer.
3. **Can it be outsourced or freelanced?** Freelance first, employ once the need is proven for three consecutive months.
4. **Then hire.**

**❓ NEEDS FROM FOUNDER:** current headcount, who does what today, who is full-time vs part-time, whether the founder is full-time on Code Square (this is already an open blocker in `[[Foundation Brief]]` §10), and the monthly budget available for people.

---

## 9. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | Who works here, and what does each person actually do today? | Every `TBD` in this file, and every `owner:` field in the vault |
| 2 | Is the founder full-time on Code Square? | Capacity, hiring order |
| 3 | Who owns the 24-hour website form response promise? | A live public commitment with no owner |
| 4 | Who has access to the domain, hosting, bank, Facebook, and repositories? | §6, and continuity |
| 5 | Are there freelancers, and are they contracted? | Legal, capacity |
| 6 | Is there a legal entity, and in whose name? | Contracts, tax |
| 7 | What is the monthly people budget? | Hiring order |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Foundation Brief]] · [[Delivery Process]] · [[Project Kickoff Checklist]] · [[Quality Standards and Handover]] · [[Support and Maintenance SLA]] · [[Operating Cadence]] · [[Tools Stack]] · [[KPI Dashboard]] · [[Sales Playbook]] · [[Website and Technical Audit]]
