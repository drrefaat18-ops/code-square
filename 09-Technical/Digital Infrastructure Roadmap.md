---
date: 2026-09-02
type: roadmap
tags:
  - technical
  - roadmap
  - infrastructure
  - planning
  - code-square
ai-first: true
status: draft
owner: TBD
severity: high
confidence: mixed
---

# Digital Infrastructure Roadmap

## For future Claude

The 12-month build-out of Code Square's own digital infrastructure, in four phases. Every phase states its objective, deliverables, dependencies, effort, owner, and **success criteria that can be checked rather than argued about**.

This note is the sequencing spine. The detail lives elsewhere: what is broken in `[[Website and Technical Audit]]`, how to fix the blockers in `[[Remediation Plan - Priority Zero]]`, discoverability in `[[SEO and AEO Foundations]]`, measurement in `[[Analytics and Measurement Setup]]`. **Do not duplicate their content here — link to it.**

Every owner is `TBD`. `[[Open Questions and Decisions Needed]]` must resolve who holds server access, who writes content, and who answers enquiries before Phase 1 can be scheduled honestly.

The final section, **§6 The Spending Gate**, is the part the founder most needs to read.

Labels: `verified` · `stated` · `researched` · `proposed` · `TBD`.

---

## 0. The shape of the year, in one paragraph

Code Square currently has a website that visitors cannot trust and search engines cannot read (`verified` 2026-09-02). **Phase 0** takes about one week and makes it work at all. **Phase 1** takes about three months and makes it findable — a real domain, readable pages, the four projects published, analytics, and a bookable first offer. **Phase 2** takes months 4–7 and makes it convert — landing pages aimed at one specific kind of buyer, lead capture that does not leak, and a system for following up. **Phase 3** takes months 8–12 and makes it authoritative — publishing in Arabic and English, a resource library, and a proper English presence for the Gulf.

**The sequence is not negotiable.** Authority content on an invisible site is invisible. Conversion optimisation on a site with no traffic optimises nothing. Traffic to a site with an expired certificate is money set on fire.

---

## Phase 0 — Stabilise
**Timing: this week. Effort: ~1 developer-day plus 3–5 days for prerendering.**

### Objective
Make the website functional: loadable without a security warning, readable by machines, and impossible to break silently again.

### Deliverables
| # | Deliverable | Detail |
|---|---|---|
| 0.1 | TLS certificate renewed | `[[Remediation Plan - Priority Zero]]` §A1 |
| 0.2 | Automated renewal repaired and verified | §A2 |
| 0.3 | Uptime, certificate-expiry and keyword monitoring, alerting to two people on two channels | §A3 |
| 0.4 | gzip compression enabled | §A4 |
| 0.5 | Real `robots.txt`; catch-all soft-404 fixed | §A5 |
| 0.6 | Contact form proven to deliver; inbox owner **named** | §A6 |
| 0.7 | `og:url = codesquare.com` resolved | §A7 |
| 0.8 | Facebook ↔ website linked in both directions | §A8 |
| 0.9 | **Prerendering live — served HTML contains real text** | §B1 |
| 0.10 | Google Search Console + Bing Webmaster live | `[[Analytics and Measurement Setup]]` §2 |
| 0.11 | GA4 with the six events | §3 |

### Dependencies
Server SSH access (**`TBD` — this is the actual blocker**). The Angular developer's availability for 0.9. Nothing else.

### Owner
`TBD` — items 0.1–0.5 and 0.9 need whoever has server and repository access. 0.6 and 0.7 need the founder.

### Success criteria — all must pass
- [ ] `curl -sSI https://mtechsquare.com/code-square/` returns `200` **without** `-k`
- [ ] Certificate expiry is >60 days away and `certbot renew --dry-run` succeeds
- [ ] A deliberately triggered alert arrives on two channels within 10 minutes
- [ ] `curl -sS .../robots.txt` returns plain text; `/nonexistent-abc123.txt` returns `404`
- [ ] Served HTML body text length **>2,000 characters** (today: 0)
- [ ] Search Console URL Inspection shows the rendered content
- [ ] A test form submission arrives in a named inbox within 5 minutes
- [ ] GA4 Realtime shows `form_submit` and `whatsapp_click` firing
- [ ] The site loads correctly on a real phone, 3D scene intact — **regression check, do not skip**

