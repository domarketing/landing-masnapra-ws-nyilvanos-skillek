# -*- coding: utf-8 -*-
"""GLOBÁLIS STÍLUS-OPCIÓK. Minden opció CSS-e a saját data-attribútumára van szűkítve:
   %S  ->  [data-<kategória>="<id>"]     %K -> egyedi keyframe-előtag
Így az élő oldalon bármelyik címsor-, gomb-, kártya-, fotó-... stílus kombinálható bármelyikkel.
Új opciót úgy adsz hozzá, hogy felveszel egy dict-et a megfelelő listába (id, nev, leiras, css)."""
from .alap import svg_uri

# --- kézi rajzolt formák (maszknak: csak az alfa számít) -------------------------------------------
NYIL = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 30"><path d="M3 5c11-3 22 3 26 17" fill="none" '
               'stroke="#000" stroke-width="3" stroke-linecap="round"/><path d="M22 18l7 5 3-8" fill="none" stroke="#000" '
               'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
HULLAM = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 48" preserveAspectRatio="none"><path d="M0 30C240 '
                 '58 480 4 720 22s480 34 720-2v28H0z"/></svg>')
SZAKADT = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 40" preserveAspectRatio="none"><path d="M0 20l20-6 '
                  '18 8 22-12 22 8 22-10 24 11 22-7 22 9 24-12 24 8 24-6 22 9 24-7 22 9 24-12 24 8v22H0z"/></svg>')
FIRKA = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 44"><path d="M4 22C16 4 28 40 40 22s24-18 36 0 '
                '24 18 40 0" fill="none" stroke="#000" stroke-width="5" stroke-linecap="round"/></svg>')
SZIKRA = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g stroke="#000" stroke-width="7" '
                 'stroke-linecap="round"><path d="M50 8v22M50 70v22M8 50h22M70 50h22M20 20l14 14M66 66l14 14M80 20 66 '
                 '34M34 66 20 80"/></g></svg>')
HUROKNYIL = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 70"><path d="M8 50C20 10 60 10 52 40c-6 20-32 '
                    '10-18-10 16-18 46-8 54 14" fill="none" stroke="#000" stroke-width="5" stroke-linecap="round"/><path '
                    'd="M78 40l10 6 4-12" fill="none" stroke="#000" stroke-width="5" stroke-linecap="round" '
                    'stroke-linejoin="round"/></svg>')
ZAJ = svg_uri("<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence "
              "type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/><feColorMatrix "
              "values='0 0 0 0 .3 0 0 0 0 .24 0 0 0 0 .18 0 0 0 .22 0'/></filter><rect width='100%' height='100%' "
              "filter='url(#n)'/></svg>")


def u(x):
    return f'url("{x}")'


CIM = [
    dict(id="c1", nev="Filctoll-kiemelés", leiras="Szövegkiemelő-csík a kulcsszó alatt, görgetésre végighúzódik. Barátságos, "
         "magabiztos, jól olvasható.", css="""
%S mark{background-image:linear-gradient(transparent 60%,color-mix(in srgb,var(--mk) 60%,transparent) 60%,color-mix(in srgb,var(--mk) 60%,transparent) 93%,transparent 93%);background-repeat:no-repeat;background-size:100% 100%;padding:0 .06em;-webkit-box-decoration-break:clone;box-decoration-break:clone;transition:background-size 1.1s var(--ease-out) .25s}
%S.js-rv [data-rv]:not(.in) mark{background-size:0% 100%}
"""),
    dict(id="c2", nev="Címke-doboz", leiras="A kulcsszó egy fehér, árnyékos címkén ül, mintha rá lenne ragasztva. Erős, "
         "plakátszerű, színes háttéren is működik.", css="""
%S mark{background:var(--c-card);color:var(--hl);padding:.02em .2em .07em;border-radius:.16em;box-shadow:var(--sh-2);-webkit-box-decoration-break:clone;box-decoration-break:clone}
%S .s-primary mark{color:var(--c-primary-d)}
"""),
    dict(id="c3", nev="Hullámos aláhúzás", leiras="Kézzel húzott hatású hullámvonal a szó alatt. Játékos, de nem harsány.", css="""
%S mark{text-decoration:underline wavy var(--mk);text-decoration-thickness:.07em;text-underline-offset:.22em;text-decoration-skip-ink:none}
"""),
    dict(id="c4", nev="Kézírásos szó", leiras="A kulcsszó kézírással, enyhén megdöntve. Személyes, meleg, mintha valaki "
         "odaírta volna.", css="""
%S mark{font-family:var(--f-hand);font-weight:700;color:var(--hl);font-size:calc(var(--fs-hand)*.95em);letter-spacing:0;text-transform:none;display:inline-block;transform:rotate(-2.5deg);line-height:.95;padding:0 .04em}
"""),
    dict(id="c5", nev="Színes hangsúly", leiras="A kulcsszó márkaszínnel és vékonyabb vastagsággal. Letisztult, elegáns, "
         "szerkesztőségi.", css="""
%S mark{color:var(--hl);font-weight:400}
"""),
    dict(id="c6", nev="Kontúrbetű", leiras="A kulcsszó csak körvonallal. Merész, modern, plakátos; nagy címeknél a legjobb.", css="""
%S mark{color:transparent;-webkit-text-stroke:max(1.5px,.032em) var(--hl);paint-order:stroke}
"""),
    dict(id="c7", nev="Kapszula-keret", leiras="Lekerekített keret a kulcsszó körül. Rendezett, barátságos, digitális érzet.", css="""
%S mark{border:max(2px,.055em) solid var(--hl);border-radius:999px;padding:0 .26em;color:var(--hl);-webkit-box-decoration-break:clone;box-decoration-break:clone}
"""),
    dict(id="c8", nev="Ferde színcsík", leiras="Kicsit megdöntött színes sáv a szó mögött. Energikus, akciós hangulat.", css="""
%S mark{background:linear-gradient(-2.5deg,transparent 10%,var(--mk) 10%,var(--mk) 90%,transparent 90%);color:var(--mk-ink);padding:0 .16em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
"""),
]

