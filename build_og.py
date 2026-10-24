import os, sys, shutil, subprocess, urllib.request, glob
# Builds the social share images at deploy time:
#   og.png    (Hebrew pages)   og-en.png (English pages)
# Centered layout so WhatsApp's square thumbnail crop still shows logo + name.
try:
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageFilter
    except ImportError:
        subprocess.run([sys.executable,'-m','pip','install','--quiet','--target','/tmp/pylib','pillow'],check=True)
        sys.path.insert(0,'/tmp/pylib')
        from PIL import Image, ImageDraw, ImageFont, ImageFilter
    LOCAL=os.environ.get('OG_LOCAL_FONTS')  # local testing only
    FONT='/tmp/rubik.ttf'
    if not LOCAL and not os.path.exists(FONT):
        urllib.request.urlretrieve('https://github.com/google/fonts/raw/main/ofl/rubik/Rubik%5Bwght%5D.ttf', FONT)
    def font(size, weight, script='hebrew'):
        if LOCAL:
            return ImageFont.truetype(f'{LOCAL}/{script}-{weight}.ttf', size, layout_engine=ImageFont.Layout.BASIC)
        f=ImageFont.truetype(FONT, size, layout_engine=ImageFont.Layout.BASIC)
        try: f.set_variation_by_axes([weight])
        except Exception: pass
        return f
    def heb(s):  # visual order for pure-Hebrew strings (PIL draws left-to-right)
        return s[::-1]

    BG=(23,26,47); WHITE=(244,246,249); GREEN=(18,184,134); MINT=(127,224,191); GREY=(201,206,219); URL=(154,163,184)
    def make(out, title, sub, tag, rtl):
        S=2; W,H=1200*S,630*S
        img=Image.new('RGB',(W,H),BG)
        glow=Image.new('RGB',(W,H),BG); g=ImageDraw.Draw(glow)
        g.ellipse([-120*S,-180*S,440*S,380*S],fill=(18,120,100))
        g.ellipse([820*S,330*S,1340*S,850*S],fill=(40,50,150))
        glow=glow.filter(ImageFilter.GaussianBlur(130*S))
        img=Image.blend(img,glow,0.7)
        d=ImageDraw.Draw(img)
        dot=tuple(round(BG[i]+(WHITE[i]-BG[i])*0.06) for i in range(3))
        for y in range(18,630,36):
            for x in range(18,1200,36):
                d.ellipse([x*S-2*S,y*S-2*S,x*S+2*S,y*S+2*S],fill=dot)
        # logo, 150px, centered
        k=150/120*S; ox,oy=(600-75)*S,70*S
        def r(x,y,w,h,rad,c): d.rounded_rectangle([ox+x*k,oy+y*k,ox+(x+w)*k,oy+(y+h)*k],radius=rad*k,fill=c)
        r(46,10,28,28,6,GREEN); r(57,38,6,14,0,WHITE); r(24,50,72,6,3,WHITE)
        for x in (24,57,90): r(x,52,6,16,0,WHITE)
        for x in (13,46,79): r(x,68,28,28,6,WHITE)
        sc='hebrew' if rtl else 'latin'
        def ctext(y, s, size, weight, fill, script=None):
            f=font(size*S,weight,script or sc); s=heb(s) if (rtl and (script or sc)=='hebrew') else s
            d.text((W/2,y*S),s,font=f,fill=fill,anchor='mt')
        ctext(232, title, 132, 900, WHITE)
        ctext(388, sub, 44, 700, MINT)
        ctext(458, tag, 34, 500, GREY)
        ctext(560, 'digital.m-eitan.co.il', 28, 500, URL, 'latin')
        d.rectangle([0,(630-10)*S,W,H],fill=GREEN)
        img=img.resize((1200,630),Image.LANCZOS)
        img.save(out,optimize=True)
        print(out,'built',os.path.getsize(out))

    try:
        make('og.png','איתן','דיגיטציה ארגונית','אוטומציות · בוטים · מערכות',True)
    except Exception as e:
        print('og.png kept as-is:',e)
    try:
        make('og-en.png','Eitan','Digital transformation','Automations · Bots · Systems',False)
    except Exception as e:
        print('og-en fallback:',e); shutil.copy('og.png','og-en.png')
    for f in glob.glob('en/*.html'):
        t=open(f,encoding='utf-8').read().replace('/og.png','/og-en.png')
        open(f,'w',encoding='utf-8').write(t)
    print('en pages now use og-en.png')
except Exception as e:
    print('og build failed:',e)
    if not os.path.exists('og-en.png'): shutil.copy('og.png','og-en.png')
