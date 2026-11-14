---
name: alutal-site
description: Maintain the ALUTAL company website (index.html + img/ in this repo, live on GitHub Pages). Use whenever the user asks to add or edit a project, add photos, change text, add a service, add a new page/section, fix something on the site, or publish/deploy it. Triggers include Arabic requests such as "اضف مشروع", "اضف صور", "عدّل", "صفحة جديدة", "انشر الموقع".
---

# ALUTAL website

Single-file bilingual (Arabic first, English second) static site.

- `index.html`: all CSS, HTML views and JS data.
- `img/*.webp`: every image, referenced by name without extension (`'zahra-1'` → `img/zahra-1.webp`).
- `.github/workflows/pages.yml`: deploys `index.html` + `img/` (+ `CNAME` if present) to GitHub Pages on every push to `main`.
- Live URL: https://pesglass019-ui.github.io/alutal (custom domain www.alutal.com.sa once DNS is set).

The user writes in Arabic (often Gulf/Levantine dialect) and is not a developer. Reply in Arabic, short, with exact clicks when they must do something.

## Golden rules

1. **No invented facts.** Areas, values, counts, years, clients and locations come only from the user or their documents. Describe scope only from what is visible in the photos. If a location is unknown, ask; don't guess.
2. **Every visible string is bilingual.** In HTML: `<span data-l="ar">…</span><span data-l="en">…</span>`. In JS data: `['عربي','English']`.
3. **Spell names exactly as the user writes them.** Example: ميناء صعبر (Saabar), not زعبر.
4. **Images in chat are only usable if saved to disk.** Images arrive under the session's `images/` folder (e.g. `…/images/6.jpg`) only when sent in a fresh message, not mid-turn. If you can't find the file, ask the user to resend it in a new message.
5. Run the check script before publishing. Then commit and push to `main`; the workflow deploys within 1–2 minutes.

## Adding a project (most common task)

1. **Convert the photos.** Each project gets a short id prefix, numbered from 1.
   ```bash
   bash .claude/skills/alutal-site/scripts/add_images.sh <prefix> <photo1> <photo2> ...
   # → img/<prefix>-1.webp, img/<prefix>-2.webp ... (max 1400px, quality 80)
   ```
   For small or blurry photos (under about 800px), upscale first with `scripts/upscale.py`. Its header explains the model download.

2. **Add an entry to the `P` array** in `index.html` (`const P=[`). Put it where it should appear; order = display order.
   ```js
   {id:'uniqueId',cat:'residential',feat:1,img:['prefix-2','prefix-1'],
    t:['اسم المشروع','Project name'],loc:['الحي، المدينة','District, City'],
    facts:[['client',['العميل','Client']],['system',['النظام','System']]],
    kv:['Curtain wall','ACP'],
    scope:[['بند العمل بالعربي.','Scope line in English.']]},
   ```
   - `cat` must be one of the `CATS` keys: `facade` · `commercial` · `gov` · `residential` · `art` · `metal`.
   - `facts` labels are keys of `LBL`: `client` · `area` · `value` · `units` · `period` · `system` and others (see `const LBL`). Values are `['ar','en']` or a plain string for numbers like `'7,200 m²'`.
   - `kv`: 1–3 short English tags shown on the card.
   - The first image in `img` is the card cover. Put the best exterior shot first.
   - `feat:1` is informational. The home page featured list is the array in `renderStatic()`: `$('#featGrid').innerHTML=[...]`. It holds exactly 6 ids; the first two get the large tiles.
   - No photos yet? Use `img:[],soon:1`. The card then shows "صور المشروع قريباً", and those cards sort last.

3. **Check, commit, push:**
   ```bash
   node .claude/skills/alutal-site/scripts/check.js      # must print: errors [] and no OVERFLOW
   git add -A && git commit -m "Add <project> project" && git push origin main
   ```

## Other edits

- **Services:** the `S` array (`code, img[], t, d, sp[[ar,en,value]]`). The home tiles use indices in `HOME_TILES`.
- **Specs tables:** `SYS` (aluminum systems), `G` (glass cards).
- **Team numbers:** `TEAM`.
- **Contact form options:** `FORM_TYPES`.
- **Static text** (hero, about, contact details) is plain HTML inside the `<div class="view" id="v-…">` blocks.
- **Hero stats:** `.stats` block in `#v-home`.

## Adding a new page

Pages are hash-routed views. To add one, e.g. `#careers`:

1. Add the view before `<!-- ============ ` of the next view, or after the contact view:
   ```html
   <div class="view" id="v-careers">
     <header class="phead"><div class="wrap">
       <div class="eyebrow"><span data-l="ar">…</span><span data-l="en">…</span></div>
       <h1><span data-l="ar">…</span><span data-l="en">…</span></h1>
       <p><span data-l="ar">…</span><span data-l="en">…</span></p>
     </div></header>
     <section><div class="wrap"> … </div></section>
   </div>
   ```
2. Add `'careers'` to `const VIEWS=[…]`, and add a title to the `titles` object inside `route()`.
3. Add a nav link in `<nav class="nav" id="nav">`, and in the footer list if relevant: `<a href="#careers">…</a>`.
4. Reuse existing classes instead of new CSS: `.split`, `.tiles`/`.tile`, `.grid` + `card()`, `.matgrid`/`.mat`, `.timeline`, `.chips`, `.tbl-wrap`/`.tbl`, `.btn btn-primary`/`.btn-line`. New colours must use the tokens (`--bg --panel --line --fg --muted --accent`), so dark and light themes keep working.
5. Add the view name to the loop in `scripts/check.js`, then run it.

## Design notes (keep consistent)

- Dark graphite theme by default, light theme via `prefers-color-scheme` / `[data-theme]`. Accent is glass-cyan `--accent`.
- Fonts: Readex Pro (Arabic display), IBM Plex Sans Arabic (body), Archivo (Latin), IBM Plex Mono (spec labels). In Arabic, mono/letter-spacing is switched off on labels, because it breaks letter joining.
- Use logical CSS (`inset-inline-start`, `padding-inline`, etc.), never left/right. The page flips with `dir`.
- Must not scroll horizontally at 390px wide.

## Custom domain

When DNS is ready (`CNAME www → pesglass019-ui.github.io`), create a file `CNAME` in the repo root containing `www.alutal.com.sa`, and push. The user also enters the domain in Settings → Pages → Custom domain and ticks Enforce HTTPS. Never touch the Zoho MX/TXT mail records.
