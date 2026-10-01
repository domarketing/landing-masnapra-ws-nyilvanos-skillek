# 2 - Az arculati mag: honnan jön a változatosság és az egyediség

Egy igényes, egyedi oldal mélységét hat réteg adja: **felület-textúra, dekor-réteg,
különleges szekcióhatár, metafora-komponensek, mozgás, egyedi ikonok**. A motor mindegyikre 5-8 kész receptet ad; a
te dolgod, hogy (1) a márka színei, betűi, formái kerüljenek bele, (2) az opciók tényleg különbözzenek, (3) legyen
legalább egy csak-ennél-a-márkánál-értelmes elem.

## 1. Öt paletta, öt karakter (a 7-es referencia szerint)

> Új szabvány: 5 paletta és 5 betűpár, 5 eltérő karakterben (elegáns · modern · merész · barátságos · klasszikus), mind
> márkára hangolva. Az alábbi archetípus-táblázat ehhez forrás, nem kötelező lista.

Minden palettához elég 5-7 hexa: `primary`, `accent`, `accent2`, `paper`, `ink` (+ opcionálisan `deep`, `card`,
`mod: "sotet"`). A motor ebből képezi a mély/halvány árnyalatokat, felületeket, vonalakat, árnyékokat, és a
kontrasztbiztos szövegszíneket (pl. sárga gombon sötét felirat). Válassz közülük 5-öt, a márkára fordítva:

| # | Archetípus | Recept | Példa (tésztázó) |
|---|---|---|---|
| 1 | **Hű, de igényesebb** | a mostani fő szín mélyebb, telítettebb változata + egy kísérőszín a márka tárgyi világából | csempezöld + kraft |
| 2 | **Merész főszín** | a szakma legerősebb „jelszíne” lesz a primary (étel: paradicsom; bio: levélzöld; tech: kobalt) | paradicsom + bazsalikom |
| 3 | **Meleg, napos** | világos, meleg primary (sárga, barack, homok) sötét felirattal + hűvös kiegészítő | durumsárga + türkiz |
| 4 | **Hűvös, friss** | a fotókon visszatérő hűvös szín (tál, csempe, víz, ég) + korall/sárga pötty | türkiz tál + korall |
| 5 | **Monokróm, kézműves** | fekete/tinta primary, papír/kraft felületek, egy apró zöld vagy piros pecsétszín | kraft + fekete tinta |
| 6 | **Sötét prémium** | `mod: "sotet"`: mélyzöld/éjkék/szén felület, arany/réz/mustár fény, egy meleg akcent | esti trattoria |

