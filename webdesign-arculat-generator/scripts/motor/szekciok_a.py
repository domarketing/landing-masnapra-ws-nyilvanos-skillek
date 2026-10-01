# -*- coding: utf-8 -*-
"""SZEKCIÓ-VÁLTOZATOK, 1. rész: navigáció, hero, tények, kínálat, ajánlat.
Minden változat: dict(id, nev, leiras, css, render(ctx) -> html). A CSS a .v-<id> gyökérosztályra szűkít,
a reszponzív szabályok @container elo (...) lekérdezések (így a mobil-előnézet is valódi)."""
from .alap import esc, md, sima, g, ui
from .kozos import (kick, shead, btn, gombsor, foto, ph, ik, logo, dk, hat, chips, nyitvatartas, nyitva_cim, fo_kapcs, adatok, social,
                    navlinkek, statok, kezi, korszoveg, uid)


def F(lst, i):
    return lst[i % len(lst)] if lst else None


def HF(c, vid):
    h = c.get("hero", {})
    return h.get("fotok_" + vid) or h.get("fotok") or []


def brand(ctx, h=44, nev=True, cls="brand"):
    n = esc(g(ctx, "marka", "nev"))
    bn = f'<span class="bn">{n}</span>' if nev and g(ctx, "nav", "nev_mutat", alap=True) else ""
    return f'<a class="{cls}" href="#top">{logo(ctx, h)}{bn}</a>'


MNU = '<button class="mnu" type="button" aria-label="Menü" data-mnu>' + ui("menu") + '</button>'

NAV_KOZOS = r"""
.nav .links a{text-decoration:none}
.nav .mnu{display:none;width:44px;height:44px;border-radius:12px;border:1px solid var(--c-line2);background:var(--c-card);cursor:pointer;place-items:center;color:var(--c-head)}
.nav .mnu .ui{width:22px;height:22px}
"""

# ============================================================== NAV
NAV = []

NAV.append(dict(id="n1", nev="Lebegő kapszula", leiras="Lekerekített, üveghatású sáv, ami a tartalom fölött lebeg és "
    "görgetéskor végig látszik. Modern, könnyed.", css=NAV_KOZOS + r"""
.v-n1{position:sticky;top:0;z-index:60;padding:12px var(--pad) 0;margin-bottom:-78px}
.v-n1 .bar{max-width:var(--wrap);margin:0 auto;display:flex;align-items:center;gap:18px;padding:7px 7px 7px 14px;border-radius:999px;background:color-mix(in srgb,var(--c0-card) 88%,transparent);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:var(--sh-2);border:1px solid var(--c0-line)}
.v-n1 .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.1rem;color:var(--c0-head)}
.v-n1 .links{display:flex;gap:2px;margin-left:auto}
.v-n1 .links a{padding:9px 14px;border-radius:999px;font-weight:700;font-size:.92rem;color:var(--c0-ink-2)}
.v-n1 .links a:hover{background:var(--c0-tint);color:var(--c0-head)}
.v-n1 .btn{font-size:.88rem}
@container elo (max-width:900px){.v-n1 .links{display:none}.v-n1 .mnu{display:grid;margin-left:auto}.v-n1 .btn{display:none}
 .v-n1.nyit .links{display:flex;flex-direction:column;position:absolute;left:var(--pad);right:var(--pad);top:74px;background:var(--c0-card);border-radius:20px;padding:10px;box-shadow:var(--sh-3)}}
""", render=lambda c: f"""<header class="nav v-n1" data-nav><div class="bar">{brand(c, 42)}<nav class="links">{navlinkek(c)}</nav>{btn(g(c, 'nav', 'cta'), ikon='tel')}{MNU}</div></header>"""))

NAV.append(dict(id="n2", nev="Infósáv + menü", leiras="Vékony, sötét felső sáv a telefonnal, nyitvatartással és címmel, "
    "alatta a menü. A legtöbb gyakorlati infó azonnal látszik.", css=NAV_KOZOS + r"""
.v-n2{position:sticky;top:0;z-index:60}
.v-n2 .info{background:var(--c-deep);color:var(--c-on-deep);font-size:.84rem}
.v-n2 .info .wrap{display:flex;gap:26px;align-items:center;min-height:38px}
.v-n2 .info span{display:inline-flex;align-items:center;gap:8px;opacity:.92}
.v-n2 .info .ui{width:15px;height:15px;color:var(--c-deep-hl)}
.v-n2 .info .jobbra{margin-left:auto}
.v-n2 .bar{background:color-mix(in srgb,var(--c0-card) 94%,transparent);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--c0-line)}
.v-n2 .bar .wrap{display:flex;align-items:center;gap:26px;min-height:74px}
.v-n2 .brand{display:flex;align-items:center;gap:12px;text-decoration:none;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.2rem;color:var(--c0-head)}
.v-n2 .links{display:flex;gap:26px;margin-left:auto}
.v-n2 .links a{font-weight:700;font-size:.95rem;color:var(--c0-ink);position:relative;padding:6px 0}
.v-n2 .links a::after{content:"";position:absolute;left:0;right:100%;bottom:0;height:2px;background:var(--c-primary);transition:right .25s var(--ease)}
.v-n2 .links a:hover::after{right:0}
.v-n2 .btn{font-size:.88rem}
@container elo (max-width:900px){.v-n2 .info .rejt{display:none}.v-n2 .links{display:none}.v-n2 .mnu{display:grid;margin-left:auto}.v-n2 .bar .btn{display:none}
 .v-n2.nyit .links{display:flex;flex-direction:column;gap:6px;position:absolute;left:0;right:0;top:100%;background:var(--c0-card);padding:14px var(--pad) 20px;box-shadow:var(--sh-3)}}
""", render=lambda c: f"""<header class="nav v-n2" data-nav><div class="info"><div class="wrap">
<span>{ui(fo_kapcs(c)[2])}{esc(fo_kapcs(c)[1])}</span><span class="rejt">{ui('ora')}{esc(g(c, 'kapcsolat', 'nyitva_rovid'))}</span>
<span class="jobbra rejt">{ui('pin')}{esc(g(c, 'kapcsolat', 'cim'))}</span></div></div>
<div class="bar"><div class="wrap">{brand(c, 50)}<nav class="links">{navlinkek(c)}</nav>{btn(g(c, 'nav', 'cta'), ikon='tel')}{MNU}</div></div></header>"""))


def _n3(c):
    lk = g(c, "nav", "linkek") or []
    fel = (len(lk) + 1) // 2
    bal = "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in lk[:fel])
    jobb = "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in lk[fel:])
    return (f'<header class="nav v-n3" data-nav><div class="wrap in"><nav class="links l">{bal}</nav>'
            f'<a class="brand" href="#top">{logo(c, 78)}</a><nav class="links r">{jobb}</nav>'
            f'<div class="cta">{btn(g(c, "nav", "cta"), ikon="tel")}</div>{MNU}</div></header>')


NAV.append(dict(id="n3", nev="Középre zárt, függő logóval", leiras="A logó középen, egy lelógó „címke” alján; a menü "
    "két oldalt. Klasszikus bolt- és vendéglőhangulat.", css=NAV_KOZOS + r"""
.v-n3{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--c0-paper) 92%,transparent);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--c0-line)}
.v-n3 .in{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;min-height:70px;gap:24px}
.v-n3 .links{display:flex;gap:28px;font-weight:700;font-size:.95rem;color:var(--c0-ink)}
.v-n3 .links a:hover{color:var(--c-primary-text)}
.v-n3 .links.l{justify-content:flex-end}
.v-n3 .links.r{justify-content:flex-start}
.v-n3 .brand{text-decoration:none;align-self:start;background:var(--c0-card);border-radius:0 0 999px 999px;padding:8px 20px 16px;box-shadow:var(--sh-2);margin-bottom:-34px;position:relative;z-index:2}
.v-n3 .cta{position:absolute;right:var(--pad);top:50%;transform:translateY(-50%)}
.v-n3 .cta .btn{font-size:.85rem}
@container elo (max-width:1100px){.v-n3 .cta{display:none}}
@container elo (max-width:820px){.v-n3 .in{grid-template-columns:auto 1fr auto}.v-n3 .links{display:none}.v-n3 .brand{grid-column:1;margin-bottom:-24px}.v-n3 .brand .logo{--logo-h:58px!important}.v-n3 .mnu{display:grid;grid-column:3}
 .v-n3.nyit .links{display:flex;flex-direction:column;position:absolute;left:0;right:0;top:100%;background:var(--c0-card);padding:12px var(--pad);gap:14px;box-shadow:var(--sh-3)}.v-n3.nyit .links.r{top:calc(100% + 120px)}}
""", render=_n3))

