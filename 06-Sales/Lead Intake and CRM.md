---
date: 2026-09-02
type: sales-operations
tags:
  - sales
  - crm
  - lead-intake
  - process
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Lead Intake and CRM — استقبال العملاء وإدارتهم

## For future Claude

This is the **operational plumbing** under `[[Sales Playbook]]`. Today (2026-09-02) there is **no record of any enquiry ever received**. Leads arrive on WhatsApp, Messenger, phone, and a website form that publicly promises a 24-hour response with nobody owning the inbox (`stated` — see `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]`). Nothing is logged. That is the most expensive gap in the company.

Everything here is `proposed` unless marked otherwise. Rules: no invented prices (`[[Pricing and Packaging]]`), no invented client names, no invented team members — **owner is `TBD`, and a `TBD` owner is itself a blocker, not a solved problem**. Arabic message text is real Egyptian dialect, ready to copy and send.

The honest answer to "which CRM?" at this company's size is **a spreadsheet**. That is written below without apology, along with the exact trigger for outgrowing it.

---

## Part 1 — What is broken today (`stated`)

| Channel | Who owns it | Where the lead is recorded | Response promise |
|---|---|---|---|
| Website contact form | **Nobody** | Nowhere | **24 hours — published on the site** |
| WhatsApp `+20 10 43547526` | Whoever picks up the phone | Nowhere | None |
| Facebook Messenger | Whoever opens the app | Nowhere | None |
| Phone `010 43547526` | Whoever picks up | Nowhere | None |
| Email `codesquareteam1@gmail.com` | Unclear | Nowhere | None |
| Referral / walk-in | The person who was there | Nowhere | None |

**Three consequences, in order of cost:**
1. **A published promise is being broken** every time a form goes unanswered. That is worse than making no promise.
2. **No lead history exists**, so no follow-up is possible, no re-engagement is possible, and every lost lead is lost permanently and invisibly.
3. **No source data exists**, so there is no way to know which marketing effort produced anything. Every pound of future ad spend is guesswork.

**Two decisions this week, before anything else in this file:**
- Name the **Response Owner** by name. One person. → `[[Open Questions and Decisions Needed]]`
- **Verify the website form actually delivers email**, and to which address. It has never been confirmed. A form that silently fails is the worst case of all.

---

## Part 2 — The unified intake form (spec)

One set of fields, captured for **every** lead on **every** channel. On the website it is a form; on WhatsApp and the phone it is a set of questions the Response Owner asks conversationally.

| # | Field | Required | Type | Notes |
|---|---|---|---|---|
| 1 | `lead_id` | ✅ | auto | `CS-YYYYMM-NNN` e.g. `CS-202609-014` |
| 2 | `date_received` | ✅ | date+time | Exact time — the SLA clock starts here |
| 3 | `name` | ✅ | text | الاسم |
| 4 | `company` | ⬜ | text | Blank often means individual/idea-stage |
| 5 | `phone_whatsapp` | ✅ | phone | The single most useful field in Egypt |
| 6 | `email` | ⬜ | email | Required on the website form only |
| 7 | `channel` | ✅ | select | Part 4 taxonomy |
| 8 | `source` | ✅ | select | Part 4 taxonomy |
| 9 | `utm` / referrer | ⬜ | text | Website only. Part 4 convention |
| 10 | `segment` | ✅ | select | بحري-لوجستي · تعليم · صحة · مكاتب مهنية · تجارة-تجزئة · أخرى |
| 11 | `city` | ✅ | select | بورسعيد · القاهرة · الجيزة · الإسكندرية · جدة · الرياض · أخرى |
| 12 | `project_type` | ✅ | select | موقع · تطبيق · MVP · نظام داخلي · تكامل · غير محدد |
| 13 | `problem_stated` | ✅ | long text | **Their words, verbatim.** Do not paraphrase. |
| 14 | `budget_band` | ⬜ | select | `TBD` — bands from `[[Pricing and Packaging]]`. Must match the website dropdown, which is currently **unknown**. |
| 15 | `timeline` | ⬜ | select | فوري · خلال شهر · خلال 3 شهور · مش محدد |
| 16 | `decision_maker` | ⬜ | yes/no/unknown | Is the person we're talking to the one who signs? |
| 17 | `score` | ✅ | number 0–100 | Part 5 |
| 18 | `stage` | ✅ | select | The 8 stages in `[[Sales Playbook]]` Part 2 |
| 19 | `owner` | ✅ | person | `TBD` until named. Never blank. |
| 20 | `next_action` | ✅ | text | **Never blank. Ever.** |
| 21 | `next_action_date` | ✅ | date | **Never blank. Ever.** |
| 22 | `touch_count` | ✅ | number | 0–7, per the cadence in Part 7 |
| 23 | `last_touch_date` | ✅ | date | |
| 24 | `notes` | ⬜ | long text | Append-only, each entry dated |
| 25 | `lost_reason` | conditional | select | Mandatory when stage = Closed Lost. Fixed list, `[[Sales Playbook]]` Part 7 |
| 26 | `reengage_date` | conditional | date | Mandatory on every Closed Lost |

