# -*- coding: utf-8 -*-
"""SZEKCIÓ-VÁLTOZATOK, 2. rész: folyamat, történet, galéria, látogatás/kapcsolat, lábléc."""
import datetime
from .alap import esc, md, sima, g, ui
from .kozos import (kick, shead, btn, gombsor, foto, ph, ik, logo, dk, hat, chips, nyitvatartas, nyitva_cim, fo_kapcs, adatok, social,
                    navlinkek, statok, kezi, uid)


def F(lst, i):
    return lst[i % len(lst)] if lst else None


# ============================================================== FOLYAMAT
FOLYAMAT = []


def _lep(c):
    return (g(c, "folyamat", "lepesek") or [])[:5]


def _f1(c):
    l = _lep(c)
    li = "".join(f'<li class="krt" data-rv><span class="no">{i + 1}</span>{ik(e.get("ikon"))}<h3 class="krt-h">{md(e.get("cim", ""))}</h3>'
                 f'<p class="krt-p">{md(e.get("szoveg", ""))}</p></li>' for i, e in enumerate(l))
    return (f'<section class="sec v-f1 s-tint tx" id="folyamat">{hat(c, masod=True)}{dk(c, "folyamat")}<div class="wrap">'
            f'{shead(c.get("folyamat"))}<ol class="ut" style="--n:{len(l) or 1}">{li}</ol></div></section>')


FOLYAMAT.append(dict(id="f1", nev="Pontozott útvonal", leiras="Lépés-kártyák egy szaggatott útvonalon, mindegyik "
    "tetején számozott pecsét. Egyértelmű, barátságos, „ilyen egyszerű”.", css=r"""
.v-f1 .ut{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:var(--gap);position:relative;margin:0;padding:0;list-style:none}
.v-f1 .ut::before{content:"";position:absolute;left:10%;right:10%;top:52px;border-top:3px dashed color-mix(in srgb,var(--c-accent) 62%,transparent);z-index:0}
.v-f1 .ut li{text-align:center;align-items:center;z-index:1}
.v-f1 .no{width:46px;height:46px;border-radius:50%;background:var(--c-accent);color:var(--c-on-accent);display:grid;place-items:center;font-family:var(--f-display);font-weight:var(--w-display);font-size:1.2rem;box-shadow:0 0 0 5px var(--c-card),0 0 0 7px color-mix(in srgb,var(--c-accent) 35%,transparent);flex:none}
.v-f1 .ik{--ik:64px}
@container elo (max-width:860px){.v-f1 .ut{grid-template-columns:1fr 1fr}.v-f1 .ut::before{display:none}}
@container elo (max-width:520px){.v-f1 .ut{grid-template-columns:1fr}}
""", render=_f1))


def _f2(c):
    l = _lep(c)
    li = "".join(f'<li data-rv><div class="pont">{ik(e.get("ikon"))}</div><div class="doboz"><span class="mono lep">{i + 1}. lépés</span>'
                 f'<h3>{md(e.get("cim", ""))}</h3><p>{md(e.get("szoveg", ""))}</p></div></li>' for i, e in enumerate(l))
    return (f'<section class="sec v-f2 s-tint tx" id="folyamat">{hat(c, masod=True)}{dk(c, "folyamat")}<div class="wrap">'
            f'{shead(c.get("folyamat"))}<ol class="tl">{li}</ol></div></section>')


FOLYAMAT.append(dict(id="f2", nev="Cikcakk idővonal", leiras="Függőleges, szaggatott idővonal; a lépések felváltva "
    "balra és jobbra ülnek, középen ikonos pontokkal. Mesélős, „a tészta útja”.", css=r"""
.v-f2 .tl{position:relative;max-width:940px;margin:0 auto;padding:0;list-style:none}
.v-f2 .tl::before{content:"";position:absolute;left:50%;top:10px;bottom:10px;width:3px;margin-left:-1.5px;background:repeating-linear-gradient(180deg,var(--hl) 0 9px,transparent 9px 18px)}
.v-f2 li{display:grid;grid-template-columns:1fr 104px 1fr;align-items:center;margin-bottom:22px}
.v-f2 .pont{grid-column:2;grid-row:1;width:82px;height:82px;border-radius:50%;background:var(--c-card);box-shadow:var(--sh-2),0 0 0 6px var(--sec-bg);display:grid;place-items:center;margin:0 auto;position:relative;z-index:1}
.v-f2 .pont .ik{--ik:54px}
.v-f2 .doboz{grid-column:1;grid-row:1;text-align:right;background:var(--c-card);border-radius:20px;padding:20px 24px;box-shadow:var(--sh-1)}
.v-f2 li:nth-child(even) .doboz{grid-column:3;text-align:left}
.v-f2 .lep{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--hl)}
.v-f2 h3{font-size:1.2rem;margin:4px 0 6px}
.v-f2 .doboz p{margin:0;color:var(--c-ink-2);font-size:.95rem}
@container elo (max-width:720px){.v-f2 .tl::before{left:41px}.v-f2 li{grid-template-columns:82px 1fr;gap:16px}.v-f2 .pont{grid-column:1}.v-f2 .doboz,.v-f2 li:nth-child(even) .doboz{grid-column:2;text-align:left}}
""", render=_f2))


def _f3(c):
    l = _lep(c)
    d = "".join(f'<div class="ns" data-rv><b>{i + 1:02d}</b><div class="fej">{ik(e.get("ikon"))}<h3>{md(e.get("cim", ""))}</h3></div>'
                f'<p>{md(e.get("szoveg", ""))}</p></div>' for i, e in enumerate(l))
    return (f'<section class="sec v-f3 s-white" id="folyamat">{hat(c, masod=True)}<div class="wrap">{shead(c.get("folyamat"), bal=True)}'
            f'<div class="nagy" style="--n:{len(l) or 1}">{d}</div></div></section>')


FOLYAMAT.append(dict(id="f3", nev="Óriás sorszámok", leiras="Hatalmas, kontúros sorszámok vastag vonal alatt, mellettük "
    "ikon és rövid szöveg. Szerkesztőségi, magabiztos, sok levegővel.", css=r"""
.v-f3 .nagy{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:clamp(18px,3cqi,40px)}
.v-f3 .ns{border-top:3px solid var(--c-head);padding-top:18px}
.v-f3 .ns b{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(3.6rem,8cqi,7rem);line-height:.82;color:transparent;-webkit-text-stroke:2px var(--hl);margin-bottom:16px}
.v-f3 .fej{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.v-f3 .fej .ik{--ik:40px}
.v-f3 h3{font-size:1.18rem}
.v-f3 .ns p{margin:0;color:var(--c-ink-2);font-size:.95rem}
@container elo (max-width:860px){.v-f3 .nagy{grid-template-columns:1fr 1fr;row-gap:34px}}
@container elo (max-width:520px){.v-f3 .nagy{grid-template-columns:1fr}}
""", render=_f3))


