# -*- coding: utf-8 -*-
"""Közös előkészítés: arculat.json beolvasása, opciók normalizálása, fotók/logó/ikonok beágyazása CSS-osztályként
(minden eszköz PONTOSAN EGYSZER kerül a fájlba), motívum-változók."""
import json, re
from pathlib import Path
from . import alap
from .alap import esc, g
from .stilusok import GLOBALIS, css_for, ZAJ
from .szekciok_a import NAV, HERO, TENYEK, KINALAT, AJANLAT
from .szekciok_b import FOLYAMAT, TORTENET, GALERIA, LATOGATAS, LABLEC

SZEKCIOK = {
    "nav": (NAV, "Navigáció (fejléc)", "A felső menüsáv: logó, menüpontok, fő gomb."),
    "hero": (HERO, "Hero (nyitó blokk)", "Az első képernyő: ez dönti el, marad-e a látogató."),
    "tenyek": (TENYEK, "Tények / bizalom", "A hero alatti gyors bizonyítékok: miért ti."),
    "kinalat": (KINALAT, "Kínálat", "A fő termék- vagy szolgáltatáscsoportok bemutatása."),
    "ajanlat": (AJANLAT, "Kiemelt tételek árakkal", "Néhány konkrét termék vagy csomag, árral."),
    "folyamat": (FOLYAMAT, "Folyamat (így működik)", "A lépések, ahogy a vevő megkapja, amit szeretne."),
    "tortenet": (TORTENET, "Rólunk / történet", "Az emberek és a történet a márka mögött."),
    "galeria": (GALERIA, "Galéria", "Hangulat: a hely, a termékek, az emberek."),
    "latogatas": (LATOGATAS, "Kapcsolat / látogatás", "A záró blokk: hol, mikor, hogyan érsz el minket."),
    "lablec": (LABLEC, "Lábléc", "Az oldal alja: elérhetőség, menü, jogi linkek."),
}
ALAP_SORREND = ["nav", "hero", "tenyek", "kinalat", "ajanlat", "folyamat", "tortenet", "galeria", "latogatas", "lablec"]
STILUS_KATOK = ["cim", "alcim", "gomb", "kartya", "foto", "felulet", "dekor", "hatar", "mozgas", "ikon"]

# Az arculati elemek csoportjai (mindig ugyanez a 12 kategória). A szekció-kategóriák NEM fixek: mindig a beadott
# oldal szekciói (spec.szekcio_sorrend), lásd csoportok(spec).
ALAP_CSOPORTOK = [
    ("Alapok", ["paletta", "betu", "ikon"]),
    ("Tipográfia", ["cim", "alcim"]),
    ("Elemek", ["gomb", "kartya", "foto"]),
    ("Felületek és díszítés", ["felulet", "dekor", "hatar", "mozgas"]),
]
CSOPORTOK = ALAP_CSOPORTOK + [("Szekciók", ALAP_SORREND)]   # visszafelé-kompatibilis alapértelmezés
# A textúra, a dekor és a szekcióhatár ötletei MINDIG az ügyfél fő témájából jönnek (egyedi_opciok), nem a könyvtárból.
TEMA_KATOK = ["felulet", "dekor", "hatar"]
KAT_NEV = {"paletta": ("Színpaletta", "A márka színei: fő szín, kiemelő, felületek, szöveg."),
           "betu": ("Betűpár", "Cím-betű + szöveg-betű (+ kézírás és címke-betű). Mind magyar ékezetbiztos."),
           "ikon": ("Ikonstílus", "Az egyedi, generált ikonok rajzstílusa. Ugyanazok az ikonok 5 stílusban.")}
for k, (_, n, l) in GLOBALIS.items():
    KAT_NEV[k] = (n, l)
for k, (_, n, l) in SZEKCIOK.items():
    KAT_NEV[k] = (n, l)

# A SZABVÁNY: a 12 arculati kategória + a beadott oldal minden szekciója, kategóriánként (legalább) 5 opcióval.
SZABVANY = [k for _, ks in CSOPORTOK for k in ks]
MIN_OPCIO = 5


def szekcio_sorrend(spec):
    return spec.get("szekcio_sorrend") or ALAP_SORREND


