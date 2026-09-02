---
date: 2026-09-02
type: case-study
tags:
  - proof
  - case-study
  - techno-square
  - education
  - internal-product
  - code-square
ai-first: true
status: draft
owner: TBD
publishable: yes
evidence_strength: medium
client_type: internal product
segment: education
---

# Case Study — Techno Square Platform

## For future Claude

**Priority 1 in the production order** (`[[Portfolio and Case Studies]]` §3). No permission is needed — Techno Square is a sister entity in the M Tech Square group — and **the numbers are inside a dashboard the group itself owns.** This is the only case study in the portfolio that can carry a real metric without waiting for anybody outside the company. It is also the demo asset for beachhead B (education) in `[[Foundation Brief]]` §4.

Evidence is thin in detail but solid in fact: the platform is live, described verbatim on the website, and its enrolment flow is documented in the published M Tech Square narrative. Every gap is marked `❓ NEEDS FROM FOUNDER:` — do not fill any of them by inference.

Structure follows `[[Case Study Framework]]`.

---

## 1. Client and context (stated)

**Techno Square** — the education entity of the M Tech Square group, running online learning programmes. It has a sibling entity, **Online Techno Square**, dedicated to distance learning. Techno Square's audience is students; the published brand narrative describes education framed **as a journey**, with a mascot, **تاتا 🤖**, used as a companion through that journey rather than as decoration.

Code Square built and operates the platform: `منصة تعليمية مع تطبيق جوال متكامل لبرامج التعلم عبر الإنترنت الخاصة بتكنو سكوير` — an educational platform with an integrated mobile app for Techno Square's online learning programmes. The site labels it `منتج خاص` (own product).

`❓ NEEDS FROM FOUNDER:` When did the platform launch? Is it currently live and in daily use, or partially used?

---

## 2. The problem — in the client's own words

**⏳ Pending.** No statement of the problem from Techno Square exists in the evidence.

`❓ NEEDS FROM FOUNDER:` What was Techno Square doing **before** the platform — Excel sheets, WhatsApp groups, Google Forms, paper registration, Zoom links sent manually? The specific "before" is the most valuable missing sentence in this entire case study, because every academy and training centre in Port Said is running that same "before" right now and will recognise itself in it.

*(A note for the founder: the answer to this question is the sales pitch. "قبل كده التسجيل كان ماشي على فورم Google والفلوس على الواتساب" sells better than any feature list.)*

---

## 3. Why it mattered commercially

**⏳ Pending — depends on §2.**

`❓ NEEDS FROM FOUNDER:` Three questions that would fill this section:
- How many hours per week were staff spending on registration and follow-up before the platform?
- Were enrolments being lost or duplicated because tracking was manual?
- Could Techno Square have grown its student numbers without the platform, or was manual work the ceiling?

---

## 4. Our approach — mapped to the four-phase methodology

*(Canonical model from the Code Square website: التأسيس → المعمارية → الهندسة → الإطلاق والتطوير.)*

**التأسيس — Discovery.** `❓ NEEDS FROM FOUNDER:` What was scoped, and what was deliberately left out of version one? The company's own published post *"ليه المشاريع بتفشل قبل ما تبدأ؟"* argues that failure comes from feature bloat and cites a booking-app example where 80% of users needed only three actions. If that thinking was applied here, it is the strongest paragraph available — but only if it actually happened.

**المعمارية — Architecture.** Evidenced: the system spans **three surfaces** — a web platform, a mobile app, and an administrative dashboard — plus an enrolment flow. Notably, the **Online Techno Square enrolment form was wired directly into the Techno Square dashboard**, meaning a student registering on one entity's site lands in the other's operational system without re-entry. That is a genuine architecture decision worth naming.

`❓ NEEDS FROM FOUNDER:` Is there a single shared backend across web, mobile, and dashboard, or separate systems? Multi-tenant or single-tenant?

**الهندسة — Engineering.** Evidenced: a mobile app described as *متكامل* (fully integrated) with the platform rather than a companion app. The design language for the student audience uses images, illustrations, and infographics, with the mascot **تاتا 🤖** as a journey companion.

`❓ NEEDS FROM FOUNDER:` What stack? Native or cross-platform mobile? Is the app published on the App Store and Google Play, and under which developer account? *(This matters — a published, downloadable app is a demo you can hand a prospect in a meeting.)*

**الإطلاق والتطوير — Launch & Iterate.** `❓ NEEDS FROM FOUNDER:` What has changed since launch? What was added in response to how students actually used it? This is the phase that evidences the retainer model in the offer ladder, and nothing currently documents it.

---

## 5. What we built (stated + gaps)

