---
date: 2026-09-02
type: sales-playbook
tags:
  - sales
  - outbound
  - prospecting
  - maritime
  - port-said
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Outbound Prospecting Playbook — التواصل المبادر

## For future Claude

How Code Square **generates demand deliberately** instead of waiting for someone to message the page. Today inbound is effectively zero — 74 Facebook followers, 1–4 reactions per post, no website traffic because the TLS certificate is expired and the site is not server-rendered (`stated`, `[[Foundation Brief]]` §1 and the website evidence note). Waiting is not a strategy when nobody can find you.

The beachhead is **maritime, logistics and port services around Port Said and the Suez Canal** (`proposed`, `[[Foundation Brief]]` §4, segment A), because Code Square already shipped the Osama Sakr Manning Agency system in that exact vertical in that exact city.

Rules: no invented prices, no invented client names or results, no invented team members (owner `TBD`). All buyer-facing wording is real Egyptian dialect; Gulf variants are `[فصحى]`.

**One structural warning that governs everything below:** outbound to Port Said works because of proximity and reputation, not volume. There are a few hundred realistic targets in this city, not thousands. Burning them with generic mass messaging destroys the only asset that makes this playbook work. **Twenty well-researched touches beat two hundred blind ones**, and in a city this size a bad message travels.

---

## Part 1 — Vocabulary

| Term | Plain meaning |
|---|---|
| **Outbound** (تواصل مبادر) | We contact them first. Opposite of inbound, where they contact us. |
| **Target list** (قائمة مستهدفة) | The named companies we intend to approach, researched before any contact. |
| **Sequence** (سلسلة تواصل) | A planned series of touches across channels over a set number of days. |
| **Touch** | One contact attempt — a message, a call, a visit. |
| **Trigger event** (إشارة توقيت) | Something that just happened at the company making now a good moment: expansion, a new hire, a new branch, a new contract. |
| **Champion** (النصير) | Someone inside the company who wants this to happen and will argue for it when we're not in the room. |
| **Gatekeeper** (حارس البوابة) | The receptionist, secretary, or office manager who decides whether we reach the decision-maker. Treat them as a person, not an obstacle. |
| **Beachhead** (رأس الجسر) | The one narrow market you win completely before expanding. |

---

## Part 2 — Building the target list

### 2.1 Who exactly we are looking for

| Sub-segment | Arabic | What they do | Why they hurt |
|---|---|---|---|
| **Manning / crewing agencies** | وكالات توظيف بحري / تطقيم | Recruit and place seafarers on ships | Certificates, medicals, visas, contracts, rotations — all expiry-dated, all currently in Excel. **We have already built this.** |
| **Shipping agencies** | وكالات ملاحية | Represent vessel owners at port — clearance, berthing, supplies | Every call is time-critical; every port call generates a paper trail across many parties |
| **Freight forwarders** | شركات شحن وتخليص | Move cargo door to door | Shipment tracking, quotes, documents, client status calls all day |
| **Customs brokers** | مخلصون جمركيون | Clear cargo through customs | Document sets per shipment, deadlines, fines for errors |
| **Stevedoring / port services** | مناولة وخدمات الموانئ | Loading, unloading, equipment | Shift scheduling, equipment tracking, labour records |
| **Ship chandlers / supply** | تموين السفن | Supply vessels with provisions and spares | Orders against a vessel's short port window; catalogue and quotes |
| **Marine survey / inspection** | مسح ومعاينة بحرية | Inspect and certify | Report generation, photos, scheduling |

**Best-fit profile:** 5–50 employees, family-owned or owner-managed, business is real and profitable, running on **Excel plus WhatsApp**, and the owner is reachable. Below 5 employees there is usually no budget; above 50 there is usually an IT department and a procurement process that a two-person team should not fight yet.

### 2.2 Where to actually find them

Sources ranked by how directly they produce a named company with a phone number.

