# -*- coding: utf-8 -*-
"""Az ARCULAT-VÁLASZTÓ oldal: minden elemből 5+ opció, opciónként megjegyzés + „végleges” jelölés,
alul az élő oldal a kiválasztott elemekből. Önálló HTML (localStorage-mentés + másolható visszajelzés)."""
import json, datetime
from . import alap
from .alap import esc, md, g
from .css_alap import ALAP_CSS
from .futas_js import FUTAS_JS
from .stilusok import GLOBALIS
from . import epito
from .epito import SZEKCIOK, STILUS_KATOK, KAT_NEV
from .kozos import shead, btn, foto, ik, kick, dk, hat, chips

PREV_W = 1280

UI_CSS = r"""
:root{--u-bg:#EEEBE5;--u-card:#fff;--u-ink:#1d1b18;--u-ink2:#5d5850;--u-ink3:#8f897e;--u-line:#e0dbd2;--u-ok:#1e8a4c;--u-okl:#e3f4ea;--u-elo:#d98a12;--u-elol:#fdf1dc;--u-acc:#2f4de0}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:76px}
body{margin:0;background:var(--u-bg);color:var(--u-ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.vl-top{position:sticky;top:0;z-index:1000;height:62px;display:flex;align-items:center;gap:16px;padding:0 18px;background:rgba(255,255,255,.92);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border-bottom:1px solid var(--u-line)}
.vl-top .mk{display:flex;align-items:center;gap:10px;font-weight:800;font-size:15px;white-space:nowrap}
.vl-top .mk i{display:block;width:34px;height:34px;background:center/contain no-repeat}
.vl-top .mk small{display:block;font-weight:600;color:var(--u-ink3);font-size:11.5px;letter-spacing:.04em;text-transform:uppercase}
.vl-prog{flex:1;max-width:340px;display:flex;align-items:center;gap:10px;font-size:13px;color:var(--u-ink2);font-weight:600}
.vl-prog .bar{flex:1;height:8px;background:#e7e2d9;border-radius:9px;overflow:hidden}
.vl-prog .bar i{display:block;height:100%;width:0;background:var(--u-ok);border-radius:9px;transition:width .4s}
.vl-top .gombok{margin-left:auto;display:flex;gap:8px}
.ub{display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 14px;border-radius:10px;border:1px solid var(--u-line);background:#fff;color:var(--u-ink);font:700 13px/1 inherit;cursor:pointer;text-decoration:none;white-space:nowrap}
.ub:hover{border-color:var(--u-ink3)}
.ub.fo{background:var(--u-ink);color:#fff;border-color:var(--u-ink)}
.ub.fo:hover{background:#000}
.ub.zold{background:var(--u-ok);border-color:var(--u-ok);color:#fff}
.ub svg{width:16px;height:16px}
.vl-lay{display:grid;grid-template-columns:250px minmax(0,1fr)}
.vl-side{position:sticky;top:62px;height:calc(100vh - 62px);overflow:auto;padding:18px 12px 40px 16px;border-right:1px solid var(--u-line);background:#f6f4f0}
.vl-side h6{margin:18px 8px 6px;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--u-ink3)}
.vl-side a{display:flex;align-items:center;gap:9px;padding:7px 8px;border-radius:9px;text-decoration:none;color:var(--u-ink);font-size:13.5px;font-weight:600}
.vl-side a:hover{background:#ebe7df}
.vl-side a .d{width:10px;height:10px;border-radius:50%;border:2px solid #c9c2b5;flex:none}
.vl-side a.elo .d{border-color:var(--u-elo);background:var(--u-elol)}
.vl-side a.veg .d{border-color:var(--u-ok);background:var(--u-ok)}
.vl-side a .n{margin-left:auto;font-size:11px;color:var(--u-ink3);font-weight:700}
.vl-side a .n.van::before{content:"💬 "}
.vl-side a.elolap{margin-top:12px;background:var(--u-ink);color:#fff}
.vl-main{padding:26px clamp(14px,2.4vw,34px) 120px;min-width:0}
.vl-intro{background:#fff;border-radius:20px;padding:26px 28px;margin-bottom:26px;border:1px solid var(--u-line);display:grid;grid-template-columns:1.3fr 1fr;gap:28px}
.vl-intro h1{margin:0 0 8px;font-size:26px;letter-spacing:-.01em}
.vl-intro p{margin:0 0 10px;color:var(--u-ink2)}
.vl-intro ol{margin:10px 0 0;padding-left:20px;color:var(--u-ink2)}
.vl-intro ol li{margin:4px 0}
.vl-intro .prof{background:#f6f4f0;border-radius:14px;padding:16px 18px;font-size:13.5px}
.vl-intro .prof b{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--u-ink3);margin:10px 0 6px}
.vl-intro .prof b:first-child{margin-top:0}
.vl-intro .sw{display:flex;gap:6px;flex-wrap:wrap}
.vl-intro .sw i{width:28px;height:28px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}
.vl-intro .mot{display:flex;gap:10px}
.vl-intro .mot i{width:34px;height:34px;background:#3d3a35;-webkit-mask:center/contain no-repeat;mask:center/contain no-repeat}
.vl-csop{margin:40px 0 12px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--u-ink3);font-weight:800;display:flex;align-items:center;gap:12px}
.vl-csop::after{content:"";flex:1;height:1px;background:var(--u-line)}
.vl-kat{background:#fff;border-radius:22px;border:1px solid var(--u-line);padding:22px 22px 24px;margin-bottom:22px}
.vl-kat>header{display:flex;align-items:flex-start;gap:14px;margin-bottom:18px;flex-wrap:wrap}
.vl-kat>header .sz{width:34px;height:34px;border-radius:10px;background:var(--u-ink);color:#fff;display:grid;place-items:center;font-weight:800;font-size:14px;flex:none}
.vl-kat>header h2{margin:0;font-size:20px;letter-spacing:-.01em}
.vl-kat>header p{margin:2px 0 0;color:var(--u-ink2);font-size:14px}
.vl-kat>header .st{margin-left:auto;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.pill{display:inline-flex;align-items:center;gap:6px;padding:5px 11px;border-radius:999px;font-size:12px;font-weight:800;background:#f1eee8;color:var(--u-ink2)}
.pill.ok{background:var(--u-okl);color:var(--u-ok)}
.pill.elo{background:var(--u-elol);color:#9a5c00}
.ujak{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;color:var(--u-ink2);cursor:pointer;user-select:none}
.vl-opts{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,370px),1fr));gap:18px}
.vl-opts.nagy{grid-template-columns:1fr}
.vl-opt{position:relative;border-radius:18px;border:2px solid var(--u-line);background:#fbfaf8;display:flex;flex-direction:column;transition:border-color .2s,box-shadow .2s}
.vl-opt:hover{border-color:#cfc8bb}
.vl-opt.is-elo{border-color:var(--u-elo);box-shadow:0 0 0 4px var(--u-elol)}
.vl-opt.is-veg{border-color:var(--u-ok);box-shadow:0 0 0 4px var(--u-okl)}
.vl-opt .badge{position:absolute;top:-11px;right:14px;z-index:5;display:none;padding:4px 10px;border-radius:999px;font-size:11.5px;font-weight:800;background:var(--u-ok);color:#fff;box-shadow:0 4px 10px rgba(0,0,0,.15)}
.vl-opt.is-veg .badge{display:inline-flex}
.vl-prev{position:relative;border-radius:16px 16px 0 0;overflow:hidden;cursor:pointer;background:#fff;min-height:60px}
.vl-prev>.elo-root{transform-origin:0 0}
.vl-opts.nagy .vl-opt{display:grid;grid-template-columns:minmax(0,1fr) 300px}
.vl-opts.nagy .vl-prev{border-radius:16px 0 0 16px;max-height:860px}
.vl-opts.nagy .vl-prev::after{content:"";position:absolute;left:0;right:0;bottom:0;height:40px;background:linear-gradient(transparent,rgba(251,250,248,.9));pointer-events:none;opacity:0}
.vl-opts.nagy .vl-prev.levag::after{opacity:1}
.vl-body{padding:14px 16px 16px;display:flex;flex-direction:column;gap:10px;min-width:0}
.vl-opts.nagy .vl-body{border-left:1px solid var(--u-line)}
.vl-nev{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.vl-nev .id{font:800 11.5px/1 ui-monospace,Menlo,monospace;padding:4px 7px;border-radius:6px;background:var(--u-ink);color:#fff;text-transform:uppercase}
.vl-nev h3{margin:0;font-size:15.5px}
.vl-nev .aj{font-size:11px;font-weight:800;padding:3px 8px;border-radius:999px;background:#e8ecff;color:var(--u-acc)}
.vl-nev .egy{font-size:11px;font-weight:800;padding:3px 8px;border-radius:999px;background:#fdeee8;color:#b5431c}
.vl-miert{margin:0;font-size:13.5px;color:var(--u-ink2)}
.vl-act{display:flex;gap:8px;flex-wrap:wrap}
.vl-act .ub{height:34px;font-size:12.5px;padding:0 12px}
.vl-act .veg.on{background:var(--u-ok);border-color:var(--u-ok);color:#fff}
.vl-act .elo.on{background:var(--u-elol);border-color:var(--u-elo);color:#8a5200}
.vl-com{width:100%;min-height:62px;resize:vertical;border-radius:12px;border:1px solid var(--u-line);padding:9px 11px;font:13.5px/1.45 inherit;background:#fff;color:var(--u-ink)}
.vl-com:focus{outline:2px solid #c9d2ff;border-color:#9aa9f5}
.vl-com.van{background:#fffdf3;border-color:#e8d9a8}
.vl-elozo{margin:0;font-size:12.5px;color:#7a5b12;background:#fdf5df;border-radius:10px;padding:7px 10px}
.vl-elozo b{font-weight:800}
.vl-nev .uj{font-size:11px;font-weight:800;padding:3px 8px;border-radius:999px;background:#e3f4ea;color:#1e8a4c}
.pill.uj{background:#e3f4ea;color:#1e8a4c}
.vl-demo-cim{font:700 10.5px/1 ui-monospace,Menlo,monospace;letter-spacing:.12em;text-transform:uppercase;color:#9b9489;padding:10px 12px 0}
.vl-elo-sec{margin-top:54px}
.vl-elo-fej{position:sticky;top:62px;z-index:900;display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--u-ink);color:#fff;border-radius:18px 18px 0 0;padding:14px 18px}
.vl-elo-fej h2{margin:0;font-size:18px}
.vl-elo-fej p{margin:0;font-size:13px;color:#cfcac2}
.vl-elo-fej .ub{height:34px;background:#2d2a26;color:#fff;border-color:#48443e}
.vl-elo-fej .ub.on{background:#fff;color:var(--u-ink)}
.vl-elo-fej .gombok{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap}
#elo-keret{background:#fff;border:1px solid var(--u-line);border-top:0;border-radius:0 0 18px 18px;overflow:clip;transition:max-width .3s}
#elo-keret.mobil{max-width:414px;margin:0 auto;border:12px solid #1d1b18;border-radius:44px;height:820px;overflow-y:auto;overflow-x:hidden}
.slot{position:relative}
.slot>.vl-slot-cimke{position:absolute;left:12px;top:12px;z-index:950;display:none;align-items:center;gap:8px;padding:6px 10px;border-radius:9px;background:rgba(29,27,24,.88);color:#fff;font:700 12px/1 -apple-system,sans-serif;text-decoration:none}
.slot:hover>.vl-slot-cimke{display:inline-flex}
#elo-keret.tiszta .vl-slot-cimke{display:none!important}
.vl-fab{position:fixed;right:22px;bottom:22px;z-index:1100;display:flex;gap:10px}
.vl-fab .ub{height:48px;padding:0 18px;border-radius:14px;box-shadow:0 12px 30px -10px rgba(0,0,0,.4);font-size:14px}
.vl-modal{position:fixed;inset:0;z-index:2000;background:rgba(20,18,15,.55);display:none;align-items:center;justify-content:center;padding:20px}
.vl-modal.on{display:flex}
.vl-modal .ab{background:#fff;border-radius:20px;max-width:820px;width:100%;max-height:90vh;display:flex;flex-direction:column;padding:22px;gap:12px}
.vl-modal h3{margin:0;font-size:20px}
.vl-modal p{margin:0;color:var(--u-ink2);font-size:14px}
.vl-modal textarea{flex:1;min-height:360px;width:100%;border-radius:12px;border:1px solid var(--u-line);padding:12px;font:12.5px/1.5 ui-monospace,Menlo,monospace;resize:vertical}
.vl-modal .gombok{display:flex;gap:8px;justify-content:flex-end;flex-wrap:wrap}
.vl-alt{background:#fff;border-radius:22px;border:1px solid var(--u-line);padding:22px;margin:22px 0}
.vl-alt h2{margin:0 0 6px;font-size:18px}
.vl-toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(30px);opacity:0;z-index:2100;background:var(--u-ink);color:#fff;padding:11px 18px;border-radius:12px;font-weight:700;font-size:14px;transition:all .3s;pointer-events:none}
.vl-toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
.vl-navfill{height:150px;display:flex;align-items:flex-end;padding:0 40px 26px;font:700 13px/1 ui-monospace,Menlo,monospace;letter-spacing:.12em;text-transform:uppercase}
.vl-mozg-play{position:absolute;right:12px;top:12px;z-index:20}
.vl-mozg-sor{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:-6px 0 16px}
.vl-mozg-sor .ub.on{background:var(--u-ink);color:#fff;border-color:var(--u-ink)}
.vl-mozg-sor small{color:var(--u-ink3);font-size:12.5px}
.vl-lassu [data-rv]{transition-duration:2.2s!important;transition-delay:calc(var(--i)*300ms)!important}
.vl-mentes{font-size:12px;font-weight:700;color:var(--u-ink3);white-space:nowrap}
.vl-mentes.ok{color:var(--u-ok)}.vl-mentes.hiba{color:#b5431c}
.vl-prev:has(.vl-mozg-play) .shead{padding-right:110px}
.ph.nincsfoto{background:repeating-linear-gradient(45deg,var(--c-tint) 0 10px,var(--c-card) 10px 20px);display:grid;place-items:center}
.ph.nincsfoto span{font:700 .7rem/1 ui-monospace,monospace;letter-spacing:.14em;color:var(--c-ink-3)}
.logo-szoveg{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.3rem;color:var(--c-head)}
@media (max-width:980px){.vl-lay{grid-template-columns:1fr}.vl-side{display:none}.vl-intro{grid-template-columns:1fr}.vl-opts.nagy .vl-opt{grid-template-columns:1fr}.vl-opts.nagy .vl-prev{border-radius:16px 16px 0 0}.vl-opts.nagy .vl-body{border-left:0}.vl-prog{display:none}}
@media (max-width:640px){.vl-top .gombok .ub:not(.fo){display:none}}
"""

