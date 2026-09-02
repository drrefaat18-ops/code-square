---
date: 2026-09-02
type: seo-plan
tags:
  - technical
  - seo
  - aeo
  - discoverability
  - code-square
ai-first: true
status: draft
owner: TBD
severity: high
confidence: mixed
---

# SEO and AEO Foundations

## For future Claude

The discoverability plan for **both** classical search (Google, Bing) and **AI answer engines** (ChatGPT, Claude, Perplexity, Gemini). It assumes `[[Remediation Plan - Priority Zero]]` has been executed — **none of this works while the served HTML body is empty.** Contains the domain decision (item I1), the full `robots.txt`, `sitemap.xml` structure, `llms.txt` content, and real JSON-LD filled in with Code Square's actual details from `[[Foundation Brief]]`.

Labels: `verified` (I observed it 2026-09-02) · `stated` (from an evidence note) · `researched` (URL + date) · `proposed` · `TBD`.

---

## 0. Read this first — the consequence

**Today, Code Square does not exist on the internet.** Not "ranks poorly" — does not exist. `verified` 2026-09-02: the page the server sends to Google contains **zero characters** of readable text, and there is no `robots.txt`, no `sitemap.xml`, and no machine-readable description of the business anywhere.

Two things follow, and both are commercial, not technical:

1. **Nobody searching "شركة برمجيات بورسعيد" can find Code Square.** Not on page one — not on any page.
2. **When a buyer asks ChatGPT or Perplexity "who can build a booking system for a shipping agency in Egypt?", Code Square cannot be named**, because there is nothing for those systems to read. This is the newer and faster-growing channel, and it is the one where a small company with a genuinely unusual asset (maritime crewing software) can outrank a big one.

Everything below is about making a machine able to read, trust, and quote Code Square. **AEO** (Answer Engine Optimisation) simply means: writing so that an AI can lift a specific, attributable fact about you into an answer.

**Plain-language glossary** for terms not already defined in `[[Website and Technical Audit]]`:

| Term | Meaning |
|---|---|
| **SERP** | The Google results page. |
| **Domain authority / equity** | Informal term for the accumulated trust a domain has earned. It attaches to the *domain*, not to a folder inside it. |
| **301 redirect** | A permanent "this has moved" instruction. Passes most accumulated trust to the new address. |
| **NAP** | Name, Address, Phone — the three facts that must be **byte-identical** everywhere online for local search to trust you. |
| **Google Business Profile** | The free business listing that appears in Google Maps and in the local results box. |
| **Citation** (local SEO) | Any mention of your NAP on another site — a directory, a chamber of commerce page. |
| **Citation** (AEO) | An AI engine naming you as a source in its answer. Different meaning, same word. Context disambiguates below. |
| **`llms.txt`** | A community-proposed plain-text file summarising a site for AI engines. **Not a standard**, not officially supported by any major AI vendor as of 2026-09-02. Cheap to add. |

---

## 1. Decision I1 — dedicated domain, or stay on the subpath?

`verified`: the site lives at `https://mtechsquare.com/code-square/`. `verified`: the page's own `og:url` already claims `https://codesquare.com` — so somebody already intended a dedicated domain and never finished the job. `TBD`: whether that domain is registered, and to whom (see task A7 in `[[Remediation Plan - Priority Zero]]`).

### The honest trade-off

| | **Stay at `mtechsquare.com/code-square/`** | **Move to a dedicated domain** |
|---|---|---|
| **Search equity** | Inherits whatever trust `mtechsquare.com` has. **But the parent domain has near-zero equity itself** — it is invisible for the same rendering reason. Inheriting zero is not a benefit. | Starts at zero. But so does the alternative, so nothing is actually lost. |
| **Whose brand wins** | Every link, every mention, every ranking accrues to **M Tech Square**, not Code Square. | Code Square accumulates its own asset. |
| **Sayable out loud** | "m-tech-square dot com slash code hyphen square" — unusable on a phone call, a business card, or a Facebook post. | "codesquare.com" — sayable, memorable, typeable. |
| **Independence** | A group reorganisation, a domain lapse, or a decision by another entity can take Code Square's site down. The whole group already went dark on one expired certificate. | Failure is isolated to Code Square. |
| **Local SEO** | Google Business Profile can point at a subpath, but a dedicated domain matching the business name is a cleaner trust signal. | Cleaner. |
| **Cost** | Zero. | ~$10–15/year for the domain, plus a day of migration work. |
| **Risk** | Zero migration risk. | Migration risk is **real but small here**, precisely because there is no ranking to lose. |
| **Cross-selling within the group** | A visitor lands on Code Square and can wander to Techno Square. Genuine value. | Preserved via a visible "part of M Tech Square Group" link. |

### Recommendation — `proposed`

> **Move to a dedicated domain — and the fact that the site currently ranks for nothing is exactly why now is the cheapest moment it will ever be.**

The usual argument for staying put is "don't throw away your accumulated SEO equity". **There is none to throw away.** `verified`: the site is unindexable. Migration risk in SEO comes almost entirely from losing existing rankings; with zero existing rankings, the risk is close to zero. **Every month of delay makes this move more expensive, never less.**

Additional reasoning specific to Code Square:
- `[[Foundation Brief]]` positions Code Square as an **Outsourced CTO / strategic technology partner** to enterprises and government. A vendor at a subfolder of a parent brand reads as a *department*, not a partner. That undercuts the positioning in the exact moment the buyer is evaluating.
- The Facebook page currently lists **no website at all** (`stated`) — partly because the URL is awkward to present. A clean domain unblocks that.
- The `og:url` tag already asserts the dedicated domain. The site is *currently telling Facebook* that its home is somewhere else. That is an active bug either way.