ALCIM = [
    dict(id="k1", nev="Vonalas felső címke", leiras="Kis nagybetűs címke két rövid vonal között. Klasszikus, rendezett, "
         "minden szekciót egyformán vezet be.", css="""
%S .kick{display:flex;align-items:center;justify-content:center;gap:12px;font-family:var(--f-body);font-weight:800;font-size:.76rem;letter-spacing:.2em;text-transform:uppercase;color:var(--hl)}
%S .kick::before,%S .kick::after{content:"";width:28px;height:2px;background:currentColor;border-radius:2px;flex:none}
%S .bal .kick{justify-content:flex-start}%S .bal .kick::after{display:none}
"""),
    dict(id="k2", nev="Mono + csíkjel", leiras="Írógépes (mono) betű, előtte három apró csík. Modern, rendszerezett, "
         "kicsit technikás.", css="""
%S .kick{display:inline-flex;align-items:center;gap:10px;font-family:var(--f-label);font-weight:600;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--c-ink-2)}
%S .kick::before{content:"";width:18px;height:11px;flex:none;background:repeating-linear-gradient(180deg,var(--c-accent2) 0 2px,transparent 2px 4.5px)}
"""),
    dict(id="k3", nev="Kapszula pöttyel", leiras="Halvány színes kapszula, benne egy élénk pötty. Barátságos, "
         "app-szerű, jól látható.", css="""
%S .kick{display:inline-flex;align-items:center;gap:9px;padding:7px 14px 7px 12px;border-radius:999px;background:var(--c-primary-ll);color:var(--c-primary-d);font-weight:800;font-size:.74rem;letter-spacing:.12em;text-transform:uppercase}
%S .kick::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--c-accent);box-shadow:0 0 0 4px color-mix(in srgb,var(--c-accent) 25%,transparent);flex:none}
%S .s-deep .kick{background:rgba(255,255,255,.1);color:var(--c-on-deep)}
%S .s-primary .kick{background:color-mix(in srgb,var(--c-on-primary) 16%,transparent);color:var(--c-on-primary)}
"""),
    dict(id="k4", nev="Kézírás nyíllal", leiras="Kézzel írt felvezető, mellette egy lefelé mutató rajzolt nyíl. "
         "Személyes, mesélős.", css="""
%S .kick{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.2rem);font-weight:700;letter-spacing:0;text-transform:none;color:var(--c-hand);display:inline-flex;align-items:flex-end;gap:6px;transform:rotate(-2deg);line-height:1.1}
%S .kick::after{content:"";width:34px;height:26px;flex:none;background:currentColor;-webkit-mask:""" + u(NYIL) + """ center/contain no-repeat;mask:""" + u(NYIL) + """ center/contain no-repeat}
%S .s-deep .kick{color:var(--c-deep-hl)}%S .s-primary .kick{color:var(--c-primary-hl)}
"""),
    dict(id="k5", nev="Sorszámozott", leiras="Minden szekció kap egy nagy sorszámot (01, 02…) és egy vékony vonalat. "
         "Szerkesztőségi, magazinos rend.", css="""
%S .kick{display:flex;align-items:center;justify-content:center;gap:12px;font-family:var(--f-label);font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-2);font-weight:600}
%S .shead .kick::before{content:attr(data-n);font-family:var(--f-display);font-size:1.55rem;letter-spacing:0;color:var(--hl);font-weight:var(--w-display);line-height:1}
%S .kick::after{content:"";width:46px;height:1px;background:var(--c-line2)}
%S .bal .kick{justify-content:flex-start}
"""),
    dict(id="k6", nev="Pecsét", leiras="Szaggatott keretes, megdöntött pecsét. Kézműves, „minőségellenőrzött” hangulat.", css="""
%S .kick{display:inline-block;padding:6px 14px;border:2px dashed currentColor;border-radius:6px;color:var(--hl);font-weight:800;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;transform:rotate(-2.5deg);background:color-mix(in srgb,var(--c-card) 55%,transparent)}
"""),
    dict(id="k7", nev="Sötét chip", leiras="Tintaszínű, szögletes chip mono betűvel. Határozott, kontrasztos, modern.", css="""
%S .kick{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;background:var(--c-ink);color:var(--c-paper);font-family:var(--f-label);font-weight:600;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;border-radius:4px}
%S .kick::before{content:"";width:7px;height:7px;background:var(--c-accent);flex:none}
%S .s-deep .kick{background:var(--c-on-deep);color:var(--c-deep)}%S .s-primary .kick{background:var(--c-on-primary);color:var(--c-primary-d)}
"""),
]

