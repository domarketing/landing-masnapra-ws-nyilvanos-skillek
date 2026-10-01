#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
szoveg_scan.py - a gepileg merheto AI-jelek kimutatasa magyar szovegben.

A szovegellenorzo skill resze. A jelek kb. felet fogja meg; a tobbi
(kimondott tanulsag, ures altalanositas, hitelesseg) itelet kerdese.

  python3 szoveg_scan.py fajl.md
  python3 szoveg_scan.py --html oldal.html
  cat szoveg.txt | python3 szoveg_scan.py -
  python3 szoveg_scan.py --json fajl.md
  python3 szoveg_scan.py --strict fajl.md     # 1-es kilepokod, ha van KOTELEZO hiba
"""
import argparse
import html as html_mod
import json
import re
import statistics
import sys
import unicodedata

# ------------------------------------------------------------------ szabalyok
# sulyok: "kotelezo" = 0 db-nak kell lennie, "eros" = eros jel, "gyenge" = figyelmeztetes
SZABALYOK = [
    {
        "id": "nem-x-hanem-y",
        "sulyy": "kotelezo",
        "cim": "„Nem X, hanem Y” szerkezet",
        "javitas": "Mondd ki simán az állítást, tagadó felvezetés nélkül.",
        "mintak": [
            r"\bnem ?(?:csupán|csak)\b[^.!?]{2,70}\bhanem\b",
            r"\bnemcsak\b[^.!?]{2,70}\bhanem\b",
        ],
    },
    {
        "id": "tagadas-felulíras",
        "sulyy": "kotelezo",
        "cim": "Rövid tagadás, majd drámai felülírás",
        "javitas": "Egy mondat, ami megmondja, mi az. A tagadó felvezetés kimarad.",
        "mondatpar": "tagadas",
    },
    {
        "id": "harom-tagadas",
        "sulyy": "eros",
        "cim": "„Nem X. Nem Y. Z.” három ütem",
        "javitas": "Egyetlen állító mondat.",
        "mondatpar": "ketto-nem",
    },
    {
        "id": "egyszavas-kerdes",
        "sulyy": "eros",
        "cim": "Egyszavas kérdés, rögtön válasszal",
        "javitas": "Írd egy kijelentő mondatba.",
        "mintak": [r"(?:^|[.!?]\s)[A-ZÁÉÍÓÖŐÚÜŰ][\wáéíóöőúüű]{1,16}\?\s+[A-ZÁÉÍÓÖŐÚÜŰ]"],
    },
    {
        "id": "ures-atvezetes",
        "sulyy": "eros",
        "cim": "Üres átvezetés",
        "javitas": "Töröld. A következő mondat önmagában is megáll.",
        "mintak": [r"\b(itt jön a lényeg|most jön a java|és most jön a|a lényeg a következő)\b"],
    },
    {
        "id": "megjatszott-kozvetlenseg",
        "sulyy": "eros",
        "cim": "Megjátszott közvetlenség",
        "javitas": "Töröld a felvezetést, a mondat marad.",
        "mintak": [r"\b(Őszintén\?|Valljuk be|Legyünk őszinték|Bevallom,|Hadd legyek őszinte)"],
    },
    {
        "id": "ures-mondatveg",
        "sulyy": "eros",
        "cim": "Üres mondatvég általános tanulsággal",
        "javitas": "Töröld a mondat végét. A tény önmagában elég.",
        "mintak": [
            r"\b(ami jól mutatja|ami rávilágít|ami jól szemlélteti|ezzel is bizonyítva|"
            r"ami azt bizonyítja|ami jól tükrözi|rámutatva arra)\b",
        ],
    },
    {
        "id": "marketinges-felfujas",
        "sulyy": "eros",
        "cim": "Marketinges felfújás",
        "javitas": "Írd le, mi történik, hétköznapi magyarul.",
        "mintak": [
            r"\b(forradalmi|egyedülálló módon|letisztult megoldás|hatékonyságnövel\w*|"
            r"innovatív megoldás|piacvezető megoldás|szinergi\w+|proaktív\w*|"
            r"felhasználóbarát módon|kulcsfontosságú szerepet)\b",
        ],
    },
    {
        "id": "emoji",
        "sulyy": "kotelezo",
        "cim": "Emoji",
        "javitas": "Törlendő. Helyette ikon vagy semmi.",
        "karakter": "emoji",
    },
    {
        "id": "hosszu-kotojel",
        "sulyy": "kotelezo",
        "cim": "Hosszú kötőjel (em vagy en dash)",
        "javitas": "Sima kötőjel vagy vessző.",
        "karakter": "dash",
    },
    {
        "id": "idegen-idezojel",
        "sulyy": "gyenge",
        "cim": "Idegen idézőjel",
        "javitas": "Magyar idézőjel: „így”.",
        "karakter": "idezo",
    },
    {
        "id": "felkialtojel",
        "sulyy": "gyenge",
        "cim": "Felkiáltójel a törzsszövegben",
        "javitas": "Pont. A hangsúlyt a mondat adja.",
        "mintak": [r"!"],
    },
    {
        "id": "azonos-kezdet",
        "sulyy": "eros",
        "cim": "Két szomszédos mondat azonos szóval indul",
        "javitas": "Írd át az egyiket.",
        "mondatpar": "azonos-kezdet",
    },
]


def szoveg_kinyer(nyers, html=False):
    if html:
        nyers = re.sub(r"<(script|style)\b.*?</\1>", " ", nyers, flags=re.S | re.I)
        nyers = re.sub(r"<!--.*?-->", " ", nyers, flags=re.S)
        nyers = re.sub(r"data:[^\"')]+", " ", nyers)
        nyers = re.sub(r"<[^>]+>", " ", nyers)
        nyers = html_mod.unescape(nyers)
    return re.sub(r"[ \t]+", " ", nyers)


def mondatokra(t):
    return [m.strip() for m in re.split(r"(?<=[.!?])\s+", t) if len(m.strip().split()) > 0]


def vizsgal(t):
    mondat = mondatokra(t)
    hossz = [len(m.split()) for m in mondat] or [0]
    talalatok = []

    for sz in SZABALYOK:
        db, peldak = 0, []
        if "mintak" in sz:
            for p in sz["mintak"]:
                for m in re.finditer(p, t, re.I):
                    db += 1
                    if len(peldak) < 3:
                        a, b = max(0, m.start() - 45), min(len(t), m.end() + 45)
                        peldak.append("..." + t[a:b].replace("\n", " ").strip() + "...")
        if sz.get("karakter") == "emoji":
            e = [c for c in t if ord(c) > 0x2100 and unicodedata.category(c) in ("So", "Sk")]
            db, peldak = len(e), sorted(set(e))[:6]
        if sz.get("karakter") == "dash":
            db = sum(t.count(c) for c in "—–‒―")
        if sz.get("karakter") == "idezo":
            # A magyar idezojel: „igy”. A ZARO (U+201D) ugyanaz a karakter, mint az
            # angol zaro idezojel, ezert azt NEM szabad idegennek szamolni: minden
            # helyesen tordelt magyar idezet tartalmazza.
            # Idegen, ami itt marad: egyenes " (U+0022), angol nyito “ (U+201C),
            # angol nyito egyszeres ‘ (U+2018).
            # SZANDEKOSAN NINCS benne: ’ (U+2019), mert az a magyar aposztrof es a
            # magyar egyszeres par zaro tagja (‚...’); tovabba « », mert a magyar
            # az idezeten beluli idezetet »igy« formaban jeloli.
            db = sum(t.count(c) for c in '"\u201c\u2018')
        if sz.get("mondatpar") == "tagadas":
            for i in range(len(mondat) - 1):
                a, b = mondat[i], mondat[i + 1]
                if (len(a.split()) <= 10 and re.search(r"\bnem\b", a, re.I)
                        and re.match(r"^(Ez|Az|Egy|Itt|Ő)\b", b) and len(b.split()) <= 16):
                    db += 1
                    if len(peldak) < 3:
                        peldak.append(a + " " + b)
        if sz.get("mondatpar") == "ketto-nem":
            for i in range(len(mondat) - 1):
                if (mondat[i].lower().startswith("nem")
                        and mondat[i + 1].lower().startswith("nem")):
                    db += 1
                    if len(peldak) < 3:
                        peldak.append(mondat[i] + " " + mondat[i + 1])
        if sz.get("mondatpar") == "azonos-kezdet":
            for i in range(len(mondat) - 1):
                a, b = mondat[i].split(), mondat[i + 1].split()
                if a and b:
                    x, y = a[0].strip(",.:;").lower(), b[0].strip(",.:;").lower()
                    if x == y and len(x) > 2:
                        db += 1
                        if len(peldak) < 3:
                            peldak.append(mondat[i][:60] + " / " + mondat[i + 1][:60])
        if db:
            talalatok.append({"id": sz["id"], "suly": sz["sulyy"], "cim": sz["cim"],
                              "db": db, "javitas": sz["javitas"], "peldak": peldak})

    toredek = sum(1 for h in hossz if h <= 3)
    return {
        "mondat": len(mondat),
        "szo": len(t.split()),
        "atlag_hossz": round(statistics.mean(hossz), 1),
        "median_hossz": round(statistics.median(hossz), 1),
        "toredek_db": toredek,
        "toredek_szazalek": round(100 * toredek / max(1, len(mondat)), 1),
        "talalatok": talalatok,
    }


def kiir(e, nev):
    print("=" * 66)
    print("  %s" % nev)
    print("=" * 66)
    print("  %d mondat · %d szó · átlag %.1f szó · medián %.1f szó"
          % (e["mondat"], e["szo"], e["atlag_hossz"], e["median_hossz"]))

    def sor(cimke, ertek, rendben, cel):
        jel = "OK  " if rendben else "!!  "
        print("  %s%-36s %-12s cél: %s" % (jel, cimke, ertek, cel))

    print()
    sor("Töredékmondat (max 3 szó)", "%d db / %.0f%%" % (e["toredek_db"], e["toredek_szazalek"]),
        e["toredek_szazalek"] <= 10, "10% alatt")
    sor("Mondathossz mediánja", "%.1f szó" % e["median_hossz"],
        12 <= e["median_hossz"] <= 16, "12-16 szó")

    kot = [t for t in e["talalatok"] if t["suly"] == "kotelezo"]
    ero = [t for t in e["talalatok"] if t["suly"] == "eros"]
    gye = [t for t in e["talalatok"] if t["suly"] == "gyenge"]

    for cim, lista in (("KÖTELEZŐ javítani", kot), ("Erős jel", ero), ("Figyelmeztetés", gye)):
        if not lista:
            continue
        print("\n  --- %s ---" % cim)
        for t in lista:
            print("  !!  %-40s %d db" % (t["cim"], t["db"]))
            print("      %s" % t["javitas"])
            for p in t["peldak"]:
                print("      > %s" % (p[:150] if isinstance(p, str) else p))

    print()
    if kot:
        print("  EREDMÉNY: NEM adható le. %d kötelező hiba." % sum(t["db"] for t in kot))
    elif ero:
        print("  EREDMÉNY: leadható, de %d erős jel maradt benne." % sum(t["db"] for t in ero))
    else:
        print("  EREDMÉNY: a gépileg mérhető jelek rendben.")
    print("  (A kimondott tanulság, az üres általánosítás és a hitelesség nem mérhető gépileg.)")
    return 1 if kot else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fajlok", nargs="+")
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    kod = 0
    for f in a.fajlok:
        nyers = sys.stdin.read() if f == "-" else open(f, encoding="utf-8", errors="replace").read()
        html = a.html or f.lower().endswith((".html", ".htm"))
        e = vizsgal(szoveg_kinyer(nyers, html))
        if a.json:
            print(json.dumps({"fajl": f, **e}, ensure_ascii=False, indent=1))
            if any(t["suly"] == "kotelezo" for t in e["talalatok"]):
                kod = 1
        else:
            kod = max(kod, kiir(e, "stdin" if f == "-" else f))
    sys.exit(kod if a.strict else 0)