NAV.append(dict(id="n4", nev="Cégér (lengő tábla)", leiras="A logó egy láncon lógó, finoman lengő cégtáblán, mint egy "
    "belvárosi üzlet cégére. Egyedi, emlékezetes, helyi bolt érzet.", css=NAV_KOZOS + r"""
.v-n4{position:sticky;top:0;z-index:60;background:var(--c0-card);border-bottom:3px solid var(--c-primary)}
.v-n4 .in{display:flex;align-items:center;gap:26px;min-height:64px}
.v-n4 .ceg{position:relative;text-decoration:none;align-self:flex-start;margin-top:14px;margin-bottom:-58px;padding:12px 18px;background:var(--c0-paper);border:2px solid var(--c0-head);border-radius:14px;box-shadow:var(--sh-3);transform-origin:50% -14px;animation:n4leng 5.5s ease-in-out infinite;z-index:3}
.v-n4 .ceg::before,.v-n4 .ceg::after{content:"";position:absolute;top:-16px;width:2px;height:16px;background:var(--c0-head)}
.v-n4 .ceg::before{left:22%}.v-n4 .ceg::after{right:22%}
.v-n4 .ceg .bn{display:block;text-align:center;font-family:var(--f-display);font-weight:var(--w-display);font-size:.9rem;color:var(--c0-head);margin-top:4px}
@keyframes n4leng{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}
.v-n4 .links{display:flex;gap:6px;margin-left:auto}
.v-n4 .links a{padding:10px 14px;border-radius:10px;font-weight:700;font-size:.94rem;color:var(--c0-ink)}
.v-n4 .links a:hover{background:var(--c0-tint)}
.v-n4 .btn{font-size:.88rem}
@container elo (max-width:900px){.v-n4 .links{display:none}.v-n4 .mnu{display:grid;margin-left:auto}.v-n4 .btn{display:none}
 .v-n4.nyit .links{display:flex;flex-direction:column;position:absolute;left:0;right:0;top:100%;background:var(--c0-card);padding:14px var(--pad);box-shadow:var(--sh-3)}}
""", render=lambda c: f"""<header class="nav v-n4" data-nav><div class="wrap in"><a class="ceg anim" href="#top">{logo(c, 58, 'ko')}<span class="bn">{esc(g(c, 'marka', 'nev'))}</span></a><nav class="links">{navlinkek(c)}</nav>{btn(g(c, 'nav', 'cta'), ikon='tel')}{MNU}</div></header>"""))

NAV.append(dict(id="n5", nev="Minimál, nagy telefonszámmal", leiras="Csak a logó, egy nagy, kattintható telefonszám és "
    "egy Menü gomb; a menüpontok lenyíló panelen. Mobilon a legtisztább.", css=NAV_KOZOS + r"""
.v-n5{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--c0-paper) 90%,transparent);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.v-n5 .in{display:flex;align-items:center;gap:20px;min-height:76px}
.v-n5 .brand{display:flex;align-items:center;gap:12px;text-decoration:none;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.15rem;color:var(--c0-head)}
.v-n5 .tel{margin-left:auto;display:flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.05rem,2cqi,1.6rem);color:var(--c-primary-text)}
.v-n5 .tel .ui{width:34px;height:34px;padding:7px;border-radius:50%;background:var(--c-primary);color:var(--c-on-primary)}
.v-n5 .mb{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;border:2px solid var(--c0-head);background:transparent;font-weight:800;font-size:.9rem;cursor:pointer;color:var(--c0-head)}
.v-n5 .links{display:none;position:absolute;left:0;right:0;top:100%;background:var(--c0-card);padding:18px var(--pad) 26px;box-shadow:var(--sh-3);gap:10px 34px;flex-wrap:wrap}
.v-n5 .links a{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.5rem;color:var(--c0-head)}
.v-n5.nyit .links{display:flex}
@container elo (max-width:560px){.v-n5 .tel span{display:none}.v-n5 .brand .bn{display:none}}
""", render=lambda c: f"""<header class="nav v-n5" data-nav><div class="wrap in">{brand(c, 50)}<a class="tel" href="{esc(fo_kapcs(c)[0])}">{ui(fo_kapcs(c)[2])}<span>{esc(fo_kapcs(c)[1])}</span></a><button class="mb" type="button" data-mnu>{ui('menu')}Menü</button><nav class="links">{navlinkek(c)}</nav></div></header>"""))

NAV.append(dict(id="n6", nev="Újságfejléc (kétszintes)", leiras="Nagy, középre zárt logó vékony vonalak között, két "
    "oldalt apró infóval; alatta középre zárt menüsor. Nyomtatott étlap vagy napilap hangulat.", css=NAV_KOZOS + r"""
.v-n6{background:var(--c0-paper);position:relative;z-index:60}
.v-n6 .fent{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:24px;padding:18px 0 14px;border-bottom:1px solid var(--c0-line2)}
.v-n6 .apro{font-family:var(--f-label);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--c0-ink-2);display:flex;align-items:center;gap:8px}
.v-n6 .apro .ui{width:15px;height:15px;color:var(--c-primary-text)}
.v-n6 .apro.r{justify-content:flex-end}
.v-n6 .brand{display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.v-n6 .brand .bn{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.5rem;color:var(--c0-head);letter-spacing:.02em}
.v-n6 .links{display:flex;justify-content:center;gap:0;padding:12px 0;border-bottom:3px double var(--c0-line2)}
.v-n6 .links a{font-weight:700;font-size:.9rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c0-ink);padding:2px 22px;border-left:1px solid var(--c0-line2)}
.v-n6 .links a:first-child{border-left:0}
.v-n6 .links a:hover{color:var(--c-primary-text)}
@container elo (max-width:820px){.v-n6 .apro{display:none}.v-n6 .fent{grid-template-columns:1fr auto 1fr}.v-n6 .links{display:none}.v-n6 .mnu{display:grid;justify-self:end}
 .v-n6.nyit .links{display:flex;flex-direction:column;align-items:center;gap:10px}.v-n6.nyit .links a{border:0}}
""", render=lambda c: f"""<header class="nav v-n6" data-nav><div class="wrap"><div class="fent"><span class="apro">{ui('pin')}{esc(g(c, 'kapcsolat', 'cim'))}</span><a class="brand" href="#top">{logo(c, 70, 'ko')}<span class="bn">{esc(g(c, 'marka', 'nev'))}</span></a><span class="apro r">{ui('ora')}{esc(g(c, 'kapcsolat', 'nyitva_rovid'))}</span>{MNU}</div><nav class="links">{navlinkek(c)}</nav></div></header>"""))

# ============================================================== HERO
HERO = []


def _hero_szoveg(c, cls="txt bal", chipek=True, jegyzet=True, stat=False):
    h = c.get("hero", {})
    return (f'<div class="{cls}" data-rv>'
            + (f'<div class="chips">{chips(h.get("badgek"))}</div>' if chipek and h.get("badgek") else kick(h.get("kicker")))
            + f'<h1 class="hcim">{md(h.get("cim", ""))}</h1>'
            + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "")
            + gombsor(h)
            + (kezi(h.get("jegyzet")) if jegyzet else "")
            + (statok(h.get("statok")) if stat else "")
            + "</div>")


def _h1(c):
    f = HF(c, "h1")
    return (f'<section class="sec v-h1 s-primary tx" id="top">{dk(c, "hero", matrica=True)}<div class="wrap grid">'
            + _hero_szoveg(c)
            + f'<div class="koll" data-rv><div class="k ka">{foto(c, F(f, 0), "4/5")}</div>'
            f'<div class="k kb">{foto(c, F(f, 1), "1/1")}</div><div class="k kc">{foto(c, F(f, 2), "1/1")}</div>'
            f'<div class="k kl">{logo(c, 110, "ko")}</div></div></div></section>')


HERO.append(dict(id="h1", nev="Színes fotókollázs", leiras="Telt márkaszínű háttér, balra a nagy cím, jobbra "
    "egymásra csúsztatott fotók, kör alakú kép és logó-matrica. Harsány, élettel teli, azonnal megjegyezhető.", css=r"""
.v-h1{padding:clamp(110px,11cqi,150px) 0 clamp(70px,8cqi,116px)}
.v-h1 .grid{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(28px,4cqi,64px);align-items:center}
.v-h1 .chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.v-h1 .chips .chip{background:color-mix(in srgb,var(--c0-card) 92%,transparent);color:var(--c0-ink);border-color:transparent}
.v-h1 .chips .chip .ui{color:var(--c0-primary-text)}
.v-h1 .lead{margin:22px 0 30px;color:var(--c-ink-2)}
.v-h1 .jegyzet{margin:30px 0 0;display:inline-block;max-width:420px;background:var(--c0-paper);color:var(--c-hand);padding:12px 18px;border-radius:6px;transform:rotate(-1.5deg);box-shadow:var(--sh-3)}
.v-h1 .koll{position:relative;min-height:clamp(380px,44cqi,560px)}
.v-h1 .k{position:absolute}
.v-h1 .ka{left:3%;top:5%;width:55%;transform:rotate(-3deg);z-index:2}
.v-h1 .kb{right:0;top:0;width:41%;transform:rotate(4deg);z-index:3}
.v-h1 .kc{right:9%;bottom:0;width:35%;z-index:4}
.v-h1 .kc .ft{background:none;padding:0;box-shadow:none;transform:none;filter:none}
.v-h1 .kc .ft::before,.v-h1 .kc .ft::after{display:none}
.v-h1 .kc .ph{border-radius:50%;box-shadow:0 0 0 7px var(--c0-card),var(--sh-3);animation:none}
.v-h1 .kl{left:0;bottom:4%;width:clamp(96px,12cqi,140px);aspect-ratio:1;border-radius:50%;background:#fff;--logo-img:var(--logo-eredeti);display:grid;place-items:center;box-shadow:var(--sh-3);transform:rotate(-8deg);z-index:5;padding:12px}
.v-h1 .kl .logo{height:100%!important;width:100%;aspect-ratio:auto!important;background-position:center}
@container elo (max-width:880px){.v-h1 .grid{grid-template-columns:1fr}.v-h1 .koll{min-height:clamp(300px,80cqi,480px);max-width:560px;width:100%;margin:0 auto}}
""", render=_h1))