def _f4(c):
    l = _lep(c)
    n = len(l) or 1
    d = "".join(f'<div class="lp krt" style="--h:{i}" data-rv><div class="krt-fej">{ik(e.get("ikon"))}<h3 class="krt-h">{md(e.get("cim", ""))}</h3></div>'
                f'<p class="krt-p">{md(e.get("szoveg", ""))}</p><span class="fok mono">{i + 1}/{n}</span></div>' for i, e in enumerate(l))
    return (f'<section class="sec v-f4 s-tint tx" id="folyamat">{hat(c, masod=True)}{dk(c, "folyamat")}<div class="wrap">'
            f'{shead(c.get("folyamat"))}<div class="lepcso" style="--n:{n}">{d}</div></div></section>')


FOLYAMAT.append(dict(id="f4", nev="Felfelé lépcső", leiras="A lépés-kártyák lépcsőzetesen emelkednek balról jobbra, "
    "mintha felfelé vinnének. Fejlődés, haladás érzete.", css=r"""
.v-f4 .lepcso{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:var(--gap);align-items:end;position:relative;padding-bottom:6px}
.v-f4 .lepcso::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--c-line2);border-radius:3px}
.v-f4 .lp{margin-bottom:calc(var(--h)*38px + 18px)}
.v-f4 .fok{margin-top:auto;padding-top:8px;font-size:.72rem;color:var(--c-ink-3);letter-spacing:.14em}
@container elo (max-width:860px){.v-f4 .lepcso{grid-template-columns:1fr 1fr}.v-f4 .lp{margin-bottom:18px}}
@container elo (max-width:520px){.v-f4 .lepcso{grid-template-columns:1fr}}
""", render=_f4))


def _f5(c):
    l = _lep(c)
    n = len(l) or 1
    st = "".join(f'<div class="st" data-rv><div class="bic">{ik(e.get("ikon"))}</div><h3>{md(e.get("cim", ""))}</h3><p>{md(e.get("szoveg", ""))}</p></div>' for e in l)
    gorgo = "<i></i>" * (n * 3)
    return (f'<section class="sec v-f5 s-white" id="folyamat">{hat(c, masod=True)}<div class="wrap">{shead(c.get("folyamat"))}'
            f'<div class="belt" style="--n:{n}"><div class="allomas">{st}</div><div class="track anim"></div>'
            f'<div class="gorgok">{gorgo}</div></div></div></section>')


FOLYAMAT.append(dict(id="f5", nev="Futószalag", leiras="Egy mozgó futószalag állomásokkal: minden lépés egy ikonos "
    "állomás a szalag felett. Játékos, „gyártósor” metafora, jól mutatja a folyamatot.", css=r"""
.v-f5 .belt{position:relative;padding-top:10px}
.v-f5 .allomas{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:18px;margin-bottom:34px;text-align:center}
.v-f5 .st{position:relative}
.v-f5 .bic{width:96px;height:96px;margin:0 auto 14px;border-radius:26px;background:var(--c-tint);display:grid;place-items:center;box-shadow:var(--sh-2);position:relative}
.v-f5 .bic::after{content:"";position:absolute;left:50%;bottom:-30px;width:2px;height:24px;background:repeating-linear-gradient(180deg,var(--c-ink-3) 0 4px,transparent 4px 8px)}
.v-f5 .bic .ik{--ik:62px}
.v-f5 h3{font-size:1.1rem;margin-bottom:6px}
.v-f5 .st p{margin:0 auto;color:var(--c-ink-2);font-size:.92rem;max-width:26ch}
.v-f5 .track{height:26px;border-radius:13px;background-color:var(--c-ink);background-image:repeating-linear-gradient(115deg,rgba(255,255,255,.16) 0 8px,transparent 8px 20px);animation:f5fut 1.4s linear infinite;box-shadow:var(--sh-2)}
.v-f5 .gorgok{display:flex;justify-content:space-between;padding:0 8px;margin-top:-6px}
.v-f5 .gorgok i{width:16px;height:16px;border-radius:50%;background:var(--c-primary);box-shadow:inset 0 0 0 3px rgba(255,255,255,.7);display:block}
@keyframes f5fut{to{background-position:44px 0}}
@container elo (max-width:760px){.v-f5 .allomas{grid-template-columns:1fr 1fr;row-gap:40px}.v-f5 .bic::after{display:none}}
""", render=_f5))

# ============================================================== TÖRTÉNET
TORTENET = []


def _ps(t, n=None):
    return "".join(f"<p>{md(p)}</p>" for p in (t.get("bekezdesek") or [])[:n])


def _alair(t, cls="alair"):
    a = t.get("alairas") or {}
    if not a:
        return ""
    return f'<div class="{cls}"><span class="kezi nev">{esc(a.get("nev", ""))}</span><span class="mono szerep">{esc(a.get("szerep", ""))}</span></div>'


def _t1(c):
    t = c.get("tortenet", {})
    f = t.get("fotok") or []
    q = f'<blockquote>{md(t["idezet"])}</blockquote>' if t.get("idezet") else ""
    return (f'<section class="sec v-t1 s-paper tx" id="rolunk">{dk(c, "tortenet")}<div class="wrap grid">'
            f'<div class="kep" data-rv>{foto(c, F(f, 0), "4/5", felirat=t.get("foto_felirat"))}</div>'
            f'<div class="szov bal" data-rv>{kick(t.get("kicker"))}<h2 class="cim">{md(t.get("cim", ""))}</h2>{_ps(t)}{q}{_alair(t)}</div></div></section>')


TORTENET.append(dict(id="t1", nev="Fotó + személyes levél", leiras="Nagy portré vagy hangulatfotó, mellette a "
    "történet, egy kiemelt idézet és kézírásos aláírás. Őszinte, személyes, bizalmat épít.", css=r"""
.v-t1 .grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(30px,5.4cqi,84px);align-items:center}
.v-t1 .cim{margin-bottom:22px}
.v-t1 .szov p{font-size:1.04rem}
.v-t1 blockquote{margin:26px 0;padding:6px 0 6px 20px;border-left:4px solid var(--c-accent);font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,1.9cqi,1.45rem);line-height:1.3;color:var(--c-head)}
.v-t1 .alair{display:flex;flex-direction:column;gap:2px;margin-top:22px}
.v-t1 .alair .nev{font-size:calc(var(--fs-hand)*1.9rem);line-height:1}
.v-t1 .szerep{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
@container elo (max-width:860px){.v-t1 .grid{grid-template-columns:1fr}.v-t1 .kep{max-width:460px}}
""", render=_t1))


def _t2(c):
    t = c.get("tortenet", {})
    f = t.get("fotok") or []
    fc = t.get("fotok_felirat") or []
    p = "".join(f'<div class="pw p{i}">{foto(c, F(f, i), "4/5", felirat=(fc[i] if i < len(fc) else None))}</div>' for i in range(min(3, max(1, len(f)))))
    return (f'<section class="sec v-t2 s-paper tx" id="rolunk">{dk(c, "tortenet")}<div class="wrap grid">'
            f'<div class="szov bal" data-rv>{kick(t.get("kicker"))}<h2 class="cim">{md(t.get("cim", ""))}</h2>{_ps(t)}{_alair(t)}</div>'
            f'<div class="polak" data-rv>{p}</div></div></section>')


