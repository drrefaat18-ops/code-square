---
date: 2026-09-02
type: sla
tags:
  - delivery
  - support
  - sla
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Support and Maintenance SLA

## For future Claude

> ## 🔴 Read this first — the claim already exists, the document does not
>
> The website currently advertises **"SLA Guarantees"** and the Facebook SaaS and support infographics advertise **"99.9% uptime"** (both `stated`, from `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]` and `[[2026-09-02 - Facebook Page Evidence]]`).
>
> **There is no SLA document behind either claim. No severity levels, no response targets, no monitoring, no reporting, nobody named.** Meanwhile the group's own site served an expired TLS certificate — meaning its own uptime, as experienced by a visitor, was effectively 0% for the duration.
>
> A promised service level that nobody measures is not a marketing weakness, it is a legal and reputational exposure. There are exactly two honest options:
>
> **① Build it.** Adopt this document, staff it, measure it, report it. Then the claim is true.
> **② Stop claiming it.** Remove "SLA Guarantees" and "99.9% uptime" from the website and from every future creative, today, until option ① is real.
>
> Both claims are on the banned-phrases list in `[[Foundation Brief]]` §5 *until a real SLA exists and is honoured*. **Option ② costs nothing and takes an hour. Do it this week regardless, then build option ① at leisure.** Do not leave the claim standing while the document is a draft.

Everything below is `proposed` (2026-09-02). Owners are **functions**, not people — the roster is unknown. Numbers in the target tables are starting proposals to be confirmed by the founder against real capacity, not commitments already made.

---

## 1. Terms

| Term | Plain meaning |
|---|---|
| **SLA** (Service Level Agreement) | A written promise about how fast we respond and fix, with what happens if we miss. |
| **Severity** | How badly the problem hurts the client's business. Not how annoyed they are. |
| **Response time** | How long until a human acknowledges the ticket and says what happens next. Not the fix. |
| **Resolution time** | How long until the problem is fixed, or a workaround is in place. |
| **Workaround** | A temporary way to keep working while the real fix is built. Counts as resolution for severity purposes if agreed with the client. |
| **Uptime** | The percentage of time the system is available. 99.9% allows about 43 minutes of downtime per month. 99% allows about 7 hours. |
| **Business hours** | The hours during which the response clock runs. |
| **Ticket** | One recorded support request with an ID. If it is not a ticket, it did not happen and cannot be measured. |
| **Retainer** | A recurring monthly fee that buys a defined support and maintenance service. |

---

## 2. Severity levels

Severity is set by **impact on the client's business**, by Code Square, using this table — not by whoever shouts loudest. If the client disagrees, they may escalate the severity classification itself (§7).

| Sev | Name | Definition | Examples |
|---|---|---|---|
| **S1** | **Critical** | The system is down, or a core business function is completely unusable, and there is no workaround. Money or safety is being lost right now. | Site or app entirely unreachable · payments failing for everyone · data loss in progress · security breach · **TLS certificate expired** · login broken for all users |
| **S2** | **High** | A core function is broken or severely degraded for many users, but the business can still partially operate. | Booking form fails for one browser · crew placement dashboard shows wrong numbers · emails not sending · one major feature down · site very slow for everyone |
| **S3** | **Medium** | A non-core function is broken, or a core function is broken for a small number of users, with a workaround available. | A report exports wrong · a filter returns bad results · a page renders badly on one device · admin task requires a manual step |
| **S4** | **Low** | Cosmetic issues, small annoyances, questions, and requests for information. | Typo · spacing off · "how do I do X?" · a request for a small content change |

**Not covered by severity at all:** new features and changes of mind. Those are change requests and are quoted separately — `[[Delivery Process]]` §9. A client calling a new feature "urgent" does not make it S1.

---

## 3. Support tiers

Three tiers so the client buys what they actually need. **Prices are `TBD` — the founder must set them (`[[Pricing and Packaging]]`).** Do not quote until set.

| | **Essential** | **Standard** | **Partner** |
|---|---|---|---|
| Intended for | Small sites, low-stakes systems | Business systems people work in daily | Systems the business cannot trade without |
| Support hours | Business hours | Business hours | Business hours + on-call for S1 |
| Channels | Email / ticket form | Email / ticket + WhatsApp | Email / ticket + WhatsApp + phone |
| Included hours per month | `TBD` | `TBD` | `TBD` |
| Monitoring | Uptime | Uptime + errors | Uptime + errors + performance |
| Backups | Weekly | Daily | Daily + verified restore test quarterly |
| Reporting | Quarterly | Monthly | Monthly + quarterly review meeting |
| Named contact | No | Yes | Yes, with a named backup |
| Uptime commitment | Best effort, no figure | `TBD` | `TBD` |
| Price / month | `TBD` | `TBD` | `TBD` |

