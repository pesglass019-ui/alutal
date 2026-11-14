# ALUTAL website: standing instructions

This repo is the website of **شركة الوتال للألومنيوم والزجاج وتشكيل المعادن (ALUTAL)**, Jeddah.
Static site: `index.html` + `img/`. Every push to `main` is deployed to GitHub Pages by `.github/workflows/pages.yml` (1–2 min).
Live: https://pesglass019-ui.github.io/alutal

For every change, follow the `alutal-site` skill (`.claude/skills/alutal-site/SKILL.md`). Always reply in Arabic, short and friendly. The owner is not a developer.

## Be ready to act immediately
When the owner says anything like «اضف مشروع», «اضف الصور على الموقع», «طوّر الموقع» or «صفحة جديدة», do it directly in this repo: edit, test with `scripts/check.js`, commit, push, then give the live link. No need to ask how; the skill has the steps.

## What to ask the owner for (only what is missing)
- **Photos:** as attachments **in a new message**, not while Claude is still working on a previous request. Photos sent mid-turn are not saved to disk. If a photo isn't on disk, ask for it again in a new message.
- **For each project:** name, district and city, client, type of works. If available, also area, contract value and year.
- **For a new page:** page name, what should appear on it, and photos if any.
- Never invent numbers, clients or locations. Describe scope only from what the photos show.

Template to send the owner when info is missing:
> أرسل الصور كمرفقات في رسالة جديدة، ومعها: اسم المشروع، الحي والمدينة، العميل، نوع الأعمال (وإن توفرت: المساحة، القيمة، السنة).

## Open items (update this list when they change)
- **Custom domain www.alutal.com.sa:** the domain is at **Sahara Net (صحاري نت)**; mail is on Zoho. The owner was asked to add DNS `CNAME www → pesglass019-ui.github.io`, keeping the Zoho MX/TXT records. Only **after** they confirm the record exists, add a `CNAME` file containing `www.alutal.com.sa` and push. Then tell them to enter the domain in Settings → Pages → Custom domain and tick Enforce HTTPS. Adding the file earlier breaks the live site.
- **مطعم دوّار السعادة (`id:'dawar'`):** city/district unknown; `loc` currently says «واجهة مطعم». Ask the owner.
- **عمارة تركي الغامدي:** assumed to be the red-brick building (`img/turki-1.webp`). The owner did not object.
