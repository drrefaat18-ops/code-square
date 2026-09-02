---
date: 2026-09-02
type: market-analysis
tags:
  - market
  - icp
  - segmentation
  - code-square
ai-first: true
status: draft
owner: TBD
---

# ICP — Ideal Customer Profiles

## For future Claude

This note profiles the **four candidate segments** named in `[[Foundation Brief]]` §4 (A maritime/logistics, B education, C healthcare, D professional offices). It does **not** pick the winner — that is `[[Beachhead Decision]]`. It does not set prices — that is `[[Pricing and Packaging]]`.

Every line is tagged: **stated** (from Code Square's own evidence notes) · **researched** (external, URL + date) · **proposed** (analysis, 2026-09-02) · **TBD** (unknown, founder must answer).

If the founder later confirms a real client list, real pricing, or real close rates, **update this note and downgrade the `proposed` labels to `stated`**. Never invent a client, a revenue figure, or a headcount for Code Square.

---

## Jargon glossary (read this first)

The reader of this vault is a pharmacist, not an MBA. Terms used below, defined once:

| Term | Plain meaning |
|---|---|
| **ICP** (Ideal Customer Profile) | A description of the *type of company* worth selling to. Not a person — a company shape. |
| **Firmographics** | Company facts: size, revenue, headcount, location, industry. Like "demographics", but for businesses. |
| **Trigger event** | Something that just happened to the company that makes them suddenly willing to spend. Without a trigger, even a perfect-fit company does nothing. |
| **Economic buyer** | The person who can say yes to the money. |
| **Blocker** | The person who cannot say yes, but can say no — usually the operations manager or the accountant. |
| **Sales cycle** | Time from first contact to signed contract. |
| **Ticket size** | The money in one deal. |
| **Disqualifier** | A reason to walk away. A segment with no disqualifiers is not a segment, it is a wish. |
| **Manning / crewing agency** | A company that recruits, documents, and rotates ship crews for shipowners. |
| **Freight forwarder** | Arranges cargo movement door-to-door; does not own ships. |
| **Customs broker** (مخلص جمركي) | Clears goods through customs on the importer's behalf. |
| **Ship chandler** | Supplies food, spares, and stores to ships in port. |
| **Bunkering** | Selling and delivering marine fuel to ships. |
| **Port call** | One vessel's complete visit to a port, from arrival to departure. |
| **Disbursement Account (DA)** | The estimate, then the final bill, of everything a port agent spent on behalf of a vessel. |

---

## The two questions every ICP must answer

1. **Who has an expensive, repeating, manual workflow** that software removes?
2. **Why would they choose Code Square** over a freelancer, an ERP, or doing nothing? — and "doing nothing" is the real incumbent. See `[[Competitive Landscape]]`.

A segment that cannot answer both is not an ICP; it is just a market you happen to be able to serve.

---

## Segment A — Maritime, logistics & port services

**Status: highest value, highest defensibility. The only segment where Code Square holds a shipped reference.**

### A.1 Sub-segments (do not treat these as one market)

| Sub-segment | What they do | Software pain (proposed) | Attractiveness |
|---|---|---|---|
| **Manning / crewing agencies** | Recruit and rotate seafarers for shipowners | Crew database, certificate expiry tracking (STCW, medicals, visas), rotation planning, payroll and allotments, client reporting | ⭐⭐⭐⭐⭐ — **Code Square has already shipped this** (Osama Sakr) |
| **Shipping / port agencies** (وكالة ملاحية) | Represent the vessel in port: berthing, formalities, disbursement | Port call file per vessel, DA estimate vs final, document chase, multi-party email and WhatsApp threads | ⭐⭐⭐⭐⭐ |
| **Freight forwarders** | Arrange cargo movement | Shipment file, quote-to-booking, rate sheets, container tracking, customer status requests | ⭐⭐⭐⭐ |
| **Customs brokers** (مخلصون جمركيون) | Clear goods through Egyptian customs | Declaration status, document packs, ACI/Nafeza filings, per-client fee accounting | ⭐⭐⭐⭐ — heavily regulated, high compliance urgency |
| **Ship chandlers / suppliers** | Supply stores to vessels | Quote to delivery note, stock, vessel-by-vessel order history, foreign-currency invoicing | ⭐⭐⭐ — smaller tickets |
| **Bunkering suppliers** | Marine fuel | Nomination → delivery → Bunker Delivery Note → invoice reconciliation, price volatility | ⭐⭐⭐ — few players, big tickets, long cycles |

### A.2 Firmographics (proposed profile of the winnable company)

| Attribute | Target |
|---|---|
| Headcount | **8–60 people.** Under 8, the owner does everything and buys nothing. Over 60, they likely have an incumbent system or an in-house IT team. |
| Revenue band | **TBD** — Egyptian private maritime SMEs do not publish figures. Practical proxy: 8–60 staff and multi-currency invoicing. |
| Geography | Port Said and East Port Said first (driving distance; the founder can walk in), then Damietta, Ismailia, Suez, Ain Sokhna, Alexandria. |
| Ownership | Owner-managed or family-run, often with a second generation now entering the business. **The second generation is usually the buyer.** |
| Current tooling | Excel + WhatsApp + email + a shared network drive. Sometimes an ageing Egyptian desktop accounting package. |
| Language | Operations in Arabic; documentation and client correspondence in English. **Bilingual UI is a hard requirement**, consistent with the bilingual rule in `[[Foundation Brief]]`. |

### A.3 The painful manual workflows (proposed, grounded in the Osama Sakr project scope)

Ranked by how cleanly software replaces them:

1. **Certificate and document expiry tracking.** A crewing agency holds hundreds of seafarer certificates with hard expiry dates. Miss one and the seafarer cannot board — an immediate, countable financial loss. *Today: a colour-coded Excel sheet that one person maintains.*
2. **Port call / shipment file assembly.** One vessel call generates dozens of documents spread across email, WhatsApp, and paper. *Today: a folder per vessel on a shared drive, plus somebody's memory.*
3. **Quote or DA estimate versus final invoice reconciliation.** The gap between estimate and actual is where margin quietly leaks. *Today: two Excel files that do not reconcile.*
4. **"Where is my container / my crew / my clearance?" status requests.** Clients phone and WhatsApp; a staff member stops work to look it up. *Today: interrupt-driven, uncounted, and probably the largest hidden labour cost in the business.*
5. **Multi-currency invoicing and receivables.** Billing in USD or EUR, paying costs in EGP, collecting late.
6. **Regulatory filings** (ACI/Nafeza, customs declarations, ETA e-invoicing). *Today: manual re-keying into a government portal from an Excel row.*

### A.4 Trigger events (proposed — a perfect fit without a trigger does not buy)

| Trigger | Why it forces a decision |
|---|---|
| **Egyptian Tax Authority e-invoicing enforcement.** The VAT registration threshold dropped from EGP 500,000 to **EGP 250,000**, with registration due **31 March 2026**, an **EGP 20,000** penalty for operating unregistered plus **EGP 1,000/day** thereafter (**researched** — [orchidatax.com, 2026](https://orchidatax.com/countries-compliance/egypt-e-invoicing-compliance/); [wafeq.com](https://www.wafeq.com/en-eg/tax-and-reporting/electronic-invoice-system), accessed 2026-09-02) | A legal deadline with a daily fine attached. This is the strongest, cleanest trigger available in the Egyptian SMB market right now: every invoice-issuing business must produce structured invoice data. Excel cannot do this cleanly. |
| **A near-miss.** An expired certificate, a missed berth window, a mis-declared shipment. | Converts "someday" into "this week". Ask for it in discovery: *"آخر مرة حصل غلط كلّفكم فلوس، كان إيه؟"* |
| **Succession.** The owner's son or daughter returns from university or from abroad and is handed operations. | The new generation will not run the company on a shared drive. Highest-probability buyer inside a family firm. |
| **A key person is the system.** One employee holds everything in their head and is about to leave, retire, or has just left. | Existential. Pays fastest. |
| **A large client demands visibility.** A shipping line, a multinational shipper, or a new SCZone tenant asks for a tracking portal or an API feed. | Externally imposed, non-negotiable deadline. |
| **SCZone growth.** The Suez Canal Economic Zone drew roughly **$7bn across 117 projects** (**researched** — [AGBI, Aug 2026](https://www.agbi.com/logistics/2026/08/egypts-suez-canal-economic-zone-draws-7bn-from-investors/)); AD Ports Group signed a 50-year agreement for a 20 km² industrial and logistics park **near Port Said** (**researched** — [Baird Maritime](https://www.bairdmaritime.com/shipping/ports/ad-ports-group-suez-canal-economic-zone-to-develop-logistics-park-at-port-said), accessed 2026-09-02). | More volume through Port Said means existing agencies handle more calls with the same staff. Volume growth *is* the trigger. |

### A.5 Budget reality (proposed — must be validated; see `[[Open Questions and Decisions Needed]]`)

There is no published price list for custom maritime software in Egypt. The anchors that do exist:

- Egyptian freelance web work: **EGP 5,000–15,000** basic site, **EGP 15,000–50,000** business site; freelancer hourly **EGP 200–500** (**researched** — [novaroids.com, 2026](https://www.novaroids.com/en/eg/blogs/website-development-cost-egypt); [queentechsolutions.net](https://www.queentechsolutions.net/web-development-2/website-development-cost/), accessed 2026-09-02).
- Odoo ERP for a small Egyptian business: **EGP 125,000–350,000** all-in for a basic 5–10 user deployment (**researched** — [buildn.tech, 2026](https://buildn.tech/en/blog/erp-implementation-cost-egypt-2026)).
- Egyptian dev-shop offshore rates: **$25–$39/hr** typical, median around **$37/hr** (**researched** — [thescalers.com](https://thescalers.com/offshore-software-development-rates-by-country/); [insigniaresource.com](https://www.insigniaresource.com/research/outsourcing-rates-by-country/), accessed 2026-09-02). At roughly **EGP 51 per USD** (**researched** — [XE, 2026-09-02](https://www.xe.com/en-us/currencyconverter/convert/?Amount=1&From=EGP&To=USD)) that is about **EGP 1,275–2,000/hr**.

**Proposed working bands for Segment A** — a hypothesis to test, **not a price list**:

| Rung | Proposed band (EGP) | Note |
|---|---|---|
| Blueprint (paid discovery, 1–2 weeks) | 25,000 – 60,000 | Must be creditable against the build. See `[[Pricing and Packaging]]`. |
| V1 build (one workflow, one department) | 150,000 – 500,000 | Deliberately positioned *above* the freelancer band and *at or below* the Odoo band. |
| Monthly retainer ("Outsourced CTO") | 15,000 – 50,000 / month | Where the margin actually lives. |

⚠️ These are **proposed anchors for the founder to accept, reject, or replace.** Never quote them to a client before sign-off.

### A.6 Who signs, who blocks

| Role | Detail |
|---|---|
| **Economic buyer** | The **owner / managing director**, or in a family firm the **son or daughter running operations**. There is no procurement department at this size. |
| **Blocker** | The **operations manager** and the **head accountant**. The ops manager fears disruption during a live port call; the accountant fears the numbers not matching. Win both, or the owner's yes evaporates. |
| **Champion** | Usually the person drowning in the Excel sheet. Find them during discovery and make them the hero of the internal story. |

### A.7 Sales cycle (proposed)

**6–14 weeks** with a warm introduction. **4–8 months** cold. Maritime SMEs buy on trust and reference, not on a website.

### A.8 Why Code Square specifically can win Segment A

| Advantage | Evidence |
|---|---|
| **A shipped maritime reference in the same city** | Osama Sakr Manning Agency — recruitment, project tracking, live analytics dashboards (**stated** — `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`). No Cairo agency can say this. |
| **Physical proximity** | Port Said, شارع ممفيس (**stated**). This segment buys after a face-to-face meeting. A Cairo vendor's travel cost is Code Square's home-field advantage. |
| **Bilingual delivery** | The site already ships Arabic and English in parallel (**stated**). Maritime paperwork is English; the office floor is Arabic. |
| **"Outsourced CTO" framing already written** | Point 7 of "لماذا كود سكوير" (**stated**). These firms will never hire a CTO. They will rent one. |

### A.9 Disqualifiers — say no to these

- Fewer than roughly 8 staff, or a one-person brokerage. The workflow lives in one head; software has nothing to replace.
- Anyone who opens with *"عايز حاجة زي [X] بس أرخص"* and cannot describe a workflow. That is a freelancer job. See `[[Competitive Landscape]]`.
- Firms mid-implementation on an international maritime package. Do not fight a migration you cannot win.
- Firms whose real ask is a **website**. Refer it out or price it as a fixed micro-project; do not let it consume engineering capacity.
- Anyone who will not name an internal workflow owner. No internal owner means failed delivery, which means no case study.
- Anyone proposing equity, revenue share, or payment "after the system makes money".

### A.10 Where these buyers actually are

| Channel | Note |
|---|---|
| **Port Said Chamber of Shipping** published member list (**researched** — [pscsegypt.com/list.php](http://www.pscsegypt.com/list.php), accessed 2026-09-02; dozens of member firms — **count and segment it manually**) | **The single highest-value action in this note.** A named, addressable, local target list already exists in public. |
| ISSA Egypt / Port Said ship-supplier directory (**researched** — [shipsupply.org/country/egypt/port-said/](https://shipsupply.org/country/egypt/port-said/), accessed 2026-09-02) | Ship chandlers, named and contactable. |
| Egyptian Chamber of Shipping, customs-broker syndicates, SCZone investor events | Association membership buys credibility faster than ads in this segment. |
| **The Osama Sakr referral** | One warm introduction from an existing client outperforms every other channel in this note combined. **Ask for it.** |
| LinkedIn filters: "Operations Manager", "Crewing Manager", "Managing Director" + Port Said / Ismailia / Damietta | Thin but real in Egyptian maritime. |
| Physical presence — the agencies cluster within a small radius of the port | Unfashionable, and the highest-conversion channel available. |

---

## Segment B — Education (academies, training centres, private teachers)

**Status: the volume and demo engine. Fastest to a sale, smallest ticket.**

### B.1 Firmographics (proposed)

| Attribute | Target |
|---|---|
| Type | Private training academies, language centres, professional and exam-prep centres, tutoring سناتر, small private schools |
| Headcount | 5–40, mostly part-time instructors |
| Students | **200–3,000 enrolled per term.** Below ~200 the owner runs it on WhatsApp and a notebook and will not pay. |
| Geography | Port Said, Damietta, Ismailia, Mansoura, Cairo, Alexandria — geography-independent once the product is proven |
| Current tooling | WhatsApp groups, Google Forms, a Facebook page, an Excel attendance sheet, cash or InstaPay collection |

### B.2 Painful manual workflows

1. **Enrolment and payment collection.** Registering by WhatsApp, taking cash or InstaPay screenshots, reconciling who actually paid. Chronic revenue leakage.
2. **Group, schedule, room, and instructor allocation.** A weekly Tetris puzzle solved by hand.
3. **Attendance and progress reporting to parents.** Manual, inconsistent, and the leading cause of parent complaints.
4. **Re-enrolment for the next term.** The largest revenue event of the year, run entirely on memory and broadcast messages.
5. **Content and recording distribution.** Drive links pasted into WhatsApp, then shared outside the paying group — direct piracy loss.

### B.3 Trigger events

- **Start of term** (September, February). The buying happens in the 6–10 weeks *before* term, not during it.
- **A discovered cash leak** — students attending without having paid.
- **Opening a second branch.** Manual coordination breaks the moment there are two locations.
- **A competitor academy launches an app.** Parent-facing prestige pressure is real and moves fast in this market.
- **ETA e-invoicing** applies here too once revenue passes EGP 250,000 (see A.4).

### B.4 Budget, signer, cycle

| | Detail |
|---|---|
| Budget (proposed) | **EGP 40,000 – 150,000** V1; **EGP 3,000 – 12,000/month** retainer. Some buyers will only accept **per-student or per-month SaaS** pricing — a different business model with a different cashflow shape. Decide this deliberately in `[[Pricing and Packaging]]`. |
| Economic buyer | The **academy owner**, almost always one individual and often the founding teacher. |
| Blocker | The **admin and reception staff** who currently *are* the system, plus **senior instructors** who resist being measured. |
| Sales cycle (proposed) | **2–6 weeks.** The fastest of the four segments. |

### B.5 Why Code Square can win it

**Techno Square** and **Online Techno Square** are live: platform, mobile app, dashboard, enrolment flow, and a mascot (تاتا) (**stated**). Code Square can **demo working software on the first call with no client permission required**, because the group owns it (**stated**). That beats any competitor who can only show mockups.

### B.6 Disqualifiers

- Single private tutors. They will not pay and they churn. Sell them a template product or nothing.
- Anyone whose stated need is "زي منصة X بالظبط". Clone requests are unprofitable and produce no referenceable story.
- Centres under roughly 200 students.
- Anyone who wants payment deferred until enrolment revenue arrives.

### B.7 Where they are

Facebook groups for academy and training-centre owners · licensed training-centre directories (**TBD** — confirm which are public) · the physical clusters of سناتر in Port Said and Damietta · **the Techno Square network itself** — instructors, partners, and parents already inside the group are a warm list (**stated** that the group exists; **TBD** whether the list is usable and permitted).

---

## Segment C — Healthcare (pharmacies, clinics, medical centres)

**Status: highest founder fluency, zero proof. Needs exactly one pilot.**

### C.1 Firmographics (proposed)

| Attribute | Target |
|---|---|
| Type | Independent pharmacy **chains of 3–15 branches**, polyclinics, radiology and lab centres, specialist clinics |
| Headcount | 5–50 |
| Geography | Port Said, Damietta, Ismailia first — the founder's own network |
| Current tooling | An Egyptian desktop pharmacy system, a paper appointment book, WhatsApp for patient contact |

**Note the split.** Single pharmacies are already served by cheap local desktop software and are a bad target. **Small chains** are the real ICP, because nothing they own consolidates across branches.

### C.2 Painful manual workflows

1. **Multi-branch inventory and expiry visibility.** Branch A is out of a drug that Branch C is about to write off. This is money burning on a shelf and no branch can see it. **Directly quantifiable in EGP — the best possible case-study number.**
2. **Purchasing and supplier price comparison** across distributors, done from memory and WhatsApp price lists.
3. **Appointment booking and no-show follow-up** for clinics — reception phone tag.
4. **Patient recall** for chronic-disease refills and follow-up visits — high-margin revenue nobody chases because nobody has the list.
5. **Insurance and corporate-account claim paperwork.**

### C.3 Trigger events

- **Opening a third branch** — the point at which manual coordination provably fails.
- **A stock-take revealing a large expiry write-off.**
- **A regulatory or inspection incident.**
- **ETA e-invoicing and e-receipt** reaching retail businesses with multiple locations that aggregate above EGP 250,000 (**researched** — [orchidatax.com FAQ, 2026](https://orchidatax.com/eta-e-invoicing-egypt-faqs/), accessed 2026-09-02).
- **A partner or family dispute over the numbers.** The demand for a single source of truth is often about *governance*, not efficiency. Do not miss this motive.

### C.4 Budget, signer, cycle

| | Detail |
|---|---|
| Budget (proposed) | **EGP 60,000 – 250,000** V1; retainer **EGP 5,000 – 20,000/month**. Chains pay materially more than single sites. |
| Economic buyer | **Owner-pharmacist** or clinic **medical director** — usually also a practising clinician, so their time is scarce and their attention window is short. |
| Blocker | The **branch manager or head pharmacist** whose informal control the system replaces, and the **incumbent software vendor** defending their seat. |
| Sales cycle (proposed) | **4–10 weeks** through the founder's network; considerably longer cold. |

### C.5 Why Code Square can win it

The founder is a **pharmacist** (**stated** — `[[Foundation Brief]]` §3). In a first meeting he can name the workflow before the client finishes describing it. That is the fastest trust-builder available in this vault, and **a competitor cannot copy it**. The constraint is not credibility — it is that **no healthcare project has shipped yet**. One pilot fixes that.

### C.6 Disqualifiers

- Single-branch pharmacies. Served by cheap incumbents, no consolidation pain.
- Anyone asking for medical-device, diagnostic, or clinical-decision functionality. That is a regulated product class with a liability profile Code Square is not set up to carry. **Refuse it explicitly and in writing.**
- Anyone wanting patient data hosted without a written data-handling agreement. Egypt's Personal Data Protection Law (Law 151/2018) applies (**TBD** — confirm the current status of its executive regulations before signing any healthcare contract; do not rely on this note for legal advice).
- Hospitals. Wrong size, wrong procurement process, wrong cycle length.

### C.7 Where they are

The founder's own professional network — pharmacy-school cohort, syndicate contacts, distributor representatives (**stated** that the founder is a pharmacist; the network itself is **TBD**) · Pharmacists' Syndicate (نقابة الصيادلة) branch events · **pharmaceutical distributor sales reps**, who visit every pharmacy weekly and know exactly which chains are growing — the best introduction channel in this segment.

---

## Segment D — Professional offices (lawyers, accountants)

**Status: real need, no edge, no proof. An expansion market, not a launch market.**

### D.1 Profile (proposed, deliberately brief)

| Attribute | Detail |
|---|---|
| Type | Law firms, accounting and audit offices, tax consultants, engineering consultancies |
| Headcount | 3–25 |
| Pain | Case and engagement file tracking, deadline and hearing calendars, document versioning, time and billing, client status requests |
| Trigger | **ETA e-invoicing** — which hits accounting and tax offices hardest, and makes them a *channel* as well as a customer · a missed deadline · partner succession |
| Budget (proposed) | EGP 30,000 – 120,000 V1 — the lowest willingness to pay of the four segments |
| Signer | Managing partner |
| Blocker | The other partners. Partnerships decide by consensus, which is why the cycle is long for a small ticket. |
| Cycle (proposed) | 8–20 weeks — **long cycle plus small ticket is the worst combination of the four** |

### D.2 Why it is not the beachhead

No portfolio proof, no domain edge, no local advantage, and the segment is already crowded by generic practice-management SaaS and ready-made templates. `[[Foundation Brief]]` §4 rates it correctly.

### D.3 The one reason to keep it on the list

**Accounting offices are a distribution channel.** Every accounting office serves dozens of SMEs and is *right now* walking each one through ETA e-invoicing registration ahead of the 31 March 2026 deadline. A referral partnership with two or three accounting offices in Port Said reaches Segment A and Segment C buyers at the exact moment of their trigger event. **Treat Segment D as a partner channel first and a customer second.** This belongs in `[[Sales Playbook]]`.

---

## Cross-segment comparison

| | **A · Maritime** | **B · Education** | **C · Healthcare** | **D · Professional** |
|---|---|---|---|---|
| Proof held today | ✅ Osama Sakr | ✅ Techno Square | ❌ none | ❌ none |
| Proposed V1 ticket (EGP) | 150k – 500k | 40k – 150k | 60k – 250k | 30k – 120k |
| Proposed sales cycle | 6–14 wks warm | 2–6 wks | 4–10 wks | 8–20 wks |
| Competitive intensity | **Low** | High | Medium | High |
| Founder access | Medium — one client | High — group asset | **High — own profession** | Low |
| Repeatability of the build | High — same workflows recur | **Very high — product exists** | High | Medium |
| Gulf expansion potential | **High** — Jeddah Islamic Port and Dammam are the same industry | Medium | Medium | Low |
| Is there a public target list? | ✅ Chamber of Shipping | Partly | Via network only | Syndicates |

Scored and weighted in `[[Beachhead Decision]]`.

---

## Open questions this note could not answer

Add to `[[Open Questions and Decisions Needed]]`:

1. Will **Osama Sakr** and **El Shoush** give written permission to be named, and one number each?
2. What are the **real budget bands** in the website form dropdown? (**TBD** — flagged as unextracted in `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`.)
3. Does the **B2G project** exist? If yes, it materially changes Segment A's score.
4. Is the founder **full-time** on Code Square? Segment A's cycle assumes someone can attend in-person meetings on demand.
5. What is the **real delivery capacity** — how many parallel V1 builds can the team run? Headcount is **TBD** and must not be invented.
6. Is the founder's pharmacy network **actually reachable**, or is it a theoretical asset?

## Related
[[Foundation Brief]] · [[Buyer Personas]] · [[Competitive Landscape]] · [[Market Map - Egypt and Gulf]] · [[Beachhead Decision]] · [[Brand Positioning]] · [[Pricing and Packaging]] · [[Sales Playbook]] · [[Open Questions and Decisions Needed]]