**Until every box above is ticked, Phase 1 does not start and no marketing money is spent (§6).**

---

## Phase 1 — Foundations
**Timing: months 1–3. Effort: ~25–35 developer-days plus content-writing time.**

### Objective
Make Code Square findable, credible, and contactable. At the end of Phase 1 a stranger should be able to find the company through search, read a real case study, and book a first conversation without a human intervening.

### Deliverables

**1A · Domain**
| # | Deliverable | Ref |
|---|---|---|
| 1.1 | Founder decision on the dedicated domain | `[[SEO and AEO Foundations]]` §1 |
| 1.2 | Domain registered, certificate issued, monitoring extended to it | §1 |
| 1.3 | Site served at the new root; **one-to-one 301 redirects** from every old URL | §1 |
| 1.4 | Search Console Change of Address; every reference updated (Facebook, `og:url`, JSON-LD, `llms.txt`, signatures) | §1 |

**1B · Site architecture and content**
| # | Deliverable | Ref |
|---|---|---|
| 1.5 | Single page split into ~20 routes — one per service, one per project, one per industry | §2 |
| 1.6 | Unique title + meta description on every page, both languages, written natively | §3 |
| 1.7 | Reciprocal `hreflang` + `dir="rtl"` on Arabic pages | §4 |
| 1.8 | Canonical tags, `og:image`, Arabic meta descriptions | §3 |
| 1.9 | `sitemap.xml` generated from the prerender route list; submitted | §7 |
| 1.10 | **The canonical methodology page — one framework, not two** | `[[Foundation Brief]]` rule 6 |

**1C · Structured data and AEO**
| # | Deliverable | Ref |
|---|---|---|
| 1.11 | Organization + LocalBusiness JSON-LD sitewide | §5.1 |
| 1.12 | Service + BreadcrumbList JSON-LD on the new pages | §5.2–5.3 |
| 1.13 | FAQPage blocks with buyer-phrased questions | §5.5 |
| 1.14 | `llms.txt` published | §8 |
| 1.15 | Google Business Profile created, verified, populated | §11.1 |
| 1.16 | NAP canonical forms decided and applied everywhere | §11.2 |
| 1.17 | LinkedIn Company Page created | §11.3 |

**1D · Proof**
| # | Deliverable | Ref |
|---|---|---|
| 1.18 | **Written publication permission from El Shoush and Osama Sakr** | `[[Portfolio and Case Studies]]` |
| 1.19 | Four case-study pages, problem → approach → result, **each with at least one real number** | `[[Foundation Brief]]` §7 |
| 1.20 | The maritime industry page — **highest-leverage single page on the site** | `[[SEO and AEO Foundations]]` §9 |

**1E · The offer**
| # | Deliverable | Ref |
|---|---|---|
| 1.21 | Diagnostic Session page with a **working booking link** (Cal.com or Google Calendar appointment schedule — both free) | `[[Foundation Brief]]` §6 |
| 1.22 | WhatsApp on the site with **per-page pre-filled source tags** | `[[Analytics and Measurement Setup]]` §5.1 |
| 1.23 | Phone number visible on the site | CONT-01 |
| 1.24 | Lead-source question added to the contact form; lead log started | §7 |
| 1.25 | Privacy policy and terms with **real content**, both languages; consent banner | §8 |

**1F · Performance and hygiene**
| # | Deliverable | Ref |
|---|---|---|
| 1.26 | Spline viewer self-hosted, off `unpkg.com` | `[[Remediation Plan - Priority Zero]]` §B4 |
| 1.27 | Lighthouse baseline recorded; the ~7.5 MB payload figure finally measured | §B5 |
| 1.28 | Security headers (HSTS, CSP, X-Frame-Options, Referrer-Policy) | SEC-04 |

