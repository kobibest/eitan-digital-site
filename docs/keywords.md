# Keyword tracking

Source of truth for which keyword each article targets, and what Google Search Console shows for it.
Data comes from the Make scenario "Search Console API (Claude)" (property `https://digital.m-eitan.co.il/`):
`POST /v3/sites/https%3A%2F%2Fdigital.m-eitan.co.il%2F/searchAnalytics/query` with
`{"startDate":"...","endDate":"...","dimensions":["query","page"],"rowLimit":250}`.

## Weekly review (every Sunday morning run)
1. Pull the last 28 days by query+page. Log the top queries below (date, query, page, clicks, impressions, CTR, position).
2. Act on it:
   - Position 5 to 20 with impressions: strengthen that article (cover the exact query phrasing in an h2 or FAQ, add depth, internal links from related articles). Bump `updated`.
   - Many impressions, low CTR: rewrite `title` and `description` around the query.
   - Queries with impressions and no matching article: add to the backlog in `docs/blog.md`, top priority.
   - A query landing on the wrong page: add a clear internal link to the right page.
3. Changes to published articles also go to Kobi for approval before they reach `main`.
4. After publishing anything, resubmit the sitemap: `PUT /v3/sites/https%3A%2F%2Fdigital.m-eitan.co.il%2F/sitemaps/https%3A%2F%2Fdigital.m-eitan.co.il%2Fsitemap.xml`.

## Targets
| slug | primary keyword | secondary | status |
|---|---|---|---|
| `ai-customer-service-bot` | בוט AI לשירות לקוחות | צ'אטבוט לעסק, צ'אטבוט לשירות לקוחות, העברה לנציג אנושי, מאגר ידע לבוט | draft |
| `automation-roi` | החזר השקעה אוטומציה | כדאיות אוטומציה, ROI אוטומציה, תקופת החזר, חישוב חיסכון בשעות עבודה | draft |
| `business-process-weak-points` | ייעול תהליכים בעסק | נקודות תורפה בעסק, צווארי בקבוק, מיפוי תהליכים עסקיים | published |
| `connecting-business-systems` | חיבור בין מערכות | אינטגרציה בין מערכות, חיבור CRM להנהלת חשבונות, חיבור סליקה למערכת, אוטומציה בין מערכות | draft |
| `excel-to-system` | מעבר מאקסל למערכת | ניהול עסק באקסל, מאקסל למערכת ניהול, העברת נתונים מאקסל, חסרונות אקסל לניהול עסק | draft |
| `how-to-choose-crm` | איך לבחור CRM | מערכת CRM לעסק קטן, בחירת מערכת CRM, השוואת מערכות CRM, החלפת CRM | draft |
| `small-business-automation` | אוטומציה לעסק קטן | אוטומציות לעסקים, אוטומציה עסקית, כלי אוטומציה לעסקים, אוטומציה של משימות חוזרות | draft |
| `small-business-digitization` | דיגיטציה לעסק קטן | טרנספורמציה דיגיטלית לעסקים קטנים, דיגיטציה של עסק, תוכנית דיגיטלית לעסק, מעבר לעבודה דיגיטלית | draft |
| `system-adoption` | הטמעת מערכת בארגון | הטמעת מערכת מידע, ניהול שינוי בארגון, התנגדות עובדים לשינוי, הטמעת CRM, הדרכת עובדים על מערכת חדשה | draft |
| `whatsapp-bot-for-business` | בוט ווצאפ לעסק | בוט וואטסאפ, צ'טבוט לווצאפ, בוט ווצאפ AI, מענה אוטומטי בווצאפ | draft |
| `whatsapp-business-api-vs-app` | WhatsApp Business API | ווצאפ עסקי רשמי, ווצאפ ביזנס, וואטסאפ API, חסימת מספר ווצאפ | draft |

## Search Console log
- 2026-10-27: property verified, sitemap submitted 2026-10-24 (11 URLs, 0 indexed yet). No query data yet, the site is new.
