---
date: 2026-09-02
type: operations
tags:
  - operations
  - tools
  - security
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Tools Stack

## For future Claude

The operating toolkit by function, with a free-or-cheap starting recommendation suited to a small Egyptian company, what each tool is actually for in plain language, a cost band, and the trigger that justifies upgrading.

**The vault does not know what Code Square uses today** — nothing in the evidence files names a single internal tool. So this is a `proposed` starting stack, not a description of reality. `❓ NEEDS FROM FOUNDER:` what is actually in use right now, and what is already being paid for.

Two principles run through everything below:

1. **Fewer tools beats better tools.** Every tool is a subscription, a login, a place information hides, and a thing to offboard someone from. Start with the fewest that cover the work.
2. **Free tiers are enough for a long time.** Almost everything here has a free tier that carries a small company for its first year. Upgrade against a trigger, never against a feature list.

Cost bands: **Free** · **$** = under $10/user/month · **$$** = $10–30 · **$$$** = above $30.

---

## 1. Communication

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Internal team chat | **Slack free**, or **WhatsApp** if the team is tiny | Day-to-day talk, separated into channels per project | Free | Slack free hides old messages past a limit — upgrade when you cannot find a decision from two months ago |
| Client chat | **WhatsApp Business** | What Egyptian clients actually use. Do not fight this | Free | — |
| Email | **Google Workspace** | A professional address. `codesquareteam1@gmail.com` (`stated`) is a credibility leak — every proposal sent from a free Gmail address costs a little trust | $ | Immediate. This is the cheapest credibility upgrade available |
| Video calls | **Google Meet** or **Zoom free** | Client sessions, demos, remote work | Free | Zoom free caps group calls at 40 minutes — a problem for a 90-minute kickoff |
| Calendar | **Google Calendar** | Meetings, and the renewal calendar in `[[Operating Cadence]]` §8 | Free | — |

> **Priority action:** get a real domain and email. `[[Foundation Brief]]` §10 already lists "dedicated domain" as an open blocker. Email and domain are one purchase.

---

## 2. Project and task management

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Task board | **Trello free** or **Notion free** | One board per project: To do / Doing / Review / Done | Free | More than 3 concurrent projects, or you need time tracking |
| Later, if needed | **Linear** or **Jira** | Structured issue tracking with sprints | $$ | Only when a team of 4+ engineers is genuinely blocked by Trello |
| Documents and wiki | **Notion free**, plus this **Obsidian vault** | Notion for shared client-facing docs; Obsidian for the company's own thinking | Free | — |

**Rule: one board per project, and the client sees a read-only view or a weekly written note — not both, and never neither.**

Do not buy Jira. A company this size with Jira spends more time administering it than delivering.

---

## 3. Design

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| UI design and prototyping | **Figma** | Wireframes, screens, clickable prototypes, client review with comments | Free tier, then $$ | Free tier limits shared files — upgrade at 3+ active client projects |
| Graphics and social creatives | **Canva** | Facebook creatives, one-pagers, proposal covers | Free, Pro $$ | Pro when brand templates and background removal are used weekly |
| Asset storage | With Google Drive, §11 | Logos, photos, source files | — | — |

**Brand rule, not a tool rule:** `[[Foundation Brief]]` §8 records two conflicting colour systems in use. Whatever tool is used, one shared template set with the canonical tokens must exist, or the split continues.

---

## 4. Code and version control

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Version control | **GitHub**, free for private repositories | Every line of code, with history. Lose the laptop, keep the work | Free | Team plan when you need enforced code review rules |
| **Organisation account, not personal** | GitHub Organization | Repositories belong to the company, not to a person who might leave | Free | Do this on day one, not later |
| Code review | GitHub pull requests | The second pair of eyes required by `[[Quality Standards and Handover]]` §1a | Free | — |
| Editor | Whatever each developer prefers | — | — | — |

> **This is a continuity control as much as a technical one.** Client code in a personal GitHub account is a single point of failure — `[[Org and Roles]]` §6, row 7.

---

## 5. CI/CD and deployment

**CI/CD** = a robot that checks and publishes the code automatically when it changes, instead of someone copying files onto a server by hand.

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Automated checks and deploys | **GitHub Actions** | Runs tests and deploys on every change | Free tier generous | Only if free minutes run out |
| Simple site or frontend hosting | **Vercel** or **Netlify** | Deploys on push, free TLS certificate that **auto-renews** | Free, then $$ | Real traffic, or team features |

