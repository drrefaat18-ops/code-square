---
date: 2026-09-02
type: guide
tags:
  - offers
  - estimation
  - scoping
  - margin
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Scoping and Estimation Guide — Code Square

## For future Claude

How to turn *"عايز تطبيق"* into a number Code Square can defend and still make money on.

Rules:
- **No Code Square day rate appears here.** The rate is blocker **B4**, unanswered. This guide produces an estimate in **days**; `[[Pricing and Packaging]]` §2 turns days into money once the founder sets the cost floor. Keeping the two separate is deliberate — it stops a rate guess from contaminating a scope estimate.
- Day ranges in §4 are `proposed` planning defaults, **not measured**. Replace them with Code Square's actual data after ~5 projects (§8).
- **Estimate ≠ quote ≠ deadline.** The estimate is engineering judgement; the quote is a commercial decision made on top of it (`[[Pricing and Packaging]]`); the deadline is what gets promised. Confusing the three is trap #9.

---

## 1. The rule that prevents most losses

> **Never give a number in the room.**

The estimate that leaves your mouth in a meeting is the number the client remembers, forever, regardless of what the written quote later says. When asked live:

> *"مش هديك رقم من غير ما أفهم الشغل كويس — الأرقام اللي بتتقال على الطاير هي اللي بتخرب المشاريع. هبعتلك رقم مكتوب خلال {{n}} أيام، أو نعمل خريطة مشروع ونطلع برقم ثابت مبني على تحليل حقيقي."*

If a range is unavoidable, give an **order of magnitude with the assumptions attached** ("systems like this are usually weeks not days, and the number depends entirely on X") — never a figure.

The paid Blueprint (`[[Offer Ladder]]` rung 2) exists precisely so that a real number can be produced safely.

---

## 2. The intake question set

Run before any estimate. Extends the Diagnostic questions in `[[Offer Ladder]]` §3 — those establish *whether* to build; these establish *how big*.

### A — The problem
1. إيه المشكلة اللي بنحلها؟ (not "what do you want built")
2. إزاي الشغل ماشي دلوقتي، خطوة بخطوة؟
3. كام واحد بيلمس العملية دي؟ وبيعملوا إيه بالظبط؟
4. لو مانعملش حاجة، هيحصل إيه؟

### B — Users and scale
5. مين هيستخدم النظام؟ **اذكر كل نوع مستخدم بصلاحياته.** ← *each user role is a multiplier, not an addition*
6. كام مستخدم في السنة الأولى؟ وبعد ٣ سنين؟
7. كام سجل / معاملة في اليوم؟
8. موبايل، ويب، ولا الاتنين؟ ولو موبايل: iOS، أندرويد، ولا الاتنين؟

### C — Data
9. البيانات موجودة فين دلوقتي؟
10. في بيانات قديمة لازم تتنقل؟ **كام سجل، وبأي صيغة، ونضيفة قد إيه؟** ← *migration is almost always underestimated; dirty data is the real cost*
11. مين اللي محتاج يشوف تقارير؟ وإيه بالظبط؟

### D — Integrations ← *the highest-risk block in the whole set*
12. النظام لازم يتكلم مع أنظمة تانية؟ **اذكرها بالاسم.**
13. كل نظام منهم عنده API موثق؟ **شوفت التوثيق بنفسك؟**
14. مين المسؤول عن كل نظام، وهل وافق فعلًا؟
15. في بيئة اختبار (sandbox)؟
16. في نظام منهم مالوش API ولا تصدير؟ ← *if yes: hard scope boundary, `[[Service Catalog]]` §9*

### E — Constraints
17. في تاريخ نهائي حقيقي؟ وسببه إيه؟ ← *"ASAP" is not a date; a contract renewal is*
18. في متطلبات تنظيمية أو قانونية؟ (خاصة قطاع C — الصحة)
19. في تكنولوجيا معينة لازم نستخدمها؟ وليه؟
20. في حد جرب يبني ده قبل كده؟ حصل إيه؟

### F — Decisions and delivery
21. مين اللي بيقبل التسليمات؟ **شخص واحد بالاسم.**
22. هيقدر يرد خلال ٣ أيام عمل؟
23. مين هيوفر المحتوى، وإمتى؟
24. مين هيشغّل النظام بعد التسليم؟

**If B, D, or F cannot be answered, do not estimate.** Sell a Blueprint, or an integration feasibility week (`[[Service Catalog]]` §7), and get paid to find out.

---

## 3. Complexity checklist

Score each. More boxes ticked → higher t-shirt size **and** higher risk multiplier.

