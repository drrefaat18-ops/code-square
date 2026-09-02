---
date: 2026-09-02
type: template
tags:
  - offers
  - proposal
  - sow
  - contract
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Proposal and SOW Template — Code Square

## For future Claude

A **fill-in-the-blanks** template, not a description of one. Copy §2 (client-facing proposal) and §3–§13 (SOW) into a new note per deal, replace every `{{placeholder}}`, delete what does not apply.

Rules:
- Every `{{placeholder}}` must be replaced before sending. A proposal that goes out with `{{` in it is the fastest way to lose a deal.
- **No prices are pre-filled anywhere.** Real pricing is blocker **B4**, unanswered. Every commercial figure carries `❓ NEEDS FROM FOUNDER:`. Derive numbers from `[[Pricing and Packaging]]` §2 (cost floor) and §3 (value ceiling) — never guess.
- The approach section maps to the **website's 4-phase methodology** (التأسيس / المعمارية / الهندسة / الإطلاق والتطوير). That is the canonical framework in this vault; the Facebook 5-stage model is retired (`[[Foundation Brief]]` §0.6).
- Only **four** clients exist (M Tech Square, Techno Square, El Shoush Travel, Osama Sakr Manning Agency). §2.6 may reference **only these**. Never invent a reference.
- Arabic is the default client-facing language for Egypt; English/MSA for Gulf. Both are provided for the key sections. Never machine-translate between them.
- This is not legal advice. §10, §11 and §13 need a lawyer's review before first use. Tracked in `[[Open Questions and Decisions Needed]]`.

---

## 1. How to use this document

| Part | Sections | Purpose | Audience |
|---|---|---|---|
| **Proposal** | §2 | Persuade. Why us, why this, why now | Decision-maker. Often read on a phone |
| **SOW** (Scope of Work) | §3–§13 | Protect. Exactly what is and is not being bought | Signed by both. Read again only when there is a dispute |

**SOW** = the contractual annex defining scope, deliverables, timeline, and terms. The proposal sells; the SOW is what you point at eleven weeks later. Send them as **one document, in this order**. Splitting them means the client signs the enthusiasm and never reads the boundaries.

**Length discipline:** proposal ≤ 4 pages. Nobody reads page 5. Detail belongs in the SOW.

| Rule | Why |
|---|---|
| Present the proposal **live**, never by email alone | An emailed price is a number with no context; the first objection you never hear is the one that kills the deal |
| Lead with **their** problem in **their** words | `[[Offer Ladder]]` §3 — the Diagnostic exists to give you this language |
| Include the **retainer line in the original proposal** | `[[Service Catalog]]` §8 attach rule. Not an upsell after handover |
| Quote validity **30 days** | `[[Pricing and Packaging]]` §9.4 |
| One price, not a menu of three | A menu invites the client to design the project. Options belong in the phasing, not the price |

---

## 2. THE PROPOSAL — client-facing

### 2.0 Cover

```markdown
# {{عنوان المشروع}}
### عرض فني ومالي مقدم إلى {{اسم الشركة}}

**إعداد:** Code Square — {{اسم مقدم العرض}}
**التاريخ:** {{التاريخ}}
**رقم العرض:** CS-{{YYYY}}-{{NNN}}
**صالح حتى:** {{التاريخ + 30 يوم}}
**جهة الاتصال:** {{الاسم}} · {{تليفون}} · {{إيميل}}

---
Code Square — إحدى شركات مجموعة M Tech Square
شارع ممفيس، بورسعيد، مصر 42511
```

**EN cover** — identical fields: *Technical & Commercial Proposal for {{Company}} · Prepared by · Date · Ref · Valid until · Contact.*

> Never put a logo-only cover with no content. The first screen should already say what this is about.

### 2.1 الملخص التنفيذي / Executive summary

Half a page. Written last. Assume it is the only part the decision-maker reads.