UI_JS = r"""
(function(){
var D = JSON.parse(document.getElementById('vl-data').textContent);
var KEY = 'wag:' + D.marka.slug + ':v' + D.verzio;
var S = null;
try { S = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch(e) {}
if (!S || !S.val) S = {val:{}, alt:''};
var friss = !S.val || !Object.keys(S.val).length;
var KAT = {}; D.kategoriak.forEach(function(k){ KAT[k.kat] = k; if(!S.val[k.kat]) S.val[k.kat] = {veg:null, elo:null, megj:{}, ujakat:false}; });
var EL = (D.elozo && D.elozo.valasztas) || {};
D.kategoriak.forEach(function(k){
  var e = EL[k.kat]; if (!e) return;
  var ids = k.opciok.map(function(x){return x.id;});
  if (friss && e.vegleges && ids.indexOf(e.vegleges) >= 0) { S.val[k.kat].veg = e.vegleges; S.val[k.kat].elo = e.vegleges; }
  var box = document.getElementById('kat-' + k.kat); if (!box) return;
  Object.keys(e.megjegyzesek || {}).forEach(function(id){
    var o = box.querySelector('.vl-opt[data-id="' + id + '"] .vl-com'); if (!o) return;
    var p = document.createElement('p'); p.className = 'vl-elozo'; p.innerHTML = '<b>Előző kör:</b> ' + String(e.megjegyzesek[id]).replace(/[<>&]/g, function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;'}[c];});
    o.parentNode.insertBefore(p, o);
  });
  if (e.opciok) ids.forEach(function(id){ if (e.opciok.indexOf(id) < 0) { var n = box.querySelector('.vl-opt[data-id="' + id + '"] .vl-nev'); if (n) n.insertAdjacentHTML('beforeend', '<span class="uj">Új</span>'); } });
  if (e.ujakat) { var st = box.querySelector('header .st'); if (st) st.insertAdjacentHTML('afterbegin', '<span class="pill uj">Új opciók a kérésed alapján</span>'); }
});
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));}
function ment(){ try { localStorage.setItem(KEY, JSON.stringify(S)); } catch(e) {} dbMent(); }
/* claude.ai-n publikálva (capabilities: db): a jelölések és megjegyzések az artifact adatbázisába mentődnek
   (arculat/valasztas), más gépről is látszanak, és a Claude közvetlenül kiolvassa őket. Helyi fájlként: localStorage. */
var DBDOC = null, dbT = null, dbFut = false, dbUjra = false, dbKesz = false;
function mentesJel(c, t){ var m = document.getElementById('vl-mentes'); if (m) { m.className = 'vl-mentes ' + (c || ''); m.textContent = t; } }
function dbMent(){
  if (!DBDOC || !dbKesz) return; clearTimeout(dbT);
  dbT = setTimeout(function fl(){
    if (dbFut) { dbUjra = true; return; }
    dbFut = true; mentesJel('', 'mentés…');
    var e = exportAdat();
    DBDOC.set({allapot: JSON.stringify(S), gepi: JSON.stringify(e.json), szoveg: e.szoveg, frissitve: new Date().toISOString(), verzio: D.verzio})
      .then(function(){ dbFut = false; mentesJel('ok', '✓ mentve a Claude-nál'); if (dbUjra) { dbUjra = false; dbMent(); } },
            function(err){ dbFut = false; mentesJel('hiba', 'mentés nem sikerült (' + ((err && err.code) || '?') + ')'); });
  }, 700);
}
function dbIndit(){
  if (!(window.claude && typeof window.claude.use === 'function')) return;
  window.claude.use('db').then(function(db){
    if (!db) return;
    try { DBDOC = db.doc('arculat/valasztas-v' + D.verzio); } catch(e) { return; }
    mentesJel('', 'kapcsolódás…');
    DBDOC.get().then(function(snap){
      var d = snap.exists ? snap.data() : null;
      if (d && d.allapot) { try { var r = JSON.parse(d.allapot); if (r && r.val) { S = r; D.kategoriak.forEach(function(k){ if (!S.val[k.kat]) S.val[k.kat] = {veg:null, elo:null, megj:{}, ujakat:false}; });
        $$('.vl-opt .vl-com').forEach(function(t){ var o = t.closest('.vl-opt'), k = o.closest('.vl-kat').getAttribute('data-kat'), id = o.getAttribute('data-id'); t.value = (S.val[k].megj || {})[id] || ''; t.classList.toggle('van', !!t.value.trim()); });
        alt.value = S.alt || ''; frissit(); } } catch(e) {} }
      dbKesz = true; mentesJel('ok', '✓ mentés a Claude-nál bekapcsolva');
      if (!d) dbMent();
    }, function(){ mentesJel('hiba', 'az adatbázis nem elérhető (marad a böngésző)'); });
  });
}
function eff(k){ var v = S.val[k] || {}; var kk = KAT[k]; return v.veg || v.elo || (kk && kk.ajanlott) || (kk && kk.opciok[0] && kk.opciok[0].id); }
var toastT;
function toast(t){ var el = document.getElementById('vl-toast'); el.textContent = t; el.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(function(){ el.classList.remove('on'); }, 2200); }

function tokenek(el, tok, jel){ if (!tok || el.getAttribute('data-'+jel) === tok._id) return; for (var p in tok) if (p !== '_id') el.style.setProperty(p, tok[p]); el.setAttribute('data-'+jel, tok._id); }
function szinkron(){
  $$('.elo-root.szink').forEach(function(el){
    var own = (el.getAttribute('data-own') || ':').split(':');
    D.stilusKatok.forEach(function(k){ el.setAttribute('data-'+k, k === own[0] ? own[1] : eff(k)); });
    tokenek(el, D.paletta[own[0]==='paletta' ? own[1] : eff('paletta')], 'tp');
    tokenek(el, D.betu[own[0]==='betu' ? own[1] : eff('betu')], 'tb');
  });
}
function tpl(slot, id){ var t = document.getElementById('tpl-'+slot+'-'+id); return t ? t.innerHTML : ''; }

var PAR = {'s-paper':'s-white','s-white':'s-paper','s-tint':'s-sand','s-sand':'s-tint'};
function ritmus(){
  var elozo = null;
  $$('#elo .slot').forEach(function(s){
    var sec = s.querySelector('section.sec'); if(!sec){ elozo = null; return; }
    if (sec._eredeti === undefined) sec._eredeti = sec.className;
    sec.className = sec._eredeti;
    var f = null; ['s-paper','s-white','s-tint','s-sand','s-deep','s-primary'].forEach(function(x){ if (sec.classList.contains(x)) f = x; });
    if (f && f === elozo && PAR[f]) { sec.classList.remove(f); sec.classList.add(PAR[f]); f = PAR[f]; }
    elozo = f;
  });
  $$('#elo .hat').forEach(function(h, i){ h.setAttribute('data-hn', i % 3); });
}
function eloOldal(){
  D.slotok.forEach(function(slot){
    var box = document.querySelector('#elo .slot[data-slot="'+slot+'"]'); if (!box) return;
    var id = eff(slot);
    if (box.getAttribute('data-cur') === id) return;
    box.setAttribute('data-cur', id);
    var o = (KAT[slot].opciok.filter(function(x){return x.id===id;})[0]) || {};
    box.innerHTML = '<a class="vl-slot-cimke" href="#kat-'+slot+'">'+KAT[slot].nev+' · '+id.toUpperCase()+' '+(o.nev||'')+' ↑</a>' + tpl(slot, id);
    if (window.WAG) WAG.init(box);
  });
  ritmus();
}
var elozoMozg = null;
function allapot(){
  var kesz = 0;
  D.kategoriak.forEach(function(k){
    var v = S.val[k.kat], id = eff(k.kat);
    if (v.veg) kesz++;
    $$('#kat-'+k.kat+' .vl-opt').forEach(function(o){
      var oid = o.getAttribute('data-id');
      o.classList.toggle('is-veg', v.veg === oid);
      o.classList.toggle('is-elo', !v.veg && v.elo === oid);
      var bv = o.querySelector('.veg'), be = o.querySelector('.elo');
      if (bv) { bv.classList.toggle('on', v.veg === oid); bv.innerHTML = v.veg === oid ? '✓ Végleges' : '★ Ez legyen a végleges'; }
      if (be) be.classList.toggle('on', id === oid && !v.veg);
    });
    var p = document.querySelector('#kat-'+k.kat+' .pill.allapot');
    if (p) { p.className = 'pill allapot' + (v.veg ? ' ok' : v.elo ? ' elo' : ''); p.textContent = v.veg ? '✓ Végleges: ' + v.veg.toUpperCase() : v.elo ? 'Előnézetben: ' + v.elo.toUpperCase() : 'Még nincs döntés'; }
    var a = document.querySelector('.vl-side a[href="#kat-'+k.kat+'"]');
    if (a) { a.classList.toggle('veg', !!v.veg); a.classList.toggle('elo', !v.veg && !!v.elo);
      var n = Object.keys(v.megj||{}).filter(function(x){return (v.megj[x]||'').trim();}).length; var ne = a.querySelector('.n'); ne.textContent = n ? n : ''; ne.classList.toggle('van', n>0); }
    var uj = document.querySelector('#kat-'+k.kat+' .ujak input'); if (uj) uj.checked = !!v.ujakat;
  });
  document.querySelector('.vl-prog .bar i').style.width = (kesz / D.kategoriak.length * 100) + '%';
  document.querySelector('.vl-prog span').textContent = kesz + ' / ' + D.kategoriak.length + ' végleges';
}
function frissit(){
  szinkron(); eloOldal(); allapot(); ment();
  var m = eff('mozgas'); if (m !== elozoMozg) { elozoMozg = m; var e = document.getElementById('elo'); $$('[data-rv]', e).forEach(function(x){ x.classList.remove('in','rv-kesz'); }); if (window.WAG) WAG.reveal(e); }
}

// előnézetek
function nagyitas(){
  $$('.vl-prev[data-zoom]').forEach(function(p){
    var r = p.querySelector('.elo-root'); if (!r) return;
    var z = p.clientWidth / D.prevW; r.style.zoom = z;
    p.classList.toggle('levag', r.getBoundingClientRect().height > p.clientHeight + 4);
  });
}
$$('.vl-prev[data-tpl]').forEach(function(p){
  var r = p.querySelector('.elo-root'); var t = p.getAttribute('data-tpl').split(':');
  r.innerHTML = (t[0]==='nav' ? '' : '') + tpl(t[0], t[1]) + (t[0]==='nav' ? '<div class="vl-navfill s-tint sec" style="background:var(--c-tint);color:var(--c-ink-3)">(ide kerül a hero)</div>' : '');
});
$$('.vl-prev .elo-root').forEach(function(r){ $$('.hat', r).forEach(function(h, i){ h.setAttribute('data-hn', i % 3); }); });
szinkron();
$$('.vl-prev .elo-root').forEach(function(r){ if (window.WAG) WAG.init(r, true); });
nagyitas(); window.addEventListener('resize', nagyitas);

// események
document.addEventListener('click', function(e){
  var b = e.target.closest('[data-akcio]'); if (!b) return;
  var a = b.getAttribute('data-akcio'), o = b.closest('.vl-opt'), k = o && o.closest('.vl-kat').getAttribute('data-kat'), id = o && o.getAttribute('data-id');
  if (a === 'elo') { S.val[k].elo = id; if (S.val[k].veg && S.val[k].veg !== id) S.val[k].veg = null; frissit(); toast('Lent az élő oldalon már így látszik: ' + id.toUpperCase()); }
  if (a === 'veg') { var v = S.val[k]; if (v.veg === id) { v.veg = null; toast('Visszavontad a véglegest'); } else { v.veg = id; v.elo = id; toast('✓ ' + KAT[k].nev + ': ' + id.toUpperCase() + ' a végleges'); } frissit(); }
  if (a === 'play') { var r = o.querySelector('.elo-root'); $$('[data-rv]', r).forEach(function(x){ x.classList.remove('in','rv-kesz'); }); void r.offsetWidth; WAG.reveal(r); }
});
document.addEventListener('click', function(e){
  var p = e.target.closest('.vl-prev'); if (!p || e.target.closest('a,button,[data-tab],.rail')) return;
  var o = p.closest('.vl-opt'); var k = o.closest('.vl-kat').getAttribute('data-kat'); var id = o.getAttribute('data-id');
  S.val[k].elo = id; if (S.val[k].veg && S.val[k].veg !== id) S.val[k].veg = null; frissit(); toast('Előnézetben: ' + id.toUpperCase() + ' (lent az élő oldalon)');
});
document.addEventListener('click', function(e){ var a = e.target.closest('.vl-prev a[href]'); if (a) e.preventDefault(); }, true);
var mentT;
$$('.vl-opt .vl-com').forEach(function(t){
  var o = t.closest('.vl-opt'), k = o.closest('.vl-kat').getAttribute('data-kat'), id = o.getAttribute('data-id');
  t.value = (S.val[k].megj || {})[id] || ''; t.classList.toggle('van', !!t.value.trim());
  t.addEventListener('input', function(){ S.val[k].megj[id] = t.value; t.classList.toggle('van', !!t.value.trim()); clearTimeout(mentT); mentT = setTimeout(function(){ ment(); allapot(); }, 400); });
});
$$('.ujak input').forEach(function(c){ c.addEventListener('change', function(){ S.val[c.closest('.vl-kat').getAttribute('data-kat')].ujakat = c.checked; ment(); }); });
var alt = document.getElementById('vl-altalanos'); alt.value = S.alt || ''; alt.addEventListener('input', function(){ S.alt = alt.value; clearTimeout(mentT); mentT = setTimeout(ment, 400); });

document.getElementById('vl-ajanlott').addEventListener('click', function(){
  var n = 0; D.kategoriak.forEach(function(k){ var v = S.val[k.kat]; if (!v.veg) { v.veg = v.elo || k.ajanlott; n++; } });
  frissit(); toast(n ? n + ' elemnél elfogadtad az ajánlottat (vagy az előnézetet)' : 'Már mindenhol van végleges');
});
var resetT = null;
document.getElementById('vl-reset').addEventListener('click', function(){
  var b = this; if (!resetT) { b.textContent = '⚠ Biztos? Kattints újra'; resetT = setTimeout(function(){ resetT = null; b.textContent = '↺ Újrakezdés'; }, 3500); return; }
  clearTimeout(resetT); resetT = null; b.textContent = '↺ Újrakezdés';
  S = {val:{}, alt:''}; D.kategoriak.forEach(function(k){ S.val[k.kat] = {veg:null, elo:null, megj:{}, ujakat:false}; });
  $$('.vl-opt .vl-com').forEach(function(t){ t.value=''; t.classList.remove('van'); }); alt.value=''; frissit();
});
$$('[data-nezet]').forEach(function(b){ b.addEventListener('click', function(){
  var k = document.getElementById('elo-keret'), n = b.getAttribute('data-nezet');
  if (n === 'mobil' || n === 'asztal') { k.classList.toggle('mobil', n === 'mobil'); $$('[data-nezet="mobil"],[data-nezet="asztal"]').forEach(function(x){ x.classList.toggle('on', x===b); }); }
  if (n === 'tiszta') { k.classList.toggle('tiszta'); b.classList.toggle('on'); }
}); });

// export
function exportAdat(){
  var sor = [], json = {marka: D.marka.slug, verzio: D.verzio, datum: (function(d){ function k(n){return (n<10?'0':'')+n;} return d.getFullYear()+'-'+k(d.getMonth()+1)+'-'+k(d.getDate())+' '+k(d.getHours())+':'+k(d.getMinutes()); })(new Date()), valasztas: {}, altalanos: S.alt || ''};
  var kesz = D.kategoriak.filter(function(k){ return S.val[k.kat].veg; }).length;
  sor.push('=== ARCULAT-VÁLASZTÁS: ' + D.marka.nev + ' (v' + D.verzio + ') · ' + json.datum + ' ===');
  sor.push('Végleges döntés: ' + kesz + ' / ' + D.kategoriak.length + ' elemnél.');
  sor.push('');
  D.kategoriak.forEach(function(k, i){
    var v = S.val[k.kat], nev = function(id){ var o = k.opciok.filter(function(x){return x.id===id;})[0]; return o ? id.toUpperCase() + ' „' + o.nev + '”' : id; };
    var fej = '[' + (i+1) + '] ' + k.nev + ' → ';
    if (v.veg) fej += 'VÉGLEGES: ' + nev(v.veg); else if (v.elo) fej += 'nincs végleges (előnézetben: ' + nev(v.elo) + ')'; else fej += 'nincs döntés (ajánlott: ' + nev(k.ajanlott) + ')';
    if (v.ujakat) fej += '   ⚠ ÚJ OPCIÓKAT KÉR';
    sor.push(fej);
    var mj = {}; Object.keys(v.megj || {}).forEach(function(id){ var t = (v.megj[id] || '').trim(); if (t) { mj[id] = t; sor.push('    • ' + nev(id) + ': ' + t.replace(/\n+/g,' / ')); } });
    json.valasztas[k.kat] = {vegleges: v.veg, elonezet: v.elo, ajanlott: k.ajanlott, megjegyzesek: mj, ujakat: !!v.ujakat, opciok: k.opciok.map(function(x){return x.id;})};
  });
  if ((S.alt||'').trim()) { sor.push(''); sor.push('Általános megjegyzés: ' + S.alt.trim()); }
  sor.push(''); sor.push('--- GÉPI ADAT (ezt ne töröld, ebből dolgozik tovább a Claude) ---'); sor.push(JSON.stringify(json));
  return {szoveg: sor.join('\n'), json: json};
}
var modal = document.getElementById('vl-modal'), mt = modal.querySelector('textarea');
document.getElementById('vl-export').addEventListener('click', function(){ mt.value = exportAdat().szoveg; modal.classList.add('on'); });
document.getElementById('vl-export2').addEventListener('click', function(){ mt.value = exportAdat().szoveg; modal.classList.add('on'); });
modal.addEventListener('click', function(e){ if (e.target === modal || e.target.closest('[data-bezar]')) modal.classList.remove('on'); });
document.getElementById('vl-masol').addEventListener('click', function(){
  var ok = function(){ toast('Kimásolva. Illeszd be a Claude-os beszélgetésbe.'); };
  if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(mt.value).then(ok, function(){ mt.select(); document.execCommand('copy'); ok(); });
  else { mt.select(); document.execCommand('copy'); ok(); }
});
document.getElementById('vl-letolt').addEventListener('click', function(){
  try { var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([JSON.stringify(exportAdat().json, null, 1)], {type:'application/json'})); a.download = 'valasztas.json'; document.body.appendChild(a); a.click(); a.remove(); }
  catch(e) { toast('A letöltés itt nem engedélyezett: használd a Másolás gombot.'); }
});
// mozgás-demó: automatikus ismétlés, lassítás, élő oldal újrajátszása
var mozgAuto = true;
function mozgUjra(r){ $$('[data-rv]', r).forEach(function(x){ x.classList.remove('in','rv-kesz'); }); void r.offsetWidth; if (window.WAG) WAG.reveal(r); }
var mozgLathato = [];
if ('IntersectionObserver' in window) {
  var mio = new IntersectionObserver(function(es){ es.forEach(function(e){ var i = mozgLathato.indexOf(e.target); if (e.isIntersecting && i < 0) mozgLathato.push(e.target); if (!e.isIntersecting && i >= 0) mozgLathato.splice(i, 1); }); });
  $$('#kat-mozgas .vl-prev .elo-root').forEach(function(r){ mio.observe(r); });
}
setInterval(function(){ if (mozgAuto) mozgLathato.forEach(mozgUjra); }, 4000);
$$('[data-mozg]').forEach(function(b){ b.addEventListener('click', function(){
  if (b.getAttribute('data-mozg') === 'auto') { mozgAuto = !mozgAuto; b.classList.toggle('on', mozgAuto); }
  else { var k = document.getElementById('kat-mozgas'); var on = !k.classList.contains('vl-lassu'); k.classList.toggle('vl-lassu', on); b.classList.toggle('on', on); $$('#kat-mozgas .vl-prev .elo-root').forEach(mozgUjra); }
}); });
var mel = document.getElementById('vl-mozg-elo');
if (mel) mel.addEventListener('click', function(){ var e = document.getElementById('elo'); $$('[data-rv]', e).forEach(function(x){ x.classList.remove('in','rv-kesz'); }); void e.offsetWidth; if (window.WAG) WAG.reveal(e); toast('A beúszás újraindult: görgess végig az élő oldalon'); });
frissit();
dbIndit();
})();
"""


