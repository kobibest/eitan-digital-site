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
| `customer-journey-lead-to-payment` | מסע לקוח | מיפוי מסע לקוח, תהליך מכירה בעסק, ניהול לידים, משפך מכירות | published 2026-11-06 |
| `member-management-system-organization` | מערכת לניהול חברים | ניהול חברים בעמותה, CRM לעמותות, ניהול דמי חבר, מערכת לניהול ארגון | published 2026-11-08 |

## Search Console log
- 2026-10-27: property verified, sitemap submitted 2026-10-24 (11 URLs, 0 indexed yet). No query data yet, the site is new.
- 2026-11-01 (28 days to 2026-10-31): first data. 0 clicks overall, 25 URLs submitted, 0 reported indexed in the sitemap report (impressions show some pages are already served).
  - Pages by impressions: /conferences 10 (avg pos 29.7), /eitan 7 (pos 4.3), blog/small-business-automation 7 (pos 71.6), /privacy 6, /terms 6, /en 5, /en/conferences 4 (pos 11.5), /, /blog, /whatsapp, blog/connecting-business-systems (pos 14.3), blog/whatsapp-business-api-vs-app (pos 28) 3 each.
  - Queries: "אוטומציה לעסקים קטנים" 6 impr pos 69.5 (small-business-automation); "איך לבצע אינטגרציה בין מערכת הסליקה לבין מערכת הנהלת החשבונות שלי?" 2 impr pos 5 (connecting-business-systems); "הטמעת מערכת מידע חדשה בארגון" 2 impr pos 19 (system-adoption); "רישום לכנסים" 3 impr pos 59.7 and "מערכת רישום לכנסים" 1 impr pos 73 (/conferences); "וואטסאפ עסקי יתרונות וחסרונות" 1 impr pos 14 and "וואטסאפ ביזנס" 2 impr pos 35 (whatsapp-business-api-vs-app); "שילוב מערכות תשלום באתר" 1 impr pos 33; "איך לעשות אוטומציה לעסק" 1 impr pos 84.
  - Approved and applied 2026-11-01 (updated dates bumped). Actions: clearing-to-accounting FAQ in connecting-business-systems; "מערכת מידע חדשה" phrasing in system-adoption; a pros/cons section in whatsapp-business-api-vs-app. /eitan ranks well (pos 4.3), so the Eitan CRM review was written to support it.
- 2026-11-08 (28 days to 2026-11-07): still 0 clicks; 31 URLs submitted. Impressions grew on the blog.
  - Pages: blog/small-business-automation 24 impr (pos 72.7), blog/whatsapp-business-api-vs-app 16 (pos 23.6, was 28), blog/small-business-digitization 14 (pos 16.2, new), blog/connecting-business-systems 12 (pos 12.7, was 14.3), /conferences 10 (29.7), blog/automatic-customer-reminders 9 (25.3), blog/automation-roi 9 (37.3), /eitan 8 (4.3), blog/ai-customer-service-bot 7 (67.6), blog/system-adoption 6 (25.3), /en/conferences 6 (10.2), /en/eitan 5 (6.4), blog/recurring-payments-failed-charges 1 (pos 8).
  - Movers after the 2026-11-01 changes: clearing-to-accounting query 6 impr pos 6.2 (was 2 impr pos 5); "שילוב מערכות תשלום באתר" pos 15.5 (was 33); "וואטסאפ עסקי יתרונות וחסרונות" pos 12.3 (was 14); "הטמעת מערכת מידע חדשה בארגון" pos 16 (was 19).
  - New in 5-20: "דיגיטציה עסקית" 14 impr pos 16.2 (small-business-digitization); "אוטומציה למתחילים" pos 18 (small-business-automation). Near: "וואטסאפ ביזנס api" pos 21.3, "תוכנה לניהול וואטסאפ עסקי" pos 24.
  - Approved and applied 2026-11-08: "דיגיטציה עסקית" phrasing in small-business-digitization; a beginners FAQ in small-business-automation; an FAQ on software to run WhatsApp Business as a team in whatsapp-business-api-vs-app.
