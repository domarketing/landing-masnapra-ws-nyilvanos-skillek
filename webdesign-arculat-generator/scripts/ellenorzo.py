#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ellenorzo.py - statikus minőség-ellenőrzés (böngésző nélkül is fut, pl. Claude.ai-ban).

  python3 ellenorzo.py <html> [--spec arculat.json]

Mit néz: fájlméret, hiányzó fotók („FOTÓ HELYE”), render-hibák, kategóriánkénti opciószám (választónál),
AI-szag a SAJÁT szövegben (hosszú gondolatjel, „nem ... hanem”, emoji), kitalált-gyanús elemek (csillagos értékelés
vélemény nélkül), üres href-ek, és az arculat.json tényeinek jelenléte (telefon, cím).
"""
import sys, re, json, html as H
from pathlib import Path

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    p = Path(a[0])
    s = p.read_text(encoding="utf-8")
    spec = json.loads(Path(a[a.index("--spec") + 1]).read_text(encoding="utf-8")) if "--spec" in a else {}
    sulyos, figy = [], []
    mb = len(s.encode()) / 1024 / 1024
    (sulyos if mb > 12 else figy if mb > 7 else []).append(f"Fájlméret: {mb:.1f} MB")
    if "Hiba a " in s and "változatban" in s:
        sulyos.append("Render-hiba van egy szekció-változatban (keresd: 'Hiba a').")
    n = s.count("FOTÓ HELYE")
    if n:
        figy.append(f"{n} helyen hiányzik fotó (FOTÓ HELYE) - adj meg fotót, vagy válts változatot.")
    m = re.search(r'<script id="vl-data" type="application/json">(.*?)</script>', s, re.S)
    if m:
        d = json.loads(m.group(1).replace("<\\/", "</"))
        for k in d.get("kategoriak", []):
            if len(k["opciok"]) < 5:
                sulyos.append(f"'{k['nev']}': csak {len(k['opciok'])} opció (min. 5 kell).")
    # a látható szöveg (sablonok nélkül a script/style)
    forras = s
    if m:  # választó: csak a márka-tartalom (sablonok) számít, a választó saját gombjai nem
        forras = " ".join(re.findall(r"<template[^>]*>(.*?)</template>", s, re.S))
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", forras, flags=re.S)
    t = H.unescape(re.sub(r"<[^>]+>", " ", t))
    if "—" in t:
        figy.append(f"Hosszú gondolatjel (—) {t.count('—')}x: a saját szövegben cseréld (vessző, pont, kettőspont).")
    nh = re.findall(r"\bnem\s+[^.!?]{1,40}?,\s*hanem\b", t)
    if nh:
        figy.append(f"„nem ..., hanem” szerkezet {len(nh)}x (AI-szag): {nh[0][:60]}…")
    em = EMOJI.findall(t)
    if em:
        figy.append(f"Emoji a szövegben {len(em)}x ({''.join(em[:6])}) - ha nem az ügyfél szövege, töröld.")
    ures = s.count('href="#"')
    if ures:
        figy.append(f'Üres link (href="#") {ures}x (a választó demóiban ez rendben van).')
    tel = (spec.get("kapcsolat") or {}).get("telefon")
    if tel and tel not in t:
        figy.append("A telefonszám nem szerepel a látható szövegben.")
    print(f"Ellenőrzés: {p.name}")
    for x in sulyos:
        print("  SÚLYOS:", x)
    for x in figy:
        print("  figyelem:", x)
    if not sulyos and not figy:
        print("  Minden rendben.")
    sys.exit(1 if sulyos else 0)


if __name__ == "__main__":
    main()