| # | Source | What you get | How |
|---|---|---|---|
| **1** | **Port Said Chamber of Shipping — member list** (الغرفة التجارية / غرفة الملاحة ببورسعيد) | The single best source: a published list of exactly these companies, by category, with contact details. Members are, by definition, real registered businesses. | Request or download the member directory. Then also: attend a members' event. A chamber introduction is worth twenty cold messages. |
| **2** | **Port Said Chamber of Commerce** (الغرفة التجارية ببورسعيد) | Broader membership — includes forwarders, brokers, traders | Same approach. Ask whether they have a technology or digitalisation committee. |
| 3 | **Suez Canal Authority / Port Said Port Authority published lists** (هيئة قناة السويس · هيئة ميناء بورسعيد) | Licensed agents and service providers. Being licensed is itself a qualification signal. | Authority websites and published circulars. |
| 4 | **Physical proximity** — the streets around the port and the customs area | Company names on doors and signage, walking distance | Walk the district with a notebook. This is the most underrated method available and costs nothing but shoe leather. |
| 5 | **Egyptian shipping/logistics associations and syndicates** | Member lists, events, published contacts | Ask each association about member events and sponsorship. |
| 6 | **LinkedIn** — search by company location Port Said + industry Maritime/Logistics | Names and titles of actual people, plus job postings that reveal pain | Free search plus company pages. Job posts are trigger events. |
| 7 | **Facebook groups and pages** for Port Said trade and shipping | Company pages, active owners, real conversations | Egyptian SMBs are far more active on Facebook than LinkedIn. |
| 8 | **Google Maps** — search each sub-segment term in Arabic and English around Port Said | Address, phone, sometimes a website, and whether they are near you | Fastest way to get from zero to a hundred names. |
| 9 | **Existing client's network** | The strongest source of all | Osama Sakr Manning Agency knows every other agency in the city. See Part 6 — **but ask permission first**. |
| 10 | **Egyptian B2B directories** (Yellow Pages Egypt, sector directories) | Bulk names, variable accuracy | Verification pass required; treat as raw material. |

**Where to start, concretely, in week one:** the Chamber of Shipping member list, cross-checked against Google Maps for location and phone, filtered to companies within driving distance. That alone produces a workable first 50.

### 2.3 The list schema

Same file, same discipline as `[[Lead Intake and CRM]]`. One row per company.

| Field | Notes |
|---|---|
| `company_name_ar` / `company_name_en` | |
| `sub_segment` | From the table in §2.1 |
| `address` | Street-level. Determines whether an in-person visit is possible. |
| `distance` | Walking · short drive · out of city |
| `phone` / `whatsapp` | |
| `contact_name` / `title` | Blank is acceptable at first — filling it is the research job |
| `is_decision_maker` | yes / no / unknown |
| `source` | Chamber · Maps · LinkedIn · walk · referral |
| `trigger_event` | §3.2 — and the date it happened |
| `research_done` | ✅ before any contact. **Gate.** |
| `sequence_stage` | 0–6 |
| `last_touch` / `next_touch` | Dates |
| `outcome` | |

**Hard gate: no company is contacted while `research_done` is blank.** Ten minutes of research is the entire difference between an outbound message and spam, and it is the rule most likely to be quietly broken under time pressure.

---

## Part 3 — Research before contact

### 3.1 The ten-minute checklist

| # | Question | Where |
|---|---|---|
| 1 | What exactly do they do, in one sentence? | Their page, Maps, chamber listing |
| 2 | Roughly how big — how many employees, how many branches? | LinkedIn, Facebook, the office itself |
| 3 | Who owns or runs it? Is the name findable? | Facebook, LinkedIn, chamber listing |
| 4 | Do they have a website? Does it work? Is it current? | Open it |
| 5 | Are they active on Facebook? When did they last post? | Their page |
| 6 | Are they hiring? For what? | Job posts — the single richest source of pain signals |
| 7 | Any recent news — new branch, new contract, expansion, an award? | Search, their page, local news |
| 8 | Do we know anyone in common? | Ask around. In Port Said the answer is often yes. |
| 9 | Which of our four projects is closest to their shape? | `[[Portfolio and Case Studies]]` |
| 10 | **What is my single specific opening line for this company?** | Written down before contact |