def _h2(c):
    h = c.get("hero", {})
    f = HF(c, "h2")
    return (f'<section class="sec v-h2 s-paper tx" id="top">{dk(c, "hero")}<div class="wrap grid"><div class="txt bal" data-rv>'
            f'{logo(c, 104)}<p class="meta mono">{md(h.get("meta") or h.get("kicker", ""))}</p>'
            f'<h1 class="hcim">{md(h.get("cim", ""))}</h1>'
            + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "") + gombsor(h) + kezi(h.get("jegyzet"))
            + statok(h.get("statok")) + '</div><div class="mozaik" data-rv><div class="c1">'
            + foto(c, F(f, 0), "16/11") + foto(c, F(f, 1), "16/11") + foto(c, F(f, 2), "16/11")
            + f'</div><div class="c2">{foto(c, F(f, 3), "3/5")}</div></div></div></section>')


HERO.append(dict(id="h2", nev="Fotómozaik + álló kép", leiras="Nagy logó, apró betűs „menetrend” sor, erős cím, "
    "számok; jobbra fotómozaik egy magas képpel és halvány szellemszóval. Fesztiválos, gazdag, sokat mutat.", css=r"""
.v-h2{padding:clamp(100px,10cqi,140px) 0 clamp(64px,7cqi,100px)}
.v-h2 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,4.4cqi,70px);align-items:center}
.v-h2 .logo{margin-bottom:16px}
.v-h2 .meta{border-top:2px solid var(--c-head);padding-top:10px;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--c-ink-2);margin:0 0 22px}
.v-h2 .meta b{color:var(--hl)}
.v-h2 .lead{margin:20px 0 28px}
.v-h2 .jegyzet{margin-top:22px;max-width:380px}
.v-h2 .stat{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--c-line2);margin-top:30px;padding-top:18px;gap:14px}
.v-h2 .stat b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,2.6cqi,2.2rem);line-height:1;color:var(--c-head);margin-bottom:6px}
.v-h2 .stat span{font-family:var(--f-label);font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--c-ink-3);line-height:1.35;display:block}
.v-h2 .mozaik{display:grid;grid-template-columns:1fr .9fr;gap:14px;align-items:start}
.v-h2 .c1{display:grid;gap:14px}
.v-h2 .c2{margin-top:60px}
@container elo (max-width:900px){.v-h2 .grid{grid-template-columns:1fr}.v-h2 .mozaik{max-width:620px}}
""", render=_h2))


def _h3(c):
    h = c.get("hero", {})
    f = HF(c, "h3")
    return (f'<section class="sec v-h3 s-paper" id="top">{ph(c, F(f, 0), "bg")}<div class="shade"></div>'
            f'<div class="wrap"><div class="card s-vilagos bal" data-rv>{kick(h.get("kicker"))}'
            f'<h1 class="hcim">{md(h.get("cim", ""))}</h1>' + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "")
            + gombsor(h) + f'<div class="chips">{chips(h.get("badgek"))}</div></div></div>'
            + (f'<div class="float kezi" data-rv>{md(h["jegyzet"])}</div>' if h.get("jegyzet") else "") + '</section>')


HERO.append(dict(id="h3", nev="Teljes képes, kártyával", leiras="A legjobb fotó kitölti a teljes képernyőt, rajta egy "
    "tiszta, világos kártya a címmel és a gombokkal. Hangulatos, „itt vagy” érzés.", css=r"""
.v-h3{padding:clamp(120px,12cqi,170px) 0 clamp(60px,7cqi,100px);min-height:clamp(560px,60cqi,740px);display:flex;align-items:center}
.v-h3 .bg{position:absolute;inset:0;aspect-ratio:auto;height:100%;z-index:-2}
.v-h3 .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.42),rgba(0,0,0,.08) 62%,transparent);z-index:-1}
.v-h3 .wrap{width:100%}
.v-h3 .card{max-width:580px;background:color-mix(in srgb,var(--c0-card) 95%,transparent);border-radius:26px;padding:clamp(24px,3.4cqi,46px);box-shadow:var(--sh-3)}
.v-h3 .lead{margin:18px 0 26px}
.v-h3 .chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.v-h3 .float{position:absolute;right:var(--pad);bottom:clamp(24px,4cqi,50px);background:var(--c0-paper);padding:12px 18px;border-radius:8px;transform:rotate(2deg);box-shadow:var(--sh-3);max-width:320px;z-index:3}
@container elo (max-width:760px){.v-h3{min-height:0;padding-top:58cqi;align-items:flex-end}.v-h3 .bg{height:62cqi;bottom:auto}.v-h3 .shade{display:none}.v-h3 .float{display:none}}
""", render=_h3))


def _h4(c):
    h = c.get("hero", {})
    f = HF(c, "h4")
    pe = g(c, "motivum", "matricak", 0) or ""
    return (f'<section class="sec v-h4 s-paper tx" id="top">{dk(c, "hero")}<div class="wrap"><div class="top bal" data-rv>'
            f'{kick(h.get("kicker"))}<h1 class="hcim">{md(h.get("cim", ""))}</h1></div>'
            f'<div class="row" data-rv>' + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "") + gombsor(h)
            + f'</div><div class="strip" data-rv><div class="s s1">{foto(c, F(f, 0), "4/5")}</div>'
            f'<div class="s s2">{foto(c, F(f, 1), "5/4")}</div><div class="s s3">{foto(c, F(f, 2), "4/5")}</div>'
            + (f'<div class="pecset"><span>{esc(pe)}</span></div>' if pe else "") + '</div></div></section>')


HERO.append(dict(id="h4", nev="Plakát-tipográfia", leiras="Óriási, plakátszerű cím a teljes szélességben, alatta egy "
    "lépcsőzetes fotósor pecséttel. Magabiztos, városi, nagyon karakteres.", css=r"""
.v-h4{padding:clamp(110px,11cqi,150px) 0 clamp(60px,7cqi,100px)}
.v-h4 .hcim{font-size:calc(var(--t-hero)*1.42);line-height:.96;max-width:15ch}
.v-h4 .row{display:flex;gap:34px;align-items:flex-end;justify-content:space-between;margin:28px 0 46px;flex-wrap:wrap}
.v-h4 .row .lead{margin:0;max-width:52ch}
.v-h4 .strip{display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:18px;align-items:end;position:relative}
.v-h4 .s2{transform:translateY(-28px)}
.v-h4 .pecset{position:absolute;left:50%;top:-58px;width:124px;height:124px;border-radius:50%;background:var(--c-accent);color:var(--c-on-accent);display:grid;place-items:center;text-align:center;padding:16px;font-family:var(--f-display);font-weight:var(--w-display);font-size:.88rem;line-height:1.1;text-transform:uppercase;transform:translateX(-50%) rotate(-10deg);box-shadow:var(--sh-3);z-index:4}
.v-h4 .pecset::before{content:"";position:absolute;inset:7px;border-radius:50%;border:1.5px dashed currentColor;opacity:.6}
@container elo (max-width:760px){.v-h4 .strip{grid-template-columns:1fr 1fr}.v-h4 .s3{display:none}.v-h4 .s2{transform:none}.v-h4 .pecset{width:96px;height:96px;font-size:.7rem;top:-40px}}
""", render=_h4))


def _h5(c):
    h = c.get("hero", {})
    f = HF(c, "h5")
    km = h.get("kiemelt") or {}
    kk = (f'<div class="kartya s-vilagos">{ik(km.get("ikon"))}<div><b>{esc(km.get("cim", ""))}</b>'
          f'<span>{md(km.get("szoveg", ""))}</span></div></div>') if km else ""
    return (f'<section class="sec v-h5 s-tint" id="top"><div class="grid"><div class="txt"><div class="in bal" data-rv>'
            f'{kick(h.get("kicker"))}<h1 class="hcim">{md(h.get("cim", ""))}</h1>'
            + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "") + gombsor(h) + statok(h.get("statok"))
            + f'</div></div><div class="kep" data-rv>{foto(c, F(f, 0), "auto")}{kk}</div></div></section>')