```markdown
## الملخص التنفيذي

{{اسم الشركة}} بتخسر {{الرقم من جلسة التشخيص}} بسبب {{المشكلة}}.

بنقترح بناء {{الحل في جملة واحدة}} على {{عدد}} مراحل، النسخة الأولى
خلال {{المدة}}، وبعدها اتفاق شهري للدعم والتطوير المستمر.

| | |
|---|---|
| المشكلة | {{بكلمات العميل}} |
| الحل المقترح | {{جملة واحدة}} |
| مدة النسخة الأولى | {{المدة}} |
| الاستثمار | ❓ NEEDS FROM FOUNDER: التكلفة الإجمالية — B4 |
| العائد المتوقع | {{القيمة السنوية من §2.2}} — استرداد التكلفة خلال {{الشهور}} |
| الخطوة التالية | {{اجتماع / توقيع / دفعة مقدمة}} بتاريخ {{التاريخ}} |
```

**EN:** *{{Company}} currently loses {{number}} to {{problem}}. We propose {{solution in one sentence}}, delivered in {{n}} phases, with V1 live in {{duration}}, followed by a monthly agreement for support and continuous improvement.*

### 2.2 فهمنا للمشكلة / Understanding the problem

**The most important section in the proposal.** Restated in the client's own words from the Diagnostic (`[[Offer Ladder]]` §3). If they do not recognise their own situation here, nothing after it lands.

```markdown
## فهمنا للمشكلة

### الوضع الحالي
{{وصف العملية الحالية خطوة بخطوة، بلغة العميل. من غير مصطلحات تقنية.}}

### فين بالظبط بيضيع الوقت والفلوس
| # | النقطة | التأثير الحالي | المصدر |
|---|---|---|---|
| 1 | {{...}} | {{الرقم}} | كلام {{الاسم}} في جلسة التشخيص بتاريخ {{التاريخ}} |
| 2 | {{...}} | {{الرقم}} | |
| 3 | {{...}} | {{الرقم}} | |

### تكلفة إن الوضع يفضل زي ما هو
{{القيمة السنوية المحسوبة — ساعات × تكلفة الساعة + الأخطاء + الفرص الضايعة}}

### اللي مش هنحله في المرحلة دي
{{على الأقل بند واحد. الوضوح هنا بيبني ثقة أكتر من أي وعد.}}
```

> Cite the source of every number (`"من كلام {{الاسم}} في جلسة {{التاريخ}}"`). It signals these are *their* figures, not Code Square's marketing. `[[Pricing and Packaging]]` §3.3 — value pricing only works if the value is stated out loud.

**EN heading:** *Understanding the problem — Current state · Where time and money leak today · The cost of doing nothing · What this phase will not solve.*

### 2.3 المنهجية / Our approach — the 4 phases

```markdown
## منهجيتنا

| # | المرحلة | إيه اللي بيحصل | المخرجات | المدة |
|---|---|---|---|---|
| 1 | **التأسيس** (Discovery) | استكشاف استراتيجي لفهم الرؤية، الأهداف، ورسم خارطة الطريق للمتطلبات التقنية | {{وثيقة المتطلبات · رحلة المستخدم · النطاق بالأولوية}} | {{المدة}} |
| 2 | **المعمارية** (Architecture) | تصميم مخططات هيكلية متينة مصممة للتوسع والأداء | {{المخطط المعماري · نموذج البيانات · تصميم الشاشات}} | {{المدة}} |
| 3 | **الهندسة** (Engineering) | بناء المشروع بدقة هندسية مع أفضل الممارسات البرمجية | {{النظام العامل · الاختبارات · عروض كل أسبوعين}} | {{المدة}} |
| 4 | **الإطلاق والتطوير** (Launch & Iterate) | إطلاق انسيابي متبوع بحلقات تحسين مستمرة | {{النشر · التدريب · التوثيق · الاتفاق الشهري}} | {{المدة}} |
```

Phase descriptions are the website's own verbatim wording — `stated`. Use them exactly; consistency between what the site says and what the proposal says is free credibility.

> If a `[[Offer Ladder]]` Blueprint was purchased, phase 1 and part of phase 2 are **already complete**. Say so, and show the credit in §2.5.

