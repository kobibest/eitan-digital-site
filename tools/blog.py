#!/usr/bin/env python3
"""Build the blog from content/blog/*.html.

Each source file starts with a JSON meta block:

    <!--meta
    {"slug": "...", "title": "...", "h1": "...", "description": "...",
     "keyword": "...", "date": "2026-10-27", "updated": "2026-10-27",
     "read_min": 7, "summary": "...", "faq": [{"q": "...", "a": "..."}]}
    -->
    <p>Article body HTML...</p>

Run from the repo root: python3 tools/blog.py
It writes blog/<slug>.html, blog/index.html, and refreshes the blog
blocks inside sitemap.xml and llms.txt (between the blog markers).
"""
import glob, html, json, os, re

SITE = 'https://digital.m-eitan.co.il'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
WA_KOBI = 'https://wa.me/972532208816?text=%D7%A9%D7%9C%D7%95%D7%9D%20%D7%A7%D7%95%D7%91%D7%99%2C%20%D7%94%D7%92%D7%A2%D7%AA%D7%99%20%D7%9E%D7%94%D7%90%D7%AA%D7%A8'

HEAD_TRACKING = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H1X9EHS4XM"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-H1X9EHS4XM');</script>
<!-- Microsoft Clarity -->
<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","z4hj73vzhz");</script>'''

HEAD_COMMON = '''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;700&family=IBM+Plex+Sans+Hebrew:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v=20261028">
<link rel="stylesheet" href="/extra.css?v=20261028">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="קובי איתן">
<meta name="theme-color" content="#171A2F">
<meta property="og:site_name" content="איתן | דיגיטציה ארגונית">
<meta property="og:locale" content="he_IL">
<meta property="og:image" content="https://digital.m-eitan.co.il/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://digital.m-eitan.co.il/og.png">'''

LOGO = '''<svg viewBox="0 0 120 120" aria-hidden="true"><rect x="46" y="10" width="28" height="28" rx="6" fill="#12B886"/><rect x="57" y="38" width="6" height="14" fill="#171A2F"/><rect x="24" y="50" width="72" height="6" rx="3" fill="#171A2F"/><rect x="24" y="52" width="6" height="16" fill="#171A2F"/><rect x="57" y="52" width="6" height="16" fill="#171A2F"/><rect x="90" y="52" width="6" height="16" fill="#171A2F"/><rect x="13" y="68" width="28" height="28" rx="6" fill="#171A2F"/><rect x="46" y="68" width="28" height="28" rx="6" fill="#171A2F"/><rect x="79" y="68" width="28" height="28" rx="6" fill="#171A2F"/></svg>'''

HEADER = f'''<div class="wrap">
  <header class="top">
    <a class="brand" href="/" aria-label="איתן, דיגיטציה ארגונית, לדף הבית">
      {LOGO}
      <span><b>איתן</b><small>דיגיטציה ארגונית</small></span>
    </a>
    <nav class="top" aria-label="ניווט ראשי">
      <a href="/">דף הבית</a>
      <a href="/blog">מאמרים</a>
      <a href="/#reviews">המלצות</a>
      <a class="cta" href="#contact">לשיחת ייעוץ חינם</a>
    </nav>
  </header>
'''