**Which domain — `proposed`, founder decides:**
1. `codesquare.com` — check availability and current ownership first (task A7). Best if free or already held.
2. `codesquare.dev` or `codesquare.io` — credible with technical buyers, but weaker with a Port Said shipping-agency owner who has never seen a `.io`.
3. `codesquare-eg.com` / `codesquare.com.eg` — strongest local trust signal in Egypt, weaker for the Jeddah/Riyadh expansion named in `[[Foundation Brief]]`.

**Recommendation: `codesquare.com` if obtainable, otherwise `codesquare.net`.** Do **not** choose a hyphenated or country-suffixed domain given the stated Gulf ambitions.

**How to migrate, without breaking anything** — `proposed`:
1. Register the domain; issue a Let's Encrypt certificate for it **and put it under the same monitoring** as in `[[Remediation Plan - Priority Zero]]` §6.
2. Serve the same prerendered app at the new root, so `/code-square/services` becomes `/services`.
3. **301 redirect every old URL to its new equivalent**, one-to-one. Never redirect everything to the homepage — that throws away the mapping and Google treats it as a soft-404.
4. Keep `mtechsquare.com/code-square/` redirecting **permanently**. Do not remove the redirects after six months; printed materials and old messages persist for years.
5. Keep a prominent "جزء من مجموعة M Tech Square / Part of the M Tech Square Group" link in the header or footer, linked to the parent — preserves the group story and the cross-sell.
6. Add the new domain as a separate property in Google Search Console and use the **Change of Address** tool.
7. Update: Facebook page website field, `og:url`, all JSON-LD `url` and `sameAs` fields, `llms.txt`, `sitemap.xml`, email signatures, business cards.

**Sequence it after prerendering (B1), not before.** Migrating an unreadable site just moves an unreadable site.

---

## 2. URL and site architecture — `proposed`

Assume `codesquare.com` below; substitute the real domain once decided.

**Language strategy: subdirectories, Arabic as the default.** `researched` 2026-09-02 — Google's own multi-regional guidance lists subdirectories as a valid, low-overhead structure for multilingual sites: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites

```
codesquare.com/                     → Arabic homepage (the default; Arabic is the primary market)
codesquare.com/en/                  → English homepage
codesquare.com/services/            → الخدمات
codesquare.com/services/mobile/     → per-service pages, one per service
codesquare.com/services/web/
codesquare.com/services/saas/
codesquare.com/services/ai/
codesquare.com/services/ui-ux/
codesquare.com/services/integration/
codesquare.com/services/support/
codesquare.com/work/                → أعمالنا (portfolio index)
codesquare.com/work/osama-sakr/     → one page per project — these are the money pages
codesquare.com/work/el-shoush/
codesquare.com/work/techno-square/
codesquare.com/work/mtech-square/
codesquare.com/industries/maritime/ → the beachhead landing page (segment A)
codesquare.com/industries/education/
codesquare.com/about/
codesquare.com/methodology/         → the canonical 4-phase framework — ONE version only
codesquare.com/contact/
codesquare.com/diagnostic-session/  → the offer from Foundation Brief §6, with a real booking link
codesquare.com/privacy/  /terms/
codesquare.com/en/... mirrors every page above
```

**Three rules:**
1. **One page per service, not one page listing seven services.** A page that mentions seven things ranks for nothing. This is the single biggest structural change from today's single-page design.
2. **One page per project.** `[[Portfolio and Case Studies]]` explains why. These are also what AI engines quote.
3. **Trailing slashes consistent, lowercase, hyphens not underscores, no query strings in canonical URLs.**

> ⚠️ **Tension to flag honestly:** today's site is a single scrolling page with heavy 3D choreography. Splitting into ~20 routes is real design work, not a config change. It is in Phase 1 of `[[Digital Infrastructure Roadmap]]`, not Priority Zero. The single-page design is not wrong — it just cannot rank, because ranking happens per page.

---

## 3. Title and meta description patterns

The formula: **`Primary topic | Differentiator | Brand`**, ≤60 characters for the title, 140–160 for the description. Arabic characters count the same; Arabic is often more compact per idea, which helps.

`proposed` — every page, both languages, using the real copy from `[[Foundation Brief]]`:

