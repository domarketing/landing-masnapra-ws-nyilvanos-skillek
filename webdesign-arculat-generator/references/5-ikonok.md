# 5 - Ikonok: lista, stílusok, generálás

## Melyik ikonok? (8-10 db)
Minden ikon egy konkrét tárgy a márka világából, egy mondatban leírva angolul (a modell angolul pontosabb):
- a **kínálat** kategóriái (pl. tészta, rizottó, leves, desszert; vagy: fogfehérítés, implantátum, gyerekfogászat),
- a **tények / folyamat** lépései (alapanyag, reggeli készítés, főzés, elvitel; vagy: konzultáció, terv, kivitelezés),
- 1-2 jellegzetes tárgy (a csomagolás, a szerszám, a hely).
Ugyanaz az ikon több helyen is szerepelhet (kínálat + folyamat). Ikonra SOHA nem kerül szöveg.

## Öt stílus a választóba (előtagok)
Válassz 5-öt ebből a hatból (a márkához nem illőt hagyd ki), a `{primary}` `{accent}` `{accent2}` `{ink}` helyére a
javasolt (ajánlott) paletta színei kerülnek az `ikon-spec.json` `szinek` mezőjéből. Ételnél adj hozzá egy természetes
kiegészítő színt (pl. „warm cream #F2DFA7”), különben zöld lesz a tészta.

| id | Név | Előtag (angol, a promptba) |
|---|---|---|
| i1 | Lapos, kétszínű | Modern flat vector icon, friendly rounded geometric shapes, bold simple solid shapes, no gradients, no outlines, no 3D. Limited palette only: {primary}, {accent}, {accent2}, with tiny {ink} details. |
| i2 | Vonalas + színfolt | Minimal monoline line-art icon: uniform medium-weight {ink} strokes with rounded caps, plus two flat colour blobs in {accent} and {primary} slightly offset behind the line drawing like a misregistered print. Clean, editorial, lots of white space. |
| i3 | Kézzel rajzolt | Hand-drawn doodle icon drawn with a thick felt-tip marker in {ink}: loose, imperfect, slightly wobbly lines, simple flat colour fills in {primary} and {accent} that slightly miss the outlines. Charming sketchbook style. |
| i4 | Matrica | Die-cut sticker illustration: cute flat illustration in {primary}, {accent} and {accent2}, with a thick white outline border around the whole object and a subtle soft shadow under the sticker. Playful, glossy-free. |
| i5 | Puha 3D (agyag) | Soft 3D clay-style icon: rounded chunky matte shapes, gentle studio light from the top left, soft ambient occlusion, colours based on {primary}, {accent} and {accent2}. No harsh reflections, no floor. |
| i6 | Retró nyomat | Retro two-colour risograph print icon: bold simple forms in {primary} and {accent} inks only, visible grain texture and slight misregistration, flat, no gradients. |

A szkript minden prompt végére automatikusan hozzáteszi: átlátszó háttér, egyenletes margó, semmi szöveg/betű/szám/
logó, egyetlen tárgy, 48 px-en is felismerhető.

## Futtatás, ellenőrzés, újragenerálás
```bash
cd <munkamappa>
python3 <SKILL>/scripts/ikon_generalo.py --spec ikon-spec.json          # csak a hiányzókat generálja
python3 <SKILL>/scripts/tablo.py ikonok --ki tablo-ikonok.jpg --oszlop 8 --meret 150 --sakk
```
- Nézd meg a tablót. Ha egy ikon kilóg (szöveg került rá, rossz tárgy, más stílus), töröld a PNG-t és futtasd újra.
- A végleges paletta ismeretében: írd át a `szinek`-et, és `--csak <választott stílus> --ujra` (csak azt a stílust
  generálja újra, kb. 40 Ft).
- Költség (gpt-image-2.5, medium, 1024²): kb. 4-5 Ft/ikon; 8 ikon × 5 stílus ≈ 180 Ft. A szkript a végén kiírja a
  valós, tokenalapú becslést forintban.
- Utómunka automatikus: átlátszó perem levágása, négyzetre igazítás, 256 px, 128 színre kvantálás (kb. 15-30 KB/ikon).

## Fotók
Az ügyfél saját fotóit használd (a kinyerő letölti). Valódi arcot soha ne generálj. Ha kevés a fotó: inkább kevesebb
fotós változatot válassz (pl. k1 ikonos kártyák a k2 fotós helyett), és a záró üzenetben írd le, milyen fotók
hiányoznak (belső tér, csapat, termék közelről).
