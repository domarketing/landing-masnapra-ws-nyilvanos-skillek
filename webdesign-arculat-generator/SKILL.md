---
name: webdesign-arculat-generator
description: >
  Webdesign ARCULAT- és DESIGNRENDSZER-GENERÁTOR egyetlen weboldal-URL-ből. Kinyeri a vállalkozás mostani oldalából a
  logót, színeket, betűket, fotókat és tényeket, legenerálja az egyedi ikonjait (OpenAI), majd elkészít egy interaktív
  ARCULAT-VÁLASZTÓT: a 12 arculati elemből (paletta, betűpár, ikonstílus, címsor, alcím, gomb, kártya, fotókezelés,
  háttér-textúra, dekor, szekcióhatár, mozgás) 5-5 opciót, plusz a BEADOTT OLDAL MINDEN SZEKCIÓJÁBÓL 5-5 elrendezést,
  mindegyik mellé megjegyzés-mezővel és „végleges” jelöléssel, alul az élő oldallal. Az alap-elemek 5 eltérő karakterben
  (elegáns, modern, merész, barátságos, klasszikus) készülnek, mind az ügyfél márkájához igazítva; a textúra, a dekor és
  a határ ötletei mindig az ügyfél fő témájából jönnek. Artifactként publikálva a jelölések és megjegyzések az artifact
  adatbázisába mentődnek, a Claude közvetlenül kiolvassa. A visszajelzés után megépíti a végleges oldalt és a
  DESIGN-RENDSZER.md-t. Használd MINDIG, ha valaki ilyet kér: "csinálj arculatot / designrendszert a weboldalamhoz",
  "új design a főoldalamnak", "modernizáld a weboldalamat", "tervezz új weboldalt ennek a cégnek: <URL>", "milyen
  színek, betűk, gombok legyenek", "webdesign opciók", "arculat-választó", "mutass több design-változatot", vagy csak
  beküld egy URL-t azzal, hogy legyen szebb. Ne használd: ha csak szöveget kell írni, csak logót kell tervezni, vagy egy
  már véglegesített designrendszerrel kell csak egy újabb aloldal (arra is jó, de akkor a 0. lépés szerint kihagyja a választót).
version: 2.0.0
---

# Webdesign arculat-generátor

Egy URL-ből egyedi, márkára szabott designrendszer, amit az ügyfél **maga választ ki** egy élő, kommentelhető
választóban. Nem dönt az ügyfél helyett: minden elemből 5 utat mutat, és az élő oldalon azonnal látszik a kombináció.

A motor kész: `scripts/epit.py` egy `arculat.json`-ból építi a választót és a végleges oldalt. **A te dolgod a
márkára szabott tartalom**: az opciók megírása (CSS az `egyedi_opciok`-ban), a válogatás, az indoklások, a szövegek.

## A SZABVÁNY (minden futásnál ugyanaz a szerkezet)

1. **A 12 arculati kategória, ebben a sorrendben, mindegyikben 5 opció:** Alapok (színpaletta, betűpár, ikonstílus) ·
   Tipográfia (címsorok, alcímek) · Elemek (gombok, kártyák, fotókezelés) · Felületek és díszítés (háttér-textúra,
   dekor-réteg, szekcióhatárok, mozgás).
2. **Az alap-elemek 5 ELTÉRŐ KARAKTERBEN, márkára hangolva.** Paletta, betűpár, ikon, címsor, alcím, gomb, kártya,
   fotó, mozgás: az 5 opció tudatosan 5 más karakter (jellemzően **elegáns · modern · merész · barátságos ·
   klasszikus**), de MIND az ügyfél márkájához illik (a színei, a hangneme, a tárgyai). Tisztességes, modern webdesign,
   nem extra különleges. Ne a könyvtár alapértelmezéseit add oda: írd meg (vagy igazítsd) a CSS-t az ügyfélre, az
   `egyedi_opciok.<kategória>` listában. Ugyanannak a könyvtári gombnak/kártyának 5 ügyfélnél ugyanúgy kinézni tilos.
3. **A textúra, a dekor és a szekcióhatár: 5-5 kreatív ötlet az ügyfél FŐ TÉMÁJÁBÓL.** Pénzügynél: árfolyamgörbe,
   bankjegy-guilloche, gyertyadiagram, érmék, hozamgörbe-él, tőzsdei ticker; étteremnél: terítő, tányérperem, gőz,
   recept-margó; fogászatnál: …  Ezek mindig `egyedi_opciok` (a motor hibát ad, ha könyvtári opciót kapnak).
   Recept: `references/7-alap-es-tema.md`.