**EN:** *Discovery · Architecture · Engineering · Launch & Iterate.*

### 2.4 المخرجات / What you receive

```markdown
## اللي هتستلمه

| # | المخرج | الوصف | المرحلة |
|---|---|---|---|
| 1 | {{...}} | {{...}} | {{...}} |

بالإضافة إلى:
- الكود المصدري كامل، ملكك بالكامل بعد سداد الدفعة الأخيرة
- كل الحسابات (الاستضافة، النطاق، المتاجر) باسم شركتك من اليوم الأول
- توثيق التشغيل ودليل الاستخدام
- جلسة تدريب واحدة **مسجلة** — تقدر تدرب بيها موظفين جدد من غير ما ترجعلنا
- ضمان ٣٠ يوم على أي عطل في النطاق المتفق عليه
```

### 2.5 الاستثمار / Commercial summary

```markdown
## الاستثمار

| البند | المبلغ |
|---|---|
| {{المرحلة / النطاق}} | ❓ NEEDS FROM FOUNDER — B4 |
| خصم خريطة المشروع (مدفوعة مسبقًا) | −{{مبلغ الخريطة}} |
| **الإجمالي** | ❓ NEEDS FROM FOUNDER — B4 |
| الدعم الشهري — باقة {{الباقة}} | ❓ NEEDS FROM FOUNDER — B4 / شهريًا |

### جدول الدفع
| # | الدفعة | التوقيت | النسبة |
|---|---|---|---|
| 1 | دفعة مقدمة | قبل بدء العمل | ❓ NEEDS FROM FOUNDER (المقترح ٤٠–٥٠٪) |
| 2 | {{مرحلة}} | عند قبول {{المخرج}} | ❓ |
| 3 | الدفعة الأخيرة | عند القبول النهائي | ❓ (المقترح ≤ ٢٠٪) |

**العملة:** {{EGP / USD / SAR}} · **العرض صالح ٣٠ يوم من تاريخه**
{{بند تعديل سعر الصرف — للمشاريع أكتر من ٣ شهور بالجنيه}}
```

> **Show the Blueprint credit as a visible line.** `[[Pricing and Packaging]]` §5.7: the build is priced on build scope alone, and the credit is presented as a subtraction. The client sees the concession; the price integrity survives.
>
> **The retainer line is mandatory in every build proposal** — `[[Service Catalog]]` §8.

### 2.6 ليه Code Square / Why us

Only what can be proven. `[[Foundation Brief]]` §0.5.

```markdown
## ليه Code Square

- **لا نطارد الصيحات العابرة؛ بل نبني أسساً تدوم طويلاً.**
- **لسنا مجرد مبرمجين؛ نحن مهندسو أنظمة برمجية قابلة للتوسع.**
- **لسنا مجرد مزودي خدمة؛ نحن شريكك التكنولوجي الاستراتيجي.**

### أعمال مشابهة
{{اختار ١–٢ بس من الأربعة الموجودين فعلًا:}}
- **وكالة أسامة صقر** — منصة إدارة وكالة: توظيف، تتبع مشاريع، لوحات تحليلات لحظية
- **نظام El Shoush للسفر** — نظام حجز وإدارة سفر متعدد اللغات مع تكامل الخرائط
- **منصة Techno Square** — منصة تعليمية مع تطبيق جوال ولوحة تحكم وتسجيل
- **موقع M Tech Square** — موقع مؤسسي متعدد العلامات، عربي وإنجليزي

{{لو المشروع في مجال بحري/لوجستي: اربطه بأسامة صقر صراحةً — ده أقوى دليل عندنا في القطاع ده.}}
```

> **Four projects exist. Reference only those.** No "trusted by X companies", no client counts, no years-in-business. `[[Foundation Brief]]` §0.1. Do not publish a client name without written permission on file (`[[Portfolio and Case Studies]]`).
>
> Banned in every proposal: أقوى فريق · أفضل شركة · حلول متكاملة · أحدث التقنيات · Awwwards-tier · 99.9% uptime · SLA Guarantees · worldwide.