GOMB = [
    dict(id="g1", nev="Pecsét-3D kapszula", leiras="Kerek gomb „talppal” és színes derengéssel: rámutatva megemelkedik, "
         "kattintásra lenyomódik. A legkattinthatóbb érzet.", css="""
%S .btn{padding:1.05em 1.8em;border-radius:999px;background:linear-gradient(180deg,color-mix(in srgb,var(--b-bg),#fff 14%),var(--b-bg));color:var(--b-ink);box-shadow:0 5px 0 var(--b-deep),0 18px 30px -14px color-mix(in srgb,var(--b-bg) 75%,transparent);transition:transform .15s var(--ease),box-shadow .15s var(--ease)}
%S .btn:hover{transform:translateY(-2px);box-shadow:0 7px 0 var(--b-deep),0 24px 36px -14px var(--b-bg)}
%S .btn:active{transform:translateY(4px);box-shadow:0 1px 0 var(--b-deep),0 8px 14px -8px var(--b-bg)}
%S .btn.alt{background:var(--balt-bg);color:var(--balt-ink);box-shadow:0 5px 0 var(--c-line2),0 14px 24px -16px rgba(0,0,0,.35)}
%S .btn.alt:hover{box-shadow:0 7px 0 var(--c-line2),0 18px 30px -16px rgba(0,0,0,.4)}
%S .btn.alt:active{box-shadow:0 1px 0 var(--c-line2)}
"""),
    dict(id="g2", nev="Lapos, nyíl-dobozzal", leiras="Enyhén lekerekített, lapos gomb, a nyíl külön kis dobozban, ami "
         "rámutatva előreugrik. Tiszta, modern, webshopos.", css="""
%S .btn{padding:.6em .62em .6em 1.35em;border-radius:14px;background:var(--b-bg);color:var(--b-ink);transition:background .2s var(--ease)}
%S .btn:not(:has(.ui)){padding:.95em 1.5em}
%S .btn .ui{width:2.1em;height:2.1em;padding:.5em;border-radius:10px;background:color-mix(in srgb,var(--b-ink) 16%,transparent);transition:transform .25s var(--ease)}
%S .btn:hover .ui{transform:translateX(4px)}
%S .btn:hover{background:color-mix(in srgb,var(--b-bg),#000 10%)}
%S .btn.alt{background:transparent;color:var(--c-head);box-shadow:inset 0 0 0 2px var(--c-line2)}
%S .btn.alt .ui{background:var(--c-tint)}
%S .btn.alt:hover{box-shadow:inset 0 0 0 2px var(--c-head)}
"""),
    dict(id="g3", nev="Telt ↔ kontúr", leiras="Kerek, telt gomb, ami rámutatva kontúrossá válik; a másodlagos gomb "
         "fordítva. Elegáns, visszafogott.", css="""
%S .btn{padding:.95em 1.65em;border-radius:999px;background:var(--b-bg);color:var(--b-ink);border:2px solid var(--b-bg);transition:background .25s,color .25s}
%S .btn:hover{background:transparent;color:var(--hl)}
%S .btn.alt{background:transparent;color:var(--c-head);border-color:currentColor}
%S .btn.alt:hover{background:var(--c-head);color:var(--sec-bg,var(--c-paper));border-color:var(--c-head)}
"""),
    dict(id="g4", nev="Matrica (neo-brutál)", leiras="Vastag tintakeret, kemény eltolt árnyék, kicsit megdöntve. "
         "Merész, játékos, fiatalos.", css="""
%S .btn{padding:.9em 1.5em;border-radius:12px;background:var(--b-bg);color:var(--b-ink);border:2.5px solid var(--c-ink);box-shadow:4px 4px 0 var(--c-ink);transform:rotate(-1deg);transition:transform .15s,box-shadow .15s}
%S .btn:hover{transform:rotate(0) translate(-2px,-2px);box-shadow:6px 6px 0 var(--c-ink)}
%S .btn:active{transform:translate(3px,3px);box-shadow:1px 1px 0 var(--c-ink)}
%S .btn.alt{background:var(--balt-bg);color:var(--balt-ink);transform:rotate(1deg)}
"""),
    dict(id="g5", nev="Árcédula", leiras="Címke alakú gomb lyukkal, mint egy bolti árcédula. Kereskedelmi, "
         "kézzelfogható metafora.", css="""
%S .btn{padding:.95em 1.6em .95em 2.15em;border-radius:6px;background:var(--b-bg);color:var(--b-ink);clip-path:polygon(16px 0,100% 0,100% 100%,16px 100%,0 50%);transition:filter .2s,transform .2s}
%S .btn::before{content:"";position:absolute;left:13px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;background:var(--sec-bg,var(--c-paper))}
%S .btn:hover{transform:rotate(-2deg);filter:brightness(1.07)}
%S .btn.alt{background:var(--c-head);color:var(--sec-bg,var(--c-paper))}
"""),
    dict(id="g6", nev="Puha fény", leiras="Kerek gomb finom fényátmenettel és nagy, színes derengéssel. Prémium, "
         "puha, modern.", css="""
%S .btn{padding:1em 1.75em;border-radius:999px;background:linear-gradient(135deg,color-mix(in srgb,var(--b-bg),#fff 20%),var(--b-bg) 55%,color-mix(in srgb,var(--b-bg),#000 12%));color:var(--b-ink);box-shadow:0 14px 30px -12px color-mix(in srgb,var(--b-bg) 80%,transparent),inset 0 1px 0 rgba(255,255,255,.35);transition:transform .25s var(--ease),box-shadow .25s}
%S .btn:hover{transform:translateY(-3px);box-shadow:0 22px 40px -14px var(--b-bg),inset 0 1px 0 rgba(255,255,255,.4)}
%S .btn.alt{background:color-mix(in srgb,var(--balt-bg) 80%,transparent);color:var(--balt-ink);box-shadow:inset 0 0 0 1px var(--c-line2),0 10px 24px -16px rgba(0,0,0,.3);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
"""),
    dict(id="g7", nev="Szögletes, elegáns", leiras="Szögletes, tintaszínű gomb nagybetűs, ritkított felirattal; a "
         "másodlagos csak egy aláhúzott link. Divatos, szerkesztőségi.", css="""
%S .btn{padding:1.1em 1.9em;border-radius:0;background:var(--c-head);color:var(--sec-bg,var(--c-paper));font-size:.82rem;letter-spacing:.15em;text-transform:uppercase;transition:background .25s,color .25s}
%S .btn:hover{background:var(--b-bg);color:var(--b-ink)}
%S .btn.alt{background:transparent;color:var(--c-head);padding-left:0;padding-right:0;box-shadow:inset 0 -2px 0 currentColor}
%S .btn.alt:hover{color:var(--hl);background:transparent}
"""),
]