CONTACT = f'''  <section id="contact" aria-labelledby="contactH">
    <div class="contact">
      <div>
        <p class="eyebrow">שיחת ייעוץ ראשונית, חינם</p>
        <h2 id="contactH">רוצים שנמפה את זה יחד אצלכם?</h2>
        <p>שיחה של כ־20 דקות, בלי עלות ובלי התחייבות. נעבור על התהליכים שחוזרים על עצמם ומתישים אתכם, ונראה מה כדאי לשפר בשינוי של התהליך ומה באוטומציה.</p>
        <div class="me"><img src="/img/kobi-face.webp" width="96" height="96" loading="lazy" decoding="async" alt="קובי איתן"><p><b>קובי איתן</b>יועץ ארגוני מוסמך. כל פנייה מגיעה אליי ישירות.</p></div>
        <p class="note">אפשר גם לכתוב לי בווצאפ ל־<a href="{WA_KOBI}" target="_blank" rel="noopener">053-2208816</a> או במייל ל־<a href="mailto:kobi@eitan-m.co.il">kobi@eitan-m.co.il</a></p>
      </div>
      <form id="lead" data-subject="{{subject}}">
        <label>שם<input name="name" autocomplete="name" required></label>
        <label>עסק או ארגון <small>(לא חובה)</small><input name="org" autocomplete="organization"></label>
        <label>טלפון<input name="phone" type="tel" inputmode="tel" autocomplete="tel" required></label>
        <label>מייל <small>(לא חובה)</small><input name="email" type="email" autocomplete="email"></label>
        <label>מה הייתם רוצים לשפר?<textarea name="msg" required></textarea></label>
        <button class="btn solid" type="submit">לתיאום שיחת ייעוץ חינם</button>
        <p class="note" id="formNote">הפנייה תישלח ישירות אליי.</p>
        <p class="note">הפרטים משמשים רק כדי לחזור אליכם. <a href="/privacy">מדיניות פרטיות</a></p>
      </form>
    </div>
  </section>
'''

FOOTER = '''  <footer>
    <span>איתן | דיגיטציה ארגונית · <a href="mailto:kobi@eitan-m.co.il">kobi@eitan-m.co.il</a> · <a href="https://www.linkedin.com/in/kobi-eitan-03a4b3235" rel="me noopener" target="_blank">לינקדאין</a></span>
    <nav aria-label="מערכות"><a href="/blog">מאמרים</a><a href="/conferences">ניהול כנסים</a><a href="/whatsapp">ווצאפ רשמי</a><a href="/eitan">מערכת איתן</a></nav>
    <p class="legal-line">Eitan Connect הוא שירות של "איתן", עוסק מורשה, ישראל · <a href="/privacy">מדיניות פרטיות</a> · <a href="/terms">תנאי שימוש</a> · <a href="/data-deletion">מחיקת נתונים</a></p>
    <p class="legal-line" dir="ltr" lang="en">Eitan Connect is a service of "Eitan" (איתן), a registered Israeli business (Osek Murshe) · <a href="mailto:kobi@eitan-m.co.il">kobi@eitan-m.co.il</a> · <a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="/data-deletion">Data Deletion</a></p>
  </footer>
</div>
<script src="/site.js?v=20261028"></script>
</body>
</html>
'''

ORG = {"@type": "ProfessionalService", "@id": SITE + "/#org", "name": "איתן | דיגיטציה ארגונית", "url": SITE + "/"}
PERSON = {"@type": "Person", "@id": SITE + "/#kobi", "name": "קובי איתן", "alternateName": "Kobi Eitan",
          "jobTitle": "יועץ ארגוני מוסמך ומוביל דיגיטציה", "url": SITE + "/",
          "sameAs": ["https://www.linkedin.com/in/kobi-eitan-03a4b3235", "https://www.xplace.com/il/u/user1790252229559"]}


def esc(s):
    return html.escape(s, quote=True)


def he_date(d):
    y, m, day = d.split('-')
    return f'{int(day)} ב{MONTHS[int(m) - 1]} {y}'


def strip_tags(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()


def load():
    posts = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'content/blog/*.html'))):
        src = open(path, encoding='utf-8').read()
        m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->\s*', src, re.S)
        if not m:
            raise SystemExit(f'{path}: missing <!--meta {{...}} --> header')
        meta = json.loads(m.group(1))
        for k in ('slug', 'title', 'h1', 'description', 'keyword', 'date', 'read_min', 'summary'):
            if not meta.get(k):
                raise SystemExit(f'{path}: meta.{k} is required')
        meta.setdefault('updated', meta['date'])
        meta.setdefault('faq', [])
        meta['body'] = src[m.end():].strip()
        posts.append(meta)
    slugs = [p['slug'] for p in posts]
    if len(slugs) != len(set(slugs)):
        raise SystemExit('duplicate slug')
    posts.sort(key=lambda p: p['date'], reverse=True)
    return posts