### 2.7 الخطوة التالية / Next step

```markdown
## الخطوة التالية

1. مراجعة العرض ورد بأي أسئلة بحلول {{التاريخ}}
2. توقيع نطاق العمل المرفق
3. سداد الدفعة المقدمة — العمل بيبدأ خلال {{عدد}} أيام عمل من وصولها
4. اجتماع الانطلاق يوم {{التاريخ}}

**العرض صالح حتى {{التاريخ}}.**
```

One next step with a date. "Let us know what you think" is not a next step.

---

## 3. THE SOW — scope of work

```markdown
# نطاق العمل / Statement of Work
**المشروع:** {{...}} · **المرجع:** CS-{{YYYY}}-{{NNN}}
**بين:** Code Square ("المنفذ") و {{الاسم القانوني الكامل}} ("العميل")
**التاريخ:** {{...}} · **الإصدار:** {{1.0}}

نطاق العمل ده جزء لا يتجزأ من العرض رقم {{المرجع}}.
في حالة أي تعارض، **نطاق العمل ده هو المرجع**.
```

---

## 4. النطاق — داخل وخارج / Scope in and out

```markdown
## ٤.١ داخل النطاق
| # | البند | الوصف | معيار القبول (§8) |
|---|---|---|---|
| 1 | {{...}} | {{وصف محدد وقابل للقياس}} | AC-{{n}} |

## ٤.٢ خارج النطاق صراحةً
| # | البند | ملاحظة |
|---|---|---|
| 1 | {{...}} | يمكن تسعيره في مرحلة لاحقة |

{{الصق البنود المستبعدة من [[Service Catalog]] لخط الخدمة المعني — الأقسام §2–§8}}

**البنود المستبعدة القياسية في كل المشاريع:**
- المحتوى، النصوص، الترجمة، التصوير
- رسوم الاستضافة، النطاق، الشهادات، المتاجر، بوابات الدفع، مزودي الذكاء الاصطناعي — كلها بحساب العميل وباسمه
- التسويق، الإعلانات، تحسين محركات البحث كمحتوى
- التكاملات غير المذكورة بالاسم في §4.1
- الأنظمة اللي مالهاش API ولا تصدير بيانات
- الدعم بعد ضمان الـ٣٠ يوم (ده بند الاتفاق الشهري)
- جولات مراجعة تصميم أكتر من جولتين
- أي حاجة مش مكتوبة في §4.1
```

> **§4.2 is the most commercially valuable page in the document.** Every dispute an agency has is about something that was in neither list. `[[Service Catalog]]` §9. If it is not written in §4.1, it is not included — say that sentence out loud at kickoff.

**EN:** *In scope · Explicitly out of scope · Standard exclusions across all projects.*

---

## 5. المخرجات / Deliverables

```markdown
| # | المخرج | الصيغة | المرحلة | تاريخ التسليم | معيار القبول |
|---|---|---|---|---|---|
| D1 | {{...}} | {{Figma / كود / وثيقة / نظام يعمل}} | {{1–4}} | {{...}} | AC-{{n}} |
```

Every deliverable needs a **format**. "التصميم" is a dispute; "٢٤ شاشة في Figma + نموذج تفاعلي" is a deliverable.

---

## 6. الجدول الزمني والمراحل / Timeline and milestones

```markdown
| # | المرحلة | البداية | النهاية | مخرجات | بوابة قبول | دفعة |
|---|---|---|---|---|---|---|
| M1 | التأسيس | {{...}} | {{...}} | D1, D2 | ✅ | ❓ NEEDS FROM FOUNDER |
| M2 | المعمارية | | | D3 | ✅ | ❓ |
| M3 | الهندسة | | | D4–D7 | ✅ | ❓ |
| M4 | الإطلاق | | | D8 | ✅ | ❓ |

### مسؤوليات العميل بمواعيدها
| # | المطلوب من العميل | التاريخ النهائي | تأثير التأخير |
|---|---|---|---|
| C1 | {{المحتوى / الصلاحيات / البيانات}} | {{...}} | الجدول بيتأجل يوم بيوم |

### إيقاع العمل
- تقرير أسبوعي مكتوب: اتعمل إيه / الجاي / المعطل / قرارات مطلوبة
- **عرض حي للنظام كل أسبوعين** — البرنامج الشغال هو المقياس الوحيد للتقدم
- قبول مكتوب عند كل بوابة
```

