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
| `ai-customer-service-bot` | בוט AI לשירות לקוחות | צ'אטבוט לעסק, צ'אטבוט לשירות לקוחות, העברה לנציג אנושי, מאגר ידע לבוט | published 2026-10-28 |
| `automation-roi` | החזר השקעה אוטומציה | כדאיות אוטומציה, ROI אוטומציה, תקופת החזר, חישוב חיסכון בשעות עבודה | published 2026-10-28 |
| `business-process-weak-points` | ייעול תהליכים בעסק | נקודות תורפה בעסק, צווארי בקבוק, מיפוי תהליכים עסקיים | published |
| `connecting-business-systems` | חיבור בין מערכות | אינטגרציה בין מערכות, חיבור CRM להנהלת חשבונות, חיבור סליקה למערכת, אוטומציה בין מערכות | published 2026-10-28 |
| `excel-to-system` | מעבר מאקסל למערכת | ניהול עסק באקסל, מאקסל למערכת ניהול, העברת נתונים מאקסל, חסרונות אקסל לניהול עסק | published 2026-10-28 |
| `how-to-choose-crm` | איך לבחור CRM | מערכת CRM לעסק קטן, בחירת מערכת CRM, השוואת מערכות CRM, החלפת CRM | published 2026-10-28 |
| `small-business-automation` | אוטומציה לעסק קטן | אוטומציות לעסקים, אוטומציה עסקית, כלי אוטומציה לעסקים, אוטומציה של משימות חוזרות | published 2026-10-28 |
| `small-business-digitization` | דיגיטציה לעסק קטן | טרנספורמציה דיגיטלית לעסקים קטנים, דיגיטציה של עסק, תוכנית דיגיטלית לעסק, מעבר לעבודה דיגיטלית | published 2026-10-28 |
| `system-adoption` | הטמעת מערכת בארגון | הטמעת מערכת מידע, ניהול שינוי בארגון, התנגדות עובדים לשינוי, הטמעת CRM, הדרכת עובדים על מערכת חדשה | published 2026-10-28 |
| `whatsapp-bot-for-business` | בוט ווצאפ לעסק | בוט וואטסאפ, צ'טבוט לווצאפ, בוט ווצאפ AI, מענה אוטומטי בווצאפ | published 2026-10-28 |
| `whatsapp-business-api-vs-app` | WhatsApp Business API | ווצאפ עסקי רשמי, ווצאפ ביזנס, וואטסאפ API, חסימת מספר ווצאפ | published 2026-10-28 |
| `automatic-customer-reminders` | תזכורות אוטומטיות ללקוחות | תזכורת לתור בווצאפ, אי הגעה לתור, הפחתת ביטולים, הודעות SMS ללקוחות | published 2026-10-28 |
| `conference-management-system-review` | מערכת לניהול כנסים | מערכת רישום לכנסים, ניהול נופש לארגון, שיבוץ חדרים לכנס, ניהול אירועים לארגונים | published 2026-10-30 |
| `eitan-crm-mortgage-advisors-review` | CRM ליועצי משכנתאות | מערכת לניהול משרד ייעוץ משכנתאות, תוכנה ליועצי משכנתאות, מערכת איתן, ניהול תיקי משכנתא | published 2026-11-01 |
| `official-whatsapp-eitan-connect-review` | ווצאפ רשמי לארגונים | חיבור ווצאפ ל-CRM, WhatsApp Business API לארגון, הודעות ווצאפ אוטומטיות, Eitan Connect | published 2026-11-02 |
| `recurring-payments-failed-charges` | הוראות קבע | תשלומים חוזרים, חיוב שנכשל, הוראת קבע בכרטיס אשראי, גבייה חודשית | published 2026-11-03 |
| `privacy-amendment-13-business-systems` | תיקון 13 לחוק הגנת הפרטיות | הגנת פרטיות לעסקים, אבטחת מידע לעסק קטן, מאגר מידע עסק, מדיניות פרטיות לעסק | published 2026-11-04 |
| `custom-erp-vs-off-the-shelf` | ERP מותאם אישית | מערכת ERP לעסק, ERP או מערכת מדף, מערכת ניהול לארגון, פיתוח מערכת ניהול | published 2026-11-05 |

## Search Console log
- 2026-10-27: property verified, sitemap submitted 2026-10-24 (11 URLs, 0 indexed yet). No query data yet, the site is new.
- 2026-11-01 (28 days to 2026-10-31): first data. 0 clicks overall, 25 URLs submitted, 0 reported indexed in the sitemap report (impressions show some pages are already served).
  - Pages by impressions: /conferences 10 (avg pos 29.7), /eitan 7 (pos 4.3), blog/small-business-automation 7 (pos 71.6), /privacy 6, /terms 6, /en 5, /en/conferences 4 (pos 11.5), /, /blog, /whatsapp, blog/connecting-business-systems (pos 14.3), blog/whatsapp-business-api-vs-app (pos 28) 3 each.
  - Queries: "אוטומציה לעסקים קטנים" 6 impr pos 69.5 (small-business-automation); "איך לבצע אינטגרציה בין מערכת הסליקה לבין מערכת הנהלת החשבונות שלי?" 2 impr pos 5 (connecting-business-systems); "הטמעת מערכת מידע חדשה בארגון" 2 impr pos 19 (system-adoption); "רישום לכנסים" 3 impr pos 59.7 and "מערכת רישום לכנסים" 1 impr pos 73 (/conferences); "וואטסאפ עסקי יתרונות וחסרונות" 1 impr pos 14 and "וואטסאפ ביזנס" 2 impr pos 35 (whatsapp-business-api-vs-app); "שילוב מערכות תשלום באתר" 1 impr pos 33; "איך לעשות אוטומציה לעסק" 1 impr pos 84.
  - Approved and applied 2026-11-01 (updated dates bumped). Actions: clearing-to-accounting FAQ in connecting-business-systems; "מערכת מידע חדשה" phrasing in system-adoption; a pros/cons section in whatsapp-business-api-vs-app. /eitan ranks well (pos 4.3), so the Eitan CRM review was written to support it.
