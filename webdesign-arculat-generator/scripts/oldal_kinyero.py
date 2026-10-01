#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""oldal_kinyero.py - egy weboldalból (főoldal + a legfontosabb aloldalak) kinyer mindent az arculat-tervezéshez.

    python3 oldal_kinyero.py <url> <munkamappa> [--max-oldal 8] [--nincs-kep] [--nincs-kepernyokep]

Kimenet a <munkamappa>/bemenet/ alatt:
  osszegzes.json   gépi összegzés: oldalak, címsorok, képek (méret, alt), logó-jelöltek, színek, betűk, kapcsolat
  szoveg/<oldal>.md  oldalanként a látható szöveg szerkezettel (#, -, [KÉP], [GOMB])
  arculat.md       emberi összefoglaló: színek, betűk, logó, kapcsolat, fotólista
  kepek/           a letöltött képek (logó, fotók)
  eredeti-*.png    képernyőkép a főoldalról, ha van Chrome (nem kötelező)

Csak Python 3 stdlib + (opcionálisan) Pillow. A kulcsot, jelszót nem kér, nem ír ki semmit a hálózatra
a megadott oldalon kívül.
"""
import sys, re, os, json, html as H, urllib.request, urllib.parse, subprocess, shutil, tempfile, time
from pathlib import Path
from collections import Counter, OrderedDict
from html.parser import HTMLParser

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/128 Safari/537.36", "Accept-Language": "hu-HU,hu;q=0.9,en;q=0.6"}
FONTOS_ALOLDAL = ("rolunk", "bemutatkoz", "about", "tortenet", "szolgaltat", "service", "kinalat", "etlap", "menu",
                  "termek", "product", "ar", "arak", "price", "csomag", "kapcsolat", "contact", "referenci",
                  "velemeny", "galeria", "gallery", "csapat", "team", "blog")
KIHAGY_LINK = ("kosar", "cart", "login", "belep", "regisztr", "adatkezel", "aszf", "privacy", "cookie", "wp-admin",
               "feed", "mailto:", "tel:", "javascript:", "#", ".pdf", ".jpg", ".png", "facebook.com", "instagram.com")


def get(url, binary=False, timeout=35):
    req = urllib.request.Request(urllib.parse.quote(url, safe=":/?=&%#~+,;@!$*'()"), headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = r.read()
        ct = r.headers.get("Content-Type", "")
    if binary:
        return d
    m = re.search(r"charset=([\w-]+)", ct)
    return d.decode(m.group(1) if m else "utf-8", "replace")


def absol(base, u):
    if not u:
        return ""
    u = H.unescape(u.strip())
    if u.startswith("//"):
        return "https:" + u
    return urllib.parse.urljoin(base, u)


class Kinyero(HTMLParser):
    """Látható szöveg szerkezettel + képek + gombok + linkek."""
    BLOKK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "figcaption", "td", "th", "summary",
             "button", "a", "div", "section", "article", "span", "label", "dt", "dd"}
    CIM = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}
    KIHAGY = {"script", "style", "noscript", "svg", "head", "template", "iframe"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.sorok, self.kepek, self.linkek, self.cimek = [], [], [], []
        self.stack, self.skip, self.buf, self.cim, self.li, self.gomb = [], 0, "", 0, 0, 0
        self.nav = 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag in ("br",):
            self.buf += " "
            return
        if tag in ("img", "source", "input", "meta", "link", "hr", "wbr"):
            if tag == "img" and not self.skip:
                src = a.get("data-lazy-src") or a.get("data-src") or a.get("src") or ""
                if a.get("srcset") and not src.startswith("http"):
                    src = a["srcset"].split(",")[0].split()[0]
                if src and not src.startswith("data:"):
                    self._flush()
                    u = absol(self.base, src)
                    self.kepek.append({"url": u, "alt": a.get("alt", "")[:120], "class": a.get("class", "")[:80],
                                       "w": a.get("width", ""), "h": a.get("height", ""), "nav": bool(self.nav)})
                    self.sorok.append(f"[KÉP: {u.split('/')[-1][:70]} | alt={a.get('alt', '')[:60]}]")
            return
        if tag in self.KIHAGY:
            self.skip += 1
        if tag in ("nav", "header"):
            self.nav += 1
        self.stack.append(tag)
        if tag == "a" and a.get("href"):
            self.linkek.append(absol(self.base, a["href"]))
        if tag in ("button",) or (tag == "a" and re.search(r"btn|button|gomb|cta", a.get("class", ""), re.I)):
            self._flush()
            self.gomb += 1
        if tag in self.CIM:
            self._flush()
            self.cim = self.CIM[tag]
        if tag == "li":
            self._flush()
            self.li += 1

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        while self.stack:
            t = self.stack.pop()
            if t in self.KIHAGY:
                self.skip -= 1
            if t in ("nav", "header"):
                self.nav -= 1
            if t in self.CIM or t in self.BLOKK:
                self._flush()
            if t == "li" and self.li:
                self.li -= 1
            if (t == "button" or t == "a") and self.gomb:
                self.gomb -= 1
            if t == tag:
                break

    def handle_data(self, d):
        if self.skip:
            return
        d = re.sub(r"\s+", " ", d)
        if not d.strip():
            if self.buf and not self.buf.endswith(" "):
                self.buf += " "
            return
        self.buf += d

    def _flush(self):
        s = re.sub(r"\s+", " ", self.buf).strip()
        self.buf = ""
        if not s:
            self.cim = 0
            return
        if self.cim:
            self.cimek.append((self.cim, s))
            s = "#" * self.cim + " " + s
        elif self.gomb:
            s = f"[GOMB: {s}]"
        elif self.li:
            s = "- " + s
        self.cim = 0
        if not self.sorok or self.sorok[-1] != s:
            self.sorok.append(s)


def meta(raw, name):
    for pat in (rf'<meta[^>]+(?:name|property)=["\']{name}["\'][^>]+content=["\']([^"\']*)',
                rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:name|property)=["\']{name}["\']'):
        m = re.search(pat, raw, re.I)
        if m:
            return H.unescape(m.group(1)).strip()
    return ""


SEMLEGES = {"#ffffff", "#000000", "#fff", "#000", "#fefefe", "#f5f5f5", "#eeeeee", "#333333", "#222222", "#111111",
            "#f8f9fa", "#dee2e6", "#e9ecef", "#212529", "#6c757d", "#cccccc", "#dddddd", "#999999", "#666666",
            "#f0f0f0", "#fafafa", "#e5e5e5", "#444444", "#555555", "#777777", "#888888", "#aaaaaa", "#bbbbbb"}


def hex6(h):
    h = h.lower()
    if len(h) == 4:
        h = "#" + "".join(c * 2 for c in h[1:])
    return h


def szinek_css(szoveg):
    c = Counter()
    for h in re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", szoveg):
        c[hex6(h)] += 1
    for r, g, b in re.findall(r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})", szoveg):
        c["#%02x%02x%02x" % (int(r), int(g), int(b))] += 1
    semleges = {k: v for k, v in c.items() if k in SEMLEGES or telitettseg(k) < 0.12}
    markas = [(k, v) for k, v in c.most_common() if k not in semleges]
    return markas[:16], sorted(semleges.items(), key=lambda x: -x[1])[:8]


def telitettseg(h):
    try:
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    except Exception:
        return 0
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == mn:
        return 0
    l = (mx + mn) / 2
    return (mx - mn) / (1 - abs(2 * l - 1)) if l not in (0, 1) else 0


def betuk(raw, css):
    f = Counter()
    for m in re.findall(r"fonts\.googleapis\.com/css2?\?([^\"'>]+)", raw + css):
        for fam in re.findall(r"family=([A-Za-z0-9+ %]+)", H.unescape(m)):
            f[urllib.parse.unquote_plus(fam).strip()] += 5
    for fam in re.findall(r"font-family\s*:\s*([^;}{]+)", css + raw):
        first = fam.split(",")[0].strip().strip("'\"")
        if first and first.lower() not in ("inherit", "sans-serif", "serif", "monospace", "initial", "var(--",
                                           "system-ui", "-apple-system", "cursive") and not first.startswith("var("):
            f[first] += 1
    return [k for k, _ in f.most_common(10)]


def kep_szinek(path, n=6):
    """A logó domináns színei Pillow-val (átlátszó és szinte-fehér pixelek nélkül)."""
    try:
        from PIL import Image
    except Exception:
        return []
    try:
        im = Image.open(path)
        im.load()
        im = im.convert("RGBA")
        im.thumbnail((200, 200))
        px = [p for p in im.getdata() if p[3] > 160]
        if not px:
            return []
        flat = Image.new("RGB", (len(px), 1))
        flat.putdata([p[:3] for p in px])
        q = flat.quantize(colors=n + 4, method=Image.Quantize.MEDIANCUT)
        pal = q.getpalette()
        cnt = sorted(q.getcolors(), reverse=True)
        out = []
        for c, idx in cnt:
            r, g, b = pal[idx * 3: idx * 3 + 3]
            h = "#%02x%02x%02x" % (r, g, b)
            out.append({"hex": h, "arany": round(c / len(px), 3), "semleges": telitettseg(h) < 0.12})
        return out[:n]
    except Exception:
        return []


def kep_meret(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size, im.mode
    except Exception:
        return (0, 0), ""


def logo_jeloltek(kepek, raw, base):
    j = []
    for k in kepek:
        s = (k["url"] + " " + k["alt"] + " " + k["class"]).lower()
        pont = 0
        if "logo" in s:
            pont += 5
        if k["nav"]:
            pont += 3
        if "header" in s or "brand" in s:
            pont += 2
        if pont:
            j.append((pont, k["url"]))
    og = meta(raw, "og:image")
    if og:
        j.append((1, absol(base, og)))
    for m in re.findall(r'<link[^>]+rel=["\'][^"\']*(?:apple-touch-icon|icon)[^"\']*["\'][^>]+href=["\']([^"\']+)', raw, re.I):
        j.append((1, absol(base, m)))
    seen, out = set(), []
    for p, u in sorted(j, key=lambda x: -x[0]):
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out[:6]


def kapcsolat(szoveg):
    t = " ".join(szoveg)
    tel = sorted(set(re.findall(r"(?:\+36|06)[\s/-]?\d{1,2}[\s/-]?\d{3}[\s/-]?\d{3,4}", t)))
    email = sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", t)))
    irsz = sorted(set(re.findall(r"\b\d{4}\s+[A-ZÁÉÍÓÖŐÚÜŰ][\wáéíóöőúüű]+,?\s+[^|\n]{3,40}?(?:utca|út|tér|u\.|krt|körút|sor|köz|útja|tere)\s*\d+[\w/.-]*", t)))
    return {"telefon": tel[:3], "email": email[:3], "cim": irsz[:3]}


def fajlnev(u):
    n = urllib.parse.unquote(urllib.parse.urlsplit(u).path.split("/")[-1]) or "kep"
    return re.sub(r"[^A-Za-z0-9._-]", "-", n)[:80]


def kepernyokep(url, cel, szel=1440, mag=4200):
    chrome = next((p for p in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                               shutil.which("google-chrome") or "", shutil.which("chromium") or "",
                               shutil.which("chromium-browser") or "") if p and os.path.exists(p)), None)
    if not chrome:
        return False
    prof = tempfile.mkdtemp(prefix="wagch")
    try:
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
                        "--force-prefers-reduced-motion", f"--user-data-dir={prof}", f"--window-size={szel},{mag}",
                        "--timeout=15000", f"--screenshot={cel}", url],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=70)
    except subprocess.TimeoutExpired:
        subprocess.run(["pkill", "-f", prof], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(prof, ignore_errors=True)
    return os.path.exists(cel)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        sys.exit(0)
    url, mappa = args[0], Path(args[1])
    if not url.startswith("http"):
        url = "https://" + url
    max_oldal = 8
    if "--max-oldal" in sys.argv:
        max_oldal = int(sys.argv[sys.argv.index("--max-oldal") + 1])
    be = mappa / "bemenet"
    (be / "szoveg").mkdir(parents=True, exist_ok=True)
    (be / "kepek").mkdir(parents=True, exist_ok=True)
    host = urllib.parse.urlsplit(url).netloc.replace("www.", "")

    print("letöltés:", url)
    raw0 = get(url)
    (be / "eredeti-fooldal.html").write_text(raw0, encoding="utf-8")
    p0 = Kinyero(url)
    p0.feed(raw0)
    p0._flush()

    # aloldalak: a menüből, a fontos kulcsszavak előre
    jel = OrderedDict()
    for l in p0.linkek:
        sp = urllib.parse.urlsplit(l)
        if sp.netloc.replace("www.", "") != host:
            continue
        low = l.lower()
        if any(k in low for k in KIHAGY_LINK) or l.rstrip("/") == url.rstrip("/"):
            continue
        clean = urllib.parse.urlunsplit((sp.scheme, sp.netloc, sp.path, sp.query, ""))
        pont = sum(3 for k in FONTOS_ALOLDAL if k in low) + 1
        jel[clean] = max(jel.get(clean, 0), pont)
    aloldalak = [u for u, _ in sorted(jel.items(), key=lambda x: -x[1])][:max_oldal - 1]

    oldalak = [{"url": url, "nev": "fooldal", "raw": raw0, "p": p0}]
    for u in aloldalak:
        try:
            raw = get(u)
        except Exception as ex:
            print("  kihagyva:", u, type(ex).__name__)
            continue
        p = Kinyero(u)
        p.feed(raw)
        p._flush()
        nev = re.sub(r"[^a-z0-9]+", "-", urllib.parse.urlsplit(u).path.lower()).strip("-")[:50] or "oldal"
        oldalak.append({"url": u, "nev": nev, "raw": raw, "p": p})
        time.sleep(0.3)

    # css
    css_osszes = []
    for o in oldalak[:3]:
        css_osszes += re.findall(r"<style[^>]*>(.*?)</style>", o["raw"], re.S)
    for c in re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', raw0)[:14]:
        try:
            css_osszes.append(get(absol(url, c)))
        except Exception:
            pass
    css = "\n".join(css_osszes)
    markas, semleges = szinek_css(css + raw0)
    fontok = betuk(raw0, css)

    # szöveg oldalanként
    minden_sor = []
    for o in oldalak:
        fej = f"# forrás: {o['url']}\n# A tények (árak, nevek, számok, nyitvatartás) SZENTEK: betűre így használd.\n\n"
        (be / "szoveg" / f"{o['nev']}.md").write_text(fej + "\n".join(o["p"].sorok) + "\n", encoding="utf-8")
        minden_sor += o["p"].sorok

    # képek
    kepek, seen = [], set()
    for o in oldalak:
        for k in o["p"].kepek:
            if k["url"] in seen:
                continue
            seen.add(k["url"])
            k["oldal"] = o["nev"]
            kepek.append(k)
    for o in oldalak:  # háttérképek a css/inline stílusból
        for m in re.findall(r"url\(['\"]?([^'\")]+\.(?:jpe?g|png|webp))", o["raw"], re.I):
            u = absol(o["url"], m)
            if u not in seen:
                seen.add(u)
                kepek.append({"url": u, "alt": "", "class": "hatterkep", "w": "", "h": "", "nav": False,
                              "oldal": o["nev"]})
    logok = logo_jeloltek(kepek, raw0, url)
    letoltott = []
    if "--nincs-kep" not in sys.argv:
        for k in kepek[:80]:
            u = k["url"]
            if re.search(r"\.(svg|gif)(\?|$)", u, re.I) and u not in logok:
                continue
            nev = fajlnev(u)
            cel = be / "kepek" / nev
            try:
                if not cel.exists():
                    cel.write_bytes(get(u, binary=True))
                (w, h), mode = kep_meret(cel)
                k.update({"fajl": f"kepek/{nev}", "px": [w, h], "mode": mode, "kb": round(cel.stat().st_size / 1024)})
                letoltott.append(k)
            except Exception as ex:
                k["hiba"] = type(ex).__name__
    for u in logok:
        nev = fajlnev(u)
        cel = be / "kepek" / nev
        if not cel.exists():
            try:
                cel.write_bytes(get(u, binary=True))
            except Exception:
                pass
    logo_info = []
    for u in logok:
        f = be / "kepek" / fajlnev(u)
        if f.exists():
            (w, h), mode = kep_meret(f)
            logo_info.append({"url": u, "fajl": f"kepek/{f.name}", "px": [w, h], "mode": mode,
                              "szinek": kep_szinek(f)})

    osszegzes = {
        "url": url, "host": host,
        "cim": re.sub(r"\s+", " ", H.unescape((re.search(r"<title[^>]*>(.*?)</title>", raw0, re.S | re.I) or [None, ""])[1])).strip(),
        "leiras": meta(raw0, "description") or meta(raw0, "og:description"),
        "oldalak": [{"url": o["url"], "nev": o["nev"], "cimsorok": o["p"].cimek[:40], "sorok": len(o["p"].sorok)} for o in oldalak],
        "szinek_css": markas, "semleges_css": semleges, "betuk": fontok,
        "logo_jeloltek": logo_info,
        "kepek": [k for k in letoltott if k.get("px", [0, 0])[0] >= 200],
        "kis_kepek": [k["fajl"] for k in letoltott if k.get("px", [0, 0])[0] < 200],
        "kapcsolat": kapcsolat(minden_sor),
        "social": sorted(set(l for o in oldalak for l in o["p"].linkek if re.search(r"facebook\.com|instagram\.com|tiktok\.com|youtube\.com|linkedin\.com", l)))[:8],
    }
    (be / "osszegzes.json").write_text(json.dumps(osszegzes, ensure_ascii=False, indent=1), encoding="utf-8")

    sorok = [f"# A mostani arculat: {osszegzes['cim']}", f"forrás: {url}", "",
             "## Logó-jelöltek (nézd meg, melyik a valódi logó)"]
    for l in logo_info:
        sz = ", ".join(f"{c['hex']} {int(c['arany'] * 100)}%" + (" (semleges)" if c["semleges"] else "") for c in l["szinek"])
        sorok.append(f"- {l['fajl']}  {l['px'][0]}x{l['px'][1]} {l['mode']}  színek: {sz}")
    sorok += ["", "## Márkaszín-jelöltek a CSS-ből (gyakoriság)"] + [f"- `{h}` ({n}x)" for h, n in markas]
    sorok += ["", "## Semleges színek"] + [f"- `{h}` ({n}x)" for h, n in semleges]
    sorok += ["", "## Betűk"] + [f"- {f}" for f in fontok]
    sorok += ["", "## Kapcsolat (kiolvasva, ellenőrizd!)", json.dumps(osszegzes["kapcsolat"], ensure_ascii=False),
              "social: " + ", ".join(osszegzes["social"])]
    sorok += ["", "## Oldalak"] + [f"- {o['nev']}: {o['url']}" for o in oldalak]
    sorok += ["", "## Fotók (min. 200 px széles)"] + [
        f"- {k['fajl']}  {k['px'][0]}x{k['px'][1]}  {k['kb']} KB  alt=\"{k['alt']}\"  ({k['oldal']})" for k in osszegzes["kepek"]]
    (be / "arculat.md").write_text("\n".join(sorok) + "\n", encoding="utf-8")

    if "--nincs-kepernyokep" not in sys.argv:
        ok = kepernyokep(url, str(be / "eredeti-fooldal-1440.png"))
        print("  képernyőkép:", "kész" if ok else "kimaradt (nincs Chrome)")
    print(f"  {len(oldalak)} oldal · {len(osszegzes['kepek'])} fotó · {len(logo_info)} logó-jelölt · "
          f"{len(markas)} márkaszín-jelölt · betűk: {', '.join(fontok[:4]) or '-'}")
    print("KÉSZ:", be / "arculat.md")


if __name__ == "__main__":
    main()
