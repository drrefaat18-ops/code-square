---
date: 2026-09-02
type: standard
tags:
  - delivery
  - quality
  - handover
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Quality Standards and Handover

## For future Claude

The definition of "finished" at three levels, the checklist that must pass before anything goes live, what the client receives at handover, and how acceptance is signed. All `proposed` (2026-09-02) unless marked `stated`.

Two things drive the content here:

1. The website already claims *"صيانة ما بعد الإطلاق"*, *"Awwwards-tier"* UI, and **SLA Guarantees** (`stated`). Claims like these need a standard behind them or they become the banned unfalsifiable claims in `[[Foundation Brief]]` §5.
2. **The group's own TLS certificate is expired** (`stated`, `[[Website and Technical Audit]]`). A company that sells digital trust served an untrusted site. The TLS check below is therefore not a routine line item — it is called out separately and it blocks launch.

Owners are **functions**, not people. Roster unknown.

---

## Terms used here

| Term | Plain meaning |
|---|---|
| **Definition of Done (DoD)** | The written conditions work must meet before anyone is allowed to call it finished. |
| **Defect / bug** | The system does not do what the agreed scope says it should. |
| **Regression** | Something that used to work and now does not. |
| **TLS certificate** | The file that makes a site load as `https://` with a padlock. If it expires, every visitor sees a full-page security warning before your site. |
| **Auto-renew** | The certificate or domain renews itself on a schedule with no human remembering. |
| **Accessibility** | Whether people using a screen reader, keyboard only, or with low vision can actually use it. |
| **SEO basics** | The minimum that lets Google and AI engines read and list a page. |
| **Analytics** | A tool that records how many people visit and what they do. |
| **Error monitoring** | A tool that alerts you when the live system throws an error, instead of you finding out from an angry client. |
| **Backup** | A copy of the data and the site, stored somewhere else, that has actually been restored at least once to prove it works. |
| **Warranty period** | A window after launch in which defects in the delivered scope are fixed free. |
| **Acceptance** | The client formally confirming the delivered work meets the agreed criteria. |

---

## 1. Definition of Done — three levels

Each level includes all the levels below it. Nothing skips a level because it is "small" or "urgent".

### 1a. Task level (a single piece of work)

- [ ] Does what its written acceptance condition says
- [ ] Tested by the person who built it, on the actual device or browser it targets
- [ ] Code reviewed by a second person — a review by nobody is not a review
- [ ] Handles the obvious failure cases: empty state, no internet, wrong input, very long text, Arabic and English content
- [ ] No credentials, keys, or passwords in the code
- [ ] Merged, and running on staging
- [ ] The task item is updated with what was actually done

**If only one person can review code today, say so and record it as a known single point of failure in `[[Org and Roles]]`. Do not quietly drop the rule.**

### 1b. Feature level (something a user can do end to end)

Everything above, plus:

- [ ] The complete user journey works start to finish, not just the happy path
- [ ] Works on mobile — the majority of Egyptian users, and the site is heavy today (`stated`, `[[Website and Technical Audit]]`)
- [ ] Arabic and English both correct, including right-to-left layout, dates, and numbers
- [ ] Permissions correct: a user cannot see or change what they should not
- [ ] Data validated at the point of entry, so bad data cannot get in
- [ ] Errors show the user something useful, not a blank screen or a raw technical message
- [ ] Loading and empty states designed, not accidental
- [ ] Demonstrated to the client in a weekly demo, and their feedback either applied or logged as a change request
- [ ] Documentation note written while it is fresh

### 1c. Project level (V1 ready to launch)

Everything above, plus the full pre-launch checklist in §2, plus:

- [ ] Every V1 scope item delivered, or formally deferred with client agreement in writing
- [ ] Known defects listed, each classified *fix before launch* or *accepted, fix later* — with the client having seen the list
- [ ] Client has personally tested on staging and confirmed
- [ ] Handover pack complete (§3)
- [ ] Success metric baseline recorded so the 30-day review can compare against it

---

## 2. Pre-launch checklist

Run against **staging** before launch, then run the critical items again against **production** immediately after deploy. Both runs are recorded with a date and a name.

### 2.1 Functional
- [ ] Every screen and flow in the V1 scope exercised once, manually
- [ ] Every form submits and the submission actually arrives — verified by receiving it, not by seeing a success message
- [ ] Every email the system sends is received, correctly formatted, in Arabic and English, and not in the spam folder
- [ ] Login, logout, and password reset work
- [ ] Payments, if in scope: a real end-to-end test transaction, plus a deliberate failed transaction
- [ ] Every third-party integration verified against the live service, not a test key
- [ ] Search and filters return correct results
- [ ] File uploads work, including a large file and a wrong file type
- [ ] Admin dashboard: create, read, update, delete all work
- [ ] No placeholder text, no lorem ipsum, no test data left in the live system

### 2.2 Cross-browser
- [ ] Chrome, Safari, Firefox, Edge — current versions
- [ ] Safari on iOS specifically — it behaves differently and it is where problems hide
- [ ] Chrome on Android
- [ ] Right-to-left layout checked in each

