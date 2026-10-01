# -*- coding: utf-8 -*-
"""A VÉGLEGES OLDAL: az arculat.json + a választás (valasztas.json) alapján csak a kiválasztott elemekből
épít egy statikus, önálló HTML-t (+ DESIGN-RENDSZER.md, tokenek.css)."""
import json, re, datetime
from pathlib import Path
from . import alap, epito
from .alap import esc, g
from .css_alap import ALAP_CSS
from .futas_js import FUTAS_JS
from .epito import SZEKCIOK, STILUS_KATOK, KAT_NEV
from .stilusok import GLOBALIS

EXTRA_CSS = r"""
html{scroll-behavior:smooth;scroll-padding-top:90px}
body{margin:0;background:var(--c-paper)}
.ph.nincsfoto{background:repeating-linear-gradient(45deg,var(--c-tint) 0 10px,var(--c-card) 10px 20px);display:grid;place-items:center}
.ph.nincsfoto span{font:700 .7rem/1 ui-monospace,monospace;letter-spacing:.14em;color:var(--c-ink-3)}
.logo-szoveg{font-family:var(--f-display);font-weight:var(--w-display);font-size:1.3rem;color:var(--c-head)}
.skip{position:absolute;left:-999px;top:0;background:#000;color:#fff;padding:10px 14px;z-index:9999}
.skip:focus{left:10px;top:10px}
"""


def valasztas_olvas(ut, opc):
    """valasztas.json VAGY a teljes bemásolt visszajelzés-szöveg (a GÉPI ADAT sort kikeresi)."""
    s = Path(ut).read_text(encoding="utf-8")
    m = re.search(r'\{"marka".*\}\s*$', s.strip(), re.S)
    d = json.loads(m.group(0) if m else s)
    val = d.get("valasztas", d)
    out = {}
    for kat, o in opc.items():
        v = val.get(kat) or {}
        out[kat] = v.get("vegleges") or v.get("elonezet") or v.get("ajanlott") or o["ajanlott"]
    return out, d


