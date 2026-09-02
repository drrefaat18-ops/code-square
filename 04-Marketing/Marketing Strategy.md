---
date: 2026-09-02
type: marketing-strategy
tags:
  - marketing
  - strategy
  - code-square
  - funnel
ai-first: true
status: draft
owner: TBD
confidence: mixed
---

# Marketing Strategy — Code Square

## For future Claude

This file turns `[[Foundation Brief]]` §9 (sequenced priorities) into a marketing plan. The Foundation Brief is canonical — if anything here contradicts it, the brief wins.

The single most important thing to understand before editing this file: **Code Square's marketing problem is not content quality.** The company publishes well-made infographics and a genuinely good ten-part case study, and gets 1–4 reactions on each. The cause is structural — no position, no offer, no link to the website, no distribution. A plan that says "post three times a week and use hashtags" would be treating the symptom. Do not rewrite this into that plan.

Everything labelled `proposed` was invented on 2026-09-02 and needs founder approval. Everything labelled `stated` traces to `[[2026-09-02 - Facebook Page Evidence]]` or `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`.

**Note on the superseded plan:** `plan/خطة_كود_سكوير_لأول_ثلاثة_شهور.pdf` could not be rendered in this environment; its contents are taken from the summary recorded in the Facebook Evidence note. If someone later extracts the full PDF text and finds material this file missed, update the "What we keep from the old plan" section.

---

## 1. The diagnosis in one paragraph

Code Square has, on a website nobody can reach, a sharp written identity, a four-phase methodology, an "Outsourced CTO" positioning, and **four real projects — two of them for external B2B clients**. It has, on a Facebook page 74 people follow, beginner-level explainers about the difference between UI and UX, zero named clients, and no link to that website. The website's TLS certificate is expired, so every visitor who does try gets a browser security warning; the site is client-side-rendered with no prerender, so Google and every AI engine see a blank page. The company is not failing to make content. It is making content that points nowhere, for nobody in particular, with no next step to take. (`stated` — see both evidence notes.)

---

## 2. Priority 0 is not marketing, and marketing cannot start without it

**Say this plainly to the founder, in these words if necessary: every pound spent on marketing before the website is fixed is money set on fire.**

Concretely, here is what happens today if a Facebook ad works perfectly:

1. A shipping-agency owner in Port Said sees the ad and is interested.
2. He looks for a website. The Facebook page lists none. (`stated`)
3. If he finds `mtechsquare.com/code-square/` anyway, his browser shows a full-page security warning: *this site's certificate has expired*. (`stated`)
4. If he clicks through the warning, he lands on a heavy Angular app (~7.5 MB of JS) on Egyptian mobile data. (`stated`)
5. If he shares the link, the preview says "M Tech Square Group — Beyond Squares", not Code Square. (`stated`)
6. If he asks ChatGPT "who builds custom software in Port Said", the site is invisible — the served HTML has no text in it. (`stated`)

There is no amount of creative skill that survives that path. **Priority 0 from `[[Foundation Brief]]` §9 is the gate on this entire strategy.** Marketing execution in the first two weeks is limited to work that does not depend on the website: writing the case studies, getting client permission, fixing the Facebook page itself, and direct outreach where a human, not a link, carries the message.

> **Gate 0 (must all be true before any paid spend):** TLS certificate valid · SSR or prerender live on `/code-square/` · `sitemap.xml`, `robots.txt`, `llms.txt` present · page-level `<title>` and `<meta description>` for Code Square · contact form verified to deliver, with a named human owning the inbox.

---

## 3. Objectives, mapped to the sequenced priorities

Each objective is tied to a priority from `[[Foundation Brief]]` §9. Nothing later starts before the thing above it is done.

