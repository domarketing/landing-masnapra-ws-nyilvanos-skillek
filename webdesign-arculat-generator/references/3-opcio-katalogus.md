# 3 - Opció-katalógus

A motor könyvtára kategóriánként. Az `arculat.json` → `opciok.<kategória>.lista`-ban 5-7 id-t válogatsz, `ajanlott`-at
jelölsz, és ahol kell, márkára szabott `miert`-et írsz. Ha nem adsz listát, a kategória összes opciója megjelenik.
Frissíthető: `python3 scripts/epit.py lista`.

## Válogatási elv: minden kategóriában legyen kontraszt
- egy **csendes** (letisztult, szerkesztőségi), egy **meleg** (kézműves, személyes), egy **harsány** (plakátos,
  neo-brutál, színes), egy **metafora** (a szakma tárgya: árcédula, jegy, étlap, pecsét, tábla), és egy **meglepő**.
- Ami a márkához biztosan nem illik, azt hagyd ki (pl. ételfotónál a duotone `f8`, gyászszolgáltatásnál a játékos
  `m3`, ügyvédnél a kézi firkák `d5`). Ne legyen öt nagyon hasonló.

## Iparági kiindulópontok (ajánlottnak)
| Iparág | Hero | Kártya | Kínálat | Záró blokk | Egyéb |
|---|---|---|---|---|---|
| vendéglátás, étel | h7 krétatábla, h1 kollázs | egyedi (doboz/étlap), r5 | k7 kerek fotók, k2 | l4 térkép, l1 | a1 étlap, lb5 nyugta, s6 napellenző |
| szolgáltató, szakértő | h5 osztott, h3 teljes képes | r2, r7 | k5 váltakozó, k1 | l1, l5 | t1 levél, p5 számok |
| kézműves, kivitelező | h2 mozaik, h4 plakát | r1 füzetlap, r3 | k3 bento, k4 sín | l3 jegy, l2 | f5 futószalag, t4 minta |
| gyerek, család, oktatás | h6 lebegő, h1 | r6 puha, r3 | k7, k6 fülek | l6 hírlevél | m3 játékos, d5 firkák |
| prémium, szépség | h5, h3 | r5, r7 | k5, k6 | l5 | g7 szögletes gomb, f3 boltív, m4 filmes |
| esemény, közösség | h2, h4 | r4 jegy, r2 | k4, k3 | l2 | s3 futószalag, d1 szellemszó |

## A teljes könyvtár

