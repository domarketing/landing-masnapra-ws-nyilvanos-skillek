---
name: szovegellenorzo
description: "Magyar szövegellenőrző. Minden LEGENERÁLT magyar szöveget átnéz és átír úgy, hogy ne lehessen ráismerni, hogy AI írta. Futtasd MINDEN szöveg leadása előtt: e-mail, hírlevél, Facebook- és Instagram-poszt, hirdetésszöveg, weboldal, landing oldal, prezentáció, videószkript, ügyfélszolgálati válasz, ajánlat, dokumentum. Triggerek: 'ellenőrizd a szöveget', 'nézd át a szöveget', 'ne látszódjon hogy AI', 'AI-szagú', 'emberibb legyen', 'szövegellenőrzés', 'de-slop', 'humanizáld', valamint ha egy másik skill a végén ide irányít. Nem ez írja meg a szöveget nulláról, hanem a kész szöveget javítja."
---

# Szövegellenőrző

Ez a skill **nem ír szöveget nulláról**. Kész szöveget kap, és két dolgot csinál vele:
kiszedi belőle azt, amiről a magyar olvasó ma már felismeri az AI-t, és egy nyugodt, felnőtt hangnemre
állítja. A szakmai szerkezet (mi legyen a sorrend, mi hova kerüljön) a hívó skill dolga,
nem ezé.

## Mikor fut

**Minden legenerált szöveg leadása előtt.** Nincs kivétel: a levél, a poszt, a hirdetés,
az oldal, a prezentáció szövege, az ügyfélszolgálati válasz és a videószkript is ezen megy át.

Ha egy másik skill hívott ide, a szakmai szerkezetet **ne bántsd**. Csak a
megfogalmazáshoz nyúlj.

---

## 1. A hangnem, amire állítunk

**Nyugodt, felnőtt regiszter.** A feszültséget a helyzet adja, nem a tipográfia. Nincs
felkiáltójeles eladás, nincs nagybetűs kiabálás, nincs töredékmondatokból gyártott dobpergés.
Ettől nem lesz gyengébb a szöveg, hanem hitelesebb.

**Konkrét szám, vagy semmilyen.** „5326 kattintás” jó. „Jelentős növekedés” rossz.
Ha nincs valódi, ellenőrizhető szám, inkább ne legyen szám a mondatban. Kerekített,
hihetőnek szánt számot **soha ne találj ki**.

**A korlátot mondd ki.** Ha valamit a termék nem tud, vagy egy ígéret csak feltétellel
igaz, az kerüljön bele. Ez a leghitelesebb elem egy szövegben, és pont ezt nem írja le
magától egyetlen nyelvi modell sem.

**Sima szavak.** Semmi marketinges felfújás: nincs „forradalmi”, „egyedülálló”,
„letisztult megoldás”, „hatékonyságnövelés”. Írd le, mi történik, hétköznapi magyarul.

**Egy bekezdés, egy gondolat.** Ha egy bekezdés két dolgot akar, vágd ketté.

---

## 2. Amit ki kell szedni

### Nulla tolerancia

> **A „nem X, hanem Y” szerkezet és minden rokona: 0 darab.**

Ide tartozik:

| Tiltott | Helyette |
|---|---|
| „nem csupán X, hanem Y” | Mondd ki simán, amit állítasz. |
| „nemcsak X, hanem Y is” | Két külön mondat, vagy egy állítás. |
| „Ez nem egy oldal. Ez egy készség.” | „Egy készség, ami minden kampányodnál ott lesz.” |
| „Nem X. Nem Y. Z.” | Egy mondat, ami megmondja, mi az. |

Ez a leggyakoribb és a legárulkodóbb minta. A magyar olvasó erre ugrik rá elsőként.
Ha a mondat tagadással nyit és állítással üt, át kell írni.

### Szintén tiltott

- **Hármas felsorolás ritmusként.** „gyorsabbá, egyszerűbbé és hatékonyabbá”. Bontsd
  kettőre vagy négyre, eltérő hosszúságú elemekkel. Hétköznapi felsorolás (három valódi
  dolog megnevezése) maradhat, a **ritmus** a baj, nem a szám.