| Priority | Marketing objective | Definition of done | Timing |
|---|---|---|---|
| **P0** | Make the proof reachable and citable | Gate 0 above, all six items green | Week 1 |
| **P1** | Turn four projects into four published case studies | 4 case studies live on site + published as social series; written permission on file from El Shoush and Osama Sakr | Weeks 1–2 |
| **P2** | Say one thing to one buyer | Beachhead chosen; FB bio, cover, CTA button, pinned post rewritten to it; Diagnostic Session bookable via a real link | Weeks 2–4 |
| **P3** | Make enquiries survivable | Intake form, CRM (even a spreadsheet), 24h response SLA with a named owner, follow-up cadence | Month 2 |
| **P4** | Buy attention, only now | Meta campaigns live against a working funnel — see `[[Paid Media Plan]]` | Month 3+ |

**Jargon note (the reader is a pharmacist, so terms are defined on first use):**
- **Funnel** — the sequence of steps a stranger passes through on the way to becoming a client. Named because many enter the top and few reach the bottom.
- **Beachhead** — one narrow market you attack first, chosen because you can win it, and from which you expand. Borrowed from amphibious landings.
- **SLA** — Service Level Agreement, a promise about response time. The website currently promises 24 hours with nobody assigned to keep it.
- **CRM** — Customer Relationship Management, i.e. the single list where every enquiry lives so none is forgotten. A spreadsheet counts.

---

## 4. The funnel: stranger → Diagnostic Session

The offer ladder is defined in `[[Offer Ladder]]`; this is how a person travels it.

```
STRANGER
   │  sees a case study or a problem post about their own industry
   ▼
AWARE — "these people have built software for a manning agency"
   │  follows, or clicks through to the website
   ▼
INTERESTED — reads a case study end to end, sees a real number
   │  the only CTA on social: احجز جلسة تشخيص مجانية (book a free Diagnostic Session)
   ▼
ENQUIRY — WhatsApp message, form submission, or DM
   │  intake questions answered, qualified against [[ICP - Ideal Customer Profiles]]
   ▼
DIAGNOSTIC SESSION — 30–45 min, free, ends with a one-page written output
   │  they keep the page whether or not they buy
   ▼
BLUEPRINT (paid, fixed price) ──► BUILD ──► RETAINER
```

**Design rules for this funnel (`proposed`):**

1. **One CTA on social. Ever.** Every post ends with the Diagnostic Session or with a question. Nothing else. Multiple calls to action on a page with 74 followers guarantees that none of them accumulates recognition.
2. **The Diagnostic Session must be genuinely valuable if they never buy.** The one-page written output is the product. It is also the single best piece of proof-of-competence marketing the company can produce, because the prospect shows it to colleagues.
3. **The website is the proof layer, not the conversion layer.** Conversion happens in WhatsApp, where Egyptian B2B buyers actually transact. The site's job is to make someone believe Code Square is real before they open WhatsApp.
4. **Nothing enters the funnel that cannot be answered within 24 hours** — that promise is already published on the site. Either honour it or remove it.

**The leak to watch:** today, the funnel has no middle. A follower's only option is "message and hope" (`[[Foundation Brief]]` §2, Layer 4). The Diagnostic Session exists to be the middle.

---

## 5. Channel strategy — why each channel earns its place

A channel earns a place only if it can be named against a specific job. Anything that cannot is in §9, "What we are not doing".

### 5.1 LinkedIn vs Facebook for maritime B2B — the argument, resolved

This is the most consequential channel decision in the plan, so here is the reasoning rather than the conclusion alone.

**The case for LinkedIn:** maritime is a global, English-speaking, corporate industry. Shipping lines, P&I clubs, crewing managers, and freight forwarders maintain real LinkedIn presences. Job titles are searchable — "Crewing Manager", "Operations Manager", "Port Agent" — which makes cold outreach targetable in a way Facebook cannot match. Content there carries professional credibility. And the Gulf service areas already listed on the page (Jeddah, Riyadh — `stated`) are LinkedIn-heavy markets.

**The case against LinkedIn:** the actual buyer for Code Square's first ten deals is not a crewing manager at Maersk. It is the **owner of a 12-to-40-person shipping agency, crewing agent, or customs brokerage in Port Said or Damietta** — a man in his forties or fifties who runs the business personally, whose LinkedIn profile is a dormant shell created in 2014, and who conducts all business by phone and WhatsApp. Reaching him on LinkedIn means reaching an inbox he does not open.

