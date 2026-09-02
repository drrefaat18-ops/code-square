# _CLAUDE.md — Code Square Operations Vault

**Read this file first, every session, before touching anything.** These rules override default behaviour and any generic skill defaults.

---

## 0. What this vault is

The operating brain for **Code Square (CS)** — a software company in Port Said, Egypt, and an entity of the **M Tech Square** group. It holds the company's identity, market, offers, proof, marketing, sales, delivery, operations, and technical infrastructure in one place, so that any person or AI agent can pick up any part of the business without re-deriving it.

**The owner is a pharmacist**, not a marketer, engineer, or MBA. Every note must be readable by an intelligent person with no business or software background: define jargon inline on first use, lead with the consequence before the mechanism, prefer tables and checklists over essays.

**Working languages:** Arabic (Egyptian dialect for social and sales, Modern Standard for formal documents) and English (Gulf, enterprise, technical). Never machine-translate — write each language natively. Preserve Arabic verbatim when quoting the company's own published words.

---

## 1. The truth hierarchy — never break this

```
00-Source/  (immutable evidence)
      ↓
Foundation Brief.md  (canonical strategy — everything must agree with it)
      ↓
All other notes
```

1. **`00-Source/` is immutable.** The two evidence notes record what existed on 2026-09-02. Never rewrite them with strategy or new opinions. If the Facebook page or website changes, write a NEW dated evidence note; never overwrite an old one.
2. **`00-Source/Foundation Brief.md` is canonical.** If any note contradicts it, the brief wins — until the founder explicitly decides otherwise, at which point update the brief FIRST and then propagate.
3. Everything else is derived and may be rewritten as thinking improves.

---

## 2. Anti-fabrication — the hardest rule in this vault

This vault will be used to write proposals, ads, and case studies that go to real clients. A fabricated fact becomes a lie told to a customer.

**Never invent:** client names · revenue, headcount, or years in business · project results, percentages, or timelines · testimonials or quotes · awards or certifications · team member names or roles · prices, day rates, or margins · founding dates.

**Only these four clients exist** and only two are external: `M Tech Square Website` (internal) · `Techno Square Platform` (internal product) · `El Shoush Travel System` (external, B2B) · `Osama Sakr Manning Agency` (external, B2B). Do not add a fifth without evidence.

**When a fact is unknown:**
- Write `TBD` in the note, and
- Add the question to `[[Open Questions and Decisions Needed]]`, and
- In a case study or client-facing draft, write `❓ NEEDS FROM FOUNDER: <the exact question>`.

**Never claim absence from memory.** Before saying a note does not exist or creating a new one, search the vault by every plausible name and folder. Duplicate notes are vault rot.

---

## 3. Confidence labelling — required on every substantive claim

| Label | Means |
|---|---|
| `stated` | Evidenced in `00-Source/` or said directly by the founder |
| `verified` | Independently checked in this session — say what was observed and when |
| `researched` | External source — **must** carry a URL and a date |
| `proposed` | A recommendation invented by an agent. Never present as fact. |
| `TBD` | Unknown. Must also appear in Open Questions. |

---

## 4. Note format — every note, no exceptions

```yaml
---
date: YYYY-MM-DD
type: <profile|strategy|playbook|case-study|audit|reference|decision|source-evidence>
tags:
  - <topic>
ai-first: true
status: <draft|active|superseded|awaiting-founder-decision>
owner: <name or TBD>
---
```

Then an H1, then a `## For future Claude` section: 2–3 sentences saying what the note is and when a future session should read it. Then the content.

Cross-link liberally with `[[Wikilinks]]`. Linking to a note that does not exist yet is fine and desirable — it marks the gap.

---

## 5. Folder map

| Folder | Contains | Owner discipline |
|---|---|---|
| `00-Source/` | Immutable evidence + the canonical Foundation Brief | Never rewrite evidence |
| `01-Identity/` | Profile, positioning, messaging, voice, visual identity, values | Brand |
| `02-Market/` | ICP, personas, competition, market map, beachhead decision | Strategy |
| `03-Offers/` | Service catalog, offer ladder, pricing, proposal template, scoping | Commercial |
| `04-Marketing/` | Strategy, content system, social playbook, calendar, paid media, templates | Marketing |
| `05-Proof/` | Portfolio, case studies, permissions, testimonials | Proof |
| `06-Sales/` | Playbook, discovery script, objections, CRM, outbound, qualification | Sales |
| `07-Delivery/` | Delivery process, kickoff, quality, support SLA | Delivery |
| `08-Operations/` | Org and roles, tools, cadence, KPIs | Ops |
| `09-Technical/` | Website audit, remediation, SEO/AEO, analytics, infrastructure roadmap | Technical |
| `10-Group/` | M Tech Square and sister entities | Group |
| `plan/` | Legacy artifacts (the superseded 3-month plan PDF) | Read-only history |
| `Logs/` | Per-day append-only operation log | Never delete |

---

## 6. Standing decisions already made

- The old `plan/خطة_كود_سكوير_لأول_ثلاثة_شهور.pdf` is **superseded**, not adopted. Reference it as history only.
- The `$19 / $49 / $99` tiers on the SaaS infographic are **mockup art**. Never quote them as prices.
- **Banned phrases** (unfalsifiable, no proof behind them): أقوى فريق · أفضل شركة · حلول متكاملة · أحدث التقنيات · ثقة عملائنا · "Awwwards-tier" · "99.9% uptime" and "SLA Guarantees" (until a real SLA document exists) · "worldwide"/"globally" (until a non-Egypt/Gulf client exists).
- **Creative rule:** one idea per creative, maximum 15 words on the image. Detail goes in the caption.
- **Priority 0 gate:** no paid marketing spend until the expired TLS certificate and the non-rendering website are fixed. Traffic sent to a browser security warning is money burned.

---

## 7. Two known unresolved contradictions

Do not silently pick a side — surface them until the founder decides.

1. **Two methodologies published.** The website ships a 4-phase model (التأسيس → المعمارية → الهندسة → الإطلاق والتطوير); Facebook ships a 5-stage model (Discovery → User Analysis → UX/UI → Development → Testing & Launch). One must become canonical.
2. **Two colour systems.** The website uses navy `#001F3F` + gold `#D5B182` + Code Square purple `#A855F7`; the Facebook creatives use violet on near-black with no gold.

---

## 8. Propagation — never create in isolation

| When you write… | Also update… |
|---|---|
| Any new note | `index.md` and today's file in `Logs/` |
| A strategic decision | `Foundation Brief.md` and `Open Questions and Decisions Needed.md` |
| A new fact about a client or project | The relevant case study in `05-Proof/` |
| A resolved unknown | Remove it from Open Questions and replace `TBD` everywhere it appears |
| A new technical finding about the site | `09-Technical/Website and Technical Audit.md` |

---

## 9. Multi-agent rule

Two agents must never own the same file. When spawning a swarm, assign each agent an exclusive folder or explicit file list and say so in the prompt. Shared files (`index.md`, `log.md`, `Foundation Brief.md`, `Open Questions`) are written by the coordinating session only.
