---
date: 2026-09-02
type: analytics-plan
tags:
  - technical
  - analytics
  - measurement
  - attribution
  - code-square
ai-first: true
status: draft
owner: TBD
severity: high
confidence: mixed
---

# Analytics and Measurement Setup

## For future Claude

What to instrument, in what order, so Code Square can stop guessing. `verified` 2026-09-02: **there is no analytics tag of any kind on the site** — the served HTML contains three external scripts and none of them measure anything. Nothing has ever been counted.

This note deliberately specifies a **minimum honest setup**, not an enterprise stack. Everything named here is free or near-free, and each item earns its place by answering a question the founder actually has. If a tool does not change a decision, it is not on this list.

Depends on `[[Remediation Plan - Priority Zero]]` (a site nobody can load produces no data worth having) and feeds `[[KPI Dashboard]]`.

Labels: `verified` · `stated` · `researched` (URL + date) · `proposed` · `TBD`.

---

## 0. The consequence, first

**Every marketing decision Code Square has ever made was made blind.** Not badly — blind. There is no record of how many people visited the site, where they came from, how many started the contact form and gave up, or whether a single Facebook post ever produced an enquiry.

That has three costs:
1. **You cannot tell what is working**, so you cannot do more of it.
2. **You cannot tell what is broken.** Nobody knows whether the contact form has ever delivered an email (`stated` — unverified, tracked as CONT-02 in `[[Website and Technical Audit]]`). A form that silently fails looks identical to a market that is not interested.
3. **There is no baseline.** When the site is fixed, nobody will be able to say by how much things improved — because "before" was never measured. **Every week without instrumentation is a week of baseline permanently lost.**

The whole of this note is about 6–8 hours of setup work, costing nothing, that turns "I think Facebook isn't working" into "43 people came from Facebook, 2 started the form, 0 finished it, and here is why".

**Plain-language glossary:**

| Term | Meaning |
|---|---|
| **GA4** | Google Analytics 4. The free tool that counts visits and what people did. |
| **Event** | A recorded action — a page view, a button click, a form submission. |
| **Conversion / key event** | An event that matters commercially. A WhatsApp click is one; scrolling is not. |
| **Tag** | A small piece of JavaScript added to the site that reports to a measurement tool. |
| **Pixel** | Facebook's word for its tag. |
| **UTM parameters** | Labels added to the end of a link (`?utm_source=facebook`) so the analytics tool knows where a visitor came from. |
| **Attribution** | Working out which marketing effort produced a given enquiry. |
| **Conversions API (CAPI)** | Facebook's server-to-server reporting channel, used when the browser tag is blocked. |
| **Consent** | The visitor's permission to be tracked. Legally required for EU visitors. |

---

## 1. Order of implementation

Do these in order. Later items depend on earlier ones existing.

| # | What | Depends on | Effort | Why now |
|---|---|---|---|---|
| **1** | **Google Search Console + Bing Webmaster** | Certificate fixed | 30 min | Free, tells you what Google thinks, and would have caught the crawl failures |
| **2** | **GA4 with the six events that matter** | Certificate fixed | 2–3 h | The baseline. Every day of delay is lost history |
| **3** | **The lead-source question on the contact form** | Nothing | 15 min | The cheapest attribution that survives WhatsApp |
| **4** | **UTM convention, written down and used** | Nothing | 30 min | Worthless unless applied consistently from day one |
| **5** | **WhatsApp click tracking + pre-filled message** | Site links to WhatsApp | 1 h | This is how Egyptian B2B leads actually arrive |
| **6** | **Meta Pixel** | GA4 done | 1 h | Only worth it once ads are contemplated |
| **7** | **Meta Conversions API** | Pixel live, ads running | 3–4 h | Defer until there is real ad spend |
| **8** | **A lead log (spreadsheet, not a CRM)** | Nothing | 1 h | See §7 |

**Items 1–5 are the honest minimum and take one working day.** Items 6–8 wait for `[[Paid Media Plan]]` to actually begin.

---

## 2. Google Search Console and Bing Webmaster Tools — do these first

