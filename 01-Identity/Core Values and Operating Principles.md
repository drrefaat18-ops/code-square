---
date: 2026-09-02
type: identity
tags:
  - identity
  - values
  - operating-principles
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Core Values and Operating Principles — Code Square

## For future Claude

These five values were not invented — each is **derived from something Code Square has already published about itself**, with the source quoted verbatim. Read this note when deciding whether to take a project, how to respond to a client request, or whether a piece of marketing is honest. Each value states what it looks like in practice and, more importantly, **what would violate it** — a value with no violation attached is decoration.

---

## How these were derived

The company already publishes three philosophy statements, a strategic core, a preamble, and a support promise. Read together, they describe a real operating stance. This note turns those published words into decision rules. Nothing generic ("integrity", "excellence", "innovation") appears below, because nothing generic appears in the source material.

| # | Value | Derived from (verbatim, stated) |
|---|---|---|
| 1 | نفهم الشغل قبل الكود / Understand the business before the code | *نبدأ بفهم عميق لطبيعة عمل العميل واحتياجاته* · *نحلل قواعد عملك بدقة هندسية قبل كتابة أول سطر من الكود* |
| 2 | مخصص، مش قالب / Custom, not template | *لا قوالب جاهزة هنا* · *"Custom-built. مش Copy & Paste."* |
| 3 | شريك، مش مورّد / Partner, not vendor | *لسنا مجرد مزودي خدمة؛ نحن شريكك التكنولوجي الاستراتيجي* · *Outsourced CTO* |
| 4 | أسس، مش صيحات / Fundamentals, not trends | *لا نطارد الصيحات العابرة؛ بل نبني أسساً تدوم طويلاً* · *لسنا مجرد مبرمجين؛ نحن مهندسو أنظمة* |
| 5 | بنفضل بعد التسليم / We stay after handover | *مش بنسلم ونمشي... إحنا مكملين معاك* · methodology phase 4: الإطلاق والتطوير |

---

## Value 1 — نفهم الشغل قبل الكود · Understand the business before the code

**The value.** We do not accept a feature list as a brief. We start by understanding how the business actually operates today — who does what, where the work gets stuck, what happens when someone is on leave — and only then decide what should be built.

**Source (stated, verbatim):** نحن لا نبني برمجيات فحسب... بل نبدأ بفهم عميق لطبيعة عمل العميل واحتياجاته · فهم عميق للأعمال — نحلل قواعد عملك بدقة هندسية قبل كتابة أول سطر من الكود.

**What it looks like in practice**
- The first meeting asks **"إيه اللي ناقص؟"** — the question that actually opened the M Tech Square engagement — not "what should it look like?"
- Every engagement starts with the **جلسة تشخيص** (Diagnostic Session) and produces a written one-page output the prospect keeps regardless of whether they buy. See [[Offer Ladder]].
- Discovery (التأسيس) is phase 1 of the methodology and is never skipped to hit a deadline.
- We ask for the spreadsheet, the paper form, the WhatsApp group. The current mess is the specification.
- We are willing to say "the thing you asked for is not the thing you need" — with the reasoning shown.

**What would violate it**
- Quoting a price before understanding the workflow.
- Building exactly what the client asked for while knowing it will not solve their problem.
- Skipping discovery because the client says "we're in a hurry".
- Treating discovery as an unpaid formality to get to the build.
- Marketing that leads with a capability list instead of a problem. ([[Foundation Brief]] §0 rule 4)

---

## Value 2 — مخصص، مش قالب · Custom, not template

**The value.** Every business has a workflow that does not fit a generic tool — that is usually the whole reason they called. We build around the actual workflow rather than forcing the business to bend to a template.

**Source (stated, verbatim):** لا قوالب جاهزة هنا. كل حل يُبنى خصيصاً... · كل مشروع هو حالة فريدة، وكل شركة تمتلك هوية مختلفة. لهذا السبب نبدأ بفهم عميق لاحتياجاتك بدلاً من القوالب الجاهزة. · Custom-built. مش Copy & Paste.

**What it looks like in practice**
- A maritime manning agency gets a crewing system, not a re-skinned CRM.
- Reusing our own *patterns* (auth, dashboards, enrolment flows) is fine and smart. Reusing a *previous client's product* with the logo swapped is not.
- We recommend an off-the-shelf tool and decline the project when off-the-shelf genuinely fits better. That refusal is the value working correctly.
- Design decisions are traceable to something specific about this client.

**What would violate it**
- Selling a "package" that is the same build for every buyer.
- Cloning a delivered client system for a competitor in the same segment.
- Choosing an architecture because it is what we already have lying around, then presenting it as tailored.
- A portfolio where four projects are visibly the same product in different colours.

---

## Value 3 — شريك، مش مورّد · Partner, not vendor

**The value.** We are accountable for whether the client's business improves, not only for whether the deliverable matched the spec. That includes disagreeing with them.

**Source (stated, verbatim):** لسنا مجرد مزودي خدمة؛ نحن شريكك التكنولوجي الاستراتيجي · عقلية الشراكة — تكامل عميق مع فريقك للعمل كذراع تقني استراتيجي (Outsourced CTO).

**What it looks like in practice**
- We argue features **out** of scope. The published booking-app example is the model: 80% of users only needed search, book, confirm — so the rest was cut.
- Bad news travels early and in full: a slipped date is reported when it is known, not on the deadline.
- We tell a client when a cheaper or smaller solution is the right one, even when a bigger one is available to sell.
- We are honest about what we do not know. Founder is a pharmacist, not a maritime engineer — domain gaps are named, not bluffed.
- Phased scope, so the client can stop after any phase and still own something that works.

