# -*- coding: utf-8 -*-
"""Az oldal futásidejű JS-e (élő előnézet ÉS kész oldal): beúszás, mobilmenü, sín, fülek, galéria, „most nyitva”.
Minden függvény egy gyökérre (root) fut, így az élő előnézetben egy kicserélt szekcióra újra lehet hívni."""

FUTAS_JS = r"""
(function(){
var W = window.WAG = window.WAG || {};
function $$(r,s){return Array.prototype.slice.call(r.querySelectorAll(s));}
var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

W.reveal = function(root, azonnal){
  var host = root.closest ? (root.closest('.elo-root') || root) : root;
  var mozg = host.getAttribute('data-mozgas');
  var els = $$(root,'[data-rv]');
  els.forEach(function(el){
    var sibs = el.parentNode ? Array.prototype.filter.call(el.parentNode.children,function(x){return x.hasAttribute('data-rv');}) : [el];
    el.style.setProperty('--i', Math.min(sibs.indexOf(el), 8));
  });
  if (azonnal || RM || mozg === 'm5' || !('IntersectionObserver' in window)) { els.forEach(function(e){e.classList.add('in');}); host.classList.remove('js-rv'); return; }
  host.classList.add('js-rv');
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }); },{rootMargin:'0px 0px -10% 0px', threshold:0.01});
  els.forEach(function(e){ if(!e.classList.contains('in')) io.observe(e); });
  setTimeout(function(){ els.forEach(function(e){e.classList.add('in');}); }, 4000);
};
document.addEventListener('transitionend', function(e){
  var t = e.target; if (t && t.hasAttribute && t.hasAttribute('data-rv') && e.propertyName === 'clip-path') t.classList.add('rv-kesz');
}, true);

W.menu = function(root){
  $$(root,'[data-mnu]').forEach(function(b){
    if (b._wag) return; b._wag = 1;
    b.addEventListener('click', function(){ var n = b.closest('[data-nav]'); if(n) n.classList.toggle('nyit'); });
  });
  $$(root,'[data-nav] .links a').forEach(function(a){ a.addEventListener('click', function(){ var n=a.closest('[data-nav]'); if(n) n.classList.remove('nyit'); }); });
};

W.rail = function(root){
  $$(root,'[data-railw]').forEach(function(w){
    if (w._wag) return; w._wag = 1;
    var r = w.querySelector('.rail'), bar = w.querySelector('.rail-bar i');
    if (!r) return;
    function sync(){ var max = r.scrollWidth - r.clientWidth; var p = max>0 ? r.scrollLeft/max : 1; var vis = r.scrollWidth? r.clientWidth/r.scrollWidth : 1;
      if(bar){ bar.style.width = Math.max(12, vis*100)+'%'; bar.style.transform = 'translateX('+(p*(100/Math.max(vis,.01)-100))+'%)'; } }
    $$(w,'[data-rail]').forEach(function(b){ b.addEventListener('click', function(){
      var k = r.firstElementChild; var step = k ? k.getBoundingClientRect().width + 22 : 300;
      r.scrollBy({left: step * (+b.getAttribute('data-rail')), behavior:'smooth'}); }); });
    r.addEventListener('scroll', sync, {passive:true}); window.addEventListener('resize', sync); sync();
    var down=false,x0=0,l0=0,moved=0;
    r.addEventListener('pointerdown',function(e){ if(e.pointerType==='touch') return; down=true; moved=0; x0=e.clientX; l0=r.scrollLeft; });
    window.addEventListener('pointermove',function(e){ if(!down) return; var dx=e.clientX-x0; moved=Math.abs(dx); r.scrollLeft=l0-dx; });
    window.addEventListener('pointerup',function(){ down=false; });
    r.addEventListener('click',function(e){ if(moved>6){ e.preventDefault(); e.stopPropagation(); } },true);
  });
};

W.tabs = function(root){
  $$(root,'[data-tabs]').forEach(function(t){
    if (t._wag) return; t._wag = 1;
    $$(t,'.tb').forEach(function(b){ b.addEventListener('click', function(){
      var k = b.getAttribute('data-tab');
      $$(t,'.tb').forEach(function(x){ x.classList.toggle('on', x===b); });
      $$(t,'.pane').forEach(function(p){ p.classList.toggle('on', p.getAttribute('data-tab')===k); });
    }); });
  });
};

W.galeria = function(root){
  $$(root,'[data-galw]').forEach(function(w){
    if (w._wag) return; w._wag = 1;
    var sec = w.closest('section') || root, big = w.querySelector('.nagy'), fc = w.querySelector('.fc');
    $$(sec,'.th[data-gal]').forEach(function(b){ b.addEventListener('click', function(){
      $$(sec,'.th').forEach(function(x){ x.classList.toggle('on', x===b); });
      if (big) { big.style.opacity = .2; setTimeout(function(){ big.className = 'ph nagy ' + b.getAttribute('data-gal'); big.style.opacity = 1; }, 160); }
      if (fc) fc.textContent = b.getAttribute('data-fc') || '';
    }); });
  });
};

W.nyitva = function(root){
  var cfg = W.NYITVA; if (!cfg) return;
  $$(root,'[data-nyitva]').forEach(function(el){
    var d = new Date(), nap = ((d.getDay()+6)%7)+1, t = cfg[String(nap)], h = d.getHours()+d.getMinutes()/60;
    var nyitva = t && h >= t[0] && h < t[1];
    el.hidden = false; el.textContent = nyitva ? 'Most nyitva' : 'Most zárva'; el.classList.toggle('zarva', !nyitva);
  });
};

W.szamoz = function(root){ var host = root.closest ? (root.closest('.elo-root') || root) : root; $$(host,'.shead').forEach(function(h,i){ var k = h.querySelector('.kick'); if(k) k.setAttribute('data-n', (i<9?'0':'') + (i+1)); }); };
W.init = function(root, azonnal){ root = root || document; W.szamoz(root); W.menu(root); W.rail(root); W.tabs(root); W.galeria(root); W.nyitva(root); W.reveal(root, azonnal); };
})();
"""
