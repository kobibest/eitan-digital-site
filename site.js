(function(){
  var EN=document.documentElement.lang==='en';
  var nav=document.querySelector('nav.top');
  if(nav&&!EN&&!nav.querySelector('.lang')){
    var map={'/':'/en','/conferences':'/en/conferences','/whatsapp':'/en/whatsapp','/eitan':'/en/eitan'};
    var p=location.pathname.replace(/\.html$/,'').replace(/\/index$/,'/')||'/';
    var a=document.createElement('a');a.className='lang';a.lang='en';a.hreflang='en';a.textContent='English';a.href=map[p]||'/en';
    var cta=nav.querySelector('.cta');nav.insertBefore(a,cta);
  }
  // Sticky CTA on mobile, hidden while the contact section is on screen
  var navCta=nav&&nav.querySelector('.cta'), contactSec=document.getElementById('contact');
  if(navCta&&contactSec){
    var bar=document.createElement('div');bar.className='sticky-cta';
    var b=document.createElement('a');b.className='btn solid';b.href=navCta.getAttribute('href');b.textContent=navCta.textContent;
    var w=document.createElement('a');w.className='btn wa';w.target='_blank';w.rel='noopener';
    w.href=EN?'https://wa.me/972532208816?text=Hi%20Kobi%2C%20I%20found%20you%20through%20your%20website':'https://wa.me/972532208816?text=%D7%A9%D7%9C%D7%95%D7%9D%20%D7%A7%D7%95%D7%91%D7%99%2C%20%D7%94%D7%92%D7%A2%D7%AA%D7%99%20%D7%9E%D7%94%D7%90%D7%AA%D7%A8';
    w.setAttribute('aria-label',EN?'WhatsApp Kobi':'ווצאפ לקובי');
    w.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg><span>'+(EN?'WhatsApp':'ווצאפ')+'</span>';
    bar.appendChild(b);bar.appendChild(w);document.body.appendChild(bar);document.body.classList.add('has-sticky');
    var hero=document.querySelector('.hero .btns')||document.querySelector('main h1'),heroVis=true,contactVis=false;
    var upd=function(){bar.classList.toggle('show',!heroVis&&!contactVis);};
    if('IntersectionObserver' in window){
      new IntersectionObserver(function(es){es.forEach(function(e){if(e.target===contactSec)contactVis=e.isIntersecting;else heroVis=e.isIntersecting;});upd();}).observe(contactSec);
      if(hero)new IntersectionObserver(function(es){heroVis=es[0].isIntersecting;upd();}).observe(hero);else{heroVis=false;upd();}
    }else{heroVis=false;upd();}
  }
  // Analytics events: WhatsApp clicks and email clicks
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]'); if(!a||typeof gtag!=='function')return;
    var h=a.getAttribute('href');
    if(/wa\.me\//.test(h))gtag('event','whatsapp_click',{link_url:h,wa_target:/972532208816/.test(h)?'kobi':'demo_bot',page_path:location.pathname});
    else if(/^mailto:/.test(h))gtag('event','email_click',{page_path:location.pathname});
  });
  var KEY='55804344-6275-4e9e-995e-75155ee5fc93';
  var f=document.getElementById('lead'); if(!f)return;
  var note=document.getElementById('formNote');
  var btn=f.querySelector('button[type=submit]');
  var T=EN?{ready:'Your message goes straight to me.',sending:'Sending...',sent:'Sent',ok:"Thanks, your message was sent. I'll get back to you soon.",fail:'Sending failed. You can email me directly at kobi@eitan-m.co.il',def:'Website inquiry',from:'Eitan website (English)'}
         :{ready:'הפנייה תישלח ישירות אליי.',sending:'שולח...',sent:'נשלח',ok:'הפנייה נשלחה. אחזור אליכם בהקדם.',fail:'השליחה לא הצליחה. אפשר לכתוב ישירות ל־kobi@eitan-m.co.il',def:'פנייה מהאתר',from:'אתר איתן | דיגיטציה ארגונית'};
  if(note)note.textContent=T.ready;
  var started=false;
  f.addEventListener('input',function(){if(started)return;started=true;if(typeof gtag==='function')gtag('event','form_start',{form_subject:f.getAttribute('data-subject')||'',page_path:location.pathname});});
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var subject=(f.getAttribute('data-subject')||T.def)+' – '+f.name.value;
    var val=function(n){return f[n]?f[n].value.trim():'';};
    var email=val('email')||(/@/.test(val('contact'))?val('contact'):'');
    var data={access_key:KEY,subject:subject,from_name:T.from,'שם':f.name.value,'ארגון':val('org'),'טלפון':val('phone')||val('contact'),'מייל':email,'הודעה':f.msg.value,'עמוד':location.pathname};
    if(email)data.replyto=email;
    btn.disabled=true; var old=btn.textContent; btn.textContent=T.sending;
    fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json();})
      .then(function(j){
        if(j&&j.success){if(typeof gtag==='function')gtag('event','generate_lead',{form_subject:f.getAttribute('data-subject')||'',page_path:location.pathname});f.reset(); if(note)note.textContent=T.ok; btn.textContent=T.sent;}
        else throw new Error();
      })
      .catch(function(){
        btn.disabled=false; btn.textContent=old;
        if(note)note.textContent=T.fail;
      });
  });
})();