Put the **client's own deadlines in the same table as Code Square's**. It is the only way the 3-working-day feedback SLA becomes real rather than aspirational.

---

## 7. الافتراضات والاعتماديات / Assumptions and dependencies

```markdown
## الافتراضات
التقديرات والأسعار في العرض ده مبنية على الافتراضات دي. **لو اتغير أي افتراض، الجدول والسعر بيتراجعوا.**

| # | الافتراض | لو اتغير |
|---|---|---|
| A1 | العميل بيرد على المراجعات خلال **٣ أيام عمل** | تأجيل يوم بيوم + رسوم إعادة تعبئة بعد {{n}} يوم تراكمي |
| A2 | شخص واحد محدد بالاسم له صلاحية القبول | |
| A3 | {{النظام الخارجي}} عنده API موثق وبيئة اختبار | يتحول البند لعمل بالوقت والمواد |
| A4 | المحتوى بيوصل بالكامل بتاريخ {{...}} | |
| A5 | عدد الشاشات = {{n}}، جولتين مراجعة | شاشات إضافية بطلب تغيير |
| A6 | تصدير بيانات النظام القديم متاح بصيغة قابلة للقراءة | |
| A7 | مافيش متطلبات تنظيمية أو اعتمادات خارجية غير المذكورة | |

## الاعتماديات
| # | الاعتمادية | المسؤول | تاريخ الاحتياج |
|---|---|---|---|
```

Estimation assumptions come from `[[Scoping and Estimation Guide]]`. **Write down every assumption made while estimating** — an unwritten assumption is a free option the client gets to exercise later.

---

## 8. معايير القبول / Acceptance criteria

```markdown
| # | المخرج | معيار القبول — قابل للاختبار | طريقة الاختبار |
|---|---|---|---|
| AC-1 | D1 | {{"مستخدم بصلاحية X يقدر يعمل Y وينتج Z"}} | عرض حي على بيئة الإنتاج |

### عملية القبول
1. Code Square بتسلم وتخطر العميل
2. العميل عنده **{{n}} أيام عمل** (المقترح ٥) للاختبار
3. القبول = توقيع، **أو** عدم الرد خلال المدة = قبول ضمني
4. الرفض لازم يكون **مكتوب ومحدد**، ومرتبط بمعيار قبول بالاسم
5. طلبات خارج معايير القبول = طلبات تغيير (§9)، مش أسباب رفض
```

**Deemed acceptance after silence is essential.** Without it, an unresponsive client freezes the final payment indefinitely and the project never ends.

---

## 9. إدارة التغيير / Change control

```markdown
كل تغيير على النطاق الموقّع لازم يكون **مكتوب**. مافيش نطاق شفهي.

### نموذج طلب التغيير
| الحقل | القيمة |
|---|---|
| رقم الطلب | CR-{{NNN}} |
| الوصف | {{...}} |
| السبب | {{...}} |
| المجهود | {{n}} يوم |
| التكلفة | ❓ NEEDS FROM FOUNDER — السعر اليومي القياسي، بدون خصم المشروع |
| تأثير الجدول | +{{n}} يوم |
| صالح حتى | {{التاريخ + ١٤ يوم}} |
| التوقيع | ______ |

- طلبات التغيير بتتسعّر بالسعر القياسي — الخصم كان مقابل النطاق الأصلي
- التغييرات المتراكمة اللي بتتعدى {{n}}٪ من النطاق الأصلي بتستدعي **إعادة تخطيط وتسعير كاملة**، مش طلب تغيير جديد
```

