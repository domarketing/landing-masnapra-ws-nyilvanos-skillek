# 7 - Az opciók megírása: 5 karakter (alap-elemek) + az ügyfél témája (textúra, dekor, határ)

## A. Alap-elemek: 5 eltérő karakter, mind márkára hangolva

Paletta, betűpár, ikonstílus, címsor, alcím, gomb, kártya, fotókezelés, mozgás. Az 5 opció 5 KÜLÖNBÖZŐ KARAKTER,
de mind az ügyfélé: az ő színei, az ő hangneme, az ő tárgyainak apró részletei (pl. pénzügyi oktatónál az arany
pecsét éle a gombon; tésztázónál a kraft doboz). Tisztességes, modern webdesign, nem kísérleti művészet.

| Karakter | Gomb (példa) | Címsor-kiemelés | Alcím | Kártya | Fotó |
|---|---|---|---|---|---|
| Elegáns | szögletes, ritkított nagybetű, vékony márka-éllel | dőlt, kiemelő színnel | ritkított, két hajszálvonal | vékony belső keret | nagy lekerekítés, mély árnyék |
| Modern | lekerekített, nyíl külön dobozban | vékony színes aláhúzás | kapszula pöttyel | kétszínű felső sáv | eltolt kontúr |
| Merész | telt kiemelő színű kapszula „talppal” | vastag kiemelő-csík | sötét címke | vastag keret, kemény eltolt árnyék | színblokk mögötte |
| Barátságos | puha pill, színes derengés | kézírásos szó | kézírásos felvezető | puha, színezett, nagy lekerekítés | „kinyomtatott” fotó |
| Klasszikus | dupla keret (oklevél/bankjegy) | könyvelői dupla aláhúzás | sorszámozott (01, 02…) | okirat/étlap-keret | paszpartu |

A táblázat kiindulópont: a részletet mindig az ügyfélből vezesd le (szín, anyag, a szakma egy apró jele). A palettánál
legyen egy hű (a mostani színek igényesebb változata) és egy sötét/prémium; a betűknél legyen egy, ami a mostanihoz
közel áll. Írd meg a CSS-t `egyedi_opciok.<kategória>` alá (`%S` = a kategória data-attribútuma, `%K` = keyframe-előtag);
a könyvtári opciók (`epit.py lista`) CSS-e jó kiindulás, de igazítsd az ügyfélre. A `miert` mindig a márkáról szóljon.

## B. Téma-elemek: textúra, dekor, határ az ügyfél FŐ TÉMÁJÁBÓL

Kérdés: *„Milyen képek, minták, tárgyak jutnak eszébe valakinek erről a szakmáról?”* Ezekből 5-5 ötlet. Nem kell
külön „koncepció”: a téma maga a forrás.

| Téma | Textúra (háttér) | Dekor (lebegő/óriás díszek) | Határ (szekciók között) |
|---|---|---|---|
| Pénzügy, befektetés | árfolyamgörbe, bankjegy-guilloche, gyertyadiagram, kamatos kamat-görbék, mikroírás | érmék, növekedési nyíl, mini-grafikonok, rozetta, garancia-pecsét | hozamgörbe-él, árfolyam-cikcakk, tőzsdei ticker, bankjegy-hullám, oszlopdiagram |
| Étterem, étel | kockás terítő, receptkártya-vonalak, liszt-szemcse | gőz, fűszerlevelek, tányérperem, matrica | napellenző-ív, tépett étlap, kenyérhéj-él |
| Fogászat, egészség | finom fogkontúr-minta, tiszta pöttyrács | csepp, fogkefe-fej, tükör-kör | hullámos „mosoly” ív, steril varrásvonal |
| Ács, építőipar | tervlap-rács, faerezet | szögfej, fecskefark-kötés, mérőszalag | fűrészfog, mérőszalag-vonalzó |
| Oktatás, gyerek | füzetrács, krétatábla-szemcse | ceruza, betűkockák, matrica | vonalas füzetlap-él, cikcakk |

Technika:
- **Textúra**: `%S .tx::before{background-color:var(--c-primary);-webkit-mask:url(<svg>) …;mask:…;opacity:.07-.15}`.
  Az SVG-t Pythonból generáld (pl. egy árfolyam-pontokat számoló függvény + Catmull-Rom görbe).
  Sötét felületre `%S .s-deep.tx::before{background-color:var(--c-deep-hl)}`.
- **Dekor**: a `.dk` elemei (`dk-a dk-b dk-c dk-jel dk-r dk-f1 dk-f2 dk-szo dk-m`) alapból rejtettek; az opció
  megjeleníti és formázza őket (maszk-SVG, animáció `%K`-val). A `dk-m` a matrica szövegét kapja (motivum.matricak).
  Mobilra csak 340 px alatt rejts el, különben a választó keskeny demóiban sem látszik.
- **Határ**: a `.hat` a szekció tetején ül (alapból 0 magas); maszkkal formázd (`background:var(--sec-bg)`), vagy a
  `.hat .tick` futószalagot jelenítsd meg (motivum.ticker). **Váltakozó határ**: a motor minden `.hat`-ot sorszámoz
  (`data-hn` = 0/1/2 az oldal sorrendjében), így `%S .hat[data-hn="0"]{…} %S .hat[data-hn="1"]{…}` háromféle határt
  ad egymás után.
- Mind az 5 legyen jól látható a demóban, és ne nyomja el a szöveget.

## C. Szekciók: a beadott oldal szekciói, 5-5 elrendezés

A `szekcio_sorrend` a beadott oldal szekcióit sorolja (amit ott találsz, abban a sorrendben). Szekciónként 5
elrendezés: a motor típusaiból (`nav hero tenyek kinalat ajanlat folyamat tortenet galeria latogatas lablec`,
`epit.py lista`) válassz 5 illőt, vagy írj egyedit (`egyedi_opciok.<szekció>`: `html` + `css`, a CSS a `.v-<id>`
osztályra szűkítsen). Ha egy szekció egyik típushoz sem illik (pl. „Árak”, „GYIK”, „Csapat”), vedd fel:
`"egyedi_szekciok": {"gyik": {"nev": "GYIK", "leiras": "Gyakori kérdések"}}`, és írj hozzá 5 változatot.