def epit(spec, valasztas, ki, md_ki=None):
    opc = epito.opciok(spec)
    for h in epito.ellenoriz(opc, spec):
        print("  ! szabvány:", h)
    if isinstance(valasztas, (str, Path)):
        V, nyers = valasztas_olvas(valasztas, opc)
    else:
        V, nyers = dict(valasztas), {}
    for kat in opc:
        V.setdefault(kat, opc[kat]["ajanlott"])
    logo_info, logo_css = epito.logo_elokeszit(spec)
    ctx = epito.ctx_keszit(spec, logo_info)
    pal = next(p for p in opc["paletta"]["lista"] if p["id"] == V["paletta"])
    bet = next(b for b in opc["betu"]["lista"] if b["id"] == V["betu"])
    tok = alap.paletta_tokenek(pal)
    btok = alap.betu_tokenek(bet)
    sorrend = epito.szekcio_sorrend(spec)
    reszek = []
    for slot in sorrend:
        if slot not in SZEKCIOK:
            continue
        x = next((y for y in opc[slot]["lista"] if y["id"] == V[slot]), None)
        if x:
            reszek.append(epito.render_szekcio(x, ctx))
    reszek = epito.ritmus(reszek)
    body = "\n".join(reszek)
    _n = [0]

    def _hn(m):
        _n[0] += 1
        return f'<div class="hat{m.group(1)}" data-hn="{(_n[0] - 1) % 3}"'
    body = re.sub(r'<div class="hat( masod)?"', _hn, body)   # váltakozó szekcióhatárokhoz (data-hn 0/1/2)
    hasznalt = set(re.findall(r'class="ph f-([\w-]+)', body)) | set(re.findall(r'data-gal="f-([\w-]+)"', body))
    csak = {k: V[k] for k in list(GLOBALIS) + list(SZEKCIOK)}
    css = "\n".join([ALAP_CSS, EXTRA_CSS, epito.motivum_css(spec), logo_css,
                     epito.stilus_css_osszes(opc, csak), epito.szekcio_css_osszes(opc, csak),
                     epito.ikonok_css(spec, csak_stilus=V.get("ikon")), epito.fotok_css(spec, csak=hasznalt, max_px=1600),
                     spec.get("egyedi_css", "")])
    root = ":root{" + alap.tokenek_css(tok) + ";" + alap.tokenek_css(btok) + "}"
    furl = alap.google_fonts_url([bet.get(k) for k in ("display", "body", "hand", "label") if bet.get(k)])
    attrs = " ".join(f'data-{k}="{esc(V[k])}"' for k in STILUS_KATOK)
    m = spec.get("marka", {})
    seo = spec.get("seo", {})
    cim = seo.get("title") or f'{m.get("nev", "")} · {m.get("szlogen", "")}'.strip(" ·")
    leiras = seo.get("description") or g(spec, "hero", "lead") or ""
    leiras = re.sub(r"==|\*\*", "", leiras)
    html = f"""<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(cim)}</title><meta name="description" content="{esc(leiras[:300])}">
<meta property="og:title" content="{esc(cim)}"><meta property="og:description" content="{esc(leiras[:300])}"><meta property="og:type" content="website">
{f'<link rel="canonical" href="{esc(m["url"])}">' if m.get("url") else ''}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{f'<link rel="stylesheet" href="{esc(furl)}">' if furl else ''}
<style>{css}
{root}</style>
<noscript><style>[data-rv]{{opacity:1!important;transform:none!important;clip-path:none!important}}</style></noscript>
</head><body><a class="skip" href="#top">Ugrás a tartalomra</a>
<div class="elo-root" {attrs}>
{body}
</div>
<script>{FUTAS_JS}
WAG.NYITVA = {json.dumps(g(spec, "kapcsolat", "nyitva_gep") or None)};
if (/[?&]mozdulatlan=1/.test(location.search)) document.documentElement.classList.add('noanim');
WAG.init(document.querySelector('.elo-root'), document.documentElement.classList.contains('noanim'));</script>
</body></html>"""
    Path(ki).write_text(html, encoding="utf-8")
    if md_ki:
        Path(md_ki).write_text(design_md(spec, opc, V, tok, btok, nyers), encoding="utf-8")
        (Path(md_ki).parent / "tokenek.css").write_text(root.replace(";", ";\n  ").replace("{", "{\n  ") + "\n", encoding="utf-8")
    return len(html), V