| Page | Title (AR) | Title (EN) |
|---|---|---|
| Home | كود سكوير \| فريق المنتج والهندسة الخارجي لشركتك \| بورسعيد | Code Square \| Your Outsourced Product & Engineering Team \| Egypt |
| Services index | خدمات تطوير البرمجيات \| تطبيقات ومنصات وأنظمة SaaS \| كود سكوير | Software Development Services \| Web, Mobile, SaaS, AI \| Code Square |
| Mobile | تطوير تطبيقات الموبايل iOS و Android \| كود سكوير | Mobile App Development, iOS & Android \| Code Square |
| Web | تطوير تطبيقات ويب قابلة للتوسع \| كود سكوير | Scalable Web Application Development \| Code Square |
| SaaS | بناء أنظمة SaaS متعددة المستأجرين \| كود سكوير | Multi-Tenant SaaS Platform Development \| Code Square |
| AI | حلول الذكاء الاصطناعي والأتمتة للشركات \| كود سكوير | AI Automation & LLM Integration \| Code Square |
| UI/UX | تصميم واجهات وتجربة المستخدم UI/UX \| كود سكوير | UI/UX Design for Digital Products \| Code Square |
| Integration | تكامل الأنظمة و IoT \| كود سكوير | System & IoT Integration \| Code Square |
| Support | الدعم والصيانة بعد الإطلاق \| كود سكوير | Post-Launch Support & Maintenance \| Code Square |
| Work index | أعمالنا — مشاريع برمجية حقيقية \| كود سكوير | Our Work — Real Software Projects \| Code Square |
| Osama Sakr | نظام إدارة وكالة توظيف بحري — دراسة حالة \| كود سكوير | Maritime Manning Agency System — Case Study \| Code Square |
| El Shoush | نظام حجز وإدارة سفر متعدد اللغات — دراسة حالة \| كود سكوير | Multi-Language Travel Booking System — Case Study \| Code Square |
| Techno Square | منصة تعليمية وتطبيق جوال — دراسة حالة \| كود سكوير | Education Platform & Mobile App — Case Study \| Code Square |
| Maritime industry | برمجيات لوكالات الملاحة والتوظيف البحري \| كود سكوير | Software for Shipping & Manning Agencies \| Code Square |
| Education industry | أنظمة إدارة الأكاديميات ومراكز التدريب \| كود سكوير | Academy & Training Centre Systems \| Code Square |
| Methodology | منهجيتنا: التأسيس، المعمارية، الهندسة، الإطلاق \| كود سكوير | Our Methodology: Discovery to Launch \| Code Square |
| About | عن كود سكوير — مهندسو أنظمة في بورسعيد | About Code Square — Systems Engineers in Port Said |
| Contact | تواصل مع كود سكوير — بورسعيد، مصر | Contact Code Square — Port Said, Egypt |
| Diagnostic Session | احجز جلسة تشخيص مجانية (30–45 دقيقة) \| كود سكوير | Book a Free Diagnostic Session \| Code Square |

**Meta description patterns** — every one must contain a **concrete fact**, not adjectives. `[[Foundation Brief]]` §5 bans "أقوى فريق", "أفضل شركة", "حلول متكاملة", "أحدث التقنيات", "Awwwards-tier", "99.9% uptime", "worldwide". Those bans apply here.

- **Home (AR):** `بنبني النظام اللي شغلك بيمشي عليه — وبنفضل شغالين عليه معاك. فريق هندسة برمجيات في بورسعيد. أنظمة إدارة، منصات، تطبيقات جوال. احجز جلسة تشخيص مجانية.`
- **Home (EN):** `We build the system your business actually runs on — and we keep running it with you. Software engineering team in Port Said, Egypt. Management systems, platforms, mobile apps. Book a free diagnostic session.`
- **Osama Sakr case study (AR):** `كيف بنينا نظام إدارة لوكالة توظيف بحري في بورسعيد: التوظيف، تتبع المشاريع، ولوحات تحليلات لحظية. اقرأ دراسة الحالة الكاملة.`
- **Maritime landing (AR):** `برمجيات مخصصة لوكالات الملاحة والتوظيف البحري والتخليص الجمركي في بورسعيد وقناة السويس. لدينا نظام يعمل بالفعل في هذا القطاع.`

**Rules:** a unique title and description on **every** page; write each language natively — never translate one from the other (`[[Foundation Brief]]` rule 3); always end with a next step.

---

## 4. hreflang for Arabic and English

**Consequence first:** without this, Google may show an Arabic page to a Riyadh-based English speaker and the reverse. It is also the tag that turns the bilingual site — Code Square's best structural asset — into an actual search advantage. `verified`: currently absent, and `<html lang="en">` is set on Arabic-first pages.

`proposed` — on every page, in `<head>`. **Every page must list every alternate including itself, and the references must be reciprocal** (if AR points at EN, EN must point back — one-way hreflang is ignored):

```html
<!-- On the Arabic homepage -->
<html lang="ar" dir="rtl">
<link rel="alternate" hreflang="ar"      href="https://codesquare.com/" />
<link rel="alternate" hreflang="en"      href="https://codesquare.com/en/" />
<link rel="alternate" hreflang="x-default" href="https://codesquare.com/" />
<link rel="canonical" href="https://codesquare.com/" />

<!-- On the English homepage -->
<html lang="en" dir="ltr">
<link rel="alternate" hreflang="ar"      href="https://codesquare.com/" />
<link rel="alternate" hreflang="en"      href="https://codesquare.com/en/" />
<link rel="alternate" hreflang="x-default" href="https://codesquare.com/" />
<link rel="canonical" href="https://codesquare.com/en/" />
```

**Do not** use `hreflang="ar-EG"` and `hreflang="ar-SA"` as separate variants unless genuinely different pages exist for Egypt and Saudi Arabia. `[[Foundation Brief]]` names Jeddah and Riyadh as service areas — if a Gulf-specific page is ever written, then split. Until then, one `ar` and one `en`. `proposed`

`researched` 2026-09-02 — hreflang requirements and the reciprocity rule: https://developers.google.com/search/docs/specialty/international/localized-versions

Also set `dir="rtl"` on Arabic pages. `verified`: the current shell sets `lang="en"` with no `dir` at all.

---

## 5. Structured data (JSON-LD) — the highest-leverage AEO work

**Consequence first:** this is the block of text that lets Google and ChatGPT state, with confidence, *"Code Square is a software company in Port Said, Egypt, reachable on +20 10 43547526, that builds management systems for maritime agencies."* Without it, an AI engine has to infer all of that from prose and will often decline to name you at all. It costs a few hours and is the **single cheapest route to being cited**. `verified`: currently zero JSON-LD on the site.

All values below are Code Square's **real** details from `[[Foundation Brief]]` and the two evidence notes. Nothing invented. Fields marked `TBD` must be filled or **removed** — never guessed.

