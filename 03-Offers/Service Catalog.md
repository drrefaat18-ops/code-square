---
date: 2026-09-02
type: service-catalog
tags:
  - offers
  - services
  - code-square
  - catalog
ai-first: true
status: draft
owner: TBD
---

# Service Catalog — Code Square

## For future Claude

This is the **definitive list of what Code Square sells**. It exists because the company has published its seven service lines three times (Facebook cover strip, Facebook infographic batch, website services section) in three slightly different forms, and nobody has ever written down what is *included*, what is *excluded*, or what "finished" means.

Rules for editing this file:
- The **AR description column marked `stated`** is verbatim from the website or the Facebook page. **Never rewrite it here.** If the founder wants new wording, change it on the site first, then copy it here.
- Everything under *Included / Excluded / Duration / Client must provide / Definition of done* is `proposed` (2026-09-02) and needs founder sign-off.
- **No prices in this file.** Pricing lives in `[[Pricing and Packaging]]`.
- The website claims **"SLA Guarantees"**, **"99.9% uptime"** and **"Awwwards-tier"**. `[[Foundation Brief]]` §5 bans these until a real SLA document exists. They are quoted here only as evidence of what is currently published, marked ⚠️.
- The reader is a pharmacist. Every technical term gets defined in the glossary at the bottom, and on first use.

Source of truth: `[[Foundation Brief]]` · `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]` · `[[2026-09-02 - Facebook Page Evidence]]`

---

## 0. How to read this catalog

| Label | Meaning |
|---|---|
| `stated` | Published word-for-word by Code Square already. Evidence file cited. |
| `proposed` | Written 2026-09-02 as part of this vault. Founder has not approved it yet. |
| `researched` | External market fact with a source URL and a date. Never a Code Square fact. |
| `TBD` | Genuinely unknown. Goes to `[[Open Questions and Decisions Needed]]`. |

**A note on why "excluded" matters more than "included."** Most agency money is lost in the gap between what the client assumed was in the price and what the team assumed was out of it. The Excluded row of each service is the single most commercially valuable part of this document. It is what you paste into a proposal. See `[[Scoping and Estimation Guide]]` for how that gap turns into unpaid work.

---

## 1. The seven service lines at a glance

| # | Service (AR) | Service (EN) | Primary ICP segment | Default engagement shape |
|---|---|---|---|---|
| 1 | تطبيقات الجوال | Mobile Applications | B — Education · A — Maritime field staff | Fixed-scope build → retainer |
| 2 | تطوير الويب والمنصات | Web & Platform Development | A — Maritime/logistics · D — Professional offices | Fixed-scope build → retainer |
| 3 | أنظمة SaaS المخصصة | Custom SaaS Systems | Product founders · B — Education | Phased build + revenue-share option |
| 4 | حلول الذكاء الاصطناعي والأتمتة | AI & Automation Solutions | A — Maritime · C — Healthcare | Time & materials or small fixed pilots |
| 5 | تصميم الـ UI/UX | UI/UX Design | All segments; also a standalone entry offer | Fixed-price, short |
| 6 | تكامل الأنظمة (IoT) | System Integration (incl. IoT) | A — Maritime/logistics · industrial | Time & materials |
| 7 | الدعم والصيانة | Support & Maintenance | Every past client | Monthly retainer |

ICP segment letters map to `[[Foundation Brief]]` §4 and are expanded in `[[ICP - Ideal Customer Profiles]]`: **A** = maritime, logistics & port services · **B** = education · **C** = healthcare · **D** = professional offices.

> **Rule from `[[Foundation Brief]]` §0.4 — do not violate.** This list of seven is a *catalog*, not a *message*. It belongs in a proposal, a pricing conversation, and this file. It must never appear as a headline, a cover image, or a social post. Seven services shouted at everybody is why the page has 74 followers.

---

## 2. Service 1 — تطبيقات الجوال / Mobile Applications

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | تطبيقات أصلية (Native) وعابرة للمنصات بنظامي Android و iOS نُهندسها لتعمل بسرعة فائقة وأداء انسيابي. |
| Website EN `stated` | Mobile Applications — native and cross-platform, Android and iOS. |
| Facebook `stated` | **تطوير تطبيقات الموبايل** — "نحول فكرتك لتطبيق قوي في إيد المستخدم" |
| Facebook 8 points `stated` | UX/UI design · iOS & Android · high performance · API/DB/payment integration · security · scalability · pre-launch testing · continuous support |

### In plain language `proposed`

A phone app your customers or your staff install and open. Two ways to build it: **native** (a separate program written for iPhone and another for Android — fastest, most expensive) or **cross-platform** (one codebase that produces both — cheaper, ~90% as good for most business apps). Code Square does both and should default to cross-platform unless the app needs heavy camera, offline, or hardware work.

### What is included `proposed`