| # | Factor | Simple | Complex |
|---|---|---|---|
| 1 | User roles | 1 | 3+ with different permissions |
| 2 | Core screens | < 10 | 25+ |
| 3 | Workflow | Linear | Branching, approvals, state machine |
| 4 | Integrations | 0 | 2+, or one undocumented |
| 5 | Data migration | None | Large, dirty, or unknown format |
| 6 | Reporting | Fixed list | Ad-hoc, filterable, exportable |
| 7 | Payments | None | Gateway + refunds + reconciliation |
| 8 | Offline / sync | No | Yes ← *doubles most mobile estimates* |
| 9 | Real-time | No | Live dashboards, sockets, IoT streams |
| 10 | Multi-tenant | No | Yes ← *`[[Service Catalog]]` §4; isolation is most of the cost* |
| 11 | Languages | 1 | AR + EN with **RTL layout** |
| 12 | Notifications | None | Push + email + SMS + WhatsApp |
| 13 | Regulatory | None | Health, financial, government |
| 14 | New tech for the team | No | Yes |
| 15 | Client decision-making | One person | Committee |
| 16 | Design | Reuse patterns | Bespoke, animation-heavy |
| 17 | Legacy system | Greenfield | Must coexist with or replace a running system |

**Bilingual AR+EN with RTL (row 11) is systematically underestimated.** It is not translation — it is mirrored layouts, RTL-aware components, bidirectional text handling, and double the QA. Code Square ships AR+EN on its own site, so this is core competence — but it must be *priced*, not absorbed.

---

## 4. T-shirt size → day range

`proposed` planning defaults. **Team days, not calendar days.**

| Size | Team days | Typical shape | Complexity boxes |
|---|---|---|---|
| **XS** | 3–8 | Landing page · design prototype sprint · single automation · integration feasibility week | 0–2 |
| **S** | 10–25 | Marketing site · small internal tool · one-role CRUD app · UI/UX for ~15 screens | 2–4 |
| **M** | 30–70 | Web app, 2–3 roles, one integration, dashboard · mobile MVP | 5–8 |
| **L** | 80–150 | Multi-role operations system · mobile + web + admin · several integrations | 9–12 |
| **XL** | 180+ | Multi-tenant SaaS · IoT platform · full business operating system | 13+ |

**Rules:**
- **XL is never one estimate.** Split into phased L/M chunks with a re-quote gate between each (`[[Pricing and Packaging]]` §5.4).
- Days include design, engineering, QA, project management, deployment, and handover — **not** sales, not the Diagnostic, not post-launch support.
- Calendar time ≠ team days. Two people rarely halve a duration, client review gates add dead time, and `[[Pricing and Packaging]]` §2.1 assumes 60% utilisation. **Calendar ≈ team days ÷ realistic parallelism × 1.3.**

### Bottom-up check
Always cross-check the t-shirt size against a feature-level estimate: list features → days each → sum → add the fixed overheads below. **If the two methods disagree by more than 30%, something is misunderstood — go find it.**

| Always-forgotten overhead | Typical |
|---|---|
| Environment setup, CI/CD, deployment pipeline | 2–5 days |
| Auth, roles, permissions | 3–8 days |
| Admin panel | 5–15 days |
| QA and bug-fixing | **+20–30% of build days** |
| Project management and comms | **+10–15%** |
| Documentation and training | 2–4 days |
| Handover and account transfer | 1–2 days |

> Every one of these is real work that appears in every project and in almost no estimate. Add them as line items, not as a vague cushion.

---

## 5. Risk multipliers

Applied to the base estimate. **Multiplicative, not additive** — risks compound.

| Risk | Trigger | Multiplier `proposed` |
|---|---|---|
| **Unclear requirements** | No Blueprint, vague brief | **× 1.4 – 2.0** ← *biggest single factor* |
| **Third-party integration** | Documented API, sandbox seen | × 1.2 |
| | API exists, **not verified by Code Square** | **× 1.5 – 1.8** |
| | No API / undocumented / vendor unresponsive | **Do not fixed-price. T&M only** |
| **Client-side delay risk** | Committee, or a slow client history | × 1.3 |
| **New technology** | Team has not shipped it before | × 1.3 – 1.6 |
| **Regulatory** | Health, financial, government | × 1.3 – 1.5 |
| **Legacy coexistence** | Must integrate with a running old system | × 1.4 |
| **Data migration** | Volume/quality unknown | × 1.3, or carve out as a separate T&M line |
| **Fixed hard deadline** | Immovable date | × 1.2 (overtime, parallelism waste) |
| **Distributed/remote client** | Different city or country, no site access | × 1.15 |

**Worked example (illustrative — no Code Square figures):**
```
Base bottom-up estimate            60 days
× 1.5  requirements not blueprinted
× 1.5  one unverified integration
× 1.3  committee decision-making
= 175 days
```
60 → 175. **That is not padding — that is the actual expected cost of the unknowns.** The commercial answer is not to swallow it: it is to sell a Blueprint and an integration feasibility week, which collapse the first two multipliers toward 1.0 and let Code Square quote ~90 days honestly. **The Blueprint literally pays for itself in removed risk multiplier.**