TORTENET.append(dict(id="t2", nev="Szórt fotókollázs", leiras="Balra a történet, jobbra három egymásra dobott, "
    "feliratos fotó. Emlékalbumos, családias, meleg.", css=r"""
.v-t2 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5cqi,80px);align-items:center}
.v-t2 .cim{margin-bottom:20px}
.v-t2 .alair{display:flex;flex-direction:column;margin-top:18px}.v-t2 .alair .nev{font-size:calc(var(--fs-hand)*1.8rem);line-height:1}
.v-t2 .szerep{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
.v-t2 .polak{position:relative;min-height:clamp(380px,46cqi,560px)}
.v-t2 .pw{position:absolute;width:52%}
.v-t2 .p0{left:0;top:2%;transform:rotate(-5deg);z-index:1}
.v-t2 .p1{right:0;top:10%;transform:rotate(4deg);z-index:2}
.v-t2 .p2{left:22%;bottom:0;transform:rotate(-1deg);z-index:3}
@container elo (max-width:860px){.v-t2 .grid{grid-template-columns:1fr}.v-t2 .polak{min-height:clamp(320px,90cqi,520px)}}
""", render=_t2))


def _t3(c):
    t = c.get("tortenet", {})
    f = t.get("fotok") or []
    mk = t.get("merfoldkovek") or []
    li = "".join(f'<li data-rv><b class="ev">{esc(a)}</b><i></i><p>{md(b)}</p></li>' for a, b in mk)
    return (f'<section class="sec v-t3 s-white" id="rolunk"><div class="wrap">{shead(t, bal=True)}'
            f'<div class="t3g"><div class="szov" data-rv>{_ps(t)}{_alair(t)}</div><div class="kep" data-rv>{foto(c, F(f, 0), "16/10")}</div></div>'
            f'<ol class="mk" style="--n:{len(mk) or 1}">{li}</ol></div></section>')


TORTENET.append(dict(id="t3", nev="Mérföldkő-idővonal", leiras="Rövid történet fotóval, alatta vízszintes idővonal a "
    "fontos dátumokkal és tényekkel. Tárgyilagos, hiteles, „így jutottunk ide”.", css=r"""
.v-t3 .t3g{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(26px,4.4cqi,64px);align-items:center}
.v-t3 .alair{margin-top:14px;display:flex;flex-direction:column}.v-t3 .alair .nev{font-size:calc(var(--fs-hand)*1.6rem);line-height:1}
.v-t3 .szerep{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
.v-t3 .mk{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:20px;position:relative;margin:clamp(40px,5cqi,64px) 0 0;padding:0;list-style:none}
.v-t3 .mk::before{content:"";position:absolute;left:0;right:0;top:50px;height:2px;background:var(--c-line2)}
.v-t3 .ev{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.15rem,2cqi,1.5rem);color:var(--hl);min-height:40px;line-height:1.15}
.v-t3 .mk i{display:block;width:18px;height:18px;border-radius:50%;background:var(--c-accent);box-shadow:0 0 0 6px var(--sec-bg);margin:0 0 14px;position:relative}
.v-t3 .mk p{margin:0;color:var(--c-ink-2);font-size:.95rem}
@container elo (max-width:820px){.v-t3 .t3g{grid-template-columns:1fr}.v-t3 .mk{grid-template-columns:1fr;gap:10px}.v-t3 .mk::before{display:none}}
""", render=_t3))


def _t4(c):
    t = c.get("tortenet", {})
    f = t.get("fotok") or []
    a = t.get("alairas") or {}
    return (f'<section class="sec v-t4 s-tint tx" id="rolunk">{dk(c, "tortenet")}<div class="wrap szuk">'
            f'<figure class="q" data-rv><span class="qm" aria-hidden="true">„</span><blockquote>{md(t.get("idezet", ""))}</blockquote>'
            f'<figcaption class="ki">{ph(c, F(f, 0), "port")}<div><b>{esc(a.get("nev", ""))}</b><span>{esc(a.get("szerep", ""))}</span></div></figcaption></figure>'
            f'<div class="ps2" data-rv>{kick(t.get("kicker"))}<h2 class="cim">{md(t.get("cim", ""))}</h2><div class="cols">{_ps(t)}</div></div></div></section>')


TORTENET.append(dict(id="t4", nev="Nagy idézet", leiras="Óriás idézőjel és egy nagy, kiemelt mondat a tulajdonostól, "
    "kerek portréval; alatta két hasábban a történet. Erős, emberi, emlékezetes.", css=r"""
.v-t4 .q{text-align:center;margin:0 auto clamp(40px,5cqi,70px);max-width:820px}
.v-t4 .qm{display:block;font-family:var(--f-display);font-size:clamp(6rem,12cqi,10rem);line-height:1;height:.92em;margin:-.34em 0 0;color:var(--hl)}
.v-t4 blockquote{margin:0;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.6rem,3.3cqi,2.7rem);line-height:1.2;color:var(--c-head);text-wrap:balance}
.v-t4 .ki{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:26px;text-align:left}
.v-t4 .port{width:66px;height:66px;aspect-ratio:1;border-radius:50%;box-shadow:0 0 0 4px var(--c-card),var(--sh-2)}
.v-t4 .ki b{display:block;font-size:1.02rem}.v-t4 .ki span{font-size:.86rem;color:var(--c-ink-2)}
.v-t4 .ps2 .cim{margin-bottom:18px}
.v-t4 .cols{columns:2;column-gap:44px}
.v-t4 .cols p{break-inside:avoid}
@container elo (max-width:720px){.v-t4 .cols{columns:1}}
""", render=_t4))


def _t5(c):
    t = c.get("tortenet", {})
    f = t.get("fotok") or []
    return (f'<section class="sec v-t5 s-sand tx" id="rolunk">{dk(c, "tortenet")}<div class="wrap"><div class="level s-vilagos" data-rv>'
            f'<i class="tape t1"></i><i class="tape t2"></i><div class="lkep">{foto(c, F(f, 0), "4/5", felirat=t.get("foto_felirat"))}</div>'
            f'<div class="lszov">{kick(t.get("kicker"))}<h2 class="cim">{md(t.get("cim", ""))}</h2>{_ps(t)}{_alair(t)}</div></div></div></section>')