| Included | Notes |
|---|---|
| Discovery workshop and feature prioritisation | Phase 1 التأسيس of the 4-phase methodology |
| UI/UX design of every screen in the agreed scope | Delivered as a Figma prototype before any code |
| One codebase producing Android + iOS builds | Native only if the signed scope says native |
| Connection to one backend (**API** — see glossary) | Either Code Square's or the client's existing one |
| User accounts, roles, and permissions | Standard login/registration |
| Push notifications | Basic setup, not a campaign tool |
| Integration with **one** payment gateway | e.g. Paymob, Fawry, Stripe — one, named in the SOW |
| Testing on a defined device matrix | Named devices/OS versions listed in the SOW, not "all phones" |
| Store submission support | Preparing and uploading the build |
| 30-day post-launch defect warranty | Bugs against agreed scope, fixed free. New requests are change requests |

### What is explicitly excluded `proposed`

| Excluded | Why / what to do instead |
|---|---|
| App Store and Play Store **developer account fees** | Client pays Apple/Google directly and owns the accounts |
| Store **review rejections caused by the client's business model** | e.g. a category Apple bans; not Code Square's risk |
| Content, product photography, copywriting, translation | Client provides. Can be quoted separately |
| Ongoing hosting, server, and third-party subscription costs | Client's accounts, client's card. See §9 |
| App Store Optimisation, ads, user acquisition | Not a Code Square service line |
| Support after the 30-day warranty | That is Service 7, on a retainer |
| Backend build, if the SOW says "connect to existing" | A new backend is Service 2 or 3, priced separately |
| Support for OS versions older than the SOW matrix | |
| Unlimited design revision rounds | Two rounds included; a third is a change request |

### Typical duration `proposed`

| Size | Range | What that buys |
|---|---|---|
| Small / **MVP** | 6–10 weeks | 3–5 core screens, one user type, one integration |
| Medium | 10–16 weeks | Multiple user roles, payments, dashboard |
| Large | 16+ weeks | Offline mode, complex sync, several integrations |

`TBD — founder must confirm against real team capacity.` These ranges assume the team size in `[[Delivery Process]]`, which is itself `TBD`.

### What the client must provide

Brand assets · content and copy · a **single named decision-maker** with authority to approve · access/credentials for any system to be integrated · their own store, payment gateway, and hosting accounts · test users · feedback within the agreed SLA (default: 3 working days per review gate).

> The single most common cause of a late project is not engineering — it is a client review that takes 3 weeks. This is why the SOW puts a clock on client feedback. See `[[Scoping and Estimation Guide]]` trap #4.

### Definition of "done" `proposed`

The signed scope's screens function on the named device matrix, the acceptance criteria in the SOW pass, the build is submitted to both stores, the source code and accounts are handed to the client, and the client has signed the acceptance form. Store *approval* is not part of "done" — approval is Apple's and Google's decision, not Code Square's.

---

## 3. Service 2 — تطوير الويب والمنصات / Web & Platform Development

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | بناء تطبيقات ويب متطورة وقابلة للتوسع باستخدام أحدث الأطر البرمجية، من النماذج الأولية إلى الأنظمة المؤسسية. |
| Website EN `stated` | "From MVPs to robust enterprise portals." |
| Facebook `stated` | **تطوير المواقع والمنصات** — "نحول فكرتك إلى منصة رقمية قوية تدعم نمو أعمالك" |
| Facebook 8 points `stated` | professional interfaces · responsive · speed · system integration · easy content management · security · scalability · continuous support |

### In plain language `proposed`

Everything that runs in a browser. This service line covers three genuinely different products that must never be quoted as if they were the same thing:

| Sub-type | What it is | Who buys it |
|---|---|---|
| **Marketing website** | Pages that explain a business. No logins, no data. | Any segment; a low-ticket entry |
| **Web application** | Staff or customers log in and *do work*: bookings, records, tracking. This is what El Shoush Travel and Osama Sakr actually are. | A — maritime/logistics, D — offices |
| **Internal operating system** | The web app replaces the company's spreadsheets end to end. The `[[Foundation Brief]]` positioning statement — "the operating system your business actually runs on" — is sold here. | A, C |

**Sales note:** the second and third rows are where the money and the differentiation are. The first row is a commodity that a freelancer or a template shop will always undercut. Do not lead with it. See `[[Sales Playbook]]`.

### What is included `proposed`

Discovery and requirements document · information architecture · UI/UX design of agreed screens · responsive front end (works on phone, tablet, desktop) · backend and database · user accounts, roles, permissions · admin dashboard · content management for the pages the SOW names · one third-party integration (named) · **CI/CD** deployment pipeline (see glossary) · basic **SEO** technical setup (sitemap, robots.txt, per-page meta) · security basics: HTTPS, hashed passwords, input validation at every boundary · testing · deployment to the client's hosting · handover documentation · 30-day defect warranty.

