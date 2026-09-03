---
date: 2026-09-02
type: reference
tags:
  - identity
  - visual-identity
  - design-system
  - code-square
ai-first: true
status: draft
owner: TBD
---

# Visual Identity — Code Square

## For future Claude

This note holds the authoritative colour tokens, typography, logo rules, and social template specs for Code Square. Read it before designing anything — a post, a deck, a page, a proposal cover. The colour values below are copied verbatim from the compiled website CSS in [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]]; that file is the source, this file is the working system.

> **Jargon defined once.** *Token* = a named design value (a colour, a font, a spacing unit) used everywhere instead of typing the raw value, so one change updates everything. *Hex value* = the `#RRGGBB` code that names an exact colour. *Contrast ratio* = how readable text is against its background; `4.5:1` is the accessibility minimum for body text.

---

## 1. Colour tokens (stated — authoritative, verbatim from the compiled site CSS)

```css
/* ── Ground ────────────────────────────────── */
--navy:            #001F3F;   /* primary ground, also <meta theme-color> */
--navy-dark:       #0A0F1F;
--navy-deep:       #050a14;

/* ── Group accent (M Tech Square) ──────────── */
--gold:            #D5B182;
--gold-bright:     #E8C9A0;

/* ── Neutrals ──────────────────────────────── */
--white:           #FFFFFF;
--text-muted:      rgba(255,255,255,.55);

/* ── Per-entity accents ────────────────────── */
--code-accent:     #A855F7;   /* ← CODE SQUARE purple */
--techno-accent:   #FDD017;   /* Techno Square */
--online-accent:   #17A2B8;   /* Online Techno Square */
--msquare-accent:  #1E40AF;   /* M Square */
--digital-accent:  #00A3B1;   /* Digital Square */

/* ── Surfaces & effects ────────────────────── */
--glass-bg:        rgba(255,255,255,.03);
--glass-border:    rgba(213,177,130,.2);
--neon-glow:       0 0 15px rgba(213,177,130,.3);

/* ── Type ──────────────────────────────────── */
--font-sans:       "Playfair Display", serif;
--font-arabic:     "Tajawal", sans-serif;
```

### Role assignment for Code Square (proposed)

| Role | Token | Use for |
|---|---|---|
| Ground / background | `--navy` `#001F3F` | Every dark surface. This is the brand's floor. |
| Deeper ground | `--navy-dark` `#0A0F1F`, `--navy-deep` `#050a14` | Layering, depth, section separation |
| **Primary accent** | `--code-accent` `#A855F7` | Code Square's own colour — CTAs, active states, highlights, the "this is CS" signal |
| Group furniture | `--gold` `#D5B182` | Borders, dividers, group lockup, "part of M Tech Square" markers |
| Primary text | `--white` `#FFFFFF` | Headlines and body on navy |
| Secondary text | `--text-muted` `rgba(255,255,255,.55)` | Captions, labels, metadata — **never body copy** |
| Surface | `--glass-bg` + `--glass-border` | Cards, panels |

### Accessibility notes (proposed — verify before shipping)

| Pair                                 | Approx. ratio | Verdict                                                                                     |
| ------------------------------------ | ------------- | ------------------------------------------------------------------------------------------- |
| `#FFFFFF` on `#001F3F`               | ~15.9:1       | ✅ Excellent                                                                                 |
| `#D5B182` on `#001F3F`               | ~7.9:1        | ✅ Passes for body and headings                                                              |
| `#A855F7` on `#001F3F`               | ~3.6:1        | ⚠️ **Large text and UI elements only.** Not for body copy or small labels.                  |
| `rgba(255,255,255,.55)` on `#001F3F` | ~6.5:1        | ✅ For labels only, not paragraphs                                                           |
| `#FFFFFF` on `#A855F7`               | ~3.5:1        | ⚠️ Fails for small text. Use `#001F3F` text on purple buttons instead, or enlarge the type. |

**Rule (proposed):** purple is a *signal*, not a text colour. Never set body copy in `#A855F7`.

---

## 2. The palette conflict — and the recommendation

