---
date: 2026-09-02
type: source-evidence
tags:
  - source
  - website
  - code-square
  - technical-audit
ai-first: true
source: "https://mtechsquare.com/code-square/"
captured: 2026-09-02
confidence: stated
---

# Website Evidence — mtechsquare.com/code-square

## For future Claude

The **second and more important** evidence file. Code Square has a real, well-written website living under the parent group's domain — and it says something completely different from the Facebook page. This note records the site's content verbatim plus a technical audit. Extracted 2026-09-02 by pulling the Angular JS bundles directly (the served HTML is an empty shell). Immutable: do not edit with strategy. The gap between this note and `[[2026-09-02 - Facebook Page Evidence]]` is the single most important finding in the vault.

---

## 🔴 Critical technical findings (fix before any marketing spend)

| # | Finding | Impact | Severity |
|---|---|---|---|
| 1 | **TLS certificate is EXPIRED** on `mtechsquare.com` (`SEC_E_CERT_EXPIRED`) | Every visitor gets a full-page browser security warning before seeing anything. A company selling digital trust is serving an untrusted site. Ad traffic sent here is money burned. | 🔴 Blocker |
| 2 | **Angular client-side rendering, no SSR / no prerender** | The served HTML is an empty shell — `<body>` contains zero text. Google, Bing, and every AI engine (ChatGPT, Perplexity, Claude) see a blank page. The entire site is invisible to search and to AI citation. | 🔴 Blocker |
| 3 | **No `sitemap.xml`** (404) | Nothing to crawl even if rendering were fixed. | 🟡 High |
| 4 | **No `robots.txt`** (404) | No crawler guidance, no `llms.txt` for AI engines. | 🟡 High |
| 5 | **No page-level meta** for `/code-square/` | It inherits the group's `<title>` "M Tech Square Group — Beyond Squares" and the group description. A share or search result never says "Code Square". | 🟡 High |
| 6 | **Spline 3D viewer loaded from `unpkg.com`** + Three.js + GSAP + Rapier physics + Skia/CanvasKit | Very heavy payload (~7.5 MB of JS chunks). Likely poor mobile performance on Egyptian 3G/4G — the exact audience. Third-party CDN is a single point of failure. | 🟡 High |
| 7 | **Site lives at `/code-square/` under the parent domain** | No `codesquare.*` domain. Weakens brand recall, makes the Facebook CTA awkward, and every ounce of SEO equity accrues to the parent. | 🟡 High |
| 8 | **No phone number or WhatsApp on the site** | Facebook has the phone; the site has only a form + email. The two channels do not reinforce each other. | 🟡 Medium |

**Stack detected:** Angular (webpack, lazy chunks) · GSAP + ScrollTrigger + ScrollSmoother · Three.js · Spline (`@splinetool/viewer@1.0.94`) · Rapier physics · Skia/CanvasKit · MessagePack.
**Fonts:** Playfair Display (display), Cormorant Garamond, Syne, **Tajawal** (Arabic).

---

## Brand tokens (verbatim from the compiled CSS — authoritative)

```css
--navy:            #001F3F   /* primary ground, also <meta theme-color> */
--navy-dark:       #0A0F1F
--navy-deep:       #050a14
--gold:            #D5B182   /* group accent */
--gold-bright:     #E8C9A0
--white:           #FFFFFF
--text-muted:      rgba(255,255,255,.55)

/* per-entity accents */
--code-accent:     #A855F7   /* ← CODE SQUARE purple */
--techno-accent:   #FDD017   /* Techno Square yellow */
--online-accent:   #17A2B8   /* Online Techno Square teal */
--msquare-accent:  #1E40AF   /* M Square blue */
--digital-accent:  #00A3B1   /* Digital Square teal */

--glass-bg:     rgba(255,255,255,.03)
--glass-border: rgba(213,177,130,.2)
--neon-glow:    0 0 15px rgba(213,177,130,.3)

--font-sans:   "Playfair Display", serif
--font-arabic: "Tajawal", sans-serif
```