# ------------------------------------------------------------------ demók a globális stílusokhoz

def demo_html(kat, ctx, opc):
    k = ctx.get("kinalat", {})
    h = ctx.get("hero", {})
    el = (k.get("elemek") or [{}])
    e0, e1 = el[0], el[1 % len(el)]
    fotok = [x for x in (g(ctx, "hero", "fotok") or [])] + [x.get("foto") for x in el if x.get("foto")]
    ikonok = [x.get("ikon") for x in el if x.get("ikon")] or ["teszta"]
    t = ctx.get("tenyek", {})
    if kat == "cim":
        return (f'<section class="sec s-paper" style="padding:34px 0 30px"><div class="wrap">{shead({"kicker": k.get("kicker"), "cim": k.get("cim") or h.get("cim"), "lead": None}, rv=False)}</div></section>'
                f'<section class="sec s-primary" style="padding:26px 0 30px"><div class="wrap"><header class="shead" style="margin-bottom:0"><h2 class="cim" style="font-size:2rem">{md(g(ctx, "latogatas", "cim") or h.get("cim", ""))}</h2></header></div></section>')
    if kat == "alcim":
        return (f'<section class="sec s-paper" style="padding:30px 0 16px"><div class="wrap">{shead({"kicker": k.get("kicker"), "cim": k.get("cim")}, rv=False)}</div></section>'
                f'<section class="sec s-tint" style="padding:26px 0 26px"><div class="wrap">{shead({"kicker": t.get("kicker") or g(ctx, "folyamat", "kicker"), "cim": g(ctx, "folyamat", "cim")}, bal=True, rv=False)}</div></section>')
    if kat == "gomb":
        g1 = {"szoveg": g(h, "cta1", "szoveg") or "Megnézem", "href": "#"}
        g2 = {"szoveg": g(h, "cta2", "szoveg") or "Hívj minket", "href": "#"}
        return (f'<section class="sec s-paper" style="padding:34px 0"><div class="wrap"><div class="gombsor" style="justify-content:center">{btn(g1)}{btn(g2, alt=True, ikon="tel")}</div></div></section>'
                f'<section class="sec s-primary" style="padding:26px 0"><div class="wrap"><div class="gombsor" style="justify-content:center">{btn(g1)}{btn(g2, alt=True, ikon="")}</div></div></section>'
                f'<section class="sec s-deep" style="padding:26px 0"><div class="wrap"><div class="gombsor" style="justify-content:center">{btn(g1)}{btn(g2, alt=True, ikon="")}</div></div></section>')
    if kat == "kartya":
        c1 = (f'<article class="krt"><div class="krt-fej">{ik(e0.get("ikon"))}<h3 class="krt-h">{md(e0.get("nev", ""))}</h3></div>'
              f'<p class="krt-p">{md(e0.get("leiras", ""))}</p><p class="krt-meta">{esc(e0.get("ar", ""))}</p></article>')
        c2 = (f'<article class="krt">{foto(ctx, e1.get("foto"), "16/10", "krt-kep")}<div class="krt-fej">{ik(e1.get("ikon"))}<h3 class="krt-h">{md(e1.get("nev", ""))}</h3></div>'
              f'<p class="krt-p">{md(e1.get("leiras", ""))}</p><p class="krt-meta">{esc(e1.get("ar", ""))}</p></article>')
        return f'<section class="sec s-paper" style="padding:26px 0"><div class="wrap" style="padding:0 22px"><div class="racs" style="--oszlop:2">{c1}{c2}</div></div></section>'
    if kat == "foto":
        fs = (fotok + [None, None, None])[:3]
        return (f'<section class="sec s-paper" style="padding:34px 0 40px"><div class="wrap" style="padding:0 30px"><div style="display:grid;grid-template-columns:1fr 1.2fr 1fr;gap:24px;align-items:center">'
                f'{foto(ctx, fs[0], "4/5", felirat=None)}{foto(ctx, fs[1], "1/1", felirat=g(ctx, "fotok", fs[1] or "", "alt") or None)}{foto(ctx, fs[2], "4/5")}</div></div></section>')
    if kat == "felulet":
        return (f'<section class="sec s-paper tx" style="padding:40px 0 34px"><div class="wrap">{shead({"kicker": k.get("kicker"), "cim": k.get("cim")}, rv=False)}</div></section>'
                f'<section class="sec s-tint tx" style="padding:34px 0"><div class="wrap"><p class="lead" style="text-align:center;margin:0 auto">{md(k.get("lead") or h.get("lead", ""))}</p></div></section>')
    if kat == "dekor":
        return (f'<section class="sec s-paper" style="padding:58px 0 72px;min-height:300px">{dk(ctx, "hero", matrica=True)}<div class="wrap">{shead({"kicker": h.get("kicker"), "cim": k.get("cim")}, rv=False)}</div></section>'
                f'<section class="sec s-tint" style="padding:40px 0 50px">{dk(ctx, "kinalat")}<div class="wrap"><p class="lead" style="text-align:center;margin:0 auto">{md(k.get("lead") or "")}</p></div></section>')
    if kat == "hatar":
        return (f'<section class="sec s-paper" style="padding:40px 0 64px"><div class="wrap"><p class="lead" style="margin:0 auto;text-align:center">{md(h.get("lead", ""))}</p></div></section>'
                f'<section class="sec s-tint" style="padding:64px 0 40px">{hat(ctx)}<div class="wrap">{shead({"kicker": k.get("kicker"), "cim": k.get("cim")}, rv=False)}</div></section>'
                f'<section class="sec s-deep" style="padding:60px 0 34px">{hat(ctx, masod=True)}<div class="wrap"><p style="text-align:center;margin:0">{esc(g(ctx, "kapcsolat", "cim"))}</p></div></section>')
    if kat == "mozgas":
        fs = (fotok + [None, None])[:2]
        kk = "".join(f'<article class="krt" data-rv style="min-height:150px"><div class="krt-fej">{ik(x.get("ikon"))}<h3 class="krt-h">{md(x.get("nev", ""))}</h3></div>'
                     f'<p class="krt-p">{md(x.get("leiras", ""))[:70]}…</p></article>' for x in el[:3])
        return (f'<section class="sec s-tint" style="padding:30px 0 34px"><div class="wrap" style="padding:0 22px">'
                f'<header class="shead" data-rv style="margin-bottom:18px"><h2 class="cim" style="font-size:1.8rem">{md(k.get("cim", ""))}</h2></header>'
                f'<div class="racs" style="--oszlop:3">{kk}</div>'
                f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px"><div data-rv>{foto(ctx, fs[0], "16/9")}</div><div data-rv>{foto(ctx, fs[1], "16/9")}</div></div>'
                f'<div class="gombsor" data-rv style="justify-content:center;margin-top:20px">{btn({"szoveg": g(h, "cta1", "szoveg") or "Megnézem", "href": "#"})}</div></div></section>')
    if kat == "ikon":
        return (f'<section class="sec s-paper" style="padding:26px 0 22px"><div class="wrap" style="padding:0 22px"><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px 10px;justify-items:center">'
                + "".join(f'<span class="ik ik-{esc(n)}" style="--ik:84px"></span>' for n in ctx.get("_ikon_nevek", [])) + '</div></div></section>')
    if kat == "paletta":
        return (f'<div class="pal-sav">' + "".join(f'<i style="background:var({v})" title="{v}"></i>' for v in
                ("--c-primary", "--c-accent", "--c-accent2", "--c-paper", "--c-tint", "--c-sand", "--c-deep", "--c-ink")) + '</div>'
                f'<section class="sec s-paper" style="padding:28px 0 24px"><div class="wrap">{shead({"kicker": h.get("kicker"), "cim": h.get("cim")}, rv=False)}'
                f'<div class="gombsor" style="justify-content:center">{btn({"szoveg": g(h, "cta1", "szoveg") or "Megnézem", "href": "#"})}{btn({"szoveg": g(h, "cta2", "szoveg") or "Hívj", "href": "#"}, alt=True, ikon="")}</div></div></section>'
                f'<section class="sec s-deep" style="padding:20px 0"><div class="wrap" style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">{chips(h.get("badgek") or [])}</div></section>')
    if kat == "betu":
        return (f'<section class="sec s-paper" style="padding:28px 0 26px"><div class="wrap" style="padding:0 30px">'
                f'<div style="display:flex;align-items:baseline;gap:18px;flex-wrap:wrap"><span style="font-family:var(--f-display);font-weight:var(--w-display);font-size:4.2rem;line-height:1;color:var(--c-primary-text);text-transform:var(--tt-display)">Aa Őű</span>'
                f'<span class="kezi" style="font-size:calc(var(--fs-hand)*1.5rem)">{esc(g(ctx, "marka", "szlogen"))}</span></div>'
                f'<h2 class="cim" style="font-size:2rem;margin:14px 0 10px">{md(h.get("cim", ""))}</h2>'
                f'<p style="color:var(--c-ink-2);margin:0 0 12px;max-width:60ch">{md(h.get("lead", ""))}</p>'
                f'<p class="mono" style="font-size:.78rem;text-transform:uppercase;color:var(--c-ink-3);margin:0">{esc(g(ctx, "kapcsolat", "nyitva_rovid"))}</p></div></section>')
    return ""