> **The auto-renewing TLS certificate is the point.** The expired certificate on `mtechsquare.com` (`stated`) is a class of failure that modern hosting removes entirely. Prefer platforms where certificates renew themselves.

---

## 6. Hosting

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Static sites and frontends | **Vercel / Netlify / Cloudflare Pages** | Fast, free tier, automatic TLS | Free–$$ | Traffic or team needs |
| Full applications with a backend | **DigitalOcean** or **Hetzner** | A server you control, priced predictably | $$ | — |
| Databases | Managed database from the same provider, or **Supabase** free tier | Backups and updates handled for you | Free–$$ | Data volume |
| Files and media | Cloudflare R2 or provider object storage | Uploads, images | $ | — |
| DNS and CDN | **Cloudflare free** | Speeds the site up and hides the origin server | Free | — |

**Rules:** every hosting account is in the **company's** name, with billing on a company card. Every client system's hosting is recorded in that project's handover pack with cost, renewal date, and owner.

---

## 7. Monitoring

Without this section, the SLA in `[[Support and Maintenance SLA]]` cannot exist and no uptime figure may be published.

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Uptime monitoring | **UptimeRobot free** or **Better Stack free** | Checks the site every few minutes, alerts a named person when it stops | Free | More than the free number of monitors |
| Error monitoring | **Sentry free** | Tells you the app threw an error before the client does | Free | Event volume |
| **Certificate expiry alerts** | Included in most uptime tools — turn it on | 30-day warning before a certificate expires | Free | — |
| Performance | Google Lighthouse, plus Cloudflare analytics | Page speed, especially on slow connections | Free | Partner-tier clients |

> **Turn on uptime monitoring for Code Square's own site today.** Any future uptime claim must be backed by 90 days of measurement — see `[[Support and Maintenance SLA]]` §3.

---

## 8. Analytics

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Website analytics | **Google Analytics 4**, or **Plausible** if privacy matters to the client | Who visits, from where, what they do | Free / $ | — |
| Search visibility | **Google Search Console** | What Google actually sees. **Free, essential, and currently absent** — the site is invisible to crawlers (`stated`) | Free | Set up immediately |
| Facebook insights | Built into the page | Reach and engagement — but beware vanity metrics, `[[KPI Dashboard]]` §7 | Free | — |

---

## 9. CRM (customer relationship management — a record of every lead and deal)

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Start here | **A Google Sheet** | Date, name, source, what they want, stage, next step, next-step date, outcome | Free | Genuinely enough below ~30 leads a month |
| Then | **HubSpot free CRM** | Contacts, deals, pipeline stages, email history | Free | More than one person selling, or leads being forgotten |
| Never yet | Salesforce and similar | — | $$$ | Not for years |

> **The tool is not the problem — the absence of any record is.** `[[Foundation Brief]]` §2 Layer 4: the site promises a 24-hour response with no CRM behind it. A shared sheet solves that this afternoon.

---

## 10. Accounting and finance

| Need | Recommendation | What it is for | Band | Upgrade trigger |
|---|---|---|---|---|
| Bookkeeping | **A spreadsheet**, then a local accounting package an Egyptian accountant supports | Money in, money out, cash on hand, runway | Free–$$ | When an accountant asks for it, or when VAT registration applies |
| Invoicing | **Wave free** or invoices from the accounting tool | Professional, numbered, traceable invoices | Free | Volume |
| Expense records | Photograph every receipt into a dated folder | Tax, and knowing the real margin | Free | — |
| International payments | **Wise** or **Payoneer** | Gulf and overseas clients — Jeddah and Riyadh are `stated` service areas | Per transaction | — |

`❓ NEEDS FROM FOUNDER:` is there an accountant? A registered entity? Is VAT registration in place? See `[[Operating Cadence]]` §8.

---

## 11. File storage

| Need | Recommendation | Band |
|---|---|---|
| Company files | **Google Drive** (comes with Workspace) | $ |
| Structure | One folder per client → one folder per project → contracts / discovery / design / handover | Free |
| Rule | **Nothing important lives only on a laptop.** A laptop is a single point of failure with a battery | — |

---

