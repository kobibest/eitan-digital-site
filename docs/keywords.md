# Keyword tracking

Source of truth for which keyword each article targets, and what Google Search Console shows for it.
Data comes from the Make scenario "Search Console API (Claude)" (property `https://digital.m-eitan.co.il/`):
`POST /v3/sites/https%3A%2F%2Fdigital.m-eitan.co.il%2F/searchAnalytics/query` with
`{"startDate":"...","endDate":"...","dimensions":["query","page"],"rowLimit":250}`.

## Daily status report (every morning run, since 2026-11-18)
Kobi wants a full daily review of the site in Google Search. Each run:
1. Pull the last 28 days by page and by query+page, plus the last 7 days by page, and the sitemap status (submitted vs indexed).
2. Compare with the previous log entry: clicks, impressions, average position per page, queries that moved, new queries.
3. Report to Kobi in Hebrew: totals, top pages, top queries, notable movers, indexing status, and what was done about it. Note that Search Console data lags by 2 to 3 days.
4. Log a short dated entry below.

## Weekly review (every Sunday morning run)
1. Pull the last 28 days by query+page. Log the top queries below (date, query, page, clicks, impressions, CTR, position).
2. Act on it:
   - Position 5 to 20 with impressions: strengthen that article (cover the exact query phrasing in an h2 or FAQ, add depth, internal links from related articles). Bump `updated`.
   - Many impressions, low CTR: rewrite `title` and `description` around the query.
   - Queries with impressions and no matching article: add to the backlog in `docs/blog.md`, top priority.
   - A query landing on the wrong page: add a clear internal link to the right page.
3. Since 2026-11-18, changes to published articles are self-checked like new articles and published without waiting for approval; they are listed in the daily report.
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
| `digital-signature-for-business` | חתימה דיגיטלית לעסק | חתימה דיגיטלית על מסמכים, חתימה אלקטרונית, טפסים דיגיטליים, מסמכים לחתימה ללקוחות | published 2026-11-09 |
| `landing-page-leads-to-crm` | דף נחיתה לידים | חיבור טופס ל-CRM, ניהול לידים, מקור ליד, טופס לידים באתר | published 2026-11-10 |
| `google-workspace-email-migration` | מעבר ל-Google Workspace | מייל ארגוני, העברת מיילים לדומיין, גוגל וורקספייס לעסק, תיבת מייל משותפת | published 2026-11-11 |
| `sms-into-business-system` | קליטת SMS למערכת | SMS ל-CRM, העברת SMS אוטומטית, הודעות SMS ללקוחות, ניהול SMS בעסק | published 2026-11-12 |
| `mailing-from-inside-the-system` | מערכת דיוור לעסק | דיוור ללקוחות, דיוור לחברי ארגון, דיוור מתוך CRM, ניוזלטר לעסק | published 2026-11-13 |
| `building-an-erp-system` | בניית מערכת ERP | פיתוח מערכת ERP, יצירת מערכת ERP, אפיון מערכת ERP, הטמעת ERP | published 2026-11-15 |
| `whatsapp-business-app-guide` | וואטסאפ ביזנס | ווצאפ ביזנס, WhatsApp Business, וואטסאפ עסקי, הגדרת וואטסאפ ביזנס | published 2026-11-16 |
| `replacing-erp-integrator` | החלפת אינטגרטור ERP | החלפת ספק מערכת, החלפת ספק תוכנה, העברת מערכת לספק אחר, שותף יישום ERP | published 2026-11-17 |
| `collecting-documents-from-clients` | איסוף מסמכים מלקוחות | קבלת מסמכים מלקוחות, רשימת מסמכים חסרים, קליטת מסמכים אוטומטית, העלאת מסמכים ללקוחות | published 2026-11-18 |
| `small-business-digitization-case-study` | דיגיטציה בעסק קטן מקרה בוחן | דיגיטציה עסקית דוגמה, אוטומציה למשרד ייעוץ משכנתאות, משרד דיגיטלי | published 2026-11-19 |
| `data-migration-to-new-system` | העברת נתונים למערכת חדשה | הסבת נתונים, ניקוי נתונים, מעבר CRM, ייבוא נתונים למערכת | published 2026-11-20 |

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
- 2026-11-15 (28 days to 2026-11-14): still 0 clicks; 37 URLs submitted.
  - small-business-digitization: "דיגיטציה עסקית" 44 impr pos 14.1 (was 14 impr pos 16.2 before the 2026-11-08 heading/FAQ change). Many impressions, 0 clicks.
  - whatsapp-business-api-vs-app: 29 impr pos 21.7; "וואטסאפ עסקי יתרונות וחסרונות" 11 impr pos 15.8; "תוכנה לניהול וואטסאפ עסקי" pos 16.3 (was 24 before the team FAQ); "וואטסאפ ביזנס" 10 impr pos 29. Searchers write וואטסאפ, the site writes ווצאפ.
  - custom-erp-vs-off-the-shelf (new): 23 impr; "בניית מערכת erp" 10 impr pos 30.5; "מה חשוב לבדוק כשמחליפים אינטגרטור או שותף יישום למערכת erp קיימת?" pos 9.
  - system-adoption: "הטמעת מערכת מידע חדשה בארגון" pos 15.4 (was 16). recurring-payments-failed-charges pos 17. /eitan pos 5.6.
  - automation-roi: "החזר השקעה מחסן אוטומטי" 8 impr pos 35.8: warehouse intent, not ours, ignore.
  - Approved and applied 2026-11-15: rewrite title/description of small-business-digitization around "דיגיטציה עסקית"; whatsapp-business-api-vs-app title with "וואטסאפ ביזנס" spelling and "יתרונות וחסרונות"; an FAQ on replacing an ERP integrator in custom-erp-vs-off-the-shelf.