def toc(body):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(items) < 3:
        return ''
    lis = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="תוכן המאמר"><p>במאמר הזה</p><ol>{lis}</ol></nav>\n'


def article_page(p, posts):
    url = f'{SITE}/blog/{p["slug"]}'
    graph = [
        ORG, PERSON,
        {"@type": "BlogPosting", "@id": url + "#article", "headline": p['h1'], "description": p['description'],
         "inLanguage": "he", "datePublished": p['date'], "dateModified": p['updated'],
         "author": {"@id": SITE + "/#kobi"}, "publisher": {"@id": SITE + "/#org"},
         "mainEntityOfPage": url, "image": SITE + "/og.png", "keywords": p['keyword']},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "דף הבית", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "מאמרים", "item": SITE + "/blog"},
            {"@type": "ListItem", "position": 3, "name": p['h1'], "item": url}]},
    ]
    if p['faq']:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": strip_tags(f['a'])}}
            for f in p['faq']]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(',', ':'))

    faq = ''
    if p['faq']:
        items = '\n'.join(f'      <details class="faq"><summary>{esc(f["q"])}</summary><p>{f["a"]}</p></details>' for f in p['faq'])
        faq = f'''    <section class="post-faq" aria-labelledby="faqH">
      <h2 id="faqH">שאלות נפוצות</h2>
      <div class="faqs">
{items}
      </div>
    </section>
'''
    others = [o for o in posts if o['slug'] != p['slug']][:3]
    more = ''
    if others:
        cards = '\n'.join(f'      <a class="post-card" href="/blog/{o["slug"]}"><h3>{esc(o["h1"])}</h3><p>{esc(o["summary"])}</p><span>לקריאה</span></a>' for o in others)
        more = f'''  <section aria-labelledby="moreH">
    <h2 id="moreH">עוד מאמרים</h2>
    <div class="post-list">
{cards}
    </div>
  </section>
'''
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
{HEAD_TRACKING}
{HEAD_COMMON}
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p['h1'])}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:image:alt" content="{esc(p['h1'])}">
<meta property="article:published_time" content="{p['date']}">
<meta property="article:modified_time" content="{p['updated']}">
<meta name="twitter:title" content="{esc(p['h1'])}">
<meta name="twitter:description" content="{esc(p['description'])}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{HEADER}
  <main>
    <article class="post">
      <nav class="crumbs" aria-label="פירורי לחם"><a href="/">דף הבית</a><span aria-hidden="true">›</span><a href="/blog">מאמרים</a></nav>
      <h1>{esc(p['h1'])}</h1>
      <div class="byline"><img src="/img/kobi-face.webp" width="96" height="96" alt="" decoding="async"><p><b>קובי איתן</b>יועץ ארגוני מוסמך · <time datetime="{p['date']}">{he_date(p['date'])}</time> · {p['read_min']} דקות קריאה</p></div>
      {toc(p['body'])}<div class="post-body">
{p['body']}
      </div>
      <aside class="post-cta">
        <p><b>רוצים לעשות את זה עם מישהו שכבר עשה את זה הרבה פעמים?</b> בשיחת ייעוץ ראשונית של כ־20 דקות, בחינם, נמפה יחד את התהליכים שמתישים אתכם ונבחר מה לשפר קודם.</p>
        <a class="btn solid" href="#contact">לשיחת ייעוץ ראשונית חינם</a>
      </aside>
    </article>
{faq}  </main>
{more}{CONTACT.replace('{subject}', esc('מאמר: ' + p['h1']))}{FOOTER}'''


def index_page(posts):
    url = SITE + '/blog'
    ld = json.dumps({"@context": "https://schema.org", "@graph": [ORG, PERSON, {
        "@type": "Blog", "@id": url + "#blog", "name": "מאמרים על דיגיטציה, אוטומציה וייעול תהליכים", "url": url,
        "inLanguage": "he", "publisher": {"@id": SITE + "/#org"},
        "blogPost": [{"@type": "BlogPosting", "headline": p['h1'], "url": f'{SITE}/blog/{p["slug"]}', "datePublished": p['date']} for p in posts]}]},
        ensure_ascii=False, separators=(',', ':'))
    cards = '\n'.join(
        f'      <a class="post-card" href="/blog/{p["slug"]}"><time datetime="{p["date"]}">{he_date(p["date"])}</time><h3>{esc(p["h1"])}</h3><p>{esc(p["summary"])}</p><span>לקריאה · {p["read_min"]} דקות</span></a>'
        for p in posts)
    desc = 'מדריכים מעשיים לבעלי עסקים ומנהלים: ייעול תהליכים, אוטומציה עסקית, בוטים, CRM וחיבור בין מערכות. בלי תיאוריה, עם צעדים שאפשר ליישם מחר בבוקר.'
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
{HEAD_TRACKING}
{HEAD_COMMON}
<title>מאמרים על ייעול תהליכים, אוטומציה ודיגיטציה לעסקים | איתן</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="מאמרים על ייעול תהליכים, אוטומציה ודיגיטציה">
<meta property="og:description" content="{desc}">
<meta property="og:image:alt" content="איתן | דיגיטציה ארגונית">
<meta name="twitter:title" content="מאמרים על ייעול תהליכים, אוטומציה ודיגיטציה">
<meta name="twitter:description" content="{desc}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{HEADER}
  <main>
    <div class="hero sub blog-hero">
      <div>
        <p class="eyebrow">מאמרים</p>
        <h1>ייעול תהליכים, אוטומציה ודיגיטציה, בפועל</h1>
        <p class="lede">{desc}</p>
      </div>
    </div>
    <section aria-label="כל המאמרים" class="blog-list">
    <div class="post-list">
{cards}
    </div>
    </section>
  </main>
{CONTACT.replace('{subject}', 'שיחת ייעוץ ראשונית (מאמרים)')}{FOOTER}'''