If question 10 has no answer, the research is not finished. A first message that could be sent to any company will be read by none.

### 3.2 Trigger events — reach out when

| Trigger | Why it matters | How you spot it |
|---|---|---|
| **Hiring for a data-entry / coordinator / admin role** | They are about to hire a person to do what software should do. This is the strongest trigger there is. | Job posts on Facebook, LinkedIn, local groups |
| **New branch or expanded office** | Growth breaks manual processes first | Their page, a sign on a building |
| **New contract, new line, new vessel client announced** | Volume just increased | Announcements, local news |
| **New manager or new generation joining the family business** | The son or daughter who wants to modernise — the classic Egyptian SMB champion | LinkedIn, Facebook |
| **A visible complaint about delays or errors** | Public pain | Comments, reviews |
| **Regulatory or certification change in the sector** | Forced documentation change | Authority circulars, chamber news |
| **A competitor of theirs launched something digital** | Competitive pressure works faster than any argument | Watching the segment |
| **Season start** | Cargo and crewing have seasons; work while they're quiet | Sector knowledge |

Log the trigger and its date in the list. A message referencing a real event from last month lands; one referencing something from two years ago reads as a lie.

---

## Part 4 — The multi-channel sequence

Six touches over about 20 days. **In Port Said, the in-person visit is not a fallback — it is the strongest channel available and it should be planned in, not improvised.**

| # | Day | Channel | Purpose |
|---|---|---|---|
| 1 | 0 | WhatsApp | The specific opener. One question. |
| 2 | 3 | Phone | Voice contact. Gatekeeper likely. |
| 3 | 6 | **In-person visit** (if in Port Said) | The one that actually works here |
| 4 | 10 | WhatsApp | Give value, ask nothing |
| 5 | 15 | LinkedIn or email | Different channel, different framing |
| 6 | 20 | WhatsApp | The honest close |

Stop the moment they reply. Never run two sequences at the same company simultaneously.

### 4.1 Channel notes

**WhatsApp** — the primary B2B channel in Egypt. Business hours only. Never a voice note on first contact (it demands their time and feels intrusive from a stranger). Never a document, PDF, or price list on first contact. Under 80 words.

**Phone** — expect a gatekeeper. Be honest with them; they remember both honesty and manipulation, and they talk to each other.

**In-person** — the genuine advantage of being in Port Said. A stranger who walks in, asks for fifteen minutes, and does not pitch is memorable in a way no message can be. Weekday mornings. Never during a vessel's port call chaos if you can tell.

**LinkedIn** — thin among Port Said SMB owners, better for larger firms and Gulf targets. Connection request with a short note, no pitch.

**Email** — weakest here. Use for formal follow-up after contact exists, and for Gulf prospects where it is the norm.

---

## Part 5 — The actual opening messages

### 5.1 Maritime / logistics — WhatsApp, touch 1

**Manning / crewing agency (our strongest — we have the reference):**
> **أستاذ [الاسم]، صباح الخير 🙏**
> **أنا [الاسم] من Code Square — شركة برمجيات هنا في بورسعيد.**
> **إحنا شغالين على نظام لوكالة توظيف بحري في بورسعيد: بيانات البحارة، الشهادات ومواعيد انتهائها، العقود، والتقارير — كلها في مكان واحد بدل الإكسل.**
> **سؤال واحد بس: عندكم مين بيتابع مواعيد انتهاء الشهادات دلوقتي، وبيعمل ده إزاي؟**
> **لو الإجابة "إكسل وتنبيهات في دماغنا" — أنا شايف ده كتير، وعندي كلام ممكن يفيدك حتى لو مشتغلناش مع بعض.**

