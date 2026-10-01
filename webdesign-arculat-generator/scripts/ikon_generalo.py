#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ikon_generalo.py - egyedi ikonkészletek OpenAI képmodellel, TÖBB STÍLUSBAN egyszerre (az arculat-választóhoz).

  python3 ikon_generalo.py --check                         -> OK / NO_KEY / HIBA: <ok> (a kulcsot nem írja ki)
  python3 ikon_generalo.py --spec ikon-spec.json           -> generálás (párhuzamosan), optimalizálás, költség forintban
  python3 ikon_generalo.py --spec ikon-spec.json --csak i2 -> csak egy stílus (pl. újragenerálás a végleges palettával)
  python3 ikon_generalo.py --spec ikon-spec.json --ujra    -> a meglévő fájlokat is újragenerálja

ikon-spec.json:
{
  "mappa": "ikonok",                      # ide: ikonok/<stílus-id>/<ikon-nev>.png
  "quality": "medium",                    # low | medium | high  (medium ≈ 4-5 Ft/ikon)
  "szinek": {"primary": "#1f5e4b", "accent": "#c8925a", "ink": "#1e2a24"},
  "stilusok": [{"id": "i1", "nev": "Lapos kétszínű", "elotag": "Flat vector icon ... {primary} ... {accent} ..."}],
  "ikonok":   [{"nev": "teszta", "tema": "a bowl of fusilli pasta with a fork"}]
}
A {primary} {accent} {ink} helyére a színek kerülnek. Minden prompt végére automatikusan bekerül az
átlátszó háttér + „semmi szöveg” záradék.

KULCS (sorrendben): OPENAI_API_KEY környezeti változó -> --kulcs-fajl <út> -> openai-kulcs.txt a munkamappában
vagy feljebb -> /mnt/user-data/uploads/openai-kulcs.txt (Claude.ai feltöltés) -> ~/.config/openai-kulcs.txt.
A kulcsot a szkript SOHA nem írja ki, nem naplózza.