TORTENET.append(dict(id="t5", nev="Levélpapír", leiras="A történet egy vonalas levélpapíron, ragasztószalaggal "
    "felragasztott fotóval és aláírással. Kézzel írt levél hatás, nagyon személyes.", css=r"""
.v-t5 .level{position:relative;max-width:1020px;margin:0 auto;background-color:var(--c-card);background-image:repeating-linear-gradient(180deg,transparent 0 31px,color-mix(in srgb,var(--c-primary) 9%,transparent) 31px 32px);border-radius:4px;box-shadow:var(--sh-3);padding:clamp(34px,5cqi,64px) clamp(26px,5cqi,64px) clamp(34px,5cqi,64px) clamp(40px,7cqi,96px);display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(24px,4cqi,52px);transform:rotate(-.5deg)}
.v-t5 .level::before{content:"";position:absolute;left:clamp(22px,4cqi,60px);top:0;bottom:0;width:2px;background:color-mix(in srgb,var(--c-accent) 50%,transparent)}
.v-t5 .tape{position:absolute;display:block;width:128px;height:34px;background:color-mix(in srgb,var(--c-accent) 40%,rgba(255,255,255,.4));opacity:.9;z-index:3}
.v-t5 .t1{left:9%;top:-14px;transform:rotate(-7deg)}.v-t5 .t2{right:8%;top:-12px;transform:rotate(5deg)}
.v-t5 .lkep{transform:rotate(-2.5deg)}
.v-t5 .cim{margin-bottom:18px}
.v-t5 .lszov p{line-height:32px;margin-bottom:0}
.v-t5 .alair{margin-top:18px;display:flex;flex-direction:column}.v-t5 .alair .nev{font-size:calc(var(--fs-hand)*2rem);line-height:1}
.v-t5 .szerep{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3)}
@container elo (max-width:820px){.v-t5 .level{grid-template-columns:1fr;transform:none}.v-t5 .lkep{max-width:380px}}
""", render=_t5))

# ============================================================== GALÉRIA
GALERIA = []


def _gf(c):
    return g(c, "galeria", "fotok") or []


def _g1(c):
    f = _gf(c)[:6]
    d = "".join(f'<div class="mz m{i}" data-rv>{foto(c, x.get("id"), "auto", felirat=None)}<span class="fc">{esc(x.get("felirat", ""))}</span></div>' for i, x in enumerate(f))
    return (f'<section class="sec v-g1 s-white" id="galeria"><div class="wrap">{shead(c.get("galeria"))}'
            f'<div class="moz">{d}</div></div></section>')


GALERIA.append(dict(id="g1", nev="Mozaik-rács", leiras="Különböző méretű fotók szoros mozaikban, rámutatva "
    "felirattal. Gazdag, rendezett, „nézz körül”.", css=r"""
.v-g1 .moz{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:clamp(120px,15cqi,200px);gap:14px}
.v-g1 .mz{position:relative}
.v-g1 .m0{grid-column:span 2;grid-row:span 2}.v-g1 .m3,.v-g1 .m4,.v-g1 .m5{grid-column:span 2}
.v-g1 .mz .ft{height:100%}
.v-g1 .mz .ph{aspect-ratio:auto;height:100%}
.v-g1 .fc{position:absolute;left:12px;bottom:12px;z-index:3;background:var(--c0-card);color:var(--c0-head);font-weight:700;font-size:.82rem;padding:6px 12px;border-radius:999px;opacity:0;transform:translateY(6px);transition:all .25s var(--ease)}
.v-g1 .mz:hover .fc{opacity:1;transform:none}
.v-g1 .fc:empty{display:none}
@container elo (max-width:700px){.v-g1 .moz{grid-template-columns:1fr 1fr}.v-g1 .m0{grid-column:span 2;grid-row:span 1}.v-g1 .m3,.v-g1 .m4{grid-column:span 1}}
""", render=_g1))


def _g2(c):
    f = _gf(c)[:6]
    d = "".join(f'<div class="sz" data-rv>{foto(c, x.get("id"), "4/5", felirat=x.get("felirat"))}</div>' for x in f)
    return (f'<section class="sec v-g2 s-sand tx" id="galeria">{dk(c, "galeria")}<div class="wrap">{shead(c.get("galeria"))}'
            f'<div class="szort">{d}</div></div></section>')


GALERIA.append(dict(id="g2", nev="Asztalra szórt fotók", leiras="Kicsit ferdén, egymásra csúszva szórt fotók; "
    "rámutatva kiegyenesednek és előrejönnek. Játékos, emlékalbumos.", css=r"""
.v-g2 .szort{display:flex;flex-wrap:wrap;justify-content:center;gap:0;padding:10px 0}
.v-g2 .sz{width:clamp(170px,23cqi,270px);margin:-8px -10px;transition:transform .35s var(--ease),z-index 0s}
.v-g2 .sz:nth-child(1){transform:rotate(-6deg)}.v-g2 .sz:nth-child(2){transform:rotate(4deg) translateY(18px)}
.v-g2 .sz:nth-child(3){transform:rotate(-2deg)}.v-g2 .sz:nth-child(4){transform:rotate(6deg) translateY(10px)}
.v-g2 .sz:nth-child(5){transform:rotate(-4deg) translateY(22px)}.v-g2 .sz:nth-child(6){transform:rotate(3deg)}
.v-g2 .sz:hover{transform:rotate(0) scale(1.06);z-index:5}
""", render=_g2))


def _g3(c):
    f = _gf(c)[:6]
    if not f:
        return ""
    big = ph(c, f[0].get("id"), "nagy")
    th = "".join(f'<button type="button" class="th{" on" if i == 0 else ""}" data-gal="f-{esc(x.get("id"))}" data-fc="{esc(x.get("felirat", ""))}">{ph(c, x.get("id"))}</button>' for i, x in enumerate(f))
    return (f'<section class="sec v-g3 s-white" id="galeria"><div class="wrap">{shead(c.get("galeria"))}'
            f'<div class="nagyw" data-galw data-rv>{big}<span class="fc">{esc(f[0].get("felirat", ""))}</span></div><div class="thumbs">{th}</div></div></section>')


GALERIA.append(dict(id="g3", nev="Nagy kép + bélyegképek", leiras="Egy nagy, széles fotó, alatta kattintható "
    "bélyegképek. Egyszerre mutat sokat és semmi nem zsúfolt.", css=r"""
.v-g3 .nagyw{position:relative;border-radius:var(--r);overflow:hidden;box-shadow:var(--sh-3)}
.v-g3 .nagy{aspect-ratio:16/8;transition:opacity .3s}
.v-g3 .fc{position:absolute;left:18px;bottom:18px;background:var(--c0-card);color:var(--c0-head);font-weight:700;font-size:.9rem;padding:8px 14px;border-radius:999px}
.v-g3 .fc:empty{display:none}
.v-g3 .thumbs{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:14px}
.v-g3 .th{padding:0;border:3px solid transparent;border-radius:14px;overflow:hidden;cursor:pointer;background:none;transition:border-color .2s,transform .2s}
.v-g3 .th .ph{aspect-ratio:1}
.v-g3 .th.on{border-color:var(--c-primary)}.v-g3 .th:hover{transform:translateY(-3px)}
@container elo (max-width:600px){.v-g3 .thumbs{grid-template-columns:repeat(3,1fr)}.v-g3 .nagy{aspect-ratio:4/3}}
""", render=_g3))


def _g4(c):
    f = _gf(c)
    d = "".join(f'<div class="gi">{foto(c, x.get("id"), "4/3", felirat=x.get("felirat"))}</div>' for x in f) * 2
    return (f'<section class="sec v-g4 s-paper" id="galeria"><div class="wrap">{shead(c.get("galeria"))}</div>'
            f'<div class="sav-w"><div class="sav anim">{d}</div></div></section>')


