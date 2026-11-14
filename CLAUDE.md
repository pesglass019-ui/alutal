# ALUTAL website: standing instructions

This repo is the website of **شركة الوتال للألومنيوم والزجاج وتشكيل المعادن (ALUTAL)**, Jeddah.
Static site: `index.html` + `img/`. Every push to `main` is deployed to GitHub Pages by `.github/workflows/pages.yml` (1–2 min).
Live: https://www.alutal.com.sa (old https://pesglass019-ui.github.io/alutal redirects there)

For every change, follow the `alutal-site` skill (`.claude/skills/alutal-site/SKILL.md`). Always reply in Arabic, short and friendly. The owner is not a developer.

## Be ready to act immediately
When the owner says anything like «اضف مشروع», «اضف الصور على الموقع», «طوّر الموقع» or «صفحة جديدة», do it directly in this repo: edit, test with `scripts/check.js`, commit, push, then give the live link. No need to ask how; the skill has the steps.

## What to ask the owner for (only what is missing)
- **Photos:** as attachments **in a new message**, not while Claude is still working on a previous request. Photos sent mid-turn are not saved to disk. If a photo isn't on disk, ask for it again in a new message.
- **For each project:** name, district and city, client, type of works. If available, also area, contract value and year.
- **For a new page:** page name, what should appear on it, and photos if any.
- **No personal names on the site** (owners, sheikhs, engineers, staff). Private projects are titled generically: «فيلا خاصة — الحي», «عمارة سكنية خاصة — الحي», «قصر خاص». Company names (clients/contractors) are fine.
- **Never write "since 1986" or a founding year.** ALUTAL is a new name; the team has 30+ years of experience. Use that wording.
- Never invent numbers, clients or locations. Describe scope only from what the photos show.

Template to send the owner when info is missing:
> أرسل الصور كمرفقات في رسالة جديدة، ومعها: اسم المشروع، الحي والمدينة، العميل، نوع الأعمال (وإن توفرت: المساحة، القيمة، السنة).

## Open items (update this list when they change)
- **Custom domain: done.** Live at https://www.alutal.com.sa (DNS at Sahara Net, `CNAME` file in repo, Enforce HTTPS on). Keep the `CNAME` file; never touch the Zoho mail records.

Project history (what was done and decided, in Arabic): `HISTORY.md`. Append to it after each change session.