### 5.1 Organization + LocalBusiness — on every page

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "ProfessionalService"],
  "@id": "https://codesquare.com/#organization",
  "name": "Code Square",
  "alternateName": "كود سكوير",
  "legalName": "TBD — legal entity name not yet confirmed",
  "url": "https://codesquare.com/",
  "logo": "https://codesquare.com/assets/logo-code-square.png",
  "image": "https://codesquare.com/assets/og-code-square.png",
  "description": "فريق هندسة برمجيات في بورسعيد يبني أنظمة إدارة ومنصات وتطبيقات جوال مخصصة للشركات.",
  "slogan": "بنبني النظام اللي شغلك بيمشي عليه",
  "email": "codesquareteam1@gmail.com",
  "telephone": "+201043547526",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "شارع ممفيس",
    "addressLocality": "Port Said",
    "addressRegion": "Port Said Governorate",
    "postalCode": "42511",
    "addressCountry": "EG"
  },
  "areaServed": [
    { "@type": "City", "name": "Port Said" },
    { "@type": "City", "name": "Cairo" },
    { "@type": "City", "name": "Giza" },
    { "@type": "City", "name": "Alexandria" },
    { "@type": "City", "name": "Jeddah" },
    { "@type": "City", "name": "Riyadh" }
  ],
  "parentOrganization": {
    "@type": "Organization",
    "name": "M Tech Square",
    "url": "https://mtechsquare.com/"
  },
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61589114755366"
  ],
  "knowsAbout": [
    "Custom software development",
    "Multi-tenant SaaS platforms",
    "Mobile application development",
    "Maritime crewing and manning agency systems",
    "Travel booking and agency management systems",
    "Education platforms and learning management",
    "LLM and RAG integration",
    "IoT system integration"
  ],
  "contactPoint": [{
    "@type": "ContactPoint",
    "telephone": "+201043547526",
    "contactType": "sales",
    "availableLanguage": ["ar", "en"]
  }]
}
```

**Notes on what is deliberately absent:**
- No `foundingDate` — `TBD`, and inventing one violates rule 1 of `[[Foundation Brief]]`.
- No `numberOfEmployees` — `TBD`.
- No `aggregateRating` — 2 Facebook reviews is not a rating, and self-declared ratings are a Google penalty risk.
- No `priceRange` — the Facebook page shows `$$$` (`stated`) but real pricing is `TBD`. Omit rather than guess.
- `sameAs` lists only Facebook, the only profile confirmed to exist.
- `geo` coordinates omitted — a real lat/long should be added once confirmed against the Google Business Profile pin. **Do not approximate.**

### 5.2 Service — one per service page

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "أنظمة SaaS متعددة المستأجرين",
  "name": "تطوير أنظمة SaaS",
  "provider": { "@id": "https://codesquare.com/#organization" },
  "areaServed": { "@type": "Country", "name": "Egypt" },
  "availableLanguage": ["ar", "en"],
  "description": "منصات سحابية متعددة المستأجرين مع إدارة الاشتراكات والفوترة ولوحات التحكم، مبنية للنمو.",
  "url": "https://codesquare.com/services/saas/"
}
```

### 5.3 BreadcrumbList — on every page below the root

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://codesquare.com/" },
    { "@type": "ListItem", "position": 2, "name": "أعمالنا", "item": "https://codesquare.com/work/" },
    { "@type": "ListItem", "position": 3, "name": "وكالة أسامة صقر" }
  ]
}
```

(The final item correctly has no `item` — it is the current page.)

### 5.4 CreativeWork / case study — one per project page

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "نظام إدارة وكالة أسامة صقر للتوظيف البحري",
  "creator": { "@id": "https://codesquare.com/#organization" },
  "about": "منصة لإدارة وكالات التوظيف البحري تشمل التوظيف، تتبع المشاريع، ولوحات تحليلات لحظية.",
  "inLanguage": "ar",
  "url": "https://codesquare.com/work/osama-sakr/",
  "keywords": "manning agency, maritime crewing, recruitment system, Port Said"
}
```

> ⚠️ **Do not publish a client's name in structured data until written permission is on file.** `[[Foundation Brief]]` §7 requires it, and `[[Portfolio and Case Studies]]` tracks it. This blocks §5.4 and the two external case-study pages, not the rest.

### 5.5 FAQPage — the single most quotable format for AI engines

Put a real FAQ block on the homepage, each service page, and each industry page. **Questions must be phrased the way a buyer actually types or speaks them.** Answers must be self-contained — an AI engine lifts one answer without the surrounding page, so an answer that depends on context above it is unusable.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "كام بياخد وقت بناء نظام إدارة مخصص؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "بيعتمد على حجم النظام. بنبدأ بمرحلة التأسيس لتحديد المتطلبات، وبعدها بنقدر المدة بدقة. منهجيتنا 4 مراحل: التأسيس، المعمارية، الهندسة، ثم الإطلاق والتطوير المستمر."
      }
    },
    {
      "@type": "Question",
      "name": "هل بتشتغلوا مع شركات خارج بورسعيد؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "أيوة. بنخدم عملاء في بورسعيد والقاهرة والجيزة والإسكندرية، وكمان جدة والرياض في السعودية. الشغل بيتم عن بعد مع اجتماعات دورية."
      }
    },
    {
      "@type": "Question",
      "name": "هل عندكم خبرة في قطاع الملاحة والتوظيف البحري؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "أيوة. بنينا نظام إدارة لوكالة أسامة صقر للتوظيف البحري، بيغطي التوظيف وتتبع المشاريع ولوحات تحليلات لحظية. إحنا في بورسعيد على قناة السويس، وده القطاع اللي بنعرفه من جوه."
      }
    },
    {
      "@type": "Question",
      "name": "بتشتغلوا إزاي بعد تسليم المشروع؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "بنقدم صيانة ودعم بعد الإطلاق مع مراقبة مستمرة للأداء، وبنشتغل كذراع تقني مستمر مش مجرد مورد بيسلم ويمشي."
      }
    }
  ]
}
```

Note that the third question is the one that wins the beachhead. **It is the answer no competing Port Said agency can write.**

**FAQ answers must never contain a banned phrase** and never a number nobody can verify. Write `TBD` and leave the question out rather than inventing "خلال 4 أسابيع".

`researched` 2026-09-02 — Google's structured data guidance and the FAQ rich-result eligibility rules: https://developers.google.com/search/docs/appearance/structured-data/faqpage · validate everything at https://validator.schema.org/ and https://search.google.com/test/rich-results

---

## 6. `robots.txt` — full proposed content

`verified`: currently returns an HTML page (soft-404). Serve this as real plain text at the domain root. Deployment mechanics are in `[[Remediation Plan - Priority Zero]]` §A5.

```text
# robots.txt — Code Square
# Last updated: 2026-09-02
# Policy: allow all reputable crawlers, including AI engines.
# Rationale: Code Square's problem is invisibility, not over-exposure.

