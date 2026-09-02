---
date: 2026-09-02
type: technical-audit
tags:
  - technical
  - website
  - seo
  - audit
  - code-square
ai-first: true
status: draft
owner: TBD
severity: blocker
confidence: mixed
---

# Website and Technical Audit

## For future Claude

This is the **findings register** for `mtechsquare.com/code-square/`. It builds on the immutable evidence note `[[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]` and adds a **live re-test performed 2026-09-02 at 12:46 UTC** by direct HTTP request. Where the re-test *changed* a finding from the original audit, that is called out explicitly — do not silently overwrite. Fixes live in `[[Remediation Plan - Priority Zero]]`; discoverability strategy lives in `[[SEO and AEO Foundations]]`.

Every row is labelled `verified` (I observed it), `stated` (from an evidence note or the founder), `researched` (external source + URL + date), `proposed` (my recommendation), or `NEEDS VERIFICATION`.

---

## The one-paragraph version, for the founder

Code Square's website is the strongest asset the company owns — the writing, the bilingual structure and the design craft are genuinely good. **Nobody can reach it.** The security certificate expired on **31 August 2026**, so every single visitor now sees a full-screen red browser warning that says the site is unsafe before they see a single word. And because of the way the site is built, Google and ChatGPT see a completely **blank page** — the site is, to a search engine, empty. These two problems are not "SEO improvements". They are the difference between having a website and not having one. Everything else in this note is secondary.

---

## Glossary — every technical term used below, in plain language

| Term | What it actually means |
|---|---|
| **TLS / SSL certificate** | The thing that makes the browser show a padlock instead of a scary full-page warning. It is a file that expires on a fixed date and must be renewed, like a car licence. |
| **Let's Encrypt** | A free, automated provider of those certificates. Free forever; renews itself if configured correctly. |
| **Server-side rendering (SSR)** | The web server sends a finished, readable page. The opposite is *client-side rendering*, where the server sends an empty shell and the visitor's browser builds the page using JavaScript. Google and AI engines usually read the shell. |
| **Prerendering** | A cheaper version of SSR: at build time you generate a finished HTML file for each page and serve that. Same benefit, far less complexity. |
| **Crawler / bot** | The automated program Google, Bing, ChatGPT and Perplexity send to read your site. |
| **`robots.txt`** | A plain text file at the root of a site telling crawlers what they may read. |
| **`sitemap.xml`** | A list of every page on the site, given to search engines so they do not have to guess. |
| **`llms.txt`** | A newer, community-proposed file (not an official standard) that gives AI answer engines a clean summary of the site. See `[[SEO and AEO Foundations]]`. |
| **Structured data / JSON-LD** | A small block of machine-readable facts (address, phone, services) embedded in a page so Google and AI engines can state them confidently. |
| **`<title>` and meta description** | The blue headline and grey summary line you see in a Google result, and the text that appears when a link is pasted into WhatsApp or Facebook. |
| **Canonical URL** | A tag saying "this is the one true address of this page", preventing search engines from treating duplicates as separate pages. |
| **hreflang** | A tag telling Google "this page has an Arabic version and an English version", so the right one is shown to the right person. |
| **gzip / brotli compression** | Squeezing files before sending them over the network. Typically cuts transfer size by 70–80%. Free, one line of server config. |
| **CDN** | A network that serves files from a server near the visitor. `unpkg.com` is a third-party CDN the site currently depends on. |
| **Soft 404** | The server says "200 OK, here is your page" for a page that does not exist. Confuses crawlers badly. |
| **HSTS** | A header that tells browsers "always use the secure version of this site". |

---

## 1. Live re-test — what I actually observed, 2026-09-02 12:46 UTC

`verified`