---

## 6. Contingency policy

Distinct from risk multipliers. Multipliers cover *known* unknowns; contingency covers the unknown unknowns.

| Situation | Contingency on top |
|---|---|
| Post-Blueprint, familiar work, verified integrations | **+10%** |
| Standard project | **+15%** |
| New domain or new technology | **+25%** |
| No Blueprint (should be rare) | **+40%, or refuse fixed price** |

**Rules:**
1. **Contingency is internal.** It is inside the price, never a visible line item. A visible contingency line is a line the client negotiates away.
2. **Contingency is not profit.** Margin is set separately in `[[Pricing and Packaging]]` §2. Contingency that survives the project is a lucky margin, not a planned one.
3. **Never cut contingency to win a deal.** Reduce *scope* instead (`[[Pricing and Packaging]]` §10.2). Cutting contingency does not make the risk smaller — it just moves who pays for it.
4. **Track consumption.** Record contingency used per project. If it is always exhausted, the base estimates are wrong; if it is never touched, the multipliers are too high. Either way you only learn by measuring (§8).

---

## 7. The top 10 estimation traps

Ranked by how much money each one costs.

### 1. Estimating without discovery
**What happens:** a 45-minute conversation produces a fixed price. The real scope is 3× larger, and the price is already anchored in the client's mind.
**Mitigation:** never quote fixed off a call. Sell the Blueprint (`[[Offer Ladder]]` rung 2). If the client refuses to pay for discovery, either the first build phase is a paid discovery phase with a re-quote gate, or walk away (`[[Pricing and Packaging]]` §10.4).

### 2. Estimating the happy path only
**What happens:** you estimate "user books an appointment". You did not estimate: validation, errors, no availability, cancellation, rescheduling, double-booking, timezones, notifications, permissions, empty states, the admin's view of all of it. **The happy path is typically 30–40% of the real work.**
**Mitigation:** for every feature, ask *what happens when it fails, when it is empty, when two people do it at once, and who fixes it afterwards?* Estimate those explicitly.

### 3. Forgetting the invisible work
**What happens:** the estimate covers features and omits auth, admin panel, QA, deployment, documentation, training, meetings, and handover. Then 30% of the project is unpriced.
**Mitigation:** the fixed-overhead table in §4 goes into every estimate as line items. Code Square's own Facebook post already says it — *"اللي بيشوف النتيجة النهائية غالبًا مش شايف ٧٠٪ من الشغل الحقيقي."* Estimate the 70%.

### 4. Ignoring client-caused delay
**What happens:** content arrives six weeks late, reviews take three weeks each, and the client still expects the original date. The team is re-mobilised repeatedly — and context-switching back into a paused project costs real days.
**Mitigation:** 3-working-day feedback SLA in the SOW (`[[Proposal and SOW Template]]` §7 A1); client deadlines listed in the same timeline table as Code Square's (§6); **notify slippage in writing the day it happens, not at the end**; re-mobilisation fee after a defined cumulative delay (`[[Pricing and Packaging]]` §8.3).

### 5. Death by a thousand small changes
**What happens:** fifteen requests, each too small to argue about, each answered with *"سهلة، هعملهالك"*. Together they are three unbilled weeks and the margin is gone. **No single moment where anyone noticed.**
**Mitigation:** every change is written (`[[Pricing and Packaging]]` §8). Standard response: *"فكرة كويسة — دي خارج النطاق، هبعتلك طلب تغيير."* Cap absorbed goodwill at ~3% of project days and **log every absorbed item** — then show the client the list. Invisible generosity buys nothing.

### 6. Trusting an unverified integration
**What happens:** "they have an API" turns out to mean an undocumented endpoint, no sandbox, a vendor who does not reply, and a rate limit discovered in week 6. One integration consumes the whole project margin.
**Mitigation:** `[[Service Catalog]]` §7 mandatory feasibility gate — **never fixed-price an integration against a system whose API documentation you have not personally read**. Paid feasibility week first, prove one record moves end to end, then quote. Otherwise T&M.

### 7. Estimating with the optimistic developer
**What happens:** "two days" means two days of uninterrupted, error-free work by someone who already knows the answer. Real days contain meetings, reviews, environment breakage, and the bug that eats an afternoon.
**Mitigation:** estimate in **three points** — best / likely / worst — and use `(best + 4×likely + worst) ÷ 6`. Have a second person estimate blind and reconcile the gap; the conversation about *why* they differ is where the missed scope surfaces. Never let the person who will do the work estimate it alone under time pressure.

