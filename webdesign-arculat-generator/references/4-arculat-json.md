# 4 - Az `arculat.json` sémája

A fájl a munkamappában van, az
útvonalak (fotók, logó, ikon-spec) ehhez képest relatívak. Minden mező opcionális, ami hiányzik, kimarad az oldalról.
Szövegekben: `==kiemelt szó==` (a címsor-stílus emeli ki), `**félkövér**`, ` | ` sortörés.

```jsonc
{
  "verzio": 1,                               // választó-kör; új kör = +1 (új localStorage-kulcs)
  "marka": {"nev": "", "szlogen": "", "slug": "kisbetus-kotojeles", "url": "https://..."},
  "seo": {"title": "", "description": ""},   // a végleges oldal <head>-je
  "logo": {"fajl": "bemenet/kepek/logo.png", "feher_fajl": null},   // a fehér változatot a motor elkészíti, ha nincs
  "profil": {"osszefoglalo": "", "talalt_szinek": ["#..."], "talalt_betuk": [""], "motivumok": ""},
  "motivum": {
    "formak": {"nev1": "<path d='...'/>", "nev2": "...", "nev3": "..."},   // 100x100, fekete; az első 3 a textúra
    "jel": "nev1",                                                        // az óriás jel
    "szellemszavak": {"hero": "", "tenyek": "", "kinalat": "", "ajanlat": "", "folyamat": "", "tortenet": "", "galeria": "", "latogatas": ""},
    "ticker": ["rövid tény", "..."],          // futószalag
    "matricak": ["2-4 szó", "..."]            // kerek matricák
  },
  "fotok": {"id": {"fajl": "bemenet/kepek/x.jpg", "alt": "", "pozicio": "50% 40%", "max": 1280}},
  "kapcsolat": {"telefon": "", "email": "", "cim": "", "terkep_url": "",
                "nyitvatartas": [["Hétfő–péntek", "9:00–17:00"]], "nyitva_rovid": "H–P 9–17",
                "nyitva_gep": {"1": [9, 17], "7": null},      // 1=hétfő; a „Most nyitva / zárva” jelzéshez
                "social": [{"tipus": "facebook", "url": ""}]},
  "nav": {"linkek": [["Szöveg", "#horgony"]], "cta": {"szoveg": "", "href": "tel:+36...", "ikon": "tel"}, "nev_mutat": true},
  "hero": {"kicker": "", "meta": "apró sor **kiemeléssel**", "badgek": [{"ikon": "ora", "szoveg": ""}],
           "cim": "Cím ==kiemelt==", "lead": "", "cta1": {"szoveg": "", "href": ""}, "cta2": {"szoveg": "", "href": "", "ikon": "tel"},
           "jegyzet": "kézírásos megjegyzés", "statok": [["2023", "óta"]], "fotok": ["id1", "id2", "id3", "id4"],
           "fotok_h5": ["id"],                // változatonként más fotó-sorrend (h1..h7)
           "kiemelt": {"ikon": "", "cim": "", "szoveg": ""},             // h5 lebegő kártya
           "tabla": {"cim": "", "sorok": [["tétel", "ár"]], "lab": ""}}, // h7 krétatábla
  "tenyek": {"kicker": "", "cim": "", "elemek": [{"ikon": "", "szam": "rövid kulcsszó/szám", "cim": "", "szoveg": "", "korszoveg": "pecsét-felirat"}]},
  "kinalat": {"kicker": "", "cim": "", "lead": "", "cta": {},
              "elemek": [{"nev": "", "leiras": "", "ar": "", "ikon": "", "foto": "", "link": "", "link_szoveg": ""}]},
  "ajanlat": {"kicker": "", "cim": "", "lead": "", "lab": "apró megjegyzés", "cta": {},
              "elemek": [{"nev": "", "leiras": "", "ar": "", "cimkek": [""], "foto": "", "csoport": "a3 fülekhez"}]},
  "folyamat": {"kicker": "", "cim": "", "lepesek": [{"ikon": "", "cim": "", "szoveg": ""}]},        // 3-5 lépés
  "tortenet": {"kicker": "", "cim": "", "bekezdesek": [""], "idezet": "", "alairas": {"nev": "", "szerep": ""},
               "fotok": ["id"], "fotok_felirat": [""], "foto_felirat": "", "merfoldkovek": [["év", "szöveg"]]},
  "galeria": {"kicker": "", "cim": "", "fotok": [{"id": "", "felirat": ""}]},                      // 4-6 fotó
  "latogatas": {"kicker": "", "cim": "", "lead": "", "cta1": {}, "cta2": {}, "foto": "id"},
  "hirlevel": {"kicker": "", "cim": "", "szoveg": "", "cta": {"szoveg": "", "href": ""}},           // l6
  "lablec": {"szoveg": "", "cegnev": "", "felhivas": "", "linkek": [["", ""]], "jogi": [["", ""]]},
  "ikonok": {"spec": "ikon-spec.json"},
  "szekcio_sorrend": ["nav", "hero", "kinalat", "tortenet", "gyik", "latogatas", "lablec"],   // A BEADOTT OLDAL szekciói, sorban
  "egyedi_szekciok": {"gyik": {"nev": "GYIK", "leiras": "Gyakori kérdések"}},   // ha egy szekció nem illik a motor típusaihoz
  // -> egyedi_opciok.gyik: 5 változat (html + css). Minden szekció-kategóriában 5 opció.
  "opciok": {
    "paletta": {"ajanlott": "p1", "lista": [{"id": "p1", "nev": "", "miert": "", "primary": "#", "accent": "#", "accent2": "#", "paper": "#", "ink": "#", "deep": "#", "card": "#", "mod": "sotet"}]},
    "betu": {"ajanlott": "b1", "lista": [{"id": "b1", "nev": "", "miert": "", "display": "", "body": "", "hand": "", "label": "", "w_display": 700, "ls_display": "-0.02em", "nagybetus": false, "lh_display": 1.06, "hero_scale": 1, "fs_hand": 1.25}]},
    "ikon": {"ajanlott": "i1", "miert": {"i1": ""}},
    "cim": {"ajanlott": "cE", "lista": ["cE", "cM", "cB", "cF", "cK"], "miert": {"cE": "márkára szabott indoklás"}}
    // 5 opció, 5 karakter (elegáns · modern · merész · barátságos · klasszikus), a CSS az egyedi_opciok-ban.
    // felulet, dekor, hatar: KÖTELEZŐEN egyedi_opciok (az ügyfél témájából), lásd references/7-alap-es-tema.md
    // ... ugyanígy: alcim, gomb, kartya, foto, felulet, dekor, hatar, mozgas, nav, hero, tenyek, kinalat, ajanlat,
    //     folyamat, tortenet, galeria, latogatas, lablec
  },
  "egyedi_opciok": {
    "kartya": [{"id": "rx1", "nev": "", "leiras": "", "css": "%S .krt{...}"}],             // globális stílus: %S szűkít
    "hero":   [{"id": "hx1", "nev": "", "leiras": "", "html": "<section class='sec v-hx1' id='top'>...</section>", "css": ".v-hx1{...}"}]
  },
  "egyedi_css": ""                            // finomítás a visszajelzés után (a választó és a végleges oldal végére)
}
```

