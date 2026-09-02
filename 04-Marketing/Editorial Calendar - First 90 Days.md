---
date: 2026-09-02
type: editorial-calendar
tags:
  - marketing
  - content
  - calendar
  - code-square
ai-first: true
status: draft
owner: TBD
confidence: proposed
---

# Editorial Calendar — First 90 Days

## For future Claude

Thirteen weeks, executable without asking a question. Every row names the post, a working Arabic headline, the format, the channel, the asset needed, the CTA, the owner, and how success is measured.

**Assumptions this calendar is built on. If any changes, the calendar changes:**
1. Beachhead = **A, maritime/logistics** (`[[Foundation Brief]]` §4). Weeks 5–13 are written for that buyer.
2. Priority 0 (website fix) completes in week 1. **If it slips, weeks 1–4 still run** — none of them depends on the site except where explicitly noted. Paid media does not start regardless.
3. Client permission is requested in week 1 and lands by week 3.
4. Three posts per week on Facebook, Sunday/Tuesday/Thursday. LinkedIn 1/week from week 3. Instagram is repurposed only and is not listed row by row.

**Owners:** F = Founder · P = Producer · D = Designer · R = Responder. Roster is `TBD` (`[[Foundation Brief]]` §10) — assign real names before week 1.

**Every headline below is a working headline.** It is a real draft in Egyptian dialect, not a description. Sharpen it, do not replace it with a topic label.

**The placeholder rule:** `[[INSERT REAL NUMBER — see Portfolio and Case Studies]]` appears wherever a number is needed and does not yet exist. A post carrying an unfilled placeholder **does not publish**.

---

## Month 1 — Fix the foundations, publish the proof

The goal of month 1 is not engagement. It is that by day 30 the company is *findable, coherent, and provable*. Judge it on assets shipped, not on likes.

### Week 1 — Foundations. Almost no publishing.

**This week is 80% infrastructure.** Resist the urge to post through it.

| Task | Detail | Owner | Done when |
|---|---|---|---|
| Renew TLS certificate | `mtechsquare.com` — currently expired | F / dev | Site loads with no browser warning |
| SSR / prerender | Angular Universal or a prerender step for `/code-square/` | dev | `view-source` shows real text |
| `sitemap.xml`, `robots.txt`, `llms.txt` | Plus page-level `<title>` + `<meta description>` for Code Square | dev | All four return 200 |
| Verify the contact form | Send a test; confirm it arrives; **name the human who owns the inbox** | F | A named owner and a working test |
| Facebook page surgery | All 14 items in `[[Social Media Playbook]]` §6 | P + D | Checklist complete |
| WhatsApp Business setup | Greeting, away message, quick replies, labels, catalogue | P | Test message returns the greeting |
| **Permission asks** | WhatsApp to El Shoush **and** Osama Sakr, script in `[[Content System]]` §3.3 | **F** | Both sent. **Do this Sunday — everything downstream waits on it** |
| Number requests | Same conversation: ask for hours saved / placements / bookings / error reduction | F | Asked |
| Analytics | GA4 or Plausible + Meta Pixel installed (the pixel does nothing yet; it starts building an audience today) | dev | Firing |
| UTM convention agreed | See `[[Paid Media Plan]]` §4 | P | Documented |

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Thu | **P1** — the reset post | **بقالنا فترة بنتكلم عن الشغل بشكل عام. من النهاردة هنتكلم عن شغل حقيقي.** | Single image | FB | 1 creative, ≤15 words | تابعنا — أول مشروع الأسبوع الجاي | P/D | 5+ reactions; 1+ comment. Baseline reset marker |

**Week 1 success metric:** the website loads clean, the page has a link and a CTA button, and both permission asks are sent. Nothing else counts.

---

### Week 2 — Case study 1: M Tech Square (no permission needed)

Start with the internal project so the engine runs while permissions are pending.

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | **P2** — the problem | **شركة بتبني الوجود الرقمي لغيرها… وملهاش وجود رقمي.** | Single image | FB | Creative + master case study draft | اقرا القصة كاملة على الموقع [link] | P/D | 8+ reactions; 20+ link clicks |
| Tue | **P3** — the discovery question | **أول سؤال سألناه مكانش "الموقع يبقى شكله إيه؟" — كان "إيه اللي ناقص؟"** | Carousel, 6 frames | FB | 6 frames + caption | نفس السؤال ينفع على شغلك — احجز جلسة تشخيص | P/D | 3+ shares; 2+ comments |
| Thu | **P4** — the idea | **الحل كان فكرة واحدة: الشركة كون، وكل شركة جواها كوكب.** | Carousel, 8 frames | FB + IG | 8 frames, screens from the site | شوف النتيجة بنفسك [link] | P/D | 10+ reactions; 30+ clicks |
| — | Website | The M Tech Square case-study page goes live | Page | Website | Master case study | — | P | Page live and indexable |