def csoportok(spec):
    """A választó kategória-csoportjai erre az oldalra: 12 arculati elem + az oldal saját szekciói."""
    return ALAP_CSOPORTOK + [("Szekciók", [s for s in szekcio_sorrend(spec) if s in SZEKCIOK])]


def szabvany(spec):
    return [k for _, ks in csoportok(spec) for k in ks]


def egyedi_szekciok_regisztral(spec):
    """Ad-hoc szekció-típusok (pl. egy sales oldal legókockái): spec.egyedi_szekciok = {slot: {nev, leiras}}.
    Könyvtári elrendezésük nincs, az 5 változat az egyedi_opciok.<slot> listából jön."""
    for slot, d in (spec.get("egyedi_szekciok") or {}).items():
        if slot not in SZEKCIOK:
            SZEKCIOK[slot] = ([], d.get("nev", slot), d.get("leiras", ""))
        KAT_NEV[slot] = (d.get("nev", slot), d.get("leiras", ""))
UI_IKONOK = {"tel", "pin", "ora", "mail", "nyil", "le", "pipa", "csillag", "fb", "ig", "menu", "plusz", "bal", "jobb",
             "szem", "szoveg", "haz", "kulcs"}

# Kulcs nélküli tartalék: ha nincsenek generált ikonok, az ikon-kategória a márka saját motívum-formáiból épül
# (5 kezelés), így a választó szerkezete akkor is ugyanaz. A valódi, tárgyat ábrázoló ikonokhoz OpenAI-kulcs kell.
TARTALEK_IKON = [
    dict(id="iT1", nev="Márkaforma, telt", miert="A márka saját formái telt, egyszínű jelként. (Tartalék: generált ikonokhoz OpenAI-kulcs kell.)",
         css="%S .ik{position:relative;background:none!important;padding:0!important}%S .ik::before{content:\"\";position:absolute;inset:8%;background:var(--c-primary);-webkit-mask:var(--ikm) center/contain no-repeat;mask:var(--ikm) center/contain no-repeat}"),
    dict(id="iT2", nev="Márkaforma körben", miert="Halvány körben ülő telt forma. Nyugodt, rendezett. (Tartalék.)",
         css="%S .ik{position:relative;border-radius:50%;background:var(--c-primary-ll)!important;padding:0!important}%S .ik::before{content:\"\";position:absolute;inset:22%;background:var(--c-primary);-webkit-mask:var(--ikm) center/contain no-repeat;mask:var(--ikm) center/contain no-repeat}"),
    dict(id="iT3", nev="Márkaforma kontúrgyűrűben", miert="Vékony színes gyűrű, benne a forma kiemelő színben. Könnyed, grafikus. (Tartalék.)",
         css="%S .ik{position:relative;border-radius:50%;background:none!important;box-shadow:inset 0 0 0 3px var(--c-accent);padding:0!important}%S .ik::before{content:\"\";position:absolute;inset:24%;background:var(--c-accent2);-webkit-mask:var(--ikm) center/contain no-repeat;mask:var(--ikm) center/contain no-repeat}"),
    dict(id="iT4", nev="Márkaforma-matrica", miert="Színes, fehér szegélyes matrica a formával. Játékos, kézzelfogható. (Tartalék.)",
         css="%S .ik{position:relative;border-radius:30%;background:var(--c-accent)!important;box-shadow:0 0 0 4px #fff,var(--sh-2);padding:0!important;transform:rotate(-6deg)}%S .ik::before{content:\"\";position:absolute;inset:22%;background:var(--c-on-accent);-webkit-mask:var(--ikm) center/contain no-repeat;mask:var(--ikm) center/contain no-repeat}"),
    dict(id="iT5", nev="Márkaforma-pecsét", miert="Sötét, kettős szegélyű pecsét a formával. Kézműves, „minősített”. (Tartalék.)",
         css="%S .ik{position:relative;border-radius:50%;background:var(--c-deep)!important;box-shadow:inset 0 0 0 4px var(--c-deep),inset 0 0 0 6px var(--c-deep-hl);padding:0!important}%S .ik::before{content:\"\";position:absolute;inset:26%;background:var(--c-deep-hl);-webkit-mask:var(--ikm) center/contain no-repeat;mask:var(--ikm) center/contain no-repeat}"),
]


