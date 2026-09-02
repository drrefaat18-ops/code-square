---
date: 2026-09-02
type: remediation-plan
tags:
  - technical
  - website
  - priority-zero
  - code-square
ai-first: true
status: draft
owner: TBD
severity: blocker
confidence: mixed
---

# Remediation Plan — Priority Zero

## For future Claude

This is the **fix-this-week** plan derived from `[[Website and Technical Audit]]`. It covers only the blockers: the things that must be true before **any** marketing money, content push, or sales outreach makes sense. Longer-horizon work lives in `[[Digital Infrastructure Roadmap]]`.

Section 1 is written for the founder (a pharmacist, no technical background) and is enough to approve the work. Sections 2 onward are written for whoever holds server access, and are specific enough to execute without further research. Every task has an **acceptance test** — a command or check that produces a yes/no answer, so "done" is never a matter of opinion.

`owner: TBD` throughout — `[[Open Questions and Decisions Needed]]` must resolve who actually has server access before any of this starts.

---

## 1. The plain-language summary — what you are approving

**Right now your website is doing you active harm.** Not "underperforming" — harm. There are three separate problems and they are unrelated to each other, so fixing one does not fix the others.

**Problem 1 — the padlock expired.** Websites carry a certificate, a bit like a car licence, that tells the browser "this site is who it says it is". Yours ran out on **31 August**. Since that morning, every person who types your address gets a full red screen saying the site may be trying to steal from them. Most people leave without ever seeing a word you wrote. **Cost to fix: 20 minutes, zero money.** The certificates are free.

**Problem 2 — it renewed itself before, and nobody noticed it stopped.** These certificates last 90 days and are supposed to renew automatically. Yours did — until it did not, and there was no alarm. **Fix: turn the automatic renewal back on, and add a free service that emails you 21 days before the next one expires.** 1–2 hours.

**Problem 3 — Google cannot read your site.** This is the expensive one and it is not obvious, because the site looks perfect to you. Your site is built so that the page is assembled inside the visitor's browser after it arrives. A human browser does this fine. Google's reader, and ChatGPT's, usually do not — they receive an empty page and conclude you have nothing to say. **This is why nobody finds you.** It is not a marketing problem and no amount of posting will fix it. **Fix: a developer changes how the site is published so a finished page is sent instead of an empty one.** 3–8 days of developer time depending on the option chosen. My recommendation is the cheapest of the three options (see §4).

**Three smaller items are worth doing in the same week** because they take minutes: turning on file compression (makes the site meaningfully faster on Egyptian mobile, one line of configuration), publishing a proper crawler-instructions file, and **testing that your contact form actually sends email to somebody** — nobody has ever confirmed that it does, and the form publicly promises a reply within 24 hours.

**What this costs:** the certificate, the compression, the monitoring, and the crawler file cost **nothing but time**. The rendering fix costs developer days. Nothing here requires new software licences.

**What to say yes to:** all of Phase A (this week) and the recommended option in §4. Everything else can wait.

---

## 2. Order of operations

Do these in this order. Later steps depend on earlier ones being true.

| # | Task | ID | Time | Blocking? |
|---|---|---|---|---|
| **A1** | Renew the TLS certificate | SEC-01 | 20 min | 🔴 Blocks everything |
| **A2** | Fix or restore automatic renewal | SEC-02 | 1 h | 🔴 |
| **A3** | Add certificate-expiry + uptime monitoring | SEC-03 | 45 min | 🔴 |
| **A4** | Enable gzip/brotli compression | PERF-01 | 15 min | — |
| **A5** | Serve a real `robots.txt` and stop the soft-404 catch-all | CRAWL-02, CRAWL-04 | 45 min | — |
| **A6** | Test the contact form end to end; name its owner | CONT-02 | 30 min | 🔴 Blocks lead gen |
| **A7** | Resolve the `og:url = codesquare.com` question | CRAWL-09 | 30 min | Blocks domain decision |
| **A8** | Link Facebook → website and website → Facebook | CONT-07 | 20 min | — |
| **B1** | **Make the site readable by search engines** (prerender/SSR) | CRAWL-01 | 3–8 days | 🔴 Blocks all SEO/AEO |
| **B2** | Publish `sitemap.xml` | CRAWL-03 | 2 h | Depends on B1 |
| **B3** | Add canonical + `og:image` + Arabic meta description | CRAWL-05, CRAWL-10, CONT-03 | 2 h | Depends on B1 |
| **B4** | Self-host the Spline viewer instead of `unpkg.com` | PERF-03 | 30 min | — |
| **B5** | Capture a Lighthouse baseline and record it | PERF-04 | 30 min | Depends on A1 |