GALERIA.append(dict(id="g4", nev="Végtelen fotósáv", leiras="A fotók lassan, végtelenítve úsznak a képernyőn "
    "keresztül. Élő, pörgős hangulat, kevés szöveggel.", css=r"""
.v-g4 .sav-w{overflow:hidden;padding:14px 0 10px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.v-g4 .sav{display:flex;width:max-content;animation:g4fut 60s linear infinite}
.v-g4 .sav:hover{animation-play-state:paused}
.v-g4 .gi{width:clamp(220px,26cqi,330px);margin-right:20px;flex:none}
@keyframes g4fut{to{transform:translateX(-50%)}}
""", render=_g4))


def _g5(c):
    f = _gf(c)[:4]
    d = "".join(f'<figure class="iv" data-rv>{ph(c, x.get("id"))}<figcaption class="kezi">{esc(x.get("felirat", ""))}</figcaption></figure>' for x in f)
    return (f'<section class="sec v-g5 s-white" id="galeria"><div class="wrap">{shead(c.get("galeria"))}'
            f'<div class="ivek" style="--n:{len(f) or 1}">{d}</div></div></section>')


GALERIA.append(dict(id="g5", nev="Boltíves ablaksor", leiras="Egymás mellett álló, magas boltíves „ablakok” a "
    "fotókkal, alattuk kézírásos felirat. Mediterrán, elegáns, nyugodt.", css=r"""
.v-g5 .ivek{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:clamp(14px,2.4cqi,28px);margin:0}
.v-g5 .iv{margin:0;text-align:center}
.v-g5 .iv .ph{aspect-ratio:3/4.4;border-radius:999px 999px 18px 18px;box-shadow:var(--sh-3)}
.v-g5 .iv:nth-child(even){margin-top:40px}
.v-g5 figcaption{margin-top:12px;font-size:calc(var(--fs-hand)*1.15rem)}
@container elo (max-width:700px){.v-g5 .ivek{grid-template-columns:1fr 1fr}.v-g5 .iv:nth-child(even){margin-top:24px}}
""", render=_g5))

# ============================================================== LÁTOGATÁS / KAPCSOLAT
LATOGATAS = []


def _nyitva_jelzo(c):
    return '<span class="nyitva" data-nyitva hidden></span>' if g(c, "kapcsolat", "nyitva_gep") else ""


def _l1(c):
    l = c.get("latogatas", {})
    return (f'<section class="sec v-l1 s-primary tx" id="kapcsolat">{hat(c)}{dk(c, "latogatas", matrica=True)}<div class="wrap grid">'
            f'<div class="bal" data-rv>{kick(l.get("kicker"))}<h2 class="cim">{md(l.get("cim", ""))}</h2>'
            + (f'<p class="lead">{md(l["lead"])}</p>' if l.get("lead") else "") + gombsor(l)
            + f'</div><div class="nyk s-vilagos" data-rv><h3>{ui("ora")} {esc(nyitva_cim(c))} {_nyitva_jelzo(c)}</h3>{nyitvatartas(c)}{adatok(c)}</div></div></section>')


LAT_KOZOS = r"""
.nyt{display:grid;gap:0;margin:0}
.nyt li{display:flex;justify-content:space-between;gap:16px;padding:11px 0;border-bottom:1px dashed var(--c-line2);font-size:.98rem}
.nyt li:last-child{border-bottom:0}
.nyt b{font-weight:800;color:var(--c-head);white-space:nowrap}
.adat{display:grid;gap:10px;margin-top:18px}
.adat a{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;color:var(--c-ink)}
.adat a .ui{color:var(--hl);flex:none}
.adat a:hover span{text-decoration:underline}
.nyitva{display:inline-flex;align-items:center;gap:6px;margin-left:auto;font-family:var(--f-body);font-size:.74rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:4px 10px;border-radius:999px;background:#e6f6ec;color:#17693a}
.nyitva.zarva{background:#fbeaea;color:#9b2c2c}
.nyitva::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}
"""

LATOGATAS.append(dict(id="l1", nev="Színes sáv + nyitvatartás-kártya", leiras="Telt márkaszínű blokk nagy "
    "meghívással és gombokkal, mellette tiszta nyitvatartás-kártya élő „most nyitva” jelzéssel.", css=LAT_KOZOS + r"""
.v-l1 .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5cqi,80px);align-items:center}
.v-l1 .lead{margin:18px 0 28px}
.v-l1 .nyk{background:var(--c0-card);border-radius:26px;padding:clamp(22px,3cqi,36px);box-shadow:var(--sh-3)}
.v-l1 .nyk h3{display:flex;align-items:center;gap:10px;font-size:1.3rem;margin-bottom:12px}
.v-l1 .nyk h3 .ui{color:var(--hl)}
@container elo (max-width:860px){.v-l1 .grid{grid-template-columns:1fr}}
""", render=_l1))


def _l2(c):
    l = c.get("latogatas", {})
    k = c.get("kapcsolat", {})
    ch = []
    if k.get("nyitva_rovid"):
        ch.append({"ikon": "ora", "szoveg": k["nyitva_rovid"]})
    if k.get("cim"):
        ch.append({"ikon": "pin", "szoveg": k["cim"]})
    return (f'<section class="sec v-l2 s-deep tx" id="kapcsolat">{hat(c)}{dk(c, "latogatas", matrica=True)}<div class="wrap"><div class="mid" data-rv>'
            f'{kick(l.get("kicker"))}<h2 class="cim">{md(l.get("cim", ""))}</h2>'
            f'<a class="telnagy{"" if k.get("telefon") else " email"}" href="{esc(fo_kapcs(c)[0])}">{esc(fo_kapcs(c)[1])}</a>'
            + (f'<p class="lead">{md(l["lead"])}</p>' if l.get("lead") else "") + gombsor(l)
            + f'<div class="chips">{chips(ch)}</div></div></div></section>')


LATOGATAS.append(dict(id="l2", nev="Sötét blokk, óriás telefonszámmal", leiras="Középre zárt, sötét záró blokk, benne "
    "a telefonszám óriási, kattintható betűkkel. Egyértelmű: „hívj, és kész”.", css=LAT_KOZOS + r"""
.v-l2 .mid{text-align:center;max-width:880px;margin:0 auto}
.v-l2 .kick{justify-content:center}
.v-l2 .telnagy{display:block;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(2.3rem,7.4cqi,5.8rem);line-height:1;color:var(--hl);text-decoration:none;margin:24px 0 16px;letter-spacing:-.01em}
.v-l2 .telnagy.email{font-size:clamp(1.3rem,4.2cqi,3rem);overflow-wrap:anywhere}
.v-l2 .lead{margin:0 auto 28px}
.v-l2 .gombsor{justify-content:center}
.v-l2 .chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:26px}
.v-l2 .chip{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18);color:var(--c-on-deep)}
""", render=_l2))


