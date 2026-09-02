---
date: 2026-09-02
type: identity
tags:
  - identity
  - voice
  - tone
  - style-guide
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Brand Voice and Tone — Code Square

## For future Claude

This note defines *how* Code Square sounds — the voice that stays constant everywhere, the tone that shifts by channel, and the mechanical style rules (Arabic dialect, emoji, numbers, English terms inside Arabic sentences). Read it alongside [[Messaging Framework]] whenever you write anything a human will read. Messaging says *what* to say; this note says *how it should sound*.

> **Jargon defined once.** *Voice* = the personality, constant across every channel. *Tone* = how that voice adjusts to the situation — the same person is warmer in a WhatsApp reply than in a proposal, but is still the same person.

---

## 1. Voice in one line

**An engineer explaining, not a salesperson selling.** Direct, specific, shows the reasoning, never inflates.

This is not invented — it is the voice the company already uses at its best. The website says *"نحلل قواعد عملك بدقة هندسية قبل كتابة أول سطر من الكود"*, and the best-performing published content is the M Tech Square case study, which opens by asking a question rather than making a claim.

---

## 2. Voice principles with do / don't pairs

### 2.1 Specific, never vague

Vague copy is the default failure mode of every agency in this market. Specificity is the cheapest available differentiation.

| ❌ Don't | ✅ Do |
|---|---|
| بنقدم حلول متكاملة بأحدث التقنيات لكل القطاعات. | عملنا نظام لوكالة manning: التوظيف، تتبع المشاريع، ولوحة تحليلات بتتحدث لحظة بلحظة. |
| We deliver integrated solutions using cutting-edge technologies. | We built a manning-agency platform: recruitment, project tracking, and a live analytics dashboard. |

### 2.2 Show the reasoning, not the adjectives

The buyer cannot verify "professional". They can verify a decision that made sense.

| ❌ Don't | ✅ Do |
|---|---|
| صممنا واجهة احترافية وسهلة الاستخدام. | العميل كان محتاج ٣ حاجات بس: يدور، يحجز، يتأكد. شيلنا ٨ شاشات من النسخة الأولى عشان كده. |
| We designed a professional, easy-to-use interface. | The user needed three things: search, book, confirm. So we cut eight screens out of v1. |

### 2.3 Say the hard thing

An Outsourced CTO who agrees with everything is not a CTO. Disagreement, said respectfully and with a reason, is the strongest trust signal available.

| ❌ Don't | ✅ Do |
|---|---|
| تمام، هنعملك التطبيق والموقع والـ AI كله مع بعض. | التطبيق دلوقتي مش هيفيدك. ابدأ بصفحة هبوط ونظام حجز بسيط، ولما يبقى فيه استخدام متكرر نبني التطبيق. |
| Sure, we'll build the app, the site and the AI together. | An app won't help you yet. Start with a landing page and a simple booking flow; build the app when there's repeat usage. |

### 2.4 Never inflate

Every unfalsifiable claim discounts the true claims sitting next to it.

| ❌ Don't | ✅ Do |
|---|---|
| إحنا أقوى فريق تقني في مصر وثقة عملائنا تتكلم عننا. | إحنا فريق صغير في بورسعيد. دي المشاريع اللي سلمناها، وده اللي اتغير للعميل. |
| We're the strongest technical team in Egypt. | We're a small team in Port Said. Here's what we shipped and what changed for the client. |

### 2.5 Teach only what leads somewhere

Educational content is fine — the company already does it well — but only when it ends in a decision the reader can act on. "What is UX" teaches a beginner who will never buy. "Which three screens does your booking flow actually need" teaches a buyer.

| ❌ Don't | ✅ Do |
|---|---|
| إيه الفرق بين الـ UI والـ UX؟ | ليه بتخسر حجوزات في آخر خطوة؟ ٣ حاجات بنشوفها في كل نظام حجز، وإزاي تتصلح. |
| What's the difference between UI and UX? | Why you lose bookings on the last step — three things we see in every booking system, and how to fix them. |

### 2.6 End with a next step, always

Every post, message, and page ends with a question or one named action. Never a dead end, never a wall of hashtags.

| ❌ Don't | ✅ Do |
|---|---|
| … للتواصل، رسالة على الصفحة. #برمجة #تصميم #تطوير_مواقع | شغلك بيمشي على إكسل دلوقتي؟ ابعتلي إزاي، وأقولك أول حاجة تتظبط. |
| … DM us for more info. | Running on spreadsheets today? Tell me how, and I'll tell you the first thing I'd fix. |