**The documented conflict (stated).**

| | Website | Facebook creatives |
|---|---|---|
| Ground | Navy `#001F3F` | Near-black |
| Accent | Purple `#A855F7` | Violet |
| Gold group furniture | Present (`#D5B182`) | **Absent entirely** |
| Overall read | Premium, group-connected, engineered | Generic dark tech template |

A prospect who sees a Facebook post and then the website sees two different companies. This is the visual half of the coherence problem in [[Foundation Brief]] §2, Layer 2.

**Recommendation (proposed — decision required from the founder).**

> **Adopt the website tokens as canonical and rebuild all social templates on them.**

Reasons:
1. The website tokens are the *only* system defined in code, with a full per-entity structure. Facebook's palette is undocumented and was chosen post-by-post.
2. Navy + gold + purple ties Code Square to the M Tech Square group, which is a genuine credibility asset. Near-black violet ties it to nothing and looks like every template.
3. It is cheaper. The site does not change; only the social templates do, and those need rebuilding anyway (see §5).
4. It resolves the conflict permanently instead of maintaining two systems.

**The rejected alternative:** formally splitting the group look from the CS look. Rejected because a 74-follower company cannot afford to spend recognition on maintaining two visual systems, and the group connection is an asset rather than a constraint.

**Migration rule (proposed):** from the decision date onward, every new creative uses the canonical tokens. Do not retroactively redo old posts — republish only what is still being actively linked.

---

## 3. Typography (stated — the four fonts detected on the live site)

| Font | Role | Where |
|---|---|---|
| **Playfair Display** (serif) | Display / headlines, Latin | `--font-sans` in the site CSS. Hero headlines, section titles, big statements. |
| **Tajawal** (sans-serif) | **All Arabic**, headlines and body | `--font-arabic`. The only Arabic face. Never substitute. |
| **Syne** | Accent / technical labels, Latin | Detected on site. Use for small caps labels, status tags, navigation. |
| **Cormorant Garamond** (serif) | Editorial secondary, Latin | Detected on site. Long-form editorial and pull quotes only. |

### Rules (proposed)

- **Maximum two Latin faces in any single piece.** The site currently loads four; a social creative that uses four is unreadable. Default pairing: **Playfair Display** (headline) + **Syne** (label/UI). Reserve Cormorant Garamond for long editorial pieces.
- **Arabic is always Tajawal**, at every weight. Do not pair Arabic with a display serif — Playfair has no Arabic coverage, and the fallback will be an unbranded system font.
- **Fallback stacks must be written explicitly**, or Arabic silently falls back to Times on some devices:
  ```css
  font-family: "Playfair Display", Georgia, "Times New Roman", serif;
  font-family: "Tajawal", "Segoe UI", Tahoma, Arial, sans-serif;
  font-family: "Syne", "Helvetica Neue", Arial, sans-serif;
  ```
- **Body copy is never Playfair Display.** Serif display faces at small sizes on a dark ground are hard to read on a phone.
- **Minimum sizes:** 16px body on web; 32px equivalent minimum for any text placed inside a social image.
- **Arabic line height** runs looser than Latin — set `1.8` for Arabic body, `1.5` for Latin.

---

## 4. Logo usage

**What exists (verified — 2026-09-02):** a `CODE SQUARE` wordmark with the lockup line `YOU IMAGINE ... WE CREATE`. The folder `Code Square visual assets/` contains one Illustrator source file, 13 SVG files, and eight PNG exports; [[Brand Assets Library]] records their verified paths, dimensions, and visible contents.

### Verified asset inventory & variants