> ⚠️ **Internal irony to fix before selling this.** Code Square's own site currently ships with an **expired TLS certificate**, no sitemap, no robots.txt, and no server-side rendering (`[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`). Every item in that "included" list is one Code Square is failing on its own property. `[[Foundation Brief]]` §9 Priority 0. Fix it before quoting it.

### What is explicitly excluded `proposed`

Content writing, translation, photography, video · hosting/domain/certificate **fees** (client's accounts — but Code Square should offer to *manage* them under Service 7) · SEO content strategy, link building, ads · data migration from an old system unless a migration line item is in the SOW · integrations beyond the one named · training beyond one handover session · legal pages (privacy policy, terms) — the *text* is the client's lawyer's job, Code Square only publishes it · accessibility certification to a formal standard unless scoped · load/performance guarantees beyond the SOW's stated numbers.

### Typical duration `proposed`

| Size | Range |
|---|---|
| Marketing site | 2–4 weeks |
| Web application (small) | 8–12 weeks |
| Web application (medium) | 12–20 weeks |
| Internal operating system | 20+ weeks, always phased |

`TBD — founder must confirm.`

### What the client must provide

Named decision-maker · content · brand assets · access to the systems being replaced (including **exports of existing data**, in a readable format) · hosting/domain accounts · the real users for testing · feedback in 3 working days.

### Definition of "done"

Agreed screens and workflows pass the acceptance criteria in the SOW, on the production URL, on the client's hosting, with the client's data loaded (if migration was scoped), documentation handed over, one training session delivered, acceptance form signed.

---

## 4. Service 3 — أنظمة SaaS المخصصة / Custom SaaS Systems

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | منصات سحابية متعددة المستأجرين مصممة للنمو السريع مع دمج أنظمة الفوترة وإدارة المستخدمين المتقدمة. |
| Website tags `stated` | Multi-tenant Logic · Stripe Integration |
| Facebook `stated` | **أنظمة SaaS** — "نحول فكرتك إلى نظام SaaS جاهز للنمو" |
| Facebook 8 points `stated` | system design · cloud (⚠️ 99.9% uptime claim) · subscription & plan management · scalable performance · data security & backup · smart dashboards · API integration · ongoing updates |

> 🔴 **Hard rule.** The Facebook SaaS infographic shows sample tiers of **$19 / $49 / $99 per month**. `[[2026-09-02 - Facebook Page Evidence]]` records these as **mockup art inside a screenshot of a fake product**. They are not Code Square's prices, not a client's prices, and not a benchmark. **They must never be quoted, screenshotted into a proposal, or referenced in a sales call.** Repeated in `[[Pricing and Packaging]]` §11 because it is the single most likely accidental price commitment in the company.

### In plain language `proposed`

**SaaS** = software a customer *rents monthly* instead of buying once. **Multi-tenant** = one single copy of the software serves many separate customer companies, each seeing only its own data. Building multi-tenant is meaningfully harder than building a system for one company, because every single database query has to be certain it never leaks company A's data to company B.

**This service has two completely different buyers.** Quoting them the same way is a commercial error:

| Buyer | What they want | Risk to Code Square |
|---|---|---|
| **A founder with a product idea** | Build my startup | High. Often underfunded, scope-hungry, may want equity instead of cash. This is where agencies die. |
| **An existing business productising its own tool** | Turn the system we already run into something we sell to peers | Much lower. Funded from an operating business, real users already exist. |

**Prefer the second buyer.** Techno Square (`[[Foundation Brief]]` §3) is exactly this pattern, already proven, and is the demo asset for it.

### What is included `proposed`

Product discovery and feature prioritisation · multi-tenant architecture design (the data-isolation model, written down and reviewed) · UI/UX · web application · tenant onboarding and provisioning · subscription plan management · **billing integration with one named gateway** · usage limits and plan enforcement · admin/superadmin console · per-tenant dashboards and reports · **API** for integrations · automated backups · deployment pipeline (**CI/CD**) · security review of the tenant-isolation boundary · handover documentation · 30-day defect warranty.

### What is explicitly excluded `proposed`

Cloud/hosting bills (client's account, client's card — a real SaaS runs $100s/month and clients are routinely shocked by this) · payment-gateway fees and merchant account approval · **the client's own pricing decisions** (Code Square builds the plan machinery; what a plan costs is the client's call, and Code Square should say so in writing) · go-to-market, marketing, sales · SOC 2 / ISO / HIPAA certification · a formal uptime **SLA** unless a signed SLA document exists — see the ⚠️ below · unlimited tenants at a fixed price where cost scales per tenant · white-labelling per tenant unless scoped · mobile app (that is Service 1).