### 2.7 Bilingual by intent, not by translation

Write each language natively. A machine translation of Egyptian dialect into English reads as broken; a literal English translation into Arabic reads as foreign. Same idea, two native expressions.

| ❌ Don't | ✅ Do |
|---|---|
| "نحن نبني بيزنسك رقمياً" translated word-for-word into "We build your business digitally-ly" | AR: بنبني بيزنسك رقميًا · EN: We build the system your business runs on. |

---

## 3. Tone by channel

| Channel | Language | Tone | Length | CTA | Notes |
|---|---|---|---|---|---|
| **Facebook (feed post)** | Egyptian dialect | Conversational, peer-to-peer, opinionated. Talk like a person, not a page. | 40–120 words in the caption; **max 15 words on the image** | One question or one named action | Currently the weakest surface — it explains beginner concepts and never links to the website. Fix both. |
| **Facebook (case study carousel)** | Egyptian dialect | Narrative — problem → what we found → what we decided → result | 1 idea per slide | "شوف المشروع كامل" + link | The existing M Tech Square carousel is the model to copy structurally. |
| **LinkedIn** | English primary, Arabic (MSA) secondary | Professional, analytical, first-person. Decision-focused. | 150–300 words | A question to peers, or a link | Currently unused. This is where the Gulf and enterprise buyer lives. |
| **Website** | Full AR + EN parity | Premium, precise, engineering-confident. MSA, not dialect — except the one existing dialect line, which stays. | Tight. Every sentence earns its place. | ابدأ رحلة الابتكار → the diagnostic session | Already the strongest voice the company owns. Do not water it down. |
| **Proposal / SOW** | Client's language; MSA if Arabic | Formal, structured, explicit about scope, assumptions, and what is **out** of scope | As long as clarity needs | Named next step with a date | Never use dialect. Never use marketing adjectives. Numbers and dates only. |
| **WhatsApp reply** | Egyptian dialect | Fast, warm, human, direct. Answer first, pitch never. | 1–4 short lines | One question | Reply within business hours with a real answer, not "أهلاً، ابعتلنا تفاصيل أكتر". |
| **Email (cold or follow-up)** | Match the recipient; MSA or English for Gulf | Brief, respectful, specific to *their* business. No template energy. | Under 120 words | One low-friction ask | Never open with "نحن شركة رائدة في مجال…". Open with something true about them. |
| **Client update (during a project)** | Client's language | Plain, honest, no hedging. Bad news early and in full. | Short | What happens next, and when | This is where the "partner not vendor" claim is actually tested. |

---

## 4. Arabic dialect policy

| Context | Register | Reason |
|---|---|---|
| Facebook, Instagram, WhatsApp, TikTok, informal video | **Egyptian dialect (عامية مصرية)** | The local buyer talks this way; MSA on social reads stiff and corporate. |
| Website body copy, vision/mission, methodology, services | **Modern Standard Arabic (فصحى)** | Already the site's register. Reads as engineering-grade and travels to the Gulf. |
| Proposals, contracts, invoices, tenders, government | **MSA only** | Formality is a compliance signal in these contexts. |
| Gulf audiences (Jeddah, Riyadh) | **MSA or English** | Egyptian dialect can read as informal or unclear outside Egypt. |
| Mixing dialect and MSA in one paragraph | **Not allowed** | Reads as careless. Pick a register per piece. |
| Exception | The existing site line **إحنا مش بس بنبني برامج… إحنا بنبني مشروعك رقميًا** stays as-is | It is a deliberate, effective register break and it is already published. |

---

## 5. Emoji policy

| Where | Rule |
|---|---|
| **Website** | None. Zero. |
| **Proposals, contracts, invoices** | None. |
| **LinkedIn** | Maximum one, only if it genuinely aids scanning. Never in the first line. |
| **Facebook / Instagram captions** | Maximum 2–3, functional only — marking a list item or a step. Never as decoration, never as emotional filler. |
| **WhatsApp replies** | Natural human use is fine (👍 ✅). Do not perform enthusiasm. |
| **Inside images / creatives** | None, unless it is an intentional design element. |
| **Emoji bullet walls** (🚀✨💡🔥 stacked in a row) | Banned outright. It is the visual signature of low-credibility marketing and directly contradicts the engineer voice. |
| **Mascot exception** | **تاتا 🤖** belongs to Techno Square, not Code Square. Do not borrow it. |