4. **A szekciók a BEADOTT OLDAL szekciói.** Nincs fix szekciólista: ami a mostani oldalon van (pl. fejléc, hero,
   szolgáltatások, rólunk, vélemények, kapcsolat, lábléc), azt sorolod fel a `szekcio_sorrend`-ben, és MINDEGYIKHEZ
   5 elrendezés-változat jár. A motor szekció-típusai: `nav hero tenyek kinalat ajanlat folyamat tortenet galeria
   latogatas lablec` (könyvtárral). Ha egy szekció egyikhez sem illik, vedd fel `egyedi_szekciok`-ként (név, leírás),
   és írj hozzá 5 változatot az `egyedi_opciok.<szekció>` alá. Ad-hoc bővítés (pl. a felhasználó egy sales oldal
   legókockáit is kéri) ugyanígy, vagy fix blokként az élő oldalon (`references/4-arculat-json.md`).
5. **Minden opció ugyanúgy véleményezhető:** élő előnézet, „Kipróbálom lent”, „★ Ez legyen a végleges”, megjegyzés;
   kategóriánként „kérek újakat”; általános megjegyzés; alul az élő oldal (asztali/mobil, „▶ Mozgás lejátszása”);
   a mozgás-kategória előnézetei maguktól ismétlődnek, és lassíthatók.
6. **A választót MINDIG a motor építi** (`scripts/epit.py valaszto`). Ha a szabvány sérül, NEM épít: a hibalista
   megmondja, mit pótolj.
7. **A visszajelzés MENTŐDIK.** Ha a sessionben van `Artifact` eszköz, a választót MINDIG artifactként is publikáld
   `capabilities: {"db": {}}`-vel (lásd 4. lépés): a jelölések és megjegyzések az artifact adatbázisába mentődnek
   (`arculat/valasztas-v<verzio>`), és te az `ArtifactData`-val közvetlenül kiolvasod őket, bemásolás nélkül.
   Helyi fájlként a böngésző menti, és marad a „Visszajelzés másolása”.
8. **Második kör:** `--elozo valasztas.json` és `verzio` +1: ugyanaz a szerkezet, az előző véglegesek előre
   bejelölve, az előző megjegyzések az opciók mellett, az új opciókon „Új” jelvény. Ugyanarra az artifact-`url`-re
   publikálj újra.
9. **Nincs „ujjlenyomat” vagy futások közötti emlékezet:** a skill az ügyfél saját fiókjában fut. Az egyediséget a
   márkára írt opciók és az ügyfél témájából jövő ötletek adják.

## Alapszabályok

| # | Szabály | Miért |
|---|---|---|
| 1 | **Első futás = arculat-választó.** Soha ne építs rögtön végleges oldalt, ha még nincs `valasztas.json`. | Az ügyfél akarja kiválasztani; a választó a termék. |
| 2 | **Minden kategóriában 5 opció**, 5 tényleg más karakterrel (nem 5 árnyalat ugyanabból), mind márkára hangolva. | Ettől van értelme választani. |
| 3 | **A tények szentek.** Árak, nevek, címek, nyitvatartás, számok csak az oldalról, betűre. Nincs kitalált vélemény, díj, szám, ügyfélszám. | Hitelesség; az ügyfél cégéről van szó. |
| 4 | **Az ügyfél arculata a kiindulás.** A logó marad; legalább egy paletta a mostani színek hű, igényesebb változata. | Frissítés, nem idegen márka. |
| 5 | **A téma-elemek az ügyfél fő témájából.** Textúra, dekor, határ, motívumok, matricák: a szakma tárgyaiból és képeiből (`references/7-alap-es-tema.md`). Ne találj ki külön „kreatív koncepciót”: az ügyfelek nem akarnak túl különlegeset. | Ettől nem sablon, mégis érthető. |
| 6 | **Ne kérdezz feleslegesen.** Ami hiányzik, azt levezeted; a végén 3-5 sorban jelzed, mit feltételeztél. Csak az OpenAI-kulcsot és a hálózatot kérdezd, ha nincs. | Egy URL, egy választó. |
| 7 | **Magyar szöveg, emberi hangon**: nincs hosszú gondolatjel a saját szövegedben, nincs „nem X, hanem Y” fordulat, nincs emoji, nincs üres marketing-töltelék. | Ne legyen AI-szaga. |
| 8 | **A kulcsot soha nem írod ki**, nem teszed fájlba a kimenet mellé, nem kerül a HTML-be. | Biztonság. |

