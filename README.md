# Landing Másnapra ws - nyilvános skillek

A Landing Másnapra workshop résztvevőinek összeállított, Claude-hoz készült skillek.

| Skill | Mire jó |
|---|---|
| [`ertekesitesi-oldal-keszito`](ertekesitesi-oldal-keszito) | Vázlatból vagy dokumentumból magyar értékesítési oldalt (egyetlen HTML-fájlt) készít a 16 legókockás keretrendszer szerint. |
| [`webdesign-arculat-generator`](webdesign-arculat-generator) | Egy weboldal címéből arculat-választót, majd a kiválasztott elemekből kész főoldalt és designrendszer-leírást készít. A telepítés leírása a `TELEPITES.md`-ben van. |
| [`szovegellenorzo`](szovegellenorzo) | Kész magyar szövegből kiszedi az AI-ra árulkodó mintákat, és méri az eredményt. |

## Telepítés

**Claude Code:** másold a kívánt skill mappáját a `~/.claude/skills/` alá, és indíts új sessiont.

**Claude.ai / asztali app:** tömörítsd ZIP-be a skill mappáját, majd Settings → Capabilities → Skills → Upload skill.

A skillek együtt működnek: az értékesítési oldal készítő a végén a szövegellenőrzőt futtatja, ezért érdemes mindkettőt telepíteni.

## Mire figyelj

- A webdesign-generátor ikongenerálásához saját OpenAI API-kulcs kell. A kulcsot soha ne tedd fel a repóba.
- A skillek kiindulópontok. A saját márkádra, ajánlatodra és hangodra neked kell szabnod őket.