- **Egyszavas kérdés rögtön válasszal.** „Az eredmény? Több érdeklődő.”
- **Üres átvezetés.** „És itt jön a lényeg”, „Most jön a java”.
- **Megjátszott közvetlenség.** „Őszintén?”, „Valljuk be”, „Legyünk őszinték”.
- **Két szomszédos mondat azonos szóval indítva.**
- **Töredékmondat-sorozat.** „Egyetlen oldal. Egyetlen kampányra. Nem sablon.”
  Egy-két töredék az egész szövegben rendben van, sorozatban nem.
- **Üres mondatvég általános tanulsággal.** „ami jól mutatja a folyamatos fejlődést”.
- **Emoji, hosszú kötőjel (em és en dash egyaránt), idegen idézőjel.**
  Magyar idézőjel: „így”.

### Szerkezeti szinten

Ez a réteg fontosabb, mint a szócsere, és ezt a legtöbb ellenőrzés kihagyja.

- **A tanulságot egyszer mondd ki**, ott, ahol a legjobban üt. Húzd ki az összes
  ismétlést, a szekciók végi összefoglalókat, a „mindez azt jelenti” mondatokat.
- **Hagyj legalább egy példát magyarázat nélkül.** Az AI minden példát értelmez.
- **Az érzelmet mondd ki, ne játszd el.** „Ez bosszantó” jó. „Összeszorult a gyomrom”,
  „elakadt a lélegzetem” rossz: a testi megjelenítés a legerősebb gépi jegy.
- **Nevezd meg a dolgokat.** „Egy ismert tárhelyszolgáltató” helyett a neve. „Nemrég”
  helyett a dátum. Ár, verziószám, város.

---

## 3. A változatosság-szabály

> **Szövegenként 1-2 szerkezeti beavatkozást válassz, és váltogasd őket.**

Ha minden szöveged ugyanúgy nyit, ugyanúgy zár és pontosan ugyanazokat a mintákat
kerüli, az fél év múlva egy **új** felismerhető minta lesz. Mérésünk is ezt mutatta:
két nyelvi modell a töredékmondatokat kijavította, de közben behozott helyette egy másikat.

Ne fusson le minden szövegen a teljes menü. Nézd meg, mi az adott szöveg legrosszabb két
hibája, azt javítsd, a többit hagyd.

---

## 4. Önellenőrzés, a leadás előtt

**Kötelező.** Futtasd le, és a szöveg mellé **írd is ki** az eredményt, hogy a kolléga lássa.

```bash
python3 scripts/szoveg_scan.py <fajl>          # vagy: cat szoveg.txt | python3 scripts/szoveg_scan.py -
python3 scripts/szoveg_scan.py --json <fajl>   # gépi kimenet
```

A szkript a gépileg mérhető felét számolja. A többi ítélet kérdése, és ezt mondd is ki:
ne tegyél úgy, mintha mindent meg tudnál mérni.

```
[ ] „Nem X, hanem Y” és rokonai        0 db        KÖTELEZŐ
[ ] Hármas felsorolás ritmusként       0-1 db
[ ] Töredékmondat (max 3 szó)          10% alatt
[ ] Mondathossz mediánja               12-16 szó
[ ] Két szomszédos mondat azonos szóval indul
[ ] Egyszavas kérdés + rögtön válasz
[ ] Megjátszott közvetlenség
[ ] Üres átvezetés
[ ] Üres mondatvég általános tanulsággal
[ ] Felkiáltójel a törzsszövegben
[ ] Emoji 0 · hosszú kötőjel 0 · magyar idézőjel
[ ] A tanulság egyszer van kimondva, nem minden szekció végén
[ ] Ha van szám, konkrét és nem kerekített
[ ] Van legalább egy hely, ahol elismerünk egy korlátot
```

---

## Amit ez a skill NEM csinál

- **Nem ír szöveget nulláról.** Azt a hívó skill csinálja.
- **Nem nyúl a szerkezethez.** A 16 legókocka sorrendje, a levél felépítése, a poszt
  hookja a hívó skill dolga.
- **Nem tesz semmit felismerhetetlenné.** Ilyen nincs. Azt éri el, hogy a legárulkodóbb
  minták ne legyenek benne, és hogy minden szöveg ellenőrizve legyen, ne csak néha.

## Kapcsolódó skillek

Az `ertekesitesi-oldal-keszito` skill a végén ezt futtatja a kész szövegen. Az értékesítési oldalra
vonatkozó külön szabályok (főcím, kifogáskezelés, ár a CTA-ban) ott vannak, nem itt.