KARTYA = [
    dict(id="r1", nev="Füzetlap", leiras="Fehér lap halvány sorvonalakkal és színes margóvonallal. Kézzelfogható, "
         "gondos, „jegyzetelt” érzet.", css="""
%S .krt{--kp:24px;--kpl:44px;padding:var(--kp) var(--kp) var(--kp) var(--kpl);background-color:var(--c-card);border:1px solid var(--c-line);border-radius:var(--r);box-shadow:var(--sh-2);overflow:hidden;background-image:repeating-linear-gradient(180deg,transparent 0 29px,color-mix(in srgb,var(--c-primary) 7%,transparent) 29px 30px);background-position:0 14px}
%S .krt::before{content:"";position:absolute;left:24px;top:0;bottom:0;width:2px;background:color-mix(in srgb,var(--c-accent) 55%,transparent);z-index:1}
%S .krt .ik{--ik:48px}
"""),
    dict(id="r2", nev="Színes felső sáv", leiras="Tiszta fehér kártya, tetején kétszínű márkasáv, rámutatva megemelkedik.",
         css="""
%S .krt{--kp:26px;padding:var(--kp);background:var(--c-card);border-radius:var(--r);box-shadow:var(--sh-2);overflow:hidden;transition:transform .3s var(--ease),box-shadow .3s}
%S .krt::after{content:"";position:absolute;left:0;right:0;top:0;height:5px;background:linear-gradient(90deg,var(--c-primary) 0 58%,var(--c-accent) 58% 100%);z-index:3}
%S .krt:hover{transform:translateY(-4px);box-shadow:var(--sh-3)}
"""),
    dict(id="r3", nev="Neo-brutál", leiras="Vastag tintakeret, kemény eltolt árnyék, színes ikon-doboz. Karakteres, "
         "fiatalos, nem hagyja figyelmen kívül a szem.", css="""
%S .krt{--kp:24px;padding:var(--kp);background:var(--c-card);border:2px solid var(--c-ink);border-radius:14px;box-shadow:6px 6px 0 var(--c-ink);transition:transform .15s,box-shadow .15s;overflow:hidden}
%S .krt:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--c-ink)}
%S .krt .krt-fej .ik{--ik:56px;background-color:var(--c-accent-l);border:2px solid var(--c-ink);border-radius:12px;padding:6px;background-origin:content-box}
%S .krt>.krt-kep{border-bottom:2px solid var(--c-ink)}
"""),
    dict(id="r4", nev="Perforált jegy", leiras="Belépőjegy-forma oldalsó kivágással és szaggatott tépővonallal; az ár "
         "a letéphető szelvényen ül. Esemény, kupon, ajánlat hangulat.", css="""
%S .krt{--kp:24px;--szel:62px;padding:var(--kp) var(--kp) calc(var(--kp) + var(--szel));background:var(--c-card);border-radius:16px;box-shadow:inset 0 0 0 1px var(--c-line);-webkit-mask:radial-gradient(circle 11px at 0 calc(100% - var(--szel)),#0000 98%,#000) 0 0/51% 100% no-repeat,radial-gradient(circle 11px at 100% calc(100% - var(--szel)),#0000 98%,#000) 100% 0/51% 100% no-repeat;mask:radial-gradient(circle 11px at 0 calc(100% - var(--szel)),#0000 98%,#000) 0 0/51% 100% no-repeat,radial-gradient(circle 11px at 100% calc(100% - var(--szel)),#0000 98%,#000) 100% 0/51% 100% no-repeat}
%S .krt::after{content:"";position:absolute;left:20px;right:20px;bottom:var(--szel);border-top:2px dashed var(--c-line2)}
%S .krt .krt-meta{position:absolute;left:var(--kp);right:var(--kp);bottom:0;height:var(--szel);display:flex;align-items:center;margin:0;padding:0}
%S .krt:not(:has(.krt-meta)){--szel:26px}
"""),
    dict(id="r5", nev="Étlap-keret", leiras="Dupla vékony keret, középre zárt cím díszpontokkal, mint egy nyomtatott "
         "étlap vagy meghívó. Elegáns, klasszikus.", css="""
%S .krt{--kp:28px;padding:var(--kp);background:var(--c-card);border:1px solid var(--c-line2);border-radius:6px;outline:1px solid var(--c-line2);outline-offset:-8px;text-align:center;align-items:center;box-shadow:var(--sh-1)}
%S .krt .krt-fej{flex-direction:column;gap:12px}
%S .krt .krt-h::after{content:"";display:block;width:54px;height:8px;margin:10px auto 0;background:radial-gradient(circle,var(--c-accent) 2.4px,transparent 2.9px) center/12px 8px repeat-x}
%S .krt>.krt-kep{margin:0 0 6px!important;width:100%}
%S .krt>.krt-kep .ph{border-radius:3px}
"""),
    dict(id="r6", nev="Puha, színezett", leiras="Halványan márkaszínes kártya keret nélkül, nagy lekerekítéssel, ikon "
         "fehér körben. Barátságos, nyugodt, modern.", css="""
%S .krt{--kp:26px;padding:var(--kp);background:var(--c-tint);border-radius:28px;transition:background .3s,transform .3s var(--ease);overflow:hidden}
%S .krt .krt-fej .ik{--ik:60px;background-color:var(--c-card);border-radius:50%;padding:10px;background-origin:content-box;box-shadow:var(--sh-2)}
%S .krt:hover{background:var(--c-primary-ll);transform:translateY(-3px)}
%S .s-tint .krt{background:var(--c-card)}%S .s-tint .krt:hover{background:var(--c-card)}
"""),
    dict(id="r7", nev="Oldalsávos", leiras="Fehér kártya vastag, színes bal oldali sávval. Egyszerű, rendezett, "
         "szakmai.", css="""
%S .krt{--kp:24px;--kpl:26px;padding:var(--kp) var(--kp) var(--kp) var(--kpl);background:var(--c-card);border-radius:6px 18px 18px 6px;box-shadow:var(--sh-1),0 0 0 1px var(--c-line);border-left:6px solid var(--c-accent);overflow:hidden}
"""),
]

