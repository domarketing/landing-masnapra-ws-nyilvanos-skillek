# -*- coding: utf-8 -*-
"""Közös segédek: színmatek, paletta-levezetés, betű-URL, szöveg-jelölés, képbeágyazás, UI-ikonok, motívumok."""
import re, html, base64, io, json, os, urllib.parse
from pathlib import Path

# ------------------------------------------------------------------ szöveg


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def md(s):
    """Egyszerű jelölés a tartalomban: ==kiemelt== -> <mark>, **félkövér** -> <b>, sortörés: |"""
    s = esc(s)
    s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s.replace(" | ", "<br>")


def sima(s):
    """Jelölés nélküli szöveg (alt, aria, title)."""
    return re.sub(r"==|\*\*", "", str(s or "")).replace(" | ", " ")


def g(d, *kulcsok, alap=""):
    """Biztonságos mélységi lekérés: g(ctx, 'hero', 'cim')."""
    for k in kulcsok:
        if isinstance(d, dict):
            d = d.get(k)
        elif isinstance(d, list) and isinstance(k, int) and -len(d) <= k < len(d):
            d = d[k]
        else:
            return alap
        if d is None:
            return alap
    return d


# ------------------------------------------------------------------ szín

def h2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb2h(r, g_, b):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in (r, g_, b))


def mix(a, b, t):
    """a és b keveréke, t = b aránya (0..1)."""
    A, B = h2rgb(a), h2rgb(b)
    return rgb2h(*(A[i] * (1 - t) + B[i] * t for i in range(3)))


def lum(h):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g_, b = h2rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g_) + 0.0722 * ch(b)


