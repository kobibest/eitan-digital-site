# Blog: daily SEO articles

Source lives in `content/blog/<slug>.html` (JSON meta block + body HTML). `tools/blog.py` generates
`blog/<slug>.html`, `blog/index.html`, and the blog blocks in `sitemap.xml` and `llms.txt`.
`content/`, `tools/` and `docs/` are excluded from the deploy (`.vercelignore`). Always commit the generated files.

## Daily workflow (approval first, then publish)
1. Pick the next topic from the backlog below (or a better one found by keyword research). Skip anything already published (`ls content/blog`).
2. Research the Hebrew search intent: WebSearch for the keyword, look at what ranks, find what is missing there. Optionally use the hofit&goni `seo_meta` / `seo_schema` / `seo_audit` tools.
3. Write `content/blog/<slug>.html`. Latin kebab-case slug. Set `date` and `updated` to the publish day.
4. Run `python3 tools/blog.py`, render the page with Playwright and check mobile + desktop.
5. Send Kobi the draft in chat for approval: title, meta description, target keyword, and the full text. Do NOT publish yet.
6. Only after an explicit approval: apply requested edits, rebuild, commit, push to `main` (production). Unapproved drafts are never pushed to `main`.

## Writing rules
- Practical and genuinely useful: concrete steps, checklists, examples, a small table or calculation where it helps. 1,000 to 1,800 words.
- Hebrew that sounds like Kobi: direct, plain, "אתם" voice. No AI phrasing ("בעולם של היום", "חשוב לציין", "לסיכום,"), no hype, no em dashes.
- One primary keyword in `title`, `h1`, the first paragraph and one `h2`; related keywords used naturally. `description` up to about 155 characters.
- 5 to 8 `<h2 id="...">` sections (the TOC is built from them), plus 2 to 4 FAQ items in meta (they become FAQPage JSON-LD).
- Only real facts about Kobi's work (see `index.html`: the association of about 1,900 members, Eitan CRM, the conference system, his own office). Never invent clients, numbers, quotes or results.
- Link to a relevant service page where it fits (`/conferences`, `/whatsapp`, `/eitan`, `/#method`) and to earlier articles.
- Kobi is a "יועץ ארגוני מוסמך". Never "licensed".

## Topic backlog (Hebrew keyword in parentheses)
- [x] Weak points in business processes (ייעול תהליכים בעסק): published 2026-10-27 as business-process-weak-points
- [ ] Which tasks to automate first in a small business (אוטומציה לעסק קטן)
- [ ] WhatsApp bot for a business: what it can and cannot do (בוט ווצאפ לעסק)
- [ ] How to choose a CRM without regretting it a year later (איך לבחור CRM)
- [ ] When Excel stops being enough (מעבר מאקסל למערכת)
- [ ] Official WhatsApp Business API vs regular WhatsApp Business (ווצאפ עסקי API)
- [ ] Connecting systems: accounting, payments, CRM (חיבור בין מערכות / אינטגרציה)
- [ ] Managing a conference or retreat registration without spreadsheets (ניהול רישום לכנס)
- [ ] Automatic document reading and data entry (קליטת מסמכים אוטומטית)
- [ ] Digital transformation for small businesses: where to start (דיגיטציה לעסק קטן)
- [ ] How to calculate the ROI of automation (החזר השקעה אוטומציה)
- [ ] Getting a team to actually adopt a new system (הטמעת מערכת בארגון)
- [ ] Recurring payments and standing orders: avoiding failed charges (הוראות קבע / סליקה)
- [ ] AI bots for customer service: a practical guide (בוט AI לשירות לקוחות)
- [ ] Amendment 13 to the Privacy Protection Law for small businesses (תיקון 13 לחוק הגנת הפרטיות)
- [ ] Automatic reminders that cut no-shows (תזכורות אוטומטיות ללקוחות)
- [ ] Custom ERP vs off-the-shelf: when each makes sense (ERP מותאם אישית)
- [ ] Mapping a customer journey from lead to payment (מסע לקוח)
