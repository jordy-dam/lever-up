"""Knipt een contactblad in gelijke vierkante cellen en slaat ze op als 512 px webp.
Gebruik: python3 tools/sheet-cut.py blad.png uitmap naam1 naam2 ... [--cols 3]
Cellen lopen van links naar rechts, rij voor rij. Voorbeeld voor de rangbeelden (3 x 2):
  python3 tools/sheet-cut.py assets/_raw/ranks-sheet.png assets/ranks lev groentje veertje bar-baas lucht-ninja legende
Vereist pillow."""
import sys, os
from PIL import Image
args = [a for a in sys.argv[1:]]
cols = 3
if "--cols" in args:
    i = args.index("--cols"); cols = int(args[i + 1]); del args[i:i + 2]
src, outdir, names = args[0], args[1], args[2:]
rows = -(-len(names) // cols)
im = Image.open(src).convert("RGB")
W, H = im.size
cw, ch = W / cols, H / rows
inset = 0.03
os.makedirs(outdir, exist_ok=True)
for n, name in enumerate(names):
    r, c = divmod(n, cols)
    x0, y0 = c * cw + cw * inset, r * ch + ch * inset
    x1, y1 = (c + 1) * cw - cw * inset, (r + 1) * ch - ch * inset
    side = min(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    box = tuple(int(v) for v in (cx - side / 2, cy - side / 2, cx + side / 2, cy + side / 2))
    im.crop(box).resize((512, 512), Image.LANCZOS).save(os.path.join(outdir, name + ".webp"), quality=90)
    print(os.path.join(outdir, name + ".webp"), box)