HERO.append(dict(id="h5", nev="Osztott, nagy fotóval", leiras="Kettéosztott kép: balra halvány márkaszínű panel a "
    "szöveggel, jobbra egy nagy, magas fotó lebegő kiemelő-kártyával. Letisztult, magazinos, prémium.", css=r"""
.v-h5{padding:0}
.v-h5 .grid{display:grid;grid-template-columns:1fr 1fr;min-height:clamp(560px,58cqi,740px)}
.v-h5 .txt{display:flex;align-items:center;justify-content:flex-end;padding:clamp(110px,10cqi,150px) clamp(24px,5cqi,76px) clamp(56px,6cqi,90px) var(--pad)}
.v-h5 .in{max-width:560px}
.v-h5 .lead{margin:20px 0 28px}
.v-h5 .stat{display:flex;gap:28px;margin-top:34px;flex-wrap:wrap}
.v-h5 .stat b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.9rem;line-height:1;color:var(--hl)}
.v-h5 .stat span{font-size:.84rem;color:var(--c-ink-2)}
.v-h5 .kep{position:relative;padding:clamp(90px,8cqi,110px) var(--pad) 28px 0}
.v-h5 .kep .ft{height:100%}
.v-h5 .kep .ph{aspect-ratio:auto;height:100%;min-height:440px}
.v-h5 .kartya{position:absolute;left:-34px;bottom:64px;display:flex;gap:12px;align-items:center;background:var(--c0-card);border-radius:18px;padding:14px 18px 14px 14px;box-shadow:var(--sh-3);max-width:320px;z-index:3}
.v-h5 .kartya .ik{--ik:52px}
.v-h5 .kartya b{display:block;font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.05rem);color:var(--c-hand);line-height:1.1}
.v-h5 .kartya span{font-size:.9rem;font-weight:700;color:var(--c0-head)}
@container elo (max-width:860px){.v-h5 .grid{grid-template-columns:1fr}.v-h5 .kep{order:-1;padding:96px var(--pad) 0}.v-h5 .kep .ph{min-height:300px}.v-h5 .txt{justify-content:flex-start;padding-top:40px}.v-h5 .kartya{left:auto;right:calc(var(--pad) + 10px);bottom:-24px}}
""", render=_h5))


def _h6(c):
    h = c.get("hero", {})
    f = HF(c, "h6")
    return (f'<section class="sec v-h6 s-paper tx" id="top">{dk(c, "hero")}'
            f'<div class="fl anim a">{foto(c, F(f, 0), "1/1")}</div><div class="fl anim b">{foto(c, F(f, 1), "4/5")}</div>'
            f'<div class="fl anim cc">{foto(c, F(f, 2), "4/5")}</div><div class="fl anim d">{foto(c, F(f, 3), "1/1")}</div>'
            f'<div class="wrap"><div class="mid" data-rv>{kick(h.get("kicker"))}<h1 class="hcim">{md(h.get("cim", ""))}</h1>'
            + (f'<p class="lead">{md(h["lead"])}</p>' if h.get("lead") else "") + gombsor(h)
            + f'<div class="chips">{chips(h.get("badgek"))}</div></div></div></section>')


HERO.append(dict(id="h6", nev="Középre zárt, lebegő fotókkal", leiras="Középen a cím és a gombok, körülötte négy fotó "
    "lassan lebeg a sarkokban. Nyitott, barátságos, játékos.", css=r"""
.v-h6{padding:clamp(140px,13cqi,190px) 0 clamp(90px,10cqi,150px);text-align:center}
.v-h6 .mid{max-width:760px;margin:0 auto;position:relative;z-index:3}
.v-h6 .kick{justify-content:center}
.v-h6 .lead{margin:20px auto 30px}
.v-h6 .gombsor{justify-content:center}
.v-h6 .chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:26px}
.v-h6 .fl{position:absolute;z-index:1;width:clamp(120px,15cqi,220px);animation:h6lebeg 8s ease-in-out infinite alternate}
.v-h6 .a{left:3%;top:16%;--r:-6deg}.v-h6 .b{left:8%;bottom:6%;width:clamp(100px,12cqi,180px);--r:5deg;animation-duration:9.5s}
.v-h6 .cc{right:4%;top:13%;--r:6deg;animation-duration:7.2s}.v-h6 .d{right:9%;bottom:7%;width:clamp(100px,12cqi,170px);--r:-4deg;animation-duration:10s}
@keyframes h6lebeg{from{transform:translateY(0) rotate(var(--r))}to{transform:translateY(-14px) rotate(calc(var(--r)*-1))}}
@container elo (max-width:980px){.v-h6 .b,.v-h6 .d{display:none}.v-h6 .a,.v-h6 .cc{width:18cqi;top:92px}.v-h6{padding-top:calc(120px + 16cqi)}}
""", render=_h6))


def _h7(c):
    h = c.get("hero", {})
    f = HF(c, "h7")
    t = h.get("tabla") or {}
    sorok = "".join(f'<li><span class="n">{esc(n)}</span><i></i><span class="a">{esc(a)}</span></li>' for n, a in (t.get("sorok") or []))
    return (f'<section class="sec v-h7 s-sand tx" id="top">{dk(c, "hero")}<div class="wrap grid">'
            + _hero_szoveg(c, jegyzet=False)
            + f'<div class="tw" data-rv><div class="tabla s-deep"><p class="tc">{esc(t.get("cim", ""))}</p><ul>{sorok}</ul>'
            f'<p class="tl">{md(t.get("lab", ""))}</p></div><div class="tf">{foto(c, F(f, 0), "1/1")}</div></div></div></section>')


HERO.append(dict(id="h7", nev="Krétatábla", leiras="Balra a cím, jobbra egy fakeretes krétatábla a kedvenc "
    "tételekkel és árakkal, sarkán egy kerek fotóval. Vendéglátós, őszinte, azonnal informál.", css=r"""
.v-h7{padding:clamp(110px,11cqi,150px) 0 clamp(64px,7cqi,104px)}
.v-h7 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5cqi,80px);align-items:center}
.v-h7 .chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.v-h7 .lead{margin:20px 0 28px}
.v-h7 .tw{position:relative;padding:44px 0 10px 0}
.v-h7 .tabla{position:relative;background:var(--c-deep);color:var(--c-on-deep);border-radius:12px;padding:clamp(24px,3.2cqi,40px) clamp(22px,3.2cqi,40px) 30px;border:12px solid color-mix(in srgb,var(--c-accent) 45%,#5b3f28);box-shadow:var(--sh-3),inset 0 0 60px rgba(0,0,0,.35);transform:rotate(1.2deg)}
.v-h7 .tabla::before{content:"";position:absolute;inset:0;background-image:var(--zaj);opacity:.5;mix-blend-mode:screen;pointer-events:none;border-radius:4px}
.v-h7 .tc{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.55rem);line-height:1.1;margin:0 0 14px;color:var(--c-deep-hl);padding-right:clamp(96px,12cqi,150px)}
.v-h7 ul{display:grid;gap:12px}
.v-h7 li{display:flex;align-items:baseline;gap:8px;font-size:1.02rem}
.v-h7 li .n{font-weight:700}
.v-h7 li i{flex:1;border-bottom:2px dotted var(--c-line2);transform:translateY(-4px)}
.v-h7 li .a{font-family:var(--f-display);font-weight:var(--w-display);color:var(--c-deep-hl);white-space:nowrap}
.v-h7 .tl{margin:18px 0 0;font-size:.84rem;color:var(--c-on-deep-2)}
.v-h7 .tf{position:absolute;right:-16px;top:0;width:clamp(116px,13cqi,164px);z-index:3}
.v-h7 .tf .ft{background:none;padding:0;box-shadow:none;transform:none;filter:none}
.v-h7 .tf .ft::before,.v-h7 .tf .ft::after{display:none}
.v-h7 .tf .ph{border-radius:50%;box-shadow:0 0 0 7px var(--c0-card),var(--sh-3);animation:none}
@container elo (max-width:900px){.v-h7 .grid{grid-template-columns:1fr}.v-h7 .tf{right:0}}
""", render=_h7))

# ============================================================== TÉNYEK
TENYEK = []


def _tel(c):
    return (g(c, "tenyek", "elemek") or [])[:5]


def _szam(e):
    return f'<b class="szam">{esc(e["szam"])}</b>' if e.get("szam") else ""


def _p1(c):
    el = _tel(c)
    k = "".join(f'<article class="krt" data-rv><div class="krt-fej">{ik(e.get("ikon"))}</div>{_szam(e)}'
                f'<h3 class="krt-h">{md(e.get("cim", ""))}</h3><p class="krt-p">{md(e.get("szoveg", ""))}</p></article>' for e in el)
    return (f'<section class="sec v-p1 s-white"><div class="wrap">{shead(c.get("tenyek"))}'
            f'<div class="racs" style="--oszlop:{min(4, len(el) or 1)}">{k}</div></div></section>')


TENYEK.append(dict(id="p1", nev="Tény-kártyák számokkal", leiras="Kártyasor: ikon, nagy szám vagy kulcsszó, rövid "
    "magyarázat. A kártyák a választott kártyastílust kapják.", css=r"""
.v-p1 .szam{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.3rem,2.1cqi,1.9rem);line-height:1.05;color:var(--hl);overflow-wrap:anywhere;margin-top:4px}
.v-p1 .krt-h{font-size:1.08rem}
""", render=_p1))