### 2.3 Mobile
- [ ] Small phone (≈360px wide) and large phone both checked on a real device, not only a simulator
- [ ] Tablet checked
- [ ] Nothing overflows horizontally; nothing requires sideways scrolling
- [ ] Tap targets big enough to hit with a thumb
- [ ] Forms usable with the on-screen keyboard up
- [ ] Tested on a slow connection — throttle to 3G. **This matters more than any other performance test for an Egyptian audience.**

### 2.4 Performance
- [ ] Lighthouse (a free tool built into Chrome) run on the main pages; scores recorded
- [ ] Main page usable within 3 seconds on a simulated 3G connection
- [ ] Images compressed and correctly sized — not a 4MB photo scaled down in the browser
- [ ] Heavy libraries justified. The group site loads ~7.5MB of JavaScript (`stated`); do not repeat this on client work
- [ ] Third-party scripts counted and each one justified
- [ ] Caching configured
- [ ] Database queries checked for the obvious slow ones on a realistic data volume

### 2.5 Security basics
- [ ] Site served over HTTPS everywhere; HTTP redirects to HTTPS
- [ ] No credentials, keys, or tokens in the code or in the browser-visible files
- [ ] Passwords stored hashed, never in plain text
- [ ] Input validated on the server, not only in the browser
- [ ] File uploads restricted by type and size
- [ ] Admin areas require login and check permissions on every request
- [ ] Default and test accounts removed
- [ ] Dependencies checked for known vulnerabilities
- [ ] Rate limiting on login and on public forms
- [ ] Personal data handled per the privacy policy the site publishes

### 2.6 Accessibility basics
Not a full audit — the minimum that keeps the product usable and the claim honest.
- [ ] All images have alternative text
- [ ] Colour contrast passes for body text
- [ ] Every function reachable with a keyboard alone
- [ ] Visible focus indicator when tabbing
- [ ] Form fields have real labels, not just placeholder text
- [ ] Heading levels used in order
- [ ] `lang` attribute correct, and switched correctly between Arabic and English
- [ ] Nothing conveyed by colour alone

### 2.7 SEO basics
This section exists because the group site fails every line of it (`stated`).
- [ ] Every page has its own title and description — not inherited from a parent site
- [ ] One `<h1>` per page, describing that page
- [ ] `sitemap.xml` present and reachable
- [ ] `robots.txt` present and correct
- [ ] `llms.txt` present, for AI engines
- [ ] Content is present in the served HTML — if the page is JavaScript-rendered, server-side rendering or prerendering is in place. **A page that is blank to a crawler is invisible to Google and to every AI engine.**
- [ ] Social sharing preview (Open Graph) set: title, description, image
- [ ] Canonical URLs set
- [ ] Arabic and English versions declared to each other (`hreflang`)
- [ ] No broken links
- [ ] 404 page exists and is useful

### 2.8 Analytics and monitoring
- [ ] Analytics installed and verified by generating a real visit and seeing it appear
- [ ] Key actions tracked — the ones tied to the client's success metric, not just page views
- [ ] Error monitoring installed, with alerts going to a **named person**, not an unwatched inbox
- [ ] Uptime monitoring configured
- [ ] Someone is named as the person who looks at the alerts

### 2.9 Backups
- [ ] Automated backups configured — database and files
- [ ] Frequency agreed with the client and written down
- [ ] Backups stored somewhere other than the production server
- [ ] **A restore has actually been tested once.** An untested backup is a rumour.
- [ ] Retention period set
- [ ] Restore procedure written into the handover pack

### 2.10 TLS certificate — called out separately

> The group's own certificate expired and put a browser security warning in front of every visitor to `mtechsquare.com` (`stated`, `[[Website and Technical Audit]]`). This is the single most embarrassing failure available to a software company, it is completely preventable, and it must never happen on client work.

- [ ] Certificate valid right now
- [ ] **Auto-renewal enabled and verified** — verified means someone confirmed the renewal mechanism runs, not that a box was ticked
- [ ] Expiry date recorded in the annual calendar in `[[Operating Cadence]]` with a named owner
- [ ] An alert is configured to fire **30 days before expiry** to a named person
- [ ] Covers all variants used: bare domain, `www`, and any subdomains
- [ ] Whole site is HTTPS; no mixed content warnings
- [ ] Same checks applied to Code Square's own properties, on the same schedule as client properties

---

## 3. The handover pack

Delivered at Gate D. One folder, one index page, everything linked from it.

### 3.1 Documentation
- [ ] **Admin guide** — how to do the everyday tasks, written for the client's staff, with screenshots, in the language they work in
- [ ] **Technical documentation** — architecture, how to run it locally, how to deploy, environment variables, third-party services used
- [ ] **Data model** — what is stored and what the rules are
- [ ] **Integration list** — every external service, what it does, what it costs, whose account it is, when it renews
- [ ] **Runbook** — what to do when something breaks: how to check status, how to restore a backup, who to call
- [ ] **Known limitations and deferred items** — what V1 deliberately does not do
- [ ] **Scope sheet and change log** — the final record of what was agreed and what changed

