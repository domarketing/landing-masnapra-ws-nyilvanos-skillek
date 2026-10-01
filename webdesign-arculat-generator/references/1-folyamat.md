# 1 - Folyamat a gyakorlatban: környezet, hálózat, kulcs, átadás

## Hol fut a skill?

| | Claude Code (asztali / terminál) | Claude.ai (web, asztali app, „Skills” funkció) |
|---|---|---|
| Skill helye | a plugin mappája | `/mnt/skills/user/<skill>/` (vagy ahova a feltöltés tette; keresd: `find / -name SKILL.md -path "*arculat*" 2>/dev/null`) |
| Munkamappa | a felhasználó mappájában új almappa: `<marka>-arculat/` | `/mnt/user-data/outputs/<marka>-arculat/` |
| Kimenet átadása | útvonal + `open <fájl>` (Mac) | a HTML az outputs mappában: a felhasználó letölti és böngészőben nyitja meg |
| Képernyőkép (QA) | van Chrome → `scripts/kepernyokep.py` | általában nincs böngésző → `scripts/ellenorzo.py`; ha van Playwright, a kepernyokep.py azt használja |
| Hálózat | szabad | a kódfuttatás hálózati engedélyétől függ (lásd lent) |

A választó egyetlen önálló HTML (minden kép, ikon, CSS, JS benne van; csak a Google Fonts jön a netről).
**Ha van `Artifact` eszköz: mindig artifactként publikáld** (`epit.py valaszto … --artifact`, majd publish a
`-artifact.html`-lel és `capabilities: {"db": {}}`-vel). Ott a jelölések és megjegyzések az artifact adatbázisába
mentődnek (`arculat/valasztas-v<verzio>`), és `ArtifactData get`-tel kiolvasod (a `gepi` mező → `valasztas.json`).
Helyi fájlként a böngésző localStorage-a ment, a visszajelzés útja: **„Visszajelzés másolása” → beillesztés a chatbe**.

## Hálózat (Claude.ai)

A skillnek három helyet kell elérnie:
1. az ügyfél weboldalát (letöltés, képek),
2. `api.openai.com` (ikonok),
3. opcionálisan `api.frankfurter.app` (árfolyam a forintos költséghez; ha nincs, 330 Ft/USD-vel számol).

Ha a letöltés `403`, `Forbidden`, `ProxyError` vagy „host not allowed” hibát ad: a felhasználónak a Claude beállításaiban
engedélyeznie kell a hálózati hozzáférést (Settings → Capabilities → Code execution → „Allow network egress”: *All
domains*, vagy a fenti domainek felvétele az engedélyezett listára). Ezt pontosan így írd meg neki, egyszer.

**Ha nem tudja engedélyezni:** a szöveget a beépített web-olvasó eszközzel (web_fetch) szedd le oldalanként, a
felhasználótól kérj: logót (PNG/SVG), 1 képernyőképet a mostani oldalról és 6-15 fotót. A színeket a logóból és a
képernyőképből olvasd ki (`oldal_kinyero.py` nélkül is: Pillow `quantize`). Ikonok ilyenkor nincsenek (nincs
OpenAI-elérés) → az ikon-kategóriát kihagyod, és ezt jelzed.

## OpenAI-kulcs

`python3 <SKILL>/scripts/ikon_generalo.py --check` → `OK` / `NO_KEY`. Ha nincs kulcs, ezt írd a felhasználónak
(egyszer, röviden):

> Az egyedi ikonokhoz egy OpenAI API-kulcs kell (platform.openai.com → API keys → Create new secret key).
> A legegyszerűbb: tedd egy `openai-kulcs.txt` nevű fájlba (egyetlen sor: `sk-...`), és töltsd fel ide. Egy teljes
> ikonkészlet (40 ikon, 5 stílus) kb. 150-250 Ft. Ha a képmodellhez „Verify organization” kell, azt az OpenAI-oldalon
> egyszer el kell végezni (Settings → Organization → General).

A szkript sorrendben keresi: `OPENAI_API_KEY` környezeti változó → `--kulcs-fajl` → `openai-kulcs.txt` a munkamappában
vagy feljebb → `/mnt/user-data/uploads/openai-kulcs.txt` → `~/.config/openai-kulcs.txt`. Ha a felhasználó a chatbe
írja a kulcsot, tedd a munkamappán KÍVÜLI helyre (`~/.config/openai-kulcs.txt`, 600-as jog), és soha ne írd vissza,
ne tedd a kimenetek közé.

Modell: `gpt-image-2.5-flare` (a leggyorsabb, legjobb), ha a fiókon nem elérhető, automatikusan `gpt-image-2` →
`gpt-image-1.5` → `gpt-image-1`. Egy példafutás mérése: 40 ikon 86 mp alatt, 0,56 USD ≈ 178 Ft.

## Időzítés, költség, iteráció

- Kinyerés: 1-2 perc. Arculati mag + JSON: ez a legtöbb gondolkodás, nem kell sietni. Ikonok: 1-3 perc. Építés: 10-30 mp.
- Második kör (új opciók): `verzio` +1, csak az érintett kategóriák opcióit cseréld, és építsd így:
  `epit.py valaszto arculat.json --elozo valasztas.json`. A szerkezet ugyanaz marad (12 arculati kategória + az oldal szekciói); az előző
  véglegesek előre bejelölve, az előző megjegyzések „Előző kör:” címkével az opciók mellett, az új opciókon „Új”
  jelvény, a kért kategóriákon „Új opciók a kérésed alapján”.
- A végleges oldal után az ügyfél kérhet még finomítást: kis módosítás → `egyedi_css` vagy tartalom; nagy → új
  választó-kör csak arra az elemre.