## 12. Password and secret management — mandatory

**A password manager is not optional and not a "later" item.** It is the tool that makes the credential rule in `[[Project Kickoff Checklist]]` §6 physically possible.

| Need | Recommendation | What it is for | Band |
|---|---|---|---|
| Team password manager | **Bitwarden** (free tier is genuinely usable; Teams is cheap) | Store and share credentials without ever typing them into a chat | Free–$ |
| Per-client vaults | Bitwarden collections | One vault per client; access granted and removed per project | — |
| Secrets in code | Environment variables, plus the hosting provider's secret storage | **Never** in the repository | Free |

---

## 13. AI tooling

| Need | Recommendation | What it is for | Band | Note |
|---|---|---|---|---|
| Coding assistance | **Claude Code**, **GitHub Copilot**, or **Cursor** | Faster building, faster reading of unfamiliar code | $$ | Reviewed by a human before merging — the Definition of Done does not change |
| Writing and analysis | **Claude** or **ChatGPT** | Proposals, documentation, Arabic and English drafting | Free–$$ | Never publish machine translation — `[[Foundation Brief]]` rule 3 |
| Client-facing AI features | Per project | The site already sells LLM integration and RAG pipelines (`stated`) | Per use | Costs are per-usage and must be in the client's quote, not absorbed |

> **Client data rule:** do not paste a client's confidential data, personal data, or credentials into any AI tool without the client's written agreement. Put this in the contract. A company that sells AI integration must be visibly careful with data.

---

## 14. Security baseline — mandatory, not optional

These six rules are the floor. A company selling digital trust cannot fall below them.

| # | Rule | Why | Owner |
|---|---|---|---|
| 1 | **Password manager for everything.** No shared passwords in chat, in notes, in a spreadsheet, or in someone's head | One leaked chat backup exposes every client | TBD — assign |
| 2 | **2FA on every account** — email, GitHub, hosting, domain registrar, bank, Facebook, Google | The single highest-value control available, and it is free | TBD — assign |
| 3 | **No credentials in chat, ever** — WhatsApp, Messenger, email, screenshots, voice notes. If one arrives, treat it as compromised and rotate it | Chat history syncs to phones and clouds nobody audits | TBD — assign |
| 4 | **Quarterly access review** — list every tool, list who has access, remove anyone who should not | Ex-team members and finished projects accumulate access silently | TBD — assign |
| 5 | **Backup policy** — automated, stored off the production server, **and restored once to prove it works** | An untested backup is a rumour | TBD — assign |
| 6 | **Company-owned accounts** — domains, repositories, hosting, and cloud in the company's name, never a personal one | A personal account is one departure away from losing a client's system | TBD — assign |

Add rules 1–3 to the onboarding checklist for every new person and freelancer.

---

## 15. The starting stack — what to set up this month

In order, cheapest and highest-impact first:

- [ ] Domain + Google Workspace email — replaces the free Gmail address
- [ ] Bitwarden, with 2FA turned on everywhere
- [ ] GitHub Organization, repositories moved off any personal account
- [ ] UptimeRobot on Code Square's own site, and every client site
- [ ] Google Search Console for the website
- [ ] A Google Sheet CRM, with a named owner for the 24-hour response promise
- [ ] Google Drive folder structure
- [ ] Trello or Notion, one board per project
- [ ] Cloudflare in front of the site, free tier

Total cost: roughly the price of one Workspace seat. Everything else is free.

---

## 16. Open questions

| # | Question | Blocks |
|---|---|---|
| 1 | What tools are in use today, and what is already being paid for? | This entire file |
| 2 | Is there a company domain and professional email? | Credibility, §1 |
| 3 | Where does client code live today, and in whose account? | `[[Org and Roles]]` §6 |
| 4 | Is there a password manager at all? | The whole security baseline |
| 5 | Is there an accountant and a registered entity? | §10, `[[Operating Cadence]]` §8 |
| 6 | Who owns tool subscriptions and access reviews? | §14 |

Add these to `[[Open Questions and Decisions Needed]]`.

## Related
[[Org and Roles]] · [[Operating Cadence]] · [[KPI Dashboard]] · [[Project Kickoff Checklist]] · [[Quality Standards and Handover]] · [[Support and Maintenance SLA]] · [[Website and Technical Audit]] · [[Foundation Brief]]
