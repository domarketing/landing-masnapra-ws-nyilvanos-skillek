#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""epit.py - az arculat-generátor építője.

  python3 epit.py valaszto <arculat.json> [--ki arculat-valaszto.html] [--elozo valasztas.json] [--artifact]
        -> az ARCULAT-VÁLASZTÓ: a szabványos 22 kategória, mindegyikben 5+ opció, megjegyzés, végleges-jelölés,
           alul élő oldal. Ha nem felel meg a szabványnak, NEM épül meg (a hibalista megmondja, mit pótolj).
           --elozo: második kör; az előző kör véglegesei előre bejelölve, a megjegyzései az opciók mellett.
           --artifact: mellé <név>-artifact.html is (Artifact-publikáláshoz, capabilities: {"db": {}}).

  python3 epit.py oldal <arculat.json> <valasztas.json | visszajelzes.txt> [--ki fooldal.html] [--md DESIGN-RENDSZER.md]
        -> a VÉGLEGES OLDAL a kiválasztott elemekből (+ DESIGN-RENDSZER.md, tokenek.css)

  python3 epit.py lista
        -> a könyvtár összes opciója kategóriánként (id, név, leírás) - ebből válogatsz az arculat.json-ba
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from motor import epito, valaszto, oldal  # noqa: E402


def arg(nev, alap=None):
    a = sys.argv
    return a[a.index(nev) + 1] if nev in a else alap


def artifact_valtozat(ki):
    """Ugyanaz a választó, a dokumentum-váz nélkül (az Artifact eszköz maga teszi köré). Publikálás:
    capabilities: {"db": {}} -> a jelölések és megjegyzések az artifact adatbázisába mentődnek (arculat/valasztas-v<verzio>)."""
    import re
    ki = Path(ki)
    h = ki.read_text(encoding="utf-8")
    h = re.sub(r'^<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport"[^>]*>\s*', "", h, flags=re.I)
    h = h.replace("</style></head><body>", "</style>", 1)
    h = re.sub(r"</body></html>\s*$", "", h)
    cel = ki.with_name(ki.stem + "-artifact.html")
    cel.write_text(h, encoding="utf-8")
    return cel


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    mod = sys.argv[1]
    if mod == "lista":
        from motor.stilusok import GLOBALIS
        for kat, (lst, nev, leiras) in list(GLOBALIS.items()) + list(epito.SZEKCIOK.items()):
            print(f"\n## {kat} · {nev} ({len(lst)} opció) - {leiras}")
            for x in lst:
                print(f"  {x['id']:5} {x['nev']}: {x['leiras']}")
        return
    spec_ut = Path(sys.argv[2])
    spec = epito.betolt(spec_ut)
    if mod == "valaszto":
        ki = Path(arg("--ki", spec_ut.parent / "arculat-valaszto.html"))
        elozo = None
        if arg("--elozo"):
            import json, re
            t = Path(arg("--elozo")).read_text(encoding="utf-8")
            m = re.search(r'\{"marka".*\}\s*$', t.strip(), re.S)
            elozo = json.loads(m.group(0) if m else t)
        n = valaszto.epit(spec, ki, elozo=elozo, engedd="--engedd" in sys.argv)
        print(f"KÉSZ: {ki}  ({n / 1024 / 1024:.2f} MB)")
        if "--artifact" in sys.argv:
            print("  + artifact-változat:", artifact_valtozat(ki))
    elif mod == "oldal":
        v = sys.argv[3]
        ki = Path(arg("--ki", spec_ut.parent / "fooldal.html"))
        md = Path(arg("--md", ki.parent / "DESIGN-RENDSZER.md"))
        n, V = oldal.epit(spec, v, ki, md)
        print(f"KÉSZ: {ki}  ({n / 1024 / 1024:.2f} MB)\n  + {md}\n  választás: " +
              ", ".join(f"{k}={v}" for k, v in V.items()))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