def _l3(c):
    l = c.get("latogatas", {})
    return (f'<section class="sec v-l3 s-sand tx" id="kapcsolat">{hat(c)}{dk(c, "latogatas")}<div class="wrap">{shead(l)}'
            f'<div class="jegy s-vilagos" data-rv><div class="csonk"><span class="mono">{ui("ora")} {esc(nyitva_cim(c))}</span>{nyitvatartas(c)}</div>'
            f'<div class="fo"><h3>{esc(g(c, "marka", "nev"))}</h3>{adatok(c)}{gombsor(l)}</div></div></div></section>')


LATOGATAS.append(dict(id="l3", nev="Belépőjegy", leiras="A kapcsolati adatok egy nagy, perforált belépőjegyen: a "
    "letéphető szelvényen a nyitvatartás, a fő részen a cím és a gombok. Játékos, emlékezetes.", css=LAT_KOZOS + r"""
.v-l3 .jegy{display:grid;grid-template-columns:36% 64%;max-width:980px;margin:0 auto;background:var(--c0-card);border-radius:22px;filter:drop-shadow(0 22px 30px rgba(0,0,0,.14));-webkit-mask:radial-gradient(circle 18px at 36% 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 18px at 36% 100%,#0000 98%,#000) bottom/100% 51% no-repeat;mask:radial-gradient(circle 18px at 36% 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 18px at 36% 100%,#0000 98%,#000) bottom/100% 51% no-repeat}
.v-l3 .csonk{background:var(--c-primary);color:var(--c-on-primary);padding:clamp(24px,3.4cqi,40px);border-right:3px dashed color-mix(in srgb,var(--c-on-primary) 40%,transparent);--c-head:var(--c-on-primary);--c-line2:color-mix(in srgb,var(--c-on-primary) 30%,transparent)}
.v-l3 .csonk .mono{display:flex;align-items:center;gap:8px;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}
.v-l3 .fo{padding:clamp(24px,3.4cqi,44px)}
.v-l3 .fo h3{font-size:clamp(1.6rem,3cqi,2.4rem);margin-bottom:6px}
.v-l3 .fo .gombsor{margin-top:24px}
@container elo (max-width:760px){.v-l3 .jegy{grid-template-columns:1fr;-webkit-mask:none;mask:none;overflow:hidden}.v-l3 .csonk{border-right:0;border-bottom:3px dashed color-mix(in srgb,var(--c-on-primary) 40%,transparent)}}
""", render=_l3))


def _l4(c):
    l = c.get("latogatas", {})
    return (f'<section class="sec v-l4 s-paper" id="kapcsolat">{hat(c)}<div class="terkep" aria-hidden="true"><div class="utcak"></div>'
            f'<div class="pin">{ui("pin")}<span>{esc(g(c, "marka", "nev"))}</span></div></div>'
            f'<div class="wrap"><div class="kartya s-vilagos" data-rv>{kick(l.get("kicker"))}<h2 class="cim">{md(l.get("cim", ""))}</h2>'
            + (f'<p class="lead">{md(l["lead"])}</p>' if l.get("lead") else "") + f'{nyitvatartas(c)}{gombsor(l)}</div></div></section>')


LATOGATAS.append(dict(id="l4", nev="Stilizált térkép", leiras="A háttér egy rajzolt, márkaszínű „térkép” lüktető "
    "tűvel; előtte kártya a címmel, nyitvatartással és útvonal-gombbal. Helyi, „itt vagyunk”.", css=LAT_KOZOS + r"""
.v-l4{overflow:hidden}
.v-l4 .terkep{position:absolute;inset:0;background:var(--c-tint);z-index:0}
.v-l4 .utcak{position:absolute;inset:-25%;background:radial-gradient(circle at 72% 40%,color-mix(in srgb,var(--c-primary) 16%,transparent) 0 90px,transparent 91px),radial-gradient(ellipse 160px 90px at 20% 78%,color-mix(in srgb,var(--c-primary) 14%,transparent) 99%,transparent),linear-gradient(90deg,transparent 47%,var(--c0-card) 47% 53%,transparent 53%) 0 0/230px 190px,linear-gradient(0deg,transparent 45%,var(--c0-card) 45% 55%,transparent 55%) 0 0/270px 210px,linear-gradient(32deg,transparent 49.3%,color-mix(in srgb,var(--c-accent) 55%,var(--c0-card)) 49.3% 50.7%,transparent 50.7%) 0 0/100% 100%;transform:rotate(-9deg)}
.v-l4 .pin{position:absolute;right:20%;top:40%;display:flex;flex-direction:column;align-items:center;gap:6px;z-index:2}
.v-l4 .pin .ui{width:64px;height:64px;color:var(--c-primary);fill:var(--c0-card);filter:drop-shadow(0 10px 12px rgba(0,0,0,.25));animation:l4ugral 2.2s ease-in-out infinite}
.v-l4 .pin span{background:var(--c0-card);color:var(--c0-head);font-weight:800;font-size:.86rem;padding:6px 12px;border-radius:999px;box-shadow:var(--sh-2)}
.v-l4 .pin::before{content:"";position:absolute;top:50px;width:70px;height:22px;border-radius:50%;background:color-mix(in srgb,var(--c-primary) 30%,transparent);animation:l4pulz 2.2s ease-out infinite;z-index:-1}
@keyframes l4ugral{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes l4pulz{0%{transform:scale(.4);opacity:.9}100%{transform:scale(1.6);opacity:0}}
.v-l4 .kartya{position:relative;z-index:3;max-width:520px;background:var(--c0-card);border-radius:26px;padding:clamp(24px,3.4cqi,42px);box-shadow:var(--sh-3)}
.v-l4 .lead{margin:14px 0 18px}
.v-l4 .gombsor{margin-top:22px}
@container elo (max-width:760px){.v-l4 .pin{right:12%;top:8%}.v-l4 .kartya{margin-top:140px}}
""", render=_l4))


def _l5(c):
    l = c.get("latogatas", {})
    return (f'<section class="sec v-l5 s-white" id="kapcsolat">{hat(c)}<div class="wrap grid"><div class="kep" data-rv>{foto(c, l.get("foto"), "4/3")}</div>'
            f'<div class="info bal" data-rv>{kick(l.get("kicker"))}<h2 class="cim">{md(l.get("cim", ""))}</h2>'
            + (f'<p class="lead">{md(l["lead"])}</p>' if l.get("lead") else "")
            + f'<div class="ket"><div><h3>{ui("ora")}{esc(nyitva_cim(c))} {_nyitva_jelzo(c)}</h3>{nyitvatartas(c)}</div><div><h3>{ui("pin")}Elérhetőség</h3>{adatok(c)}</div></div>{gombsor(l)}</div></div></section>')


LATOGATAS.append(dict(id="l5", nev="Fotó + két infóhasáb", leiras="Balra az üzlet fotója, jobbra meghívó cím és két "
    "tiszta hasáb: nyitvatartás és elérhetőség. Egyszerű, informatív.", css=LAT_KOZOS + r"""
.v-l5 .grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5cqi,80px);align-items:center}
.v-l5 .lead{margin:14px 0 22px}
.v-l5 .ket{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-bottom:26px}
.v-l5 h3{display:flex;align-items:center;gap:8px;font-size:1.06rem;margin-bottom:6px;flex-wrap:wrap}
.v-l5 h3 .ui{color:var(--hl)}
.v-l5 .adat{margin-top:4px}
@container elo (max-width:860px){.v-l5 .grid{grid-template-columns:1fr}}
@container elo (max-width:520px){.v-l5 .ket{grid-template-columns:1fr}}
""", render=_l5))