def _p2(c):
    el = _tel(c)
    sp = "".join(f'<span>{ik(e.get("ikon"))}{md(e.get("cim", ""))}</span>' for e in el) * 2
    return f'<section class="v-p2 s-primary" aria-label="Röviden"><div class="tick"><div class="tick-in anim">{sp}</div></div></section>'


TENYEK.append(dict(id="p2", nev="Futó tény-szalag", leiras="Megdöntött, végtelenül futó szalag a legfontosabb "
    "tényekkel és ikonokkal, közvetlenül a hero alatt. Fesztiválos energia, kevés helyen sok infó.", css=r"""
.v-p2{position:relative;z-index:6;background:var(--c-primary);color:var(--c-on-primary);margin:-18px -2% 0;width:104%;transform:rotate(-1.3deg);box-shadow:var(--sh-3);overflow:hidden}
.v-p2 .tick-in{display:flex;width:max-content;animation:p2fut 38s linear infinite}
.v-p2 span{display:inline-flex;align-items:center;gap:14px;padding:18px 30px 18px 0;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.02rem,1.55cqi,1.32rem);text-transform:uppercase;letter-spacing:.01em;white-space:nowrap}
.v-p2 .ik{--ik:40px}
@keyframes p2fut{to{transform:translateX(-50%)}}
""", render=_p2))


def _p3(c):
    el = _tel(c)
    li = "".join(f'<li data-rv>{ik(e.get("ikon"))}<div><h3>{md(e.get("cim", ""))}</h3><p>{md(e.get("szoveg", ""))}</p></div></li>' for e in el)
    return (f'<section class="sec v-p3 s-white"><div class="wrap">{shead(c.get("tenyek"))}'
            f'<ul class="sor" style="--n:{len(el) or 1}">{li}</ul></div></section>')


TENYEK.append(dict(id="p3", nev="Ikonos sor elválasztókkal", leiras="Egyetlen tiszta sor: ikon és rövid szöveg, "
    "szaggatott vonalakkal elválasztva, kártyák nélkül. Levegős, gyorsan olvasható.", css=r"""
.v-p3 .sor{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr))}
.v-p3 li{display:flex;gap:14px;align-items:flex-start;padding:4px 24px;border-left:2px dashed var(--c-line2)}
.v-p3 li:first-child{border-left:0;padding-left:0}
.v-p3 .ik{--ik:54px}
.v-p3 li h3{font-size:1.06rem;margin:4px 0 6px}
.v-p3 li p{margin:0;font-size:.93rem;color:var(--c-ink-2)}
@container elo (max-width:980px){.v-p3 .sor{grid-template-columns:1fr 1fr;gap:26px 0}.v-p3 li:nth-child(odd){border-left:0;padding-left:0}}
@container elo (max-width:560px){.v-p3 .sor{grid-template-columns:1fr}.v-p3 li{border-left:0;padding-left:0;border-top:2px dashed var(--c-line2);padding-top:18px}.v-p3 li:first-child{border-top:0}}
""", render=_p3))


def _p4(c):
    el = _tel(c)[:4]
    out = []
    for e in el:
        i = uid()
        out.append(f'<div class="pe" data-rv><div class="kor"><svg class="gyuru anim" viewBox="0 0 160 160" aria-hidden="true">'
                   f'<defs><path id="pk{i}" d="M80,80 m-62,0 a62,62 0 1,1 124,0 a62,62 0 1,1 -124,0"/></defs>'
                   f'<text><textPath href="#pk{i}">{korszoveg(e.get("korszoveg") or sima(e.get("cim", "")))}</textPath></text></svg>'
                   f'{ik(e.get("ikon"))}</div><h3>{md(e.get("cim", ""))}</h3><p>{md(e.get("szoveg", ""))}</p></div>')
    return (f'<section class="sec v-p4 s-paper tx">{dk(c, "tenyek")}<div class="wrap">{shead(c.get("tenyek"))}'
            f'<div class="pecsetek" style="--n:{len(el) or 1}">{"".join(out)}</div></div></section>')


TENYEK.append(dict(id="p4", nev="Minőségi pecsétek", leiras="Kerek pecsétek körbefutó felirattal (lassan forognak), "
    "középen ikon, alatta a tény. Kézműves „garancia” hatás.", css=r"""
.v-p4 .pecsetek{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:var(--gap);text-align:center}
.v-p4 .kor{position:relative;width:156px;height:156px;margin:0 auto 18px;display:grid;place-items:center}
.v-p4 .gyuru{position:absolute;inset:0;width:100%;height:100%;animation:p4forog 36s linear infinite}
.v-p4 .gyuru text{font-family:var(--f-label);font-size:11.5px;letter-spacing:2.1px;fill:var(--hl);font-weight:600}
.v-p4 .kor::before{content:"";position:absolute;inset:27px;border-radius:50%;background:var(--c-card);box-shadow:var(--sh-2);border:2px dashed var(--c-line2)}
.v-p4 .kor .ik{position:relative;--ik:60px}
.v-p4 .pe h3{font-size:1.1rem;margin-bottom:6px}
.v-p4 .pe p{font-size:.93rem;color:var(--c-ink-2);max-width:30ch;margin:0 auto}
@keyframes p4forog{to{transform:rotate(360deg)}}
@container elo (max-width:900px){.v-p4 .pecsetek{grid-template-columns:1fr 1fr;row-gap:36px}}
""", render=_p4))


def _p5(c):
    el = _tel(c)[:4]
    d = "".join(f'<div class="sz" data-rv><b>{md(e.get("szam") or e.get("cim", ""))}</b>'
                f'{"<h3>" + md(e.get("cim", "")) + "</h3>" if e.get("szam") else ""}<p>{md(e.get("szoveg", ""))}</p></div>' for e in el)
    return (f'<section class="sec v-p5 s-white"><div class="wrap grid">{shead(c.get("tenyek"), bal=True)}'
            f'<div class="szamok">{d}</div></div></section>')


TENYEK.append(dict(id="p5", nev="Szerkesztőségi számok", leiras="Balra a szekció címe, jobbra 2×2 rácsban nagy "
    "számok vagy kulcsszavak vékony vonalakkal. Magabiztos, adatvezérelt, magazinos.", css=r"""
.v-p5 .grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(30px,5cqi,80px);align-items:start}
.v-p5 .shead{margin-bottom:0}
.v-p5 .szamok{display:grid;grid-template-columns:1fr 1fr}
.v-p5 .sz{padding:22px 26px 22px 0;border-top:1px solid var(--c-line2)}
.v-p5 .sz b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.7rem,3.4cqi,2.9rem);line-height:1.02;color:var(--hl);margin-bottom:10px}
.v-p5 .sz h3{font-size:1rem;margin-bottom:4px}
.v-p5 .sz p{margin:0;font-size:.93rem;color:var(--c-ink-2)}
@container elo (max-width:860px){.v-p5 .grid{grid-template-columns:1fr}}
@container elo (max-width:520px){.v-p5 .szamok{grid-template-columns:1fr}}
""", render=_p5))


def _p6(c):
    el = _tel(c)
    ch = "".join(f'<span class="chip nagy" data-rv>{ik(e.get("ikon"))}<b>{md(e.get("cim", ""))}</b></span>' for e in el)
    return (f'<section class="sec v-p6 s-tint">{dk(c, "tenyek")}<div class="wrap">{shead(c.get("tenyek"))}'
            f'<div class="felho">{ch}</div></div></section>')


TENYEK.append(dict(id="p6", nev="Chip-felhő", leiras="Középre zárt, enyhén megdöntött „címkék” ikonnal. Könnyed, "
    "kompakt, ha a tények rövidek.", css=r"""
.v-p6 .felho{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;max-width:940px;margin:0 auto}
.v-p6 .chip.nagy{padding:9px 20px 9px 10px;font-size:1.02rem;gap:12px;box-shadow:var(--sh-2)}
.v-p6 .chip.nagy b{font-weight:800}
.v-p6 .chip .ik{--ik:38px}
.v-p6 .chip:nth-child(odd){transform:rotate(-1.2deg)}.v-p6 .chip:nth-child(even){transform:rotate(1deg)}
""", render=_p6))

# ============================================================== KÍNÁLAT
KINALAT = []


def _kel(c):
    return g(c, "kinalat", "elemek") or []


def _link(e, szoveg="Részletek"):
    if not e.get("link"):
        return ""
    return f'<a class="tovabb" href="{esc(e["link"])}">{esc(e.get("link_szoveg", szoveg))}{ui("nyil")}</a>'


def _kin_lab(c):
    k = c.get("kinalat", {})
    b = btn(k.get("cta"))
    return f'<div class="lab">{b}</div>' if b else ""


KIN_KOZOS = r"""
.tovabb{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:.9rem;color:var(--hl);text-decoration:none}
.tovabb .ui{width:16px;height:16px;transition:transform .2s var(--ease)}
.tovabb:hover .ui{transform:translateX(4px)}
.lab{display:flex;justify-content:center;margin-top:clamp(28px,4cqi,48px)}
"""