### Dependencies
- **All of Phase 0.** Non-negotiable.
- **1.18 blocks 1.19 for the two external projects.** The two internal ones (M Tech Square, Techno Square) need no permission — **start with those** so the portfolio is not held hostage by a client's response time.
- 1.19 blocks 1.20 having anything to point at.
- 1.5 blocks 1.6, 1.9, 1.11–1.13.
- 1.1 should be decided **before** 1.5, so the split is built once at the right address.
- 1.21 requires the founder to commit to a calendar and to actually attend the sessions.

### Owner
`TBD`. Realistically three roles: a developer (1.2–1.9, 1.11–1.14, 1.26–1.28), a bilingual writer (1.6, 1.10, 1.19, 1.20, 1.25), and the founder (1.1, 1.15, 1.18, 1.21, 1.24).

### Success criteria
- [ ] Search Console reports **>15 pages indexed** (today: effectively 0)
- [ ] The site returns results for a `site:` search on the new domain
- [ ] Google Business Profile verified and appearing for "Code Square Port Said"
- [ ] Four case-study pages live, **each containing at least one number**
- [ ] Rich Results Test passes for Organization, FAQPage and BreadcrumbList
- [ ] Diagnostic Session bookable end-to-end by a stranger with no human in the loop
- [ ] GA4 shows a full month of data with non-zero `whatsapp_click`
- [ ] **At least one AI engine names Code Square** for one of the ten questions in `[[SEO and AEO Foundations]]` §9 *(stretch — do not treat failure here as failure of the phase)*
- [ ] Lighthouse mobile performance score recorded and **improved over the Phase 0 baseline**

---

## Phase 2 — Conversion
**Timing: months 4–7. Effort: ~20–30 developer-days plus content and process work.**

### Objective
Turn visitors into logged, followed-up, qualified conversations. Phase 1 makes people arrive; Phase 2 stops them leaking away. **This is also the first phase in which paid advertising is defensible.**

### Deliverables
| # | Deliverable | Detail |
|---|---|---|
| 2.1 | **A dedicated landing page per beachhead segment** — maritime first, then education, then healthcare | Distinct from the industry pages: single-offer, single-CTA, no site navigation. One page per segment named in `[[Foundation Brief]]` §4 |
| 2.2 | A segment-specific lead magnet per landing page | e.g. *"10 أسئلة تسألها قبل ما تبني نظام إدارة لوكالتك"* — a one-page PDF, not a course |
| 2.3 | Lead capture that does not depend on the form | WhatsApp with source tags, a callback request, and the booking link on every page |
| 2.4 | **CRM, chosen and populated** | Graduate from the spreadsheet once >20 open leads or >1 person handling them. `proposed`: HubSpot free tier or Zoho CRM free tier — both usable in Egypt at no cost. Migrate the lead log; do not start empty |
| 2.5 | Transactional email properly configured | Brevo or Resend free tier, so form notifications never silently fail again |
| 2.6 | An email follow-up sequence for Diagnostic Session bookings | Confirmation → reminder → the written one-page output → follow-up |
| 2.7 | A named response process with an owner and an SLA that is actually met | Closes CONT-02 permanently. `[[Lead Intake and CRM]]` |
| 2.8 | Meta Pixel live; conversion events mapped | `[[Analytics and Measurement Setup]]` §6.1 |
| 2.9 | Meta Conversions API — **only if monthly spend >~5,000 EGP** | §6.2 |
| 2.10 | Proposal and quote templates, bilingual | Reduces time-to-quote, which is itself a competitive advantage |
| 2.11 | Performance work on the 3D payload — lazy-load below the fold, budget the hero | PERF-02. By now there is a measured baseline to improve against |
| 2.12 | Case-study pages extended with a client quote and, where possible, a filmed testimonial | `[[Foundation Brief]]` §7 |

### Dependencies
- **All of Phase 1.** Landing pages with no analytics and no proof convert nothing.
- 2.1 requires the beachhead decision in `[[Foundation Brief]]` §4 to be **confirmed by the founder**, not left open.
- 2.4 requires 1.24 (the lead log) to have real rows in it — a CRM populated from an empty spreadsheet is a subscription, not a system.
- 2.9 requires `[[Paid Media Plan]]` to be active with real spend.
- 2.7 requires a named person with capacity. **This is a hiring/time question, not a technology question.**

