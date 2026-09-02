---
date: 2026-09-02
type: decision-register
tags:
  - decisions
  - blockers
  - canonical
ai-first: true
status: active
owner: Founder
---

# Open Questions and Decisions Needed

## For future Claude

The single register of everything the vault does not know and every decision waiting on the founder. **Read this before doing any new work** — most `TBD` markers elsewhere in the vault point here. When an item is answered: record the answer here, strike the row, update `[[Foundation Brief]]`, and replace the `TBD` everywhere it appears. Nothing in this vault should stay `TBD` silently.

**How to use it:** the founder answers the 🔴 blockers first. Each answer unlocks named downstream work. Do not start work that depends on an unanswered blocker — do the independent parts and come back.

---

## 🔴 Blockers — work is stopped until these are answered

| # | Question | Why it blocks | Unblocks |
|---|---|---|---|
| B1 | **Who renews the TLS certificate on `mtechsquare.com`, and when?** It is currently expired — every visitor sees a browser security warning. | The website is effectively unreachable. All marketing spend is wasted until fixed. | Everything in `[[Marketing Strategy]]`, `[[Paid Media Plan]]` |
| B2 | **Will we add server-side rendering / prerendering to the Angular site?** Today Google and every AI engine see a blank page. | The company is invisible to search and AI. | `[[SEO and AEO Foundations]]` |
| B3 | **Which beachhead segment do we lead with?** Maritime/logistics · Education · Healthcare · Professional offices. **Scored recommendation now exists: `[[Beachhead Decision]]` — Segment A maritime 4.35 vs Segment B education 3.65.** Awaiting founder sign-off. Five must-be-true conditions named there; four unverified, one currently false (expired TLS). | Every message, ad, page, and script needs one audience. | `[[ICP - Ideal Customer Profiles]]`, `[[Messaging Framework]]`, `[[Editorial Calendar - First 90 Days]]` |
| B4 | **What does one delivery day cost you?** Fully-loaded day rate, utilisation %, overhead ratio, target margin. Without these there is no cost floor and every quote is a coin flip — answer this BEFORE setting any price. Then: **what are the actual prices?** Diagnostic Session (free?), Blueprint fixed price, MVP bands, retainer tiers, day rate, minimum project size. | No proposal, quote, or ad can be produced. | `[[Pricing and Packaging]]`, `[[Proposal and SOW Template]]` |
| B5 | **Who is on the team, and what does each person actually do?** Names, roles, capacity, full-time vs part-time. Are you full-time on Code Square? | Cannot assign a single owner. Cannot promise a timeline or an SLA. | `[[Org and Roles]]`, `[[Delivery Process]]`, every `owner: TBD` |
| B6 | **Can we publish El Shoush Travel and Osama Sakr as named case studies?** Written permission needed for name, logo, screenshots, metrics, and quote. | The two external references are the strongest proof the company owns and cannot currently be used. | `[[Portfolio and Case Studies]]`, all of `05-Proof/` |
| B7 | **What is the real monthly marketing budget, and for how many months?** The old plan assumed 10,000 EGP/month. | Determines whether the plan is organic-first or paid-supported. | `[[Paid Media Plan]]`, `[[Marketing Strategy]]` |

---

## 🟡 Important — needed within 30 days

| # | Question | Notes |
|---|---|---|
| I1 | **Do we buy a dedicated domain** (`codesquare.*`) or stay at `mtechsquare.com/code-square/`? | Affects brand recall, SEO equity, and every printed asset. Analysis in `[[SEO and AEO Foundations]]`. |
| I2 | **Which methodology is canonical** — the website's 4-phase model or Facebook's 5-stage model? | Two conflicting frameworks are published today. **Recommendation in `[[Delivery Process]]`: adopt the website's 4-phase model; the Facebook 5 stages survive as named activities inside phases 1–2, so nothing already published becomes false.** Awaiting founder sign-off. |
| I3 | **Which colour system is canonical** — the website's navy + gold + purple, or the Facebook violet-on-black? | Two visual identities share one name. |
| I4 | **Does the government (B2G) project exist?** A `مشروع حكومي B2G` label sits in the website code with no matching project shown. | If it exists it is a major credibility asset. If not, remove the label. |
| I5 | **Who owns the website contact form inbox**, and does the form actually deliver? The site promises a **24-hour response**. | An unowned SLA is a broken promise. Test it end to end. |
| I6 | **What email address does the site's "email us directly" link point to?** Is it `codesquareteam1@gmail.com` or another? | A `@gmail.com` address on a company selling enterprise software is a trust cost — consider a domain address. |
| I7 | **What are the budget bands in the website form's dropdown?** They were not recoverable from the code. | Needed for lead qualification. |
| I8 | **What is the legal entity name and registration status?** Sole proprietorship, LLC, part of M Tech Square, or unregistered? | Required for contracts, invoicing, and Gulf clients. |
| I9 | **What is the real relationship to M Tech Square?** Subsidiary, division, brand, or partner? Who owns the P&L? | Affects positioning, contracts, and how the group is presented. |
| I10 | **Are Jeddah and Riyadh real markets or aspirational?** Any client, partner, or presence there? | Currently listed as service areas with no evidence behind them. |
| I11 | **What actually happened with the two Facebook reviews?** Who left them and what do they say? | Existing social proof that is currently unused. |
| I12 | **Do "SLA Guarantees" and "99.9% uptime" have any document behind them?** Both are advertised. | Either build the SLA or stop claiming it. See `[[Support and Maintenance SLA]]`. |
| I13 | **Do the Privacy Policy and Terms of Service pages have real content?** | Legal exposure and a trust signal. |

---

## 🟢 Useful — answer when convenient

| # | Question |
|---|---|
| U1 | When was Code Square founded? What is the origin story? |
| U2 | What is the current monthly revenue and cost base? Is the company profitable? |
| U3 | What is the delivery capacity today — how many projects can run at once? |
| U4 | What technologies is the team genuinely strong in, versus what the website claims? (The site advertises RAG pipelines, LLM integration, IoT, Stripe, multi-tenant SaaS — is all of that real, delivered capability?) |
| U5 | Which past enquiries were lost, and why? Any record of them? |
| U6 | Is there an existing CRM, project management tool, or accounting system? |
| U7 | Who currently writes and designs the Facebook content? Internal or the outgoing media buyer? |
| U8 | Are there existing brand files — logo vectors, brand guidelines, font licences? |
| U9 | What is the target: a services agency, or a product company funded by services? |
| U10 | Is there an existing client base beyond the four documented projects — small jobs, referrals, retainers? |

---

## Decisions log

Record every answered decision here. Never delete a row; supersede it.

| Date | Decision | Made by | Rationale | Supersedes |
|---|---|---|---|---|
| 2026-09-02 | The 3-month plan PDF in `plan/` is superseded, not adopted | Founder | "no actual identity, no actual written message, no real plan or direction" | — |
| 2026-09-02 | `$19/$49/$99` on the SaaS infographic is mockup art and must never be quoted | Session | It is placeholder design content, not a price list | — |
| 2026-09-02 | No paid marketing spend until the TLS certificate and site rendering are fixed | Session (proposed) | Traffic sent to a browser security warning is money burned | — |

## Related
[[Foundation Brief]] · [[2026-09-02 - Facebook Page Evidence]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]