FOTO = [
    dict(id="f1", nev="Lekerekített, mély árnyékkal", leiras="Nagy lekerekítés és puha, mély árnyék. Letisztult, "
         "prémium, a fotó a főszereplő.", css="""
%S .ft .ph{border-radius:22px;box-shadow:var(--sh-3)}
%S .ft.krt-kep .ph{border-radius:0;box-shadow:none}
"""),
    dict(id="f2", nev="Polaroid", leiras="Fehér keretes, kicsit megdöntött „kinyomtatott” fotók kézírásos felirattal. "
         "Személyes, emlékkönyves, családias.", css="""
%S .ft{background:#fff;padding:10px 10px 12px;box-shadow:var(--sh-3);border-radius:4px}
%S .ft .ph{border-radius:2px}
%S .ft:nth-child(odd){transform:rotate(-2deg)}%S .ft:nth-child(even){transform:rotate(1.8deg)}
%S .ft figcaption{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1rem);color:#333;text-align:center;margin-top:8px}
%S .ft.krt-kep{background:none;padding:0;box-shadow:none;transform:none;border-radius:0}
"""),
    dict(id="f3", nev="Boltív", leiras="Felül íves, alul szögletes forma, mint egy ablak vagy kapu. Meleg, "
         "mediterrán, elegáns.", css="""
%S .ft .ph{border-radius:999px 999px 16px 16px}
%S .ft.krt-kep .ph{border-radius:0}
"""),
    dict(id="f4", nev="Eltolt kontúr", leiras="Lekerekített fotó, mögötte egy eltolt, színes vonalkeret. Grafikus, "
         "rendezett, kicsit játékos.", css="""
%S .ft .ph{border-radius:18px}
%S .ft::before{content:"";position:absolute;inset:0 0 auto 0;aspect-ratio:var(--ar,4/3);border:2px solid var(--c-accent);border-radius:22px;transform:translate(12px,12px);z-index:-1}
%S .ft.krt-kep::before{display:none}%S .ft.krt-kep .ph{border-radius:0}
"""),
    dict(id="f5", nev="Organikus folt", leiras="Szabálytalan, puha folt-forma, lassan lélegzik. Természetes, bio, "
         "kézműves érzet.", css="""
%S .ft .ph{border-radius:58% 42% 52% 48% / 46% 54% 46% 54%;animation:%Kfolt 16s ease-in-out infinite alternate}
@keyframes %Kfolt{to{border-radius:44% 56% 46% 54% / 56% 44% 56% 44%}}
%S .ft.krt-kep .ph{border-radius:0;animation:none}
"""),
    dict(id="f6", nev="Színblokk mögötte", leiras="A fotó mögött egy eltolt, halvány márkaszínű blokk. Magazinos, "
         "rétegzett, mélységet ad.", css="""
%S .ft .ph{border-radius:14px}
%S .ft::before{content:"";position:absolute;inset:0 0 auto 0;aspect-ratio:var(--ar,4/3);border-radius:18px;background:var(--c-primary-l);transform:translate(-14px,14px) rotate(-2deg);z-index:-1}
%S .ft.krt-kep::before{display:none}%S .ft.krt-kep .ph{border-radius:0}
"""),
    dict(id="f7", nev="Bélyeg", leiras="Fogazott szélű fehér keret, mint egy postabélyeg. Nosztalgikus, gyűjthető, "
         "egyedi.", css="""
%S .ft{padding:11px;background:radial-gradient(circle at 6px 6px,transparent 4.2px,#fff 4.8px) -6px -6px/12px 12px;filter:drop-shadow(0 8px 14px rgba(0,0,0,.18))}
%S .ft:nth-child(odd){transform:rotate(-1.5deg)}%S .ft:nth-child(even){transform:rotate(1.2deg)}
%S .ft.krt-kep{padding:0;background:none;filter:none;transform:none}
"""),
    dict(id="f8", nev="Márkaszínű duotone", leiras="Fekete-fehér fotó márkaszínnel átszínezve. Nagyon egységes, "
         "grafikus. Ételfotóhoz NEM ajánlott (étvágytalan).", css="""
%S .ft .ph{border-radius:16px;filter:grayscale(1) contrast(1.08) brightness(1.06)}
%S .ft::after{content:"";position:absolute;inset:0 0 auto 0;aspect-ratio:var(--ar,4/3);border-radius:16px;background:var(--c-primary);mix-blend-mode:multiply;opacity:.55;pointer-events:none}
"""),
]