**Resolution (`proposed`):** they are not competitors, they are different stages.

- **Facebook is where the Port Said buyer actually is.** It stays the primary organic channel *for the local beachhead*, and it is also where Meta's local geo-targeting makes paid reach cheap (see `[[Paid Media Plan]]`).
- **LinkedIn is where the buyer's company and his staff are, and where the credibility record lives.** Its job in the first 90 days is not lead generation — it is (a) making the company verifiable when someone searches the name after a meeting, and (b) enabling direct, named outreach to the larger agencies and the Gulf market.
- **LinkedIn becomes more important than Facebook only when the beachhead expands beyond driving distance** — to Alexandria, Damietta, Jeddah, and Riyadh — because that is the point at which no local relationship or physical visit is possible. `proposed`: expect that at month 6–9, not month 1.

So: Facebook first for the beachhead, LinkedIn built in parallel as the credibility and outbound layer, LinkedIn overtakes Facebook when geography stops being the acquisition mechanism. Do not invert that order for the sake of "B2B means LinkedIn".

### 5.2 The full channel table

| Channel | Job in the funnel | Why it earns its place | Priority |
|---|---|---|---|
| **Facebook page** | Awareness → Interested, for Port Said/Egypt | The buyer is already there. 74 followers is a starting condition, not a verdict. Also the cheapest geo-targeted paid reach in Egypt. | **1** |
| **WhatsApp Business** | Interested → Enquiry → Session | The real conversion surface in Egyptian B2B. Already on the page (`stated`). Needs a catalogue, greeting message, away message, and labels — currently a bare number. | **1** |
| **Direct outreach** | Cold → Session, targeted | With four case studies and a maritime reference, twenty named agencies within driving distance is a better use of week 3 than any amount of posting. Highest-conversion channel available at this size. | **1** |
| **Website + case studies** | Proof layer for every other channel | Blocked by Gate 0. Once fixed, it is the asset every channel points at, and the only one that earns compounding search and AI-citation value. | **1** (after P0) |
| **LinkedIn (company + founder)** | Credibility record; outbound to larger and Gulf accounts | See §5.1. Founder profile matters more than company page at this size — people follow people. | **2** |
| **Referral** | Client → new client | Two external clients exist. A structured ask ("who else in the port has this problem?") costs nothing and converts better than everything else. Currently not being asked. | **2** |
| **Local / offline Port Said** | Cold → warm, in person | Underrated and specific to this company: the Chamber of Commerce, shipping-agency associations, the customs-broker community, and Port Said's business network are small and relationship-driven. A founder who shows up at three industry gatherings will out-perform three months of posting. Also: the Osama Sakr relationship is a physical, local reference that can be visited. | **2** |
| **Email** | Nurture; case-study delivery; Blueprint follow-up | Not a broadcast newsletter at this stage — there is no list. Its first job is transactional: sending the Diagnostic Session output, the case-study PDF, and the follow-up sequence after an enquiry goes quiet. A list gets built as a by-product. | **3** |
| **Instagram** | Secondary distribution, recruiting, visual proof | Honest assessment: it does not reach the maritime buyer. It earns a place only as a repurposing destination (zero marginal cost — see `[[Content System]]`) and because the M Tech Square group's 3D/animation craft is genuinely strong visual material. Do not build a separate strategy for it. | **4** |

### 5.3 Channel rationale in one line each

- Facebook because the buyer is there. WhatsApp because the deal closes there. Outreach because twenty of the right conversations beat twenty thousand impressions. The website because it is the only asset that compounds. LinkedIn because it is where the name gets verified. Referral because it is free and warm. Offline because Port Said is a town, not a market. Email because enquiries go cold without it. Instagram because repurposing is free.

---

## 6. The north-star metric

> **North star: qualified Diagnostic Sessions booked per month.** (`proposed`)