**Rule: do not publish an uptime figure on any tier until it has been measured for 90 days by a monitoring tool.** Measure first, then promise. This is exactly how the "99.9%" claim came to be unsupported.

---

## 4. Response and resolution targets

Clock runs during **support hours only** (§5) unless the tier includes on-call.

### Response (a human acknowledges and states next steps)

| Sev | Essential | Standard | Partner |
|---|---|---|---|
| S1 | 8 business hours | 4 business hours | **1 hour, 24/7** |
| S2 | 1 business day | 8 business hours | 4 business hours |
| S3 | 3 business days | 2 business days | 1 business day |
| S4 | 5 business days | 3 business days | 2 business days |

### Resolution, or an agreed workaround

| Sev | Essential | Standard | Partner |
|---|---|---|---|
| S1 | 3 business days | 1 business day | **8 hours, continuous effort** |
| S2 | 5 business days | 3 business days | 1 business day |
| S3 | Next maintenance window | 10 business days | 5 business days |
| S4 | Best effort | Next maintenance window | 10 business days |

**Honesty rules on these numbers:**
- These are **`proposed` starting points**. Before signing anyone to the Partner tier, confirm a real human can actually be reached in one hour. If the answer is "only if that person is awake and not on holiday", the tier is not deliverable yet — sell Standard.
- Resolution targets do not apply where the cause is outside our control: a hosting provider outage, a third-party service failure, or the client's own change. We still respond, communicate, and drive the fix; the clock is paused and the pause is recorded on the ticket.
- The clock pauses while we are waiting on the client for information or access, and the pause is visible on the ticket.

---

## 5. Support hours and channels

| | |
|---|---|
| **Business hours** | `TBD — set`. Proposal: Sunday–Thursday, 09:00–17:00 Egypt time |
| **Weekend** | Friday and Saturday outside business hours, S1 only on the Partner tier |
| **Public holidays** | Egyptian public holidays; the list published to clients each January |
| **Ramadan** | Reduced hours, published to clients before Ramadan begins |
| **Gulf clients** | Jeddah and Riyadh are `stated` service areas — confirm whether their working week (Sun–Thu) and holidays are handled by the same schedule |

### Channels, in order of preference

1. **Ticket form or support email** — the only channel where the SLA clock officially starts. Everything ends up here.
2. **WhatsApp** (Standard and Partner) — convenient for the client; **every WhatsApp request is copied into a ticket by us**, not by the client. An untracked WhatsApp message is invisible to the SLA and to `[[KPI Dashboard]]`.
3. **Phone** (Partner, S1 only) — followed by a ticket within the hour.

> **Rule: no ticket, no SLA.** Say this to clients plainly and kindly at handover, and then do the ticket-creation work for them rather than arguing about it. Support that lives only in chat cannot be measured, cannot be staffed, and cannot be billed.

---

## 6. What is included vs what is billable

### Included in the retainer
- Fixing defects in delivered work
- Security patches and dependency updates
- Hosting, domain, and **TLS certificate renewal monitoring**
- Backup running and verification
- Uptime, error, and performance monitoring
- Small content edits within the included hours
- Answering how-to questions
- Monthly reporting
- Escalation and incident communication

### Billable, quoted separately
- New features and new pages or screens
- Design changes
- Third-party licence and service fees (hosting, gateways, APIs)
- Data migration
- Training sessions beyond the one at handover
- Work caused by the client's own changes to the system
- Work caused by a third party the client engaged
- Recovery from an incident caused by client-side credential loss or misuse
- Anything beyond the included hours in the month

### Explicitly not included
- Support for software Code Square did not build, unless separately agreed
- 24/7 coverage on any tier below Partner
- Guaranteed availability of a specific individual
- Anything the client considers "urgent" that is actually a new feature

**Rule on included hours:** unused hours do not roll over. Overage is quoted before it is worked, never billed as a surprise.

---

## 7. Escalation

| Level | Trigger | Who | Target |
|---|---|---|---|
| **1** | Ticket approaching its response or resolution target | Support function alerts the delivery owner | Before the target is missed, not after |
| **2** | Target missed, or S1 open beyond target | Delivery owner contacts the client directly with a status, a plan, and a new committed time | Within 2 hours of the miss |
| **3** | Repeated misses, or a client dispute | Code Square leadership ↔ client decision-maker | Within 1 business day |
| **Severity dispute** | Client disagrees with the severity we assigned | Delivery owner reviews against §2 with the client; if still disputed, treat it one level higher until resolved | Same business day |

**S1 communication rule:** during an S1, the client gets an update every hour whether or not there is news. Silence during an outage destroys more trust than the outage.

---

## 8. Monitoring and backup commitments