FELULET = [
    dict(id="t1", nev="Füzet-rács", leiras="Halvány kockás rács, ami középen elhalványul. Tervezett, rendezett, "
         "„kiszámolt” hatás.", css="""
%S .tx::before{background-image:linear-gradient(var(--c-line) 1px,transparent 1px),linear-gradient(90deg,var(--c-line) 1px,transparent 1px);background-size:34px 34px;-webkit-mask-image:linear-gradient(180deg,#000,rgba(0,0,0,.2) 55%,#000);mask-image:linear-gradient(180deg,#000,rgba(0,0,0,.2) 55%,#000)}
"""),
    dict(id="t2", nev="Pöttyrács", leiras="Finom pöttyminta a szélek felé erősödve. Könnyed, modern, nem zavarja a "
         "szöveget.", css="""
%S .tx::before{background-image:radial-gradient(color-mix(in srgb,var(--c-ink) 24%,transparent) 1.3px,transparent 1.7px);background-size:22px 22px;-webkit-mask-image:radial-gradient(ellipse 75% 70% at 50% 45%,transparent 25%,#000 90%);mask-image:radial-gradient(ellipse 75% 70% at 50% 45%,transparent 25%,#000 90%)}
"""),
    dict(id="t3", nev="Vonalas lap", leiras="Sorvonalas papír margóvonallal. Iskolás, jegyzetes, személyes.", css="""
%S .tx::before{background-image:linear-gradient(90deg,transparent calc(7% - 1px),color-mix(in srgb,var(--c-accent) 40%,transparent) calc(7% - 1px) calc(7% + 1px),transparent calc(7% + 1px)),repeating-linear-gradient(180deg,transparent 0 31px,var(--c-line) 31px 32px);-webkit-mask-image:linear-gradient(90deg,#000,rgba(0,0,0,.35) 50%,#000);mask-image:linear-gradient(90deg,#000,rgba(0,0,0,.35) 50%,#000)}
"""),
    dict(id="t4", nev="Motívum-minta", leiras="A márka saját formáiból (lásd a Dekor-motívumokat) szőtt, halvány, "
         "ismétlődő minta. A legegyedibb felület: csak ennél a márkánál van értelme.", css="""
%S .tx::before{background-color:var(--c-primary);-webkit-mask:var(--minta) 0 0/132px 132px repeat;mask:var(--minta) 0 0/132px 132px repeat;opacity:.075}
%S .s-deep.tx::before{background-color:var(--c-deep-hl);opacity:.1}%S .s-primary.tx::before{background-color:var(--c-on-primary);opacity:.1}
"""),
    dict(id="t5", nev="Színfoltok", leiras="Két nagy, elmosódott márkaszínű fényfolt a sarkokban. Meleg, lágy, "
         "„napfényes” hangulat.", css="""
%S .tx::before{background:radial-gradient(640px 440px at 90% 6%,color-mix(in srgb,var(--c-accent) 24%,transparent),transparent 70%),radial-gradient(560px 440px at 4% 96%,color-mix(in srgb,var(--c-primary) 17%,transparent),transparent 70%)}
"""),
    dict(id="t6", nev="Papír-szemcse", leiras="Finom, nyomott papírra emlékeztető szemcse. Kézműves, meleg, "
         "analóg; nagyon visszafogott.", css="""
%S .tx::before{background-image:""" + u(ZAJ) + """,radial-gradient(ellipse at 50% 40%,transparent 50%,color-mix(in srgb,var(--c-accent) 14%,transparent));background-size:180px 180px,100% 100%;opacity:1;mix-blend-mode:multiply}
%S .s-deep.tx::before,%S .s-primary.tx::before{mix-blend-mode:screen;opacity:.5}
"""),
    dict(id="t7", nev="Kockás terítő", leiras="Halvány, kockás terítő-minta a szekció szélein. Vendéglátós, "
         "piknikes, családias.", css="""
%S .tx::before{--gc:color-mix(in srgb,var(--c-primary) 12%,transparent);background-image:linear-gradient(90deg,var(--gc) 50%,transparent 50%),linear-gradient(var(--gc) 50%,transparent 50%);background-size:44px 44px;-webkit-mask-image:linear-gradient(180deg,#000,transparent 24%,transparent 76%,#000);mask-image:linear-gradient(180deg,#000,transparent 24%,transparent 76%,#000)}
%S .s-deep.tx::before{--gc:rgba(255,255,255,.06)}
"""),
    dict(id="t8", nev="Tiszta felület", leiras="Nincs minta, csak a felületek színe váltakozik. A legcsendesebb; a "
         "fotók és a tipográfia viszik az oldalt.", css="""
%S .tx::before{display:none}
"""),
]