A **qualified** session means the prospect meets the criteria in `[[ICP - Ideal Customer Profiles]]` — right segment, a real budget owner in the room, a named problem. Every other number in this vault is a leading indicator of that one.

**Why not the obvious alternatives:**

| Candidate | Why it is rejected |
|---|---|
| Followers | Code Square already proves the point — high-quality output, 74 followers, zero pipeline. Followers are a vanity number that can rise while revenue is flat. |
| Reach / impressions | Measures the platform's generosity, not the company's. |
| Website traffic | Currently meaningless (the site cannot be reached), and even when fixed it is a step, not an outcome. |
| Revenue | Correct in the long run but lags by months at this deal size — too slow to steer weekly decisions. |
| Total enquiries | Rewards volume over fit. Ten "how much for a website?" messages are worse than one qualified session. |

**Target (`proposed`, founder to confirm against capacity):** 4 qualified Diagnostic Sessions in month 3, 8 per month by month 6. At a `proposed` 25% session→Blueprint rate, that is one paid Blueprint in month 3.

---

## 7. KPI table, channel by channel

Baselines are `stated` where a real number exists; everything else is `TBD` until measurement is in place. **Do not invent baselines.**

| Channel | Leading indicator | Baseline today | 90-day target (`proposed`) | Review cadence |
|---|---|---|---|---|
| **North star** | Qualified Diagnostic Sessions booked | 0 (`stated` — offer does not exist) | 4 in month 3 | Weekly |
| Facebook organic | Saves + shares on case-study posts | 0–3 shares/post (`stated`) | 10+ shares on the best case-study post | Weekly |
| Facebook organic | Comments per post | 0–1 (`stated`) | 5+ on beachhead problem posts | Weekly |
| Facebook page | Followers *in the beachhead segment* | TBD (74 total, segment unknown) | 300 total, segment tracked | Monthly |
| Facebook page | Click-throughs to website | 0 (`stated` — no link exists) | 150/month | Weekly |
| WhatsApp | Inbound conversations started | TBD (not measured) | 20/month | Weekly |
| WhatsApp | Conversation → session rate | TBD | 25% | Monthly |
| Website | Case-study page views | TBD (unmeasurable today) | 400/month | Weekly |
| Website | Form submissions | TBD (delivery unverified) | 8/month | Weekly |
| Website | Median response time to a form | Unmeasured, 24h promised (`stated`) | Under 4 working hours | Weekly |
| Direct outreach | Named accounts contacted | 0 | 60 over 90 days | Weekly |
| Direct outreach | Reply rate | — | 20% | Monthly |
| Direct outreach | Meetings booked | 0 | 6 | Weekly |
| LinkedIn | Founder connections in beachhead | TBD | 200 | Monthly |
| LinkedIn | Post impressions from target titles | TBD | Tracked, no target yet | Monthly |
| Referral | Referral asks made | 0 | 10 | Monthly |
| Referral | Referral introductions received | 0 | 3 | Monthly |
| Local / offline | Industry events or visits attended | TBD | 6 over 90 days | Monthly |
| Email | Diagnostic outputs delivered | 0 | 1 per session, 100% | Per session |
| Instagram | — | — | No target. Repurposing only. | Quarterly |

**Two counter-metrics** — numbers that must *not* rise while the others do:

- **Unanswered enquiries older than 24 hours.** Target: zero. Every marketing pound is wasted the moment this is non-zero.
- **Unqualified sessions as a share of all sessions.** Rising means the targeting is drifting back to "anyone with an idea".

---

## 8. Budget allocation logic

The founder's monthly budget is `TBD` (`[[Foundation Brief]]` §10). The old plan proposed 10,000 EGP/month. This section is the *logic* for allocation; the concrete 10,000 EGP structure lives in `[[Paid Media Plan]]`.

**Principle 1 — Fix before amplify.** The first money goes to Priority 0, not to ads. A TLS certificate and a prerender step cost a fraction of one month's ad budget and multiply the return on every pound that follows. Spending on ads first is buying traffic for a broken door.