**Why first:** free, 30 minutes, no code beyond a verification tag, and it is the only tool that reports on *invisible* problems. `verified`: Search Console would have flagged that the site renders nothing — no one was listening.

**Setup:**
1. Create a **Domain property** in Search Console (https://search.google.com/search-console) via a DNS TXT record. Domain-level verification covers `http`, `https`, `www`, and every subpath at once — do not use the URL-prefix method, which only covers one variant and is the usual cause of "why is half my data missing".
2. Submit `sitemap.xml` once it exists (`[[SEO and AEO Foundations]]` §7).
3. **Turn on email alerts.** This is the point of the exercise.
4. Repeat at Bing Webmaster Tools (https://www.bing.com/webmasters) — it can import the Search Console setup in one click. Bing matters more than its market share suggests because **it feeds some AI answer engines**.
5. Use **URL Inspection → Test Live URL → View Crawled Page** as the acceptance test for the prerendering work in `[[Remediation Plan - Priority Zero]]` §B1. This is Google telling you directly whether it can read the page.

**What to check monthly:** total impressions and clicks, which queries produce them, coverage errors, and any manual actions. Record the first month's numbers in `[[KPI Dashboard]]` as the baseline — **including if they are zero.** A recorded zero is data.

**Owner:** TBD. **Cost:** 0.

---

## 3. GA4 — and only the events that matter

**The trap to avoid:** GA4 default installs report dozens of automatic events, most of which nobody will ever look at. **A dashboard nobody reads is worse than no dashboard**, because it creates the feeling of measurement without any. Instrument the six things below and ignore the rest.

### 3.1 The six events

Each answers a specific question the founder has today.

| Event name | Fires when | The question it answers |
|---|---|---|
| `form_start` | Someone types into the first contact-form field | How many people *wanted* to enquire? |
| `form_submit` | The form submits successfully | How many finished? **`form_start` minus `form_submit` is the abandonment number — and it is usually the most actionable figure on the whole site.** |
| `whatsapp_click` | A WhatsApp link or button is clicked | How many chose the channel Egyptians actually use? |
| `phone_click` | A `tel:` link is clicked | Same, for phone. |
| `case_study_view` | A project page is viewed for >15 seconds | Is the portfolio — the company's best asset — being read? |
| `scroll_75` | A visitor reaches 75% of a service or industry page | Did the page hold them, or did they bounce off the 3D hero? |

Mark `form_submit`, `whatsapp_click` and `phone_click` as **key events** (GA4's term for conversions). The other three are diagnostics, not goals.

### 3.2 Implementation — the lazy version

**Skip Google Tag Manager for now.** GTM is the right answer when several people manage many tags across many sites. Code Square has one site and six events. GTM adds an interface, a publishing workflow, and one more thing to configure wrongly. `proposed`: install the GA4 tag directly, and adopt GTM later if tag count grows past about a dozen.

```html
<!-- In <head>, after consent (see §8) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

The six events, from the Angular app:

```javascript
// form_start — once per session, on first interaction with the form
gtag('event', 'form_start', { form_id: 'contact' });

// form_submit — on the success response, NOT on button click.
// A click that fails is not a lead, and counting it hides the failure.
gtag('event', 'form_submit', {
  form_id: 'contact',
  project_type: selectedProjectType,   // from the existing dropdown
  budget_band: selectedBudget,         // once the bands are confirmed (CONT-08)
  lead_source: selectedLeadSource      // see §4
});

// whatsapp_click / phone_click
gtag('event', 'whatsapp_click', { location: 'header' });   // or 'footer', 'contact_section'
gtag('event', 'phone_click',    { location: 'footer' });

// case_study_view — after 15s on a /work/ page
gtag('event', 'case_study_view', { project: 'osama-sakr' });

// scroll_75 — GA4's enhanced measurement fires a 90% scroll automatically;
// use that instead of custom code unless 75% is genuinely needed.
```

`project_type` and `budget_band` reuse dropdowns that **already exist on the form** (`stated`). That means, at zero extra friction to the visitor, GA4 can answer *"which project types actually enquire, and at what budget?"* — the most commercially useful question in this whole note.

### 3.3 Configuration that prevents bad data

- **Exclude internal traffic.** Add the office and founder IP addresses under Admin → Data Streams → Configure tag settings → Define internal traffic. Without this, a small site's numbers are mostly the team looking at their own website.
- **Set data retention to 14 months** (Admin → Data Settings). The default is 2 months, which makes year-on-year comparison impossible. Free, one click, and cannot be applied retroactively — do it on day one.
- **Set the reporting timezone to Egypt** and currency to EGP.
- **Do not enable Google Signals** unless the consent notice in §8 covers it.

**Acceptance test:** open GA4 → Reports → Realtime, load the site on a phone, submit a test form, click WhatsApp. All three events must appear within 60 seconds. Then use GA4's **DebugView** to confirm the parameters carry real values, not `undefined`.

**Owner:** TBD. **Effort:** 2–3 hours. **Cost:** 0.

---

## 4. UTM naming convention

**Consequence first:** without this, every visitor from Facebook, WhatsApp, an email signature, and a QR code on a business card lands in one undifferentiated bucket called "direct", and nobody can tell which effort worked. UTMs are free and take ten seconds per link — but **only if the naming is consistent.** `utm_source=Facebook` and `utm_source=facebook` are two different sources in every analytics tool ever built.

### The rules — `proposed`

1. **Lowercase always.** No exceptions.
2. **Hyphens between words**, never spaces or underscores.
3. **`utm_source`** = the platform (`facebook`, `whatsapp`, `linkedin`, `email`, `print`).
4. **`utm_medium`** = the type of traffic. Use only these five: `social-organic`, `social-paid`, `email`, `referral`, `offline`.
5. **`utm_campaign`** = `<yyyy-mm>-<segment>-<theme>`. The date prefix makes campaigns sort chronologically and prevents the same name being reused a year later.
6. **Never put a UTM on an internal link.** It restarts the session and destroys the original attribution — the most common self-inflicted analytics wound.
7. **Every link gets one.** A link without a UTM is a lead whose origin is lost forever.

### Filled-in examples

| Where the link appears | Full URL |
|---|---|
| Facebook page "Website" button | `https://codesquare.com/?utm_source=facebook&utm_medium=social-organic&utm_campaign=2026-09-profile-link` |
| Organic post about the maritime case study | `https://codesquare.com/work/osama-sakr/?utm_source=facebook&utm_medium=social-organic&utm_campaign=2026-09-maritime-case-study` |
| Paid ad to the maritime landing page | `https://codesquare.com/industries/maritime/?utm_source=facebook&utm_medium=social-paid&utm_campaign=2026-10-maritime-diagnostic&utm_content=video-a` |
| Link sent in a WhatsApp conversation | `https://codesquare.com/diagnostic-session/?utm_source=whatsapp&utm_medium=referral&utm_campaign=2026-09-founder-outreach` |
| Email signature | `https://codesquare.com/?utm_source=email&utm_medium=email&utm_campaign=2026-signature` |
| QR code on a business card | `https://codesquare.com/?utm_source=print&utm_medium=offline&utm_campaign=2026-business-card` |
| Diagnostic Session link in a proposal PDF | `https://codesquare.com/diagnostic-session/?utm_source=proposal&utm_medium=offline&utm_campaign=2026-proposal-doc` |

**Keep a single sheet of every UTM link ever created**, with the date and who made it. When a spike appears in GA4 six weeks later, that sheet is the only way to know what caused it. `proposed`

`researched` 2026-09-02 — Google's Campaign URL Builder generates these correctly: https://ga-dev-tools.google/campaign-url-builder/

---

## 5. WhatsApp and phone attribution in an Egyptian context

**This is the section that matters most in this market, and it is the one generic analytics advice always gets wrong.**

The reality: `stated` — the Facebook page carries the phone and WhatsApp; the site has only a form and an email. Most Egyptian B2B buyers will **not** fill in a form. They will tap WhatsApp and type a message. **The moment they do, they leave every tracking system Code Square has.** GA4 records a click and then goes blind. Facebook records nothing.

There is no free tool that follows a person into WhatsApp. So the answer is not a tool — it is **carrying the source into the conversation itself.**

### 5.1 Pre-filled WhatsApp messages — the single best trick here

Use `wa.me` links with a pre-filled message that **encodes where the click came from**:

```html
<!-- On the maritime industry page -->
<a href="https://wa.me/201043547526?text=%D8%B9%D8%A7%D9%88%D8%B2%20%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%B1%20%D8%B9%D9%86%20%D9%86%D8%B8%D8%A7%D9%85%20%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9%20%5Bmaritime%5D">
  تواصل واتساب
</a>
```

The decoded message reads: *"عاوز استفسر عن نظام إدارة [maritime]"*.

The person taps, WhatsApp opens with the text already typed, they usually send it as-is. **The `[maritime]` tag arrives in the inbox.** Whoever answers now knows the lead came from the maritime page without asking, and can log it.

Use a different tag per page: `[maritime]`, `[education]`, `[saas]`, `[home]`, `[case-osama-sakr]`, `[ad]`. `proposed`

**This costs nothing, requires no tool, needs no consent banner, and survives the channel handoff completely.** It is the highest-return item in this note.

### 5.2 Click tracking on the way out

Fire `whatsapp_click` and `phone_click` (§3.1) with a `location` parameter. This gives the *front half* of the funnel: how many people wanted to talk, and from which page. Combined with §5.1's inbox tags, the two halves reconcile — and **a large gap between clicks and messages received is itself a finding** (usually a broken link or a wrong number).

### 5.3 What NOT to buy yet

- **Call-tracking numbers** (a different phone number per campaign) work well in the UK and US but are awkward and expensive for Egyptian mobile numbers, and a changing number **breaks NAP consistency** (`[[SEO and AEO Foundations]]` §11.2), which actively damages local SEO. **Do not do this.** `proposed`
- **WhatsApp Business API** with a CRM integration is the proper long-term answer, but it costs money per conversation and needs a CRM that does not exist yet. `TBD` — revisit in Phase 2 of `[[Digital Infrastructure Roadmap]]`.
- **Use the free WhatsApp Business app** in the meantime: labels (`جديد`, `تم الرد`, `عرض سعر`, `مكسوب`, `مرفوض`) and quick replies are enough for the current volume, and cost nothing.

---

## 6. Meta Pixel and Conversions API

**Only worth doing once advertising is genuinely imminent.** Installing a pixel on a site with no ad spend collects a small audience and little else. But it must be installed **before** the first ad, not after — a pixel has no history on day one, and the audience it builds is the most valuable thing it produces.

### 6.1 Pixel — 1 hour

Standard base code plus these events, mapped to the GA4 ones so the two systems can be reconciled:

| Meta event | Fires on | GA4 equivalent |
|---|---|---|
| `PageView` | every page | (automatic) |
| `ViewContent` | a case-study or industry page | `case_study_view` |
| `Lead` | successful form submission | `form_submit` |
| `Contact` | WhatsApp or phone click | `whatsapp_click` / `phone_click` |

**Do not fire `Purchase`.** There is no e-commerce transaction, and misusing it corrupts every optimisation Facebook does afterwards.

### 6.2 Conversions API — defer

CAPI sends conversions from the server rather than the browser, recovering events lost to ad blockers and iOS tracking restrictions. It is genuinely valuable **once there is meaningful spend to optimise.** It is 3–4 hours of backend work and requires handling hashed personal data, which brings the privacy obligations in §8 into play.

`proposed`: **defer CAPI until monthly ad spend exceeds roughly 5,000 EGP** — below that, the measurement improvement will not change any decision. Note it as a Phase 2 item in `[[Digital Infrastructure Roadmap]]` and link it from `[[Paid Media Plan]]`.

---

## 7. Lead-source tracking that survives the WhatsApp handoff

**The problem in one sentence:** a lead arrives by WhatsApp, is discussed by phone, quoted by email, and closed in a meeting — and **no analytics tool sees any of it.** GA4 will happily report "3 form submissions" while the business actually received eleven enquiries.

**The fix is not a tool. It is a habit plus one field.**

### 7.1 Ask the question on the form

Add one optional field to the contact form: **"عرفت عنّا منين؟"** — with options: فيسبوك · بحث جوجل · ترشيح من صديق · معرفة شخصية · واتساب · أخرى.

Self-reported source is imperfect — people misremember. But **it is the only signal that captures offline and word-of-mouth referrals**, which for a company with 74 followers and a founder network are probably the majority of real leads today. Pass the answer into GA4 as the `lead_source` parameter (§3.2).

### 7.2 Log every enquiry, from every channel, in one place

**Do not buy a CRM yet.** `proposed`. At current volume a CRM is an unused subscription. A single shared spreadsheet, filled in the same day, beats an empty HubSpot every time. Columns:

| Date | Name | Company | Channel | Source detail | Segment | Project type | Budget signal | First response time | Stage | Outcome | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

- **Channel** — `whatsapp` / `form` / `phone` / `messenger` / `email` / `in-person`
- **Source detail** — the `[maritime]` tag from §5.1, the UTM campaign, or "referral from X"
- **Segment** — maritime / education / healthcare / other, per `[[Foundation Brief]]` §4
- **First response time** — this is the one that audits the published **24-hour SLA** (CONT-02). Nobody currently knows whether it is being met.

Graduate to a real CRM when the sheet exceeds roughly 20 open leads or more than one person is handling them. That trigger belongs in `[[Lead Intake and CRM]]` and Phase 2 of `[[Digital Infrastructure Roadmap]]`.

### 7.3 Reconcile monthly

Once a month, compare: GA4 `whatsapp_click` count · messages actually received · rows in the lead log · form submissions in GA4 · emails in the inbox.

**The gaps are the findings.** Many clicks and few messages means a broken link. Form submissions in GA4 but no emails means **the form is silently failing** — and that check is the only thing that would ever catch it.

---

## 8. Privacy and consent

**Consequence first:** most of Code Square's traffic is Egyptian and Gulf, where consent-banner obligations are lighter than in Europe. But `[[Foundation Brief]]` names an English site for Gulf and international buyers, and **any EU visitor triggers GDPR regardless of where the company is based.** More practically: **Code Square sells trust.** A privacy notice that is honest and readable is a sales asset, not a compliance chore.

### What actually applies — `researched` 2026-09-02

| Jurisdiction | Position | What it requires here |
|---|---|---|
| **Egypt** | Personal Data Protection Law No. 151 of 2020. Passed and in force in principle; the executive regulations establishing the supervisory centre have been slow to arrive, so enforcement practice is still limited. **`NEEDS VERIFICATION` — confirm current enforcement status with an Egyptian lawyer before relying on any interpretation here.** | Consent for personal-data processing; a published privacy notice. |
| **Saudi Arabia** | Personal Data Protection Law (PDPL), enforced by SDAIA since September 2024. https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf | Consent, a privacy notice, and a lawful basis. Relevant given the stated Jeddah/Riyadh service areas. |
| **EU/EEA visitors** | GDPR + ePrivacy. Applies to any EU visitor regardless of company location. | **Prior consent before setting analytics or advertising cookies.** GA4 and Meta Pixel both require it. |

### The proportionate implementation — `proposed`

1. **A real privacy policy page in Arabic and English.** `stated`: links exist; content unconfirmed (CONT-05). It must say plainly: what is collected, why, who it is shared with (Google, Meta), how long it is kept (14 months in GA4 — §3.3), and how to request deletion, with a working contact address.
2. **A consent banner, shown to everyone.** Do not build geo-detection to show it only in Europe — the engineering is not worth it, and showing it universally signals seriousness to every buyer. Requirements: Accept and Reject buttons of **equal prominence** (a greyed-out reject button fails GDPR), no pre-ticked boxes, no tracking scripts fire before a choice is made, and the choice is re-askable.
3. **Google Consent Mode v2** if using GA4 in Europe at all — GA4 receives anonymous, cookieless signals until consent is given, so data is not simply lost. `researched` 2026-09-02: https://developers.google.com/tag-platform/security/guides/consent
4. **Free implementation options:** a hand-rolled banner (~50 lines, entirely sufficient for two tools), or **Cookiebot** / **CookieYes** free tiers. `proposed`: hand-roll it. Two tools do not justify a third-party consent platform on every page load, and this site already has a payload problem.
5. **If Meta CAPI is implemented (§6.2):** it sends hashed customer data server-side. That materially increases the obligation. Do not implement it without updating the privacy policy in the same change.
6. **Never send personally identifying data to GA4.** No names, no emails, no phone numbers in event parameters or URLs — it violates Google's terms and will get the property deleted.

**Owner:** TBD — needs founder sign-off on the policy wording. **Legal review recommended** before publishing the Arabic privacy policy.

---

## 9. Reporting cadence

**A report nobody reads is waste.** Three rhythms, and no more.

### Weekly — 10 minutes, founder alone
Check only: enquiries received this week (from the lead log), first-response times against the 24-hour SLA, and any alert from UptimeRobot or Search Console. **Do not open GA4 weekly.** At this traffic level, weekly numbers are noise, and reading noise as signal produces bad decisions.

### Monthly — 45 minutes, into `[[KPI Dashboard]]`

| Metric | Source |
|---|---|
| Sessions, users, and top traffic sources | GA4 |
| `form_start` vs `form_submit` (the abandonment gap) | GA4 |
| `whatsapp_click` + `phone_click` | GA4 |
| Enquiries logged, by channel and segment | Lead log |
| Enquiry → Diagnostic Session booked | Lead log |
| Median first-response time | Lead log |
| Search impressions, clicks, and top queries | Search Console |
| Coverage / indexing errors | Search Console |
| **AI visibility: the ten questions from `[[SEO and AEO Foundations]]` §9** | Manual, recorded verbatim |
| Site uptime and any incidents | UptimeRobot |
| Core Web Vitals | Search Console / Lighthouse |

### Quarterly — 2 hours, strategic
Trend the monthly numbers. Re-run the full audit acceptance tests from `[[Remediation Plan - Priority Zero]]`. Re-check AI crawler names in `robots.txt`. Refresh `llms.txt`. Verify NAP consistency. Review whether the beachhead choice in `[[Foundation Brief]]` §4 is supported by where enquiries actually came from.

### The rule that makes this work
**Write the numbers down even when they are zero, and even when they are bad.** A recorded zero for three months is what makes month four's "seven enquiries" meaningful. The most common failure of a measurement programme is not bad tooling — it is quietly stopping when the numbers are embarrassing.

---

## 10. What must NOT be bought

- **No paid analytics tools.** GA4, Search Console, Bing Webmaster, UptimeRobot and a spreadsheet cover everything at this stage, for nothing.
- **No CRM** until the lead sheet is genuinely straining (§7.2).
- **No call-tracking numbers** (§5.3) — they break NAP consistency.
- **No heatmap or session-recording tool yet.** Hotjar and similar are useful at a few hundred sessions a month. Below that they record the team's own visits.
- **No dashboard-building tool.** A spreadsheet updated monthly is the correct instrument for this volume.
- **No A/B testing tool.** Testing requires traffic that does not exist. Fix the site first.
- **No Meta CAPI** until ad spend justifies it (§6.2).

Every one of these becomes right later. None is right now, and buying them early converts a measurement problem into a subscription problem.

---

## Related
[[Website and Technical Audit]] · [[Remediation Plan - Priority Zero]] · [[SEO and AEO Foundations]] · [[Digital Infrastructure Roadmap]] · [[Foundation Brief]] · [[KPI Dashboard]] · [[Marketing Strategy]] · [[Paid Media Plan]] · [[Lead Intake and CRM]] · [[Portfolio and Case Studies]] · [[Open Questions and Decisions Needed]]