**Phase A is one working day of effort in total.** Phase B is the real project.

---

## 3. Phase A — the fixes that take minutes

### A1 · Renew the TLS certificate 🔴

**What is wrong.** `verified` 2026-09-02: the certificate on `mtechsquare.com` was issued by Let's Encrypt, valid `2026-06-02 → 2026-08-31 18:57 UTC`. It has expired. Server is `nginx/1.24.0 (Ubuntu)`.

**Why it happened is the important part.** The certificate is Let's Encrypt, which means it was almost certainly obtained with `certbot`, which means automatic renewal *was* set up at some point and has since broken. Three usual causes:
1. The `certbot.timer` systemd unit is disabled or the server was rebuilt without it.
2. Renewal succeeded but nginx was never reloaded, so it kept serving the old file from memory. (This one is nasty — the new certificate is sitting on disk unused.)
3. The HTTP-01 challenge now fails because a redirect or firewall rule blocks `/.well-known/acme-challenge/`.

**Check which one before fixing** — it tells you what to repair in A2:

```bash
sudo certbot certificates          # is a newer cert already on disk?
sudo systemctl status certbot.timer
sudo journalctl -u certbot --since "60 days ago" | tail -50
```

**The fix.** If a valid newer certificate is already on disk, this is just a reload:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Otherwise renew properly. With the nginx plugin (edits and reloads nginx for you):

```bash
sudo certbot renew --nginx
# or, if the certificate lineage is damaged, reissue from scratch:
sudo certbot --nginx -d mtechsquare.com -d www.mtechsquare.com
```

If the HTTP-01 challenge is blocked, use webroot instead:

```bash
sudo certbot certonly --webroot -w /var/www/html \
  -d mtechsquare.com -d www.mtechsquare.com
sudo systemctl reload nginx
```

Ensure nginx does not intercept the challenge path — this block must sit **above** any catch-all `location /`:

```nginx
location ^~ /.well-known/acme-challenge/ {
    root /var/www/html;
    default_type "text/plain";
    try_files $uri =404;
}
```

**Acceptance test** — all three must pass:

```bash
# 1. A normal, validating request succeeds (no -k flag)
curl -sSI https://mtechsquare.com/code-square/ | head -1
#    expect: HTTP/1.1 200 OK   (today this fails with SEC_E_CERT_EXPIRED)

# 2. The expiry date is in the future, ~90 days out
echo | openssl s_client -connect mtechsquare.com:443 -servername mtechsquare.com 2>/dev/null \
  | openssl x509 -noout -dates
#    expect: notAfter = a date roughly 90 days from today

# 3. Full chain is valid from an independent checker
#    https://www.ssllabs.com/ssltest/analyze.html?d=mtechsquare.com  → grade A or better
```

Also open the site in Chrome **and** Safari on a real phone and confirm a padlock, no warning.

**Owner:** TBD — whoever holds server SSH access. **Effort:** 20 minutes.

---

### A2 · Fix automatic renewal 🔴