**Note the conflict:** the website's Code Square accent is `#A855F7` on a `#001F3F` navy ground with **gold** group furniture. The Facebook creatives use a violet-on-near-black palette with **no gold at all**. These are two different brands wearing the same name. See `[[Visual Identity]]`.

---

## Site content — verbatim

### Navigation
الرئيسية · خدماتنا · أعمالنا · المشاريع · اتصل بنا
(Home · Services · Our Work · Projects · Contact)

### Hero
- **EN:** "We turn complex ideas into effortless digital experiences" / "Engineering Effortless Digital Experiences"
- **AR:** نحن مهندسو أنظمة نبني حلولاً رقمية فائقة الجودة تدفع حدود الممكن وتُشكّل مستقبل أعمالك.
- **CTA:** ابدأ رحلة الابتكار

### Vision & Mission (verbatim — this is the real written identity)
- **الرؤية:** أن نكون الشريك التكنولوجي الموثوق الذي يحول الأفكار إلى حلول رقمية قوية، تساعد الشركات على النمو بشكل أسرع وأكثر ذكاءً وبدون حدود.
- **الرسالة:** تمكين الشركات الطموحة من خلال حلول رقمية ذكية وقابلة للتوسع ومصممة خصيصًا لاحتياجاتها، مع تقديم دعم مستمر والعمل كشريك نجاح طويل الأمد.
- **النواة الاستراتيجية (Strategic Core):** نحن لا نبني برمجيات فحسب... بل نبدأ بفهم عميق لطبيعة عمل العميل واحتياجاته، ثم نحول الأفكار إلى حلول رقمية فعالة وقابلة للنمو.
- **Egyptian-dialect line:** إحنا مش بس بنبني برامج… إحنا بنبني مشروعك رقميًا

### Philosophy — فلسفتنا (three statements, verbatim)
| AR | EN |
|---|---|
| لا نطارد الصيحات العابرة؛ بل نبني أسساً تدوم طويلاً. | We don't chase trends. We build fundamentals that last. |
| لسنا مجرد مبرمجين؛ نحن مهندسو أنظمة برمجية قابلة للتوسع. | We don't just code. We architect for scale. |
| لسنا مجرد مزودي خدمة؛ نحن شريكك التكنولوجي الاستراتيجي. | We're not just service providers. We're your technology partner. |

Preamble: كل مشروع هو حالة فريدة، وكل شركة تمتلك هوية مختلفة. لهذا السبب نبدأ بفهم عميق لاحتياجاتك بدلاً من القوالب الجاهزة. نحلل متطلباتك، ونفهم أهدافك، ونُهندس حلولاً تنمو مع نمو أعمالك.

### Methodology — المنهجية (4 phases)
| # | AR | EN | Description (AR verbatim) |
|---|---|---|---|
| 1 | التأسيس | Discovery | استكشاف استراتيجي لفهم الرؤية، الأهداف، ورسم خارطة الطريق للمتطلبات التقنية. |
| 2 | المعمارية | Architecture | تصميم مخططات هيكلية متينة مصممة للتوسع والأداء المثالي تحت أقصى ضغط. |
| 3 | الهندسة | Engineering | بناء المشاريع بدقة هندسية، مع الاستفادة من أحدث أطر العمل وأفضل الممارسات البرمجية العالمية. |
| 4 | الإطلاق والتطوير | Launch & Iterate | خطوط إمداد انسيابية للإطلاق متبوعة بحلقات تحسين وتطوير مستمرة. |

> This is a **different** framework from the 5-stage model published on Facebook (Discovery → User Analysis → UX/UI → Development → Testing & Launch). Two published methodologies, neither cross-referenced. See `[[Open Questions and Decisions Needed]]`.

### Services — تخصصاتنا الهندسية ("Architected for scale and performance")