> ⚠️ **The 99.9% uptime claim.** `[[Foundation Brief]]` §5 bans it until a real SLA exists. 99.9% permits ~43 minutes of downtime per month; committing to it contractually means monitoring, on-call rotation, and credits when you miss. Code Square has none of these documented. **Remove the claim from the infographic, or build the SLA.** Tracked in `[[Open Questions and Decisions Needed]]`.

### Typical duration `proposed`

Discovery + architecture 2–3 weeks · V1 (single-tenant proof) 10–16 weeks · multi-tenant + billing 6–10 weeks more. Always phased, never one lump. `TBD — founder must confirm.`

### What the client must provide

A named product owner (not a committee) · the pricing and plan structure they want to sell · their payment gateway and cloud accounts · legal terms and privacy policy · first design-partner customers to test with · decisions within 3 working days.

### Definition of "done"

A phase is done when its acceptance criteria pass in production, with at least one real tenant onboarded end to end including a successful billing event. "SaaS" is never "done" — the model is phase → phase → retainer.

### ICP fit

Product founders (with capital) and B — Education. **C — Healthcare** is a strong second-wave fit given the founder's pharmacy background: a multi-tenant pharmacy or clinic operations system is the single most defensible SaaS Code Square could build. It requires one pilot first (`[[Foundation Brief]]` §7.3).

---

## 5. Service 4 — حلول الذكاء الاصطناعي والأتمتة / AI & Automation Solutions

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | أنظمة أتمتة ذكية لرفع كفاءة سير العمل. ندمج نماذج LLM المتطورة مباشرة في قنوات البيانات الخاصة بك. |
| Website tags `stated` | Machine Learning · RAG Pipelines · LLM integration |
| Facebook `stated` | **حلول الذكاء الاصطناعي والأتمتة** — "نحول فكرتك إلى حلول AI وأتمتة ذكية تخدم نمو أعمالك" |
| Facebook 8 points `stated` | smart chatbot · process automation · smart analytics · data-driven recommendations · system integration · data security · scalability · continuous updates |

### In plain language `proposed`

Two very different things are bundled under one name here, and the cheaper one is where the money actually is:

| | **Automation** | **AI** |
|---|---|---|
| What it does | Removes repeated manual steps: this form arrives → create this record → send this WhatsApp → update this sheet | Reads unstructured text/images and answers, classifies, drafts, or summarises |
| Predictability | High. Deterministic. Testable. | Lower. Probabilistic. It is sometimes wrong, by design. |
| Time to value | Days to weeks | Weeks to months |
| Sell it as | **Sell this first.** It is fast, provable, and produces a number ("6 hours a week back") | Sell after automation has earned trust |

**Recommendation `proposed`:** lead every AI conversation with automation. A shipped automation that saves a maritime crewing clerk 6 hours a week is the exact "number" `[[Foundation Brief]]` §7.2 says the company is missing.

**RAG** (Retrieval-Augmented Generation) = before the AI answers, the system searches *the client's own documents* and gives the AI those passages to answer from. It is how you stop an AI inventing answers about a company's own policies. See glossary.

### What is included `proposed`

Process mapping of the current manual workflow (before automating it, write it down) · a **measured baseline** — how long the task takes today, how often it errors (this is non-negotiable; without a baseline there is no proof and no case study) · automation build and integration into existing systems · for AI: data preparation, prompt/pipeline design, RAG index over client documents, evaluation set with pass/fail examples · human-in-the-loop review step where the output is consequential · monitoring and logging · cost-per-run estimate · handover and training · 30-day defect warranty.

### What is explicitly excluded `proposed`