## Ikon-nevek
Az ikon-mezők (`ikon`) az `ikon-spec.json` → `ikonok[].nev` értékei. A beépített UI-ikonok (gombokban, chipekben:
`ikon` kulcs a gomb/badge objektumokban): `tel pin ora mail nyil le pipa csillag fb ig menu plusz bal jobb szem szoveg haz kulcs`.

## CSS-változók, amiket egyedi opcióban használhatsz
Színek: `--c-primary(-d,-dd,-l,-ll) --c-accent(-d,-l) --c-accent2 --c-paper --c-card --c-tint --c-sand --c-deep --c-ink
--c-ink-2 --c-ink-3 --c-head --c-line --c-line2 --c-on-primary --c-on-accent --hl` (kiemelt szöveg színe az adott
felületen) · betűk: `--f-display --f-body --f-hand --f-label --w-display` · egyéb: `--r --sh-1 --sh-2 --sh-3 --ease
--logo-img --logo-eredeti --m1 --m2 --m3 --mjel --minta --zaj`. Felület-osztályok: `.s-paper .s-white .s-tint .s-sand
.s-deep .s-primary`, a színes felületen belüli világos doboz: `.s-vilagos`.

## Mentés artifactban
A választó artifactként (`capabilities: {"db": {}}`) az `arculat/valasztas-v<verzio>` dokumentumba ment:
`{allapot, gepi, szoveg, frissitve, verzio}`. A `gepi` a GÉPI ADAT JSON (ugyanaz, mint a „Visszajelzés másolása”
végén), ezt mentsd `valasztas.json`-ba, és az `epit.py oldal` / `--elozo` közvetlenül érti.