**Also this week:** follow up both permission asks if unanswered by Tuesday. Publish the four case-study pages' skeletons so links exist.

---

### Week 3 — Case study 2: Osama Sakr (the beachhead anchor)

**Gate:** publishes only with written permission on file (`[[Content System]]` §5, Gate B). If permission has not landed by Sunday, run the anonymised version — "وكالة ملاحية في بورسعيد" — and swap in the name later.

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | **P5** — the pain | **وكالة توظيف بحري بتشتغل على إكسيل وواتساب. تخيل يوم شغل واحد جواها.** | Single image | FB | Creative; client approval | لو ده شغلك، احجز جلسة تشخيص مجانية | F/P | 10+ reactions; 3+ comments from the segment |
| Tue | **P6** — the build | **بنينا لوكالة أسامة صقر نظام: توظيف، تتبع مشاريع، ولوحة تحليلات لحظية.** | Carousel, 8 frames | FB | 8 frames, redacted screens, client approval | القصة كاملة [link] | P/D | 5+ shares; 40+ clicks |
| Thu | **P7** — the number | **`[[INSERT REAL NUMBER — see Portfolio and Case Studies]]`** (e.g. "X ساعة في الأسبوع رجعت للفريق") | Single image, number only | FB + LinkedIn (EN) | The real number. **Blocks publication if empty** | عايز نفس الحسبة على شغلك؟ | F | 15+ reactions; highest-performing post of month 1 |
| — | LinkedIn | English version, founder first person | Text + image | LinkedIn | EN master | — | F | First LinkedIn post live |

**Contingency:** no permission and no number → publish P5 and P6 anonymised and hold P7. Do not invent a number under any circumstances.

---

### Week 4 — Case study 3: Techno Square + the Diagnostic Session launch

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | **P8** — the platform | **منصة تعليمية كاملة: تطبيق موبايل، لوحة تحكم، ونظام تسجيل — شغالة دلوقتي.** | Carousel, 7 frames | FB + IG | Live screens (internal, no permission needed) | شوفها شغالة [link] | P/D | 8+ reactions; 25+ clicks |
| Tue | **P9** — the offer launch | **جلسة تشخيص مجانية، ٣٠ دقيقة: هنمشي على شغلك ونطلعلك ورقة واحدة تفضل معاك.** | Single image | FB + LinkedIn | Booking link or WhatsApp link **live**; the one-page output template | احجز دلوقتي [link] | **F** | **2+ session requests** |
| Thu | **P10** — daylight | **الورقة اللي بنسلمها بعد جلسة التشخيص — دي هي بالظبط.** | Photo of the real template | FB | The actual template, filled with a dummy example | احجز جلستك | F/P | 6+ reactions; 1+ session request |
| — | Pin | Pin P6 or P7, whichever performed better | — | FB | — | — | P | Pinned |

**Month 1 review (first Sunday of month 2).** Ship a written answer to: how many enquiries came in? From which post? Is the site indexed — search `site:mtechsquare.com/code-square`? Did any post reach someone in the maritime segment? What is the single best-performing format?

**Month 1 exit criteria:** website clean and indexable · FB page rebuilt · 3 case studies published · Diagnostic Session live and bookable · ≥2 session requests · both permission conversations resolved either way.

---

## Month 2 — Beachhead problem/solution content

Every week now has a shape: **Sunday = the pain · Tuesday = the proof or the how · Thursday = daylight or POV.** Stop explaining what UI/UX is. Start describing the buyer's Tuesday morning.

### Week 5 — The cost of manual operations

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P11 | **شهادة بحّار خلصت وانت مش واخد بالك. النتيجة؟ الطاقم مش هيسافر.** | Single image | FB | Creative | لو ده بيحصل عندك، احجز جلسة تشخيص | P/D | 4+ comments |
| Tue | P12 | **إكسيل مش نظام. إكسيل ملف بيمشي مع اللي فاتحه.** | Carousel, 5 frames | FB + LinkedIn | 5 frames | ابعتلنا شغلك بيتعمل إزاي دلوقتي | P/D | 3+ shares |
| Thu | P13 — POV | **أنا صيدلي. أول مرة فهمت يعني إيه نظام مش شغال كانت جوه صيدلية، مش جوه شركة برمجيات.** | Founder photo + text | FB + LinkedIn | Real photo | ✍️ question: أنهي شغل عندك لسه بالورق؟ | **F** | Highest comment count of the month |
| — | **Outreach begins** | 10 named maritime/port accounts, WhatsApp or in person | — | Direct | The Osama Sakr PDF one-pager | Book a session | **F** | 10 contacted; 2 replies |

