#!/usr/bin/env python3
"""Draws the site's images that the app can't capture: the app icon and favicons, and the Open Graph cards,
in English and French. Everything is drawn as HTML and SVG, then rendered by Chrome. The row of app screens
comes from the simulator instead: scripts/capture-screens.sh.

    python3 scripts/make-images.py            # everything
    python3 scripts/make-images.py og         # or: icons

Needs Google Chrome.
"""

import os
import struct
import subprocess
import sys
import tempfile

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(SITE, "assets")
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

# The app's palette: warm paper and ink.
PAPER = "#f5f3ee"
INK = "#17212b"
MUTED = "#686a6c"
# The habits' colors in light mode (Shared/HabitColor.swift), with the sample habits' progress.
RINGS = [("#2a6fad", 0.625), ("#2e7d4f", 0.82), ("#b85a16", 1.0), ("#8f6a1c", 1.0), ("#6a4fc2", 0.4), ("#3f57b5", 0.0)]


def page(body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
      * {{ margin: 0; box-sizing: border-box; }}
      html, body {{ background: {PAPER}; color: {INK}; }}
      {css}</style></head><body>{body}</body></html>"""


def ring(cx, cy, r, width, color, fraction, track_opacity=0.16):
    """A habit's ring: a faint track, and its progress from the top, clockwise."""
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-opacity="{track_opacity}" stroke-width="{width}"/>'
    if fraction > 0:
        out += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
                f'pathLength="100" stroke-dasharray="{fraction * 100:.2f} 100" transform="rotate(-90 {cx} {cy})"/>')
    return out


# « Flamme »: the streak flame, two-tone like the app's feature icons, with a gold core, glowing on ink.
# The same drawing as ../coutume-ios's AppIcon (drawn there with CoreGraphics), on a 100-unit grid.
ICON_FLAME = "#f29a5c"
ICON_GOLD = "#ffd23f"
ICON_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs><radialGradient id="glow" gradientUnits="userSpaceOnUse" cx="50" cy="62" r="40.4">
    <stop offset="0" stop-color="{ICON_FLAME}" stop-opacity="0.35"/><stop offset="1" stop-color="{ICON_FLAME}" stop-opacity="0"/>
  </radialGradient></defs>
  <rect width="100" height="100" fill="#0a0a0b"/>
  <rect width="100" height="100" fill="url(#glow)"/>
  <path d="M50 20C56 31 68 38 68 55C68 66 60 75 50 75C40 75 32 66 32 55C32 46 38 41 41 34C43 41 46 44 49 45C48 36 47 28 50 20Z"
        fill="{ICON_FLAME}" fill-opacity="0.25" stroke="{ICON_FLAME}" stroke-width="3.2" stroke-linejoin="round"/>
  <path d="M50 52C53 57 58 59 58 64.5C58 69 54.5 72 50 72C45.5 72 42 69 42 64.5C42 60 46 58 50 52Z" fill="{ICON_GOLD}"/>
</svg>"""


def render(html, out_png, width, height, scale=2):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        src = f.name
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                        f"--force-device-scale-factor={scale}", f"--window-size={width},{height}",
                        "--virtual-time-budget=4000", f"--screenshot={out_png}", f"file://{src}"],
                       check=True, capture_output=True)
    finally:
        os.unlink(src)


def ico(pngs, out):
    """An .ico holding PNG images, which every current browser reads."""
    data = [open(p, "rb").read() for p, _ in pngs]
    header = struct.pack("<HHH", 0, 1, len(pngs))
    offset = 6 + 16 * len(pngs)
    entries = b""
    for (p, size), blob in zip(pngs, data):
        entries += struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0, 1, 32, len(blob), offset)
        offset += len(blob)
    with open(out, "wb") as f:
        f.write(header + entries + b"".join(data))


def make_icons():
    with open(os.path.join(ASSETS, "icon.svg"), "w") as f:
        f.write(ICON_SVG + "\n")
    # The App Store wants a square 1024 px PNG without transparency; iOS rounds it.
    tmp = tempfile.mkdtemp()
    square = lambda size, radius: page(
        f'<div style="width:{size}px;height:{size}px;border-radius:{radius}%;overflow:hidden">'
        f'{ICON_SVG.replace("<svg ", f"<svg width=\"{size}\" height=\"{size}\" ", 1)}</div>',
        f"html, body {{ width: {size}px; height: {size}px; background: transparent; }}")
    # The app icon, as iOS rounds it; the favicons are a little rounder so they read at small sizes.
    targets = [("icon.png", 512, 22.37), ("icon-1024.png", 1024, 0), ("apple-touch-icon.png", 180, 0),
               ("android-chrome-512x512.png", 512, 22.37), ("android-chrome-192x192.png", 192, 22.37),
               ("favicon-32x32.png", 32, 24), ("favicon-16x16.png", 16, 24)]
    for name, size, radius in targets:
        png = os.path.join(tmp, name)
        render(square(size, radius), png, size, size, scale=1)
        os.replace(png, os.path.join(ASSETS, name))
        print("icon", name)
    ico([(os.path.join(ASSETS, "favicon-16x16.png"), 16), (os.path.join(ASSETS, "favicon-32x32.png"), 32)],
        os.path.join(SITE, "favicon.ico"))


OG = {
    "en": ("Keep your habits, <em>one day at a time.</em>", "Good habits to build, bad ones to quit, for iPhone. Free, no account, no ads."),
    "fr": ("Tiens tes habitudes, <em>un jour à la fois.</em>", "Les bonnes à prendre, les mauvaises à laisser, sur iPhone. Gratuite, sans compte, sans pub."),
}


def make_og():
    # The day's six rings, as on the app's first screen, in two columns.
    cells = "".join(ring(130 + (i % 2) * 230, 120 + (i // 2) * 200, 70, 22, color, fraction)
                    for i, (color, fraction) in enumerate(RINGS))
    art = f'<svg viewBox="0 0 490 640" width="490" height="640">{cells}</svg>'
    for lang, (title, line) in OG.items():
        html = page(
            f'<div class="art">{art}</div><div class="txt">'
            f'<p class="brand"><img src="file://{ASSETS}/icon.png">Coutume</p><h1>{title}</h1><p class="line">{line}</p></div>',
            f"""html, body {{ width: 1200px; height: 630px; overflow: hidden; }}
            body {{ font-family: "Inter", -apple-system, system-ui; }}
            .art {{ position: absolute; right: 70px; top: 6px; }}
            .txt {{ position: absolute; left: 80px; top: 92px; width: 640px; }}
            .brand {{ display: flex; align-items: center; gap: 16px; font-size: 30px; font-weight: 600; }}
            .brand img {{ width: 56px; height: 56px; border-radius: 13px; }}
            h1 {{ margin-top: 64px; font-size: 66px; font-weight: 600; line-height: 1.08; letter-spacing: -0.03em; }}
            h1 em {{ font-family: "Instrument Serif", Georgia, serif; font-size: 1.12em; font-weight: 400; font-style: italic; letter-spacing: 0; color: #a8501a; }}
            .line {{ margin-top: 28px; font-size: 26px; line-height: 1.4; color: {MUTED}; width: 580px; text-wrap: balance; }}""")
        html = html.replace("<head>", "<head><link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Instrument+Serif:ital@1&display=swap'>")
        render(html, os.path.join(ASSETS, f"og-{lang}.png"), 1200, 630, scale=1)
        print("og", lang)


if __name__ == "__main__":
    jobs = sys.argv[1:] or ["icons", "og"]
    for job in jobs:
        {"icons": make_icons, "og": make_og}[job]()