DEKOR = [
    dict(id="d1", nev="Szellemszó", leiras="Óriás, halvány körvonalas szó a szekciók szélén (pl. TÉSZTA, ÉTLAP). "
         "Plakátos, magabiztos, sok mélységet ad.", css="""
%S .dk-szo{display:block;right:-.04em;bottom:-.16em;font-family:var(--f-display);font-weight:900;font-size:clamp(84px,17cqi,250px);line-height:.8;letter-spacing:-.02em;text-transform:uppercase;white-space:nowrap;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--c-ink) 14%,transparent)}
%S .sec:nth-of-type(even) .dk-szo{right:auto;left:-.04em;top:-.08em;bottom:auto}
"""),
    dict(id="d2", nev="Lebegő motívumok", leiras="A márka saját formái (pl. tésztaforma, levél) lassan lebegnek a "
         "szekciók sarkaiban. Élő, játékos, egyedi.", css="""
%S .dk-a,%S .dk-b,%S .dk-c{display:block;width:var(--s,54px);height:var(--s,54px);background:var(--c-accent);-webkit-mask:var(--m1) center/contain no-repeat;mask:var(--m1) center/contain no-repeat;opacity:.6;animation:%Klebeg 9s ease-in-out infinite alternate}
%S .dk-a{--s:58px;left:3.5%;top:11%;--rot:-14deg}
%S .dk-b{--s:44px;right:5%;top:16%;background:var(--c-primary);-webkit-mask-image:var(--m2);mask-image:var(--m2);animation-duration:7.4s;--rot:10deg}
%S .dk-c{--s:40px;right:12%;bottom:10%;background:var(--c-accent2);-webkit-mask-image:var(--m3);mask-image:var(--m3);animation-duration:10.5s;--rot:24deg}
%S .s-primary .dk-a,%S .s-primary .dk-b,%S .s-primary .dk-c{background:var(--c-primary-hl)}
@keyframes %Klebeg{from{transform:translateY(0) rotate(var(--rot,-8deg))}to{transform:translateY(-16px) rotate(calc(var(--rot,-8deg) + 16deg))}}
@container elo (max-width:640px){%S .dk-c,%S .dk-b{display:none}}
"""),
    dict(id="d3", nev="Óriás jel", leiras="A márka fő motívuma óriási méretben, alig láthatóan a sarokban. "
         "Nyugodt, elegáns márkaépítés.", css="""
%S .dk-jel{display:block;width:clamp(220px,34cqi,440px);aspect-ratio:1;right:-6%;top:-8%;background:var(--c-primary);-webkit-mask:var(--mjel) center/contain no-repeat;mask:var(--mjel) center/contain no-repeat;opacity:.07;transform:rotate(-12deg)}
%S .sec:nth-of-type(even) .dk-jel{right:auto;left:-7%;top:auto;bottom:-10%;transform:rotate(10deg)}
%S .s-deep .dk-jel{background:var(--c-deep-hl);opacity:.1}%S .s-primary .dk-jel{background:var(--c-on-primary);opacity:.12}
"""),
    dict(id="d4", nev="Gyűrű + pöttyfolt", leiras="Lassan forgó szaggatott gyűrű és egy apró pöttyfolt. Geometrikus, "
         "finom, „tervezett” díszítés.", css="""
%S .dk-r{display:block;width:150px;height:150px;border-radius:50%;border:2px dashed color-mix(in srgb,var(--c-accent) 62%,transparent);right:5%;top:10%;animation:%Kforog 50s linear infinite}
%S .dk-f2{display:block;width:126px;height:92px;left:3%;bottom:9%;background:radial-gradient(color-mix(in srgb,var(--c-primary) 48%,transparent) 2px,transparent 2.6px) 0 0/15px 15px}
@keyframes %Kforog{to{transform:rotate(360deg)}}
"""),
    dict(id="d5", nev="Kézi firkák", leiras="Kézzel rajzolt hullámvonal, csillanás és hurkos nyíl. Spontán, "
         "vidám, emberi.", css="""
%S .dk-f1{display:block;width:120px;height:40px;left:4%;top:13%;background:var(--c-accent);-webkit-mask:""" + u(FIRKA) + """ center/contain no-repeat;mask:""" + u(FIRKA) + """ center/contain no-repeat;transform:rotate(-8deg)}
%S .dk-f2{display:block;width:54px;height:54px;right:7%;top:15%;background:var(--c-primary);-webkit-mask:""" + u(SZIKRA) + """ center/contain no-repeat;mask:""" + u(SZIKRA) + """ center/contain no-repeat;animation:%Kcsillan 3.2s ease-in-out infinite}
%S .dk-r{display:block;width:96px;height:68px;right:9%;bottom:9%;background:var(--c-accent2);-webkit-mask:""" + u(HUROKNYIL) + """ center/contain no-repeat;mask:""" + u(HUROKNYIL) + """ center/contain no-repeat}
%S .s-primary .dk-f1,%S .s-primary .dk-f2,%S .s-primary .dk-r{background:var(--c-primary-hl)}
@keyframes %Kcsillan{0%,100%{transform:scale(.8) rotate(0);opacity:.55}50%{transform:scale(1.08) rotate(20deg);opacity:1}}
"""),
    dict(id="d6", nev="Matricák", leiras="Kerek, megdöntött matrica egy rövid ténnyel (pl. „Friss tészta minden "
         "reggel”) a hero-ban és a záró blokkban. Kézzelfogható, figyelemfelkeltő.", css="""
%S .dk-m{display:grid;place-items:center;width:124px;height:124px;border-radius:50%;right:4.5%;top:8%;background:var(--c-accent);color:var(--c-on-accent);font-family:var(--f-display);font-weight:var(--w-display);font-size:.9rem;line-height:1.08;text-align:center;padding:16px;transform:rotate(12deg);box-shadow:var(--sh-2);text-transform:uppercase;letter-spacing:.02em;z-index:5}
%S .dk-m::before{content:"";position:absolute;inset:6px;border-radius:50%;border:1.5px dashed currentColor;opacity:.55}
%S .dk-a{display:block;width:34px;height:34px;left:4%;bottom:12%;background:var(--c-primary);-webkit-mask:var(--m1) center/contain no-repeat;mask:var(--m1) center/contain no-repeat;opacity:.5;transform:rotate(-18deg)}
@container elo (max-width:700px){%S .dk-m{width:96px;height:96px;font-size:.72rem;right:3%;top:2%}}
"""),
    dict(id="d7", nev="Letisztult", leiras="Nincs díszítő réteg. Minimalista; a tartalom és a fotók beszélnek.", css="""
%S .dk>i{display:none!important}
"""),
]

HATAR = [
    dict(id="s1", nev="Hullám", leiras="Lágy hullámvonal a szekciók között. Barátságos, folyékony, természetes.", css="""
%S .hat{top:-46px;height:47px;background:var(--sec-bg);-webkit-mask:""" + u(HULLAM) + """ center bottom/100% 100% no-repeat;mask:""" + u(HULLAM) + """ center bottom/100% 100% no-repeat}
%S .hat.masod{transform:scaleX(-1)}
"""),
    dict(id="s2", nev="Fogazott jegy-él", leiras="Cikkcakkos él, mint egy letépett blokk vagy belépőjegy. "
         "Kereskedelmi, játékos.", css="""
%S .hat{top:-15px;height:16px;background:var(--sec-bg);-webkit-mask:conic-gradient(from 135deg at top,#000 90deg,#0000 0) 50%/30px 100%;mask:conic-gradient(from 135deg at top,#000 90deg,#0000 0) 50%/30px 100%}
"""),
    dict(id="s3", nev="Futószalag", leiras="Megdöntött, végtelenítve futó szalag a márka rövid tényeivel a szekciók "
         "határán. Fesztiválos, energikus, sok információt ad át észrevétlenül.", css="""
%S .hat{top:0;height:auto;left:-2%;right:-2%;transform:translateY(-50%) rotate(-1.4deg)}
%S .hat .tick{display:block;background:var(--c-primary);color:var(--c-on-primary);padding:13px 0;overflow:hidden;box-shadow:var(--sh-2)}
%S .hat.masod{transform:translateY(-50%) rotate(1.2deg)}
%S .hat.masod .tick{background:var(--c-accent);color:var(--c-on-accent)}
%S .hat .tick-in{display:flex;width:max-content;animation:%Ktick 40s linear infinite}
%S .hat .tick-in span{display:inline-flex;align-items:center;gap:20px;padding-right:20px;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.08rem;text-transform:uppercase;letter-spacing:.02em;white-space:nowrap}
%S .hat .tick-in span::after{content:"";width:18px;height:18px;background:currentColor;opacity:.7;-webkit-mask:var(--m1) center/contain no-repeat;mask:var(--m1) center/contain no-repeat}
%S .sec:has(>.hat){padding-top:calc(var(--sec-y) + 28px)}
@keyframes %Ktick{to{transform:translateX(-50%)}}
"""),
    dict(id="s4", nev="Ferde vágás", leiras="Átlós vágás a szekciók között. Dinamikus, lendületes, sportos.", css="""
%S .hat{top:-44px;height:45px;background:var(--sec-bg);clip-path:polygon(0 100%,100% 0,100% 101%,0 101%)}
%S .hat.masod{clip-path:polygon(0 0,100% 100%,100% 101%,0 101%)}
"""),
    dict(id="s5", nev="Szakadt papír", leiras="Egyenetlen, tépett papírél. Kézműves, újságkivágásos, spontán.", css="""
%S .hat{top:-21px;height:22px;background:var(--sec-bg);-webkit-mask:""" + u(SZAKADT) + """ 0 100%/360px 100% repeat-x;mask:""" + u(SZAKADT) + """ 0 100%/360px 100% repeat-x}
"""),
    dict(id="s6", nev="Napellenző-ív", leiras="Apró félkörívek sora, mint egy bolti napellenző vagy csipke. "
         "Vendégváró, üzletes, bájos.", css="""
%S .hat{top:-17px;height:18px;background:var(--sec-bg);-webkit-mask:radial-gradient(circle at 50% 100%,#000 17px,#0000 17.6px) 0 100%/34px 18px repeat-x;mask:radial-gradient(circle at 50% 100%,#000 17px,#0000 17.6px) 0 100%/34px 18px repeat-x}
"""),
    dict(id="s7", nev="Varrás-vonal", leiras="Csak egy finom szaggatott vonal jelzi a határt. A legcsendesebb, "
         "letisztult megoldás.", css="""
%S .hat{top:-1px;height:2px;left:max(var(--pad),calc(50% - 560px));right:max(var(--pad),calc(50% - 560px));background:repeating-linear-gradient(90deg,var(--c-line2) 0 10px,transparent 10px 18px)}
"""),
]