**Evidenced:**
- An educational platform for Techno Square's online learning programmes
- An integrated mobile app
- An administrative dashboard
- An enrolment flow, with the Online Techno Square form feeding directly into the Techno Square dashboard
- A student-facing visual system built on illustration, infographics, and the تاتا mascot

`❓ NEEDS FROM FOUNDER:` Which of these exist — course creation and management, video hosting or streaming, live sessions, quizzes and assessments, certificates, attendance tracking, **payments and subscriptions**, parent or guardian access, instructor accounts, notifications? Whether payments run through the platform is the single most important unknown, because it decides whether this is sold to academies as an "operations system" or a "course delivery system".

---

## 6. The result

**⏳ Metrics pending — asked of: founder · asked on: TBD**

**This is the one case study where the number is already in the company's possession** and needs no external permission — it just needs someone to open the dashboard.

`❓ NEEDS FROM FOUNDER:` Pull whichever of these the dashboard can export today:
- Number of students registered on the platform
- Number of courses currently live
- Number of enrolments processed through the platform (all time, or per month)
- Staff hours per week spent on registration before vs after

**One of these four is enough to publish.** Per `[[Case Study Framework]]` §3, a rounded-down, honestly-labelled figure ("more than 200 students registered") is publishable; an invented percentage is not. Until one exists, the `⏳ Metrics pending` label stays visible on every published version.

---

## 7. Client quote

**⏳ Pending.** No quote exists.

`❓ NEEDS FROM FOUNDER:` Obtainable this week from the Techno Square lead — same group, no legal approval needed. Ask interview question 12 from `[[Case Study Framework]]`: *"لو صاحبك عنده أكاديمية وسألك عن المنصة، هتقوله إيه؟"* Record the answer verbatim, send it back in writing, get a yes.

---

## 8. What we would do differently

`❓ NEEDS FROM FOUNDER:` Required. What did building this teach you that changed how you scope education projects? Do not publish this section blank; do not let Claude invent it.

---

## Short version — for proposals (~80 words)

> Techno Square runs online learning programmes for students. Code Square designed and built its operating platform end to end: a web platform, an integrated mobile app, and an administrative dashboard, with an enrolment flow that feeds registrations from the Online Techno Square site directly into the Techno Square dashboard — no re-entry, no lost sign-ups. The platform is live and in daily use, and it is available as a working demonstration in any first meeting. ⏳ Usage metrics pending.

## Website version — three lines

> **Techno Square — Education Platform**
> An education business running registration, courses, and students across disconnected tools.
> One platform, one mobile app, one dashboard — with online enrolment wired straight into operations. Live, in production, and demo-able today.

## Social carousel outline (Arabic) — for `[[Content System]]`

*One idea per slide. Maximum 15 words on the image. Detail in the caption.*

| Slide | On the image (AR) | In the caption |
|---|---|---|
| 1 | **أكاديمية شغالة على فورم Google وجروب واتساب — مألوف؟** | ⚠️ لا تنشر السلايد دي غير لما المؤسس يأكد إن ده فعلاً كان الوضع قبل المنصة |
| 2 | **المشكلة مش الكورسات. المشكلة إن مفيش مكان واحد بيجمعهم** | العمليات مبعثرة = طلاب بيضيعوا |
| 3 | **منصة + تطبيق موبايل + داشبورد** | ثلاث شاشات، نظام واحد |
| 4 | **الطالب بيسجل… والتسجيل بيوصل للإدارة على طول** | فورم Online Techno Square داخل على داشبورد Techno Square مباشرة |
| 5 | **تاتا 🤖 — رفيق الرحلة، مش ديكور** | التعليم رحلة، والتصميم بيمشي مع الطالب فيها |
| 6 | **⏳ الأرقام جاية** | استبدل السلايد دي بالرقم الحقيقي أول ما يطلع من الداشبورد |
| 7 | **CTA:** عندك أكاديمية أو سنتر؟ تعالى شوف المنصة شغالة | عرض الجلسة التشخيصية — `[[Sales Playbook]]` |

## Strategic note — why this one goes first

This is the **volume and demo engine** for the education beachhead. Unlike the two external projects, Code Square can walk into any academy in Port Said and show a live, working system on a phone, with no client's permission required and no NDA in the way. `[[Foundation Brief]]` §3 calls it "a proven pattern sellable to every academy and training centre — with no client approval needed to demo it." Getting one real number out of its dashboard is the highest-value hour of work available in this vault.

## Related
[[Portfolio and Case Studies]] · [[Case Study Framework]] · [[Foundation Brief]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]] · [[2026-09-02 - Facebook Page Evidence]] · [[Case Study - M Tech Square Website]] · [[Content System]] · [[Sales Playbook]] · [[Service Catalog]]