## A folyamat

### 0. Előkészítés (1 perc)
- Munkamappa: Claude Code-ban a felhasználó mappájában egy új almappa (`<marka>-arculat/`); Claude.ai-ban `/mnt/user-data/outputs/<marka>-arculat/`. A skill mappája: `<SKILL>` (ahol ez a fájl van).
- **Van már döntés?** Ha a mappában van `valasztas.json` és `DESIGN-RENDSZER.md`, NE készíts új választót: az új kérést ezzel a rendszerrel építsd (lásd 6. lépés).
- Kulcs-ellenőrzés: `python3 <SKILL>/scripts/ikon_generalo.py --check`. Ha `NO_KEY`: kérd el a felhasználótól (`references/1-folyamat.md` → „OpenAI-kulcs”). Ha nem ad kulcsot, a motor tartalék ikonstílusokat épít a márka formáiból (a kategória megmarad), és ezt jelzed.
- Hálózat: ha a letöltés hibázik (Claude.ai-ban tiltott domain), lásd `references/1-folyamat.md` → „Hálózat”.

### 1. Kinyerés
```bash
python3 <SKILL>/scripts/oldal_kinyero.py <url> <munkamappa>          # főoldal + max. 7 fontos aloldal
python3 <SKILL>/scripts/tablo.py <munkamappa>/bemenet/kepek --ki <munkamappa>/tablo-fotok.jpg --sakk
```
Olvasd el: `bemenet/arculat.md` (színek, betűk, logó-jelöltek, kapcsolat, fotólista), `bemenet/szoveg/*.md` (minden
tény innen jön), és **nézd meg a fotótablót** (Read): melyik a logó, melyek a legjobb fotók, mi a márka tárgyi
világa (tálak, csomagolás, szerszámok, terek). Ha van `eredeti-fooldal-1440.png`, azt is.

### 2. Arculati mag → `arculat.json` (a munka lelke)
Séma: `references/4-arculat-json.md`. Az opciók megírása: `references/7-alap-es-tema.md` (5 karakter + téma-ötletek,
CSS-receptekkel). Ebben a sorrendben töltsd:
1. **profil**: 3-5 mondat arról, mit láttál (ez megjelenik a választó tetején, legyen konkrét és kedves).
2. **opciok.paletta**: 5 paletta, 5 karakter (pl. elegáns = a mostani fő szín igényesebb változata, modern, merész
   vagy sötét prémium, barátságos, klasszikus/monokróm), hexákkal és márkára szabott indoklással. Legalább egy hű a
   mostani színekhez.
3. **opciok.betu**: 5 betűpár KIZÁRÓLAG a `references/betuk.json` listájából (mind ékezetbiztos), 5 karakter; ha az
   ügyfél saját betűje a listán van, az legyen az egyik.
4. **motivum**: szellemszavak, 5-7 rövid tény a futószalagra (pl. ticker-határ), 2-4 matrica-szöveg. Csak valódi tény!
5. **Tartalom**: a beadott oldal szekcióinak szövege a kinyert anyagból (`hero`, `kinalat`, …, vagy egyedi
   szekció-kulcsok). Címeket írhatsz, a kiemelt szót `==így==` jelöld. **`szekcio_sorrend` = a beadott oldal
   szekciói**, ahogy ott sorban jönnek (nem a teljes típuslista).
6. **fotok**: azonosító → fájl + alt + (opcionális) `pozicio`.
7. **egyedi_opciok** (a fő munka): `cim alcim gomb kartya foto mozgas` → 5-5 márkára írt opció 5 karakterben;
   `felulet dekor hatar` → 5-5 ötlet az ügyfél témájából (maszk-SVG mintákkal); minden szekcióhoz 5 elrendezés
   (könyvtárból válogatva: `python3 <SKILL>/scripts/epit.py lista`, vagy egyedi `html`+`css`).
8. **opciok.<kategória>**: `lista` (az 5 id), `ajanlott` (a szerinted legjobb), `miert` (indoklás a márkáról).