| Test | Result |
|---|---|
| `curl https://mtechsquare.com/code-square/` (normal, certificate validated) | **FAILS** — `SEC_E_CERT_EXPIRED`. Connection refused by the client. |
| Certificate details (`openssl s_client`) | Subject `CN=mtechsquare.com` · Issuer **Let's Encrypt (CN=YE1)** · Valid **2026-06-02 → 2026-08-31 18:57 UTC**. **Expired 2 days ago.** |
| Same request with certificate checking disabled | `HTTP 200`, 30,405 bytes of HTML |
| Server software | `nginx/1.24.0 (Ubuntu)` |
| `http://` → `https://` redirect | `301` present — correct |
| Rendered text inside `<body>` of the served HTML | **0 characters.** Confirmed empty shell (`<app-root>` with no content, no Angular hydration markers). |
| `/robots.txt` | Returns **HTTP 200 with the Angular HTML page**, not a robots file. |
| `/sitemap.xml` | Same — HTML, not a sitemap. |
| `/llms.txt` | Same — HTML. |
| `/nonexistent-abc123.txt` | Same. → the server is a **catch-all soft-404**. |
| `<title>` on `/code-square/` | **`Code Square — Engineering Effortless Digital Experiences`** ← this is *better* than the original audit recorded. |
| Meta description | Present, English only. |
| OpenGraph tags | `og:title`, `og:description`, `og:type` present. **`og:url` = `https://codesquare.com`** — a domain Code Square does not appear to control. |
| `og:image` | **Absent.** |
| Canonical tag | **Absent.** |
| `hreflang` tags | **Absent.** |
| JSON-LD structured data | **Absent** (zero `application/ld+json` blocks). |
| Scripts loaded from the HTML | `unpkg.com/@splinetool/viewer@1.0.94`, `polyfills.js` (44 KB), `main.js` (10 KB) + lazy chunks fetched at runtime |
| gzip / brotli compression | **Not enabled.** Requested `Accept-Encoding: gzip, br`; server returned no `Content-Encoding` header. |
| Static asset caching | `Cache-Control: public, max-age=31536000, immutable` — correctly configured |
| HTML caching | `no-cache, no-store, must-revalidate` — correct for a single-page app shell |
| Security headers (HSTS, CSP, X-Frame-Options) | **Absent.** |
| `Last-Modified` on the shell | 2026-07-02 — the site has not been redeployed in two months. |

### Two corrections to the original evidence note

1. **Finding #5 in the evidence note is now out of date.** `/code-square/` **does** have its own `<title>`, meta description and OpenGraph tags. It no longer inherits the group's. Credit where due — someone fixed this. `verified`
2. **Findings #3 and #4 (`sitemap.xml` 404, `robots.txt` 404) are worse than recorded, not better.** They do not 404; they return `HTTP 200` with an HTML page. A crawler asking for permission rules receives a web page instead. That is a *soft 404*, which search engines handle less predictably than an honest 404. `verified`

**`NEEDS VERIFICATION`:** the ~7.5 MB JS payload figure from the original audit. I confirmed the entry-point files (44 KB + 10 KB + 34 KB CSS, all uncompressed) but the lazy-loaded 3D chunks are fetched by the app at runtime and I did not execute JavaScript. The total is certainly large — Three.js, Rapier physics and Skia/CanvasKit are each megabyte-class libraries — but treat 7.5 MB as unmeasured until someone runs a Lighthouse or WebPageTest report. See `[[Remediation Plan - Priority Zero]]`.

---

## 2. Findings register

Severity: 🔴 **Blocker** (site is effectively non-functional) · 🟠 **High** (materially costs enquiries) · 🟡 **Medium** · 🟢 **Low**.
Effort: **XS** <1h · **S** 1–4h · **M** 1–2 days · **L** 3–10 days · **XL** >2 weeks.
Priority `P0` = this week · `P1` = weeks 1–2 · `P2` = weeks 2–6 · `P3` = later.

### Security and trust

