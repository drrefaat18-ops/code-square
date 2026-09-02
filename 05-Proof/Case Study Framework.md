---
date: 2026-09-02
type: framework
tags:
  - proof
  - case-studies
  - framework
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Case Study Framework

## For future Claude

This is the **reusable structure every Code Square case study must follow** — the four existing ones and every future one. It exists because the diagnosis in `[[Foundation Brief]]` §2 (Layer 5) is that all four projects are described by what they are, never by what changed. The framework's whole job is to force a number and a quote into every story.

Use this note as the template when writing a new case study. Do not invent a new structure per project — a consistent shape is what makes four case studies read as a body of evidence rather than four unrelated posts.

---

## 1. The eight-section structure (mandatory order)

Every case study uses these eight sections, in this order, with these headings.

| # | Section | What goes in it | Length |
|---|---|---|---|
| 1 | **Client and context** | Who they are, what business they are in, what size and shape (only what is known). If anonymised: the category and the city, never a disguised-but-identifiable description. | 2–4 sentences |
| 2 | **The problem — in the client's own words** | The client's own sentence, quoted. Not our paraphrase of their problem. If you do not have their words, this section is `❓ NEEDS FROM FOUNDER` — do not write it for them. | 1 quote + 2 sentences |
| 3 | **Why it mattered commercially** | What the problem was costing: time, money, lost bookings, errors, staff hours, missed deadlines. This is the section that makes a reader recognise their own business. | 3–5 sentences |
| 4 | **Our approach — mapped to the methodology** | The four canonical phases from the website: **التأسيس (Discovery) → المعمارية (Architecture) → الهندسة (Engineering) → الإطلاق والتطوير (Launch & Iterate)**. One short paragraph per phase saying what actually happened in that phase on this project. | 4 short paragraphs |
| 5 | **What we built** | Specific features, modules, integrations, architecture decisions. Named, concrete, checkable. "Booking module with Maps API integration" — not "a powerful platform". | Bulleted list |
| 6 | **The result — with a number** | At least one real metric. See §3 metric menu. If no metric exists yet, the section carries the literal label `⏳ Metrics pending — [what we asked for, who we asked, when]`. | 1 headline number + 2–3 sentences |
| 7 | **Client quote** | One approved sentence from the client, in their language, attributed to a named person and role — or, if they declined attribution, to a role and company type. Unapproved quotes never publish. | 1–2 sentences |
| 8 | **What we would do differently** | One honest thing. This is the credibility section: it is the part a template-shop competitor will never write, and technical buyers read it first. | 2–4 sentences |

**Methodology note:** the vault uses the website's **4-phase** model, not the 5-stage model published on Facebook. `[[Foundation Brief]]` §0 rule 6 requires one canonical framework. Until the founder formally rules, **case studies use the 4-phase model** because it is the one on the site the buyer will read. `❓ NEEDS FROM FOUNDER:` Confirm the 4-phase model is canonical and retire the Facebook 5-stage graphic.

---

## 2. The publish gate (hard rule)

> **No case study publishes without EITHER at least one real, sourced number, OR a visible `⏳ Metrics pending` label.**

There is no third option. Publishing a case study that implies results it does not have is the specific risk this whole folder exists to prevent — commercially and legally.

Three more gates, all mandatory:

1. **Permission gate.** External clients require written permission on file before the name, logo, screenshots, or any metric is published. Internal projects (M Tech Square, Techno Square) do not. See `[[Client Permission and Evidence Pack]]`.
2. **Quote-approval gate.** A client quote publishes only in the exact wording the client approved in writing. Never tidy, translate, or "improve" an approved quote without a fresh approval.
3. **Traceability gate.** Every factual sentence must be traceable to an evidence note, a client-supplied document, or a screenshot in the evidence pack. If it is not, it is marked `❓ NEEDS FROM FOUNDER:` with the exact question to ask — never softened into a vague claim.

**Banned in every case study** (from `[[Foundation Brief]]` §5): أقوى فريق · أفضل شركة · حلول متكاملة · أحدث التقنيات · "Awwwards-tier" · "99.9% uptime" · "SLA Guarantees" · "worldwide" / "globally".

---

## 3. The metric menu — what number to ask for, by project type

Ask for **one** number. A client who is asked for one number often answers; a client asked for eight answers none. Pick the row that matches, ask that question, and take the estimate if that is all you get — an estimate honestly labelled as one is still a number.

| Project type | Best single metric | The question to actually ask the client |
|---|---|---|
| **Booking / reservation system** (El Shoush) | Bookings processed per month; time to confirm one booking, before vs after | "قبل النظام، الحجز الواحد كان بياخد كام دقيقة من أول ما العميل يكلم لحد التأكيد؟ ودلوقتي؟" |
| **Recruitment / placement platform** (Osama Sakr) | Placements or candidates handled per month; hours per week saved on paperwork | "في الشهر بتتعاملوا مع كام مرشح؟ والورق ده كان بياخد كام ساعة في الأسبوع قبل النظام؟" |
| **Education platform** (Techno Square) | Students enrolled; courses live; enrolments processed through the platform vs manually | "كام طالب اتسجل من خلال المنصة؟ وكام كورس شغال عليها دلوقتي؟" |
| **Corporate / brand website** (M Tech Square) | Time-to-explain-the-company (sales cycle), enquiries received, materials replaced | "قبل الموقع، كنت بتشرح المجموعة إزاي؟ وكام مرة في الشهر كنت بتبعت presentation؟" |
| **Internal operations system** | Hours saved per week; errors eliminated per month; number of spreadsheets retired | "الشغل ده كان ماشي على كام ملف Excel؟ وكام غلطة في الشهر كانت بتحصل؟" |
| **Any project, fallback** | Time-to-quote, or headcount freed | "إيه الحاجة اللي بقيت بتعملها في وقت أقل بعد النظام؟ قد إيه أقل؟" |