These are the promises that make an uptime claim possible at all.

| Commitment | What it means | Owner |
|---|---|---|
| **Uptime monitoring** | An external service checks the system every 1–5 minutes and alerts a **named person** on failure | DevOps — TBD |
| **Error monitoring** | Application errors captured and alerted, not discovered by the client | DevOps — TBD |
| **Performance monitoring** | Page load and response times tracked over time (Partner tier) | DevOps — TBD |
| **TLS expiry alerting** | Alert 30 days before expiry, plus auto-renewal enabled — see `[[Quality Standards and Handover]]` §2.10 | DevOps — TBD |
| **Domain expiry alerting** | Auto-renew on, plus a calendar entry in `[[Operating Cadence]]` | Admin — TBD |
| **Backups** | Per tier; stored off the production server | DevOps — TBD |
| **Restore testing** | A real restore performed and documented — quarterly on Partner, annually otherwise. **An untested backup is a rumour.** | DevOps — TBD |
| **Dependency and security updates** | Reviewed monthly, applied on a schedule, urgent security patches applied out of schedule | Engineering — TBD |

**Applies to Code Square's own properties on the same schedule as clients'.** The group has already demonstrated what happens when it does not.

---

## 9. Reporting

### Monthly client report — one page, sent by the 5th

| Section | Content |
|---|---|
| Uptime | Percentage, and any incidents with duration and cause |
| Tickets | Opened, closed, still open, split by severity |
| SLA compliance | Percentage of tickets that met their response and resolution targets, and an honest note on any miss |
| Hours used | Included hours consumed vs available |
| Maintenance done | Updates, patches, backups verified |
| Risks and recommendations | What we think they should do next |

**Report the misses.** A report that only ever shows 100% is not believed, and it is usually not true.

### Internal, weekly
Ticket queue, ageing tickets, SLA breaches, and repeat issues reviewed in the weekly delivery review — `[[Operating Cadence]]`. Feeds `[[KPI Dashboard]]`.

---

## 10. Renewal, change, and exit

| Item | Terms (`proposed`) |
|---|---|
| **Initial term** | 12 months, or 3 months on Essential |
| **Renewal** | Automatic, with a written reminder 30 days before |
| **Price change** | Only at renewal, with 60 days' written notice |
| **Tier change** | Upgrade any time, effective immediately. Downgrade at renewal only |
| **Client exit notice** | 30 days |
| **Code Square exit notice** | 60 days, and we do not leave a client mid-incident |
| **On exit** | Full credential and documentation handover per `[[Quality Standards and Handover]]` §3; final report; access removed on the agreed date |
| **Non-payment** | Support paused after `TBD` days' notice in writing. **Monitoring, backups, and certificate renewal continue during any dispute** — never let a commercial argument take a client's business offline |

### Service credits
`TBD — decide`. Options:
- **① None.** Simplest. Then the word "guarantee" must not be used anywhere.
- **② Credits.** e.g. 5% of the monthly fee per missed S1 target, capped at 50%. Costs little, and it is the thing that makes "guarantee" an honest word.

**Recommendation:** option ② on the Partner tier only, once targets have been measured for 90 days. Until then, no tier uses the word "guarantee".

---

## 11. What to do this week

- [ ] **Remove "SLA Guarantees" and "99.9% uptime" from the website and all creatives** — one hour of work, removes a standing exposure
- [ ] Decide: build the SLA, or stay silent about service levels
- [ ] Assign an owner to the support function — `[[Org and Roles]]`
- [ ] Choose a ticketing tool and a monitoring tool — `[[Tools Stack]]`
- [ ] Turn on uptime monitoring for Code Square's own site and start collecting the 90 days of data that any future uptime number must be based on
- [ ] Fix and auto-renew the group's TLS certificate — `[[Website and Technical Audit]]`

---

## 12. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | Do we remove the claims, or build the service? | Website copy, legal exposure |
| 2 | What are business hours, and how are Gulf clients handled? | Every target in §4 |
| 3 | Can a human genuinely respond to an S1 within 1 hour today? | Whether the Partner tier can be sold |
| 4 | Retainer prices and included hours per tier | `[[Pricing and Packaging]]` |
| 5 | Which ticketing and monitoring tools? | `[[Tools Stack]]` |
| 6 | Service credits: yes or no? | Whether "guarantee" may be used |
| 7 | Who is the named support owner, and who is the backup? | `[[Org and Roles]]` |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Delivery Process]] · [[Quality Standards and Handover]] · [[Project Kickoff Checklist]] · [[Org and Roles]] · [[Tools Stack]] · [[Operating Cadence]] · [[KPI Dashboard]] · [[Pricing and Packaging]] · [[Service Catalog]] · [[Website and Technical Audit]] · [[Foundation Brief]]