| ID | Finding | Evidence (what was observed) | Business impact, in plain terms | Sev | Effort | Pri |
|---|---|---|---|---|---|---|
| **SEC-01** | **TLS certificate expired 2026-08-31** | `openssl` shows Let's Encrypt cert `notAfter = Aug 31 2026 18:57 UTC`. Plain `curl` refuses the connection. `verified` | Every visitor — from Facebook, from a business card, from a WhatsApp link — hits a full-screen red "Your connection is not private" warning. Most people leave. A company that sells digital trust is publishing an *officially untrusted* site. Any money spent on ads today lands here. | 🔴 | XS | P0 |
| **SEC-02** | **No automated renewal, or it silently failed** | The certificate is Let's Encrypt (90-day lifetime) and expired anyway. Either certbot was never installed, or its renewal timer is broken, or nginx was never reloaded after renewal. `verified` (that it expired) / `NEEDS VERIFICATION` (which of the three) | This will happen again in 90 days and nobody will know until a client mentions it. | 🔴 | S | P0 |
| **SEC-03** | **No certificate-expiry monitoring or uptime alerting** | Nothing in the vault names a monitor; the outage went unnoticed for at least 2 days. `stated` | The company found out about its own outage from a strategy audit. That is the real failure — not the certificate. | 🟠 | S | P0 |
| **SEC-04** | No HSTS, CSP, X-Frame-Options or Referrer-Policy headers | Response headers show none. `verified` | Low direct commercial impact today, but any enterprise or government prospect who runs a security scan before signing will see a low grade. For a company selling **B2G** work (a `مشروع حكومي B2G` label exists in the code), this is a credibility item. | 🟡 | S | P2 |

### Crawlability and discoverability

| ID | Finding | Evidence | Business impact | Sev | Effort | Pri |
|---|---|---|---|---|---|---|
| **CRAWL-01** | **Client-side rendering only; served HTML body contains zero text** | Stripped the served HTML: **0 characters** of visible text. `<app-root>` empty, no hydration attributes. `verified` | To Google, Bing, ChatGPT, Claude and Perplexity, this page is **blank**. The vision, the philosophy statements, the four projects, the seven services — none of it exists as far as any search or AI system is concerned. The company cannot be found, cited, or recommended. | 🔴 | L | P0 |
| **CRAWL-02** | **`robots.txt` returns an HTML page, not a robots file** | `GET /robots.txt` → `200` + Angular shell. `verified` | Crawlers get gibberish where the rules should be. AI crawlers (GPTBot, ClaudeBot, PerplexityBot) have no instructions. | 🟠 | XS | P0 |
| **CRAWL-03** | **No `sitemap.xml`** (soft-404s to HTML) | `GET /sitemap.xml` → `200` + HTML. `verified` | Search engines have no list of pages to fetch. Combined with CRAWL-01 there is literally nothing to index. | 🟠 | S | P1 |
| **CRAWL-04** | **Server is a catch-all soft-404** | `/nonexistent-abc123.txt` → `200` + HTML. `verified` | Any mistyped or dead URL looks like a real page. Search engines waste crawl effort and may flag the site as low quality. | 🟡 | S | P1 |
| **CRAWL-05** | **No canonical tag** | Absent from `<head>`. `verified` | `/code-square`, `/code-square/`, and any tracking-parameter version can be treated as separate duplicate pages, splitting whatever authority exists. | 🟡 | XS | P1 |
| **CRAWL-06** | **No `hreflang`; `<html lang="en">` on an Arabic-first page** | `verified` | The site is genuinely bilingual — its best structural asset — and Google is told none of it. An Arabic searcher in Port Said and an English searcher in Riyadh get the same undifferentiated signal. | 🟠 | M | P1 |
| **CRAWL-07** | **No structured data (JSON-LD) anywhere** | Zero `application/ld+json`. `verified` | Google and AI engines have no machine-readable statement that Code Square is a business in Port Said with this phone number and these services. This is the single cheapest way to become *quotable* by an AI engine. See `[[SEO and AEO Foundations]]`. | 🟠 | M | P1 |
| **CRAWL-08** | **No `llms.txt`** | Soft-404. `verified` | AI answer engines have no curated summary to read. Emerging convention, not a standard — cheap to add, meaningful upside. | 🟡 | S | P1 |
| **CRAWL-09** | **`og:url` points to `https://codesquare.com`** — a domain that does not serve this site | `verified` | Every Facebook and WhatsApp share resolves its canonical identity to a domain Code Square does not appear to own. If someone else registers it, Code Square's own shares point at a stranger. **Check immediately whether this domain is owned.** | 🟠 | XS | P0 |
| **CRAWL-10** | **No `og:image`** | `verified` | Links shared to Facebook and WhatsApp render as a bare grey box with no picture. On a phone feed this is the difference between a click and a scroll-past. This is the channel Code Square actually uses. | 🟠 | XS | P1 |
| **CRAWL-11** | **No dedicated domain — the site lives at `/code-square/` under the parent** | `stated` + `verified` | Every ounce of search authority accrues to `mtechsquare.com`. The brand cannot be spoken aloud ("go to m-tech-square-dot-com-slash-code-square"). Decision analysed in `[[SEO and AEO Foundations]]`. | 🟠 | L | P2 |

