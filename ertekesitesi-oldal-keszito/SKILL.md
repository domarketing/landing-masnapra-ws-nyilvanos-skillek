---
name: ertekesitesi-oldal-keszito
description: >
  Magyar értékesítési oldal (sales page) generálása feltöltött vázlat vagy dokumentum alapján.
  Használd MINDIG, ha a felhasználó értékesítési oldalt, sales page-t, landing page-t, ajánlati oldalt
  vagy "rendelési oldalt" kér — akár magyarul, akár angolul — és vázlatot, dokumentumot, vagy leírást
  tölt fel hozzá. Akkor is triggereld, ha a felhasználó csak annyit ír, hogy "csináld meg az értékesítési
  oldalt ebből a vázlatból", "konvertáld ezt HTML-lé", "készíts sales page-t", vagy feltölt egy
  Word/PDF/szöveges dokumentumot és értékesítési oldalt vár. A skill egy sikeresnek
  bizonyított magyar értékesítési oldalak struktúráját tanulja el és reprodukálja az új vázlat
  tartalma alapján — de saját vizuális stílussal, a vázlatban megadott színekkel, betűkkel, branding-gel.
---

# Értékesítési Oldal Készítő

Ezt a skillt akkor használd, ha a felhasználó egy vázlatot/dokumentumot tölt fel, és abból
profi magyar értékesítési oldalt (sales page HTML-t) szeretne generálni.

---

## 0. Előkészítés — dinamikus skillek keresése

**Az oldal generálása előtt** keresd meg az `available_skills` listában az alábbi típusú skilleket.
Ha valamelyiket megtalálod, olvasd el annak SKILL.md-jét és kövesd az utasításait — az általuk
összegyűjtött adatok automatikusan gazdagítják az elkészülő értékesítési oldalt.

