# Webdesign arculat-generátor: telepítés és használat

Ez a skill egyetlen weboldal-címből (URL) elkészíti a vállalkozásod új webes arculatát. Először egy
**arculat-választót** kapsz: minden elemből (színek, betűk, ikonok, gombok, kártyák, nyitó blokk, és így tovább)
legalább 5 változatot, amelyekhez megjegyzést írhatsz, és kijelölheted a véglegeset. Az oldal alján azonnal látod,
hogyan néz ki együtt, amit kiválasztottál. A visszajelzésed alapján elkészül a kész főoldal és a designrendszer leírása.

## Amire szükséged lesz
1. **Claude-előfizetés**, amiben elérhetők a Skillek és a kódfuttatás (Pro, Max, Team vagy Enterprise).
2. **OpenAI API-kulcs** az egyedi ikonokhoz. Egy teljes ikonkészlet (40 ikon) kb. 150-250 Ft.
   - platform.openai.com → bejelentkezés → **API keys** → *Create new secret key* → másold ki (`sk-...`).
   - Tölts fel pár dollár egyenleget (Settings → Billing).
   - Ha a képgeneráláshoz az OpenAI „Verify organization”-t kér: Settings → Organization → General → *Verify*.
     Ez egyszeri, pár perces lépés.

## Telepítés Claude.ai-ban (web vagy asztali app)
1. **Settings → Capabilities**: kapcsold be a *Code execution and file creation* opciót.
2. Ugyanitt a hálózati hozzáférésnél engedélyezd a kimenő forgalmat: *All domains*, vagy vedd fel az engedélyezett
   domainek közé: a saját weboldalad domainjét, `api.openai.com`, `fonts.googleapis.com`, `api.frankfurter.app`.
3. **Settings → Capabilities → Skills → Upload skill**: töltsd fel a kapott `webdesign-arculat-generator.zip` fájlt.
4. Készíts egy szöveges fájlt `openai-kulcs.txt` néven, egyetlen sorral: az `sk-...` kulcsod.

## Használat
1. Új beszélgetésben töltsd fel az `openai-kulcs.txt`-t, és írd be: *„Készíts arculatot és új főoldal-designt ehhez a
   weboldalhoz: https://…”*
2. Pár perc múlva kapsz egy `…-arculat-valaszto.html` fájlt. Töltsd le, és nyisd meg a böngésződben.
3. A választóban:
   - **kattints** bármelyik változatra: legalul, az élő oldalon azonnal úgy jelenik meg,
   - **★ Ez legyen a végleges**: így jelölöd a kedvencet (bármikor átjelölheted),
   - **megjegyzés**: minden változat alatt írhatsz, mi tetszik és mi nem,
   - ha egy elemnél egyik sem jó: pipáld be, hogy **„kérek újakat”**,
   - az élő oldalt **mobil nézetben** is megnézheted.
   A jelöléseid a böngészőben mentődnek, nyugodtan bezárhatod és később folytathatod.
4. Ha kész vagy: **📋 Visszajelzés másolása** → *Másolás* → illeszd be a Claude-os beszélgetésbe.
5. Claude összefoglalja, mit értett, és ha kell, új változatokat készít. Ha minden megvan, elkészíti a **kész
   főoldalt** (`fooldal.html`) és a **DESIGN-RENDSZER.md**-t, amiből később bármelyik új aloldal ugyanígy készülhet.

## Telepítés Claude Code-ban
Másold a skill mappáját a `~/.claude/skills/` alá (vagy telepítsd pluginként), és állítsd be a kulcsot:
`export OPENAI_API_KEY=sk-...`, vagy tedd egy `openai-kulcs.txt` fájlba a munkamappába. Ha van Google Chrome a gépen,
Claude képernyőképekkel ellenőrzi a munkáját.

## Jó tudni
- A tényeket (árak, nyitvatartás, nevek) a mostani oldaladról veszi, betűre. Vásárlói véleményt, számot nem talál ki.
  Ha van jó véleményed vagy fotód, add meg, és bekerül.
- A kulcsodat a skill nem írja ki és nem teszi bele a kész fájlokba.
- A kész oldal egyetlen HTML-fájl (a képek benne vannak). A weboldaladba a fejlesztőd vagy egy Claude-os
  beszélgetés tudja beépíteni (WordPress, Webflow, egyedi oldal).