**What would violate it**
- Saying yes to everything to protect the invoice.
- Padding scope with features the client will not use.
- Hiding a delay until it is undeniable.
- Selling an "Outsourced CTO" relationship while having no capacity to answer the phone after launch. (Capacity is currently **TBD** — this is a live risk, see [[Open Questions and Decisions Needed]].)
- Publishing a claim we cannot prove. Dishonesty toward the market is the same failure as dishonesty toward a client. ([[Messaging Framework]] §4)

---

## Value 4 — أسس، مش صيحات · Fundamentals, not trends

**The value.** We choose technology for how well it will hold in three years, not for how current it sounds this quarter.

**Source (stated, verbatim):** لا نطارد الصيحات العابرة؛ بل نبني أسساً تدوم طويلاً · لسنا مجرد مبرمجين؛ نحن مهندسو أنظمة برمجية قابلة للتوسع.

**What it looks like in practice**
- Architecture (المعمارية) is a named phase before engineering, not something discovered mid-build.
- We can explain, in the client's language, *why* a technology was chosen and what it costs them later.
- We add AI when there is a workflow that measurably improves — the site already lists real, specific AI work (LLM integration, RAG pipelines), which is the honest version of this. We do not bolt AI onto a proposal because it sells.
- We document decisions so the next engineer — ours or theirs — can understand them.
- We optimise for the client's actual conditions. Egyptian mobile networks are a design constraint, not an afterthought. The current 7.5 MB website payload is a live violation of this value by our own hand. See [[Website and Technical Audit]].

**What would violate it**
- The phrase **أحدث التقنيات** in our own marketing — it directly contradicts this value and is banned.
- Choosing a framework because it is trending.
- Shipping a build nobody but the original author can maintain.
- A company selling digital trust while serving its own site over an expired TLS certificate. That is the sharpest current violation and it is ours, not a client's. ([[Foundation Brief]] §9, Priority 0)

---

## Value 5 — بنفضل بعد التسليم · We stay after handover

**The value.** Launch is the middle of the engagement, not the end. A system that is not maintained decays into the same mess it replaced.

**Source (stated, verbatim):** مش بنسلم ونمشي... إحنا مكملين معاك · الإطلاق والتطوير — خطوط إمداد انسيابية للإطلاق متبوعة بحلقات تحسين وتطوير مستمرة.

**What it looks like in practice**
- Every engagement ends with a named post-launch arrangement — or an explicit written statement that there is none, and why.
- Portfolio status labels like `تحديثات جارية` are real: systems are still being worked on, and that is stated publicly.
- Handover includes documentation and access, so the client is never hostage to us.
- The 24-hour response promise on the website has **a named owner** and a tracked inbox. Today it does not — that is an open gap, not a value. See [[Lead Intake and CRM]].
- We answer the question a client asks six months later.

**What would violate it**
- Going quiet after the final invoice.
- A support promise with no owner, no tracking, and no response-time data — which is the current state, and must be fixed before the promise is repeated in marketing.
- Publishing "99.9% uptime" or "SLA Guarantees" with no monitoring and no SLA document behind them. Both are banned until real. ([[Messaging Framework]] §4)
- Withholding credentials or source code to keep a client dependent.

---

## Operating principles (proposed — how the values become daily rules)

| # | Principle | Applies to |
|---|---|---|
| 1 | **No claim without an artifact.** Every public statement names the project, screenshot, metric, or document behind it. | Marketing, sales, proposals |
| 2 | **Unknown is written `TBD`, never guessed.** Founding year, headcount, client count, revenue, pricing — all TBD today. | Everything |
| 3 | **No price before discovery.** | Sales |
| 4 | **Scope is phased.** The client can stop after any phase and still own something working. | Delivery |
| 5 | **Bad news early.** A slip is reported the day it is known. | Delivery |
| 6 | **One idea per creative, ≤ 15 words on the image.** | [[Visual Identity]] |
| 7 | **Both languages written natively.** Never machine-translated. | [[Brand Voice and Tone]] |
| 8 | **Published client work requires written permission.** No exceptions, including screenshots. | [[Portfolio and Case Studies]] |
| 9 | **Fix our own house first.** We do not sell digital credibility from a site with an expired certificate. | [[Website and Technical Audit]] |
| 10 | **We are allowed to say no.** Wrong-fit, price-only, and template-clone requests are declined. | Sales |

---

## How to use this note

- **Deciding whether to take a project:** run it against values 1, 2, and 3, plus principle 10.
- **Reviewing marketing copy:** values 3 and 4, plus principles 1 and 2.
- **Scoping a build:** values 2 and 4, plus principles 3, 4, and 5.
- **Closing out a project:** value 5, plus principles 5 and 8.

If a value conflicts with revenue on a specific deal, the decision belongs to the founder — but it must be a conscious decision, written down in [[Open Questions and Decisions Needed]], not a quiet drift.

---

## Related
[[Foundation Brief]] · [[Company Profile]] · [[Brand Positioning]] · [[Messaging Framework]] · [[Brand Voice and Tone]] · [[Visual Identity]] · [[Offer Ladder]] · [[Portfolio and Case Studies]] · [[Website and Technical Audit]] · [[Lead Intake and CRM]] · [[Open Questions and Decisions Needed]]