### Performance

| ID | Finding | Evidence | Business impact | Sev | Effort | Pri |
|---|---|---|---|---|---|---|
| **PERF-01** | **gzip/brotli compression not enabled** | Requested `Accept-Encoding: gzip, br`; no `Content-Encoding` in response. `verified` | Every file is sent at full size. Text assets typically shrink 70–80% with one nginx directive. On an Egyptian mobile connection this is free speed. **Best effort-to-return ratio on this entire page after the certificate.** | 🟠 | XS | P0 |
| **PERF-02** | **Very heavy 3D/animation stack** — Three.js, GSAP + ScrollSmoother, Rapier physics, Skia/CanvasKit, Spline | `stated` from the bundle audit; entry files confirmed `verified`; **total weight `NEEDS VERIFICATION`** | The audience is on Egyptian mobile networks. A site this heavy is slow to become interactive and drains battery. The irony: the 3D craft is a genuine differentiator, and it is also what makes the site unusable for the people it is meant to impress. Do not delete it — budget it. | 🟠 | L | P2 |
| **PERF-03** | **Third-party dependency on `unpkg.com`** for the Spline viewer | `verified` — script tag in the served HTML | `unpkg` is a free community CDN with no uptime guarantee, and it is occasionally slow or unreachable from some networks. If it fails, the hero of the site fails. Self-host the file. | 🟡 | XS | P1 |
| **PERF-04** | No measured Core Web Vitals baseline | Nothing in the vault. `stated` | Nobody can tell whether performance work helped. Run Lighthouse once the certificate is fixed and record the number. | 🟡 | S | P1 |

### Content, conversion and brand

| ID | Finding | Evidence | Business impact | Sev | Effort | Pri |
|---|---|---|---|---|---|---|
| **CONT-01** | **No phone number and no WhatsApp on the site** | `stated` (evidence note). Facebook has `+20 10 43547526`; the site has a form + email. The served shell has no content at all, so this must be re-checked visually once rendering is fixed. **`NEEDS VERIFICATION` in the rendered app.** | WhatsApp is how business is actually done in Egypt. Forcing a form on a buyer who wants to type a message loses the buyer. | 🟠 | XS | P1 |
| **CONT-02** | **Contact form promises a 24-hour response with no named owner and no CRM** | `stated` (evidence note) | A published promise nobody owns is a reputation liability. Worse: **nobody has confirmed the form actually delivers email.** Test it today. | 🟠 | S | P0 |
| **CONT-03** | **Meta description is English-only on an Arabic-first site** | `verified` | The Google result for an Arabic search shows an English summary. Mismatched language reduces click-through. | 🟡 | XS | P1 |
| **CONT-04** | Four real projects described by *what they are*, never by *what changed for the client* | `stated` (evidence note) | No number, no before/after, no quote. See `[[Portfolio and Case Studies]]`. | 🟠 | M | P1 |
| **CONT-05** | Privacy Policy and Terms of Service links exist; content unconfirmed | `stated`. Cannot verify — no rendering. **`NEEDS VERIFICATION`** | Empty legal pages are a trust problem for Gulf and enterprise buyers. | 🟡 | S | P2 |
| **CONT-06** | **Two conflicting published methodologies** (site's 4-phase vs Facebook's 5-stage) | `stated` (both evidence notes) | A prospect who reads both meets two different companies. `[[Foundation Brief]]` requires one canonical version. | 🟡 | S | P1 |
| **CONT-07** | **No link between Facebook and the website in either direction** | `stated` — Facebook lists no website; the site does not link the page | The two channels do not compound. The 74 followers never see the portfolio. | 🟠 | XS | P0 |
| **CONT-08** | Budget dropdown bands unknown | `stated` — not present in the extracted bundles | Leads cannot be qualified if nobody knows what the buyer was asked to choose between. | 🟡 | XS | P1 |

### Analytics

