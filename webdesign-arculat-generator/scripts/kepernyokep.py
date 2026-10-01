#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kepernyokep.py - QA-képernyőkép és konzol-ellenőrzés headless Chrome-mal (vagy Playwrighttal).

  python3 kepernyokep.py <html> <kimenet-prefix> [--w 1440] [--h 12000] [--szelet 1600] [--scale .5]
  python3 kepernyokep.py <valaszto.html> qa/hero --csak kat-hero,kat-nav     # csak ezek a kategóriák
  python3 kepernyokep.py <valaszto.html> qa/elo --elo                        # csak az élő oldal
  python3 kepernyokep.py <html> --konzol                                     # JS-hibák a konzolból

Szeletekre vágja a hosszú képet (<prefix>-00.jpg, -01.jpg ...), ezeket Read-del nézd meg.
A beúszó animációkat kikapcsolja (--force-prefers-reduced-motion), hogy a kép ne legyen félig üres.
"""
import sys, os, subprocess, tempfile, shutil, re
from pathlib import Path


def chrome():
    for p in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              shutil.which("google-chrome") or "", shutil.which("google-chrome-stable") or "",
              shutil.which("chromium") or "", shutil.which("chromium-browser") or ""]:
        if p and os.path.exists(p):
            return p
    return None


def arg(a, n, d=None):
    return a[a.index(n) + 1] if n in a else d


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    src = Path(a[0]).resolve()
    konzol = "--konzol" in a
    out = None if konzol else a[1]
    W, H = int(arg(a, "--w", 1440)), int(arg(a, "--h", 12000))
    css = ""
    if "--csak" in a:
        ids = arg(a, "--csak").split(",")
        css += (".vl-intro,.vl-csop,.vl-alt,.vl-elo-sec,.vl-fab,.vl-side{display:none!important}.vl-lay{display:block!important}"
                ".vl-kat{display:none!important}" + "".join(f"#{i}{{display:block!important}}" for i in ids))
    if "--elo" in a:
        css += (".vl-intro,.vl-csop,.vl-alt,.vl-kat,.vl-fab,.vl-side,.vl-top{display:none!important}.vl-lay{display:block!important}"
                ".vl-main{padding:0!important}.vl-elo-sec{margin:0!important}.vl-elo-fej{position:static!important}")
    html = src.read_text(encoding="utf-8")
    if css:
        html = html.replace("</head>", f"<style>{css}</style></head>", 1)
    tmp = src.parent / ".__qa_tmp.html"
    tmp.write_text(html, encoding="utf-8")
    ch = chrome()
    png = (out + ".png") if out else str(Path(tempfile.mkdtemp(prefix="wagk")) / "k.png")
    try:
        if ch:
            prof = tempfile.mkdtemp(prefix="wagqa")
            cmd = [ch, "--headless", "--disable-gpu", "--no-first-run", "--hide-scrollbars", "--force-prefers-reduced-motion",
                   f"--user-data-dir={prof}", f"--window-size={W},{H}", "--timeout=15000", "--virtual-time-budget=6000",
                   f"--screenshot={png}", tmp.as_uri()]
            if konzol:
                cmd[1:1] = ["--enable-logging=stderr", "--v=1"]
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
                log = (r.stderr or "")
            except subprocess.TimeoutExpired as e:
                subprocess.run(["pkill", "-f", prof])
                log = (e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or ""))
            shutil.rmtree(prof, ignore_errors=True)
            if konzol:
                sor = [re.sub(r"^.*CONSOLE:\d+\] ", "", x)[:400] for x in log.splitlines() if "CONSOLE" in x]
                print("\n".join(sor) if sor else "Nincs konzol-üzenet (nincs JS-hiba).")
                return
        else:
            try:
                from playwright.sync_api import sync_playwright
            except Exception:
                print("Nincs Chrome és Playwright sem: képernyőkép nem készült. Futtasd a scripts/ellenorzo.py-t helyette.")
                return
            msgs = []
            with sync_playwright() as p:
                b = p.chromium.launch()
                pg = b.new_page(viewport={"width": W, "height": 900}, reduced_motion="reduce")
                pg.on("console", lambda m: msgs.append(f"{m.type}: {m.text}"))
                pg.on("pageerror", lambda e: msgs.append(f"HIBA: {e}"))
                pg.goto(tmp.as_uri())
                pg.wait_for_timeout(2500)
                if konzol:
                    print("\n".join(msgs) or "Nincs konzol-üzenet (nincs JS-hiba).")
                    b.close()
                    return
                pg.screenshot(path=png, full_page=True)
                b.close()
    finally:
        tmp.unlink(missing_ok=True)
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(png).convert("RGB")
    px = im.load()
    last, bg = im.size[1], px[5, im.size[1] - 2]
    for y in range(im.size[1] - 1, 0, -8):
        if any(sum(abs(px[x, y][i] - bg[i]) for i in range(3)) > 12 for x in range(0, im.size[0], 24)):
            last = min(im.size[1], y + 20)
            break
    step, sc = int(arg(a, "--szelet", 1600)), float(arg(a, "--scale", .5))
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    n = 0
    for y in range(0, last, step):
        c = im.crop((0, y, im.size[0], min(last, y + step)))
        c.resize((int(c.size[0] * sc), int(c.size[1] * sc))).save(f"{out}-{n:02d}.jpg", quality=74)
        n += 1
    print(f"{png}: tartalom ~{last}px, {n} szelet ({out}-00.jpg ...)")
    if last >= H - 40:
        print(f"FIGYELEM: az oldal hosszabb lehet {H}px-nél; növeld a --h értékét (max ~16000), vagy használd a --csak kapcsolót.")


if __name__ == "__main__":
    main()
