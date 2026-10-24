(function(){
  var EN=document.documentElement.lang==='en';
  var nav=document.querySelector('nav.top');
  if(nav&&!EN&&!nav.querySelector('.lang')){
    var map={'/':'/en','/conferences':'/en/conferences','/whatsapp':'/en/whatsapp','/eitan':'/en/eitan'};
    var p=location.pathname.replace(/\.html$/,'').replace(/\/index$/,'/')||'/';
    var a=document.createElement('a');a.className='lang';a.lang='en';a.hreflang='en';a.textContent='English';a.href=map[p]||'/en';
    var cta=nav.querySelector('.cta');nav.insertBefore(a,cta);
  }
  var KEY='55804344-6275-4e9e-995e-75155ee5fc93';
  var f=document.getElementById('lead'); if(!f)return;
  var note=document.getElementById('formNote');
  var btn=f.querySelector('button[type=submit]');
  var T=EN?{ready:'Your message goes straight to me.',sending:'Sending...',sent:'Sent',ok:"Thanks, your message was sent. I'll get back to you soon.",fail:'Sending failed. You can email me directly at kobi@eitan-m.co.il',def:'Website inquiry',from:'Eitan website (English)'}
         :{ready:'הפנייה תישלח ישירות אליי.',sending:'שולח...',sent:'נשלח',ok:'הפנייה נשלחה. אחזור אליכם בהקדם.',fail:'השליחה לא הצליחה. אפשר לכתוב ישירות ל־kobi@eitan-m.co.il',def:'פנייה מהאתר',from:'אתר איתן | דיגיטציה ארגונית'};
  if(note)note.textContent=T.ready;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var subject=(f.getAttribute('data-subject')||T.def)+' – '+f.name.value;
    var contact=f.contact.value.trim();
    var data={access_key:KEY,subject:subject,from_name:T.from,'שם':f.name.value,'ארגון':f.org?f.org.value:'','פרטי קשר':contact,'הודעה':f.msg.value,'עמוד':location.pathname};
    if(/@/.test(contact))data.replyto=contact;
    btn.disabled=true; var old=btn.textContent; btn.textContent=T.sending;
    fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json();})
      .then(function(j){
        if(j&&j.success){f.reset(); if(note)note.textContent=T.ok; btn.textContent=T.sent;}
        else throw new Error();
      })
      .catch(function(){
        btn.disabled=false; btn.textContent=old;
        if(note)note.textContent=T.fail;
      });
  });
})();