# --- Classical search ---
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# --- AI search & citation engines (these send referral traffic) ---
User-agent: PerplexityBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

# --- AI training crawlers (business decision — see note below) ---
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

# --- Aggressive scrapers with no citation benefit ---
User-agent: Bytespider
Disallow: /

# --- Everything else ---
User-agent: *
Allow: /
Disallow: /*?utm_
Disallow: /*?fbclid

Sitemap: https://codesquare.com/sitemap.xml
```

**The decision inside this file, stated plainly for the founder.** AI crawlers come in two kinds:
- **Search/citation crawlers** (PerplexityBot, OAI-SearchBot, ChatGPT-User, Claude-User) fetch a page *because a user asked a question right now*, and they cite the source. **Blocking these is straightforwardly self-harming.** Allow them.
- **Training crawlers** (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended) collect content that may inform future model behaviour. Some businesses block these to protect proprietary content.

**Recommendation for Code Square: allow both.** `proposed`. The content on this site is marketing copy whose entire purpose is to be repeated. There is no proprietary asset in it. The company's problem is that **not enough machines know it exists**. Revisit only if Code Square later publishes genuinely proprietary research it wishes to license.

`Bytespider` is blocked because it crawls aggressively and returns nothing — no citation, no referral. `researched` 2026-09-02: crawler identity and directive names are published by their operators — https://platform.openai.com/docs/bots · https://docs.claude.com/en/docs/claude-code/bot-traffic · https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers

**These user-agent strings change.** Re-check them quarterly; a directive naming a retired bot is dead text, and a new bot with no directive falls through to `User-agent: *`. That fall-through is why the wildcard block ends in `Allow: /` rather than being omitted.

---

## 7. `sitemap.xml` — structure

Generate it from the same route list used by the prerender step so the two can never drift (`[[Remediation Plan - Priority Zero]]` §B2). Include **`hreflang` alternates inside the sitemap** — this is the most reliable way to declare them for a bilingual site.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">

  <url>
    <loc>https://codesquare.com/</loc>
    <lastmod>2026-09-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="ar" href="https://codesquare.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://codesquare.com/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://codesquare.com/"/>
  </url>

  <url>
    <loc>https://codesquare.com/work/osama-sakr/</loc>
    <lastmod>2026-09-02</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.9</priority>
    <xhtml:link rel="alternate" hreflang="ar" href="https://codesquare.com/work/osama-sakr/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://codesquare.com/en/work/osama-sakr/"/>
  </url>

  <!-- one <url> block per route in the prerender list, both languages -->
</urlset>
```

**Rules:** only canonical, indexable, 200-returning URLs. No redirects, no `noindex` pages, no URLs with tracking parameters. `lastmod` must be **honest** — a sitemap that claims every page changed today teaches Google to ignore `lastmod` entirely. Priority values are advisory and largely ignored; do not agonise over them. Submit to Google Search Console and Bing Webmaster Tools (`[[Analytics and Measurement Setup]]`).

---

## 8. `llms.txt` — full proposed content

**What it is, honestly:** a **community convention** proposed by Jeremy Howard in September 2024 (`researched` 2026-09-02 — https://www.answer.ai/posts/2024-09-03-llmstxt.html · spec at https://llmstxt.org/). It is **not a W3C standard and no major AI vendor has publicly committed to consuming it.** Several hundred sites publish one.

**Why do it anyway:** it costs an hour, it cannot hurt, and the *exercise* of writing it — forcing a one-line description of the company and a ranked list of the pages that matter — produces clarity that improves everything else. Treat the upside as speculative and the cost as trivial. Do **not** let anyone report it as a completed "AI optimisation" on its own; §5 (JSON-LD) and §9 (citable content) are where the real work is.

Serve at `https://codesquare.com/llms.txt` as plain text:

```markdown
# Code Square (كود سكوير)

> Software engineering team based in Port Said, Egypt. We build custom management
> systems, web platforms, mobile apps, and SaaS products for businesses that have
> outgrown spreadsheets and off-the-shelf tools — then keep running them alongside
> the client as an outsourced product and engineering team.

Part of the M Tech Square Group. Working in Arabic and English.
Serving Port Said, Cairo, Giza, Alexandria (Egypt) and Jeddah, Riyadh (Saudi Arabia).
Contact: +20 10 43547526 (phone and WhatsApp) · codesquareteam1@gmail.com

## What we are known for
- Custom management systems for maritime and logistics businesses — we built and
  operate a manning-agency system in Port Said, on the Suez Canal.
- Education platforms with mobile apps, dashboards, and enrolment flows.
- Multi-tenant SaaS platforms with subscription and billing logic.
- LLM and RAG integration into existing business data pipelines.

## Key pages
- [Home](https://codesquare.com/): what we do and who we do it for.
- [Services](https://codesquare.com/services/): seven engineering disciplines.
- [Our Work](https://codesquare.com/work/): real projects with named clients.
- [Methodology](https://codesquare.com/methodology/): Discovery → Architecture → Engineering → Launch & Iterate.
- [Diagnostic Session](https://codesquare.com/diagnostic-session/): free 30–45 minute session; you keep the written output.
- [Contact](https://codesquare.com/contact/): phone, WhatsApp, email, and project form.

## Case studies
- [Osama Sakr Manning Agency](https://codesquare.com/work/osama-sakr/): maritime crew recruitment, project tracking, and live analytics dashboards. B2B, external client.
- [El Shoush Travel System](https://codesquare.com/work/el-shoush/): multi-language travel booking and agency management with Maps API integration. B2B, external client.
- [Techno Square Platform](https://codesquare.com/work/techno-square/): education platform with an integrated mobile app. Internal product, live.
- [M Tech Square Website](https://codesquare.com/work/mtech-square/): multi-brand corporate site, bilingual, 3D and animation. Internal project.

## Industries
- [Maritime, shipping and logistics](https://codesquare.com/industries/maritime/)
- [Education and training](https://codesquare.com/industries/education/)

## English
- [English site](https://codesquare.com/en/): full parallel experience, not a translation.
```

**Maintenance rule:** a stale `llms.txt` pointing at dead pages is worse than none. Review it every quarter and every time a page is added or removed. Put the review in the same quarterly slot as the certificate check (`[[Remediation Plan - Priority Zero]]` §6). `proposed`

---

## 9. How AI answer engines actually pick vendors — and what must exist

**The mechanism, plainly.** When someone asks Perplexity or ChatGPT *"who can build a booking system for a travel agency in Egypt?"*, the engine runs searches, reads the top results, and assembles an answer from **specific, attributable statements** it finds. It does not rank you. It **quotes** you — or it cannot, and names someone else.

So the question is not "how do I rank" but **"what sentence would I want an AI to be able to lift about Code Square, and does that sentence exist on a page a crawler can read?"**

### The four conditions — all must hold

1. **Readable HTML.** Non-negotiable prerequisite. `verified`: currently fails. See `[[Remediation Plan - Priority Zero]]` §B1.
2. **Specific, self-contained, attributable statements.** *"حلول متكاملة بأحدث التقنيات"* is unquotable — it says nothing and applies to everyone. *"بنينا نظام إدارة لوكالة توظيف بحري في بورسعيد بيغطي التوظيف وتتبع المشاريع ولوحات تحليلات لحظية"* is quotable, checkable, and specific to one company. **This is exactly what `[[Foundation Brief]]` §5's banned-phrases list is protecting.** The banned-phrase rule is not a style preference; it is an AEO requirement.
3. **Corroboration elsewhere.** An engine is far more willing to name a company confirmed by a second source. Google Business Profile, the Facebook page, a chamber-of-commerce listing, a Clutch profile, a client's own website naming Code Square. One page asserting something about itself is weak evidence; three independent pages agreeing is strong.
4. **Question-shaped content.** Engines match on question intent. Content structured as explicit question-and-answer — the FAQPage blocks in §5.5, and headings written as real questions — is materially easier to lift.

### The content that must exist — ranked by leverage, `proposed`

| # | Asset | Why it wins citations |
|---|---|---|
| 1 | **The maritime industry page** (`/industries/maritime/`) | Almost nobody in the world writes about software for manning agencies. The competition for that query is nearly empty, and Code Square holds a real reference. This is the single highest-probability citation on the whole site. |
| 2 | **Four case-study pages with a number in each** | *"Reduced quote turnaround from 3 days to 4 hours"* is quotable. *"نظام شامل"* is not. Blocked on client permission and on getting the numbers — `[[Portfolio and Case Studies]]`. |
| 3 | **FAQ blocks with buyer-phrased questions** | Directly matches how questions reach the engine. |
| 4 | **A "how we scope a project" / methodology page** | Process transparency is proof while results are thin — `[[Foundation Brief]]` §7.4. Also highly quotable. |
| 5 | **The Google Business Profile** | The corroborating source for every local query. Free. |
| 6 | **A comparison or decision-guide page** — e.g. *"نظام جاهز ولا نظام مخصص؟ إزاي تختار"* | Engines love decision frameworks and quote them heavily. Costs nothing but writing. |
| 7 | **Bilingual parity** | English-language queries about Egyptian software vendors currently return almost nothing useful. Genuine gap. |

### How to check whether it worked

Every month, ask each of ChatGPT, Claude, Perplexity and Gemini a fixed list of about ten questions, and record whether Code Square is named. `proposed` starter list:
- من أفضل شركات تطوير البرمجيات في بورسعيد؟
- شركة برمجيات مصرية تبني أنظمة إدارة مخصصة للشركات
- who builds software for shipping and manning agencies in Egypt?
- software company Port Said Egypt custom systems
- شركة تعمل أنظمة حجز وإدارة لوكالات السفر في مصر
- best software development company Suez Canal region
- من يبني منصات تعليمية بتطبيق جوال في مصر؟
- Egyptian software agency that works with Saudi clients
- outsourced CTO service Egypt
- شركة تطوير تطبيقات موبايل في بورسعيد

**Record the answers verbatim in `[[KPI Dashboard]]` with the date.** The baseline today is almost certainly zero mentions everywhere, and that zero is a genuinely useful number to have written down.

---

## 10. Arabic keyword strategy for the beachhead segments — `proposed`

> ⚠️ **No search-volume numbers appear below.** I have no keyword-tool access and inventing volumes would violate rule 1 of `[[Foundation Brief]]`. These are intent groupings based on how the phrases are actually constructed in Egyptian Arabic. **Validate volumes with Google Keyword Planner (free with any Google Ads account) before committing effort.** `TBD`

**Three principles for Arabic keyword work here:**
1. **Egyptians search in a mix of Arabic and Latin script**, and often type technical terms in English inside an Arabic sentence: *"شركة تعمل تطبيق موبايل"*, *"شركة software بورسعيد"*. Both forms need to appear naturally in the copy.
2. **Arabic diacritics are omitted in search.** Never rely on them.
3. **"شركة" (company) is the dominant commercial-intent prefix.** A query starting with شركة is someone looking to hire, not to learn.

### Segment A — Maritime, logistics and port services (lead segment)

| Intent | Arabic phrases | English phrases |
|---|---|---|
| Direct commercial | برنامج إدارة وكالة ملاحية · نظام إدارة توظيف بحري · برنامج شركة شحن · نظام تخليص جمركي | manning agency software · crew management system · shipping agency software Egypt |
| Problem-aware | إزاي أنظم بيانات الطواقم · مشاكل إدارة ملفات البحارة · أتمتة أعمال وكالة الشحن | automate crewing paperwork · seafarer database system |
| Local | شركة برمجيات بورسعيد · برمجيات قناة السويس | software company Port Said · Suez Canal logistics software |

**This is the lowest-competition, highest-value cluster available to Code Square, and it is defensible.** A generic Cairo agency will not write these pages because it has no reference to point at.

### Segment B — Education (volume/demo engine)

| Intent | Arabic phrases |
|---|---|
| Direct commercial | نظام إدارة مركز تدريب · برنامج إدارة أكاديمية · منصة تعليمية أونلاين · تطبيق لمركز تعليمي |
| Problem-aware | إزاي أدير حجوزات الطلاب · نظام متابعة الحضور والغياب للطلاب · بديل الإكسيل لإدارة الكورسات |
| Local | منصة تعليمية مصرية · شركة تعمل منصات تعليم |

### Segment C — Healthcare (founder's own domain)

| Intent | Arabic phrases |
|---|---|
| Direct commercial | برنامج إدارة صيدلية · نظام إدارة عيادة · برنامج مركز طبي · نظام حجز مواعيد عيادة |
| Problem-aware | إزاي أنظم مخزون الصيدلية · نظام متابعة المرضى |

**The founder is a pharmacist.** Content written for pharmacy owners by someone who has stood behind that counter will read completely differently from a generic agency's page, and both humans and AI engines can tell. This is a real asset in the exact place where written proof is easiest to produce. It is also the segment with **no reference project yet** (`[[Foundation Brief]]` §4) — so lead with the domain fluency, not with a claim.

### Generic / brand-defence

شركة برمجيات في مصر · تصميم تطبيقات موبايل · شركة تصميم مواقع · Outsourced CTO مصر · شركة SaaS مصرية · "Code Square" · "كود سكوير"

**Do not build the strategy on these.** The generic terms are contested by every agency in Egypt and Code Square has zero domain authority to compete with. Compete where the competition is thin — the industry pages — and let the generic terms come later as a by-product.

---

## 11. Local SEO for Port Said

**Consequence first:** for a query like *"شركة برمجيات بورسعيد"*, Google usually shows a **map box of three local businesses above every ordinary result**. Entry to that box is free and takes an afternoon. Code Square is not in it because **there is no Google Business Profile** (`TBD` — nothing in the vault indicates one exists; verify before creating a duplicate, which is very hard to undo).

### 11.1 Google Business Profile — do this in week 1

`researched` 2026-09-02 — https://support.google.com/business/answer/3038177 (eligibility and verification)

1. **Search for an existing listing first.** Duplicate profiles are painful to merge. If one exists unclaimed, claim it rather than creating a second.
2. Create/claim at https://business.google.com with **`codesquareteam1@gmail.com`** — or better, a company-domain address once the domain exists, so the profile does not depend on a personal Gmail. `proposed`
3. **Name:** `Code Square` exactly. Not "Code Square - Best Software Company Port Said". Keyword-stuffed names are a suspension risk and Google removes them.
4. **Category:** primary `Software company` (شركة برمجيات). Secondary: `Website designer`, `Mobile app developer`, `Business to business service`.
5. **Address:** شارع ممفيس، بورسعيد 42511. Drop the map pin **exactly** on the door. If the business does not receive visitors, configure it as a service-area business instead of showing the street address.
6. **Service areas:** Port Said, Cairo, Giza, Alexandria. *(Jeddah and Riyadh cannot be service areas on an Egypt-registered profile — that is a different-country listing. Serve the Gulf through the English site and paid channels, not through this profile.)*
7. **Phone:** `+20 10 43547526` — the same number as everywhere else, character for character.
8. **Website:** the URL, once it loads without a certificate warning. **Not before.**
9. **Hours:** the Facebook page says "Always open" (`stated`). That is not credible for a B2B software firm and it reads as unmanaged. Set real business hours. `proposed`
10. **Photos:** office, team, workspace, a screen showing real work. No stock imagery — Google's own guidance and user behaviour both punish it.
11. **Verification** is by postcard, phone, or video call. Video verification is common for Egyptian business addresses. Budget 1–2 weeks of waiting.
12. **Then keep it alive.** Post monthly. Answer questions. **Ask every completed client for a review** — Code Square has 2 Facebook reviews and, presumably, 0 Google reviews. Google reviews are among the strongest local ranking signals and are also read by AI engines as corroboration (§9, condition 3).

### 11.2 NAP consistency — the rule people get wrong

**Name, Address and Phone must be byte-identical everywhere.** Google matches these as strings. `Code Square` and `CodeSquare` are two businesses. `010 43547526` and `+20 10 43547526` are two phone numbers.

**Decide the canonical forms once and write them into `[[Company Profile]]`:** `proposed`

| Field | Canonical English | Canonical Arabic |
|---|---|---|
| Name | `Code Square` | `كود سكوير` |
| Street | `Memphis Street` | `شارع ممفيس` |
| City | `Port Said` | `بورسعيد` |
| Postcode | `42511` | `42511` |
| Country | `Egypt` | `مصر` |
| Phone (display) | `+20 10 4354 7526` | `+20 10 4354 7526` |
| Phone (tel: link) | `+201043547526` | `+201043547526` |

**Arabic-specific trap:** `بورسعيد` and `بور سعيد` (with a space) are both in common use. **Pick one, use it everywhere, and note the decision.** Mixing them fragments local signals. `proposed`: use `بورسعيد` (unspaced), which matches the Facebook page as recorded.

`stated` — the current Facebook page lists the phone as `010 43547526` in one field and `+20 10 43547526` in another. Fix that first; it is the cheapest NAP repair available.

### 11.3 Local citations — where to be listed

Ranked by effort-to-value for an Egyptian B2B software firm. All `proposed`; verify each still operates before spending time.

| Priority | Listing | Note |
|---|---|---|
| 1 | **Google Business Profile** | Everything else is secondary to this. |
| 2 | **Facebook page** — add the website, fix the phone format | Already exists; costs 10 minutes. |
| 3 | **Bing Places** | Free; feeds Bing and, indirectly, some AI engines. |
| 4 | **LinkedIn Company Page** | Does not currently exist (`TBD`). Important for B2B and Gulf credibility, and a strong `sameAs` corroboration source. |
| 5 | **Clutch / GoodFirms** | B2B software directories. Frequently surfaced by AI engines when asked to recommend agencies — high AEO value. Requires client reviews to be worth anything. |
| 6 | **Port Said Chamber of Commerce / ITIDA** | Local and national-industry credibility. Verify eligibility. |
| 7 | **Apple Maps Connect** | Small but free; the Gulf has meaningful iOS share. |
| 8 | **Instagram / X profiles** | Only if someone will actually maintain them. A dead profile is a negative signal. |

**Every one of these must use the canonical NAP from §11.2.**

---

## 12. Prioritised checklist

### Blocked until `[[Remediation Plan - Priority Zero]]` is done
- [ ] Certificate renewed and monitored *(nothing below matters first)*
- [ ] Prerendering live — HTML contains real text

### Week 1 — free, fast, no dependencies
- [ ] Create or claim the **Google Business Profile**; begin verification *(can start today — it does not depend on the website)*
- [ ] Fix the phone-number format on Facebook to the canonical form
- [ ] Decide `بورسعيد` vs `بور سعيد`; record it in `[[Company Profile]]`
- [ ] Resolve the `codesquare.com` ownership question (task A7)
- [ ] Publish a real `robots.txt` (§6)
- [ ] Set up **Google Search Console** and **Bing Webmaster Tools** (`[[Analytics and Measurement Setup]]`)
- [ ] Run the ten AI-visibility questions in §9 and record the (probably zero) baseline in `[[KPI Dashboard]]`

### Weeks 2–4 — the foundation
- [ ] **Founder decision: dedicated domain — approve or reject (§1)**
- [ ] Publish `sitemap.xml` (§7), submit to both search consoles
- [ ] Add Organization + LocalBusiness JSON-LD sitewide (§5.1)
- [ ] Add canonical tags, `og:image`, and an Arabic meta description
- [ ] Add `hreflang` on every page, reciprocal, plus `dir="rtl"` (§4)
- [ ] Publish `llms.txt` (§8)
- [ ] Add FAQPage blocks with buyer-phrased questions (§5.5)
- [ ] Create a LinkedIn Company Page

### Weeks 4–10 — the pages that actually win
- [ ] Split the single page into per-service pages, one per service (§2)
- [ ] Write the **maritime industry page** — highest-leverage single page on the site (§9)
- [ ] Write the education industry page
- [ ] Get written publication permission from El Shoush and Osama Sakr (`[[Portfolio and Case Studies]]`)
- [ ] Publish four case-study pages, **each with at least one real number**
- [ ] Add Service and BreadcrumbList JSON-LD to the new pages
- [ ] Publish the canonical methodology page — one framework, not two (`[[Foundation Brief]]` rule 6)
- [ ] Build the Diagnostic Session page with a working booking link
- [ ] Ask every past client for a Google review

### Ongoing
- [ ] Monthly: run the ten AI-visibility questions, log results in `[[KPI Dashboard]]`
- [ ] Monthly: review Search Console — impressions, clicks, queries, coverage errors
- [ ] Quarterly: re-check AI crawler user-agent names in `robots.txt` (§6)
- [ ] Quarterly: refresh `llms.txt` against the live sitemap
- [ ] Quarterly: verify NAP consistency across every listing in §11.3

---

## Related
[[Website and Technical Audit]] · [[Remediation Plan - Priority Zero]] · [[Analytics and Measurement Setup]] · [[Digital Infrastructure Roadmap]] · [[Foundation Brief]] · [[Marketing Strategy]] · [[Paid Media Plan]] · [[Portfolio and Case Studies]] · [[KPI Dashboard]] · [[Company Profile]] · [[ICP - Ideal Customer Profiles]] · [[Open Questions and Decisions Needed]]