---

## 6. Style guide

### 6.1 Numbers

- **Arabic copy:** use Western Arabic numerals (`1, 2, 3`) — they are standard in Egyptian digital writing and match the numerals used on the website and Facebook. Do not mix `١٢٣` and `123` in one document.
- Spell out zero through nine in flowing English prose (`three phases`); use digits for anything measured (`4 projects`, `74 followers`, `24 hours`).
- **Every number in public copy must be sourced.** If it cannot be traced to a document, a dashboard, or a client, it does not ship. Write `TBD`.
- Currency: `EGP` / `جنيه` and `SAR` / `ريال` written explicitly. Never a bare `$` — the `$19/$49/$99` mockup already caused one price confusion.
- Percentages: only with a stated basis. `80% of users only needed three actions` is fine because the post states the case. `99.9% uptime` is banned because nothing measures it.
- Dates: `2026-09-02` in vault notes; `2 سبتمبر 2026` / `2 September 2026` in published copy.
- Phone number: always `+20 10 43547526` in international form in written material.

### 6.2 English technical terms inside Arabic sentences

Egyptian technical readers use English terms naturally. Forcing Arabic calques reads as translated and unclear.

| Rule | Example |
|---|---|
| Keep the English term when it is what practitioners actually say | نظام **SaaS** · تكامل **API** · **UI/UX** · **MVP** · **Outsourced CTO** · وكالة **manning** |
| Write it in Latin script, not transliterated | ✅ `API` — ❌ `إيه بي آي` |
| Attach the Arabic definite article naturally with a hyphen where common | الـ**UX** · الـ**API** |
| Give the Arabic gloss the first time for a non-obvious term | نظام **SaaS** (نظام بالاشتراك الشهري) |
| Do not use an English term where a clear Arabic word exists | ✅ `الصيانة` — ❌ `الـmaintenance` |
| Never mix scripts inside a single word | ❌ `الscaling` |
| Product and company names stay in their original form | `Techno Square` · `El Shoush` · `Osama Sakr` |

### 6.3 Brand name capitalisation

| Form | When |
|---|---|
| **Code Square** | Default everywhere. Two words, both capitalised, always. |
| **CODE SQUARE** | Logo lockup only. Never in body copy or headlines. |
| **CS** | Internal shorthand and vault notes only. Not for buyer-facing copy on first mention. |
| **كود سكوير** | Arabic copy. Do not translate the meaning ("المربع البرمجي" — never). |
| ❌ CodeSquare · codesquare · Code square | Wrong. Fix on sight. |
| **M Tech Square** | Parent group. Never "MTech Square" or "M-Tech Square". |

### 6.4 Tagline handling

`YOU IMAGINE ... WE CREATE` is in the existing logo lockup. Per [[Foundation Brief]] §5 it is generic and buyer-free.

**Rule (proposed):** it stays as a **legacy lockup line inside the logo only**. It never leads a post, a page, a headline, or an email. All copy leads with the one-liner from [[Messaging Framework]]. Do not spend money changing the logo.

### 6.5 Punctuation and formatting

- Arabic uses Arabic punctuation: `،` `؛` `؟` — not `,` `;` `?`.
- No ALL CAPS for emphasis in either language.
- No exclamation marks in body copy. One is the absolute maximum in a WhatsApp reply.
- Hashtags: maximum 3, all relevant, at the end. Never a hashtag block.
- Ellipsis: `…` as one character, used sparingly.

---

## 7. Voice self-check before publishing

1. Would an engineer say this out loud to a client's face?
2. Is there a specific noun or number in the first sentence?
3. Any banned phrase? ([[Messaging Framework]] §4)
4. Right register for the channel — dialect vs MSA?
5. Emoji count within policy?
6. One idea, and one named next step?
7. If Arabic and English both appear, was each written natively?

---

## Related
[[Foundation Brief]] · [[Messaging Framework]] · [[Brand Positioning]] · [[Visual Identity]] · [[Company Profile]] · [[Core Values and Operating Principles]] · [[Content Calendar]] · [[Sales Scripts]] · [[Open Questions and Decisions Needed]]