### 3.2 Credentials transfer
- [ ] Every account transferred to client ownership, or documented as remaining with Code Square with the reason and the cost
- [ ] Transferred via password manager share — **never in chat, never in an email body, never in a screenshot**
- [ ] Client confirms they can log into each one, live, during the training session
- [ ] 2FA moved to the client's own device or account
- [ ] Code Square's temporary access removed on the agreed date, and the removal recorded
- [ ] Domain and hosting billing moved to the client, or the arrangement written down with renewal dates
- [ ] Source code repository access transferred or granted, per the contract's intellectual property terms

### 3.3 Admin training session
- [ ] Live session, 60–90 minutes, with the people who will actually use the system
- [ ] **Recorded**, and the recording handed over — people forget, and staff change
- [ ] Covers the everyday tasks, not the impressive ones
- [ ] Covers what to do when something looks wrong, and how to raise a support ticket
- [ ] Client does the tasks themselves during the session; we watch. Watching them fail is the point — it is the last chance to catch a usability problem while it is still cheap
- [ ] Questions logged; any documentation gaps they reveal are fixed within 3 working days

### 3.4 Warranty
- [ ] Warranty period stated in writing: `TBD — set` (30 days from launch recommended)
- [ ] What warranty covers: defects in delivered V1 scope, at no charge
- [ ] What it does not cover: new features, changes of mind, content edits, third-party service failures, problems caused by client changes
- [ ] How to raise a warranty issue, and the response target
- [ ] What happens when warranty ends — the transition into `[[Support and Maintenance SLA]]`, agreed **before** launch, not after

---

## 4. Client sign-off and acceptance

### The procedure

1. **Acceptance criteria written at Gate B**, not invented at the end. They restate the scope sheet as testable statements.
2. **Client tests on staging** before launch, against those criteria.
3. **Launch.**
4. **Acceptance window opens** — recommend 10 working days (`TBD — set`).
5. Client either accepts in writing, or lists specific failures against specific acceptance criteria.
6. Failures against criteria are fixed at no charge. Anything that is not a criterion is a change request.
7. **Silence past the window counts as acceptance** — this must be written into the contract, or projects never formally close and the final invoice never falls due.
8. Signed acceptance triggers the final invoice and Gate D.

### The form

| Field | |
|---|---|
| Project | |
| Version accepted | V1 |
| Acceptance criteria met | Yes / Yes with listed exceptions |
| Exceptions accepted, to be fixed by | Date |
| Handover pack received | Yes / No |
| Credentials transferred and verified | Yes / No |
| Admin training completed | Yes / No |
| Warranty period runs | From — to |
| Signed, client decision-maker | Name, date |
| Signed, Code Square | Function — TBD, date |

**Rule: no partial verbal acceptance.** "Yeah it looks good" in a WhatsApp message is not acceptance and does not release the final invoice.

---

## 5. Post-launch review — 30 days after launch

45 minutes with the client. This meeting is where the company's proof problem actually gets solved (`[[Foundation Brief]]` §7 — four real projects, no published numbers).

### Agenda
| Item | Purpose |
|---|---|
| Did the success metric move? | Compare against the baseline recorded at kickoff |
| What is actually being used, and what is not? | Analytics, not opinion. Unused features are a lesson for scoping the next project |
| What is annoying them? | The small friction they have stopped mentioning |
| Support experience so far | Feeds `[[Support and Maintenance SLA]]` |
| **Case study** | The permission was agreed at kickoff — now collect the number, the quote, and the screenshots |
| **Testimonial** | Ask now, at peak satisfaction. Written minimum, filmed if they will |
| V2 conversation | The deferred list plus what usage revealed |
| Retainer | Confirm or agree the support arrangement |

### Internal, straight after
- [ ] Estimate vs actual recorded — hours, calendar days, cost
- [ ] Defects that escaped to production counted, and each one traced to the checklist item that would have caught it
- [ ] This file updated if a check was missing
- [ ] Case study drafted within 5 working days, while it is fresh
- [ ] KPI figures fed into `[[KPI Dashboard]]`

**Rule: if the case study is not drafted within 5 working days of the review, it will never be written.** This is how four real projects ended up with no public write-up.

---

## 6. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | Warranty period — 30 days? | Contract, SLA |
| 2 | Acceptance window — 10 working days? | Contract |
| 3 | Who owns QA when there is no dedicated QA person? | Every project |
| 4 | Do we have a second person able to review code today? | Task-level DoD |
| 5 | Which analytics, error monitoring, and uptime tools are standard? | `[[Tools Stack]]` |
| 6 | Do we drop the "Awwwards-tier" and "SLA Guarantees" claims, or build the standard behind them? | `[[Foundation Brief]]` §5, website copy |
| 7 | Who owns the TLS and domain renewal calendar for both client and own properties? | `[[Operating Cadence]]` |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Delivery Process]] · [[Project Kickoff Checklist]] · [[Support and Maintenance SLA]] · [[Website and Technical Audit]] · [[Org and Roles]] · [[Tools Stack]] · [[Operating Cadence]] · [[KPI Dashboard]] · [[Foundation Brief]] · [[Service Catalog]]
