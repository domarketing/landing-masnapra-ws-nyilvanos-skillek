# 6 - Minőség: ellenőrzőlista, tiltólista, magyar szöveg

## Mielőtt átadod a választót
- Alap-elemek: 5 eltérő karakter, mind márkára hangolva; textúra, dekor, határ: 5-5 ötlet az ügyfél témájából, a demóban jól látható.
- Szekciók: a beadott oldal minden szekciója, 5-5 elrendezés.
- Artifactként publikálva `capabilities: {"db": {}}`-vel, `ArtifactData list` lefutott.
0. A motor hiba nélkül építette meg (ha a szabvány sérül, nem épít: pótold, amit a hibalista kér; `--engedd` csak
   fejlesztéshez való, ügyfélnek így épített választó nem adható át).
1. `python3 <SKILL>/scripts/ellenorzo.py <valaszto.html> --spec arculat.json` → nincs SÚLYOS találat.
2. `python3 <SKILL>/scripts/kepernyokep.py <valaszto.html> --konzol` → nincs JS-hiba.
3. Képernyőképek (ha van böngésző): `--elo` (az élő oldal az ajánlottakkal), és legalább a `kat-paletta`,
   `kat-hero`, `kat-kinalat` kategóriák. Nézd meg őket (Read), és javítsd:
   - olvashatatlan kontraszt (világos szöveg világoson, a kiemelt szó eltűnik),
   - túlcsorduló vagy levágott szöveg (hosszú magyar szavak: „Kunszentmiklósról”),
   - hiányzó fotó („FOTÓ HELYE”) vagy torzult kép,
   - két szinte egyforma opció egy kategórián belül,
   - az élő oldalon két egymás melletti, azonos hangulatú blokk (a motor a felületeket váltogatja, de a
     változat-választás is számít).
4. Mobil: a választó élő oldalán a „📱 Mobil” gomb; képernyőképen a végleges oldalt `--w 500`-zal nézd.

## Mielőtt átadod a végleges oldalt
- `kepernyokep.py fooldal.html qa/kesz --w 1440` és `--w 500`; `ellenorzo.py fooldal.html --spec arculat.json`.
- Minden link működik (étlap, telefon `tel:`, térkép, közösségi oldalak), a horgonyok (`#etlap`) léteznek.
- A `DESIGN-RENDSZER.md` a választott opciókat és a megjegyzéseket tartalmazza.

## Tiltólista
- **Kitalált tény**: vélemény, csillagos értékelés, ügyfélszám, díj, „több mint X”, amit az oldal nem mond.
- **AI-jelek**: lila-kék gradiens, emoji a saját szövegben, üveghatás mindenhol, háromoszlopos ikonkártya minden
  szekcióban, Inter/Poppins reflexből, „Fedezd fel…”, „Tapasztald meg…”, „Emeld új szintre…”, „a legjobb választás”.
- **Hosszú gondolatjel** (—) és „nem X, hanem Y” fordulat a saját szövegedben (az ügyfél szövegében maradhat).
- **Valódi ember arcának generálása**, versenytárs arculatának másolása.

## Magyar szöveg (címek, felvezetők, mikroszövegek)
- Rövid, konkrét, a márka hangján (tegező vagy magázó: ahogy a mostani oldal). Egy cím egy gondolat.
- A kiemelt (`==...==`) rész 1-3 szó, a cím vége vagy a lényege.
- Gombszöveg igével: „Nézd meg az étlapot”, „Foglalj időpontot”, „Hívj most”.
- Számok magyarosan: `3 200 Ft`, `11:00–20:00` (itt a nagykötőjel helyes), `2023. március 1.`
- Ha a mostani oldalon van jó szlogen (pl. „Ugorj be egy tésztára!”), használd, mert az ügyfélé.