PAL_CSS = r"""
.pal-sav{display:grid;grid-template-columns:repeat(8,1fr);height:34px}
.pal-sav i{display:block}
"""


def epit(spec, ki, elozo=None, engedd=False):
    opc = epito.opciok(spec)
    hibak = epito.ellenoriz(opc, spec)
    if hibak:
        print("A választó NEM felel meg a szabványnak (minden futásnak ugyanazt a 22 kategóriát kell adnia):")
        for h in hibak:
            print("  -", h)
        if not engedd:
            raise SystemExit(2)
        print("  (--engedd: építés mégis, csak fejlesztéshez)")
    if opc["ikon"].get("tartalek"):
        print("  ! Nincsenek generált ikonok: az ikon-kategória a márka formáiból épül (tartalék). "
              "Valódi ikonokhoz: ikon_generalo.py (OpenAI-kulcs).")
    logo_info, logo_css = epito.logo_elokeszit(spec)
    ctx = epito.ctx_keszit(spec, logo_info)
    ctx["_ikon_nevek"] = epito.ikon_nevek(spec)
    pal_tok = epito.paletta_tokenek(opc)
    bet_tok = epito.betu_tokenek(opc)
    for d, t in list(pal_tok.items()):
        t["_id"] = d
    for d, t in list(bet_tok.items()):
        t["_id"] = d
    sorrend = spec.get("szekcio_sorrend") or epito.ALAP_SORREND

    # --- sablonok (minden szekció-változat egyszer, <template>-ben)
    tpls = []
    for slot in SZEKCIOK:
        for x in opc[slot]["lista"]:
            try:
                h = epito.render_szekcio(x, ctx)
            except Exception as ex:
                h = f'<div style="padding:40px;color:#b00">Hiba a {slot}/{x["id"]} változatban: {esc(ex)}</div>'
                print(f"  ! render hiba {slot}/{x['id']}: {ex}")
            tpls.append(f'<template id="tpl-{slot}-{x["id"]}">{h}</template>')

    # --- kategória-blokkok
    kat_adat = []
    blokkok = []
    szam = 0
    oldalsav = []
    for csop, katok in epito.csoportok(spec):
        katok = [k for k in katok if k in opc and opc[k]["lista"] and (k not in SZEKCIOK or k in sorrend)]
        if not katok:
            continue
        blokkok.append(f'<div class="vl-csop">{esc(csop)}</div>')
        oldalsav.append(f'<h6>{esc(csop)}</h6>')
        for kat in katok:
            szam += 1
            nev, leiras = KAT_NEV[kat]
            o = opc[kat]
            if kat == "ikon" and o.get("tartalek"):
                leiras = "Tartalék: a márka saját formái 5 kezelésben (generált ikonokhoz OpenAI-kulcs kell)."
            nagy = kat in SZEKCIOK
            kat_adat.append({"kat": kat, "nev": nev, "ajanlott": o["ajanlott"],
                             "opciok": [{"id": x["id"], "nev": x.get("nev", x["id"])} for x in o["lista"]]})
            kartyak = []
            for x in o["lista"]:
                aj = '<span class="aj">Ajánlott</span>' if x["id"] == o["ajanlott"] else ""
                eg = '<span class="egy">Csak nektek</span>' if x.get("egyedi") else ""
                if nagy:
                    prev = (f'<div class="vl-prev" data-zoom data-tpl="{kat}:{x["id"]}"><div class="elo-root szink" data-own="{kat}:{x["id"]}" '
                            f'style="width:{PREV_W}px"></div></div>')
                else:
                    play = ('<button class="ub vl-mozg-play" type="button" data-akcio="play">▶ Lejátszás</button>' if kat == "mozgas" else "")
                    prev = (f'<div class="vl-prev">{play}<div class="elo-root szink" data-own="{kat}:{x["id"]}">{demo_html(kat, ctx, opc)}</div></div>')
                kartyak.append(
                    f'<div class="vl-opt" data-id="{esc(x["id"])}"><span class="badge">✓ Végleges</span>{prev}<div class="vl-body">'
                    f'<div class="vl-nev"><span class="id">{esc(x["id"])}</span><h3>{esc(x.get("nev", ""))}</h3>{aj}{eg}</div>'
                    f'<p class="vl-miert">{md(x.get("miert", ""))}</p>'
                    f'<div class="vl-act"><button class="ub elo" type="button" data-akcio="elo">👁 Kipróbálom lent</button>'
                    f'<button class="ub veg" type="button" data-akcio="veg">★ Ez legyen a végleges</button></div>'
                    f'<textarea class="vl-com" placeholder="Megjegyzés ehhez az opcióhoz: mi tetszik benne, mi nem, mit változtatnál?"></textarea>'
                    f'</div></div>')
            mozg_sor = ('<div class="vl-mozg-sor"><button class="ub on" type="button" data-mozg="auto">⟳ Automatikus ismétlés</button>'
                        '<button class="ub" type="button" data-mozg="lassu">🐢 Lassítva (½×)</button>'
                        '<small>Minden előnézet 4 másodpercenként újrajátssza a beúszást, amíg látszik.</small></div>') if kat == "mozgas" else ""
            blokkok.append(
                f'<section class="vl-kat" id="kat-{kat}" data-kat="{kat}"><header><span class="sz">{szam}</span><div><h2>{esc(nev)}</h2>'
                f'<p>{esc(leiras)} {len(o["lista"])} opció.</p></div><div class="st"><span class="pill allapot">Még nincs döntés</span>'
                f'<label class="ujak"><input type="checkbox"> Egyik sem az igazi, kérek újakat</label></div></header>{mozg_sor}'
                f'<div class="vl-opts{" nagy" if nagy else ""}">{"".join(kartyak)}</div></section>')
            oldalsav.append(f'<a href="#kat-{kat}"><span class="d"></span>{esc(nev)}<span class="n"></span></a>')
    oldalsav.append('<a class="elolap" href="#elo-sec">▼ Az élő oldal</a>')

    # --- élő oldal
    slot_html = "".join(f'<div class="slot" data-slot="{s}"></div>' for s in sorrend if s in SZEKCIOK)

    # --- CSS
    fams = epito.betu_csaladok(opc["betu"]["lista"])
    furl = alap.google_fonts_url(fams)
    css = "\n".join([UI_CSS, PAL_CSS, ALAP_CSS, epito.motivum_css(spec), logo_css, epito.stilus_css_osszes(opc),
                     epito.szekcio_css_osszes(opc), epito.ikonok_css(spec), epito.fotok_css(spec), spec.get("egyedi_css", "")])
    for kat in ("paletta", "betu"):
        pass
    alapert = pal_tok.get(opc["paletta"]["ajanlott"]) or {}
    alapbetu = bet_tok.get(opc["betu"]["ajanlott"]) or {}
    root_tok = ".elo-root{" + alap.tokenek_css({k: v for k, v in alapert.items() if k != "_id"}) + ";" + \
               alap.tokenek_css({k: v for k, v in alapbetu.items() if k != "_id"}) + "}"

    D = {"marka": {"nev": g(spec, "marka", "nev"), "slug": g(spec, "marka", "slug") or "marka"},
         "verzio": spec.get("verzio", 1), "kategoriak": kat_adat, "paletta": pal_tok, "betu": bet_tok,
         "stilusKatok": STILUS_KATOK, "slotok": [s for s in sorrend if s in SZEKCIOK], "prevW": PREV_W,
         "elozo": elozo or None}
    prof = spec.get("profil") or {}
    sw = "".join(f'<i style="background:{esc(c)}" title="{esc(c)}"></i>' for c in prof.get("talalt_szinek", []))
    mot = "".join(f'<i style="-webkit-mask-image:url(&quot;{alap.motivum_uri(v)}&quot;);mask-image:url(&quot;{alap.motivum_uri(v)}&quot;)"></i>'
                  for v in (g(spec, "motivum", "formak") or {}).values())
    lg_css_mini = ""
    if logo_info:
        lg_css_mini = '<i class="lg"></i>'
    intro = (f'<div class="vl-intro"><div><h1>{esc(g(spec, "marka", "nev"))} · arculat-választó</h1>'
             f'<p>Minden arculati elemből több, egymástól tényleg különböző változatot készítettem a mostani oldalad, a '
             f'logód, a fotóid és a szakmád világa alapján. Nézd végig, és döntsd el, mi legyen a végleges.</p><ol>'
             f'<li><b>Kattints</b> egy opcióra (vagy a „Kipróbálom lent” gombra): legalul az <b>élő oldalon</b> azonnal úgy jelenik meg.</li>'
             f'<li>Ha megvan, jelöld: <b>★ Ez legyen a végleges</b>. Bármikor átjelölheted.</li>'
             f'<li>Írj <b>megjegyzést</b> bármelyik opcióhoz: mi tetszik, mi nem, mit vinnél át egy másikból.</li>'
             f'<li>A végén: <b>Visszajelzés másolása</b> → illeszd be a Claude-os beszélgetésbe. Ebből készül el a végleges oldal.</li></ol>'
             f'<p style="margin-top:10px;font-size:13px">A jelöléseid ebben a böngészőben automatikusan mentődnek. Ahol még nincs döntés, ott az '
             f'<b>Ajánlott</b> opció látszik az élő oldalon.</p></div>'
             f'<div class="prof"><b>Amit a mostani oldaladból kiolvastam</b>{md(prof.get("osszefoglalo", ""))}'
             + (f'<b>Talált színek</b><div class="sw">{sw}</div>' if sw else "")
             + (f'<b>Talált betűk</b>{esc(", ".join(prof.get("talalt_betuk", [])))}' if prof.get("talalt_betuk") else "")
             + (f'<b>A márka saját formái (motívumok)</b><div class="mot">{mot}</div><p style="margin:6px 0 0;font-size:12.5px;color:#6d675e">{md(prof.get("motivumok", ""))}</p>' if mot else "")
             + '</div></div>')
    alt = ('<div class="vl-alt"><h2>Általános megjegyzés</h2><p style="margin:0 0 10px;color:#5d5850;font-size:14px">Bármi, ami nem egy '
           'konkrét opcióhoz tartozik: hangulat, szövegek, fotók, amit még látni szeretnél.</p>'
           '<textarea id="vl-altalanos" class="vl-com" style="min-height:90px" placeholder="Pl.: a szövegekben legyen több humor; a fotók közül a belső teres a kedvencem…"></textarea></div>')
    ico_logo = ""
    if logo_info:
        ico_logo = '<i class="lg"></i>'
    d_json = json.dumps(D, ensure_ascii=False).replace("</", "<\\/")
    html = f"""<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(g(spec, "marka", "nev"))} · arculat-választó</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{f'<link rel="stylesheet" href="{esc(furl)}">' if furl else ''}
<style>{css}
{root_tok}</style></head><body>
<header class="vl-top"><div class="mk">{ico_logo}<div>{esc(g(spec, "marka", "nev"))}<small>Arculat-választó · v{spec.get("verzio", 1)}</small></div></div>
<div class="vl-prog"><div class="bar"><i></i></div><span>0 végleges</span></div>
<span class="vl-mentes" id="vl-mentes"></span><div class="gombok"><button class="ub" id="vl-reset" type="button" title="Minden jelölés törlése">↺ Újrakezdés</button>
<button class="ub" id="vl-ajanlott" type="button" title="Ahol nincs végleges, az ajánlott (vagy az előnézetben lévő) opció lesz az">✓ Ajánlottak elfogadása</button>
<a class="ub" href="#elo-sec">▼ Élő oldal</a><button class="ub fo" id="vl-export" type="button">📋 Visszajelzés másolása</button></div></header>
<div class="vl-lay"><nav class="vl-side">{''.join(oldalsav)}</nav><main class="vl-main">{intro}{''.join(blokkok)}{alt}
<section class="vl-elo-sec" id="elo-sec"><div class="vl-elo-fej"><div><h2>Az élő oldal a kiválasztott elemekből</h2>
<p>Ahol még nincs döntés: az előnézetben lévő, vagy az ajánlott opció látszik. Vidd az egeret egy blokkra: látod, melyik opció.</p></div>
<div class="gombok"><button class="ub" type="button" id="vl-mozg-elo">▶ Mozgás lejátszása</button><button class="ub on" type="button" data-nezet="asztal">🖥 Asztali</button><button class="ub" type="button" data-nezet="mobil">📱 Mobil</button>
<button class="ub" type="button" data-nezet="tiszta">Címkék elrejtése</button></div></div>
<div id="elo-keret"><div id="elo" class="elo-root szink">{slot_html}</div></div></section></main></div>
<div class="vl-fab"><button class="ub zold" id="vl-export2" type="button">📋 Visszajelzés másolása</button></div>
<div class="vl-modal" id="vl-modal"><div class="ab"><h3>Visszajelzés a Claude-nak</h3>
<p>Kattints a <b>Másolás</b> gombra, és illeszd be a Claude-os beszélgetésbe (vagy mentsd el <code>valasztas.json</code> néven).
Ebből készül el a végleges oldal és a teljes designrendszer. Ha a Másolás gomb nem működik: kattints a szövegbe,
<b>Ctrl/Cmd+A</b>, majd <b>Ctrl/Cmd+C</b>.</p><textarea readonly></textarea>
<div class="gombok"><button class="ub" type="button" data-bezar>Bezárás</button><button class="ub" id="vl-letolt" type="button">⬇ Letöltés (.json)</button>
<button class="ub fo" id="vl-masol" type="button">📋 Másolás</button></div></div></div>
<div class="vl-toast" id="vl-toast"></div>
{''.join(tpls)}
<script id="vl-data" type="application/json">{d_json}</script>
<script>{FUTAS_JS}
WAG.NYITVA = {json.dumps(g(spec, "kapcsolat", "nyitva_gep") or None)};</script>
<script>{UI_JS}</script>
</body></html>"""
    from pathlib import Path
    Path(ki).write_text(html, encoding="utf-8")
    return len(html)
