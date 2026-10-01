# -*- coding: utf-8 -*-
"""Az élő oldal és minden előnézet közös alapja. Minden méret konténer-egységben (cqi), így a
mobil-előnézet (keskeny konténer) is valódi mobil-elrendezést mutat."""

ALAP_CSS = r"""
.elo-root{container:elo/inline-size;position:relative;
  --wrap:1180px;--pad:clamp(18px,4.2cqi,44px);--sec-y:clamp(64px,8.4cqi,124px);--gap:clamp(16px,2.3cqi,28px);
  --t-hero:calc(clamp(2.35rem,5.5cqi,4.85rem)*var(--hero-scale,1));--t-h2:clamp(1.8rem,3.5cqi,3.05rem);
  --t-h3:clamp(1.1rem,1.55cqi,1.34rem);--t-lead:clamp(1.02rem,1.25cqi,1.19rem);
  --r:20px;--r-sm:12px;--ease:cubic-bezier(.22,.72,.2,1);--ease-out:cubic-bezier(.16,1,.3,1);
  --b-bg:var(--c-primary);--b-ink:var(--c-on-primary);--b-deep:var(--c-primary-dd);--mk:var(--c-accent);
  --mk-ink:var(--c-on-accent);--hl:var(--c-primary-text);--balt-bg:var(--c-card);--balt-ink:var(--c-head);
  font-family:var(--f-body);font-size:1.02rem;line-height:1.62;color:var(--c-ink);background:var(--c-paper);
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow:clip}
.elo-root *,.elo-root *::before,.elo-root *::after{box-sizing:border-box}
.elo-root img{max-width:100%;display:block}
.elo-root a{color:inherit}
.elo-root h1,.elo-root h2,.elo-root h3,.elo-root h4{font-family:var(--f-display);font-weight:var(--w-display);
  line-height:var(--lh-display);letter-spacing:var(--ls-display);text-transform:var(--tt-display);margin:0;color:var(--c-head);
  text-wrap:balance}
.elo-root p{margin:0 0 .9em;text-wrap:pretty}
.elo-root b,.elo-root strong{font-weight:var(--w-body-b)}
.elo-root mark{background:none;color:inherit;padding:0}
.elo-root ul{margin:0;padding:0;list-style:none}
.elo-root figure{margin:0}
.elo-root button{font:inherit;color:inherit}

.wrap{max-width:var(--wrap);margin:0 auto;padding:0 var(--pad);position:relative;z-index:2}
.wrap.szuk{max-width:860px}
.sec{position:relative;padding:var(--sec-y) 0;background:var(--sec-bg,var(--c-paper));color:var(--c-ink);isolation:isolate}
.s-paper{--sec-bg:var(--c-paper)}
.s-white{--sec-bg:var(--c-card)}
.s-tint{--sec-bg:var(--c-tint)}
.s-sand{--sec-bg:var(--c-sand)}
.s-deep{--sec-bg:var(--c-deep);--c-ink:var(--c-on-deep);--c-head:var(--c-on-deep);--c-ink-2:var(--c-on-deep-2);
  --c-ink-3:var(--c-on-deep-2);--c-line:rgba(255,255,255,.13);--c-line2:rgba(255,255,255,.24);
  --c-card:color-mix(in srgb,var(--c-deep),#fff 8%);--c-tint:color-mix(in srgb,var(--c-deep),#fff 12%);
  --c-primary-text:var(--c-deep-hl);--hl:var(--c-deep-hl);--mk:var(--c-deep-hl);--mk-ink:var(--c-on-deep-hl);
  --b-bg:var(--c-deep-btn);--b-ink:var(--c-on-deep-btn);--b-deep:var(--c-deep-btn-d)}
.s-primary{--sec-bg:var(--c-primary);--c-ink:var(--c-on-primary);--c-head:var(--c-on-primary);
  --c-ink-2:color-mix(in srgb,var(--c-on-primary) 82%,transparent);--c-ink-3:color-mix(in srgb,var(--c-on-primary) 66%,transparent);
  --c-line:color-mix(in srgb,var(--c-on-primary) 20%,transparent);--c-line2:color-mix(in srgb,var(--c-on-primary) 34%,transparent);
  --c-primary-text:var(--c-primary-hl);--hl:var(--c-primary-hl);--mk:var(--c-primary-mk);--mk-ink:var(--c-on-primary-mk);
  --b-bg:var(--c-card);--b-ink:var(--c-primary-d);--b-deep:color-mix(in srgb,var(--c-primary-dd),#000 25%);
  --balt-bg:color-mix(in srgb,var(--c-on-primary) 15%,transparent);--balt-ink:var(--c-on-primary)}

/* világos doboz színes/sötét szekción belül: minden szín visszaáll az alapra */
.s-vilagos{--c-ink:var(--c0-ink);--c-head:var(--c0-head);--c-ink-2:var(--c0-ink-2);--c-ink-3:var(--c0-ink-3);
  --c-line:var(--c0-line);--c-line2:var(--c0-line2);--c-card:var(--c0-card);--c-tint:var(--c0-tint);
  --c-primary-text:var(--c0-primary-text);--hl:var(--c0-primary-text);--mk:var(--c-accent);--mk-ink:var(--c-on-accent);
  --b-bg:var(--c-primary);--b-ink:var(--c-on-primary);--b-deep:var(--c-primary-dd);--sec-bg:var(--c0-card);color:var(--c-ink);
  --balt-bg:var(--c0-card);--balt-ink:var(--c0-head)}

/* szekciófej */
.shead{text-align:center;max-width:780px;margin:0 auto clamp(30px,4.2cqi,56px);position:relative}
.shead.bal{text-align:left;margin-left:0}
.kick{margin:0 0 14px;font-weight:700;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--hl)}
.cim{font-size:var(--t-h2)}
.hcim{font-size:var(--t-hero);line-height:calc(var(--lh-display) - .02)}
.lead{font-size:var(--t-lead);color:var(--c-ink-2);max-width:62ch;margin:16px auto 0}
.shead.bal .lead{margin-left:0}
.cim+.lead,.hcim+.lead{margin-top:18px}

/* gomb-alap (a stílust a Gombok opció adja) */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.6em;text-decoration:none;cursor:pointer;border:0;
  font-family:var(--f-body);font-weight:800;font-size:1rem;line-height:1.1;white-space:nowrap;position:relative}
.btn .ui{width:1.1em;height:1.1em;flex:none}
.gombsor{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.shead .gombsor{justify-content:center}.shead.bal .gombsor{justify-content:flex-start}

/* kártya-alap (a stílust a Kártyák opció adja) */
.krt{position:relative;display:flex;flex-direction:column;gap:10px;min-width:0}
.krt-fej{display:flex;align-items:center;gap:14px}
.krt-h{font-size:var(--t-h3);margin:0}
.krt-p{margin:0;color:var(--c-ink-2);font-size:.97rem}
.krt-meta{margin-top:auto;padding-top:6px;font-weight:800;color:var(--hl);font-size:.95rem}
.krt .ik{--ik:52px}
.racs{display:grid;gap:var(--gap);grid-template-columns:repeat(var(--oszlop,3),minmax(0,1fr))}
@container elo (max-width:900px){.racs{--oszlop:2!important}}
@container elo (max-width:560px){.racs{--oszlop:1!important}}

/* ikon (generált PNG, háttérképként) + UI ikon */
.ik{display:inline-block;width:var(--ik,56px);height:var(--ik,56px);flex:none;background:center/contain no-repeat;
  border-radius:0}
.ik.nincs{background:var(--c-primary-ll);border-radius:30%;position:relative}
.ik.nincs::after{content:"";position:absolute;inset:26%;border-radius:50%;border:3px solid var(--c-primary)}
.ui{width:20px;height:20px;flex:none;vertical-align:-.2em}

/* fotó (a keretet a Fotókezelés opció adja) */
.ft{position:relative;margin:0;isolation:isolate}
.ph{display:block;width:100%;aspect-ratio:var(--ar,4/3);background:var(--c-sand) center/cover no-repeat;
  background-position:var(--pos,50% 50%)}
.ft figcaption{font-size:.84rem;color:var(--c-ink-3);margin-top:8px}
.krt>.krt-kep{margin:calc(-1*var(--kp,24px)) calc(-1*var(--kp,24px)) 8px calc(-1*var(--kpl,var(--kp,24px)));width:auto;max-width:none}
.krt>.krt-kep .ph{--ar:16/11}

/* logó */
.logo{display:block;background:left center/contain no-repeat;height:var(--logo-h,56px);aspect-ratio:var(--logo-ar,1);flex:none}
.logo.ko{background-position:center}

/* textúra- és dekor-hordozók (a láthatóságot a Felület és a Dekor opció adja) */
.tx::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:0}
.dk{position:absolute;inset:0;pointer-events:none;z-index:1;overflow:hidden}
.dk>i{position:absolute;display:none;font-style:normal}
.hat{position:absolute;left:0;right:0;top:0;height:0;z-index:4;pointer-events:none}
.hat .tick{display:none}

/* chip, címke, pipa */
.chip{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;background:var(--c-card);
  border:1px solid var(--c-line);font-size:.86rem;font-weight:700;color:var(--c-ink);box-shadow:var(--sh-1)}
.chip .ui{width:16px;height:16px;color:var(--hl)}
.chip i.pt{width:8px;height:8px;border-radius:50%;background:var(--c-accent);display:inline-block}
.cimke{display:inline-flex;align-items:center;gap:6px;padding:3px 10px;border-radius:999px;font-size:.76rem;font-weight:700;
  background:var(--c-primary-ll);color:var(--c-primary-d)}
.s-deep .cimke{background:rgba(255,255,255,.1);color:var(--c-on-deep)}
.kezi{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.15rem);line-height:1.2;color:var(--c-hand)}
.mono{font-family:var(--f-label);letter-spacing:.06em}

/* reveal-alap (a Mozgás opció adja a stílust) */
.elo-root [data-rv]{--i:0}

/* képernyőkép- / csökkentett mozgás mód */
@media (prefers-reduced-motion:reduce){.elo-root *,.elo-root *::before,.elo-root *::after{animation:none!important;transition:none!important}
  .elo-root [data-rv]{opacity:1!important;transform:none!important;clip-path:none!important}}
.noanim .elo-root *,.noanim .elo-root *::before,.noanim .elo-root *::after,.elo-root.noanim *,.elo-root.noanim *::before{animation:none!important;transition:none!important}
.noanim .elo-root [data-rv],.elo-root.noanim [data-rv]{opacity:1!important;transform:none!important;clip-path:none!important}
"""
