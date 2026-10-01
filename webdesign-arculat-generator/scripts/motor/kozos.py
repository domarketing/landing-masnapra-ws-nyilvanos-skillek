# -*- coding: utf-8 -*-
"""HTML-darabok, amelyekből a szekció-változatok épülnek. Mindegyik a ctx (arculat.json + előkészített adatok)
alapján dolgozik, és ha egy adat hiányzik, egyszerűen kimarad (nem hibázik)."""
from .alap import esc, md, sima, g, ui

_UID = [0]


def uid():
    _UID[0] += 1
    return _UID[0]


def kick(t):
    return f'<p class="kick"><span>{md(t)}</span></p>' if t else ""


def shead(d, bal=False, tag="h2", rv=True):
    if not d:
        return ""
    p = [kick(d.get("kicker"))]
    if d.get("cim"):
        p.append(f'<{tag} class="cim">{md(d["cim"])}</{tag}>')
    if d.get("lead"):
        p.append(f'<p class="lead">{md(d["lead"])}</p>')
    if not any(p):
        return ""
    return f'<header class="shead{" bal" if bal else ""}"{" data-rv" if rv else ""}>{"".join(p)}</header>'


def btn(c, alt=False, ikon="nyil"):
    if not c or not c.get("szoveg"):
        return ""
    ik = c.get("ikon", ikon)
    href = c.get("href", "#")
    kulso = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return (f'<a class="btn{" alt" if alt else ""}" href="{esc(href)}"{kulso}>{esc(c["szoveg"])}'
            f'{ui(ik) if ik else ""}</a>')


def gombsor(d, k1="cta1", k2="cta2"):
    b = btn(d.get(k1)) + btn(d.get(k2), alt=True, ikon=g(d, k2, "ikon", alap="tel") if d.get(k2) else "")
    return f'<div class="gombsor">{b}</div>' if b else ""


def foto(ctx, fid, ar="4/3", cls="", felirat=None, pos=None, extra=""):
    f = ctx["fotok"].get(fid) if fid else None
    fc = f'<figcaption>{esc(felirat)}</figcaption>' if felirat else ""
    if not f:
        return (f'<figure class="ft {cls}" style="--ar:{ar}"><div class="ph nincsfoto" role="img" aria-label="fotó helye">'
                f'<span>FOTÓ HELYE</span></div>{fc}</figure>')
    p = pos or f.get("pozicio") or "50% 50%"
    return (f'<figure class="ft {cls}" style="--ar:{ar}"{extra}><div class="ph f-{fid}" role="img" '
            f'aria-label="{esc(sima(f.get("alt", "")))}" style="--pos:{p}"></div>{fc}</figure>')


def ph(ctx, fid, cls=""):
    """Csupasz háttérkép-div (keret nélkül, a fotókezelés NEM vonatkozik rá)."""
    f = ctx["fotok"].get(fid) if fid else None
    if not f:
        return f'<div class="ph nincsfoto {cls}"></div>'
    return (f'<div class="ph f-{fid} {cls}" role="img" aria-label="{esc(sima(f.get("alt", "")))}" '
            f'style="--pos:{f.get("pozicio", "50% 50%")}"></div>')


def ik(nev, cls=""):
    if not nev:
        return ""
    return f'<span class="ik ik-{esc(nev)} {cls}" aria-hidden="true"></span>'


def logo(ctx, h=48, cls="", feher=False):
    lg = ctx.get("_logo")
    if not lg:
        nev = esc(g(ctx, "marka", "nev"))
        return f'<span class="logo-szoveg {cls}">{nev}</span>'
    c = "lg-feher" if feher and lg.get("feher") else "lg"
    return (f'<span class="logo {c} {cls}" role="img" aria-label="{esc(g(ctx, "marka", "nev"))} logó" '
            f'style="--logo-h:{h}px;--logo-ar:{lg["ar"]}"></span>')