def replace_block(path, start, end, content):
    s = open(path, encoding='utf-8').read()
    pat = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if not pat.search(s):
        raise SystemExit(f'{path}: markers {start} / {end} not found')
    s = pat.sub(lambda m: start + content + end, s)
    open(path, 'w', encoding='utf-8').write(s)


def main():
    posts = load()
    os.makedirs(os.path.join(ROOT, 'blog'), exist_ok=True)
    for p in posts:
        open(os.path.join(ROOT, 'blog', p['slug'] + '.html'), 'w', encoding='utf-8').write(article_page(p, posts))
    open(os.path.join(ROOT, 'blog', 'index.html'), 'w', encoding='utf-8').write(index_page(posts))
    latest = posts[0]['updated'] if posts else ''
    urls = [f'\n  <url><loc>{SITE}/blog</loc><lastmod>{latest}</lastmod><priority>0.7</priority></url>']
    urls += [f'\n  <url><loc>{SITE}/blog/{p["slug"]}</loc><lastmod>{p["updated"]}</lastmod><priority>0.6</priority></url>' for p in posts]
    replace_block(os.path.join(ROOT, 'sitemap.xml'), '<!-- blog:start -->', '<!-- blog:end -->', ''.join(urls) + '\n  ')
    lines = ''.join(f'\n- [{p["h1"]}]({SITE}/blog/{p["slug"]}): {p["summary"]}' for p in posts)
    replace_block(os.path.join(ROOT, 'llms.txt'), '<!-- blog:start -->', '<!-- blog:end -->', f'\n## מאמרים\n- [כל המאמרים]({SITE}/blog){lines}\n')
    print(f'built {len(posts)} post(s)')


if __name__ == '__main__':
    main()