**Principle 2 — At this stage, production beats media.** With 74 followers and no case studies published, the constraint is *assets*, not *reach*. Money spent making four excellent case studies (photography, one video, design, possibly a client-visit shoot) returns more than the same money spent boosting posts that have nothing to say. `proposed` split for months 1–2: **80% production / 20% media**, inverting to roughly **40% production / 60% media** by month 3 once assets exist.

**Principle 3 — Media spend is a test budget until it proves itself.** No campaign gets a budget increase on the basis of cheap clicks. Scaling rules are in `[[Paid Media Plan]]` and are tied to qualified enquiries only.

**Principle 4 — Reserve for opportunity.** Hold roughly 10% unallocated. In a relationship market, the highest-return spend of the quarter may be a conference ticket, a printed case-study booklet for a client visit, or filming a testimonial — none of which appear on a media plan written in advance.

**Principle 5 — Founder time is the scarcest budget line.** Direct outreach and the Diagnostic Session both consume founder hours and both convert better than anything purchasable. Protect a `proposed` fixed block — two mornings a week — before allocating any cash.

---

## 9. What we are NOT doing, and why

This section exists to be defended. Each item is a real temptation with a real reason for refusal.

| Not doing | Why |
|---|---|
| **Posting three generic educational posts a week** | Already tried. "The difference between UI and UX" earns 1–4 reactions because it addresses nobody and asks for nothing. Volume is not the missing variable. |
| **Chasing follower growth** | Followers are free to acquire and worthless if untargeted. A page with 300 followers that includes 40 port-services owners beats one with 5,000 students. |
| **Running ads before Gate 0** | See §2. Non-negotiable. |
| **Launching all four beachhead segments at once** | `[[Foundation Brief]]` §4 explicitly says pick one. Four segments at 74 followers produces zero recall in all four. |
| **TikTok** | The Port Said shipping-agency owner is not the audience, and short-form video is the most expensive content per unit to produce well. Revisit only if the beachhead moves to education (segment B), where it would genuinely work. |
| **A weekly newsletter** | There is no list. Building one before there is anything to send is a task that generates work and no outcome. Email starts transactional (§5.2). |
| **A blog written for SEO keywords** | The site cannot currently be crawled at all. Publishing keyword articles into an unindexable Angular shell is writing into a void. Fix rendering, publish case studies, *then* consider search content. |
| **Rebranding, new logo, new colour system as a project** | `[[Foundation Brief]]` §5 is explicit: do not spend money changing the logo. Resolve the two colour systems by adopting the website tokens; that is a template rebuild, not a rebrand. |
| **Publishing both methodologies** | Two frameworks are already published and conflict (`[[Foundation Brief]]` §0.6). Pick the website's four-phase model as canonical and never publish the five-stage one again. |
| **Any claim without a proof asset** | Includes the banned phrases in `[[Foundation Brief]]` §5: أقوى فريق · أفضل شركة · حلول متكاملة · أحدث التقنيات · ثقة عملائنا · "Awwwards-tier" · "99.9% uptime" · "SLA Guarantees" · "worldwide". These are currently live on the site and in the Facebook infographics and must be removed as those assets are rewritten. |
| **Influencer marketing / paid collaborations** | No influencer reaches a crewing agent. |
| **Hiring an agency to run the page** | The scarce asset is domain knowledge — maritime workflows, the port community, the founder's pharmacy fluency. An outside agency has none of it and would regenerate exactly the generic content that produced 74 followers. |

---

## 10. Roadmap

### 90 days — "Make the proof visible and get four conversations"

| Weeks | Focus | The one thing that must be true at the end |
|---|---|---|
| 1 | Priority 0 + Facebook page surgery | The website loads without a warning; the FB page has a link, a real bio, and a CTA button |
| 2–4 | Publish the four case studies; launch the Diagnostic Session | Four case studies live and published as social series; the session is bookable |
| 5–8 | Beachhead problem/solution content + direct outreach begins | 30 named maritime/port accounts contacted; page speaks only to that buyer |
| 9–13 | Convert attention into sessions | 4 qualified Diagnostic Sessions held; 1 Blueprint quoted |