**Ongoing model/API usage fees** (OpenAI, Anthropic, etc. — client's own account and card; these are per-use and can rise with volume) · accuracy *guarantees* — Code Square commits to a measured accuracy on a defined evaluation set, never to "it will always be right" · responsibility for decisions the client takes on AI output · data labelling at scale · training a foundation model from scratch · regulatory/clinical approval of any AI touching patient care · integrations with systems that have no API and no export (see §9) · unlimited prompt tuning after acceptance.

> ⚠️ **Healthcare warning.** If segment C is opened, an AI feature touching diagnosis, dosing, or dispensing decisions carries regulatory and liability exposure that a small agency should not absorb. Default to automation and record-keeping; keep clinical judgement with the licensed human, in writing, in the SOW. Founder is a pharmacist and should set this line personally.

### Typical duration `proposed`

Automation pilot 1–3 weeks · AI assistant / RAG pilot 3–6 weeks · production rollout 6–12 weeks. `TBD — founder must confirm.`

### What the client must provide

Access to the real process and the person who performs it · sample data (with permission to use it) · document corpus for RAG · their own AI provider account · a named person to judge whether output is acceptable · sign-off on what the AI is allowed to do unsupervised.

### Definition of "done"

The automation runs on real data for an agreed observation period (default 2 weeks) at or above the agreed success rate, the before/after numbers are recorded, and the client signs acceptance. **The recorded before/after number is a mandatory deliverable, not a nice-to-have** — it is the proof asset (`[[Foundation Brief]]` §7).

---

## 6. Service 5 — تصميم الـ UI/UX / UI/UX Design

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | واجهات تجمع بين الجمالية الفائقة وسهولة الاستخدام المطلقة، تهدف للحفاظ على كثافة تفاعل المستخدمين. |
| Website tags `stated` | Figma Prototyping · User Research · ⚠️ "Awwwards-tier" |
| Facebook `stated` | **تصميم UI/UX** — "نحول فكرتك إلى تجربة رقمية احترافية وسهلة الاستخدام" |
| Facebook 8 points `stated` | user research · professional interfaces · easy & attractive UX · wireframes & prototypes · responsive · user-journey optimization · high usability · continuous improvement |
| Facebook post `stated` | "المستخدم أول حاجة بيشوفها الـUI، لكن الحاجة اللي بتخليه يرجع تاني هي الـUX." |

> ⚠️ **"Awwwards-tier" is banned** by `[[Foundation Brief]]` §5 unless Code Square has actually been recognised by Awwwards. Remove from the site.

### In plain language `proposed`

**UI** = what it looks like. **UX** = whether it makes sense to use. Code Square's own Facebook post says it better than any copy this vault could write — reuse it.

Sold two ways:
1. **As a phase inside a build.** Always included in Services 1, 2, 3.
2. **As a standalone offer.** Redesigning an existing ugly or confusing system, or producing a clickable prototype the client uses to raise money or get internal buy-in.

The standalone version is commercially useful out of all proportion to its size: it is small, fast, low-risk for the buyer, and it is the natural paid step for a prospect who is not ready to commit to a build. See `[[Offer Ladder]]` — this is close cousin to the Blueprint rung.

### What is included `proposed`

Stakeholder interviews · user research proportional to budget (from 3 interviews to a full study — the SOW states the number) · user journey map · information architecture · wireframes (grey-box layouts, structure before beauty) · visual design of the agreed screen count — **screen count is the unit; never sell "the design of the app"** · a clickable Figma prototype · responsive layouts for the agreed breakpoints · a design system / component library where the screen count justifies it · developer handover file with specs · **two revision rounds**.

### What is explicitly excluded `proposed`

Implementation/coding (that is Services 1–3) · illustration, 3D, motion design, video unless scoped · logo and brand identity creation · copywriting and translation · stock asset licences (client buys) · usability testing with recruited participants unless scoped · unlimited revisions — the third round is a change request · screens discovered after the count is agreed · print/collateral design.

> **The screen count is the commercial fence.** "Design our system" is unbounded. "Design these 14 screens, two revision rounds, extra screens at the rate in the SOW" is a deliverable. `[[Scoping and Estimation Guide]]` trap #2.

### Typical duration `proposed`

Prototype sprint (5–8 screens) 1–2 weeks · full product design (15–30 screens) 3–6 weeks · design system 2–4 weeks. `TBD — founder must confirm.`

### What the client must provide

Brand assets and any existing guidelines · access to real users for research · content and real data examples (design against real content, never lorem ipsum) · one named approver · feedback in 3 working days.

### Definition of "done"

Agreed screen count delivered in Figma, prototype clickable through the agreed journeys, handover file complete, two revision rounds consumed or waived, acceptance signed.

---

## 7. Service 6 — تكامل الأنظمة (IoT) / System Integration (incl. IoT)

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | ربط مصفوفات الـ IoT والأنظمة الذكية، وتوحيد نقاط النهاية في لوحات تحكم مركزية لمراقبة الأداء لحظياً. |
| Website tags `stated` | IoT protocols · observability dashboards |
| Facebook `stated` | **تكامل الأنظمة** — "نربط الأنظمة والأجهزة والبيانات في منظومة واحدة تعمل بكفاءة" |
| Facebook 8 points `stated` | system-to-system integration · APIs & databases · IoT/smart device connection · real-time data flow · process automation · security · scalability · ongoing support |

### In plain language `proposed`

Making systems that were never designed to talk to each other, talk to each other. The client already has an accounting package, a spreadsheet, a WhatsApp workflow, and maybe some hardware; the data is re-typed by a human between them. Integration removes the human re-typing.

**IoT** = physical devices (sensors, trackers, gates, scales, temperature probes) that send data over a network. In a port city this is genuinely valuable: container tracking, gate access, fuel and cold-chain monitoring. For segment C, cold-chain temperature logging for pharmacies and vaccine fridges is a real, regulated, unserved need.

> **This is the highest-risk service line in the catalog.** Every other service is mostly under Code Square's control. Integration is mostly *not*: it depends on a third party's API, documentation, uptime, rate limits, permission grants, and goodwill. Price it accordingly — see `[[Pricing and Packaging]]` §4, where **time & materials is the recommended default** for this line, and `[[Scoping and Estimation Guide]]` risk multiplier for third-party integration.

### What is included `proposed`

**A paid discovery/feasibility step before any fixed commitment** (see below) · integration architecture design · connectors between the named systems · data mapping and transformation · error handling, retries, and a dead-letter path for failed records · logging and an alert when a sync breaks · monitoring dashboard · for IoT: device connectivity, protocol handling, ingestion pipeline, real-time dashboard · security of credentials and data in transit · documentation · 30-day defect warranty.

### What is explicitly excluded `proposed`

**Hardware purchase, shipping, customs, and installation** (client buys; Code Square may advise on specification) · third-party licence, API, and connectivity/SIM fees · fixing the *third-party's* outages, breaking changes, or undocumented behaviour — remediation of a vendor-side change is a change request · integration with systems that expose **no API and no export** (see §9) · migrating historical data unless scoped · physical device maintenance and field callouts · anything requiring a partnership agreement the client has not obtained · guaranteed sync latency beyond the number stated in the SOW.

### The mandatory feasibility gate `proposed`

**Never quote a fixed price for an integration against a system Code Square has not personally seen the API documentation for.** The pattern:

1. Small paid feasibility step (1 week, fixed) — obtain docs and sandbox credentials, prove one record moves end to end.
2. Only then quote the build, fixed price.

If the client refuses to pay for step 1, quote the whole thing time & materials or walk away. An integration quoted blind is the classic way an agency turns a profitable project into a loss. `[[Scoping and Estimation Guide]]` trap #6.

### Typical duration `proposed`

Feasibility 1 week · simple two-system integration 2–4 weeks · multi-system hub 6–12 weeks · IoT pilot (few devices) 4–8 weeks · IoT production rollout `TBD` — driven entirely by hardware and site conditions. `TBD — founder must confirm.`

### What the client must provide

Written permission and credentials from **every** third-party vendor · API documentation and a sandbox environment · a technical contact at each vendor · physical site access for IoT · the hardware itself · sample data · a named approver.

### Definition of "done"

Data flows correctly between the named systems for an agreed observation period (default 2 weeks) at the agreed volume and latency, failures alert correctly, runbook handed over, acceptance signed.

---

## 8. Service 7 — الدعم والصيانة / Support & Maintenance

### Published description

| Source | Verbatim |
|---|---|
| Website `stated` | صيانة ما بعد الإطلاق لضمان استمرارية الأداء الفائق والسرعة الرقمية القصوى مع مراقبة السيرفرات عالمياً. |
| Website tags `stated` | ⚠️ SLA Guarantees · global server monitoring |
| Facebook `stated` | **خدمات الدعم والصيانة** — "مش بنسلم ونمشي... إحنا مكملين معاك" |
| Facebook 8 points `stated` | continuous support · fast response · performance monitoring · updates & improvements · security · long-term stability · ⚠️ 99.9% uptime |

> ⚠️ Both **"SLA Guarantees"** and **"99.9% uptime"** are banned by `[[Foundation Brief]]` §5 until a signed SLA document exists that Code Square can actually honour. See §10 below for what an honest first SLA looks like.

### In plain language `proposed`

**This is the most important service line in the company and it is currently listed last.**

Reasons:
- It is the only **recurring revenue** in the catalog. Project revenue restarts at zero every month; retainer revenue does not.
- It is where the **"Outsourced CTO"** positioning (`[[Foundation Brief]]` §3, website differentiator #7) is actually *delivered* rather than merely claimed. You cannot be someone's technology partner in a 10-week engagement and then vanish.
- The Facebook line **"مش بنسلم ونمشي... إحنا مكملين معاك"** is the best sentence Code Square has written about it. Keep it.

Rename it in sales conversations. "Maintenance" sounds like a cost. **"فريقك التقني الشهري / Your monthly technology team"** is what it actually is. Structure in `[[Pricing and Packaging]]` §6.

### What is included `proposed` — varies by tier

Tier structure and inclusions are defined in `[[Pricing and Packaging]]` §6. The building blocks:

| Component | What it means in plain language |
|---|---|
| Uptime monitoring | An automated check that the system is alive, alerting Code Square before the client notices |
| Defect fixes | Something that used to work stopped working — fixed under the retainer |
| Security patching | Updating the underlying libraries when a vulnerability is announced |
| Backup verification | Not just taking backups — periodically *restoring* one to prove it works |
| Dependency/OS updates | Keeping the platform current so it does not rot |
| Included change hours | A monthly bucket of hours for small improvements. Unused hours **do not roll over** (see below) |
| Monthly report | What broke, what was fixed, what was used, what is recommended next |
| Quarterly technology review | The actual Outsourced CTO conversation: roadmap, risk, cost |
| Response and resolution targets | The **SLA** — see §10 |

### What is explicitly excluded `proposed`

New features and new modules beyond the included hours (quoted as change requests or a new phase) · third-party hosting, licence, and API fees · problems caused by **the client's own changes** to the system or by another vendor · data loss from client action · complete rebuilds or re-platforming · **on-call outside stated support hours** unless the tier includes it · support for systems Code Square did not build, unless a paid takeover audit has been completed first (see below) · training beyond the included hours · unlimited users on the client's own helpdesk — support is via one named client contact.

### The inherited-system rule `proposed`

**Never take over maintenance of a system Code Square did not build without a paid takeover audit first** (1 week, fixed price). You are otherwise assuming unlimited liability for an unknown stranger's code, and the first month will consume the whole year's margin. The audit produces a written risk register and *then* a retainer quote — or a polite refusal.

### Typical duration

Rolling monthly with a minimum initial term. Recommended minimum term: **3 months** `proposed`. Notice period `TBD — founder must set` (30 days recommended).

### What the client must provide

One named contact who raises all requests through one named channel · production access · their own hosting/vendor accounts and payment · notice before they or another vendor change anything · timely renewal payment.

### Definition of "done"

Never. That is the point — and it is why the retainer must have a *review* cadence rather than an end date. Each month is "done" when the report is delivered and the SLA targets were met or the misses are explained.

### The attach rule `proposed`

**Every build proposal must contain a retainer line.** Not as an upsell after handover — as a line in the original proposal, presented as the normal way software is owned. A system with no maintenance line is a system the client will watch decay and then blame Code Square for.

Target: **80% of completed builds convert to a retainer.** Track in `[[Offer Ladder]]`.

---

## 9. Cross-cutting terms that apply to every service `proposed`

These belong in every SOW. See `[[Proposal and SOW Template]]` §9–§12.

| Term | Position |
|---|---|
| **Third-party costs** | Always the client's, on the client's accounts, in the client's name. Code Square never fronts a subscription. If Code Square manages them, that is a retainer service, and the bills still go to the client. |
| **Account ownership** | Domain, hosting, stores, payment gateway, AI provider, cloud — **all registered to the client from day one.** Never in Code Square's name "for convenience". It creates a hostage relationship neither party wants and a mess at handover. |
| **IP ownership** | On full payment, the client owns the custom code and the deliverables. Code Square retains its pre-existing tools, libraries, and internal frameworks, licensed to the client perpetually for use in the delivered system. Wording in `[[Proposal and SOW Template]]` §10. |
| **Data ownership** | The client's data is the client's, always. Code Square is a processor, not an owner. Export on request in a standard format, at any time, at no charge. |
| **Portfolio rights** | Code Square may name the client and show the work — **unless the client opts out in the SOW.** Get this at signature; asking 8 months later is how `[[Foundation Brief]]` §7.1 became a blocker. |
| **Outcome numbers** | The SOW includes the client's agreement to share before/after metrics for a case study. This is a *deliverable of the project*, not a favour. |
| **Systems with no API** | If a system Code Square must integrate with has no API and no export, that is a hard scope boundary. Screen-scraping and robotic re-typing are refused: they break silently, they are fragile, and Code Square carries the blame. |
| **Client feedback SLA** | 3 working days per review gate. Beyond that, the timeline moves day for day, stated in writing at the time, not at the end. |
| **Warranty** | 30 days post-acceptance, defects against agreed scope only. Not a free change window. |
| **Change requests** | Every scope change is written, estimated, priced, and signed before work starts. No verbal scope. `[[Pricing and Packaging]]` §8. |

---

## 10. The SLA problem — an honest first version `proposed`

Code Square currently publishes "SLA Guarantees" and "99.9% uptime" with no SLA document, no monitoring, no on-call rota, and no credit mechanism. That is a claim without a proof path, which `[[Foundation Brief]]` §0.5 forbids.

An honest first SLA commits only to **response**, not to uptime:

| Severity | Plain meaning | Response target |
|---|---|---|
| S1 — Critical | System down, or money/data at risk | `TBD` — recommend 4 working hours |
| S2 — High | Major function broken, workaround exists | `TBD` — recommend 1 working day |
| S3 — Normal | Something is wrong but work continues | `TBD` — recommend 3 working days |
| S4 — Request | Small change or question | Within the month's included hours |

**Response** = a human has acknowledged and started. **Resolution** targets and any **uptime** commitment come later, once monitoring and an on-call rota exist. Support hours `TBD — founder must set`; a two-person company cannot honestly promise 24/7.

Until then: **delete the uptime number from the infographic and the site.** Tracked in `[[Open Questions and Decisions Needed]]`.

---

## 11. Which services to actually lead with `proposed`

Seven services is a catalog, not a strategy. Against the `[[Foundation Brief]]` §4 beachhead recommendation (A — maritime/logistics, with B — education in parallel):

| Rank | Lead with | Why |
|---|---|---|
| 1 | **Service 2 (web applications) + Service 7 (retainer)** | This is the Osama Sakr and El Shoush pattern — the work Code Square has actually shipped for external paying clients, in the beachhead segment, with a nameable reference. Sell what you have proof of. |
| 2 | **Service 4, automation half only** | Fastest way to a *number* for a case study. Small, cheap, provable. |
| 3 | **Service 5 standalone + Service 6 feasibility** | Small paid steps that qualify a buyer without a big commitment. Feeds the Blueprint rung. |
| 4 | Services 1 and 3 | Real capability, but longer, riskier, and no cheaper than competitors. Sell on demand, do not lead. |

---

## 12. Glossary — every term in this file, in plain language

Written for a reader who is a pharmacist, not a programmer. Use these definitions verbatim with clients; they work.

| Term | Plain-language definition |
|---|---|
| **MVP** (Minimum Viable Product) | The smallest version of a product that a real person can actually use to get a real result. Not a demo, not a prototype — a real, working, deliberately small product. You ship it to learn what to build next, instead of guessing for a year. Code Square's own Facebook post makes the argument well: in a booking app, 80% of users only needed *search, book, confirm*. |
| **SaaS** (Software as a Service) | Software rented monthly rather than bought once. The vendor runs it on their servers; the customer logs in through a browser. Gmail is SaaS. The opposite is software you install and own forever. |
| **Multi-tenant** | One single copy of a program serving many separate customer companies at once, where each company sees only its own data. Like one pharmacy building with many locked rooms and one set of plumbing — cheaper to run than a separate building each, but the locks have to be perfect. Building the locks correctly is most of the extra cost of SaaS. |
| **API** (Application Programming Interface) | A defined doorway that lets one program ask another program for something, without a human retyping it. Your insurance-claim system asking the ministry system "is this card valid?" and getting an answer back in a second is an API. If a system has no API, connecting to it is expensive or impossible. |
| **RAG** (Retrieval-Augmented Generation) | A way to make an AI answer from *your own documents* rather than from what it vaguely remembers from the internet. Before answering, the system searches your files and hands the AI the relevant pages. This is how you get an AI that can answer questions about your own policies and stops inventing things. |
| **LLM** (Large Language Model) | The kind of AI behind ChatGPT and Claude — it reads and writes text. Powerful, and confidently wrong sometimes. That is why anything consequential needs a human check step. |
| **CI/CD** (Continuous Integration / Continuous Deployment) | An automated production line for software. When a developer finishes a change, the system automatically tests it and, if the tests pass, publishes it. Replaces a manual, error-prone release ritual. It is why some teams ship weekly without drama. |
| **SLA** (Service Level Agreement) | A written, contractual promise about *speed of service* — how fast someone responds when something breaks, and what the client gets if that promise is missed. If there is no document and no consequence, there is no SLA, only marketing. |
| **IoT** (Internet of Things) | Physical objects with sensors that send data over a network: a temperature probe in a vaccine fridge, a tracker on a container, a smart gate at a port. |
| **Native / Cross-platform** | Native = a separate app written specifically for iPhone and another for Android. Cross-platform = one codebase that produces both. Cross-platform is cheaper and fine for most business apps. |
| **Backend / Frontend** | Frontend = what the user sees and clicks. Backend = the engine and database behind it, storing data and enforcing rules. A design without a backend is a picture. |
| **Retainer** | A fixed monthly fee for ongoing access to the team — support, fixes, and a set number of improvement hours. Predictable for the client, predictable for Code Square. |
| **T&M** (Time & Materials) | Billing for actual hours worked rather than a fixed total. Right when the scope genuinely cannot be known in advance. |
| **Scope** | The written list of exactly what will be built. "In scope" gets built for the agreed price; "out of scope" is a new conversation. Most disputes in this industry are scope disputes. |
| **Change request** | A written, priced, signed agreement to add or alter something after the scope was agreed. The alternative — saying yes verbally — is how agencies work for free. |
| **Discovery** | The paid first phase where you work out what should actually be built, before building it. Code Square calls it **التأسيس**. |
| **Wireframe / Prototype** | Wireframe = a grey-box sketch of a screen's structure, no colours. Prototype = clickable screens that feel like the real thing but are not built yet. Both exist to let you change your mind while changing your mind is still cheap. |
| **Acceptance criteria** | The specific, testable list that decides whether a deliverable counts as finished. Written *before* the work, agreed by both sides. Without it, "done" is an opinion. |
| **Tenant** | In multi-tenant SaaS, one customer company and all of its data. |
| **Staging / Production** | Staging = a private copy for testing. Production = the live system real people use. |

---

## Related

[[Foundation Brief]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Proposal and SOW Template]] · [[Scoping and Estimation Guide]] · [[ICP - Ideal Customer Profiles]] · [[Sales Playbook]] · [[Delivery Process]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]] · [[2026-09-02 - Facebook Page Evidence]]