def betolt(ut):
    ut = Path(ut)
    spec = json.loads(ut.read_text(encoding="utf-8"))
    spec["_alap"] = ut.parent
    egyedi_szekciok_regisztral(spec)
    return spec


def _kat_beall(spec, kat):
    o = g(spec, "opciok", kat) or {}
    if isinstance(o, list):
        o = {"lista": o}
    return o


def opciok(spec):
    """Kategóriánként: [{'id','nev','miert','css'?, 'render'?, 'html'?}], ajánlott id."""
    out = {}
    # paletta, betű: a spec adja teljes egészében
    for kat in ("paletta", "betu"):
        o = _kat_beall(spec, kat)
        lst = [dict(x) for x in o.get("lista", [])]
        aj = o.get("ajanlott") or next((x["id"] for x in lst if x.get("ajanlott")), lst[0]["id"] if lst else None)
        out[kat] = {"lista": lst, "ajanlott": aj}
    # ikon: az ikon-spec stílusai
    isp = ikon_spec(spec)
    o = _kat_beall(spec, "ikon")
    if ikon_tartalek_kell(spec):
        lst = [dict(x) for x in TARTALEK_IKON]
        out["ikon"] = {"lista": lst, "ajanlott": "iT2", "tartalek": True}
    else:
        lst = [{"id": s["id"], "nev": s.get("nev", s["id"]), "miert": g(o, "miert", s["id"]) or s.get("miert", "")}
               for s in (isp.get("stilusok") or [])]
        aj = o.get("ajanlott") if o.get("ajanlott") in [x["id"] for x in lst] else (lst[0]["id"] if lst else None)
        out["ikon"] = {"lista": lst, "ajanlott": aj}
    # globális stílusok + szekciók: könyvtár + egyedi
    egyedi = spec.get("egyedi_opciok") or {}
    for kat, forras in list(GLOBALIS.items()) + list(SZEKCIOK.items()):
        konyvtar = {x["id"]: x for x in forras[0]}
        for e in egyedi.get(kat, []):
            konyvtar[e["id"]] = dict(e, egyedi=True)
        o = _kat_beall(spec, kat)
        ids = o.get("lista") or [x["id"] for x in forras[0]] + [e["id"] for e in egyedi.get(kat, [])]
        lst = []
        for i in ids:
            if i not in konyvtar:
                print(f"  ! ismeretlen opció: {kat}/{i} (kihagyva)")
                continue
            x = dict(konyvtar[i])
            x["miert"] = g(o, "miert", i) or x.get("leiras", "")
            lst.append(x)
        aj = o.get("ajanlott") or (lst[0]["id"] if lst else None)
        out[kat] = {"lista": lst, "ajanlott": aj}
    return out


def ikon_spec(spec):
    p = g(spec, "ikonok", "spec")
    if not p:
        return {}
    f = Path(spec["_alap"]) / p
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
        d["_mappa"] = f.parent / d.get("mappa", "ikonok")
        return d
    except Exception:
        return {}