Week-by-week detail: `[[Editorial Calendar - First 90 Days]]`.

**Exit criteria for the 90 days (`proposed`):** ≥4 qualified sessions · ≥1 paid Blueprint · ≥1 documented client number published · a functioning intake process with zero enquiries older than 24h.

### 6 months — "Turn a beachhead into a category"

- A second and third maritime/port client, so the reference is a pattern rather than an anecdote.
- One healthcare pilot from the founder's network (`[[Foundation Brief]]` §7.3), traded for a documented before/after — this opens segment C without diverting the beachhead.
- A **named, productised offering for the beachhead**, e.g. a crewing/agency operations system with a known scope and price band, rather than bespoke quoting every time. This is what makes marketing repeatable.
- LinkedIn becomes a first-class channel as the geography widens (§5.1).
- English content shipped properly for Jeddah/Riyadh — the service areas are already advertised and currently have no content behind them (`stated` gap).
- Paid media scaled only against proven qualified-enquiry cost.
- Decide the dedicated domain question. `codesquare.*` matters more at month 6 than month 1, because by then there is SEO equity worth owning.

### 12 months — "Be the obvious choice for one industry in one region"

- The goal is a sentence a stranger can complete: *"if you run a shipping or crewing agency in Port Said and your operations are still on Excel and WhatsApp, you talk to Code Square."*
- Three to five published maritime/logistics case studies with real numbers — enough to make the claim structural rather than reputational.
- Retainer revenue ("Outsourced CTO", `[[Offer Ladder]]` rung 3) as the base of the business, because it is the only revenue that does not restart from zero each month.
- Expansion decision point: geography (Damietta, Alexandria, Suez, then Gulf) versus vertical (education via Techno Square, healthcare via the founder). `proposed` recommendation: geography first — the same message travels; a new vertical needs a whole new message and new proof.
- A referral engine that produces a `TBD` share of new business, measured.

---

## 11. What we keep from the superseded plan

The old three-month plan is superseded, not worthless. Three things in it were right:

1. **The 10,000 EGP/month figure as a working budget order-of-magnitude.** Kept as the planning basis in `[[Paid Media Plan]]`, though the 70/30 services-versus-retargeting split is rejected — retargeting with near-zero traffic has nobody to retarget.
2. **"A project story every two weeks" as a content rhythm.** Kept and strengthened: the four real projects become case-study *series*, not single posts (`[[Content System]]`).
3. **Naming specific segments at all.** The instinct to segment was correct; the specific five segments (teachers, lawyers, company owners, idea owners, group clients) are rejected because they were chosen without reference to where proof already existed. `[[Foundation Brief]]` §4 chooses on proof.

---

## 12. Open decisions blocking this strategy

Tracked in `[[Open Questions and Decisions Needed]]`. The four that block the most work:

1. **Beachhead confirmation** — the whole plan assumes maritime/logistics (segment A). Everything in `[[Editorial Calendar - First 90 Days]]` from week 5 onward changes if the founder picks differently.
2. **Client permission from El Shoush and Osama Sakr** — blocks half the case-study content. Ask in week 1.
3. **Real numbers from those two clients** — blocks the credibility of every case study. Until they exist, every post uses `[[INSERT REAL NUMBER — see Portfolio and Case Studies]]`.
4. **Pricing and the Diagnostic Session booking mechanism** — blocks the entire conversion path.

## Related
[[Foundation Brief]] · [[Messaging Framework]] · [[ICP - Ideal Customer Profiles]] · [[Portfolio and Case Studies]] · [[Offer Ladder]] · [[Content System]] · [[Social Media Playbook]] · [[Editorial Calendar - First 90 Days]] · [[Paid Media Plan]] · [[Content Templates and Hooks]] · [[Open Questions and Decisions Needed]]