def _k1(c):
    el = _kel(c)
    k = "".join(f'<article class="krt" data-rv><div class="krt-fej">{ik(e.get("ikon"))}<h3 class="krt-h">{md(e.get("nev", ""))}</h3></div>'
                f'<p class="krt-p">{md(e.get("leiras", ""))}</p><p class="krt-meta"><span>{esc(e.get("ar", ""))}</span>{_link(e)}</p></article>' for e in el)
    return (f'<section class="sec v-k1 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="racs" style="--oszlop:{min(4, len(el) or 1)}">{k}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k1", nev="Ikonos kártyarács", leiras="Minden kategória egy kártya: ikon és cím egy sorban, "
    "rövid leírás, ár-tól. Rendezett, gyorsan átlátható.", css=KIN_KOZOS + r"""
.v-k1 .krt-meta{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
""", render=_k1))


def _k2(c):
    el = _kel(c)
    k = "".join(f'<article class="krt" data-rv>{foto(c, e.get("foto"), "16/11", "krt-kep")}<div class="krt-fej">{ik(e.get("ikon"))}'
                f'<h3 class="krt-h">{md(e.get("nev", ""))}</h3></div><p class="krt-p">{md(e.get("leiras", ""))}</p>'
                f'<p class="krt-meta"><span class="cimke">{esc(e.get("ar", ""))}</span>{_link(e)}</p></article>' for e in el)
    return (f'<section class="sec v-k2 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="racs" style="--oszlop:{min(4, len(el) or 1)}">{k}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k2", nev="Fotós csempék", leiras="Kártyák nagy fotóval a tetején, alatta ikon, cím, leírás "
    "és ár-címke. Étvágycsináló, a fotók adják el.", css=KIN_KOZOS + r"""
.v-k2 .krt-meta{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.v-k2 .krt .ik{--ik:40px}
""", render=_k2))


def _k3(c):
    el = _kel(c)
    if not el:
        return ""
    e0 = el[0]
    big = (f'<a class="b big" href="{esc(e0.get("link", "#"))}" data-rv>{ph(c, e0.get("foto"))}<div class="ov">'
           f'<span class="cimke">{esc(e0.get("ar", ""))}</span><h3>{md(e0.get("nev", ""))}</h3><p>{md(e0.get("leiras", ""))}</p></div></a>')
    rest = "".join(f'<article class="krt b" data-rv><div class="krt-fej">{ik(e.get("ikon"))}<h3 class="krt-h">{md(e.get("nev", ""))}</h3></div>'
                   f'<p class="krt-p">{md(e.get("leiras", ""))}</p><p class="krt-meta"><span>{esc(e.get("ar", ""))}</span>{_link(e)}</p></article>'
                   for e in el[1:4])
    return (f'<section class="sec v-k3 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="bento n{min(len(el), 4)}">{big}{rest}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k3", nev="Bento-rács", leiras="Egy nagy, fotós kiemelt csempe és mellette kisebb kártyák "
    "aszimmetrikus rácsban. Modern, dinamikus, a fő terméket előtérbe tolja.", css=KIN_KOZOS + r"""
.v-k3 .bento{display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-auto-rows:minmax(200px,auto);gap:var(--gap)}
.v-k3 .big{grid-row:span 2;position:relative;border-radius:var(--r);overflow:hidden;min-height:440px;color:#fff;text-decoration:none;box-shadow:var(--sh-3)}
.v-k3 .big .ph{position:absolute;inset:0;aspect-ratio:auto;height:100%;transition:transform .8s var(--ease)}
.v-k3 .big:hover .ph{transform:scale(1.04)}
.v-k3 .big .ov{position:absolute;inset:auto 0 0 0;padding:28px;background:linear-gradient(transparent,rgba(0,0,0,.74))}
.v-k3 .big h3{color:#fff;font-size:clamp(1.5rem,2.6cqi,2.2rem);margin:10px 0 6px}
.v-k3 .big p{color:rgba(255,255,255,.88);margin:0}
.v-k3 .big .cimke{background:var(--c-accent);color:var(--c-on-accent)}
.v-k3 .n4 .b:nth-child(4){grid-column:2/4}
.v-k3 .krt-meta{display:flex;justify-content:space-between;align-items:center}
@container elo (max-width:900px){.v-k3 .bento{grid-template-columns:1fr 1fr}.v-k3 .big{grid-column:1/-1;grid-row:auto;min-height:360px}.v-k3 .n4 .b:nth-child(4){grid-column:auto}}
@container elo (max-width:560px){.v-k3 .bento{grid-template-columns:1fr}}
""", render=_k3))

RAIL_CSS = r"""
.rail-w{position:relative}
.rail{display:grid;grid-auto-flow:column;grid-auto-columns:clamp(250px,29cqi,330px);gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;padding:8px 6px 22px;scrollbar-width:none;cursor:grab}
.rail::-webkit-scrollbar{display:none}
.rail>*{scroll-snap-align:start}
.rail-nav{display:flex;align-items:center;gap:16px;margin-top:8px}
.rail-nav .rb{width:46px;height:46px;border-radius:50%;border:2px solid var(--c-head);background:transparent;cursor:pointer;display:grid;place-items:center;color:var(--c-head);transition:background .2s,color .2s}
.rail-nav .rb:hover{background:var(--c-head);color:var(--sec-bg,var(--c-paper))}
.rail-bar{flex:1;height:3px;background:var(--c-line);border-radius:3px;overflow:hidden}
.rail-bar i{display:block;height:100%;width:30%;background:var(--c-primary);border-radius:3px;transform-origin:left;transition:transform .2s}
"""


def rail_nav():
    return (f'<div class="rail-nav"><button class="rb" type="button" data-rail="-1" aria-label="Vissza">{ui("bal")}</button>'
            f'<div class="rail-bar"><i></i></div><button class="rb" type="button" data-rail="1" aria-label="Tovább">{ui("jobb")}</button></div>')


def _k4(c):
    el = _kel(c)
    k = "".join(f'<article class="rk" data-rv>{foto(c, e.get("foto"), "4/5")}<div class="rt"><div class="rf">{ik(e.get("ikon"))}'
                f'<h3>{md(e.get("nev", ""))}</h3></div><p>{md(e.get("leiras", ""))}</p><div class="ra"><span class="cimke">{esc(e.get("ar", ""))}</span>{_link(e)}</div></div></article>' for e in el)
    return (f'<section class="sec v-k4 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"), bal=True)}'
            f'<div class="rail-w" data-railw><div class="rail">{k}</div>{rail_nav()}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k4", nev="Vízszintes sín", leiras="Oldalra görgethető, magas fotós kártyák nyilakkal és "
    "haladásjelzővel. Sok elemnél is rendezett; mobilon ujjal húzható.", css=KIN_KOZOS + RAIL_CSS + r"""
.v-k4 .rt{padding:16px 4px 0}
.v-k4 .rf{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.v-k4 .rf .ik{--ik:38px}
.v-k4 .rt h3{font-size:1.2rem}
.v-k4 .rt p{color:var(--c-ink-2);font-size:.95rem;margin:0 0 12px}
.v-k4 .ra{display:flex;justify-content:space-between;align-items:center}
""", render=_k4))


def _k5(c):
    el = _kel(c)
    s = "".join(f'<div class="sor" data-rv><div class="kep">{foto(c, e.get("foto"), "4/3")}</div><div class="szov">'
                f'<span class="n">{i + 1:02d}</span><div class="fej">{ik(e.get("ikon"))}<h3>{md(e.get("nev", ""))}</h3></div>'
                f'<p>{md(e.get("leiras", ""))}</p><p class="ar">{esc(e.get("ar", ""))}</p>{_link(e)}</div></div>' for i, e in enumerate(el))
    return (f'<section class="sec v-k5 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="sorok">{s}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k5", nev="Váltakozó sorok", leiras="Minden kategória egy teljes sor: nagy fotó és szöveg "
    "felváltva balra-jobbra, nagy kontúros sorszámmal. Mesélős, magazinos, prémium.", css=KIN_KOZOS + r"""
.v-k5 .sor{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(26px,5cqi,76px);align-items:center;margin-bottom:clamp(40px,6cqi,86px)}
.v-k5 .sor:last-child{margin-bottom:0}
.v-k5 .sor:nth-child(even) .kep{order:2}
.v-k5 .n{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(3.2rem,6cqi,5rem);line-height:.9;color:transparent;-webkit-text-stroke:1.5px var(--hl);margin-bottom:10px}
.v-k5 .fej{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.v-k5 .fej .ik{--ik:46px}
.v-k5 .szov h3{font-size:clamp(1.5rem,2.6cqi,2.2rem)}
.v-k5 .szov p{color:var(--c-ink-2);max-width:48ch}
.v-k5 .ar{font-family:var(--f-display);font-weight:var(--w-display);color:var(--c-head);font-size:1.25rem}
@container elo (max-width:820px){.v-k5 .sor{grid-template-columns:1fr}.v-k5 .sor:nth-child(even) .kep{order:0}}
""", render=_k5))