**The three fields that make the whole system work:** `owner`, `next_action`, `next_action_date`. A row missing any of them is a leak. The weekly review's only real job is to find blank ones.

### Website form — recommended changes

The live form asks: اسم المشروع · بريدك الإلكتروني · ميزانية المشروع · نوع المشروع · تفاصيل الرسالة (`stated`).

| Change | Why |
|---|---|
| **Add a WhatsApp number field, required** | Egyptian SMBs answer WhatsApp; many will never open the email. This is the single highest-value change. |
| Add اسمك (person's name) separate from اسم المشروع | Right now we get a project name and no human name. |
| Add القطاع (sector) | Routes the lead and shapes the first reply. |
| Add المدينة | Port Said = an in-person visit is possible. That changes everything. |
| Confirm the budget dropdown bands | Currently unknown, and they frame every conversation that follows. |
| Capture UTM + referrer in hidden fields | Without this, marketing attribution is impossible. |
| **Verify delivery** | Unconfirmed. Send a test today. |
| Keep the 24-hour promise **only if** it has an owner | Otherwise remove the sentence from the site. A broken published promise costs more than no promise. |

---

## Part 3 — Channel-by-channel intake procedure

### 3.1 Website form

| | |
|---|---|
| **SLA** | **24 hours**, published. Target: **4 working hours**. |
| **Checked** | 09:30 and 16:30 daily |
| **Steps** | 1. Log the row immediately. 2. Reply **on WhatsApp if a number was given**, email otherwise. 3. Ask the two routing questions. 4. Aim only for a booked Diagnostic Session. |

**Reply — WhatsApp (Egyptian dialect):**
> **أهلاً أستاذ [الاسم] 👋**
> **أنا [الاسم] من Code Square. وصلني طلبك عن [نوع المشروع] النهاردة.**
> **قريت اللي كتبته وعندي سؤالين بس عشان أفهم الصورة صح:**
> **١. الحاجة دي هتحل إيه عندكم بالظبط؟ يعني إيه اللي مضايقكم دلوقتي؟**
> **٢. عايزينها تكون شغالة إمتى؟**
> **ولو تحب، بنعمل جلسة تشخيص مجانية ٣٠ دقيقة — بنفهم فيها شغلك، وبتخرج منها بورقة مكتوبة فيها المشكلة والخطوة الأولى، سواء اشتغلنا مع بعض أو لأ.**
> **يوم [يوم] الساعة [وقت] يناسبك؟**

*(Hello Mr [name] 👋 — I'm [name] from Code Square. Your request about [project type] reached me today. I read what you wrote and have just two questions to understand the picture properly: 1. What exactly will this solve for you? What's bothering you now? 2. When do you want it working? And if you'd like, we do a free 30-minute Diagnostic Session — we understand your business, and you come out with a written page containing the problem and the first step, whether we work together or not. Does [day] at [time] suit you?)*

**Reply — Email (MSA, for formal / Gulf):**
> **تحية طيبة أستاذ [الاسم]،**
> **شكراً لتواصلك مع Code Square. وصلنا طلبك بخصوص [نوع المشروع].**
> **قبل أن نرسل أي تصور أو تقدير، نفضّل أن نفهم طبيعة العمل أولاً — فأي رقم قبل ذلك يكون تخميناً.**
> **نقترح جلسة تشخيص لمدة 30 دقيقة، دون أي التزام، تخرج منها بصفحة مكتوبة تلخّص المشكلة كما نراها والخطوة العملية الأولى — وهي لك سواء تعاونّا أم لا.**
> **هل يناسبك يوم [التاريخ] الساعة [الوقت]؟**
> **[الاسم] — Code Square**
> **واتساب: +20 10 43547526**

### 3.2 WhatsApp

| | |
|---|---|
| **SLA** | **2 working hours.** Outside hours: an auto-reply, then a real reply next morning. |
| **Setup** | WhatsApp **Business** (free): auto-greeting, away message, quick replies, and **labels** that mirror the pipeline stages. |
| **Rule** | Never quote a price in WhatsApp. Never send a proposal in WhatsApp before the Diagnostic. |

**Auto-greeting (first-ever message):**
> **أهلاً بيك في Code Square 👋**
> **وصلتنا رسالتك وهنرد عليك في أقرب وقت خلال ساعات العمل.**
> **ولو تحب توفر وقت، ابعتلنا: اسم الشركة، ونوع الشغل اللي بتدور عليه، وإيه المشكلة اللي عايز تحلها.**

**Away message (outside hours):**
> **شكراً لرسالتك 🙏 إحنا دلوقتي خارج مواعيد العمل. هنرد عليك أول [الوقت] بإذن الله.**
> **ولو الموضوع مستعجل، ابعت "عاجل" وهنشوفه أول ما نفتح.**

**WhatsApp labels (mirror the pipeline):**
`0-وارد` · `1-تم التواصل` · `2-مؤهل` · `3-جلسة اتعملت` · `4-عرض خريطة` · `5-خريطة شغالة` · `6-عرض بناء` · `7-كسبناه` · `7-خسرناه` · `مؤجل`

Labels are the poor man's CRM and they are genuinely enough at this size — **provided the spreadsheet row also exists**. Labels live on one phone; the spreadsheet survives the phone.

### 3.3 Facebook Messenger

| | |
|---|---|
| **SLA** | **2 working hours.** Facebook publicly displays response rate — it is visible to prospects. |
| **Setup** | Instant reply on. Saved replies for the five most common questions. |
| **Rule** | **Move to WhatsApp as early as politely possible.** Messenger threads get buried; WhatsApp does not. |

**Instant reply:**
> **أهلاً 👋 وصلتنا رسالتك، هنرد عليك في أقرب وقت.**
> **ولو تحب نتكلم أسرع، ابعتلنا واتساب على 01043547526.**

**The channel switch:**
> **تحب نكمل على الواتس؟ أسهل في إننا نبعت ملفات ونحدد ميعاد. رقمي 01043547526، أو ابعتلي رقمك وأنا أكلمك.**

### 3.4 Phone

| | |
|---|---|
| **SLA** | Answer live in working hours. Missed call → **call back the same day**, and send a WhatsApp within 15 minutes. |
| **Rule** | Log the call **during or immediately after**, never later. A call not written down did not happen. |

**Missed-call WhatsApp (within 15 minutes):**
> **أهلاً، أنا [الاسم] من Code Square، شوفت مكالمتك وماقدرتش أرد. تحب أكلمك إمتى؟ أو ابعتلي هنا اللي محتاجه وأنا أرد عليك.**

**Live-call opening:**
> **Code Square، أهلاً بحضرتك، معاك [الاسم]. اتفضل.**

**Live-call routing (three questions, then book — do not discover on the phone):**
> **حضرتك شغال في إيه؟ … وإيه اللي محتاجه بالظبط؟ … وعايزه إمتى؟**
> **تمام. الكلام ده يستاهل نقعد فيه ٣٠ دقيقة عشان أفهم الصورة صح بدل ما أديك كلام سريع. نحجزها إمتى — [يوم] ولا [يوم]؟**

### 3.5 Referral

| | |
|---|---|
| **SLA** | **Same day.** A referral goes cold faster than any other lead type — the referrer's credibility is on the line. |
| **Rule** | Always thank the referrer, and always report back the outcome. That is what produces the second referral. |

**To the referred person:**
> **أهلاً أستاذ [الاسم]، أنا [الاسم] من Code Square.**
> **[اسم المُحيل] كلمني عنك وقالي إنكم بتدوروا على [الموضوع].**
> **حبيت أتواصل معاك بنفسي. تحب نتكلم ٢٠ دقيقة، أفهم الوضع عندكم وأقولك بصراحة لو إحنا مناسبين ولا لأ؟**

**Back to the referrer (same day):**
> **شكراً على ترشيحك يا [الاسم] 🙏 كلمت [الاسم] فعلاً وهنقعد يوم [التاريخ]. هرجعلك أقولك حصل إيه.**

### 3.6 Walk-in (شارع ممفيس, Port Said — `stated` address)

| | |
|---|---|
| **SLA** | Immediate. |
| **Rule** | Never let someone leave without a logged number and a booked next step. |

> **أهلاً بيك، اتفضل. أنا [الاسم].**
> **حكيلي شغلكم إيه وإيه اللي محتاجه… تمام.**
> **بص، الكلام ده يستاهل جلسة أطول شوية عشان أفهمه صح. ممكن رقم الواتس بتاعك، وأبعتلك ميعاد نقعد فيه ٣٠–٤٥ دقيقة؟**

Log the row before they are out of sight.

---

## Part 4 — Source taxonomy and UTM convention

### Channel (how they reached us — 7 values, fixed)
`website-form` · `whatsapp` · `messenger` · `phone` · `email` · `referral` · `walk-in`

### Source (why they reached us — 10 values, fixed)
`facebook-organic` · `facebook-ad` · `google-search` · `direct` · `referral-client` · `referral-partner` · `outbound-whatsapp` · `outbound-call` · `outbound-visit` · `linkedin`

Two separate fields. `channel` = the pipe. `source` = the cause. Collapsing them into one destroys attribution.

### UTM convention

```
utm_source   = facebook | google | linkedin | whatsapp | email | partner
utm_medium   = organic | cpc | social | referral | outbound
utm_campaign = <segment>-<offer>-<yyyymm>
utm_content  = <asset>
```

Rules: all lowercase, hyphens only (never spaces or underscores), campaign always ends in `yyyymm`.

Examples:
```
?utm_source=facebook&utm_medium=organic&utm_campaign=maritime-diagnostic-202609&utm_content=post-crewing-excel
?utm_source=facebook&utm_medium=cpc&utm_campaign=education-diagnostic-202609&utm_content=video-academy
?utm_source=whatsapp&utm_medium=outbound&utm_campaign=maritime-diagnostic-202609&utm_content=first-touch
```

**Prerequisite:** UTM tracking is worthless until the website is reachable and rendered. TLS certificate and prerendering are Priority 0 in `[[Foundation Brief]]` §9. Do not build reporting on a site nobody can load.

---

## Part 5 — Lead scoring

Score every lead at intake, revise after the Diagnostic. Weights are `proposed` — recalibrate after 20 closed deals with real data.

| Signal | Points | How to read it |
|---|---|---|
| **Segment = maritime/logistics** | 25 | The beachhead. We have proof and proximity. |
| Segment = education | 15 | Live demo asset exists. |
| Segment = healthcare | 15 | Founder domain fluency. |
| Other segment | 5 | |
| **City = Port Said** | 15 | An in-person visit is possible. Enormous advantage. |
| Cairo / Giza / Alexandria | 8 | |
| Jeddah / Riyadh | 8 | Higher ticket, longer cycle, more procurement friction. |
| **Says "Excel" or describes a manual repeated process** | 20 | The strongest single buying signal we have. |
| **Named a date with a real driver** (contract, season, audit) | 15 | Urgency is real. |
| Said "مش مستعجل" / no date | 0 | |
| **Decision-maker is the person talking** | 15 | |
| Decision-maker is reachable | 8 | |
| Unknown / unreachable | 0 | |
| Budget band stated at or above minimum | 10 | Minimum is `TBD` |
| Referral or existing-client expansion | 15 | Highest-converting source there is. |
| Existing business with employees | 10 | |
| Idea-stage, no business yet | 0 | Not disqualifying — MVP path. |
| **Asked for a price before describing a problem** | **−10** | Price shopper signal. |
| **Wants equity / revenue share** | **−25** | Disqualify — `[[Objection Handling]]` #5. |
| Third-hand contact, no reply to two touches | −10 | |

| Score | Priority | Action |
|---|---|---|
| **70+** | 🔥 A | Reply within 1 hour. Call, don't message. Founder involved. |
| **45–69** | B | Standard SLA. Full 7-touch cadence. |
| **20–44** | C | Standard SLA, but book only if they engage. |
| **< 20** | D | One polite reply. No cadence. Nurture list. |

**Never let the score replace judgement.** It sorts the queue; it does not make the decision.

---

## Part 6 — Response SLAs (one table, put it on the wall)

| Channel | Target | Hard limit | Owner |
|---|---|---|---|
| Website form | 4 working hours | **24 hours (published)** | Response Owner (`TBD`) |
| WhatsApp | 30 minutes | 2 working hours | Response Owner |
| Messenger | 1 hour | 2 working hours | Response Owner |
| Phone (missed) | 15 min WhatsApp | Same-day callback | Response Owner |
| Email | 4 working hours | 24 hours | Response Owner |
| Referral | 2 hours | Same day | Founder or Response Owner |
| Walk-in | Immediate | Immediate | Whoever is present |
| Score 70+ lead, any channel | **1 hour** | 2 hours | Founder |
| Post-Diagnostic one-pager | 24 hours | **48 hours (promised on the call)** | Diagnostic Owner |
| Blueprint proposal | 2 working days | 3 working days | Diagnostic Owner |

**Working hours:** `TBD` — must be decided and published. The Facebook page currently says "Always open" (`stated`), which is a promise nobody can keep. Either publish real hours or accept the auto-reply is doing the work.

---

## Part 7 — The 7-touch follow-up cadence

Runs on every lead scoring 45+ that has not replied. Stop the instant they reply. Every touch adds something; none of them is "أي أخبار؟".

| # | Day | Channel | Purpose |
|---|---|---|---|
| 1 | 0 | WhatsApp | Reply + two questions + offer the session |
| 2 | 2 | WhatsApp | A different angle — one question about their world |
| 3 | 5 | Phone call | Voice. Voicemail/WhatsApp if missed |
| 4 | 8 | WhatsApp | Give value — one genuinely useful observation |
| 5 | 12 | WhatsApp/Email | Proof — show something real we built |
| 6 | 17 | Phone or in-person (Port Said) | Last real attempt |
| 7 | 21 | WhatsApp | The honest close |

---

**Touch 1 — Day 0.** See Part 3, per channel.

**Touch 2 — Day 2**
> **أهلاً أستاذ [الاسم]، بعتلك من يومين وعارف إن الشغل بياخد.**
> **سؤال واحد بس، ولو الإجابة "لأ" مش هزعجك تاني:**
> **الحاجة اللي كتبتها في طلبك — هي دلوقتي في أولوياتكم للشهرين الجايين، ولا لسه فكرة بتتدرس؟**
> **بسأل عشان لو لسه بدري، أسيبك وأرجعلك في وقت مناسب أحسن ما أفضل أبعتلك.**

*(Hello Mr [name], I messaged you two days ago and I know work is busy. Just one question, and if the answer is "no" I won't bother you again: the thing you wrote in your request — is it a priority for you in the next two months, or still an idea being considered? I'm asking because if it's early, I'd rather leave you and come back at a good time than keep messaging you.)*

**Touch 3 — Day 5 · phone.** If they answer, run the routing questions from §3.4. If not:
> **أهلاً أستاذ [الاسم]، كلمتك دلوقتي وماردتش، مفيش مشكلة.**
> **أنا مش هضغط عليك. حابب بس أقولك إن جلسة التشخيص مجانية ومن غير أي التزام، وبتخرج منها بورقة مكتوبة تنفعك حتى لو مشيت مع حد تاني.**
> **قولي بس الوقت المناسب ليك وأنا أظبط نفسي عليه.**

**Touch 4 — Day 8 · value.** Say one specific, useful, non-selling thing about their business. Example for maritime:
> **أستاذ [الاسم]، مش بابعت عشان أبيع. بابعت حاجة ممكن تفيدك.**
> **من شغلنا مع وكالة توظيف بحري هنا في بورسعيد، أكتر حتة بتضيع وقت مش الأوراق نفسها — إنها بتتكتب أكتر من مرة في أكتر من مكان، وكل مرة فيها احتمال غلط.**
> **لو عندكم نفس الحاجة، أول خطوة مش برنامج — أول خطوة إنك تعرف الورقة بتتنقل كام مرة. جربها ولو طلع الرقم كبير، تعالى نتكلم.**

*(Mr [name], I'm not messaging to sell. I'm sending something that might be useful. From our work with a maritime manning agency here in Port Said, the biggest time sink isn't the paperwork itself — it's that it gets written more than once in more than one place, and each time there's a chance of error. If you have the same thing, the first step isn't software — the first step is knowing how many times a document gets re-entered. Try it, and if the number comes out big, come talk to me.)*

> ⚠️ Name El Shoush or Osama Sakr **only** with written permission on file. Until then describe without naming, exactly as above.

Education variant:
> **من شغلنا على منصة تعليمية شغالة فعلاً، أكتر حاجة بتضيع فلوس على الأكاديميات مش التسويق — الطلبة اللي بيسألوا وميكملوش تسجيل عشان محدش تابعهم. لو عندك نفس الحاجة، عد كام واحد سأل الشهر ده وكام سجل. الفرق بينهم ده فلوس على الأرض.**

**Touch 5 — Day 12 · proof**
> **أستاذ [الاسم]، حابب أوريك حاجة إحنا عاملينها بدل ما أفضل بتكلم.**
> **[لينك / سكرين شوت] — ده [وصف من غير أسماء عملاء إلا بإذن].**
> **لو شبه اللي في دماغك، رد بكلمة واحدة وأنا أكلمك. ولو مش شبهه خالص، قولي وأنا أبطل أبعت.**

**Touch 6 — Day 17 · last real attempt.** In Port Said, make this an in-person visit — see `[[Outbound Prospecting Playbook]]`.
> **أستاذ [الاسم]، إحنا في بورسعيد زيكم. لو تحب، أعدي عليك ١٥ دقيقة بس، من غير عرض ومن غير ضغط — أفهم شغلكم وأقولك بصراحة لو فيه حاجة تستاهل ولا لأ.**
> **أنهي يوم يناسبك الأسبوع ده؟**

**Touch 7 — Day 21 · the honest close.** This message reliably gets the highest reply rate of the whole sequence. Send it exactly as written; do not soften it, and do not follow it with anything.
> **أستاذ [الاسم]، بعتلك كذا مرة ومجاش رد — وده عادةً معناه واحدة من اتنين: يا الوقت مش مناسب، يا الموضوع مش من أولوياتك دلوقتي.**
> **الاتنين مفهومين تماماً ومفيش أي مشكلة.**
> **هقفل الملف بتاعك عندي عشان مضايقكش تاني.**
> **ولو اتغير الوضع وبقى [المشكلة] موضوع مهم عندكم، أنا موجود في أي وقت.**
> **بالتوفيق في شغلكم 🙏**

*(Mr [name], I've messaged you several times with no reply — which usually means one of two things: either the timing isn't right, or this isn't a priority for you now. Both are completely understandable and there's no problem at all. I'll close your file so I don't bother you again. And if things change and [the problem] becomes important to you, I'm here any time. Best of luck with your work 🙏)*

Then: Closed Lost, reason `no response after full cadence`, `reengage_date` = today + 6 months.

---

## Part 8 — The stack: start with a spreadsheet

**No paid CRM on day one.** At 2–3 people with fewer than 30 live leads, a CRM is overhead that produces the *appearance* of a process while the actual discipline — log it, next action, next date — goes unpracticed. Learn the discipline in a spreadsheet, then buy the tool.

### Option A — Google Sheets (recommended)

Free, works on a phone, multiple people at once, survives a lost phone.

**Sheet 1 · `Leads`** — one row per lead, the 26 fields from Part 2 as columns.

**Sheet 2 · `Touches`** — append-only log: `lead_id`, `date`, `channel`, `direction` (in/out), `summary`, `by`.

**Sheet 3 · `Lookups`** — the fixed dropdown lists (channel, source, segment, stage, lost reason). Every select field uses Data Validation pointing here. Free-typed values destroy reporting within a month.

**Sheet 4 · `Dashboard`** — five formulas, nothing more:
- Leads this week, by source
- Leads with **blank `next_action` or blank `next_action_date`** ← the leak detector, look at it first
- Leads whose `next_action_date` is past ← overdue
- Deals by stage, with the weighted forecast from `[[Sales Playbook]]` Part 3
- Closed Lost this month grouped by reason

**Conditional formatting:** red row if `next_action_date` is in the past; amber if `date_received` is more than 24 hours ago and `stage` is still `0-Inbox`. Two colours make the SLA visible without anyone reading a report.

### Option B — Obsidian, if the founder lives in the vault

One note per lead in `06-Sales/Leads/`, filename `CS-202609-014 - [Company].md`, frontmatter carrying the Part 2 fields. A Dataview table renders the pipeline; the Kanban plugin renders the board. Advantage: the lead notes sit next to the strategy notes and link with `[[wikilinks]]`. Disadvantage: harder to share with a second person, and weak on a phone — which is where most of the leads arrive.

**Recommendation:** Sheets for the pipeline (phone-first, multi-user), Obsidian for the Diagnostic notes and Blueprints (thinking work). Link them by `lead_id`.

### Kanban board spec (Obsidian Kanban plugin compatible)

File: `06-Sales/Pipeline Board.md`

```markdown
---
kanban-plugin: board
---

## 0 · الوارد

- [ ] CS-202609-014 · شركة [X] · بحري · بورسعيد · #تشخيص-مطلوب
      وصل: 2026-09-02 09:15 · SLA: 24س · التالي: رد أولي — 2026-09-02

## 1 · تم التواصل

## 2 · مؤهل

## 3 · جلسة التشخيص

## 4 · عرض الخريطة

## 5 · الخريطة شغالة

## 6 · عرض البناء

## 7 · كسبناه

## 7 · خسرناه

%% kanban:settings
{"kanban-plugin":"board","show-checkboxes":true,"lane-width":320,"date-format":"YYYY-MM-DD"}
%%
```

Card format, fixed:
`CS-<id> · <الشركة> · <القطاع> · <المدينة> · التالي: <الإجراء> — <التاريخ>`

**Rule: the board is a view, not the record.** The spreadsheet row is the record. A card with no `التالي:` line gets deleted or fixed at the Sunday review — no exceptions.

### When to graduate to a real CRM

Move when **any two** of these are true:

1. More than **50 open leads** at once — the spreadsheet stops being scannable.
2. More than **3 people** touching leads — edit collisions and version confusion start.
3. You need automatic follow-up reminders because touches are being genuinely missed.
4. You want email/WhatsApp conversation history attached to the record automatically.
5. Someone asks for conversion rates by source and it takes more than 10 minutes to answer.
6. A lead was lost because of a data mistake, not a sales mistake.

**Do not** graduate because a CRM would look more professional. Nobody outside the company sees it.

### Which CRM, when the time comes

| Tool | Fit for an Egyptian SMB | Watch out for |
|---|---|---|
| **HubSpot Free** | Best default. Genuinely free tier, Arabic-capable UI, email tracking, unlimited contacts. | Paid tiers jump hard. Weak native WhatsApp. |
| **Zoho CRM** | Cheapest paid tier, strong Arabic support, regional presence, integrates WhatsApp Business. | Interface is dense; needs a real setup day. |
| **Bitrix24** | Free tier includes tasks and telephony. Popular in the region. | Heavy, does too much, easy to get lost in. |
| **Notion / Airtable** | Flexible, pretty, easy migration from a spreadsheet. | Not a CRM — no cadence engine, no reminders. A nicer spreadsheet. |
| **Odoo CRM** | Worth it **only** if accounting/inventory also move to Odoo. | Overkill for sales alone. |

**Choose on one criterion: WhatsApp.** In this market WhatsApp is the sales channel. A CRM that does not capture WhatsApp conversations will be abandoned within a quarter regardless of its other features.

---

## Part 9 — Daily and weekly discipline

**Daily 09:30 (15 min):** sweep all channels → log every new lead → reply to everything within SLA → clear the overdue `next_action` list.
**Daily 16:30 (10 min):** second sweep. Nothing goes overnight unanswered.
**Sunday 10:00 (45 min):** pipeline review — every Stage 2+ deal, stage, next action, date, blocker. Fix every blank field. Update the forecast.
**Monthly:** leads by source, conversion by stage, average days per stage, Closed Lost by reason. One process change from what you find.

**The only metric that matters in month one:** *leads with a blank next action = 0.* Everything else follows from that.

---

## Open questions blocking this file

→ `[[Open Questions and Decisions Needed]]`
- **Who is the Response Owner?** (blocker B5 — no team roster exists)
- **Does the website form actually deliver, and to which address?** Never verified.
- **What are the website's budget dropdown bands?** Unknown — and field 14 depends on them.
- What are the real working hours? ("Always open" on Facebook is not one.)
- Do we keep the published 24-hour promise, or remove it from the site until it has an owner?
- Sheets or Obsidian as the primary record?
- Written case-study permission from El Shoush and Osama Sakr — gates touches 4 and 5.

## Related
[[Sales Playbook]] · [[Discovery Call Script]] · [[Objection Handling]] · [[Outbound Prospecting Playbook]] · [[Qualification and Deal Review]] · [[Foundation Brief]] · [[ICP - Ideal Customer Profiles]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]