Szabályok: a papír (`paper`) soha nem tiszta fehér (#FBF8F2-féle meleg vagy #F5FAF8-féle hűvös tört fehér);
az `ink` soha nem tiszta fekete (a primary felé húzott sötét); a harmadik szín (`accent2`) csak apró díszekben jelenik
meg. **Tilos a lila-kék AI-gradiens** (#7c3aed, #6366f1…), kivéve ha tényleg az ügyfél színe. Ha a mostani oldal
színei csúnyák, az 1. archetípus akkor is a „hű” legyen: a logó színéből induljon.

## 2. Öt betűpár, öt karakter

Csak a `references/betuk.json` betűi (mind ellenőrizve ő/ű-re). Minden pár: `display` (cím) + `body` (szöveg) +
`hand` (kézírás-akcent) + `label` (mono címke). Hangolás: `w_display` (a cím vastagsága), `ls_display`
(betűköz), `nagybetus`, `lh_display`, `hero_scale` (vékony/keskeny betűnél 1.1-1.15), `fs_hand` (kézírás-szorzó;
kicsi x-magasságú kézírásnál 1.25, nagynál 1.0).

| Karakter | Cím-betű (szerep) | Szöveg | Mikor |
|---|---|---|---|
| meleg serif | Fraunces, Young Serif, Petrona | Figtree, Karla | család, étel, kézműves, pékség |
| karakteres grotesk | Bricolage Grotesque, Familjen, Schibsted | DM Sans, Work Sans | kreatív, street food, fiatalos |
| klasszikus kontraszt | Playfair Display, DM Serif Display, Bodoni Moda | Karla, Mulish | vendéglő, szépség, esküvő, butik |
| plakát / keskeny | Big Shoulders Display, Oswald, Bebas Neue | Work Sans, Archivo | esemény, sport, városi, akció |
| kerek, barátságos | Fredoka, Baloo 2, Rubik | Nunito Sans, Nunito | gyerek, desszert, család, játék |
| szerkesztőségi | Instrument Serif, Newsreader, Gloock | Instrument Sans, Commissioner | tanácsadó, prémium, magazin |
| tech / precíz | Space Grotesk, Sora, Mona Sans | IBM Plex Sans, Manrope | szoftver, mérnök, pénzügy |

Kerüld reflexből: Inter, Poppins, Montserrat, Roboto (csak ha az ügyfél saját betűje). Ne használd az Anton + Caveat +
JetBrains Mono hármast (a Fesztivál ujjlenyomata). Ha az ügyfélnek van saját betűje és benne van a listában, az
legyen az 1. pár egyik betűje.

## 3. Motívumok: a márka saját formái (3-4 db)

Kérdés, ami mindig működik: *„Milyen tárgyat, anyagot, formát fog kézbe ennek a szakmának a vevője?”* Nézd a logót
(formák), a nevet (jelentés), a fotókat (tárgyak), és a szakma eszközeit. A formákat maszk-SVG-ként adod meg
(100×100-as vászon, fekete kitöltés, egyszerű zárt formák; vonalnál `stroke='#000'` és vastag vonal). Ezekből épül:
a **Motívum-minta** textúra (t4), a **lebegő motívumok** (d2), az **óriás jel** (d3, a `jel` kulcs; legjobb a logó
egyszerűsített formája), a futószalag elválasztó-jele.

Példa (tésztázó): masni-tészta, bazsalikomlevél, búzakalász (ellipszisekből), a logó háza (`fill-rule='evenodd'`
ablakokkal). Más példák: fogászat → fog-kontúr, tükör-kör, fogkefe-fej; ács → fecskefark-kötés, szögfej, fűrészfog;
pszichológus → kavics, csepp, koncentrikus kör; kozmetika → csepp, levél, tükör; autószerviz → csavaranya (hatszög
lyukkal), fogaskerék, csavarkulcs.

**Szellemszavak** (óriás kontúrszó a szekciók szélén): 1 szó szekciónként, nagybetűvel, a márka nyelvén (TÉSZTA,
ÉTLAP, FRISS, HÁZI, HELYBELI). **Futószalag-tények**: 5-7 rövid, VALÓDI tény (nyitvatartás, alapanyag, garancia, hely).
**Matricák**: 2-4 nagyon rövid, valódi állítás (2-4 szó), mert kerek matricán ülnek.

## 4. Egyedi opció (metafora-komponens): legalább egy

A választóban „Csak nektek” címkével jelenik meg. A legjobb helye: **kártya** (a kártyastílus az egész oldalon
visszatér), **hero** vagy **kínálat**. Recept:
1. Válassz egy tárgyat a szakma világából, amit a vevő kézbe vesz: elviteles doboz, étlap, recept, időpont-cédula,
   szervizkönyv, oklevél, bérlet, belépőjegy, tervlap, csomagolás, pecsételt ajánlat.
2. Ennek 2-3 felismerhető vonása legyen CSS-ben: forma (clip-path), anyag (szín/gradiens/textúra), egy jellegzetes
   részlet (fül, perforáció, pecsét, logó-matrica, margóvonal).
3. Kártyánál a CSS `%S .krt{...}` formában (a `%S` a saját data-attribútumra szűkít), és kezeld a fotós kártyát is
   (`%S .krt>.krt-kep{...}`). A logóra `var(--logo-eredeti)` (mindig a színes változat) vagy `var(--logo-img)` (sötét
   palettán a fehér).
4. Hero/szekció egyedi opciónál `html` + `css` (a CSS a saját `.v-<id>` osztályára szűkítsen; reszponzívhoz
   `@container elo (max-width:...)`). Példa: a `egyedi_opciok.kartya` lista.

Iparági ötlettár (kiindulás): fogorvos → perforált időpont-cédula, kezelési terv kártya, röntgen-panel · ács →
tervlap-rács kártya, mérőszalag-idővonal, pecsételt árajánlat · pszichológus → jegyzetlap margóvonallal, borítékos
titoktartás · pénzügy → bankkártya chippel, guilloche-keret · ügyvéd → dosszié-fül, iktatószám · kozmetika → tükör-keret,
kezelés-cédula · oktatás → füzetlap, bérlet-jegy, oklevél · autó → szervizkönyv, mérőóra-számláló · kertészet →
vászonzsák-címke, évszak-kör · ingatlan → alaprajz-kártya, kulcscímke · étterem → étlap-lap, krétatábla, elviteles doboz.

## 5. Ajánlott kombináció

Az élő oldal az ajánlott opciókkal indul: ez az első benyomás, tehát ez legyen a legszebb, legkoherensebb összeállítás
(egy harsány elem mellé csendesebbek: pl. kollázs-hero + tiszta kártyák; neo-brutál gomb + tiszta felület). Utána
nézd meg képernyőképen, és ha valami üt, cseréld az ajánlottat.