Full policy: `[[Pricing and Packaging]]` §8. The standard verbal response is **"فكرة كويسة — دي خارج النطاق الحالي، هبعتلك طلب تغيير النهاردة"** — never "سهلة، هعملهالك".

---

## 10. الملكية الفكرية والبيانات / IP and data ownership

```markdown
### ١٠.١ الكود والمخرجات
ملكية الكود المخصص والمخرجات المذكورة في §5 بتنتقل للعميل **بالكامل عند سداد الدفعة الأخيرة**. قبل كده، ترخيص استخدام مؤقت لأغراض المراجعة والاختبار بس.

### ١٠.٢ أدوات Code Square السابقة
المكتبات والأدوات وأطر العمل الداخلية اللي طورتها Code Square قبل المشروع بتفضل ملك Code Square، **مرخصة للعميل ترخيص دائم غير حصري** للاستخدام داخل النظام المسلَّم.

### ١٠.٣ مكونات الطرف الثالث
تخضع لتراخيصها الخاصة، ومذكورة في {{ملحق}}.

### ١٠.٤ بيانات العميل
بيانات العميل ملك العميل في كل الأوقات. Code Square معالج للبيانات مش مالك. **التصدير متاح بصيغة قياسية عند الطلب، في أي وقت، بدون رسوم.**

### ١٠.٥ الحسابات
كل الحسابات (النطاق، الاستضافة، المتاجر، بوابات الدفع، مزودي الذكاء الاصطناعي) **باسم العميل من اليوم الأول**.

### ١٠.٦ حقوق العرض
☐ العميل بيوافق إن Code Square تعرض المشروع باسم الشركة في أعمالها
☐ العميل بيوافق على مشاركة أرقام قبل/بعد لدراسة حالة
☐ العميل **مش** موافق (اذكر السبب: {{...}})
```

> **§10.6 must be ticked at signature.** `[[Foundation Brief]]` §7.1 records that missing permissions are currently blocking publication of the only proof the company owns. Asking eight months later is why. Metrics are a **deliverable**, not a favour (`[[Service Catalog]]` §9).

**EN summary:** *Custom code and deliverables transfer on final payment. Code Square retains pre-existing tools, licensed perpetually and non-exclusively for use in the delivered system. Client data belongs to the client at all times and is exportable free of charge. All third-party accounts are registered in the client's name from day one. Portfolio and metric rights per the checkboxes above.*

---

## 11. الشروط التجارية / Commercial terms

```markdown
| البند | القيمة |
|---|---|
| قيمة العقد | ❓ NEEDS FROM FOUNDER — B4 |
| العملة | {{EGP / USD / SAR}} |
| الدفعة المقدمة | ❓ (المقترح ٤٠–٥٠٪) — **العمل مابيبدأش قبل وصولها فعليًا** |
| شروط السداد | خلال ❓ يوم من الفاتورة (المقترح ١٤) |
| غرامة التأخير | ❓٪ شهريًا |
| إيقاف العمل | بعد ❓ يوم تأخير (المقترح ١٥)، بإخطار كتابي مسبق |
| بند سعر الصرف | لو تحرك USD/EGP أكتر من ❓٪ (المقترح ١٠٪) بين التوقيع والمرحلة، الدفعات المتبقية بتتعدل بالفرق — **في الاتجاهين** |
| الرسوم البنكية | على العميل |
| الضرائب | {{مذكورة/غير مذكورة}} — تُضاف حسب القانون |
| صلاحية العرض | ٣٠ يوم |
| الإنهاء | {{n}} يوم إخطار كتابي؛ العميل بيسدد كل العمل المنجز والملتزم به حتى تاريخ الإنهاء |
```

All figures from `[[Pricing and Packaging]]` §2, §7, §9. **Never fill these in without the founder's decision — blocker B4.**

---

## 12. الضمان والدعم / Warranty and support