**Rules for numbers:**
- Write the source next to the number in the draft: `(source: client WhatsApp, 2026-xx-xx)` or `(source: Techno Square dashboard export)`. Strip the source before publishing, keep it in the vault note.
- An estimate is labelled as one: "the client estimates roughly 10 hours a week" — never "saved 10 hours a week".
- **Never** convert a range into a precise-sounding figure, and never compute a percentage from numbers the client did not give you.
- Round down, not up. A conservative number that is defensible beats an impressive one that is challenged.

---

## 4. The client interview — question set

30–40 minutes, voice or WhatsApp voice notes, recorded with permission. Ask in Egyptian Arabic. The goal is not information — the founder already knows what was built. The goal is **their words and their number.**

**Warm-up / context**
1. ممكن تحكيلي شغلك بيمشي إزاي قبل ما نشتغل مع بعض؟
2. مين اللي كان بيستخدم النظام القديم أو الطريقة القديمة؟

**The problem (this produces section 2 — listen for a quotable sentence)**
3. لو حد سألك "إيه المشكلة اللي كانت مضايقاك؟" هتقوله إيه بالظبط؟
4. إيه أكتر يوم فاكره كانت المشكلة دي مأثرة فيه؟
5. جربت تحلها إزاي قبل كده؟ وليه ما نفعتش؟

**The commercial cost (section 3)**
6. المشكلة دي كانت بتكلفك إيه — وقت؟ فلوس؟ عملاء؟
7. لو فضلت سنة كمان من غير حل، كان هيحصل إيه؟

**The decision (useful for `[[Sales Playbook]]`)**
8. ليه اخترت Code Square؟ وكنت خايف من إيه قبل ما تبدأ؟

**The result (section 6 — the number)**
9. [ask the single metric question from §3]
10. إيه أول حاجة لاحظتها اتغيرت بعد ما النظام اشتغل؟
11. في حاجة النظام خلاك تعملها ما كنتش تقدر تعملها خالص قبل كده؟

**The quote (section 7)**
12. لو صاحبك عنده نفس المشكلة وسألك عننا، هتقوله إيه؟
    *(This question produces the testimonial. Write down the answer verbatim, then send it back in writing for approval.)*

**Honesty (section 8)**
13. لو رجعنا نبدأ المشروع من الأول، إيه اللي كنت تحب يتعمل بشكل مختلف؟

---

## 5. Evidence checklist per case study

Nothing publishes until this list is filled or explicitly marked N/A.

- [ ] Written permission on file (external clients only) — `[[Client Permission and Evidence Pack]]`
- [ ] Client name + logo file, with permitted uses recorded
- [ ] Named contact, role, and their approval of the quote in writing
- [ ] 3–6 screenshots of the live system, with any client data blurred or replaced with dummy data
- [ ] "Before" artefact where one exists: the old spreadsheet, the paper form, the WhatsApp thread, the old site
- [ ] At least one number, with its source recorded
- [ ] Project dates: start, launch — `❓` for all four current projects
- [ ] Tech stack actually used
- [ ] Scope note: what Code Square built vs what the client or a third party provided
- [ ] Anonymised fallback version drafted, in case permission is withdrawn later

---

## 6. Output formats — every case study ships in four

Write the long version once, then cut it three ways. Each of the four case-study notes carries all four.

1. **Full case study** — the eight sections above. Lives in the vault, becomes a website page and a PDF one-pager for proposals.
2. **Proposal paragraph** — one paragraph, ~80 words, ending in the number. Pasted into proposals and emails.
3. **Website three-liner** — problem / what we built / result. Three lines, for the projects grid.
4. **Social carousel outline (Arabic)** — 6–8 slides, Egyptian dialect, **one idea per slide, max 15 words on the image** (`[[Foundation Brief]]` §8). Detail goes in the caption. Feeds `[[Content System]]`.

---

## 7. Reusable content library rule

Store extracted assets **by theme, not by project** — a proof about "cutting manual paperwork" is reusable across maritime, travel, and education pitches. Keep a running list of: quotable client sentences, numbers with sources, architecture decisions worth explaining, and honest "what we would do differently" lessons. This is what makes case study #5 take a day instead of a week.

## Related
[[Foundation Brief]] · [[Portfolio and Case Studies]] · [[Client Permission and Evidence Pack]] · [[Testimonial and Reference Playbook]] · [[Content System]] · [[Sales Playbook]] · [[Service Catalog]] · [[Open Questions and Decisions Needed]]