### 3. Ikonok (OpenAI, kb. 4-5 Ft/ikon)
Írd meg az `ikon-spec.json`-t (`references/5-ikonok.md`: 8-10 ikon a kínálatból és a tényekből, 5 stílus-előtag a
6 előre megírt közül, a javasolt paletta színeivel), aztán:
```bash
cd <munkamappa> && python3 <SKILL>/scripts/ikon_generalo.py --spec ikon-spec.json
python3 <SKILL>/scripts/tablo.py ikonok --ki tablo-ikonok.jpg --oszlop 8 --meret 150 --sakk
```
Nézd meg a tablót. Ami kilóg (szöveg van rajta, más stílus, rossz tárgy), azt töröld és futtasd újra (a meglévőket kihagyja).

### 4. A választó megépítése és ellenőrzése
```bash
python3 <SKILL>/scripts/epit.py valaszto <munkamappa>/arculat.json --ki <munkamappa>/<marka>-arculat-valaszto.html
python3 <SKILL>/scripts/kepernyokep.py <...>-arculat-valaszto.html qa/elo --elo        # élő oldal (ha van Chrome)
python3 <SKILL>/scripts/kepernyokep.py <...>-arculat-valaszto.html qa/hero --csak kat-hero
python3 <SKILL>/scripts/kepernyokep.py <...>-arculat-valaszto.html --konzol               # JS-hibák
```
Nézd meg a szeleteket (Read). Javítsd: olvashatatlan kontraszt, túlcsorduló szöveg, hiányzó fotó („FOTÓ HELYE”),
két egyforma opció. Ha nincs Chrome (Claude.ai), a `kepernyokep.py` megpróbálja a Playwrightot; ha az sincs, a
`scripts/ellenorzo.py <html>` statikus ellenőrzése kötelező.

**Átadás artifactként (ha van `Artifact` eszköz, MINDIG így):**
```bash
python3 <SKILL>/scripts/epit.py valaszto <munkamappa>/arculat.json --ki <...>-arculat-valaszto.html --artifact
```
Publikáld a `<...>-arculat-valaszto-artifact.html`-t: `Artifact` publish, `capabilities: {"db": {}}`, `icon: "palette"`.
(A második körtől ugyanarra az `url`-re.) A lap fejlécében „✓ mentve a Claude-nál” jelzi a mentést. Publikálás után
egy ellenőrzés: `ArtifactData list`, collection `arculat` (üres, amíg az ügyfél meg nem nyitotta). Helyi fájlként is
átadhatod (`open <fájl>`): ott a böngésző ment, és a „Visszajelzés másolása” gombbal jön vissza a döntés.
Írd le 4 lépésben, hogyan használja: kattintás = előnézet lent, ★ = végleges, megjegyzés bármelyik opcióhoz, és hogy
a döntései automatikusan mentődnek (szólnia kell, ha kész; másolni nem kell).

### 5. Visszajelzés feldolgozása
**Artifactból:** `ArtifactData get`, collection `arculat`, doc `valasztas-v<verzio>`: a `gepi` mező a teljes GÉPI ADAT
JSON (ezt mentsd `valasztas.json`-ba), a `szoveg` az olvasható összefoglaló. **Helyi fájlból:** a felhasználó
bemásolja a szöveget (a végén `--- GÉPI ADAT ---` JSON-sor); mentsd `valasztas.json`-ba (a teljes szöveg is jó). Olvasd végig a megjegyzéseket, és döntsd el:
- **„Új opciókat kér” (ujakat) vagy sok negatív megjegyzés egy kategóriában** → abban a kategóriában új opciók
  (más könyvtári opciók, új paletta/betű, vagy új egyedi opció), `verzio` +1, és új választó UGYANAZZAL a szerkezettel: `epit.py valaszto arculat.json --elozo valasztas.json` (a véglegesek és a megjegyzések átjönnek).
- **Finomítás** („a zöld legyen élénkebb”, „a gomb ne legyen ennyire kerek”) → a paletta hexáit írd át, vagy tedd a
  módosítást az `egyedi_css` mezőbe (a végleges oldal végére kerül). Szövegkérés → a tartalmat írd át.
- **Minden megvan** → 6. lépés.
Mindig foglald össze 3-6 pontban, mit értettél a megjegyzésekből, mielőtt építesz.

### 6. A végleges oldal és a designrendszer
```bash
python3 <SKILL>/scripts/epit.py oldal arculat.json valasztas.json --ki fooldal.html
```
Készül: `fooldal.html` (csak a kiválasztott elemek, statikus, SEO-meta, reszponzív), `DESIGN-RENDSZER.md` (tokenek,
betűk, komponensek, szabályok, a megjegyzések), `tokenek.css`. Ha a végleges paletta más, mint amivel az ikonok
készültek: írd át az `ikon-spec.json` színeit, és `--csak <ikonstílus> --ujra`. Ellenőrizd 1440 és 500 px széles
képernyőképen (`kepernyokep.py fooldal.html qa/kesz --w 1440` és `--w 500`), javíts, add át.
Záró üzenet 5-8 sorban: mi készült, mit feltételeztél, mit érdemes még (pl. valódi vélemények, jobb fotók).