| Variant | Files | Best for |
|---|---|---|
| **Full-colour horizontal logo** | [Asset 4.svg](../Code%20Square%20visual%20assets/SVG/Asset%204.svg) · [Asset 4.png](../Code%20Square%20visual%20assets/3x/Asset%204.png) | SVG has a transparent canvas; PNG has a white background. |
| **All-white horizontal logo** | [Asset 3.svg](../Code%20Square%20visual%20assets/SVG/Asset%203.svg) · [Asset 3.png](../Code%20Square%20visual%20assets/3x/Asset%203.png) | Use the SVG on dark surfaces; the PNG is white on white. |
| **All-black horizontal logo** | [Asset 2.svg](../Code%20Square%20visual%20assets/SVG/Asset%202.svg) · [Asset 2.png](../Code%20Square%20visual%20assets/3x/Asset%202.png) | Light backgrounds. |
| **Coloured `CS` monogram** | [Asset 13 logo.svg](../Code%20Square%20visual%20assets/SVG/SVG/Asset%2013%20logo.svg) | Horizontal canvas, not a ready-made square favicon. |
| **Square social artwork on navy** | [Asset 8.svg](../Code%20Square%20visual%20assets/SVG/Asset%208.svg) · [Asset 8.png](../Code%20Square%20visual%20assets/3x/Asset%208.png) | Full lockup and tagline; test legibility at the target profile size. |

See [[Brand Assets Library]] for full file inventory and direct links.

### Rules (proposed)

| Rule | Detail |
|---|---|
| **Clear space** | Minimum clear space on all four sides = the cap-height of the letter `C` in `CODE`. Nothing enters that zone. |
| **Minimum size** | Proposed: 120px wide on screen; 25mm wide in print. Below that, test the `CS` monogram rather than the full lockup. |
| **Backgrounds** | Navy `#001F3F` is the default. White and near-black are acceptable. Never place the logo on a photograph without a solid or heavily darkened panel behind it. |
| **Colour variants** | Available: full colour (`Asset 4`), all-white (`Asset 3`), all-black (`Asset 2`), and coloured `CS` monogram (`Asset 13`). `Asset 8` is the full lockup on a navy square. |
| **Tagline line** | `YOU IMAGINE ... WE CREATE` appears **only inside the logo lockup**. It never becomes a headline, a caption, a post opener, or an email signature line. See [[Brand Voice and Tone]] §6.4. |
| **Never** | Stretch, skew, rotate, recolour outside the palette, add drop shadows or outer glows, place on a busy background, or recreate the wordmark by typing it in a different font. |
| **Group lockup** | When Code Square appears alongside M Tech Square, the group mark sits in gold `#D5B182` and CS in purple `#A855F7`. Never both in the same colour. |
| **Avatar / favicon** | Candidate assets exist, but suitability is **TBD**. Test [Asset 8.png](../Code%20Square%20visual%20assets/3x/Asset%208.png) as an avatar and export a square favicon from [Asset 13 logo.svg](../Code%20Square%20visual%20assets/SVG/SVG/Asset%2013%20logo.svg); do not claim legibility until tested at 32×32 px. |

---

## 5. The creative rule that fixes the current infographics

**The problem (stated).** The seven service infographics posted on 30 May each carry **8 numbered bullets on one dark image**. On a phone, in a feed, that text is physically unreadable. Result: 1–4 reactions, several posts with zero comments.

**The rule (from [[Foundation Brief]] §8, mandatory):**

> **One idea per creative. Maximum 15 words on the image. All detail moves to the caption.**

Practically:

| Constraint | Value |
|---|---|
| Ideas per image | 1 |
| Words on the image | ≤ 15 |
| Bullets on the image | ≤ 3, and only if there are no headline words competing |
| Minimum type size on the image | 32px equivalent — readable at thumbnail size |
| Logo on the image | Once, small, in a fixed corner |
| Body detail | Caption, always — not the image |
| Emoji on the image | None (see [[Brand Voice and Tone]] §5) |

**Conversion of the existing 8-bullet infographics (proposed):** each becomes **eight separate posts or one carousel of eight slides**, one point per slide. The content is already written; only the packaging changes. This costs nothing and multiplies the usable inventory.

---

## 6. Social template specs (proposed)

All three templates: ground `#001F3F`, accent `#A855F7`, gold `#D5B182` for furniture only, Tajawal for Arabic, Playfair Display or Syne for Latin.

### 6.1 Feed post — 1080 × 1080