def kontraszt(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def rajta(bg, sotet="#111111", vilagos="#ffffff"):
    """A háttérre olvashatóbb szövegszín."""
    return vilagos if kontraszt(bg, vilagos) >= kontraszt(bg, sotet) * 0.8 else sotet


def rgba(h, a):
    r, g_, b = h2rgb(h)
    return f"rgba({r},{g_},{b},{a})"


def paletta_tokenek(p):
    """Tömör paletta-leírásból a teljes token-készlet (CSS változók).
    p: {primary, accent, accent2?, paper?, ink?, card?, deep?, mod?: 'vilagos'|'sotet'}"""
    sotet = p.get("mod") == "sotet"
    pri = p["primary"]
    acc = p.get("accent") or mix(pri, "#f2b84b", .6)
    acc2 = p.get("accent2") or mix(acc, pri, .45)
    paper = p.get("paper") or ("#141816" if sotet else "#fbf8f2")
    ink = p.get("ink") or ("#f3efe6" if sotet else mix(pri, "#141414", .82))
    card = p.get("card") or (mix(paper, "#ffffff", .06) if sotet else "#ffffff")
    deep = p.get("deep") or (mix(pri, "#000000", .55) if not sotet else mix(paper, "#000000", .35))
    head = p.get("head") or ink
    t = {
        "--c-primary": pri,
        "--c-primary-d": mix(pri, "#000000", .2),
        "--c-primary-dd": mix(pri, "#000000", .38),
        "--c-primary-l": mix(pri, paper, .72),
        "--c-primary-ll": mix(pri, paper, .88),
        "--c-accent": acc,
        "--c-accent-d": mix(acc, "#000000", .22),
        "--c-accent-l": mix(acc, paper, .72),
        "--c-accent2": acc2,
        "--c-paper": paper,
        "--c-card": card,
        "--c-sand": mix(paper, pri if sotet else "#a08a60", .07 if not sotet else .06),
        "--c-tint": mix(pri, paper, .9),
        "--c-deep": deep,
        "--c-ink": ink,
        "--c-head": head,
        "--c-ink-2": mix(ink, paper, .28),
        "--c-ink-3": mix(ink, paper, .5),
        "--c-line": mix(ink, paper, .87),
        "--c-line2": mix(ink, paper, .76),
        "--c-on-primary": rajta(pri, sotet="#161616"),
        "--c-on-accent": rajta(acc, sotet="#161616"),
        "--c-on-deep": mix("#ffffff", deep, .06),
        "--c-on-deep-2": mix("#ffffff", deep, .3),
        "--c-hand": p.get("hand") or (acc if kontraszt(acc, paper) > 2.6 else mix(acc, "#000000", .3)),
        "--sh-1": f"0 1px 2px {rgba(ink if not sotet else '#000000', .08)}",
        "--sh-2": f"0 10px 24px -14px {rgba(ink if not sotet else '#000000', .32)},0 2px 6px -3px {rgba(ink if not sotet else '#000000', .12)}",
        "--sh-3": f"0 26px 50px -24px {rgba(ink if not sotet else '#000000', .42)},0 6px 14px -8px {rgba(ink if not sotet else '#000000', .16)}",
        "--sh-color": f"0 20px 40px -18px {rgba(pri, .55)}",
    }
    # telített szín kontraszt-őre: ha a primary túl világos a papíron (pl. sárga), a szövegekhez sötétebb árnyalat kell
    t["--c-primary-text"] = pri if kontraszt(pri, paper) >= 3.2 else mix(pri, "#000000", .42 if not sotet else 0)
    if sotet:
        t["--c-primary-text"] = pri if kontraszt(pri, paper) >= 3.2 else mix(pri, "#ffffff", .4)
    t["--c-accent-text"] = acc if kontraszt(acc, paper) >= 3.2 else (mix(acc, "#000000", .42) if not sotet else mix(acc, "#ffffff", .4))

    def legjobb(bg, jeloltek, kuszob):
        for c in jeloltek:
            if kontraszt(c, bg) >= kuszob:
                return c
        return max(jeloltek, key=lambda c: kontraszt(c, bg))
    t["--c-deep-hl"] = legjobb(deep, [acc, acc2, mix(pri, "#ffffff", .45), "#ffffff"], 3.0)
    t["--c-primary-hl"] = legjobb(pri, [acc2, acc, mix(pri, "#ffffff", .75), t["--c-on-primary"]], 2.4)
    t["--c-deep-btn"] = legjobb(deep, [pri, acc, acc2, "#ffffff"], 2.6)
    t["--c-on-deep-btn"] = rajta(t["--c-deep-btn"], sotet="#161616")
    t["--c-deep-btn-d"] = mix(t["--c-deep-btn"], "#000000", .35)
    t["--c-accent2-text"] = acc2 if kontraszt(acc2, paper) >= 3 else (mix(acc2, "#000000", .42) if not sotet else mix(acc2, "#ffffff", .4))
    t["--c-on-primary-hl"] = rajta(t["--c-primary-hl"], sotet="#161616")
    # kiemelő-csík színes (primary) felületen: látsszon a háttéren, DE a rajta ülő szöveg olvasható maradjon
    onp = t["--c-on-primary"]
    mk = next((c for c in (acc, acc2) if kontraszt(c, onp) >= 2.2 and kontraszt(c, pri) >= 1.35), None)
    t["--c-primary-mk"] = mk or mix(pri, onp, .32)
    t["--c-on-primary-mk"] = onp if (mk is None or kontraszt(onp, mk) >= 2.2) else rajta(mk, sotet="#161616")
    # logó: sötét palettán a fehér változat
    t["--logo-img"] = "var(--logo-feher)" if sotet else "var(--logo-eredeti)"
    t["--c-on-deep-hl"] = rajta(t["--c-deep-hl"], sotet="#161616")
    # érintetlen másolatok: a színes/sötét szekción belüli világos dobozok (.s-vilagos) ezekre állnak vissza
    for k in ("ink", "head", "ink-2", "ink-3", "line", "line2", "card", "paper", "tint", "primary-text"):
        t[f"--c0-{k}"] = t[f"--c-{k}"]
    return t


def tokenek_css(t):
    return ";".join(f"{k}:{v}" for k, v in t.items())


# ------------------------------------------------------------------ betű

BETU_TENGELY = {}


def betu_katalogus():
    global BETU_TENGELY
    if not BETU_TENGELY:
        p = Path(__file__).resolve().parents[2] / "references" / "betuk.json"
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            BETU_TENGELY = {b["csalad"]: b.get("tengely", "") for b in data.get("betuk", [])}
        except Exception:
            BETU_TENGELY = {}
    return BETU_TENGELY


def google_fonts_url(csaladok):
    kat = betu_katalogus()
    seen, parts = set(), []
    for c in csaladok:
        if not c or c in seen:
            continue
        seen.add(c)
        ax = kat.get(c, "")
        parts.append("family=" + urllib.parse.quote_plus(c) + (":" + ax if ax else ""))
    if not parts:
        return ""
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"


def betu_tokenek(b):
    """b: {display, body, hand?, label?, w_display?, ls_display?, nagybetus?, w_body?}"""
    def st(f, fb):
        return f"'{f}',{fb}" if f else fb
    t = {
        "--f-display": st(b.get("display"), "Georgia,serif"),
        "--f-body": st(b.get("body"), "system-ui,-apple-system,'Segoe UI',sans-serif"),
        "--f-hand": st(b.get("hand"), "'Segoe Script','Bradley Hand',cursive"),
        "--f-label": st(b.get("label"), "ui-monospace,'SFMono-Regular',Menlo,monospace"),
        "--w-display": str(b.get("w_display", 800)),
        "--w-body-b": str(b.get("w_body_b", 700)),
        "--ls-display": b.get("ls_display", "-0.015em"),
        "--tt-display": "uppercase" if b.get("nagybetus") else "none",
        "--lh-display": str(b.get("lh_display", 1.06)),
        "--fs-hand": str(b.get("fs_hand", 1.25)),
        "--hero-scale": str(b.get("hero_scale", 1)),
    }
    return t


# ------------------------------------------------------------------ képek

def _kep_bytes(path, max_px=1400, minoseg=80, png=False):
    try:
        from PIL import Image
    except Exception:
        return Path(path).read_bytes(), mime_of(path)
    with Image.open(path) as im:
        im.load()
        if max(im.size) > max_px:
            im.thumbnail((max_px, max_px), Image.LANCZOS)
        buf = io.BytesIO()
        if png or (im.mode in ("RGBA", "LA", "P") and "A" in im.getbands() or (im.mode == "P" and "transparency" in im.info)):
            im = im.convert("RGBA")
            im.save(buf, format="PNG", optimize=True)
            return buf.getvalue(), "image/png"
        im.convert("RGB").save(buf, format="JPEG", quality=minoseg, optimize=True, progressive=True)
        return buf.getvalue(), "image/jpeg"


def mime_of(p):
    e = str(p).lower().rsplit(".", 1)[-1]
    return {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp",
            "svg": "image/svg+xml", "gif": "image/gif"}.get(e, "application/octet-stream")


def data_uri(path, max_px=1400, minoseg=80, png=False):
    p = str(path)
    if p.lower().endswith(".svg"):
        return "data:image/svg+xml;base64," + base64.b64encode(Path(p).read_bytes()).decode()
    b, mime = _kep_bytes(p, max_px, minoseg, png)
    return f"data:{mime};base64," + base64.b64encode(b).decode()


def logo_feher(path, cel):
    """A logó fehér (világos) változata sötét háttérre: az alfa marad, minden szín fehér lesz.
    Ha a logó nem átlátszó (fehér doboz), előbb kivágja a világos hátteret."""
    from PIL import Image
    im = Image.open(path).convert("RGBA")
    px = im.load()
    w, h = im.size
    atlatszo = any(px[x, y][3] < 200 for x in range(0, w, max(1, w // 40)) for y in range(0, h, max(1, h // 40)))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g_, b, a = px[x, y]
            if not atlatszo:
                l = (r + g_ + b) / 3
                a = int(max(0, min(255, (235 - l) * 3.2)))  # a világos háttér eltűnik
            if a > 8:
                op[x, y] = (255, 255, 255, a)
    out.save(cel)
    return cel


# ------------------------------------------------------------------ UI-ikonok (inline SVG, currentColor)

_UI = {
    "tel": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.6"/>',
    "ora": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "nyil": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "le": '<path d="M12 5v14M6 13l6 6 6-6"/>',
    "pipa": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "csillag": '<path d="m12 3.5 2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.8z"/>',
    "fb": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8.6c0-.3.3-.6.6-.6z"/>',
    "ig": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plusz": '<path d="M12 5v14M5 12h14"/>',
    "bal": '<path d="M15 5l-7 7 7 7"/>',
    "jobb": '<path d="M9 5l7 7-7 7"/>',
    "szem": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
    "szoveg": '<path d="M4 6h16M4 12h10M4 18h13"/>',
    "haz": '<path d="M4 11 12 4l8 7v9H4z"/><path d="M10 20v-5h4v5"/>',
    "kulcs": '<circle cx="8" cy="15" r="4"/><path d="m11 12 8-8M16 7l2 2"/>',
}


def ui(nev, cls="ui"):
    p = _UI.get(nev, _UI["pipa"])
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')


# ------------------------------------------------------------------ motívumok (maszk-SVG-k)

ALAP_MOTIVUMOK = {
    "plusz": '<path d="M42 10h16v32h32v16H58v32H42V58H10V42h32z"/>',
    "kor": '<circle cx="50" cy="50" r="34" fill="none" stroke="#000" stroke-width="12"/>',
    "csillag": '<path d="M50 6l11 30 32 3-24 21 8 32-27-17-27 17 8-32L7 39l32-3z"/>',
    "hullam": '<path d="M5 60c15-25 30-25 45 0s30 25 45 0" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/>',
    "pont": '<circle cx="30" cy="30" r="14"/><circle cx="72" cy="40" r="10"/><circle cx="45" cy="76" r="12"/>',
    "level": '<path d="M50 6C78 24 84 62 50 94 16 62 22 24 50 6z"/>',
}


def motivum_svg(belso, meret=100):
    s = belso if belso.strip().startswith("<") else f'<path d="{belso}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{meret}" height="{meret}">{s}</svg>'


def svg_uri(svg):
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe=" =:/,;'()@")


def motivum_uri(belso):
    return svg_uri(motivum_svg(belso)).replace('"', "'")


def minta_csempe_uri(motivumok, meret=132):
    """Ismétlődő minta-csempe 2-3 motívumból, elforgatva (a Motívum-minta textúrához)."""
    m = list(motivumok)[:3] or list(ALAP_MOTIVUMOK.values())[:3]
    poz = [(8, 10, 34, -18), (70, 44, 30, 22), (22, 78, 26, 8), (86, 100, 22, -30)]
    g_ = []
    for i, (x, y, s, r) in enumerate(poz):
        belso = m[i % len(m)]
        belso = belso if belso.strip().startswith("<") else f'<path d="{belso}"/>'
        g_.append(f'<g transform="translate({x} {y}) rotate({r} {s/2} {s/2}) scale({s/100})">{belso}</g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {meret} {meret}" width="{meret}" height="{meret}">'
           + "".join(g_) + "</svg>")
    return svg_uri(svg).replace('"', "'")


# ------------------------------------------------------------------ kisegítő HTML-darabok

def attr_id(s):
    return re.sub(r"[^a-z0-9-]", "-", str(s).lower())