def ikon_nevek(spec):
    """Az oldalon használt (generált) ikonok nevei: az ikon-specből, vagy a tartalomból összeszedve."""
    isp = ikon_spec(spec)
    if isp.get("ikonok"):
        return [x["nev"] for x in isp["ikonok"]]
    nevek = []

    def jar(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k == "ikon" and isinstance(v, str) and v not in UI_IKONOK and v not in nevek:
                    nevek.append(v)
                else:
                    jar(v)
        elif isinstance(d, list):
            for v in d:
                jar(v)
    for kulcs in ("hero", "tenyek", "kinalat", "ajanlat", "folyamat", "tortenet", "latogatas"):
        jar(spec.get(kulcs))
    return nevek


def ikon_tartalek_kell(spec):
    isp = ikon_spec(spec)
    if not isp.get("stilusok") or not isp.get("ikonok"):
        return True
    return not any((isp["_mappa"] / st["id"] / f'{ik["nev"]}.png').exists() for st in isp["stilusok"] for ik in isp["ikonok"])


def ellenoriz(opc, spec):
    """A szabvány kikényszerítése: minden kategória, min. 5 opció, érvényes ajánlott, minden szekció a sorrendben,
    és a szekciókhoz van tartalom. Visszaad: a hibák listája (üres = rendben)."""
    hiba = []
    for kat in szabvany(spec):
        o = opc.get(kat) or {}
        n = len(o.get("lista") or [])
        if n < MIN_OPCIO:
            hiba.append(f"{KAT_NEV[kat][0]} ({kat}): {n} opció, legalább {MIN_OPCIO} kell.")
        ids = [x["id"] for x in o.get("lista") or []]
        if o.get("ajanlott") not in ids:
            hiba.append(f"{KAT_NEV[kat][0]} ({kat}): az ajánlott opció ({o.get('ajanlott')}) nincs a listában.")
    sor = szekcio_sorrend(spec)
    if not [s for s in sor if s in SZEKCIOK]:
        hiba.append("A szekcio_sorrend üres: a beadott oldal szekcióit sorold fel (nav, hero, …, vagy egyedi_szekciok).")
    for kat in TEMA_KATOK:
        for x in (opc.get(kat) or {}).get("lista") or []:
            if not x.get("egyedi"):
                hiba.append(f"{KAT_NEV[kat][0]} ({kat}) / {x['id']}: könyvtári opció. A textúra, a dekor és a határ 5 ötlete "
                            f"az ügyfél fő témájából kell jöjjön (egyedi_opciok.{kat}).")
    kell = {"hero": ("cim",), "tenyek": ("elemek",), "kinalat": ("elemek",), "ajanlat": ("elemek",),
            "folyamat": ("lepesek",), "tortenet": ("bekezdesek",), "galeria": ("fotok",), "latogatas": ("cim",)}
    for slot, mezok in kell.items():
        if slot not in sor:
            continue
        for m in mezok:
            if not g(spec, slot, m):
                hiba.append(f"Hiányzik a tartalom: {slot}.{m} (vezesd le a tényekből, ne hagyd ki a szekciót).")
    if not g(spec, "kapcsolat", "telefon") and not g(spec, "kapcsolat", "email"):
        hiba.append("Hiányzik a kapcsolat (legalább telefon vagy e-mail).")
    return hiba


def fotok_css(spec, csak=None, max_px=1280):
    css = []
    for fid, f in (spec.get("fotok") or {}).items():
        if csak is not None and fid not in csak:
            continue
        src = f.get("fajl") or ""
        if src.startswith("http"):
            uri = src
        else:
            p = Path(spec["_alap"]) / src
            if not p.exists():
                print(f"  ! hiányzó fotó: {src}")
                continue
            uri = alap.data_uri(p, max_px=f.get("max", max_px), minoseg=f.get("minoseg", 78))
        css.append(f'.f-{fid}{{background-image:url("{uri}")}}')
    return "\n".join(css)


def logo_elokeszit(spec):
    lg = spec.get("logo") or {}
    if not lg.get("fajl"):
        return None, ""
    p = Path(spec["_alap"]) / lg["fajl"]
    if not p.exists():
        print("  ! hiányzó logó:", p)
        return None, ""
    try:
        from PIL import Image
        with Image.open(p) as im:
            im = im.convert("RGBA")
            bb = im.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
            if bb and (bb[2] - bb[0]) * (bb[3] - bb[1]) < im.size[0] * im.size[1] * 0.97:
                im = im.crop(bb)
                vag = Path(spec["_alap"]) / ("_logo_vagott.png")
                im.save(vag)
                p = vag
            w, h = im.size
    except Exception:
        w, h = 1, 1
    eredeti = alap.data_uri(p, max_px=480, png=True)
    css = ['.lg{background-image:var(--logo-img)}', '.lg-feher{background-image:var(--logo-feher)}']
    info = {"ar": f"{w}/{h}", "feher": False}
    feher = lg.get("feher_fajl")
    try:
        if feher:
            fp = Path(spec["_alap"]) / feher
        else:
            fp = Path(spec["_alap"]) / "_logo_feher.png"
            alap.logo_feher(p, fp)
        feher_uri = alap.data_uri(fp, max_px=480, png=True)
        info["feher"] = True
    except Exception as ex:
        feher_uri = eredeti
        print("  ! fehér logó nem készült:", ex)
    css.insert(0, f':root{{--logo-eredeti:url("{eredeti}");--logo-feher:url("{feher_uri}");--logo-img:var(--logo-eredeti)}}')
    return info, "\n".join(css)


def ikonok_css(spec, csak_stilus=None):
    isp = ikon_spec(spec)
    if ikon_tartalek_kell(spec):
        css = []
        for i, nev in enumerate(ikon_nevek(spec)):
            css.append(f'.ik-{nev}{{--ikm:var(--m{i % 3 + 1})}}')
        for x in TARTALEK_IKON:
            if csak_stilus and x["id"] != csak_stilus:
                continue
            css.append(css_for("ikon", x) if not csak_stilus else x["css"].replace("%S ", ""))
        return "\n".join(css)
    css = []
    for st in isp.get("stilusok", []):
        if csak_stilus and st["id"] != csak_stilus:
            continue
        sel = f'[data-ikon="{st["id"]}"] ' if not csak_stilus else ""
        for ik in isp.get("ikonok", []):
            f = isp["_mappa"] / st["id"] / f'{ik["nev"]}.png'
            if f.exists():
                css.append(f'{sel}.ik-{ik["nev"]}{{background-image:url("{alap.data_uri(f, max_px=256, png=True)}")}}')
            else:
                css.append(f'{sel}.ik-{ik["nev"]}{{background:var(--c-primary-ll);border-radius:30%}}')
    return "\n".join(css)


def motivum_css(spec):
    m = g(spec, "motivum", "formak") or {}
    formak = list(m.values()) or list(alap.ALAP_MOTIVUMOK.values())[:3]
    while len(formak) < 3:
        formak.append(list(alap.ALAP_MOTIVUMOK.values())[len(formak)])
    jel = m.get(g(spec, "motivum", "jel") or "", formak[0])
    v = {"--m1": formak[0], "--m2": formak[1], "--m3": formak[2], "--mjel": jel}
    s = ";".join(f'{k}:url("{alap.motivum_uri(x)}")' for k, x in v.items())
    s += f';--minta:url("{alap.minta_csempe_uri(formak)}");--zaj:url("{ZAJ}")'
    return ".elo-root{" + s + "}"


def ctx_keszit(spec, logo_info):
    c = {k: v for k, v in spec.items() if not k.startswith("_")}
    c["fotok"] = spec.get("fotok") or {}
    c["_logo"] = logo_info
    ny = g(spec, "kapcsolat", "nyitvatartas") or []
    if ny and not g(spec, "kapcsolat", "nyitva_rovid"):
        c.setdefault("kapcsolat", {})["nyitva_rovid"] = " · ".join(f"{a} {b}" for a, b in ny[:2])
    return c


def stilus_css_osszes(opc, csak=None):
    out = []
    for kat in GLOBALIS:
        for x in opc[kat]["lista"]:
            if csak and csak.get(kat) != x["id"]:
                continue
            if x.get("css"):
                out.append(css_for(kat, x))
    return "\n".join(out)


def szekcio_css_osszes(opc, csak=None):
    out, seen = [], set()
    for kat in SZEKCIOK:
        for x in opc[kat]["lista"]:
            if csak and csak.get(kat) != x["id"]:
                continue
            c = x.get("css", "")
            if c and c not in seen:
                seen.add(c)
                out.append(c)
    return "\n".join(out)


def render_szekcio(x, ctx):
    if x.get("render"):
        return x["render"](ctx)
    return x.get("html", "")


def paletta_tokenek(opc):
    return {p["id"]: alap.paletta_tokenek(p) for p in opc["paletta"]["lista"]}


def betu_tokenek(opc):
    return {b["id"]: alap.betu_tokenek(b) for b in opc["betu"]["lista"]}


def betu_csaladok(lst):
    fam = []
    for b in lst:
        for k in ("display", "body", "hand", "label"):
            if b.get(k):
                fam.append(b[k])
    return fam


def ritmus(szekciok_html):
    """Ha két egymást követő szekció ugyanolyan felületű, a másodikat a párjára cseréli."""
    par = {"s-paper": "s-white", "s-white": "s-paper", "s-tint": "s-sand", "s-sand": "s-tint"}
    out, elozo = [], None
    for h in szekciok_html:
        m = re.search(r'class="sec [^"]*?\b(s-paper|s-white|s-tint|s-sand|s-deep|s-primary)\b', h[:400])
        f = m.group(1) if m else None
        if f and f == elozo and f in par:
            h = h.replace(f, par[f], 1)
            f = par[f]
        out.append(h)
        elozo = f
    return out