```markdown
### الضمان
**٣٠ يوم** من تاريخ القبول. بيغطي العيوب مقابل النطاق المتفق عليه بس. **مش** نافذة تغييرات مجانية.

مش مشمول: تغييرات العميل على النظام · مشاكل بسبب مورد تاني · تغييرات من طرف ثالث · طلبات جديدة.

### الاتفاق الشهري (اختياري لكنه مقترح بشدة)
| | أساسي | نشط | شريك تقني |
|---|---|---|---|
| السعر الشهري | ❓ | ❓ | ❓ |
| ساعات التطوير المشمولة | ❓ | ❓ | ❓ |
| هدف الاستجابة (S1) | ❓ | ❓ | ❓ |
| مراجعة خارطة الطريق | سنوي | ربع سنوي | شهري |

- الساعات المشمولة **مابتترحّلش** للشهر اللي بعده
- الحد الأدنى للمدة ٣ شهور، إخطار الإنهاء ٣٠ يوم
- زيادة سنوية ❓٪ — بند إجباري
- الساعات الزيادة بتتحاسب بالسعر القياسي بدون خصم
```

Tier structure: `[[Pricing and Packaging]]` §6. **No uptime percentage appears anywhere** — `[[Foundation Brief]]` §5 bans it until a real SLA document exists (`[[Service Catalog]]` §10).

---

## 13. التوقيعات / Signatures

```markdown
بالتوقيع أدناه، الطرفان بيوافقوا على العرض ونطاق العمل ده بالكامل، بما فيهم النطاق (§4)، المخرجات (§5)، الجدول (§6)، الافتراضات (§7)، معايير القبول (§8)، إدارة التغيير (§9)، الملكية الفكرية (§10)، والشروط التجارية (§11).

| عن العميل | عن Code Square |
|---|---|
| الاسم: ____________ | الاسم: ____________ |
| الصفة: ____________ | الصفة: ____________ |
| الشركة: ___________ | Code Square |
| التوقيع: __________ | التوقيع: __________ |
| التاريخ: __________ | التاريخ: __________ |

**الشخص المفوّض بالقبول من جانب العميل:** {{الاسم}} · {{الإيميل}} · {{تليفون}}
**مدير المشروع من جانب Code Square:** {{الاسم}} · {{الإيميل}} · {{تليفون}}
```

**EN:** *By signing below, both parties agree to this Proposal and Statement of Work in full, including Scope (§4), Deliverables (§5), Timeline (§6), Assumptions (§7), Acceptance Criteria (§8), Change Control (§9), IP and Data Ownership (§10), and Commercial Terms (§11).*

**Name one authorised approver on each side.** A committee cannot accept a deliverable.

---

## 14. Pre-send checklist

| ☐ | Check |
|---|---|
| ☐ | No `{{` remains anywhere in the document |
| ☐ | No `❓ NEEDS FROM FOUNDER` remains — every price is a real, founder-approved number |
| ☐ | Client's legal entity name is exact |
| ☐ | §2.2 uses the client's own words and cites the Diagnostic date |
| ☐ | §4.2 exclusions pasted from the right `[[Service Catalog]]` service line |
| ☐ | Every deliverable in §5 has a format and an acceptance criterion |
| ☐ | Client's own deadlines appear in §6 |
| ☐ | Every estimation assumption is written in §7 |
| ☐ | §10.6 portfolio/metrics checkboxes present |
| ☐ | Retainer line included (§2.5 and §12) |
| ☐ | Quote validity date stated, 30 days |
| ☐ | FX clause present if EGP and > 3 months |
| ☐ | No banned phrase (`[[Foundation Brief]]` §5), no uptime %, no invented client |
| ☐ | Only real projects referenced — the four that exist |
| ☐ | Proposal ≤ 4 pages |
| ☐ | Booked to present **live**, not emailed alone |

---

## Related

[[Foundation Brief]] · [[Service Catalog]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Scoping and Estimation Guide]] · [[Sales Playbook]] · [[Delivery Process]] · [[ICP - Ideal Customer Profiles]] · [[Portfolio and Case Studies]] · [[Lead Intake and CRM]] · [[Open Questions and Decisions Needed]]