| Service | AR description (verbatim) | EN detail / tech tags |
|---|---|---|
| تطبيقات الجوال (Mobile) | تطبيقات أصلية (Native) وعابرة للمنصات بنظامي Android و iOS نُهندسها لتعمل بسرعة فائقة وأداء انسيابي. | Mobile Applications |
| تطوير الويب (Web) | بناء تطبيقات ويب متطورة وقابلة للتوسع باستخدام أحدث الأطر البرمجية، من النماذج الأولية إلى الأنظمة المؤسسية. | "From MVPs to robust enterprise portals." |
| أنظمة SaaS المخصصة | منصات سحابية متعددة المستأجرين مصممة للنمو السريع مع دمج أنظمة الفوترة وإدارة المستخدمين المتقدمة. | Multi-tenant Logic · **Stripe Integration** |
| حلول الذكاء الاصطناعي (AI) | أنظمة أتمتة ذكية لرفع كفاءة سير العمل. ندمج نماذج LLM المتطورة مباشرة في قنوات البيانات الخاصة بك. | Machine Learning · **RAG Pipelines** · LLM integration |
| تصميم الـ UI/UX | واجهات تجمع بين الجمالية الفائقة وسهولة الاستخدام المطلقة، تهدف للحفاظ على كثافة تفاعل المستخدمين. | Figma Prototyping · User Research · "Awwwards-tier" |
| تكامل الأنظمة (IoT) | ربط مصفوفات الـ IoT والأنظمة الذكية، وتوحيد نقاط النهاية في لوحات تحكم مركزية لمراقبة الأداء لحظياً. | IoT protocols · observability dashboards |
| الدعم والصيانة | صيانة ما بعد الإطلاق لضمان استمرارية الأداء الفائق والسرعة الرقمية القصوى مع مراقبة السيرفرات عالمياً. | **SLA Guarantees** · global server monitoring |

### Why Code Square — لماذا كود سكوير؟ (8 differentiators, verbatim)
1. **فهم عميق للأعمال** — نحلل قواعد عملك بدقة هندسية قبل كتابة أول سطر من الكود.
2. **حلول مخصصة وقابلة للتوسع** — لا قوالب جاهزة هنا. كل حل يُبنى خصيصاً ليتحمل الكثافة المرورية المتزايدة.
3. **الالتزام بالمواعيد** — نستخدم منهجية Agile صارمة تضمن مواءمة التطوير مع جدولك الزمني للسوق.
4. **دعم فني مستمر** — صيانة ما بعد الإطلاق تضمن استقرار النظام والحفاظ على الزخم الرقمي.
5. **تفكير استراتيجي** — نعمل ضمن أطر عمل تفاعلية تهدف للابتكار في كافة القطاعات الرقمية.
6. **تصميم UI/UX عالمي** — تصميمات تضاهي معايير Awwwards العالمية لضمان ولاء المستخدمين.
7. **عقلية الشراكة** — تكامل عميق مع فريقك للعمل كذراع تقني استراتيجي **(Outsourced CTO)**.
8. **تنفيذ فائق الكفاءة** — خطوط تفاعل CI/CD انسيابية تتيح دورات بناء واختبار سريعة للغاية.

---

## 🟢 THE PORTFOLIO — four real projects (never mentioned on Facebook)

Status labels used on the site: `قيد التنفيذ` (in progress) · `تحديثات جارية` (ongoing updates) · `مشروع داخلي` (internal project) · `منتج خاص` (own product) · `نظام SaaS` · `نظام B2B` · `تطبيق ويب B2B` · **`مشروع حكومي B2G`**

| # | Project | Type | Description (verbatim) |
|---|---|---|---|
| 1 | **موقع M Tech Square** / M Tech Square Website | Internal project | موقع مؤسسي يستعرض النظام البيئي التكنولوجي للمجموعة برسوم متحركة سينمائية. — "Corporate website showcasing M Tech Square Group's technology ecosystem with cinematic animations." |
| 2 | **منصة Techno Square** / Techno Square Platform | Internal product | منصة تعليمية مع تطبيق جوال متكامل لبرامج التعلم عبر الإنترنت الخاصة بتكنو سكوير. — "Educational platform with integrated mobile app." |
| 3 | **نظام El Shoush للسفر** / El Shoush Travel System | **External client, B2B** | نظام شامل لحجز وإدارة السفر للوكالات، يدعم لغات متعددة وتكامل الخرائط (Maps API). |
| 4 | **وكالة Osama Sakr** / Osama Sakr Manning Agency | **External client, B2B** | منصة لإدارة الوكالات تشمل التوظيف، تتبع المشاريع، ولوحات تحليلات لحظية لمراقبة الأداء. — "Agency management platform for recruitment, tracking, and team collaboration." |