MOZGAS = [
    dict(id="m1", nev="Nyugodt úszás", leiras="Az elemek lassan, finoman úsznak be. Elegáns, pihentető.", css="""
%S.js-rv [data-rv]{opacity:0;transform:translateY(16px);transition:opacity .9s var(--ease-out),transform .9s var(--ease-out);transition-delay:calc(var(--i)*60ms)}
%S.js-rv [data-rv].in{opacity:1;transform:none}
%S .dk>i{animation-duration:18s!important}
"""),
    dict(id="m2", nev="Élénk, lépcsőzetes", leiras="Az elemek egymás után, lendületesen emelkednek be; a díszek "
         "lebegnek. Energikus, modern.", css="""
%S.js-rv [data-rv]{opacity:0;transform:translateY(30px);transition:opacity .7s var(--ease-out),transform .7s var(--ease-out);transition-delay:calc(var(--i)*95ms)}
%S.js-rv [data-rv].in{opacity:1;transform:none}
"""),
    dict(id="m3", nev="Játékos pattanás", leiras="Az elemek kicsit megdöntve, rugalmasan pattannak a helyükre; "
         "rámutatva az ikonok megbillennek. Vidám, gyerekbarát.", css="""
%S.js-rv [data-rv]{opacity:0;transform:scale(.9) rotate(-2deg);transition:opacity .55s ease,transform .8s cubic-bezier(.34,1.56,.64,1);transition-delay:calc(var(--i)*85ms)}
%S.js-rv [data-rv].in{opacity:1;transform:none}
%S .krt:hover .ik,%S .ikbox:hover .ik{animation:%Kbillen .55s ease}
@keyframes %Kbillen{25%{transform:rotate(-12deg) scale(1.06)}75%{transform:rotate(9deg)}}
"""),
    dict(id="m4", nev="Filmes függöny", leiras="A blokkok alulról, függönyszerűen tárulnak fel, a fotók lassan "
         "közelítenek. Drámai, prémium, filmes.", css="""
%S.js-rv [data-rv]{clip-path:inset(0 0 100% 0);transform:translateY(34px);transition:clip-path 1.15s var(--ease-out),transform 1.15s var(--ease-out);transition-delay:calc(var(--i)*110ms)}
%S.js-rv [data-rv].in{clip-path:inset(0 0 0 0);transform:none}
%S.js-rv [data-rv].rv-kesz{clip-path:none}
%S .ph{transition:transform 1.9s var(--ease-out)}
%S.js-rv [data-rv]:not(.in) .ph{transform:scale(1.12)}
"""),
    dict(id="m5", nev="Csendes (animáció nélkül)", leiras="Nincs beúszás és lebegés, csak apró visszajelzések "
         "rámutatáskor. Gyors, akadálymentes, komoly.", css="""
%S .dk>i{animation:none!important}
"""),
]

# kategória -> (lista, rövid magyar név, mit dönt el)
GLOBALIS = {
    "cim": (CIM, "Címsorok", "Hogyan emeljük ki a címek kulcsszavát (a ==jelölt== rész)."),
    "alcim": (ALCIM, "Alcímek (felső címkék)", "A szekciók felett álló kis bevezető címke stílusa."),
    "gomb": (GOMB, "Gombok", "Az elsődleges és a másodlagos gomb formája és viselkedése."),
    "kartya": (KARTYA, "Kártyák", "Minden kártya-szerű doboz (kínálat, tények, lépések) alapformája."),
    "foto": (FOTO, "Fotókezelés", "Milyen keretet, formát kapnak a fotók az egész oldalon."),
    "felulet": (FELULET, "Háttér-textúra", "A szekciók hátterén futó finom minta."),
    "dekor": (DEKOR, "Dekor-réteg", "A tartalom mögötti díszítő elemek: szellemszó, motívumok, firkák, matricák."),
    "hatar": (HATAR, "Szekcióhatárok", "Hogyan válnak el egymástól a szekciók."),
    "mozgas": (MOZGAS, "Mozgás", "Hogyan érkeznek be az elemek görgetéskor, mennyire élő az oldal."),
}


def css_for(kat, opcio):
    sel = f'[data-{kat}="{opcio["id"]}"]'
    return opcio["css"].replace("%S", sel).replace("%K", f"k_{kat}_{opcio['id']}_")