def _k6(c):
    el = _kel(c)
    tb = "".join(f'<button class="tb{" on" if i == 0 else ""}" type="button" data-tab="{i}">{ik(e.get("ikon"))}<span>{md(e.get("nev", ""))}</span></button>' for i, e in enumerate(el))
    pn = "".join(f'<div class="pane{" on" if i == 0 else ""}" data-tab="{i}"><div class="pk">{foto(c, e.get("foto"), "4/3")}</div>'
                 f'<div class="pt"><h3>{md(e.get("nev", ""))}</h3><p class="lead">{md(e.get("leiras", ""))}</p><p class="ar">{esc(e.get("ar", ""))}</p>'
                 f'{btn({"szoveg": e.get("link_szoveg", "Megnézem"), "href": e.get("link", "#")}) if e.get("link") else ""}</div></div>' for i, e in enumerate(el))
    return (f'<section class="sec v-k6 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="tabok" data-tabs><div class="tbs" role="tablist">{tb}</div><div class="panes" data-rv>{pn}</div></div></div></section>')


KINALAT.append(dict(id="k6", nev="Fülek (lapozós)", leiras="Kapszula-fülek ikonokkal; kattintásra vált a nagy fotós "
    "panel. Kevés helyen sokat mutat, interaktív.", css=KIN_KOZOS + r"""
.v-k6 .tbs{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-bottom:28px}
.v-k6 .tb{display:inline-flex;align-items:center;gap:10px;padding:8px 18px 8px 8px;border-radius:999px;border:2px solid var(--c-line2);background:var(--c-card);font-weight:800;cursor:pointer;color:var(--c-head);transition:all .2s var(--ease)}
.v-k6 .tb .ik{--ik:36px}
.v-k6 .tb.on{background:var(--c-primary);border-color:var(--c-primary);color:var(--c-on-primary);box-shadow:var(--sh-color)}
.v-k6 .pane{display:none;grid-template-columns:1.1fr .9fr;gap:clamp(24px,4cqi,60px);align-items:center;background:var(--c-card);border-radius:28px;padding:clamp(18px,2.6cqi,30px);box-shadow:var(--sh-2)}
.v-k6 .pane.on{display:grid;animation:k6be .45s var(--ease-out)}
@keyframes k6be{from{opacity:0;transform:translateY(12px)}}
.v-k6 .pt h3{font-size:clamp(1.6rem,3cqi,2.4rem)}
.v-k6 .pt .lead{margin:14px 0 16px}
.v-k6 .ar{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.3rem;color:var(--hl)}
@container elo (max-width:780px){.v-k6 .pane.on{grid-template-columns:1fr}}
""", render=_k6))


def _k7(c):
    el = _kel(c)
    k = "".join(f'<a class="ko" href="{esc(e.get("link", "#"))}" data-rv><div class="kk">{ph(c, e.get("foto"))}{ik(e.get("ikon"), "jel")}</div>'
                f'<h3>{md(e.get("nev", ""))}</h3><p>{esc(e.get("ar", ""))}</p></a>' for e in el)
    return (f'<section class="sec v-k7 s-paper tx" id="kinalat">{hat(c)}{dk(c, "kinalat")}<div class="wrap">{shead(c.get("kinalat"))}'
            f'<div class="korok" style="--n:{min(4, len(el) or 1)}">{k}</div>{_kin_lab(c)}</div></section>')


KINALAT.append(dict(id="k7", nev="Kerek fotók ikon-matricával", leiras="Nagy, kerek fotók fehér gyűrűvel, szélükön "
    "ikon-matrica, alatta név és ár. Egyszerű, barátságos, „válassz egyet”.", css=KIN_KOZOS + r"""
.v-k7 .korok{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:var(--gap);text-align:center}
.v-k7 .ko{text-decoration:none;color:inherit}
.v-k7 .kk{position:relative;width:min(100%,250px);aspect-ratio:1;margin:0 auto 20px;border-radius:50%;box-shadow:0 0 0 8px var(--c-card),var(--sh-3);transition:transform .45s var(--ease)}
.v-k7 .kk .ph{position:absolute;inset:0;aspect-ratio:auto;height:100%;border-radius:50%}
.v-k7 .kk .jel{position:absolute;right:2%;bottom:4%;--ik:64px;background-color:var(--c-card);border-radius:50%;padding:9px;background-origin:content-box;box-shadow:var(--sh-2)}
.v-k7 .ko:hover .kk{transform:rotate(-4deg) scale(1.03)}
.v-k7 .ko h3{font-size:1.3rem}
.v-k7 .ko p{margin:4px 0 0;color:var(--hl);font-weight:800}
@container elo (max-width:820px){.v-k7 .korok{grid-template-columns:1fr 1fr;row-gap:34px}}
""", render=_k7))

# ============================================================== AJÁNLAT (kiemelt tételek árakkal)
AJANLAT = []


def _ael(c, n=8):
    return (g(c, "ajanlat", "elemek") or [])[:n]


def _cimkek(e):
    return "".join(f'<span class="cimke">{esc(x)}</span>' for x in (e.get("cimkek") or []))


def _alab(c):
    a = c.get("ajanlat", {})
    lab = f'<p class="alab">{md(a["lab"])}</p>' if a.get("lab") else ""
    b = btn(a.get("cta"))
    return f'<div class="afoot">{lab}{b}</div>' if (lab or b) else ""


AJ_KOZOS = r"""
.afoot{display:flex;flex-direction:column;align-items:center;gap:18px;margin-top:clamp(26px,3.6cqi,44px);text-align:center}
.alab{margin:0;font-size:.9rem;color:var(--c-ink-3)}
.cimkek{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
"""


def _a1(c):
    t = "".join(f'<div class="tetel" data-rv><div class="sor"><h3>{md(e.get("nev", ""))}</h3><i></i><b>{esc(e.get("ar", ""))}</b></div>'
                f'<p>{md(e.get("leiras", ""))}</p><div class="cimkek">{_cimkek(e)}</div></div>' for e in _ael(c))
    return (f'<section class="sec v-a1 s-sand tx" id="etlap">{dk(c, "ajanlat")}<div class="wrap">{shead(c.get("ajanlat"))}'
            f'<div class="etlap s-vilagos"><div class="lap">{t}</div></div>{_alab(c)}</div></section>')


AJANLAT.append(dict(id="a1", nev="Étlap pontozott vonallal", leiras="Nyomtatott étlap-lap két hasábban: név, "
    "pontozott vezetővonal, ár, alatta a leírás és címkék. Klasszikus, azonnal érthető.", css=AJ_KOZOS + r"""
.v-a1 .etlap{background:var(--c-card);border:1px solid var(--c-line2);outline:1px solid var(--c-line2);outline-offset:-11px;border-radius:8px;padding:clamp(28px,4.8cqi,64px);box-shadow:var(--sh-2)}
.v-a1 .lap{columns:2;column-gap:60px}
.v-a1 .tetel{break-inside:avoid;margin-bottom:26px}
.v-a1 .sor{display:flex;align-items:baseline;gap:8px}
.v-a1 .sor h3{font-size:1.14rem}
.v-a1 .sor i{flex:1;border-bottom:2px dotted var(--c-line2);transform:translateY(-4px);min-width:20px}
.v-a1 .sor b{font-family:var(--f-display);font-weight:var(--w-display);color:var(--hl);white-space:nowrap;font-size:1.05rem}
.v-a1 .tetel p{margin:6px 0 0;font-size:.92rem;color:var(--c-ink-2)}
@container elo (max-width:760px){.v-a1 .lap{columns:1}}
""", render=_a1))


def _a2(c):
    k = "".join(f'<article class="krt" data-rv>{foto(c, e.get("foto"), "16/11", "krt-kep")}<span class="arc">{esc(e.get("ar", ""))}</span>'
                f'<h3 class="krt-h">{md(e.get("nev", ""))}</h3><p class="krt-p">{md(e.get("leiras", ""))}</p><div class="cimkek">{_cimkek(e)}</div></article>' for e in _ael(c))
    return (f'<section class="sec v-a2 s-white" id="etlap"><div class="wrap">{shead(c.get("ajanlat"), bal=True)}'
            f'<div class="rail-w" data-railw><div class="rail">{k}</div>{rail_nav()}</div>{_alab(c)}</div></section>')


AJANLAT.append(dict(id="a2", nev="Termékkártyák sínben", leiras="Fotós termékkártyák oldalra görgethető sínben, "
    "mindegyiken lógó árcédula. Webshopos, lendületes.", css=AJ_KOZOS + RAIL_CSS + r"""
.v-a2 .krt{height:100%}
.v-a2 .arc{position:absolute;right:14px;top:14px;z-index:4;background:var(--c-accent);color:var(--c-on-accent);font-weight:800;font-size:.92rem;padding:8px 14px 8px 22px;clip-path:polygon(12px 0,100% 0,100% 100%,12px 100%,0 50%);transform:rotate(4deg);box-shadow:var(--sh-2)}
""", render=_a2))