**Már van designrendszer (újabb oldal ugyanannak a márkának):** ugyanaz az `arculat.json` és `valasztas.json`, új
tartalommal (másold le az `arculat.json`-t, cseréld a tartalmi mezőket), és `epit.py oldal`. Választó nem kell.

## Referenciák (akkor olvasd, amikor ott tartasz)
`references/1-folyamat.md` Claude.ai vs Claude Code, hálózat, kulcs, átadás · `2-arculati-mag.md` paletta-archetípusok,
betűpárosítás, motívumok, iparági metafora-tár, egyedi opció recept · `3-opcio-katalogus.md` minden opció + mikor
melyik · `4-arculat-json.md` a teljes séma · `5-ikonok.md` stílus-előtagok, ikonlista · `6-minoseg.md` ellenőrzőlista,
tiltólista, magyar szövegszabályok · `betuk.json` ékezetbiztos betűk szerepekkel · `7-alap-es-tema.md` az 5 karakter és a téma-elemek receptje.

## Kész-e? (választó)
- [ ] A motor hiba nélkül megépítette (12 arculati kategória + a beadott oldal minden szekciója, mind 5 opcióval).
- [ ] Az alap-elemek 5 tényleg eltérő karaktert mutatnak, mind az ügyfél márkájához igazítva (nem könyvtári alapértelmezés).
- [ ] A textúra, a dekor és a határ 5-5 ötlete az ügyfél fő témájából jön, és a demóban is jól látszik.
- [ ] Az `ajanlott` mindenhol a szerinted legjobb, a `miert` a márkáról szól (nem a könyvtári általános szöveg).
- [ ] Artifactként publikálva, `capabilities: {"db": {}}`-vel; az `ArtifactData list` lefutott.
- [ ] Az ikonok egységesek stílusonként, átlátszó hátterűek, nincs rajtuk szöveg.
- [ ] Az élő oldal az ajánlottakkal is szép (ez az első benyomás!), mobil nézetben sincs túlcsordulás.
- [ ] A konzolban nincs JS-hiba; a fájl egy önálló HTML (jellemzően 3-6 MB).
- [ ] Minden tény az ügyfél oldaláról jön; kitalált vélemény, szám nincs.

## Ismert buktatók
| Buktató | Megoldás |
|---|---|
| Az opciók „egyformák” | 5 karakter (elegáns · modern · merész · barátságos · klasszikus), ne ugyanannak az árnyalatai. |
| A textúra/dekor alig látszik a demóban | Maszk-mintánál 7-15% átlátszatlanság; a dekor `@container elo (max-width:…)` elrejtését csak 340 px alatt használd (a demók keskenyek). |
| A váltakozó határ (több féle egymás után) | A motor minden `.hat`-ot sorszámoz (`data-hn` 0/1/2): `%S .hat[data-hn="0"]{…}` stb. (`references/7-alap-es-tema.md`). |
| Sárga/világos főszín: fehér gombfelirat olvashatatlan | A motor automatikusan sötét feliratot tesz rá; ha mégsem jó, adj meg sötétebb `primary`-t vagy `deep`-et. |
| A motívum-forma nem látszik | Maszk: csak az alfa számít; zárt, kitöltött forma kell (`fill` alapértelmezett fekete), `stroke`-nál `stroke='#000'` és elég vastag vonal. 100×100-as vászon. |
| Nincs fotó egy helyen („FOTÓ HELYE”) | Adj meg fotót az adott mezőben, vagy válts olyan változatra, ami fotó nélkül is működik. Arcot soha ne generálj. |
| Túl nagy HTML (>8 MB) | Kevesebb fotó, vagy a `fotok.<id>.max` 1000-re; a fotók egyszer kerülnek be (CSS-osztály). |
| Claude.ai: a letöltés 403/tiltott | Hálózati engedély kell a domainre (`references/1-folyamat.md`), vagy a felhasználó feltölti a logót + képernyőképet, és `web_fetch`-csel olvasod a szöveget. |
| Az OpenAI 403 „verify organization” | A felhasználónak a platform.openai.com-on ellenőriztetnie kell a szervezetét; addig ikon nélkül megy. |