| Mit keresel | Lehetséges nevek / kulcsszavak | Hogyan használd |
|---|---|---|
| **Ügyfél hangja skill** | "ügyfél hangja", "voice of customer", "vásárló hangja" | Az autentikus ügyfélnyelvet és valódi fájdalompontokat integráld a hero szövegbe, probléma-blokkba és testimonialokba |
| **Ideális vásárló skill** | "ideális vásárló", "buyer persona", "vásárló persona", "célcsoport profil" | A persona adatait használd a problémák (#2), "kinek való" (#5, #15) és a hero szövegek megírásakor |
| **Szolgáltatások skill** | "szolgáltatások", "service catalog", "ajánlat", "termékek" | A részletes szolgáltatásleírásokat és árakat integráld az árprezentációba (#7) és termékleírásba (#3-4) |
| **Arculat skill** | "arculat", "brand identity", "vizuális identitás", "brand guidelines", "brandbook" | Az itt megadott színeket, betűtípusokat, logót és brand hangvételt alkalmazd az oldal vizuális stílusánál |

Ha egyik skill sem érhető el, dolgozz a feltöltött vázlatból. Ha valamelyik megtalálható, mindig használd.

---

## A bevált struktúra — a 16 legókocka

Az oldal tartalmát a **16 legókockás keretrendszer** alapján kell felépíteni.
Minden blokknál érdemes érteni a pszichológiai célját — a részletes leírások (CÉL, szövegezési tanácsok)
a `references/16-legokocka.md` fájlban találhatók. Olvasd el mielőtt nekiállsz a generálásnak.

### Blokksorrend

Az alábbi sorrend követendő. Minden blokk szerepelhet vagy kihagyható a vázlat tartalmától függően,
de ha van rájuk tartalom, ez a sorrend kötelező.

**Kötelező blokkok (mindig szerepeljenek, ha van rájuk tartalom):**

1. **SÜRGŐSSÉGI SÁTOR** — sticky visszaszámláló/határidő sáv a lap tetején (ha van limit)
2. **HERO — FŐ ÍGÉRET** (legókocka #1) — nagy H1 főcím konkrét ígérettel, alcím, CTA gomb
3. **PROBLÉMÁK / POZITÍV JÖVŐKÉP** (#2) — a célcsoport fájdalompontjai vagy vágyai
4. **TERMÉK ELŐNYEI** (#3) — tulajdonságokból formált előnyök, mi változik az ügyfél életében
5. **TOVÁBBI TERMÉKINFÓK** (#4) — részletesebb kifejtés, ha a termék igényli
6. **KINEK VALÓ LEGINKÁBB?** (#5) — ideális vásárló megerősítése konkrét élethelyzetekkel
7. **BÓNUSZOK** (#6) — bónuszok listája értékükkel (Ft-ban)
8. **ÁRPREZENTÁCIÓ** (#7) — tételes értékösszesítő + tényleges ár
9. **RÉSZLETFIZETÉS** (#8) — ha van ilyen lehetőség, itt jelenítsd meg
10. **ELSŐ CTA GOMB** (#9) — vásárlás gomb az ár bemutatása után
11. **GARANCIÁK** (#10) — garancia magyarázata, típusai
12. **LIMITEK** (#11) — határidő/korlátozott helyek (többször is elhelyezhető az oldalon)
13. **ÜGY TÁMOGATÁSA** (#12) — ha az ajánlat jótékony célt is támogat (opcionális)
14. **GYIK** (#13) — Gyakran Ismételt Kérdések
15. **HITELESSÉGNÖVELŐ ELEMEK** (#14) — vélemények, eredmények, díjak, logósor (szétszórva az oldalon)
16. **KINEK VALÓ / KINEK NEM?** (#15) — kétoszlopos blokk
17. **KIFOGÁSKEZELÉS** (#16) — vásárló belső kételyei + környezet várható kifogásai
18. **UTOLSÓ CTA** (+1) — az oldal alján mindig legyen vásárlás gomb
19. **FOOTER** — minimális lábléc, jogi linkek

**Opcionális blokkok (ha a vázlat tartalmazza):**
- Visszaszámláló óra (countdown timer)
- Videó szekció (YouTube embed placeholder)
- Logósor / "Ahol hallhattál rólunk"
- Közösség bemutatása
- Eredmény számok (pl. "500+ elégedett vásárló")
- Összehasonlítás tábla

---

## Vizuális stílus szabályok

A vázlatból és az arculat skillből (ha elérhető) ki kell olvasni:
- **Márkanév / logó** → hero szekció (navigációs menü NEM kell — buy or die üzemmód)
- **Fő szín** → ha nincs megadva, használj sötétkéket (#2F4B9A) + borostyánsárgát (#F2A93B) alapként
- **Betűtípus** → ha nincs megadva, Montserrat + Inter (Google Fonts)
- **Célcsoport hangvétele** → nőknek szóló oldalnál melegebb, meghittebb; B2B-nél szakmaiabb

**TILOS:** az eredeti mintaoldalak képeit, logóit, valódi neveit, konkrét árakat másolni.
**KÖTELEZŐ:** a vázlatból és a skill outputokból átvett szövegeket, árakat, neveket pontosan beépíteni.

---

## Lépések

### 1. Skillek és vázlat feldolgozása

Először hajtsd végre a 0. lépést (dinamikus skillek keresése és futtatása).
Ezután olvasd el a feltöltött dokumentumot/vázlatot, és gyűjtsd össze:

- Mi a termék/szolgáltatás neve?
- Ki a célcsoport? (ha van ideális vásárló skill output, azt is vedd figyelembe)
- Mi az ár / csomagok? (ha van szolgáltatások skill output, azt is vedd figyelembe)
- Vannak-e vélemények, bónuszok, garanciák?
- Mi a fő ígéret/eredmény?
- Van-e megadott szín, betű, branding? (ha van arculat skill output, azt is vedd figyelembe)
- Mi a CTA szövege (gombfelirat)?
- Milyen ügyfélnyelv jellemzi a célcsoportot? (ha van ügyfél hangja skill output, azt is vedd figyelembe)

Ha valami hiányzik, pótold logikusan — de jelezd a felhasználónak, mit töltöttél ki magad.

### 2. Struktúra felépítése

Olvasd el a `references/16-legokocka.md` fájlt — ez segít érteni minden blokk CÉLját és
pszichológiai logikáját, ami a jó szövegezés alapja.

Ezután kövesd a fenti blokksort. Minden blokknál:
- Használj a vázlatból és/vagy skill outputokból vett szövegeket (ne találj ki tartalmat)
- Alkalmazd a vizuális stílus szabályokat
- Mobilra is reszponzív legyen (TailwindCSS CDN-ről)
- A hitelességnövelő elemeket (#14) szórd szét az egész oldalon, ne csak egy blokkba tedd
- A limiteket (#11) is elhelyezheted többször (oldal teteje, közepe, vége)

### 3. HTML generálása

A teljes oldalt **egyetlen önálló HTML fájlba** kell beépíteni:
- TailwindCSS CDN: `https://cdn.tailwindcss.com`
- Google Fonts az `<head>`-ben
- Minden CSS inline `<style>` tag-ben vagy Tailwind osztályokkal
- Visszaszámláló: vanilla JS-sel, `<script>` tag-ben a fájl alján
- Képek helyett: szép placeholder div-ek megfelelő mérettel és háttérszínnel
- Vélemény kártyák: idézőjeles, névvel, esetleg foglalkozással
- CTA gombok: kontrasztos szín, kerekített, árnyékos
- **Navigációs menü NEM szerepelhet** — értékesítési oldalon nincs elvezető link

### 4. Output

Mentsd el a fájlt az outputs mappába: `ertekesitesi-oldal.html`
Majd használd a `present_files` toolt a fájl átadásához.

---

## Referencia fájlok

- `references/16-legokocka.md` — **a 16 legókocka részletes leírása** (CÉL, pszichológiai logika, szövegezési tanácsok) — MINDIG olvasd el generálás előtt
- `references/blokk-mintak.md` — minden blokktípushoz konkrét HTML minta-kód

---

## Minőségi ellenőrzőlista (futtatsd le magadban generálás előtt)

- [ ] Felhasználtam az összes elérhető dinamikus skill outputját (ügyfél hangja, ideális vásárló, szolgáltatások, arculat)?
- [ ] A H1 főcím ütős, konkrét ígéretet tartalmaz — nem általános szlogen?
- [ ] A fájdalompontok/vágyak listájában a vásárló saját gondolatait ismeri fel?
- [ ] A termékleírás előnyöket kommunikál, nem csak tulajdonságokat sorol?
- [ ] Van legalább 2-3 vélemény/testimonial fotóval és névvel?
- [ ] Az ár egyértelmű, és van mellette tételes értékösszesítő?
- [ ] Van garancia szekció?
- [ ] Van "kinek való / kinek nem?" blokk?
- [ ] Van kifogáskezelés az oldal vége felé?
- [ ] Legalább 3 CTA gomb szerepel (hero, első CTA az ár után, utolsó CTA)?
- [ ] Nincs navigációs menü az oldalon (buy or die)?
- [ ] Mobilon is olvasható a szövegméret?
- [ ] A visszaszámláló JS-ben működik (ha van határidő)?
- [ ] A hitelességnövelő elemek szét vannak szórva az egész oldalon?

---

## Szövegezési szabályok (2026-09, a szövegellenőrző mellé)

Ezek KIFEJEZETTEN az értékesítési oldalra vonatkoznak. Az általános, minden szövegre
érvényes anti-AI szabályok a `szovegellenorzo` skillben vannak.

1. **A főcím az olvasó fejében lévő mondat, nem a mi állításunk.**
   Gyenge: „Profittermelő landing oldalak, 90 perc alatt."
   Erős: „Az ajánlatod már megvan. Mikorra lesz hozzá oldalad?"
2. **Az első bekezdés az olvasó helyzetéről szóljon, ne a termékről.** Írd le azt a percet,
   amiben most van.
3. **A problémalista legyen idővonal, ne címkelista.** „Először...", „Utána...", „A végén..."
   A sorrend maga húzza lefelé az olvasót.
4. **A kifogást mondd ki te, mielőtt ő gondolná.** Ha az ígéretben van egy gyenge pont,
   annak külön blokk jár, és ott ki is mondjuk.
5. **Az árat tedd bele a CTA feliratába**, ha az ár alacsony. Csökkenti a súrlódást.
6. **Egy blokk, egy gondolat.** Ha egy blokk két dolgot akar, vágd ketté.

A 16 legókocka sorrendje változatlanul a `references/16-legokocka.md`-ben van.

---

## Kötelező zárás: szövegellenőrzés

Amikor a szöveg elkészült, **még a leadás előtt** futtasd rajta a
`szovegellenorzo` skillt. Az szedi ki azokat a mintákat, amikről a magyar
olvasó ma már felismeri az AI-t, és az írja ki a mérést is. A szerkezethez nem nyúl,
csak a megfogalmazáshoz.
