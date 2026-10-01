#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tablo.py - feliratos kontaktlap (montázs) képekről, hogy egy pillantással átlásd a fotókat vagy az ikonokat.

    python3 tablo.py <mappa-vagy-fájlok...> --ki tablo.jpg [--oszlop 6] [--meret 220] [--sakk]

--sakk: sakktábla-háttér (átlátszó ikonokhoz, hogy lásd az alfát).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

KIT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    ki = "tablo.jpg"
    osz, meret, sakk = 6, 220, "--sakk" in a
    if "--ki" in a:
        ki = a[a.index("--ki") + 1]
    if "--oszlop" in a:
        osz = int(a[a.index("--oszlop") + 1])
    if "--meret" in a:
        meret = int(a[a.index("--meret") + 1])
    utak = []
    skip = {ki}
    i = 0
    while i < len(a):
        if a[i] in ("--ki", "--oszlop", "--meret"):
            i += 2
            continue
        if a[i].startswith("--"):
            i += 1
            continue
        p = Path(a[i])
        if p.is_dir():
            utak += sorted(x for x in p.rglob("*") if x.suffix.lower() in KIT and str(x) not in skip)
        elif p.suffix.lower() in KIT:
            utak.append(p)
        i += 1
    if not utak:
        print("nincs kép")
        return
    sor = (len(utak) + osz - 1) // osz
    cella_h = meret + 34
    lap = Image.new("RGB", (osz * meret, sor * cella_h), "#f3f1ec")
    d = ImageDraw.Draw(lap)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
    except Exception:
        font = ImageFont.load_default()
    for n, p in enumerate(utak):
        x, y = (n % osz) * meret, (n // osz) * cella_h
        try:
            im = Image.open(p)
            im.load()
            w, h = im.size
            im = im.convert("RGBA")
            im.thumbnail((meret - 12, meret - 12))
            if sakk:
                bg = Image.new("RGBA", (meret - 12, meret - 12), "#ffffff")
                bd = ImageDraw.Draw(bg)
                for yy in range(0, meret, 12):
                    for xx in range(0, meret, 12):
                        if (xx // 12 + yy // 12) % 2:
                            bd.rectangle([xx, yy, xx + 11, yy + 11], fill="#e4e4e4")
                bg.alpha_composite(im, ((meret - 12 - im.size[0]) // 2, (meret - 12 - im.size[1]) // 2))
                im = bg
            lap.paste(im.convert("RGB"), (x + 6 + (meret - 12 - im.size[0]) // 2, y + 6 + (meret - 12 - im.size[1]) // 2))
            felirat = f"{p.name[:30]}  {w}x{h}"
        except Exception as ex:
            felirat = f"{p.name[:24]} HIBA {type(ex).__name__}"
        d.text((x + 6, y + meret + 4), felirat, fill="#222", font=font)
    lap.save(ki, quality=84)
    print(ki, len(utak), "kép")


if __name__ == "__main__":
    main()