```
## cim · Címsorok (8 opció) - Hogyan emeljük ki a címek kulcsszavát (a ==jelölt== rész).
  c1    Filctoll-kiemelés: Szövegkiemelő-csík a kulcsszó alatt, görgetésre végighúzódik. Barátságos, magabiztos, jól olvasható.
  c2    Címke-doboz: A kulcsszó egy fehér, árnyékos címkén ül, mintha rá lenne ragasztva. Erős, plakátszerű, színes háttéren is működik.
  c3    Hullámos aláhúzás: Kézzel húzott hatású hullámvonal a szó alatt. Játékos, de nem harsány.
  c4    Kézírásos szó: A kulcsszó kézírással, enyhén megdöntve. Személyes, meleg, mintha valaki odaírta volna.
  c5    Színes hangsúly: A kulcsszó márkaszínnel és vékonyabb vastagsággal. Letisztult, elegáns, szerkesztőségi.
  c6    Kontúrbetű: A kulcsszó csak körvonallal. Merész, modern, plakátos; nagy címeknél a legjobb.
  c7    Kapszula-keret: Lekerekített keret a kulcsszó körül. Rendezett, barátságos, digitális érzet.
  c8    Ferde színcsík: Kicsit megdöntött színes sáv a szó mögött. Energikus, akciós hangulat.

## alcim · Alcímek (felső címkék) (7 opció) - A szekciók felett álló kis bevezető címke stílusa.
  k1    Vonalas felső címke: Kis nagybetűs címke két rövid vonal között. Klasszikus, rendezett, minden szekciót egyformán vezet be.
  k2    Mono + csíkjel: Írógépes (mono) betű, előtte három apró csík. Modern, rendszerezett, kicsit technikás.
  k3    Kapszula pöttyel: Halvány színes kapszula, benne egy élénk pötty. Barátságos, app-szerű, jól látható.
  k4    Kézírás nyíllal: Kézzel írt felvezető, mellette egy lefelé mutató rajzolt nyíl. Személyes, mesélős.
  k5    Sorszámozott: Minden szekció kap egy nagy sorszámot (01, 02…) és egy vékony vonalat. Szerkesztőségi, magazinos rend.
  k6    Pecsét: Szaggatott keretes, megdöntött pecsét. Kézműves, „minőségellenőrzött” hangulat.
  k7    Sötét chip: Tintaszínű, szögletes chip mono betűvel. Határozott, kontrasztos, modern.

## gomb · Gombok (7 opció) - Az elsődleges és a másodlagos gomb formája és viselkedése.
  g1    Pecsét-3D kapszula: Kerek gomb „talppal” és színes derengéssel: rámutatva megemelkedik, kattintásra lenyomódik. A legkattinthatóbb érzet.
  g2    Lapos, nyíl-dobozzal: Enyhén lekerekített, lapos gomb, a nyíl külön kis dobozban, ami rámutatva előreugrik. Tiszta, modern, webshopos.
  g3    Telt ↔ kontúr: Kerek, telt gomb, ami rámutatva kontúrossá válik; a másodlagos gomb fordítva. Elegáns, visszafogott.
  g4    Matrica (neo-brutál): Vastag tintakeret, kemény eltolt árnyék, kicsit megdöntve. Merész, játékos, fiatalos.
  g5    Árcédula: Címke alakú gomb lyukkal, mint egy bolti árcédula. Kereskedelmi, kézzelfogható metafora.
  g6    Puha fény: Kerek gomb finom fényátmenettel és nagy, színes derengéssel. Prémium, puha, modern.
  g7    Szögletes, elegáns: Szögletes, tintaszínű gomb nagybetűs, ritkított felirattal; a másodlagos csak egy aláhúzott link. Divatos, szerkesztőségi.

## kartya · Kártyák (7 opció) - Minden kártya-szerű doboz (kínálat, tények, lépések) alapformája.
  r1    Füzetlap: Fehér lap halvány sorvonalakkal és színes margóvonallal. Kézzelfogható, gondos, „jegyzetelt” érzet.
  r2    Színes felső sáv: Tiszta fehér kártya, tetején kétszínű márkasáv, rámutatva megemelkedik.
  r3    Neo-brutál: Vastag tintakeret, kemény eltolt árnyék, színes ikon-doboz. Karakteres, fiatalos, nem hagyja figyelmen kívül a szem.
  r4    Perforált jegy: Belépőjegy-forma oldalsó kivágással és szaggatott tépővonallal; az ár a letéphető szelvényen ül. Esemény, kupon, ajánlat hangulat.
  r5    Étlap-keret: Dupla vékony keret, középre zárt cím díszpontokkal, mint egy nyomtatott étlap vagy meghívó. Elegáns, klasszikus.
  r6    Puha, színezett: Halványan márkaszínes kártya keret nélkül, nagy lekerekítéssel, ikon fehér körben. Barátságos, nyugodt, modern.
  r7    Oldalsávos: Fehér kártya vastag, színes bal oldali sávval. Egyszerű, rendezett, szakmai.

## foto · Fotókezelés (8 opció) - Milyen keretet, formát kapnak a fotók az egész oldalon.
  f1    Lekerekített, mély árnyékkal: Nagy lekerekítés és puha, mély árnyék. Letisztult, prémium, a fotó a főszereplő.
  f2    Polaroid: Fehér keretes, kicsit megdöntött „kinyomtatott” fotók kézírásos felirattal. Személyes, emlékkönyves, családias.
  f3    Boltív: Felül íves, alul szögletes forma, mint egy ablak vagy kapu. Meleg, mediterrán, elegáns.
  f4    Eltolt kontúr: Lekerekített fotó, mögötte egy eltolt, színes vonalkeret. Grafikus, rendezett, kicsit játékos.
  f5    Organikus folt: Szabálytalan, puha folt-forma, lassan lélegzik. Természetes, bio, kézműves érzet.
  f6    Színblokk mögötte: A fotó mögött egy eltolt, halvány márkaszínű blokk. Magazinos, rétegzett, mélységet ad.
  f7    Bélyeg: Fogazott szélű fehér keret, mint egy postabélyeg. Nosztalgikus, gyűjthető, egyedi.
  f8    Márkaszínű duotone: Fekete-fehér fotó márkaszínnel átszínezve. Nagyon egységes, grafikus. Ételfotóhoz NEM ajánlott (étvágytalan).

## felulet · Háttér-textúra (8 opció) - A szekciók hátterén futó finom minta.
  t1    Füzet-rács: Halvány kockás rács, ami középen elhalványul. Tervezett, rendezett, „kiszámolt” hatás.
  t2    Pöttyrács: Finom pöttyminta a szélek felé erősödve. Könnyed, modern, nem zavarja a szöveget.
  t3    Vonalas lap: Sorvonalas papír margóvonallal. Iskolás, jegyzetes, személyes.
  t4    Motívum-minta: A márka saját formáiból (lásd a Dekor-motívumokat) szőtt, halvány, ismétlődő minta. A legegyedibb felület: csak ennél a márkánál van értelme.
  t5    Színfoltok: Két nagy, elmosódott márkaszínű fényfolt a sarkokban. Meleg, lágy, „napfényes” hangulat.
  t6    Papír-szemcse: Finom, nyomott papírra emlékeztető szemcse. Kézműves, meleg, analóg; nagyon visszafogott.
  t7    Kockás terítő: Halvány, kockás terítő-minta a szekció szélein. Vendéglátós, piknikes, családias.
  t8    Tiszta felület: Nincs minta, csak a felületek színe váltakozik. A legcsendesebb; a fotók és a tipográfia viszik az oldalt.

## dekor · Dekor-réteg (7 opció) - A tartalom mögötti díszítő elemek: szellemszó, motívumok, firkák, matricák.
  d1    Szellemszó: Óriás, halvány körvonalas szó a szekciók szélén (pl. TÉSZTA, ÉTLAP). Plakátos, magabiztos, sok mélységet ad.
  d2    Lebegő motívumok: A márka saját formái (pl. tésztaforma, levél) lassan lebegnek a szekciók sarkaiban. Élő, játékos, egyedi.
  d3    Óriás jel: A márka fő motívuma óriási méretben, alig láthatóan a sarokban. Nyugodt, elegáns márkaépítés.
  d4    Gyűrű + pöttyfolt: Lassan forgó szaggatott gyűrű és egy apró pöttyfolt. Geometrikus, finom, „tervezett” díszítés.
  d5    Kézi firkák: Kézzel rajzolt hullámvonal, csillanás és hurkos nyíl. Spontán, vidám, emberi.
  d6    Matricák: Kerek, megdöntött matrica egy rövid ténnyel (pl. „Friss tészta minden reggel”) a hero-ban és a záró blokkban. Kézzelfogható, figyelemfelkeltő.
  d7    Letisztult: Nincs díszítő réteg. Minimalista; a tartalom és a fotók beszélnek.

## hatar · Szekcióhatárok (7 opció) - Hogyan válnak el egymástól a szekciók.
  s1    Hullám: Lágy hullámvonal a szekciók között. Barátságos, folyékony, természetes.
  s2    Fogazott jegy-él: Cikkcakkos él, mint egy letépett blokk vagy belépőjegy. Kereskedelmi, játékos.
  s3    Futószalag: Megdöntött, végtelenítve futó szalag a márka rövid tényeivel a szekciók határán. Fesztiválos, energikus, sok információt ad át észrevétlenül.
  s4    Ferde vágás: Átlós vágás a szekciók között. Dinamikus, lendületes, sportos.
  s5    Szakadt papír: Egyenetlen, tépett papírél. Kézműves, újságkivágásos, spontán.
  s6    Napellenző-ív: Apró félkörívek sora, mint egy bolti napellenző vagy csipke. Vendégváró, üzletes, bájos.
  s7    Varrás-vonal: Csak egy finom szaggatott vonal jelzi a határt. A legcsendesebb, letisztult megoldás.

## mozgas · Mozgás (5 opció) - Hogyan érkeznek be az elemek görgetéskor, mennyire élő az oldal.
  m1    Nyugodt úszás: Az elemek lassan, finoman úsznak be. Elegáns, pihentető.
  m2    Élénk, lépcsőzetes: Az elemek egymás után, lendületesen emelkednek be; a díszek lebegnek. Energikus, modern.
  m3    Játékos pattanás: Az elemek kicsit megdöntve, rugalmasan pattannak a helyükre; rámutatva az ikonok megbillennek. Vidám, gyerekbarát.
  m4    Filmes függöny: A blokkok alulról, függönyszerűen tárulnak fel, a fotók lassan közelítenek. Drámai, prémium, filmes.
  m5    Csendes (animáció nélkül): Nincs beúszás és lebegés, csak apró visszajelzések rámutatáskor. Gyors, akadálymentes, komoly.

## nav · Navigáció (fejléc) (6 opció) - A felső menüsáv: logó, menüpontok, fő gomb.
  n1    Lebegő kapszula: Lekerekített, üveghatású sáv, ami a tartalom fölött lebeg és görgetéskor végig látszik. Modern, könnyed.
  n2    Infósáv + menü: Vékony, sötét felső sáv a telefonnal, nyitvatartással és címmel, alatta a menü. A legtöbb gyakorlati infó azonnal látszik.
  n3    Középre zárt, függő logóval: A logó középen, egy lelógó „címke” alján; a menü két oldalt. Klasszikus bolt- és vendéglőhangulat.
  n4    Cégér (lengő tábla): A logó egy láncon lógó, finoman lengő cégtáblán, mint egy belvárosi üzlet cégére. Egyedi, emlékezetes, helyi bolt érzet.
  n5    Minimál, nagy telefonszámmal: Csak a logó, egy nagy, kattintható telefonszám és egy Menü gomb; a menüpontok lenyíló panelen. Mobilon a legtisztább.
  n6    Újságfejléc (kétszintes): Nagy, középre zárt logó vékony vonalak között, két oldalt apró infóval; alatta középre zárt menüsor. Nyomtatott étlap vagy napilap hangulat.

## hero · Hero (nyitó blokk) (7 opció) - Az első képernyő: ez dönti el, marad-e a látogató.
  h1    Színes fotókollázs: Telt márkaszínű háttér, balra a nagy cím, jobbra egymásra csúsztatott fotók, kör alakú kép és logó-matrica. Harsány, élettel teli, azonnal megjegyezhető.
  h2    Fotómozaik + álló kép: Nagy logó, apró betűs „menetrend” sor, erős cím, számok; jobbra fotómozaik egy magas képpel és halvány szellemszóval. Fesztiválos, gazdag, sokat mutat.
  h3    Teljes képes, kártyával: A legjobb fotó kitölti a teljes képernyőt, rajta egy tiszta, világos kártya a címmel és a gombokkal. Hangulatos, „itt vagy” érzés.
  h4    Plakát-tipográfia: Óriási, plakátszerű cím a teljes szélességben, alatta egy lépcsőzetes fotósor pecséttel. Magabiztos, városi, nagyon karakteres.
  h5    Osztott, nagy fotóval: Kettéosztott kép: balra halvány márkaszínű panel a szöveggel, jobbra egy nagy, magas fotó lebegő kiemelő-kártyával. Letisztult, magazinos, prémium.
  h6    Középre zárt, lebegő fotókkal: Középen a cím és a gombok, körülötte négy fotó lassan lebeg a sarkokban. Nyitott, barátságos, játékos.
  h7    Krétatábla: Balra a cím, jobbra egy fakeretes krétatábla a kedvenc tételekkel és árakkal, sarkán egy kerek fotóval. Vendéglátós, őszinte, azonnal informál.

## tenyek · Tények / bizalom (6 opció) - A hero alatti gyors bizonyítékok: miért ti.
  p1    Tény-kártyák számokkal: Kártyasor: ikon, nagy szám vagy kulcsszó, rövid magyarázat. A kártyák a választott kártyastílust kapják.
  p2    Futó tény-szalag: Megdöntött, végtelenül futó szalag a legfontosabb tényekkel és ikonokkal, közvetlenül a hero alatt. Fesztiválos energia, kevés helyen sok infó.
  p3    Ikonos sor elválasztókkal: Egyetlen tiszta sor: ikon és rövid szöveg, szaggatott vonalakkal elválasztva, kártyák nélkül. Levegős, gyorsan olvasható.
  p4    Minőségi pecsétek: Kerek pecsétek körbefutó felirattal (lassan forognak), középen ikon, alatta a tény. Kézműves „garancia” hatás.
  p5    Szerkesztőségi számok: Balra a szekció címe, jobbra 2×2 rácsban nagy számok vagy kulcsszavak vékony vonalakkal. Magabiztos, adatvezérelt, magazinos.
  p6    Chip-felhő: Középre zárt, enyhén megdöntött „címkék” ikonnal. Könnyed, kompakt, ha a tények rövidek.

## kinalat · Kínálat (7 opció) - A fő termék- vagy szolgáltatáscsoportok bemutatása.
  k1    Ikonos kártyarács: Minden kategória egy kártya: ikon és cím egy sorban, rövid leírás, ár-tól. Rendezett, gyorsan átlátható.
  k2    Fotós csempék: Kártyák nagy fotóval a tetején, alatta ikon, cím, leírás és ár-címke. Étvágycsináló, a fotók adják el.
  k3    Bento-rács: Egy nagy, fotós kiemelt csempe és mellette kisebb kártyák aszimmetrikus rácsban. Modern, dinamikus, a fő terméket előtérbe tolja.
  k4    Vízszintes sín: Oldalra görgethető, magas fotós kártyák nyilakkal és haladásjelzővel. Sok elemnél is rendezett; mobilon ujjal húzható.
  k5    Váltakozó sorok: Minden kategória egy teljes sor: nagy fotó és szöveg felváltva balra-jobbra, nagy kontúros sorszámmal. Mesélős, magazinos, prémium.
  k6    Fülek (lapozós): Kapszula-fülek ikonokkal; kattintásra vált a nagy fotós panel. Kevés helyen sokat mutat, interaktív.
  k7    Kerek fotók ikon-matricával: Nagy, kerek fotók fehér gyűrűvel, szélükön ikon-matrica, alatta név és ár. Egyszerű, barátságos, „válassz egyet”.

## ajanlat · Kiemelt tételek árakkal (6 opció) - Néhány konkrét termék vagy csomag, árral.
  a1    Étlap pontozott vonallal: Nyomtatott étlap-lap két hasábban: név, pontozott vezetővonal, ár, alatta a leírás és címkék. Klasszikus, azonnal érthető.
  a2    Termékkártyák sínben: Fotós termékkártyák oldalra görgethető sínben, mindegyiken lógó árcédula. Webshopos, lendületes.
  a3    Csoportok fülekkel: Kategória-fülek (pl. Tészták, Rizottók…), alattuk tiszta árlista. Sok tételnél is áttekinthető.
  a4    Kiemelt tétel + lista: Balra egy nagy kiemelt kedvenc fotóval és árral, jobbra a többi tétel kis kerek képpel. Irányítja a választást.
  a5    Árcédulás rács: Fotós kártyák rácsban, mindegyik sarkán lógó, megdöntött árcédula. Piaci, kézzelfogható, jól szkennelhető.
  a6    Krétatábla-étlap: Sötét, fakeretes krétatábla kézírásos címekkel és pontozott árlistával. Bisztró-hangulat, nagyon karakteres.

## folyamat · Folyamat (így működik) (5 opció) - A lépések, ahogy a vevő megkapja, amit szeretne.
  f1    Pontozott útvonal: Lépés-kártyák egy szaggatott útvonalon, mindegyik tetején számozott pecsét. Egyértelmű, barátságos, „ilyen egyszerű”.
  f2    Cikcakk idővonal: Függőleges, szaggatott idővonal; a lépések felváltva balra és jobbra ülnek, középen ikonos pontokkal. Mesélős, „a tészta útja”.
  f3    Óriás sorszámok: Hatalmas, kontúros sorszámok vastag vonal alatt, mellettük ikon és rövid szöveg. Szerkesztőségi, magabiztos, sok levegővel.
  f4    Felfelé lépcső: A lépés-kártyák lépcsőzetesen emelkednek balról jobbra, mintha felfelé vinnének. Fejlődés, haladás érzete.
  f5    Futószalag: Egy mozgó futószalag állomásokkal: minden lépés egy ikonos állomás a szalag felett. Játékos, „gyártósor” metafora, jól mutatja a folyamatot.

## tortenet · Rólunk / történet (5 opció) - Az emberek és a történet a márka mögött.
  t1    Fotó + személyes levél: Nagy portré vagy hangulatfotó, mellette a történet, egy kiemelt idézet és kézírásos aláírás. Őszinte, személyes, bizalmat épít.
  t2    Szórt fotókollázs: Balra a történet, jobbra három egymásra dobott, feliratos fotó. Emlékalbumos, családias, meleg.
  t3    Mérföldkő-idővonal: Rövid történet fotóval, alatta vízszintes idővonal a fontos dátumokkal és tényekkel. Tárgyilagos, hiteles, „így jutottunk ide”.
  t4    Nagy idézet: Óriás idézőjel és egy nagy, kiemelt mondat a tulajdonostól, kerek portréval; alatta két hasábban a történet. Erős, emberi, emlékezetes.
  t5    Levélpapír: A történet egy vonalas levélpapíron, ragasztószalaggal felragasztott fotóval és aláírással. Kézzel írt levél hatás, nagyon személyes.

## galeria · Galéria (5 opció) - Hangulat: a hely, a termékek, az emberek.
  g1    Mozaik-rács: Különböző méretű fotók szoros mozaikban, rámutatva felirattal. Gazdag, rendezett, „nézz körül”.
  g2    Asztalra szórt fotók: Kicsit ferdén, egymásra csúszva szórt fotók; rámutatva kiegyenesednek és előrejönnek. Játékos, emlékalbumos.
  g3    Nagy kép + bélyegképek: Egy nagy, széles fotó, alatta kattintható bélyegképek. Egyszerre mutat sokat és semmi nem zsúfolt.
  g4    Végtelen fotósáv: A fotók lassan, végtelenítve úsznak a képernyőn keresztül. Élő, pörgős hangulat, kevés szöveggel.
  g5    Boltíves ablaksor: Egymás mellett álló, magas boltíves „ablakok” a fotókkal, alattuk kézírásos felirat. Mediterrán, elegáns, nyugodt.

## latogatas · Kapcsolat / látogatás (6 opció) - A záró blokk: hol, mikor, hogyan érsz el minket.
  l1    Színes sáv + nyitvatartás-kártya: Telt márkaszínű blokk nagy meghívással és gombokkal, mellette tiszta nyitvatartás-kártya élő „most nyitva” jelzéssel.
  l2    Sötét blokk, óriás telefonszámmal: Középre zárt, sötét záró blokk, benne a telefonszám óriási, kattintható betűkkel. Egyértelmű: „hívj, és kész”.
  l3    Belépőjegy: A kapcsolati adatok egy nagy, perforált belépőjegyen: a letéphető szelvényen a nyitvatartás, a fő részen a cím és a gombok. Játékos, emlékezetes.
  l4    Stilizált térkép: A háttér egy rajzolt, márkaszínű „térkép” lüktető tűvel; előtte kártya a címmel, nyitvatartással és útvonal-gombbal. Helyi, „itt vagyunk”.
  l5    Fotó + két infóhasáb: Balra az üzlet fotója, jobbra meghívó cím és két tiszta hasáb: nyitvatartás és elérhetőség. Egyszerű, informatív.
  l6    Hírlevél-doboz + infó: Nagy, lekerekített doboz: balra a hírlevél-meghívás (újdonságok, akciók), jobbra a nyitvatartás és elérhetőség. Visszatérő vendégeket épít.

## lablec · Lábléc (5 opció) - Az oldal alja: elérhetőség, menü, jogi linkek.
  lb1   Sötét, négy hasábos: Klasszikus sötét lábléc: logó és rövid szöveg, oldalak, elérhetőség, nyitvatartás; alul a jogi sor. Teljes, rendezett.
  lb2   Óriás márkanév: Világos lábléc, alján a márkanév a teljes szélességben, óriási betűkkel. Magabiztos, modern, erős lezárás.
  lb3   Középre zárt, minimál: Minden középen: logó, egy sor menü pontokkal elválasztva, közösségi ikonok, apró betűs adatok. Csendes, elegáns.
  lb4   Színes, lekerekített: Márkaszínű lábléc lekerekített felső sarkokkal, ami ráfut az előző blokkra; tetején nagy felhívás és telefonszám. Barátságos, lendületes.
  lb5   Nyugta (blokk): A lábléc egy középre zárt, fogazott szélű pénztárblokk írógépes betűkkel: nyitvatartás, telefon, e-mail „tételekként”. Vicces, emlékezetes, vendéglátós.
```