### Week 6 — The four-phase methodology, made concrete

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P14 | **٧٠٪ من شغل أي نظام بيحصل قبل أول سطر كود.** | Single image | FB | Creative | — | P/D | 8+ reactions |
| Tue | P15 | **منهجيتنا: التأسيس → المعمارية → الهندسة → الإطلاق والتطوير.** (canonical — the 5-stage model is retired) | Carousel, 5 frames | FB + LinkedIn | 5 frames on website tokens | احجز جلسة تشخيص — دي أول مرحلة | P/D | 4+ shares |
| Thu | P16 — daylight | **دي أسئلة جلسة التأسيس اللي بنسألها لأي وكالة ملاحية. اتفضل، خدها.** | Photo of the real question list | FB | Actual discovery doc | جاوبها لنفسك، وابعتلي النتيجة | F/P | 5+ saves; 2+ DMs |
| — | Outreach | 10 more accounts | — | Direct | One-pager | — | F | 20 cumulative |

### Week 7 — Case study 4: El Shoush + the booking domain

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P17 | **وكالة سفر بتستقبل الحجوزات من ٣ أماكن مختلفة. مين بيتابع الأخطاء؟** | Single image | FB | Client approval | — | P/D | 3+ comments |
| Tue | P18 | **نظام El Shoush: حجز وإدارة، بأكتر من لغة، ومربوط بخرائط جوجل.** | Carousel, 7 frames | FB + IG | Redacted screens, approval | القصة كاملة [link] | P/D | 30+ clicks |
| Thu | P19 | **`[[INSERT REAL NUMBER — see Portfolio and Case Studies]]`** | Number card | FB + LinkedIn | The real number | احجز جلسة تشخيص | F | 12+ reactions |
| — | Outreach | 10 more | — | Direct | — | — | F | 30 cumulative; 1 meeting |

### Week 8 — Objections, answered in public

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P20 | **"النظام ده هيكلفني كتير." طب والشغل اليدوي بيكلفك كام في الشهر؟** | Single image | FB | Creative | — | P/D | 4+ comments |
| Tue | P21 | **جاهز مقابل مخصوص: امتى الجاهز يكون قرار صح فعلاً؟** (and we will tell you when it is) | Comparison carousel, 6 frames | FB + LinkedIn | 6 frames | لو مش متأكد، احجز جلسة تشخيص | P/D | 4+ shares — the honesty is the hook |
| Thu | P22 — daylight | **إحنا قلنا لعميل "الفيتشر ده متعملوش دلوقتي". أهو السبب.** | Screenshot of the real decision | FB | Real artifact, redacted | — | F/P | 3+ comments |
| — | Month 2 review | Against `[[Marketing Strategy]]` §7 | — | — | — | — | P+F | Written |

**Month 2 exit criteria:** 4 case studies published · 30 accounts contacted · ≥2 qualified sessions held · ≥1 documented client number live · the page unmistakably speaks to one industry.

---

## Month 3 — Convert attention into Diagnostic Sessions

Every week carries a direct conversion post. The page has earned the right to ask.

### Week 9 — Make the offer impossible to misunderstand

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P23 | **جلسة التشخيص: ٣٠ دقيقة، مجانية، وبتخرج منها بورقة مكتوبة. أهي بالظبط بتحصل إزاي.** | Carousel, 5 frames | FB + LinkedIn | 5 frames | احجز [link] | F/P | **3+ requests** |
| Tue | P24 | **٥ أسئلة لو مش عارف إجابتها، شغلك بيخسر فلوس دلوقتي.** | Checklist carousel | FB | 5 frames | جاوبهم في جلسة تشخيص | P/D | 6+ saves |
| Thu | P25 | **سألني عميل: "أبدأ بتطبيق ولا بنظام داخلي؟" الإجابة اتغيرت بعد سؤالين.** | Single image + long caption | FB | Anonymised, consented | — | F | 4+ comments |
| — | Outreach | 10 more + **follow up all 30 earlier accounts** | — | Direct | — | — | F | 40 cumulative; 2 meetings |

### Week 10 — Proof stacked

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P26 | **٤ أنظمة بنيناها. دي المشكلة اللي كل واحد فيهم اتبنى عشانها.** | Carousel, 5 frames | FB + LinkedIn | Summary frames | شوف الأربعة [link] | P/D | 5+ shares; 50+ clicks |
| Tue | P27 | **"[client sentence, verbatim AR]"** — `[[INSERT REAL NUMBER — see Portfolio and Case Studies]]` if a quote is not yet approved | Quote card | FB + IG | **Approved** client quote | احجز جلسة تشخيص | F | 12+ reactions |
| Thu | P28 — daylight | **لوحة التحليلات دي بتتبني إزاي؟ خد جولة ٦٠ ثانية.** | Screen-recording video, 60s, AR subtitles | FB + IG Reels | Screen recording, dummy data | — | P/D | 300+ views; 60% completion |
| — | Reviews | Ask both clients + every past contact for a page review | — | FB | — | — | F | 4+ new reviews |

