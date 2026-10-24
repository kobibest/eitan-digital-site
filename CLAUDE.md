# digital.m-eitan.co.il — איתן | דיגיטציה ארגונית

Static site (plain HTML/CSS/JS, no framework), deployed on Vercel (project `eitan-systems`).
Every push to `main` deploys to production.

## Structure
- Hebrew pages (RTL, default): `index.html`, `conferences.html`, `whatsapp.html`, `eitan.html`
- English pages: `en/*.html` (LTR, each has `hreflang` pairs with its Hebrew twin; keep both in sync)
- Legal (bilingual, needed for Meta Tech Provider / Eitan Connect): `privacy.html`, `terms.html`, `data-deletion.html` — keep the footer `legal-line` on all pages
- `styles.css` base, `extra.css` additions, `site.js` (contact form via Web3Forms + injects the "English" switcher on Hebrew pages)
- SEO: `sitemap.xml` (with xhtml:link alternates), `robots.txt`, `llms.txt`, JSON-LD in each page head
- `vercel.json`: cleanUrls, headers, build command

## Build step (share images)
`build_og.py` runs at build time and generates `og.png` (Hebrew) and `og-en.png` (English) with Pillow,
then rewrites `/og.png` → `/og-en.png` inside `en/*.html`. In source, English pages may point to either.
The committed `og.png` is only a fallback. Never hand-write binary files as base64.
Local test: `OG_LOCAL_FONTS=/path/to/ttf-dir python3 build_og.py` (expects hebrew-500/700/900.ttf, latin-500/700/900.ttf).

## Content rules
- Hebrew copy: human, precise, no AI-sounding phrasing, no em dashes in English copy.
- Kobi is a "יועץ ארגוני מוסמך" (certified organizational consultant). Never call him a "licensed" mortgage advisor.
- Demo WhatsApp bot: https://wa.me/97286430500
- Contact: kobi@eitan-m.co.il