MODELL: gpt-image-2.5-flare, ha nem elérhető a fiókon, automatikusan gpt-image-2 -> gpt-image-1.5 -> gpt-image-1.
(Az OPENAI_IMAGE_MODEL változóval felülírható.) A gpt-image modellekhez az OpenAI-nál szervezet-ellenőrzés
(Verify organization) kellhet; ha ez hiányzik, a hibaüzenet megmondja.
"""
import sys, os, json, base64, time, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API = "https://api.openai.com/v1/images/generations"
MODELLEK = [m for m in [os.environ.get("OPENAI_IMAGE_MODEL", "").strip()] if m] + [
    "gpt-image-2.5-flare", "gpt-image-2", "gpt-image-1.5", "gpt-image-1"]
TOKEN_USD = {"text_in": 5.0, "image_in": 8.0, "image_out": 30.0}   # USD / 1M token (gpt-image-2.5 / 2)
ZARADEK = (" Centered on a fully transparent background with generous even padding (about 12% on every side). "
           "Absolutely NO text, NO letters, NO numbers, NO words, NO watermark, NO logo, NO frame, NO background "
           "shape unless described. Square 1:1, one single object, clearly recognizable at 48 px.")
_MUKODO = {"modell": None}


def kulcs(kulcs_fajl=None):
    k = os.environ.get("OPENAI_API_KEY", "").strip()
    if k:
        return k
    jel = []
    if kulcs_fajl:
        jel.append(Path(kulcs_fajl))
    p = Path.cwd()
    for d in [p] + list(p.parents):
        jel += [d / "openai-kulcs.txt", d / "bemenet" / "openai-kulcs.txt"]
    jel += [Path("/mnt/user-data/uploads/openai-kulcs.txt"), Path.home() / ".config" / "openai-kulcs.txt"]
    for f in jel:
        try:
            if f.is_file():
                for sor in f.read_text(encoding="utf-8").splitlines():
                    s = sor.strip()
                    if s and not s.startswith("#"):
                        return s
        except Exception:
            pass
    return ""


def arfolyam():
    for url in ("https://api.frankfurter.app/latest?from=USD&to=HUF", "https://open.er-api.com/v6/latest/USD"):
        try:
            with urllib.request.urlopen(url, timeout=5) as r:
                v = float(json.loads(r.read())["rates"]["HUF"])
                if v > 0:
                    return v
        except Exception:
            continue
    return 330.0


def _hivas(key, modell, prompt, quality, size, atlatszo=True):
    body = {"model": modell, "prompt": prompt, "size": size, "quality": quality, "n": 1, "output_format": "png"}
    if atlatszo:
        body["background"] = "transparent"
    req = urllib.request.Request(API, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.loads(r.read())


def general(key, prompt, quality="medium", size="1024x1024", atlatszo=True):
    """Visszaad: (png_bytes, usage, modell). Modell-visszaesés 'nem létezik / nincs jogosultság' hibára."""
    sorrend = ([_MUKODO["modell"]] if _MUKODO["modell"] else []) + [m for m in MODELLEK if m != _MUKODO["modell"]]
    utolso = None
    for m in sorrend:
        for proba in range(3):
            try:
                d = _hivas(key, m, prompt, quality, size, atlatszo)
                _MUKODO["modell"] = m
                return base64.b64decode(d["data"][0]["b64_json"]), d.get("usage", {}), m
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")
                utolso = f"HTTP {e.code}: {msg[:300]}"
                if e.code in (400, 403, 404) and ("model" in msg.lower() or "verif" in msg.lower()
                                                  or "does not exist" in msg.lower() or "access" in msg.lower()):
                    break                       # következő modell
                if e.code == 400 and "background" in msg.lower():
                    atlatszo = False            # régebbi modell: átlátszóság nélkül, utómunkával
                    continue
                if e.code in (429, 500, 502, 503):
                    time.sleep(6 * (proba + 1))
                    continue
                raise RuntimeError(utolso)
            except (urllib.error.URLError, TimeoutError) as e:
                utolso = str(e)
                time.sleep(4)
    if utolso and "verif" in utolso.lower():
        raise RuntimeError("Az OpenAI-fiókodon a képmodellekhez szervezet-ellenőrzés kell: platform.openai.com -> "
                           "Settings -> Organization -> General -> Verify Organization. (" + utolso[:160] + ")")
    raise RuntimeError(utolso or "ismeretlen hiba")


def koltseg_usd(u):
    if not u:
        return 0.0
    det = u.get("input_tokens_details") or {}
    txt = det.get("text_tokens", u.get("input_tokens", 0))
    img_in = det.get("image_tokens", 0)
    out = u.get("output_tokens", 0)
    return (txt * TOKEN_USD["text_in"] + img_in * TOKEN_USD["image_in"] + out * TOKEN_USD["image_out"]) / 1e6


def utomunka(path, meret=256):
    """Átlátszó perem levágása, négyzetre igazítás, 256 px, 128 színre kvantálás (kb. 8x kisebb fájl).
    Ha a kép mégsem átlátszó (régi modell), a sarkokból indított flood kivágja a fehér hátteret."""
    try:
        from PIL import Image, ImageDraw
    except Exception:
        return
    im = Image.open(path).convert("RGBA")
    a = im.getchannel("A")
    if a.getextrema()[0] > 200:          # nincs átlátszóság -> fehér háttér kivágása
        w, h = im.size
        for xy in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
            ImageDraw.floodfill(im, xy, (255, 255, 255, 0), thresh=40)
        a = im.getchannel("A")
    bb = a.point(lambda v: 255 if v > 12 else 0).getbbox()
    if bb:
        im = im.crop(bb)
    w, h = im.size
    s = int(max(w, h) * 1.1)
    sq = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    sq.paste(im, ((s - w) // 2, (s - h) // 2), im)
    sq = sq.resize((meret, meret), Image.LANCZOS)
    try:
        q = sq.quantize(colors=128, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
        q.save(path, optimize=True)
    except Exception:
        sq.save(path, optimize=True)


def main():
    a = sys.argv[1:]
    kf = a[a.index("--kulcs-fajl") + 1] if "--kulcs-fajl" in a else None
    key = kulcs(kf)
    if "--check" in a:
        print("OK" if key else "NO_KEY")
        return
    if "--spec" not in a:
        print(__doc__)
        return
    if not key:
        print("NO_KEY: nincs OpenAI kulcs. Tedd egy openai-kulcs.txt fájlba (egy sor: sk-...), vagy "
              "állítsd be az OPENAI_API_KEY változót.")
        sys.exit(2)
    spec_ut = Path(a[a.index("--spec") + 1])
    spec = json.loads(spec_ut.read_text(encoding="utf-8"))
    alap = spec_ut.parent
    mappa = alap / spec.get("mappa", "ikonok")
    csak = a[a.index("--csak") + 1] if "--csak" in a else None
    ujra = "--ujra" in a
    q = spec.get("quality", "medium")
    sz = spec.get("szinek", {})
    feladat = []
    for st in spec["stilusok"]:
        if csak and st["id"] != csak:
            continue
        elotag = st["elotag"]
        for k, v in sz.items():
            elotag = elotag.replace("{" + k + "}", v)
        for ik in spec["ikonok"]:
            cel = mappa / st["id"] / f'{ik["nev"]}.png'
            if cel.exists() and not ujra:
                continue
            prompt = f'{elotag.strip()} Subject: {ik["tema"]}.' + ZARADEK
            feladat.append((st["id"], ik["nev"], prompt, cel))
    if not feladat:
        print("Minden ikon megvan (--ujra az újrageneráláshoz).")
        return
    print(f"{len(feladat)} ikon generálása ({q})...")
    ossz, hibak, t0 = 0.0, [], time.time()

    def egy(f):
        sid, nev, prompt, cel = f
        png, usage, modell = general(key, prompt, q)
        cel.parent.mkdir(parents=True, exist_ok=True)
        cel.write_bytes(png)
        utomunka(cel)
        return sid, nev, koltseg_usd(usage), modell

    with ThreadPoolExecutor(max_workers=int(spec.get("parhuzamos", 6))) as ex:
        fut = {ex.submit(egy, f): f for f in feladat}
        for x in as_completed(fut):
            try:
                sid, nev, usd, modell = x.result()
                ossz += usd
                print(f"  ✓ {sid}/{nev}  ({modell})")
            except Exception as e:
                f = fut[x]
                hibak.append(f"{f[0]}/{f[1]}: {e}")
                print(f"  ✗ {f[0]}/{f[1]}: {str(e)[:200]}")
    huf = arfolyam()
    print(f"\nKész: {len(feladat) - len(hibak)}/{len(feladat)} ikon, {time.time() - t0:.0f} mp. "
          f"Becsült költség: {ossz:.3f} USD ≈ {ossz * huf:.0f} Ft (árfolyam {huf:.0f} Ft/USD).")
    if hibak:
        print("HIBÁK:\n  " + "\n  ".join(hibak))
        sys.exit(1)


if __name__ == "__main__":
    main()