### Owner
`TBD`. Adds a fourth role: someone who owns lead response daily.

### Success criteria
- [ ] Each beachhead landing page live with a measurable conversion rate (any number — the first one is the baseline)
- [ ] Every enquiry from every channel lands in the CRM within 24 hours
- [ ] **Median first-response time under 24 hours, measured over a full month** — the published SLA finally honoured and evidenced
- [ ] Enquiry → Diagnostic Session booking rate recorded in `[[KPI Dashboard]]`
- [ ] At least one closed project traceable to a digital source
- [ ] Zero lost leads (reconciliation in `[[Analytics and Measurement Setup]]` §7.3 shows no unexplained gaps)
- [ ] Lighthouse mobile performance improved by a recorded margin over the Phase 1 number

---

## Phase 3 — Authority
**Timing: months 8–12. Effort: ongoing content, ~10–15 developer-days.**

### Objective
Make Code Square the company that gets found, quoted and recommended — by search engines, by AI answer engines, and by people in the industry. This is the phase that compounds, and it is the only one that keeps working when spending stops.

### Deliverables
| # | Deliverable | Detail |
|---|---|---|
| 3.1 | Blog / insights section, Arabic and English, published on the site | Not Facebook-only. Content on a platform you do not own builds someone else's asset |
| 3.2 | A sustainable publishing cadence — **two solid pieces a month beats eight thin ones** | `[[Content Calendar]]` |
| 3.3 | "Build in daylight" content — discovery documents, scoping questions, architecture decisions | `[[Foundation Brief]]` §7.4. The only content type that credibly signals "systems engineers" while results are still thin |
| 3.4 | Resource library — templates, checklists, scoping questionnaires, gated where sensible | Lead generation that runs without spend |
| 3.5 | **Decision-guide pages** — e.g. *"نظام جاهز ولا نظام مخصص؟"* | Heavily quoted by AI engines. `[[SEO and AEO Foundations]]` §9 |
| 3.6 | **A full English site for the Gulf**, written natively — not translated | `[[Foundation Brief]]` rule 3. Serves the Jeddah/Riyadh service areas |
| 3.7 | Clutch / GoodFirms profiles with real client reviews | Corroboration source for AI citations |
| 3.8 | A healthcare pilot published as a case study | Opens segment C and uses the founder's genuine domain fluency |
| 3.9 | Headless CMS with a build webhook, if publishing frequency makes rebuilds painful | **Only if it actually hurts.** Revisit the prerender decision in `[[Remediation Plan - Priority Zero]]` §4 at this point, not before |
| 3.10 | Structured data extended to Article and HowTo on published content | |
| 3.11 | Quarterly AI-visibility review as a standing process | `[[SEO and AEO Foundations]]` §9 |

### Dependencies
- Phases 1 and 2 complete.
- 3.1–3.5 depend on **someone having the time to write consistently.** This is the phase that most often fails, and it fails for capacity reasons, never technical ones. **If no one owns publishing, do not start Phase 3 — do more of Phase 2 instead.**
- 3.6 depends on the Gulf market being a confirmed priority rather than an aspiration.
- 3.8 depends on securing a healthcare pilot (`[[Foundation Brief]]` §7.3).

### Owner
`TBD`. Requires a named content owner with protected time.

### Success criteria
- [ ] Organic search is a **named source** of enquiries in the lead log, not a rounding error
- [ ] **Code Square named by at least two different AI engines** for at least three of the ten questions
- [ ] 20+ published pieces, roughly balanced Arabic and English
- [ ] At least one enquiry traceable to the resource library
- [ ] English site producing measurable Gulf traffic in GA4
- [ ] 5+ Google reviews
- [ ] Foundation score in `[[Website and Technical Audit]]` §5 at **≥75%**

---

## 4. Effort and dependency summary