def design_md(spec, opc, V, tok, btok, nyers):
    def nev(kat):
        x = next((y for y in opc[kat]["lista"] if y["id"] == V[kat]), {})
        return f'{V[kat].upper()} „{x.get("nev", "")}”'
    pal = next(p for p in opc["paletta"]["lista"] if p["id"] == V["paletta"])
    bet = next(b for b in opc["betu"]["lista"] if b["id"] == V["betu"])
    s = [f'# {g(spec, "marka", "nev")} · designrendszer', "",
         f'Készült: {datetime.date.today().isoformat()} · forrás: {g(spec, "marka", "url")} · az arculat-választó v{spec.get("verzio", 1)} döntései alapján.',
         "", "Ez a dokumentum a márka webes arculatának összefoglalója: bármely AI vagy fejlesztő ebből tud új oldalt,",
         "aloldalt vagy anyagot készíteni, ami ugyanúgy néz ki. A pontos értékek a `tokenek.css`-ben vannak.", "",
         "## 1. Színek", "", f'Paletta: **{nev("paletta")}**. {pal.get("miert", "")}', "",
         "| Szerep | Token | Érték |", "|---|---|---|"]
    for k, sz in [("--c-primary", "Fő márkaszín (gombok, kiemelés)"), ("--c-primary-d", "Fő szín, sötét (hover, talp)"),
                  ("--c-accent", "Kiemelő szín (marker, pöttyök, matricák)"), ("--c-accent2", "Harmadik szín (apró díszek)"),
                  ("--c-paper", "Oldal alapháttér"), ("--c-card", "Kártya / tiszta blokk"), ("--c-tint", "Halvány márkaszínű felület"),
                  ("--c-sand", "Meleg, mélyebb felület"), ("--c-deep", "Sötét felület (lábléc, tábla)"), ("--c-ink", "Szöveg"),
                  ("--c-ink-2", "Másodlagos szöveg"), ("--c-line", "Hajszálvonal")]:
        s.append(f"| {sz} | `{k}` | `{tok.get(k, '')}` |")
    s += ["", "Szabály: a sötét felület a márkaszín felé húzott mély tónus, nem tiszta fekete. Két egymás melletti szekció",
          "soha nem ugyanolyan felületű (paper → white → tint → sand → deep ritmus).", "",
          "## 2. Tipográfia", "", f'Betűpár: **{nev("betu")}**. {bet.get("miert", "")}', "",
          f'- Cím: **{bet.get("display")}** ({btok["--w-display"]}, sorköz {btok["--lh-display"]}, betűköz {btok["--ls-display"]}'
          f'{", NAGYBETŰS" if bet.get("nagybetus") else ""})',
          f'- Szöveg: **{bet.get("body")}**', f'- Kézírás-akcent: **{bet.get("hand", "-")}** (jegyzetek, aláírás, kiemelt szó)',
          f'- Címke / adat: **{bet.get("label", "-")}** (mono: idő, ár, apró címkék)',
          "- Méretek: hero `clamp(2.35rem, 5.5cqi, 4.85rem)`, H2 `clamp(1.8rem, 3.5cqi, 3.05rem)`, H3 `clamp(1.1rem, 1.55cqi, 1.34rem)`, törzs 1.02rem / 1.62.",
          "- Google Fonts, mind ellenőrizve magyar ékezetre (ő, ű).", "", "## 3. Komponensek (a választott változatok)", ""]
    for kat in ["cim", "alcim", "gomb", "kartya", "foto", "ikon", "felulet", "dekor", "hatar", "mozgas"]:
        x = next((y for y in opc[kat]["lista"] if y["id"] == V[kat]), {})
        s.append(f'- **{KAT_NEV[kat][0]}:** {nev(kat)}. {x.get("miert") or x.get("leiras", "")}')
    s += ["", "## 4. Az oldal szerkezete", ""]
    for kat in epito.szekcio_sorrend(spec):
        if kat in SZEKCIOK:
            x = next((y for y in opc[kat]["lista"] if y["id"] == V[kat]), {})
            s.append(f'1. **{KAT_NEV[kat][0]}:** {nev(kat)}. {x.get("miert") or x.get("leiras", "")}')
    mot = spec.get("motivum", {})
    s += ["", "## 5. A márka saját világa (motívumok)", "",
          f'{g(spec, "profil", "motivumok")}', "",
          f'- Motívum-formák: {", ".join((mot.get("formak") or {}).keys())} (maszk-SVG-k az arculat.json-ban, a textúra és a dekor ezekből épül).',
          f'- Szellemszavak: {", ".join((mot.get("szellemszavak") or {}).values())}',
          f'- Futószalag-tények: {" · ".join(mot.get("ticker") or [])}',
          f'- Matricák: {" · ".join(mot.get("matricak") or [])}', "",
          "## 6. Szabályok", "",
          "- A tények (árak, nevek, nyitvatartás, számok) csak az ügyfél saját forrásából jöhetnek, betűre.",
          "- Ikon + cím egy sorban a kártyafejekben; ikon soha nem kap szöveget.",
          "- Fotók: `aspect-ratio` + `object-fit: cover` (háttérképként), soha nem fix magasság; valódi fotó, nem kivágott.",
          "- Gombok: egy szekcióban legfeljebb egy elsődleges gomb.",
          "- Mozgás: `prefers-reduced-motion` esetén minden áll; `?mozdulatlan=1` a képernyőképekhez.",
          "- Tilos: lila-kék AI-gradiens, emoji a saját szövegben, hosszú gondolatjel a saját szövegben, kitalált vélemény.", ""]
    if nyers:
        mj = []
        for kat, v in (nyers.get("valasztas") or {}).items():
            for oid, t in (v.get("megjegyzesek") or {}).items():
                mj.append(f'- {KAT_NEV.get(kat, (kat,))[0]} / {oid.upper()}: {t}')
        if mj or nyers.get("altalanos"):
            s += ["## 7. Az ügyfél megjegyzései a választáskor", ""] + mj
            if nyers.get("altalanos"):
                s.append(f'- Általános: {nyers["altalanos"]}')
            s.append("")
    return "\n".join(s)