**A `مشروع حكومي B2G` (government project) label exists in the code** but no B2G project is described in the extracted content — either unreleased, unlabelled, or the tag is unused. **Verify with the founder.**

> **"Manning agency"** = maritime crew recruitment. Port Said is a Suez Canal port city. Project #4 is a **maritime/logistics vertical asset** in the exact city Code Square operates in. This was not visible anywhere on Facebook.

---

## Contact section

- Heading: **لنقم ببناء شيء استثنائي معاً.** / "Let's build something extraordinary."
- Sub: سواء كنت بحاجة إلى تطبيق ويب عالي الأداء، أو تجربة جوال أصلية (Native)، أو نظام مؤسسي معقد؛ نحن جاهزون لهندسته.
- **Form fields:** اسم المشروع · بريدك الإلكتروني · ميزانية المشروع (dropdown: "اختر تقديراً للميزانية…") · نوع المشروع (تطبيق ويب / تطبيق جوال / تصميم UI/UX / نظام مخصص) · تفاصيل الرسالة → **إرسال الطلب**
- Success state: **تم استلام طلبك بنجاح** — شكراً لك! سيقوم فريقنا التقني بمراجعة التفاصيل والتواصل معك خلال **24 ساعة**.
- "أو تواصل معنا عبر البريد المباشر:" — the email address itself is injected at runtime and was not in the bundles. **Confirm which address the form and this link point to.**
- ⚠️ The form promises a **24-hour response SLA**. Nothing in the vault yet says who owns that inbox or how it is tracked. See `[[Lead Intake and CRM]]`.
- ⚠️ Budget dropdown options were not in the extracted bundles — **the actual budget bands are unknown and must be confirmed.**

### Footer
- نُهندس تجارب رقمية انسيابية وفائقة الجودة. نصمم ونبني ونقدم حلولاً برمجية متميزة للشركات المتنامية حول العالم. / "Engineering effortless digital experiences. We design, architect, and deliver premium software solutions for growing enterprises worldwide."
- القدرات: هندسة الويب (Web Engineering) · معمارية الجوال (Mobile Architecture) · ذكاء اصطناعي و SaaS (AI & SaaS Logic) · منهجيتنا
- Legal links present: **سياسة الخصوصية** (Privacy Policy) · **شروط الخدمة** (Terms of Service) — ⚠️ confirm these pages actually have content; the group title/description is all that renders.

---

## The core contradiction (the finding that drives the whole vault)

| | **Website says** | **Facebook says** |
|---|---|---|
| Who they are | "مهندسو أنظمة" — systems engineers, **Outsourced CTO**, strategic technology partner | "شريكك التكنولوجي" — a friendly agency that builds websites and apps |
| Audience | "growing enterprises worldwide", B2B, B2G | anyone with an idea |
| Proof | **4 named projects**, 2 with external clients, B2B/B2G/SaaS labels | one process case study, zero named clients |
| Depth | RAG pipelines, LLM integration, multi-tenant SaaS, Stripe, IoT observability, CI/CD, SLA | "what is the difference between UI and UX" |
| Language | Full AR + EN | Arabic only |
| Tone | Premium, technical, confident | Educational, beginner-level |

**The website is 10× stronger than the Facebook page and nobody can see it** — because the cert is expired, nothing is server-rendered, and the Facebook page never links to it. The founder's instinct that there is "no identity" is half-right: **an identity was written, then buried.** The job is not to invent one from scratch; it is to surface, sharpen, and align the one that already exists.

## Related
[[2026-09-02 - Facebook Page Evidence]] · [[Foundation Brief]] · [[Company Profile]] · [[Website and Technical Audit]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]]