**What is wrong.** The renewal automation exists (this is a Let's Encrypt certificate) but did not run, or ran and did not take effect.

**The fix.** Modern certbot installs ship a systemd timer. Confirm it is enabled and that a *deploy hook* reloads nginx after every renewal — the missing reload is the most common silent failure:

```bash
sudo systemctl enable --now certbot.timer
sudo systemctl list-timers certbot.timer      # confirm the next run is scheduled

# The deploy hook: runs only when a certificate was actually renewed
sudo tee /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh >/dev/null <<'SH'
#!/bin/sh
nginx -t && systemctl reload nginx
SH
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
```

If the server has no systemd timer, a cron entry does the same job:

```cron
0 3 * * * /usr/bin/certbot renew --quiet --deploy-hook "nginx -t && systemctl reload nginx"
```

**Acceptance test.** A dry run must succeed without touching the live certificate:

```bash
sudo certbot renew --dry-run
#    expect: "Congratulations, all simulated renewals succeeded"
systemctl list-timers certbot.timer
#    expect: a NEXT time within the next 24 hours
```

**Owner:** TBD. **Effort:** 1 hour including verification.

---

### A3 · Monitoring, so this can never happen silently again 🔴

This is the item that actually matters. The certificate expiring was a mistake; **nobody finding out for two days was the failure.** All three tools below have free tiers sufficient for a site this size.

`researched` 2026-09-02 — free-tier options:

| Need | Tool | Free tier | URL |
|---|---|---|---|
| **Uptime + certificate expiry** | **UptimeRobot** | 50 monitors, 5-minute checks, SSL expiry alerts included | https://uptimerobot.com |
| Uptime (open-source, self-host) | **Uptime Kuma** | free, self-hosted; certificate-expiry notifications built in | https://github.com/louislam/uptime-kuma |
| **Certificate expiry, dedicated** | **Let's Encrypt expiry email** | free; register an email on the certificate — Let's Encrypt emails at 20 days and 7 days | set with `certbot update_account --email ...` |
| Frontend error monitoring | **Sentry** | free developer tier, ~5k errors/month | https://sentry.io |
| Independent certificate scan | **SSL Labs** | free, manual | https://www.ssllabs.com/ssltest/ |

**Minimum viable setup — do all four, they take 45 minutes total:**

1. **UptimeRobot HTTPS monitor** on `https://mtechsquare.com/code-square/`, 5-minute interval, alerting to **two** channels: the founder's email *and* a WhatsApp/Telegram number. One channel is not monitoring; it is hope.
2. **Enable UptimeRobot's SSL expiry notification** — it warns at 30/14/7 days.
3. **Register a real email on the Let's Encrypt account** so the certificate authority itself warns you independently of your own infrastructure:
   ```bash
   sudo certbot update_account --email <owner@domain>
   ```
   Use a **company address, not a personal Gmail that could be deprioritised** — and one that more than one person reads.
4. **A keyword monitor**, not just a status monitor. Once B1 ships, configure UptimeRobot to check that the response body contains the string `Code Square`. A status-only monitor returns "up" for a blank page. `proposed`

**Acceptance test.**
- Deliberately pause the site (or point the monitor at a deliberately wrong path) and confirm an alert arrives on **both** channels within 10 minutes. **An untested alarm is not an alarm.**
- Confirm the SSL-expiry alert is switched on in the monitor's settings.

**Owner:** TBD. **Effort:** 45 minutes. **Cost:** 0.

---

### A4 · Enable compression — the best minute-for-minute return on this page

**What is wrong.** `verified`: requested `Accept-Encoding: gzip, br`; the server returned no `Content-Encoding` header. Everything is being sent uncompressed. On a site carrying megabytes of JavaScript to Egyptian mobile users, this is pure waste.

**The fix.** In the nginx `http {}` block:

```nginx
gzip              on;
gzip_vary         on;
gzip_comp_level   6;
gzip_min_length   1024;
gzip_proxied      any;
gzip_types
    text/plain text/css text/xml
    application/javascript application/json application/xml
    application/xml+rss image/svg+xml
    font/woff font/woff2 application/wasm;
```

Note `application/wasm` — the Skia/CanvasKit stack ships WebAssembly, which compresses well and is otherwise large.

Brotli compresses ~15–20% better than gzip but needs the `ngx_brotli` module, which is not in the stock Ubuntu nginx package. **Ship gzip today; treat brotli as a Phase 1 nice-to-have.** `proposed`

**Acceptance test:**

```bash
curl -sSI -H "Accept-Encoding: gzip, br" \
  https://mtechsquare.com/code-square/polyfills.a7fe1c37468e57a1.js \
  | grep -i "content-encoding"
#    expect: Content-Encoding: gzip
#    today: (no output)
```

Then compare `Content-Length` before and after — expect roughly a 70% reduction on JS and CSS.

**Owner:** TBD. **Effort:** 15 minutes.

---

### A5 · A real `robots.txt`, and stop the catch-all soft-404

**What is wrong.** `verified`: `/robots.txt`, `/sitemap.xml`, `/llms.txt` and `/nonexistent-abc123.txt` all return `HTTP 200` with the Angular HTML page. The nginx configuration has a blanket `try_files $uri $uri/ /index.html` that swallows everything.

**The fix.** Two nginx changes. First, serve real static files at those paths before the SPA fallback:

```nginx
location = /robots.txt   { root /var/www/mtechsquare; try_files $uri =404; add_header Content-Type text/plain; }
location = /sitemap.xml  { root /var/www/mtechsquare; try_files $uri =404; add_header Content-Type application/xml; }
location = /llms.txt     { root /var/www/mtechsquare; try_files $uri =404; add_header Content-Type text/plain; }
```

Second, stop the SPA fallback from catching file requests. Requests with a file extension that do not exist should 404 honestly, while route paths still fall through to the app:

```nginx
# Real files with extensions must 404, not fall through to index.html
location ~* \.(txt|xml|json|js|css|map|png|jpg|svg|woff2?|ico)$ {
    try_files $uri =404;
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# Application routes still fall through
location / {
    try_files $uri $uri/ /index.html;
}
```

`robots.txt` content is specified in full — including the AI-crawler directives — in `[[SEO and AEO Foundations]]`. Do not invent one here; use that file.

**Acceptance test:**

```bash
curl -sS https://mtechsquare.com/robots.txt | head -3
#    expect: plain text beginning "User-agent:"  — NOT "<!doctype html>"

curl -sS -o /dev/null -w "%{http_code}\n" https://mtechsquare.com/nonexistent-abc123.txt
#    expect: 404   (today: 200)

curl -sS -o /dev/null -w "%{http_code}\n" https://mtechsquare.com/code-square/
#    expect: 200   (routes must still work — regression check)
```

That last check matters: it is easy to fix the soft-404 and break the app's deep links in the same commit.

**Owner:** TBD. **Effort:** 45 minutes.

---

### A6 · Prove the contact form works, and name its owner 🔴

**What is wrong.** `stated` — the form promises a reply within 24 hours (*"سيقوم فريقنا التقني بمراجعة التفاصيل والتواصل معك خلال 24 ساعة"*). Nothing in the vault names the inbox, the owner, or confirms that submissions arrive at all. The email address is injected at runtime and was not in the bundles — **nobody currently knows which address it points to.**

**The fix.** This is not a code change; it is a test and a decision.

1. Submit the form as a real prospect would, from a phone, on mobile data, with a distinctive project name (`TEST-2026-09-02-<random>`).
2. Confirm the email arrives. Note **which inbox**, and check spam.
3. If it does not arrive: the form is a silent lead shredder and this becomes the highest-priority item after the certificate. Common causes on a VPS are an unconfigured `sendmail`, or a shared-host mailer being rejected by Gmail's spam filters (a Gmail-hosted destination like `codesquareteam1@gmail.com` will often silently drop mail from an unauthenticated VPS). Fix by routing through a transactional email provider — **Brevo** (300 emails/day free) or **Resend** (3,000/month free) — rather than the server's own mailer. `researched` 2026-09-02: https://www.brevo.com/pricing/ · https://resend.com/pricing
4. **Name the owner of that inbox in `[[Open Questions and Decisions Needed]]`.** A published 24-hour SLA with no named owner is worse than no SLA.
5. If the 24-hour promise cannot be honoured, **change the copy this week** to a promise that can be. An unmet published promise costs more than a modest one.

**Acceptance test.** A test submission arrives in a named inbox within 5 minutes, is not in spam, and a named person confirms in writing that they own responses to it.

**Owner:** TBD — this one needs the founder, not the developer. **Effort:** 30 minutes.

---

### A7 · Resolve the `codesquare.com` question

**What is wrong.** `verified`: the page's `og:url` is `https://codesquare.com`. That domain does not serve this site. Either someone bought it and never pointed it, or it is aspirational placeholder text sitting in production.

**Why it is urgent.** Facebook, WhatsApp and LinkedIn use `og:url` as the canonical identity of a shared link. Every share Code Square makes currently declares that its true home is a domain it may not own. If a competitor or squatter holds it, Code Square's own marketing is advertising for someone else.

**The fix.** Run a WHOIS lookup and check whether the domain is registered and by whom. Then, one of:
- **Owned by Code Square** → point it at the site and treat it as the domain decision in `[[SEO and AEO Foundations]]`.
- **Not owned, available** → this is a live input to the domain decision; buy it if the recommendation there is followed.
- **Owned by someone else** → **remove the `og:url` tag immediately**, or set it to the real address. Do not leave it.

**Acceptance test.** `og:url` in the served HTML resolves to a domain Code Square controls, or the tag is removed.

**Owner:** founder. **Effort:** 30 minutes.

---

### A8 · Connect the two channels

**What is wrong.** `stated` — the Facebook page lists no website; the site does not link the Facebook page. The 74 followers have never been given a route to the four projects.

**The fix.** Do this only **after A1 passes.** Sending 74 followers to a certificate warning is worse than sending them nowhere.
1. Add the website URL to the Facebook page's Website field and to the About section.
2. Add a link to the Facebook page in the site footer.
3. Add the WhatsApp number to the site (see CONT-01 in `[[Website and Technical Audit]]`).

**Acceptance test.** The Facebook page shows a clickable website link that loads without a warning; the site footer links back.

**Owner:** founder / whoever manages the page. **Effort:** 20 minutes.

---

## 4. Phase B1 — making the site readable by search engines and AI

This is the substantial one, and it needs a real decision. **Read this section before approving anything.**

### The problem restated

`verified`: the HTML the server sends contains **zero characters** of visible text. All content is assembled by JavaScript in the visitor's browser. Google states it renders JavaScript, but rendering is queued, resource-limited and unreliable for heavy applications — and **AI answer engines are far more limited.** Perplexity, ChatGPT's browsing crawler and Claude's fetcher predominantly read the raw HTML response. A site whose HTML is empty has, to them, no content at all.

`researched` 2026-09-02: Google's own guidance on JavaScript SEO acknowledges the render queue and recommends server-side rendering or pre-rendering where content matters — https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics

### The three options

| | **Option 1 — Prerender at build time** | **Option 2 — Angular SSR (Angular Universal / `@angular/ssr`)** | **Option 3 — Rebuild as static** |
|---|---|---|---|
| **What it is** | At build time, run each route through a headless browser and save the finished HTML. Serve those files. The app still hydrates and behaves identically afterwards. | A Node.js server renders each page on request, then hands it to the browser to take over. | Abandon Angular for a static site generator (Astro, Next static export, Eleventy). |
| **Angular support** | Built in. `ng build --prerender` / the `prerender` builder. No new stack. | Built in. `ng add @angular/ssr`. | Full rewrite. |
| **Runtime cost** | **None.** Output is plain HTML files served by the existing nginx. | Requires a **Node.js process running permanently** on the server, plus a process manager, plus monitoring for that process. | None. |
| **New failure modes** | Almost none — if the build fails you ship the old files. | **A new always-on service that can crash, leak memory, or go down independently of nginx.** Given that this team just lost a certificate to a silent automation failure, adding a daemon to babysit is a real risk. | The rewrite itself. |
| **Handles the 3D/Spline content?** | Yes — the 3D loads client-side after hydration, exactly as now. Prerendering captures the text; the animation still runs for humans. | Yes, but the heavy WebGL/WASM libraries must be carefully guarded against running during server render (no `window`, no `document`), which is the usual source of SSR pain on animation-heavy sites. | Yes. |
| **Effort** | **3–5 developer days** including route list, CI wiring and QA | 5–10 days, plus ongoing operational overhead | 4–8 weeks, discards work that is good |
| **Fits a marketing site with ~10 static routes?** | **Perfectly** | Overkill | Overkill |

### Recommendation for THIS site — `proposed`

> **Option 1: prerender at build time.**

The reasoning:

1. **The content is static.** Vision, philosophy, methodology, seven services, four projects, contact form. Nothing on this site is personalised or changes per request. SSR exists to render per-request content. There is none here. Paying an always-on Node server to re-render identical HTML thousands of times is spending operational risk for no benefit.
2. **The operating model cannot support a daemon today.** The team just discovered a 90-day automated task had been failing silently. Adding a permanently-running Node service — which needs pm2 or systemd, log rotation, memory monitoring, and a restart policy — increases the number of things that can break silently from one to several. **Match the architecture to the operations capability you actually have.** Prerendering adds a build step and zero runtime components.
3. **The output is a set of HTML files nginx already knows how to serve** — with the correct caching headers that are already configured.
4. **It is reversible.** If Code Square later builds a client dashboard or per-user pages, adding SSR at that point is a normal upgrade. Prerendering does not paint you into a corner.

**The trade-off you accept:** every content change requires a rebuild and deploy. For a site whose HTML was last modified two months ago, that is not a constraint. If content editing becomes frequent — say, a blog in Phase 3 of `[[Digital Infrastructure Roadmap]]` — revisit the decision then, and prefer a headless CMS with a build webhook over switching to SSR.

**When Option 2 would become right:** if Code Square adds logged-in areas, per-client dashboards, or content that must be fresh within minutes. None of those are on the roadmap for six months.

**When Option 3 would become right:** never, on current evidence. The Angular work and the 3D craft are genuine assets. Do not throw them away to solve a rendering problem that has a three-day fix.

### Implementation sketch — Option 1

```bash
# Angular 17+ ships the prerender builder
ng add @angular/ssr        # installs the toolchain; you use only the prerender output
# Then in angular.json, the prerender target with an explicit route list:
```

```json
{
  "prerender": {
    "builder": "@angular-devkit/build-angular:prerender",
    "options": {
      "routesFile": "routes.txt",
      "discoverRoutes": true
    }
  }
}
```

`routes.txt` — one line per route, both languages:

```
/code-square/
/code-square/services
/code-square/work
/code-square/projects
/code-square/contact
/code-square/privacy
/code-square/terms
```

**The three things that will actually go wrong, and how to handle them** — every one of these is a `window`/`document` access during a build with no browser:
1. **Spline / Three.js / Rapier / CanvasKit initialisation.** Guard every one behind `afterNextRender()` (Angular 16+) or an `isPlatformBrowser()` check. They must never run during prerender.
2. **GSAP ScrollSmoother.** Same guard. It touches `document` on import in some configurations — import it lazily.
3. **The runtime-injected email address** (noted in the evidence file). If it comes from a browser-only source it will be missing from prerendered HTML. Move it into the build or the template.

**Acceptance test** — this is the whole point of the exercise, so test it properly:

```bash
# 1. The served HTML now contains real text
curl -sS https://mtechsquare.com/code-square/ | grep -c "مهندسو أنظمة"
#    expect: 1 or more   (today: 0)

# 2. Body text length is substantial, with scripts stripped
curl -sS https://mtechsquare.com/code-square/ \
  | python -c "import sys,re;h=sys.stdin.read();b=h[h.find('<body'):];b=re.sub(r'<script.*?</script>','',b,flags=re.S);t=re.sub(r'<[^>]+>',' ',b);print(len(re.sub(r'\s+',' ',t).strip()))"
#    expect: >2000   (today: 0)

# 3. The philosophy statements — the best copy the company owns — are in the HTML
curl -sS https://mtechsquare.com/code-square/ | grep -o "architect for scale"

# 4. Google's own renderer agrees
#    Search Console → URL Inspection → Test Live URL → View Crawled Page
#    expect: the HTML tab shows the content, not an empty <app-root>

# 5. The site still works for humans — regression, do not skip
#    Load on a real phone. 3D scene animates. Navigation works. Form submits.
```

Test 5 is the one people skip and regret. Prerendering can produce perfect HTML and a broken hydration that leaves the page frozen for real visitors.

**Owner:** TBD — needs the Angular developer who built the site. **Effort:** 3–5 days.

---

## 5. Phase B — the remaining items

### B2 · `sitemap.xml`
Generate from the same route list used for prerendering, so the two can never drift. Structure and content specified in `[[SEO and AEO Foundations]]`. Submit to Google Search Console and Bing Webmaster Tools once live (see `[[Analytics and Measurement Setup]]`).
**Acceptance:** `curl -sS https://mtechsquare.com/sitemap.xml | head -2` returns XML; Search Console reports it as read with N URLs discovered.
**Effort:** 2 hours.

### B3 · Canonical, `og:image`, Arabic description
Add per-page `<link rel="canonical">`, an `og:image` (1200×630, navy ground, Code Square wordmark, purple accent `#A855F7` — see `[[Visual Identity]]`), `og:image:alt`, `twitter:card`, and an **Arabic** meta description alongside the English one on Arabic routes. Exact tag patterns are in `[[SEO and AEO Foundations]]`.
**Acceptance:** paste the URL into Facebook's Sharing Debugger (https://developers.facebook.com/tools/debug/) and see a card with an image and the correct title.
**Effort:** 2 hours.

### B4 · Self-host the Spline viewer
Download `@splinetool/viewer@1.0.94` and serve it from the site's own assets directory. Removes a third-party single point of failure and one extra DNS + TLS handshake on the critical path.
**Acceptance:** no `unpkg.com` in the served HTML; the 3D scene still loads.
**Effort:** 30 minutes.

### B5 · Lighthouse baseline
Once A1 and A4 are done, run Lighthouse (mobile profile, simulated slow 4G) and **write the numbers into `[[KPI Dashboard]]`**: Performance score, LCP, CLS, INP, and total transferred bytes. This also finally resolves the `NEEDS VERIFICATION` on the ~7.5 MB payload figure.
**Acceptance:** four numbers recorded with a date.
**Effort:** 30 minutes.

---

## 6. Monitoring — the section that makes this permanent

The certificate was not the failure. **The absence of an alarm was the failure.** Three layers, all free:

| Layer | What it watches | Tool | Alert goes to |
|---|---|---|---|
| **Availability** | Is the site up, and does its HTML contain the word "Code Square"? | UptimeRobot, 5-min interval, keyword mode | Founder email **+** WhatsApp/Telegram |
| **Certificate** | Days until expiry | UptimeRobot SSL alert (30/14/7 days) **+** Let's Encrypt's own expiry emails **+** `certbot renew --dry-run` in a weekly cron | Two different people |
| **Errors** | JavaScript crashes for real visitors | Sentry free tier | Developer |
| **Search health** | Crawl errors, indexing failures, manual actions | Google Search Console + Bing Webmaster (free, email alerts on) | Founder + developer |

**Two rules that matter more than the tool choice:**
1. **Every alert goes to at least two people and at least two channels.** A single email address is a single point of failure, and it is exactly how two days passed unnoticed.
2. **Test each alarm once when you set it up.** Break the thing deliberately, confirm the message arrives, then fix it. An untested alarm is decoration.

Add a **quarterly 15-minute check** to the operating calendar: run `certbot renew --dry-run`, load the site on a phone, run the acceptance tests in this note. `proposed`

---

## 7. What must NOT happen until Phase A is complete

- **No paid advertising.** Every pound spent today buys a click onto a security warning.
- **No Facebook posts driving to the website.** Fix A1 first.
- **No outreach, cold email, or proposal that includes the URL.**
- **No new content production for the site** — there is nowhere for it to be found.

The full spending gate is stated at the end of `[[Digital Infrastructure Roadmap]]`.

---

## Related
[[Website and Technical Audit]] · [[SEO and AEO Foundations]] · [[Analytics and Measurement Setup]] · [[Digital Infrastructure Roadmap]] · [[Foundation Brief]] · [[Open Questions and Decisions Needed]] · [[KPI Dashboard]] · [[Paid Media Plan]] · [[Marketing Strategy]]