### 8. Anchoring on the client's budget
**What happens:** the client says "I have {{X}}", and the estimate mysteriously arrives at {{X}}. The scope did not shrink — only the price did.
**Mitigation:** **estimate the days before hearing the budget**, and write them down. If the honest estimate exceeds the budget, cut *scope* to fit, visibly, and say so: *"ده مش هيدخل في الميزانية دي — بس أقدر أبنيلك نسخة أولى أصغر تدخل، ونكمل بعد ما تشتغل."* Never silently compress the estimate.

### 9. Confusing estimate, quote, and deadline
**What happens:** an internal 60-day estimate becomes a 60-day promise with no contingency, no client-delay allowance, and no margin. The project is late on day one.
**Mitigation:** keep the three separate and written down separately. Estimate = engineering judgement (this file). Quote = commercial decision (`[[Pricing and Packaging]]`). Committed date = estimate + contingency + client-dependency buffer, converted to calendar time. Commit to the **calendar** date, never the raw estimate.

### 10. Not measuring what actually happened
**What happens:** the same mistakes repeat for years because nobody compares estimate to actual. Every project is a fresh guess.
**Mitigation:** §8. It costs one line per project.

**Honourable mentions:** free "quick fixes" for existing clients that quietly become unbilled support · assuming the client's data is clean (it never is) · estimating a redesign as if it were greenfield when a live system must keep running throughout · promising a hard date that depends on Apple's or Google's review queue (`[[Service Catalog]]` §2).

---

## 8. Calibration — the only way this file improves

Log one row per completed project. This table is worth more than every heuristic above once it has ~5 rows.

| Project | Size | Est. days | Actual days | Ratio | Multipliers applied | Contingency used | What was missed |
|---|---|---|---|---|---|---|---|
| {{...}} | {{M}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}}% | {{...}} |

**Review:**
- **Per project:** a 20-minute retrospective. What was missed? Which multiplier was wrong? *Write the answer in the last column.*
- **Quarterly:** if the median ratio is consistently above 1.2, raise the §4 day ranges — the estimates are wrong, not the team.
- **After ~5 projects:** replace the `proposed` ranges in §4 and the multipliers in §5 with Code Square's own measured numbers. Then they stop being industry heuristics and become a genuine competitive advantage.

**Target:** actual within **±20%** of estimate (`[[Offer Ladder]]` §4 conversion metrics).

---

## 9. The estimation workflow

```
Intake questions (§2)
        ↓
Blocking answers missing? → sell a Blueprint / feasibility week. STOP.
        ↓
Complexity checklist (§3)
        ↓
T-shirt size (§4)  ──cross-check──  bottom-up feature estimate + fixed overheads
        ↓                            disagree >30% → find out why
Apply risk multipliers (§5)
        ↓
Add contingency (§6)  → ESTIMATE IN DAYS
        ↓
[[Pricing and Packaging]] §2 floor  ·  §3 value ceiling  ·  §4 market check
        ↓
Commercial decision → PRICE (founder — blocker B4)
        ↓
Convert to calendar, add client-dependency buffer → COMMITTED DATE
        ↓
[[Proposal and SOW Template]] — every assumption written into §7
```

---

## 10. Estimation record — internal, never sent

Keep one per quote. When a dispute arrives eight months later, this is the only document that explains the number.

```markdown
# Estimation Record — {{Project}} · CS-{{YYYY}}-{{NNN}}
Date: {{...}} · Estimator: {{...}} · Reviewer: {{...}}

## Inputs
Source: {{Diagnostic / Blueprint / brief}} · Complexity boxes: {{n}}/17
Unanswered intake questions: {{list}}

## Estimate
| Component | Days |
|---|---|
| {{feature/phase}} | {{...}} |
| Auth & roles | {{...}} |
| Admin panel | {{...}} |
| QA (+25%) | {{...}} |
| PM (+12%) | {{...}} |
| Deployment, docs, handover | {{...}} |
| **Base** | {{...}} |

Multipliers: {{× ... = ...}}  ·  Contingency: {{+...% }}
**Total: {{n}} team days**  ·  Calendar: {{n}} weeks

## Assumptions  ← copy verbatim into SOW §7
1. {{...}}

## Risks
| Risk | Likelihood | Day impact | Mitigation |
|---|---|---|---|

## Confidence
☐ High (post-Blueprint, verified) ☐ Medium ☐ Low — **do not fixed-price**

## Post-project (fill in at close)
Actual: {{n}} days · Ratio: {{...}} · Missed: {{...}}
```

---

## Related

[[Foundation Brief]] · [[Service Catalog]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Proposal and SOW Template]] · [[Sales Playbook]] · [[Delivery Process]] · [[ICP - Ideal Customer Profiles]] · [[Open Questions and Decisions Needed]]