def _l6(c):
    l = c.get("latogatas", {})
    h = c.get("hirlevel", {})
    return (f'<section class="sec v-l6 s-tint tx" id="kapcsolat">{hat(c)}{dk(c, "latogatas")}<div class="wrap"><div class="doboz s-vilagos" data-rv>'
            f'<div class="hb">{kick(h.get("kicker") or l.get("kicker"))}<h2 class="cim">{md(h.get("cim") or l.get("cim", ""))}</h2>'
            f'<p class="lead">{md(h.get("szoveg") or l.get("lead", ""))}</p>{btn(h.get("cta")) if h.get("cta") else gombsor(l)}</div>'
            f'<div class="hj"><h3>{ui("ora")}{esc(nyitva_cim(c))}</h3>{nyitvatartas(c)}{adatok(c)}</div></div></div></section>')


LATOGATAS.append(dict(id="l6", nev="Hírlevél-doboz + infó", leiras="Nagy, lekerekített doboz: balra a hírlevél-"
    "meghívás (újdonságok, akciók), jobbra a nyitvatartás és elérhetőség. Visszatérő vendégeket épít.", css=LAT_KOZOS + r"""
.v-l6 .doboz{display:grid;grid-template-columns:1.2fr .8fr;gap:0;background:var(--c0-card);border-radius:32px;overflow:hidden;box-shadow:var(--sh-3)}
.v-l6 .hb{padding:clamp(28px,4.4cqi,60px)}
.v-l6 .hb .lead{margin:16px 0 26px}
.v-l6 .hj{padding:clamp(24px,3.6cqi,44px);background:var(--c-primary-ll)}
.v-l6 .hj h3{display:flex;align-items:center;gap:8px;font-size:1.15rem;margin-bottom:8px}
.v-l6 .hj h3 .ui{color:var(--hl)}
@container elo (max-width:820px){.v-l6 .doboz{grid-template-columns:1fr}}
""", render=_l6))

# ============================================================== LÁBLÉC
LABLEC = []


def _lbl_linkek(c):
    lk = g(c, "lablec", "linkek") or g(c, "nav", "linkek") or []
    return "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in lk)


def _jogi(c):
    j = g(c, "lablec", "jogi") or []
    ev = datetime.date.today().year
    lk = " · ".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in j)
    return f'<span>© {ev} {esc(g(c, "lablec", "cegnev") or g(c, "marka", "nev"))}</span>' + (f"<span>{lk}</span>" if lk else "")


def _lb1(c):
    return (f'<footer class="v-lb1 s-deep"><div class="wrap"><div class="cols"><div class="c0">{logo(c, 74, feher=True)}'
            f'<p>{md(g(c, "lablec", "szoveg"))}</p>{social(c)}</div><div><h4>Oldalak</h4><nav>{_lbl_linkek(c)}</nav></div>'
            f'<div><h4>Elérhetőség</h4>{adatok(c)}</div><div><h4>{esc(nyitva_cim(c))}</h4>{nyitvatartas(c)}</div></div>'
            f'<div class="also">{_jogi(c)}</div></div></footer>')


LBL_KOZOS = r"""
footer .soc{display:flex;gap:10px;margin-top:14px}
footer .soc a{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--c-line2);color:var(--c-ink);transition:all .2s}
footer .soc a:hover{background:var(--c-primary);color:var(--c-on-primary);border-color:var(--c-primary)}
footer nav{display:grid;gap:8px}
footer nav a{text-decoration:none;color:var(--c-ink-2)}
footer nav a:hover{color:var(--c-head);text-decoration:underline}
footer h4{font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;font-family:var(--f-body);font-weight:800;margin-bottom:14px;color:var(--c-head)}
footer .also{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;font-size:.84rem;color:var(--c-ink-3)}
footer .also a{color:inherit}
"""

LABLEC.append(dict(id="lb1", nev="Sötét, négy hasábos", leiras="Klasszikus sötét lábléc: logó és rövid szöveg, "
    "oldalak, elérhetőség, nyitvatartás; alul a jogi sor. Teljes, rendezett.", css=LBL_KOZOS + LAT_KOZOS + r"""
.v-lb1{background:var(--c-deep);color:var(--c-ink);padding:clamp(54px,6cqi,86px) 0 26px;position:relative}
.v-lb1 .cols{display:grid;grid-template-columns:1.3fr .8fr 1fr 1fr;gap:clamp(24px,4cqi,56px)}
.v-lb1 .c0 p{color:var(--c-ink-2);margin:16px 0 0;max-width:34ch}
.v-lb1 .nyt li{padding:7px 0;font-size:.92rem}
.v-lb1 .adat a{font-weight:600;font-size:.94rem}
.v-lb1 .also{border-top:1px solid var(--c-line);margin-top:44px;padding-top:20px}
@container elo (max-width:900px){.v-lb1 .cols{grid-template-columns:1fr 1fr}}
@container elo (max-width:540px){.v-lb1 .cols{grid-template-columns:1fr}}
""", render=_lb1))


def _lb2(c):
    return (f'<footer class="v-lb2 s-paper"><div class="wrap"><div class="cols"><div>{logo(c, 64)}<p>{md(g(c, "lablec", "szoveg"))}</p></div>'
            f'<div><h4>Oldalak</h4><nav>{_lbl_linkek(c)}</nav></div><div><h4>Elérhetőség</h4>{adatok(c)}{social(c)}</div></div>'
            f'<div class="orias" aria-hidden="true">{esc(g(c, "marka", "nev"))}</div><div class="also">{_jogi(c)}</div></div></footer>')


LABLEC.append(dict(id="lb2", nev="Óriás márkanév", leiras="Világos lábléc, alján a márkanév a teljes szélességben, "
    "óriási betűkkel. Magabiztos, modern, erős lezárás.", css=LBL_KOZOS + LAT_KOZOS + r"""
.v-lb2{background:var(--c-paper);padding:clamp(54px,6cqi,86px) 0 22px;border-top:1px solid var(--c-line);overflow:hidden}
.v-lb2 .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:clamp(24px,4cqi,56px)}
.v-lb2 .cols p{color:var(--c-ink-2);margin:14px 0 0;max-width:36ch}
.v-lb2 .orias{font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(3.4rem,15.5cqi,14rem);line-height:.82;letter-spacing:-.03em;color:var(--c-primary);white-space:nowrap;margin:clamp(36px,5cqi,60px) 0 18px;text-transform:var(--tt-display)}
@container elo (max-width:760px){.v-lb2 .cols{grid-template-columns:1fr}}
""", render=_lb2))


def _lb3(c):
    return (f'<footer class="v-lb3 s-white"><div class="wrap">{logo(c, 84, "ko")}<nav class="sor">{_lbl_linkek(c)}</nav>'
            f'{social(c)}<p class="kis">{" · ".join(esc(x) for x in (g(c, "kapcsolat", "cim"), g(c, "kapcsolat", "telefon"), g(c, "kapcsolat", "email")) if x)}</p>'
            f'<div class="also">{_jogi(c)}</div></div></footer>')