| Phase | Calendar | Developer-days | Content-days | Founder-days | Hard prerequisite |
|---|---|---|---|---|---|
| **0 Stabilise** | 1 week | 5–7 | 0 | 1 | Server access `TBD` |
| **1 Foundations** | Months 1–3 | 25–35 | 15–20 | 5–8 | Phase 0 complete |
| **2 Conversion** | Months 4–7 | 20–30 | 10–15 | 8–12 | Phase 1 + beachhead confirmed |
| **3 Authority** | Months 8–12 | 10–15 | ongoing | ongoing | Phase 2 + a named content owner |

> ⚠️ **These are `proposed` estimates from an external audit, not commitments.** They assume one competent Angular developer with existing familiarity with this codebase, and a bilingual writer. **Whoever will actually do the work must re-estimate before anything is scheduled or promised.** The largest uncertainty is 1.5 (splitting a heavily-choreographed single page into ~20 routes), which could plausibly be double the estimate.

---

## 5. The critical path

Everything that must happen in order, with nothing that can be parallelised:

```
server access → certificate → monitoring → prerendering → analytics baseline
   → domain decision → site split → case studies → beachhead landing page
      → lead process with an owner → THEN paid media
```

**The two most common ways this goes wrong:**
1. **Starting content or ads before prerendering.** Produces work nobody can find and spend nobody can trace.
2. **Waiting for client permission (1.18) before publishing anything.** The two internal projects need no permission. Publish those first and keep moving.

---

## 6. The spending gate — what marketing must NOT spend money on until Phase 0 is complete

**This section exists to be shown to anyone proposing to spend money.**

Until **every success criterion in Phase 0 is ticked**, the following must not be funded:

| Do not spend on | Why, specifically |
|---|---|
| **Facebook or Instagram ads** | `verified`: the destination serves an expired certificate and a blank page. Every click buys a security warning. This is the 10,000 EGP/month in the old plan (`stated`) landing on a red interstitial. |
| **Google Ads** | Same destination problem, plus Google may restrict ads pointing at a site with certificate errors. |
| **Boosted posts** | Same. A boosted post with no working link is paid reach with no conversion path. |
| **SEO agencies or link building** | You cannot optimise the ranking of a page that serves no text. Any agency that takes this money without fixing rendering first is selling you nothing. |
| **Influencer or sponsorship placements** | The link they share warns visitors and shows no preview image (`verified`: no `og:image`). |
| **A new logo, rebrand, or new visual identity** | `[[Foundation Brief]]` §5 explicitly says do not spend money changing the logo. The identity problem is a *surfacing* problem, not a design problem. |
| **A CRM, marketing automation, or email platform subscription** | There are no leads flowing into them yet. A spreadsheet is correct until Phase 2. |
| **Paid analytics, heatmaps, or session recording** | There is no traffic to analyse. `[[Analytics and Measurement Setup]]` §10. |
| **Printed materials carrying the URL** | The URL will change if the domain decision in `[[SEO and AEO Foundations]]` §1 is approved. Printing now guarantees reprinting. |
| **A second website, a microsite, or an app** | The existing site is good and unfixed. Building a second one does not fix the first. |

### What *can* be spent, or done, during Phase 0

- **The developer time to execute Phase 0.** This is the only spend that unblocks anything.
- **A domain registration** (~$10–15) once the §1 decision is made.
- **Google Business Profile setup** — free, and it does not depend on the website working.
- **Getting client permissions and case-study numbers** — free, takes weeks of calendar time, so start immediately.
- **Writing content** — free, and Phase 1 needs it ready.
- **Founder-network outreach and referrals** — the channel that already works and does not route through the website.

### The one-sentence version

> **Fixing the certificate takes twenty minutes and costs nothing. Until it is done, every pound spent on marketing buys a stranger a security warning with Code Square's name on it.**

---

## Related
[[Website and Technical Audit]] · [[Remediation Plan - Priority Zero]] · [[SEO and AEO Foundations]] · [[Analytics and Measurement Setup]] · [[Foundation Brief]] · [[Marketing Strategy]] · [[Paid Media Plan]] · [[Portfolio and Case Studies]] · [[KPI Dashboard]] · [[Content Calendar]] · [[Lead Intake and CRM]] · [[ICP - Ideal Customer Profiles]] · [[Open Questions and Decisions Needed]]