def dk(ctx, kulcs, matrica=False):
    m = ctx.get("motivum", {})
    szo = g(m, "szellemszavak", kulcs) or ""
    mt = ""
    if matrica:
        lst = m.get("matricak") or []
        if lst:
            i = ctx.setdefault("_mi", 0)
            ctx["_mi"] = i + 1
            mt = f'<i class="dk-m"><span>{esc(lst[i % len(lst)])}</span></i>'
    return (f'<div class="dk" aria-hidden="true"><i class="dk-szo">{esc(szo)}</i><i class="dk-jel"></i><i class="dk-a"></i>'
            f'<i class="dk-b"></i><i class="dk-c"></i><i class="dk-r"></i><i class="dk-f1"></i><i class="dk-f2"></i>{mt}</div>')


def hat(ctx, masod=False):
    t = g(ctx, "motivum", "ticker") or []
    spans = "".join(f"<span>{esc(x)}</span>" for x in t) * 2
    return (f'<div class="hat{" masod" if masod else ""}" aria-hidden="true"><div class="tick"><div class="tick-in">'
            f'{spans}</div></div></div>')


def chips(lst, ikon=None):
    out = []
    for c in lst or []:
        if isinstance(c, dict):
            i = c.get("ikon")
            t = c.get("szoveg", "")
        else:
            i, t = ikon, c
        out.append(f'<span class="chip">{ui(i) if i else "<i class=pt></i>"}{md(t)}</span>')
    return "".join(out)


def nyitvatartas(ctx, cls="nyt"):
    ny = g(ctx, "kapcsolat", "nyitvatartas") or []
    if not ny:
        return ""
    li = "".join(f'<li><span>{esc(n)}</span><b>{esc(i)}</b></li>' for n, i in ny)
    return f'<ul class="{cls}">{li}</ul>'


def nyitva_cim(ctx):
    """A nyitvatartás-blokk címe; online szolgáltatónál átírható (kapcsolat.nyitva_cim, pl. „A Klub ritmusa”)."""
    return g(ctx, "kapcsolat", "nyitva_cim") or "Nyitvatartás"


def fo_kapcs(ctx):
    """A fő elérhetőség: telefon, ha van, különben e-mail. Visszaad: (href, szöveg, ikon)."""
    k = ctx.get("kapcsolat", {})
    if k.get("telefon"):
        return "tel:" + k["telefon"].replace(" ", ""), k["telefon"], "tel"
    if k.get("email"):
        return "mailto:" + k["email"], k["email"], "mail"
    return "#", "", "tel"


def adatok(ctx, cls="adat"):
    k = ctx.get("kapcsolat", {})
    s = []
    if k.get("cim"):
        href = k.get("terkep_url") or "#"
        s.append(f'<a href="{esc(href)}" target="_blank" rel="noopener">{ui("pin")}<span>{esc(k["cim"])}</span></a>')
    if k.get("telefon"):
        s.append(f'<a href="tel:{esc(k["telefon"].replace(" ", ""))}">{ui("tel")}<span>{esc(k["telefon"])}</span></a>')
    if k.get("email"):
        s.append(f'<a href="mailto:{esc(k["email"])}">{ui("mail")}<span>{esc(k["email"])}</span></a>')
    return f'<div class="{cls}">{"".join(s)}</div>' if s else ""


def social(ctx, cls="soc"):
    s = g(ctx, "kapcsolat", "social") or []
    out = []
    for x in s:
        t = x.get("tipus", "")
        i = "fb" if "face" in t else "ig" if "insta" in t else "nyil"
        out.append(f'<a href="{esc(x.get("url", "#"))}" target="_blank" rel="noopener" aria-label="{esc(t)}">{ui(i)}</a>')
    return f'<div class="{cls}">{"".join(out)}</div>' if out else ""


def navlinkek(ctx):
    return "".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in (g(ctx, "nav", "linkek") or []))


def statok(lst, cls="stat"):
    if not lst:
        return ""
    return f'<div class="{cls}">' + "".join(f'<div><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in lst) + "</div>"


def kezi(t, cls=""):
    return f'<p class="kezi jegyzet {cls}">{md(t)}</p>' if t else ""


def korszoveg(t, hossz=44):
    t = (t or "").upper().strip()
    if not t:
        return ""
    s = ""
    while len(s) < hossz:
        s += t + " • "
    return esc(s)