LABLEC.append(dict(id="lb3", nev="Középre zárt, minimál", leiras="Minden középen: logó, egy sor menü pontokkal "
    "elválasztva, közösségi ikonok, apró betűs adatok. Csendes, elegáns.", css=LBL_KOZOS + r"""
.v-lb3{background:var(--c-card);padding:clamp(50px,6cqi,80px) 0 26px;text-align:center;border-top:1px solid var(--c-line)}
.v-lb3 .logo{margin:0 auto 18px}
.v-lb3 nav.sor{display:flex;flex-wrap:wrap;justify-content:center;gap:0}
.v-lb3 nav.sor a{padding:4px 16px;border-left:1px solid var(--c-line2);font-weight:700;color:var(--c-ink)}
.v-lb3 nav.sor a:first-child{border-left:0}
.v-lb3 .soc{justify-content:center;margin:20px 0 14px}
.v-lb3 .kis{font-size:.9rem;color:var(--c-ink-2)}
.v-lb3 .also{justify-content:center;gap:18px;margin-top:22px}
""", render=_lb3))


def _lb4(c):
    k = c.get("kapcsolat", {})
    return (f'<footer class="v-lb4 s-primary"><div class="wrap"><div class="fent"><h2 class="cim">{md(g(c, "lablec", "felhivas") or g(c, "marka", "szlogen"))}</h2>'
            f'<a class="tel" href="{esc(fo_kapcs(c)[0])}">{ui(fo_kapcs(c)[2])}{esc(fo_kapcs(c)[1])}</a></div>'
            f'<div class="cols"><div>{logo(c, 60, feher=True)}<p>{md(g(c, "lablec", "szoveg"))}</p></div><div><h4>Oldalak</h4><nav>{_lbl_linkek(c)}</nav></div>'
            f'<div><h4>{esc(nyitva_cim(c))}</h4>{nyitvatartas(c)}</div><div><h4>Kövess</h4>{social(c)}</div></div><div class="also">{_jogi(c)}</div></div></footer>')


LABLEC.append(dict(id="lb4", nev="Színes, lekerekített", leiras="Márkaszínű lábléc lekerekített felső sarkokkal, ami "
    "ráfut az előző blokkra; tetején nagy felhívás és telefonszám. Barátságos, lendületes.", css=LBL_KOZOS + LAT_KOZOS + r"""
.v-lb4{background:var(--c-primary);color:var(--c-ink);border-radius:clamp(26px,4cqi,48px) clamp(26px,4cqi,48px) 0 0;margin-top:-36px;position:relative;z-index:5;padding:clamp(46px,6cqi,80px) 0 24px}
.v-lb4 .fent{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding-bottom:30px;border-bottom:1px solid var(--c-line2);margin-bottom:34px}
.v-lb4 .fent .cim{max-width:16ch}
.v-lb4 .tel{display:inline-flex;align-items:center;gap:12px;font-family:var(--f-display);font-weight:var(--w-display);font-size:clamp(1.4rem,3cqi,2.4rem);color:var(--c-ink);text-decoration:none;background:color-mix(in srgb,var(--c-on-primary) 12%,transparent);padding:12px 22px;border-radius:999px}
.v-lb4 .cols{display:grid;grid-template-columns:1.3fr .9fr 1fr .8fr;gap:clamp(22px,4cqi,48px)}
.v-lb4 .cols p{color:var(--c-ink-2);margin-top:12px}
.v-lb4 .nyt li{padding:6px 0}
.v-lb4 .also{margin-top:40px;padding-top:18px;border-top:1px solid var(--c-line)}
@container elo (max-width:900px){.v-lb4 .cols{grid-template-columns:1fr 1fr}}
""", render=_lb4))


def _lb5(c):
    k = c.get("kapcsolat", {})
    ny = "".join(f'<li><span>{esc(n)}</span><i></i><b>{esc(i)}</b></li>' for n, i in (k.get("nyitvatartas") or []))
    return (f'<footer class="v-lb5 s-sand"><div class="wrap"><div class="blokk s-vilagos">{logo(c, 66, "ko")}'
            f'<p class="nev">{esc(g(c, "lablec", "cegnev") or g(c, "marka", "nev"))}</p><p class="mono">{esc(k.get("cim", ""))}</p>'
            f'<ul class="sorok mono">{ny}' + (f'<li><span>Telefon</span><i></i><b>{esc(k["telefon"])}</b></li>' if k.get("telefon") else "") + f'<li><span>E-mail</span><i></i><b>{esc(k.get("email", ""))}</b></li></ul>'
            f'<div class="vonal" aria-hidden="true"></div><p class="szlogen kezi">{md(g(c, "marka", "szlogen"))}</p><nav class="lk">{_lbl_linkek(c)}</nav>'
            f'{social(c)}</div><div class="also">{_jogi(c)}</div></div></footer>')


LABLEC.append(dict(id="lb5", nev="Nyugta (blokk)", leiras="A lábléc egy középre zárt, fogazott szélű pénztárblokk "
    "írógépes betűkkel: nyitvatartás, telefon, e-mail „tételekként”. Vicces, emlékezetes, vendéglátós.", css=LBL_KOZOS + r"""
.v-lb5{background:var(--c-sand);padding:clamp(56px,7cqi,96px) 0 24px}
.v-lb5 .blokk{max-width:460px;margin:0 auto;background:var(--c0-card);padding:34px 30px 30px;text-align:center;position:relative;filter:drop-shadow(0 16px 22px rgba(0,0,0,.12));-webkit-mask:conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) top/18px 51% repeat-x,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/18px 51% repeat-x;mask:conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) top/18px 51% repeat-x,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/18px 51% repeat-x}
.v-lb5 .logo{margin:0 auto 12px}
.v-lb5 .nev{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.3rem;margin:0}
.v-lb5 .mono{font-size:.8rem;color:var(--c-ink-2)}
.v-lb5 .sorok{display:grid;gap:6px;margin:18px 0;text-align:left;font-size:.8rem}
.v-lb5 .sorok li{display:flex;gap:6px;align-items:baseline}
.v-lb5 .sorok i{flex:1;border-bottom:1px dotted var(--c-ink-3)}
.v-lb5 .sorok b{font-weight:600}
.v-lb5 .vonal{height:44px;margin:16px 30px;background:repeating-linear-gradient(90deg,var(--c-ink) 0 2px,transparent 2px 4px,var(--c-ink) 4px 7px,transparent 7px 9px,var(--c-ink) 9px 10px,transparent 10px 13px)}
.v-lb5 .szlogen{font-size:calc(var(--fs-hand)*1.3rem);margin:6px 0 14px}
.v-lb5 nav.lk{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 16px;font-size:.88rem}
.v-lb5 .soc{justify-content:center}
.v-lb5 .also{justify-content:center;gap:18px;margin-top:30px}
""", render=_lb5))