| ID | Finding | Evidence | Business impact | Sev | Effort | Pri |
|---|---|---|---|---|---|---|
| **AN-01** | **No analytics tag of any kind in the served HTML** | Zero inline scripts; only 3 external scripts, none of them analytics. `verified` | There is no record of how many people have ever visited, where they came from, or how many started the contact form. Every marketing decision to date has been made blind — and there is no baseline to improve against. | 🟠 | S | P1 |
| **AN-02** | No Google Search Console or Bing Webmaster property | `stated` — nothing in the vault | Nobody can see what Google thinks of the site, or be told when it breaks. Search Console would have flagged the crawl failures for free. | 🟠 | S | P1 |
| **AN-03** | No Meta Pixel despite Facebook being the only active channel | `verified` (absent) | The 74 followers and anyone who visited cannot be retargeted. There is no way to measure whether a post drove a visit. | 🟡 | S | P2 |

Full instrumentation plan: `[[Analytics and Measurement Setup]]`.

---

## 3. What is genuinely good — and must not be broken while fixing the above

This is not a hit piece. The site has real assets that most agencies in the region do not have:

1. **The writing is the best asset Code Square owns.** The three philosophy statements — *"We don't chase trends, we build fundamentals that last" · "We don't just code, we architect for scale" · "We're not just service providers, we're your technology partner"* — are specific, confident, and falsifiable. Most competitor copy is adjectives. `stated`
2. **A real, credible bilingual structure.** Not machine-translated. Arabic-native content with an English parallel, and a proper Arabic typeface (Tajawal) alongside the display face. This is a genuine Gulf-market asset once `hreflang` is added. `stated`
3. **Four real projects, two with external clients** — including a maritime manning-agency system in a Suez Canal port city. This is a defensible vertical asset. `stated`
4. **Serious design and animation craft.** The 3D work, the scroll choreography, the glass surfaces. For a company selling UI/UX, the site *is* the portfolio. The problem is delivery weight, not the work itself. `verified` (bundle composition)
5. **Coherent, documented design tokens** in the compiled CSS — navy, gold, per-entity accents, typography. Someone built a real system. `stated`
6. **The page-level metadata was fixed** since the original audit. Somebody is maintaining this. `verified`
7. **Static asset caching is correctly configured** (`max-age=31536000, immutable`) and the HTML is correctly marked no-store. That is a competent nginx setup by someone who knew what they were doing. `verified`
8. **HTTP correctly redirects to HTTPS (301).** `verified`

**Read this list as evidence that the problem is neglect, not incompetence.** A site with correct immutable caching and a proper 301 was built by someone capable. The certificate lapsed and the rendering question was never asked. Both are fixable in days.

---

## 4. The credibility paradox

> **Code Square sells digital trust from a website the internet officially marks as untrusted, and sells discoverability from a website that no search engine can see.**

This is the most commercially damaging fact in the vault, and it operates in three separate ways.

### 4.1 The sales-conversation cost

Picture the actual moment. A shipping agency manager in Port Said is told about Code Square. He types the address. He gets a red full-screen warning that says *"Attackers might be trying to steal your information"*. He does not read the philosophy statements. He does not see the Osama Sakr manning system. He closes the tab and calls someone else — and he now believes something about Code Square that will be very hard to unbelieve.

The cost is not a lost click. It is a **lost first impression in the exact domain the company claims expertise in**. A restaurant with food-safety violations posted on the door is not judged on its menu.

Worse: the founder cannot safely send the link. Every WhatsApp introduction, every business card, every proposal that names the URL currently makes the company look worse than saying nothing. **Today, Code Square's website is a net negative asset.**

### 4.2 The discovery cost

Because the HTML body is empty, the company does not exist to:
- Google and Bing organic search
- ChatGPT, Claude, Perplexity, and Gemini when someone asks *"who builds custom software in Port Said?"*
- Facebook and WhatsApp link previews (no `og:image`, and the link warns before it loads)

Code Square is competing in a market where buyers research before they call — a point **Code Square itself argues in its own Facebook post** *"ليه أي مشروع في 2026 محتاج وجود رقمي؟"*. The company published the correct diagnosis and then failed its own test. `stated`

### 4.3 The compounding cost