### Week 11 — The specific buyer, named out loud

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P29 | **لو عندك وكالة ملاحية أو توكيلات في بورسعيد — البوست ده ليك انت بالذات.** | Single image | FB | Creative | احجز جلسة تشخيص | P/D | Comments from the segment |
| Tue | P30 | **قبل وبعد: نفس الشغل، مرة على إكسيل ومرة على نظام.** | Before/after carousel | FB + LinkedIn | 6 frames, dummy data | — | P/D | 5+ shares |
| Thu | P31 — POV | **إحنا مش أرخص حد. وده مقصود.** | Founder photo + text | FB + LinkedIn | Real photo | — | **F** | Best comment thread of the quarter |
| — | Local | Attend one Port Said business or port-industry gathering | — | Offline | One-pagers, printed | — | F | 3 conversations; 1 follow-up |

### Week 12 — Remove the friction

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P32 | **"مش عارف أشرح اللي عايزه." متقلقش — دي شغلتنا مش شغلتك.** | Single image | FB | Creative | ابعت رسالة واحدة على واتساب | P/D | 3+ DMs |
| Tue | P33 | **كل الأسئلة اللي بتتسألنا: الوقت، السعر، الملكية، الدعم، وبعد التسليم.** | FAQ carousel, 8 frames | FB + website | Real FAQ from DMs | لسه عندك سؤال؟ ابعت | P | 8+ saves |
| Thu | P34 | **الشهر ده اتكلمنا مع `[[INSERT REAL NUMBER — see Portfolio and Case Studies]]` شركة. دي أكتر ٣ مشاكل اتكررت.** | Carousel, 4 frames | FB + LinkedIn | Real, anonymised session notes | احجز جلستك | F | 4+ comments; 2+ requests |
| — | Prep | Meta Pixel event check, conversions API, lead-form fallback built | — | — | See `[[Paid Media Plan]]` | — | P/dev | Gate 1 checklist green |

### Week 13 — Close the quarter, open the next

| Day | Post | Working headline (AR) | Format | Channel | Asset needed | CTA | Owner | Success metric |
|---|---|---|---|---|---|---|---|---|
| Sun | P35 | **٩٠ يوم. دي الحاجات اللي اتعلمناها ونشرناها.** | Carousel recap, 6 frames | FB + LinkedIn | Best assets of the quarter | تابعنا | P/D | 5+ shares |
| Tue | P36 | **فاضل `[[INSERT REAL NUMBER — see Portfolio and Case Studies]]` أماكن لجلسات التشخيص الشهر الجاي.** *(only if capacity is genuinely limited — never manufacture scarcity)* | Single image | FB | Real capacity number | احجز | F | 3+ requests |
| Thu | P37 | **المشروع الجاي هننشره وإحنا بنبنيه، خطوة بخطوة.** | Single image | FB + LinkedIn | Creative | تابع السلسلة | F/P | Sets up Q2 |
| — | **Quarter review** | Full read against `[[Marketing Strategy]]` §7. Go/no-go on paid media | — | — | — | — | F+P | Written decision |

---

## Cross-cutting weekly rhythm (every week, weeks 1–13)

| Cadence | Activity | Owner |
|---|---|---|
| Sunday | 45-min planning; last week's numbers | P + F |
| Monday | Batch-write the week's copy | P |
| Tuesday | Design the week's creatives | D |
| Wednesday | Approval gates + schedule | P → F |
| Daily | Respond to every comment/DM/WhatsApp within SLA | R |
| Post day | Be present for the first 60 minutes | R |
| Daily | Capture one daylight asset to `05-Assets/Daylight/` | All |
| Friday | Founder outreach + referral block | F |

## 90-day scorecard

| Metric | Target (`proposed`) | Actual |
|---|---|---|
| **Qualified Diagnostic Sessions held** (north star) | 4 | |
| Paid Blueprints sold | 1 | |
| Case studies published with a real number | 4 (≥2 with numbers) | |
| Named accounts contacted | 40+ | |
| Website clicks from social | 150/month by month 3 | |
| FB followers | 300 | |
| FB page reviews | 8 | |
| Enquiries older than 24h unanswered | **0** | |

## Related
[[Foundation Brief]] · [[Marketing Strategy]] · [[Content System]] · [[Social Media Playbook]] · [[Content Templates and Hooks]] · [[Paid Media Plan]] · [[Portfolio and Case Studies]] · [[Offer Ladder]] · [[ICP - Ideal Customer Profiles]] · [[Messaging Framework]] · [[Open Questions and Decisions Needed]]