*(Mr [name], good morning 🙏 — I'm [name] from Code Square, a software company here in Port Said. We work on a system for a maritime manning agency in Port Said: seafarer records, certificates and their expiry dates, contracts, and reports — all in one place instead of Excel. Just one question: who tracks certificate expiry dates for you now, and how do they do it? If the answer is "Excel and reminders in our heads" — I see that a lot, and I have something that might help you even if we never work together.)*

> ⚠️ **Permission gate:** do not name Osama Sakr Manning Agency until written permission is on file (`[[Portfolio and Case Studies]]`). "وكالة توظيف بحري في بورسعيد" is accurate and needs no permission.

**Shipping agency:**
> **أستاذ [الاسم]، صباح الخير.**
> **أنا [الاسم] من Code Square، شركة برمجيات في بورسعيد.**
> **بنشتغل مع شركات في القطاع البحري واللوجستي هنا، وأكتر حاجة بتتكرر قدامي: المعلومة بتتكتب أكتر من مرة — في الإكسل، وفي الواتس، وفي الإيميل — وكل مرة فيها احتمال غلط.**
> **عندكم نفس الحكاية ولا لقيتوا طريقة؟ سؤال بجد مش مقدمة لعرض.**

*(Mr [name], good morning. I'm [name] from Code Square, a software company in Port Said. We work with companies in the maritime and logistics sector here, and the thing that keeps coming up in front of me: information gets written more than once — in Excel, in WhatsApp, in email — and each time there's a chance of error. Do you have the same story, or have you found a way around it? A genuine question, not the opening of a pitch.)*

**Freight forwarder / customs broker:**
> **أستاذ [الاسم]، صباح الخير.**
> **[الاسم] من Code Square في بورسعيد.**
> **سؤال سريع: عملاؤكم بيعرفوا شحنتهم وصلت فين إزاي — بيتصلوا ويسألوا، ولا فيه حاجة بتوريهم بنفسهم؟**
> **بسأل لأن ده أكتر حاجة بتاكل وقت الموظفين في الشركات اللي شبهكم، وفي حلول ليها مش لازم تكون معانا.**

*(Mr [name], good morning. [Name] from Code Square in Port Said. Quick question: how do your clients know where their shipment has reached — do they call and ask, or is there something that shows them themselves? I'm asking because that's the biggest time drain on staff in companies like yours, and there are solutions for it that don't have to be with us.)*

**Triggered by a job post — the highest-converting opener we have:**
> **أستاذ [الاسم]، شفت إعلانكم عن وظيفة [المسمى] وحبيت أسأل سؤال ممكن يكون مفيد قبل ما توظفوا:**
> **الشخص ده هيقضي أغلب وقته في إيه — إدخال بيانات ومتابعة وتحديث ملفات، ولا شغل محتاج قرار بشري فعلاً؟**
> **بسأل لأن لو الأولى، فيه جزء كبير من شغله ممكن يتعمل مرة واحدة ويفضل شغال، والموظف يتفرغ للحاجات اللي محدش غيره يعملها.**
> **أنا [الاسم] من Code Square في بورسعيد، وده سؤال حقيقي مش عرض.**

*(Mr [name], I saw your job posting for a [title] and wanted to ask a question that might be useful before you hire: what will this person spend most of their time on — data entry, follow-up, and updating files, or work that genuinely needs a human decision? I'm asking because if it's the first, a large part of their job could be built once and keep working, and the employee is freed for the things only they can do. I'm [name] from Code Square in Port Said, and this is a genuine question, not a pitch.)*

### 5.2 Education — WhatsApp, touch 1

> **أستاذ [الاسم]، صباح الخير 🙏**
> **أنا [الاسم] من Code Square.**
> **عندنا منصة تعليمية شغالة فعلاً — تسجيل الطلبة، متابعة الحضور، تطبيق موبايل، ولوحة تحكم للإدارة. أقدر أوريهالك شغالة دلوقتي مش سلايدات.**
> **سؤال قبل أي حاجة: الطالب اللي بيسأل عن كورس وميسجلش — بتعرفوا عددهم كام في الشهر؟**
> **الفرق بين اللي بيسأل واللي بيسجل ده فلوس على الأرض، وأغلب الأكاديميات مش بتعده.**

*(Mr [name], good morning 🙏 — I'm [name] from Code Square. We have an education platform actually running — student enrolment, attendance tracking, a mobile app, and an admin dashboard. I can show it to you live, not as slides. A question before anything: the student who asks about a course and doesn't enrol — do you know how many of those you get a month? The gap between who asks and who enrols is money on the ground, and most academies don't count it.)*

Techno Square and Online Techno Square are internal (`stated`) — **no permission needed to demo them**. This is our fastest proof asset and it should be used far more than it currently is.

### 5.3 Healthcare — WhatsApp, touch 1

The founder is a pharmacist (`stated`). That is the opener, and nobody can copy it.

> **دكتور [الاسم]، صباح الخير 🙏**
> **أنا [الاسم] من Code Square. وأنا صيدلي بالأساس قبل ما أشتغل في البرمجيات.**
> **الحتة دي بتفرق: أنا فاهم شغل الصيدلية والعيادة من جوه، مش بس كبرنامج.**
> **سؤال: إيه أكتر حاجة إدارية بتاخد من وقتك في اليوم؟**

*(Dr [name], good morning 🙏 — I'm [name] from Code Square. And I'm a pharmacist by background before I worked in software. That part matters: I understand pharmacy and clinic work from the inside, not just as a program. Question: what's the biggest administrative thing that takes your time in a day?)*

### 5.4 Phone — touch 2

**Gatekeeper:**
> **صباح الخير، أنا [الاسم] من Code Square، شركة برمجيات في بورسعيد.**
> **ممكن أكلم المسؤول عن التشغيل أو صاحب الشركة؟**
> **— بخصوص إيه؟**
> **بخصوص طريقة متابعة [البيانات/الشحنات/الشهادات] عندكم. بعتنا رسالة على الواتس قبل كده. مكالمة دقيقتين مش أكتر، ولو مش مناسب دلوقتي قوليلي أنسب وقت وأنا أكلم فيه.**

*(Good morning, I'm [name] from Code Square, a software company in Port Said. Could I speak with whoever is responsible for operations, or the owner? — Regarding what? Regarding how you track [data/shipments/certificates]. We sent a WhatsApp message before. A two-minute call, no more, and if now isn't suitable tell me the best time and I'll call then.)*

Never lie to a gatekeeper — no "he's expecting my call". Port Said is small, they talk, and the reputation you build with them is permanent.

**Decision-maker, 30 seconds:**
> **أستاذ [الاسم]، صباح الخير. [الاسم] من Code Square، شركة برمجيات في بورسعيد. هاخد دقيقتين بس.**
> **إحنا شغالين مع شركات في القطاع البحري واللوجستي هنا، وبنبني الأنظمة اللي شغلهم بيمشي عليها.**
> **مش بكلمك عشان أبيعلك حاجة دلوقتي — بكلمك عشان أسأل سؤال: [الحاجة/العملية] عندكم ماشية إزاي دلوقتي؟**
> **… (اسمع) …**
> **تمام. الكلام ده يستاهل نقعد فيه ٣٠ دقيقة، ومن غير أي التزام. وبتخرج منها بورقة مكتوبة فيها المشكلة والخطوة الأولى، سواء اشتغلنا مع بعض أو لأ. أعدي عليك يوم [يوم] الصبح؟**

*(Mr [name], good morning. [Name] from Code Square, a software company in Port Said. I'll take two minutes only. We work with companies in the maritime and logistics sector here, building the systems their businesses run on. I'm not calling to sell you anything now — I'm calling to ask a question: how does [the process] work with you at the moment? … (listen) … Right. That's worth sitting on for 30 minutes, with no obligation. And you come out with a written page containing the problem and the first step, whether we work together or not. Shall I come by on [day] morning?)*

### 5.5 In-person visit — touch 3

**Prepare:** company name and what they do, one specific question written down, the two internal projects loadable on your phone in seconds, and nothing else. **No printed brochure, no price list, no laptop.** You are not presenting; you are meeting someone.

**At reception:**
> **صباح الخير. أنا [الاسم] من Code Square، شركة برمجيات هنا في بورسعيد، على بعد [المسافة] منكم.**
> **بعتنا رسالة على الواتس وحبيت أعدي بنفسي بدل ما أفضل أبعت.**
> **مش عايز أعطّل حد — لو الأستاذ [الاسم] فاضي ١٥ دقيقة أهلاً، ولو مش فاضي، سيبولي أنسب وقت وأنا أرجع تاني.**

*(Good morning. I'm [name] from Code Square, a software company here in Port Said, [distance] from you. We sent a WhatsApp message and I wanted to come by myself instead of just messaging. I don't want to hold anyone up — if Mr [name] has 15 minutes, great; if not, give me the best time and I'll come back.)*

**If you get in:**
> **شكراً إنك خدت من وقتك. مش هطول عليك ومش معايا عرض ولا كتالوج.**
> **أنا شغال في برمجيات هنا في بورسعيد، وبشتغل مع شركات في القطاع ده. جاي بسؤال واحد بس:**
> **[العملية] عندكم ماشية إزاي دلوقتي؟**

*(Thank you for your time. I won't keep you and I don't have a proposal or a catalogue with me. I work in software here in Port Said, with companies in this sector. I came with one question only: how does [the process] work with you now?)*

**Leaving, whatever happened:**
> **شكراً. هبعتلك على الواتس اللي اتكلمنا فيه مكتوب، ولو حبيت نكمل قولي.**
> **ولو مش دلوقتي، مفيش مشكلة خالص — إحنا في نفس البلد ومش هنروح حتة.**

*(Thank you. I'll send you what we discussed on WhatsApp in writing, and if you'd like to continue, tell me. And if not now, no problem at all — we're in the same city and we're not going anywhere.)*

**Rule: never leave without the WhatsApp number.** That is the entire objective of the visit.

### 5.6 LinkedIn — touch 5

**Connection request note (300 characters max, no pitch):**
> **أستاذ [الاسم]، أنا [الاسم] من Code Square — شركة برمجيات في بورسعيد بتشتغل مع شركات القطاع البحري واللوجستي. حابب أتابع شغل [الشركة]. تحياتي.**

**After acceptance, wait 2 days, then:**
> **شكراً على الإضافة 🙏**
> **سؤال واحد لو تسمح: عندكم [العملية] بتتم إزاي دلوقتي؟ بسأل لأني بشتغل على النوع ده من الأنظمة وبحب أفهم إزاي كل شركة بتحلها بطريقتها.**

**Gulf `[فصحى]`:**
> **أستاذ [الاسم]، تحية طيبة. أنا [الاسم] من Code Square، شركة تطوير برمجيات تعمل مع شركات القطاع البحري واللوجستي.**
> **سؤال واحد إن سمحت: كيف تُدار [العملية] لديكم حالياً؟ أسأل لأننا نبني أنظمة من هذا النوع ونهتم بفهم اختلاف الممارسات بين الشركات.**

### 5.7 Touch 4 — value, ask nothing

> **أستاذ [الاسم]، مش بابعت عشان أتابع. بابعت حاجة ممكن تنفعك سواء اتكلمنا ولا لأ.**
> **من شغلنا في القطاع ده، أسهل حاجة تعملها من غير أي برنامج: خد عملية واحدة عندكم وعُدّ المعلومة بتتكتب فيها كام مرة، من أول ما توصل لحد ما تخلص.**
> **لو الرقم طلع أكتر من اتنين، فيه فلوس بتضيع كل يوم. ولو طلع اتنين أو أقل، انتوا شغالين صح فعلاً.**
> **جربها، وقولي طلع كام لو حبيت.**

*(Mr [name], I'm not messaging to follow up. I'm sending something that might be useful whether we ever talk or not. From our work in this sector, the easiest thing you can do with no software at all: take one process and count how many times the information gets written in it, from when it arrives until it's finished. If the number is more than two, money is being lost every day. If it's two or less, you're genuinely running well. Try it, and tell me what came out if you like.)*

### 5.8 Touch 6 — the honest close

> **أستاذ [الاسم]، تواصلت معاك كذا مرة ومجاش رد، ودي عادةً معناها إن الموضوع مش من أولوياتك دلوقتي — وده مفهوم تماماً.**
> **هبطل أبعتلك عشان مضايقكش.**
> **بس حابب أقولك حاجة واحدة: إحنا في بورسعيد زيكم، ولو في أي يوم احتجت رأي في حاجة تقنية — حتى لو مش هتشتغل معانا — ابعتلي وأنا أرد عليك من غير أي مقابل.**
> **بالتوفيق في شغلكم 🙏**

*(Mr [name], I've reached out several times with no reply, which usually means this isn't a priority for you right now — completely understandable. I'll stop messaging so I don't bother you. But I want to say one thing: we're in Port Said like you, and if any day you need an opinion on something technical — even if you'll never work with us — message me and I'll answer with nothing expected in return. Best of luck with your work 🙏)*

That last offer is not a tactic; honour it. In a city this size, being the person who answers a technical question for free is a distribution channel.

---

## Part 6 — Referral and partner channels

Referrals convert several times better than cold outreach in every market, and dramatically better in a relationship-driven one like Port Said. This section deserves more of the week than cold messaging does.

### 6.1 Asking an existing client

Ask **at a moment of visible success** — a delivered milestone, a working feature, a problem solved — never at the start and never in the same breath as an invoice.

> **أستاذ [الاسم]، سؤال وحضرتك مرتاح ترد عليه بلأ عادي:**
> **هل فيه حد تعرفه في نفس المجال بيعاني من نفس الحاجة اللي كانت عندكم؟**
> **مش عايزك تكلمه عني — عايز بس اسمه، وأنا أتواصل معاه بنفسي وأقوله إن حضرتك رشحته. ولو مش مرتاح، مفيش أي مشكلة والموضوع مش هيفرق في شغلنا مع بعض.**

*(Mr [name], a question and you're completely free to say no: is there someone you know in the same field suffering from the same thing you had? I don't want you to talk to him about me — I just want the name, and I'll reach out myself and say you suggested him. And if you're not comfortable, no problem at all and it changes nothing about our work together.)*

**The follow-through is what produces the second referral:** thank them the same day, and report back what happened regardless of the outcome.

### 6.2 Partner channels for maritime/logistics

| Partner type | Why they refer | What we offer them |
|---|---|---|
| **Accountants and audit offices** serving shipping companies | They see every client's broken process from the inside, and they are trusted | We never touch their accounting work; we make their data cleaner |
| **Customs brokers** | Deal with dozens of forwarders and traders | Reciprocal referral |
| **Business consultants / ISO consultants** | Recommend systems as part of their engagements | We are the implementation arm they lack |
| **Local IT and hardware suppliers** | Sell machines and networks, not software | We do not compete with them; we complete them |
| **The Chamber of Shipping / Chamber of Commerce** | Look for member benefits and educational content | A free workshop for members — see §6.3 |
| **Marine insurance brokers** | Know everyone, trusted with sensitive information | Reciprocal |

**Partner approach message:**
> **أستاذ [الاسم]، أنا [الاسم] من Code Square — شركة برمجيات في بورسعيد شغالة مع شركات القطاع البحري واللوجستي.**
> **حضرتك بتشتغل مع نفس نوع العملاء تقريباً، وإحنا مش بنتنافس — انت بتقدم [خدمته] وإحنا بنبني الأنظمة.**
> **حبيت أقعد معاك ٢٠ دقيقة نشوف لو فيه حاجة نفيد بيها بعض. مش عايز حاجة دلوقتي، بس أتعرف على شغلك.**

*(Mr [name], I'm [name] from Code Square — a software company in Port Said working with maritime and logistics companies. You work with roughly the same kind of clients, and we don't compete — you provide [their service] and we build the systems. I'd like to sit with you for 20 minutes to see if there's something we can help each other with. I don't want anything now, just to understand your work.)*

**Rule:** never offer a commission before the first successful referral, and never let money be the reason someone refers. Reputation-based referral is durable; commission-based referral produces bad-fit leads.

### 6.3 The chamber workshop play — the highest-leverage move in this file

One free 45-minute session for chamber members: *"إزاي تعرف إن شغلك محتاج نظام — وإمتى ميحتاجش"* (How to know your business needs a system — and when it doesn't).

Why it works: it puts you in front of twenty qualified owners at once, it is educational rather than promotional so the chamber will host it, and the honest framing ("and when it doesn't") is precisely what builds credibility with a sceptical audience. The offer at the end is one thing only: a free Diagnostic Session.

This one action can be worth more than a month of cold messaging. Pursue it in the first month.

---

## Part 7 — Weekly activity targets

`proposed` for the first 90 days, assuming roughly one person-day per week on prospecting.

| Activity | Weekly target |
|---|---|
| New researched companies added to the list | 15 |
| Touch-1 first contacts sent | 20 |
| Phone calls attempted | 10 |
| **In-person visits (Port Said)** | **3** |
| Value touches (touch 4) | 8 |
| Referral asks | 2 |
| Partner conversations | 1 |
| Replies received | 4–6 (expect 20–30%) |
| **Diagnostic Sessions booked from outbound** | **2** |

**Monthly:** one chamber or association event attended. One partner relationship opened. One published case study (`[[Portfolio and Case Studies]]`).

**Realistic expectation, stated plainly so nobody panics in week three:** from 20 cold touches expect roughly 4–6 replies, 2 booked sessions, and 0–1 Blueprints. Outbound compounds — month three works better than month one because the city starts recognising the name. Judge this by activity for the first six weeks, by outcomes after that.

---

## Part 8 — Rules

1. **No contact without research.** `research_done` is a gate, not a suggestion.
2. **One question per first message.** Not three.
3. **No price, ever, in an outbound message.** `[[Pricing and Packaging]]`.
4. **No attachment, PDF, or brochure on first contact.**
5. **No voice note to someone who has never spoken to you.**
6. **Never name a client without written permission on file.** Describe instead.
7. **Never lie to a gatekeeper.** Port Said is small and permanent.
8. **Business hours only.** Never Friday, never after 8pm.
9. **Stop at touch 6.** A polite exit preserves a future; persistence past it destroys one.
10. **Log every touch in the tracker** — `[[Lead Intake and CRM]]`.
11. **Never say a banned phrase** — `[[Foundation Brief]]` §5.
12. **In-person beats everything in Port Said.** If a company is within driving distance and has not replied to two messages, go.

---

## Open questions blocking this file

→ `[[Open Questions and Decisions Needed]]`
- Who runs outbound, and for how many hours a week? (owner `TBD`)
- Written case-study permission from El Shoush and Osama Sakr — gates the strongest opener in §5.1.
- Is the Chamber of Shipping member list obtainable, and at what cost or membership requirement?
- Is Code Square itself a chamber member? If not, should it join?
- Minimum project size — needed to filter the target list by company size.
- Does the founder want to be the one making in-person visits? It is the highest-converting activity and the one hardest to delegate.

## Related
[[Sales Playbook]] · [[Discovery Call Script]] · [[Objection Handling]] · [[Lead Intake and CRM]] · [[Qualification and Deal Review]] · [[Foundation Brief]] · [[ICP - Ideal Customer Profiles]] · [[Offer Ladder]] · [[Pricing and Packaging]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]]