| Zone | Spec |
|---|---|
| Safe margin | 80px on all sides — nothing but background outside it |
| Headline | 1 line, ≤ 8 words, Tajawal Bold (AR) or Playfair Display (EN), white, ~72px |
| Sub-line (optional) | 1 line, ≤ 7 words, `--text-muted`, ~40px |
| Accent element | One purple rule, dot, or underline. One only. |
| Logo | Bottom-left, 140px wide, white variant |
| Gold | A single 1px `#D5B182` border or a thin bottom rule. Nothing more. |
| Total word count | **≤ 15** |
| Forbidden | Numbered bullet lists, paragraphs, stock photography, emoji, more than two type sizes |

### 6.2 Carousel — 1080 × 1350, 5–10 slides

| Slide | Content |
|---|---|
| **1 — Hook** | The problem, as a question. ≤ 10 words. Largest type in the set. |
| **2 — Context** | Who has this problem and why it hurts. ≤ 20 words. |
| **3…n−2 — One point per slide** | One idea each, ≤ 20 words. This is where the old 8-bullet infographics unpack. |
| **n−1 — Proof** | The project, the screenshot, the number. Never skip this slide. |
| **n — Next step** | One named action + the website URL. Not "DM us for info". |

Fixed furniture on every slide: slide counter (`3 / 8`) top-right in `--text-muted`; a thin purple progress rule along the bottom; the logo on slide 1 and the final slide only.

### 6.3 Story — 1080 × 1920

| Zone | Spec |
|---|---|
| Top 250px | Empty — platform UI covers it |
| Bottom 350px | Empty — reply bar and sticker zone |
| Middle band | All content lives here |
| Headline | ≤ 8 words, ~90px |
| Interaction | One poll, question sticker, or link sticker. One only. |
| Words total | **≤ 12** — stories are read in under 3 seconds |
| Logo | Small, top-left, below the safe zone |

---

## 7. Imagery and 3D

| Asset type | Rule |
|---|---|
| **Product screenshots** | The strongest available asset and currently unused on social. Always on a navy panel with a subtle gold border. Real screens only — never a mockup pretending to be a client system. |
| **3D / Spline scenes** | Genuine craft the company owns and a real differentiator. But the site loads ~7.5 MB of JS for it. Keep 3D as a **hero moment only**, never on every page or in feed creatives. See [[Website and Technical Audit]]. |
| **Stock photography** | Banned. Handshakes, generic laptops, and smiling offices actively signal low credibility. |
| **Team photos** | Would be a real asset. None were found in the reviewed source set on 2026-09-02; whether any exist elsewhere is **TBD**. |
| **Glassmorphism** | Belongs to Online Techno Square's visual language. Code Square uses it sparingly, as surfaces only, not as a theme. |

---

## 8. Open visual decisions

| Decision | Status |
|---|---|
| Website palette adopted as canonical over the Facebook palette | **Recommended above — awaiting founder approval.** [[Open Questions and Decisions Needed]] |
| Logo source file (SVG) and variant set | **Resolved.** One `.ai` file and 13 SVG files catalogued in [[Brand Assets Library]] |
| Square avatar / favicon mark | **TBD.** Candidate assets exist, but a legibility test and favicon export are still needed. |
| Whether the `YOU IMAGINE ... WE CREATE` lockup is retained long-term | Proposed: retain in the lockup, demote everywhere else |
| Licensed weights for Tajawal / Playfair / Syne / Cormorant Garamond | TBD — confirm licensing before print or paid use |
| Brand asset library location and owner | Location resolved: `Code Square visual assets/`, catalogued in [[Brand Assets Library]]. Owner remains **TBD**. |

---

## Related
[[Brand Assets Library]] · [[Foundation Brief]] · [[2026-09-02 - Website Evidence (mtechsquare.com-code-square)]] · [[2026-09-02 - Facebook Page Evidence]] · [[Brand Positioning]] · [[Brand Voice and Tone]] · [[Messaging Framework]] · [[Company Profile]] · [[Website and Technical Audit]] · [[Editorial Calendar - First 90 Days]] · [[Open Questions and Decisions Needed]]
