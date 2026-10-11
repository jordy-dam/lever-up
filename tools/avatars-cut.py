"""Knipt een contactblad met 6 avatars (3 kolommen, 2 rijen) in assets/avatars/a1..a6.webp.
Gebruik: python3 tools/avatars-cut.py pad/naar/blad.png
Volgorde: boven a1 a2 a3 (mannen), onder a4 a5 a6 (vrouwen). Vereist pillow."""
import sys, os
from PIL import Image
src = sys.argv[1]
im = Image.open(src).convert("RGB")
W, H = im.size
cw, ch = W / 3, H / 2
inset = 0.03          # snijd een randje weg, voor het geval de cellen niet exact gelijk zijn
os.makedirs("assets/avatars", exist_ok=True)
for n in range(6):
    r, c = divmod(n, 3)
    x0, y0 = c * cw + cw * inset, r * ch + ch * inset
    x1, y1 = (c + 1) * cw - cw * inset, (r + 1) * ch - ch * inset
    side = min(x1 - x0, y1 - y0)                       # vierkant uit het midden van de cel
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    box = tuple(int(v) for v in (cx - side / 2, cy - side / 2, cx + side / 2, cy + side / 2))
    out = im.crop(box).resize((512, 512), Image.LANCZOS)
    out.save(f"assets/avatars/a{n+1}.webp", quality=90)
    print("assets/avatars/a%d.webp" % (n + 1), box)