- 2026-11-18 daily (28 days to 2026-11-17): 233 impr, 0 clicks, avg pos 30.5. Sitemap resubmitted: 41 submitted, 0 reported indexed (impressions show pages are served). 7 days by date: 8 to 17 impr/day, data up to 2026-11-15.
  - Pages: small-business-digitization 47 (pos 14.6), whatsapp-business-api-vs-app 38 (21.3), custom-erp-vs-off-the-shelf 31 (43.6), small-business-automation 24 (72.7), automation-roi 17 (38.4), connecting-business-systems 12 (12.7), /eitan 12 (5.6), /conferences 11 (29.3), automatic-customer-reminders 10 (24.9), system-adoption 10 (20.3).
  - Queries: "דיגיטציה עסקית" 47 pos 14.6; "וואטסאפ עסקי יתרונות וחסרונות" 14 pos 16.4; "בניית מערכת erp" 14 pos 34.4; "וואטסאפ ביזנס" 13 pos 26.2; clearing-to-accounting 6 pos 6.2; "הטמעת מערכת מידע חדשה בארגון" 5 pos 15.4.
  - No changes today: the 2026-11-15 title changes need another week of data. Published collecting-documents-from-clients.
- 2026-11-19 daily (28 days to 2026-11-18, data through 2026-11-17): 252 impr (was 233), 0 clicks, avg pos 30.8. Sitemap: 41 submitted, 0 reported indexed.
  - whatsapp-business-api-vs-app 44 impr pos 19.8 (was 38, 21.3); last 7 days pos 17, first sign of the 2026-11-15 title change. "וואטסאפ ביזנס" 16 impr pos 23.7 (was 26.2); "וואטסאפ עסקי יתרונות וחסרונות" pos 15.7.
  - small-business-digitization 50 impr pos 15.2 (7 days: pos 19.9, slipping); "דיגיטציה עסקית" 50 impr. Published a case study that links to it to support the cluster.
  - custom-erp-vs-off-the-shelf 33 (pos 44.1); "בניית מערכת erp" 15 impr pos 35.5. whatsapp-bot-for-business picks up "בוט לעסקים" / "בוט ווטסאפ לעסק" at pos 77-84 (watch for Sunday).
  - Published small-business-digitization-case-study.
  - 2026-11-19: home page "עסק קטן" card (he + en) now states case handling time dropped from 6 weeks to 2 (from Kobi). Track whether the home page and the case study gain impressions.
- 2026-11-20 daily: no new GSC data since yesterday (latest day still 2026-11-17): 252 impr, 0 clicks, avg pos 30.8. Sitemap: 41 submitted, 0 reported indexed (last read 2026-11-19 05:47, before the case study URL was counted). 7 days by page: whatsapp-business-api-vs-app 17 impr pos 17.2; small-business-digitization 8 impr pos 22.6; custom-erp-vs-off-the-shelf 12 impr pos 50.4.
  - Published data-migration-to-new-system (supports "החלפת מערכת מידע", ERP/CRM switch queries).