def _a3(c):
    el = _ael(c, 12)
    csop = []
    for e in el:
        cs = e.get("csoport", "Kínálat")
        if cs not in csop:
            csop.append(cs)
    tb = "".join(f'<button class="tb{" on" if i == 0 else ""}" type="button" data-tab="{i}">{esc(cs)}</button>' for i, cs in enumerate(csop))
    pn = ""
    for i, cs in enumerate(csop):
        t = "".join(f'<div class="tetel"><div class="sor"><h3>{md(e.get("nev", ""))}</h3><i></i><b>{esc(e.get("ar", ""))}</b></div>'
                    f'<p>{md(e.get("leiras", ""))}</p><div class="cimkek">{_cimkek(e)}</div></div>' for e in el if e.get("csoport", "Kínálat") == cs)
        pn += f'<div class="pane{" on" if i == 0 else ""}" data-tab="{i}">{t}</div>'
    return (f'<section class="sec v-a3 s-white" id="etlap"><div class="wrap">{shead(c.get("ajanlat"))}'
            f'<div class="tabok" data-tabs><div class="tbs">{tb}</div><div class="panes" data-rv>{pn}</div></div>{_alab(c)}</div></section>')


AJANLAT.append(dict(id="a3", nev="Csoportok fülekkel", leiras="Kategória-fülek (pl. Tészták, Rizottók…), alattuk "
    "tiszta árlista. Sok tételnél is áttekinthető.", css=AJ_KOZOS + r"""
.v-a3 .tbs{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-bottom:26px;padding:6px;background:var(--c-tint);border-radius:999px;width:max-content;max-width:100%;margin-inline:auto}
.v-a3 .tb{padding:10px 20px;border-radius:999px;border:0;background:transparent;font-weight:800;cursor:pointer;color:var(--c-ink-2)}
.v-a3 .tb.on{background:var(--c-card);color:var(--c-head);box-shadow:var(--sh-2)}
.v-a3 .pane{display:none;max-width:820px;margin:0 auto}
.v-a3 .pane.on{display:block;animation:a3be .4s var(--ease-out)}
@keyframes a3be{from{opacity:0;transform:translateY(10px)}}
.v-a3 .tetel{padding:18px 0;border-bottom:1px solid var(--c-line)}
.v-a3 .sor{display:flex;align-items:baseline;gap:8px}
.v-a3 .sor h3{font-size:1.14rem}
.v-a3 .sor i{flex:1;border-bottom:2px dotted var(--c-line2);transform:translateY(-4px)}
.v-a3 .sor b{font-family:var(--f-display);font-weight:var(--w-display);color:var(--hl);white-space:nowrap}
.v-a3 .tetel p{margin:6px 0 0;font-size:.93rem;color:var(--c-ink-2)}
""", render=_a3))


def _a4(c):
    el = _ael(c, 7)
    if not el:
        return ""
    e0 = el[0]
    f0 = (f'<article class="fo krt" data-rv>{foto(c, e0.get("foto"), "4/3", "krt-kep")}<div class="fk"><span class="cimke">Kiemelt</span>'
          f'<h3>{md(e0.get("nev", ""))}</h3><p>{md(e0.get("leiras", ""))}</p><div class="fa"><b>{esc(e0.get("ar", ""))}</b><div class="cimkek">{_cimkek(e0)}</div></div></div></article>')
    li = "".join(f'<li data-rv>{ph(c, e.get("foto"), "mini")}<div><h4>{md(e.get("nev", ""))}</h4><p>{md(e.get("leiras", ""))}</p></div><b>{esc(e.get("ar", ""))}</b></li>' for e in el[1:])
    return (f'<section class="sec v-a4 s-white" id="etlap"><div class="wrap">{shead(c.get("ajanlat"))}'
            f'<div class="grid">{f0}<ul class="lista">{li}</ul></div>{_alab(c)}</div></section>')


AJANLAT.append(dict(id="a4", nev="Kiemelt tétel + lista", leiras="Balra egy nagy kiemelt kedvenc fotóval és árral, "
    "jobbra a többi tétel kis kerek képpel. Irányítja a választást.", css=AJ_KOZOS + r"""
.v-a4 .grid{display:grid;grid-template-columns:1fr 1.05fr;gap:clamp(24px,4cqi,56px);align-items:start}
.v-a4 .fk h3{font-size:clamp(1.5rem,2.5cqi,2rem);margin:10px 0 8px}
.v-a4 .fa{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.v-a4 .fa b{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.7rem;color:var(--hl)}
.v-a4 .lista{display:grid;gap:4px}
.v-a4 .lista li{display:grid;grid-template-columns:64px 1fr auto;gap:16px;align-items:center;padding:14px 12px;border-radius:16px;transition:background .2s}
.v-a4 .lista li:hover{background:var(--c-tint)}
.v-a4 .mini{width:64px;height:64px;aspect-ratio:1;border-radius:50%;box-shadow:var(--sh-2)}
.v-a4 h4{font-size:1.05rem;margin-bottom:2px}
.v-a4 .lista p{margin:0;font-size:.86rem;color:var(--c-ink-2);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.v-a4 .lista b{font-family:var(--f-display);font-weight:var(--w-display);color:var(--c-head);white-space:nowrap}
@container elo (max-width:860px){.v-a4 .grid{grid-template-columns:1fr}}
""", render=_a4))


def _a5(c):
    k = "".join(f'<article class="krt" data-rv>{foto(c, e.get("foto"), "16/11", "krt-kep")}<span class="arc">{esc(e.get("ar", ""))}</span>'
                f'<h3 class="krt-h">{md(e.get("nev", ""))}</h3><p class="krt-p">{md(e.get("leiras", ""))}</p><div class="cimkek">{_cimkek(e)}</div></article>' for e in _ael(c, 6))
    return (f'<section class="sec v-a5 s-sand tx" id="etlap">{dk(c, "ajanlat")}<div class="wrap">{shead(c.get("ajanlat"))}'
            f'<div class="racs" style="--oszlop:3">{k}</div>{_alab(c)}</div></section>')


AJANLAT.append(dict(id="a5", nev="Árcédulás rács", leiras="Fotós kártyák rácsban, mindegyik sarkán lógó, megdöntött "
    "árcédula. Piaci, kézzelfogható, jól szkennelhető.", css=AJ_KOZOS + r"""
.v-a5 .arc{position:absolute;right:14px;top:14px;z-index:4;background:var(--c-accent);color:var(--c-on-accent);font-weight:800;font-size:.95rem;padding:9px 15px 9px 24px;clip-path:polygon(13px 0,100% 0,100% 100%,13px 100%,0 50%);transform:rotate(5deg);box-shadow:var(--sh-2)}
.v-a5 .arc::before{content:"";position:absolute;left:9px;top:50%;width:6px;height:6px;margin-top:-3px;border-radius:50%;background:var(--c-card)}
""", render=_a5))


def _a6(c):
    t = "".join(f'<div class="tetel" data-rv><div class="sor"><h3>{md(e.get("nev", ""))}</h3><i></i><b>{esc(e.get("ar", ""))}</b></div>'
                f'<p>{md(e.get("leiras", ""))}</p></div>' for e in _ael(c))
    a = c.get("ajanlat", {})
    return (f'<section class="sec v-a6 s-paper" id="etlap"><div class="wrap"><div class="tabla s-deep">'
            f'{shead(a)}<div class="lap">{t}</div>{_alab(c)}</div></div></section>')


AJANLAT.append(dict(id="a6", nev="Krétatábla-étlap", leiras="Sötét, fakeretes krétatábla kézírásos címekkel és "
    "pontozott árlistával. Bisztró-hangulat, nagyon karakteres.", css=AJ_KOZOS + r"""
.v-a6 .tabla{position:relative;background:var(--c-deep);border-radius:14px;padding:clamp(30px,5cqi,70px);border:16px solid color-mix(in srgb,var(--c-accent) 45%,#5b3f28);box-shadow:var(--sh-3),inset 0 0 80px rgba(0,0,0,.4)}
.v-a6 .tabla::before{content:"";position:absolute;inset:0;background-image:var(--zaj);opacity:.55;mix-blend-mode:screen;pointer-events:none}
.v-a6 .shead .cim,.v-a6 .tetel h3{font-family:var(--f-hand);font-weight:700;letter-spacing:0;text-transform:none}
.v-a6 .shead .cim{font-size:calc(var(--fs-hand)*var(--t-h2))}
.v-a6 .lap{columns:2;column-gap:64px;position:relative}
.v-a6 .tetel{break-inside:avoid;margin-bottom:24px}
.v-a6 .sor{display:flex;align-items:baseline;gap:8px}
.v-a6 .tetel h3{font-size:calc(var(--fs-hand)*1.28rem)}
.v-a6 .sor i{flex:1;border-bottom:2px dotted var(--c-line2);transform:translateY(-5px)}
.v-a6 .sor b{font-family:var(--f-hand);font-size:calc(var(--fs-hand)*1.25rem);color:var(--c-deep-hl);white-space:nowrap}
.v-a6 .tetel p{margin:4px 0 0;font-size:.92rem;color:var(--c-on-deep-2)}
@container elo (max-width:760px){.v-a6 .lap{columns:1}.v-a6 .tabla{border-width:10px}}
""", render=_a6))