Every day the site stays broken:
- Facebook content is produced with nowhere credible to send people (`stated`: high content output, near-zero engagement)
- Any ad spend is burned on arrival — the 10,000 EGP/month proposed in the old plan would land on a security warning
- No analytics data is accumulating, so there is no baseline to compare against later
- The four projects stay invisible, so the proof problem in `[[Portfolio and Case Studies]]` cannot even begin to be solved

### 4.4 Quantifying it — illustrative only

> ⚠️ **These numbers are illustrative arithmetic, not measurements.** There is no analytics data (finding AN-01), so real traffic is unknown. The assumptions are stated so the founder can substitute real numbers once `[[Analytics and Measurement Setup]]` is live. **Do not quote these anywhere.**

**Assumptions (all `proposed`, all replaceable):**
- **A** — 100 people per month attempt to reach the site (Facebook links, word of mouth, business cards). *Unmeasured; chosen for round arithmetic.*
- **B** — certificate-warning abandonment ≈ 80%. `researched`: browser interstitial studies consistently find that most users heed a full-page certificate warning rather than click through — see Felt et al., *"Improving SSL Warnings: Comprehension and Adherence"*, CHI 2015 (https://research.google/pubs/pub43265/), reviewed 2026-09-02. Applied here as an assumption, not a site measurement.
- **C** — enquiry rate for a visitor who *does* see the site ≈ 3%. *Assumed, unmeasured.*
- **D** — enquiry → paid project ≈ 20%. **TBD, founder must supply.**
- **E** — average project value. **TBD, founder must supply.**

**The arithmetic:**
- Working site: 100 visitors × 3% = **3 enquiries/month**
- Broken site: 100 × 20% (get past the warning) × 3% = **0.6 enquiries/month**
- **Loss ≈ 2.4 enquiries per month**, roughly **29 enquiries a year**, purely from the certificate. At assumption D, ≈ **6 lost projects a year**. Multiply by E.

**And this ignores the larger loss.** The certificate is a 20-minute fix. The rendering problem (CRAWL-01) means variable A is *permanently capped near zero* — there is no organic search channel and no AI-citation channel at all, so the company can only ever get traffic it pays for or personally introduces. That is the more expensive number, and it cannot be estimated at all until the site is crawlable and Search Console has 90 days of data.

**The honest statement to the founder:** *"I cannot tell you what this is costing you, because the instrument that would measure it does not exist. That is itself a finding. What I can tell you is that the cheapest fix on this list takes twenty minutes, and today it takes your website from actively harmful to merely invisible."*

---

## 5. Scoreboard

| Layer | Passing | Total | Score |
|---|---|---|---|
| Security and trust | 1 (HTTPS redirect) | 5 | 20% |
| Crawlability and discovery | 1 (page title/meta) | 12 | 8% |
| Performance | 1 (asset caching) | 5 | 20% |
| Content and conversion | 2 (bilingual content, real portfolio) | 10 | 20% |
| Analytics | 0 | 4 | 0% |
| **Overall** | **5** | **36** | **≈14%** |

Target after `[[Remediation Plan - Priority Zero]]` (7 days): **≈45%**. Target after Phase 1 of `[[Digital Infrastructure Roadmap]]` (90 days): **≥75%**.

---

## 6. The order everything must happen in

1. **SEC-01** — renew the certificate. Twenty minutes. Nothing else on this list has any value until this is done.
2. **PERF-01** — turn on gzip. One nginx directive. Best return per minute of the entire audit after step 1.
3. **CRAWL-02** + **CRAWL-09** — serve a real `robots.txt`; fix or claim `og:url`.
4. **CONT-02** — prove the contact form delivers, and name its owner.
5. **SEC-02 / SEC-03** — automate renewal and add monitoring so step 1 can never recur.
6. **CRAWL-01** — prerender or SSR. The big one. Days, not hours.
7. Everything else, in priority order.

---

## Related
[[Foundation Brief]] · [[Remediation Plan - Priority Zero]] · [[SEO and AEO Foundations]] · [[Analytics and Measurement Setup]] · [[Digital Infrastructure Roadmap]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]] · [[2026-09-02 - Facebook Page Evidence]] · [[Portfolio and Case Studies]] · [[Marketing Strategy]] · [[Paid Media Plan]] · [[KPI Dashboard]] · [[Open Questions and Decisions Needed]]
