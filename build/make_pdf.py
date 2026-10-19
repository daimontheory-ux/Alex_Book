"""Assemble the exported page PNGs into one print PDF.

Usage (from the repo root):
    pip install img2pdf pillow
    python build/make_pdf.py                 # build/pages/*.png -> build/right_here_with_you.pdf
    python build/make_pdf.py --check-only    # validate the pages without writing a PDF

Every page must be a 2475 x 2475 px PNG (8.25 x 8.25 in at 300 dpi: the 8 x 8 in
trim plus 1/8 in bleed on every side). Pages are taken in file-name order, so
name them page_00_title.png, page_01.png ... page_28.png. The PDF embeds the
PNGs losslessly, with each page sized exactly 8.25 x 8.25 in.

Spec source: 00_story-bible.md section 7.5.
"""
import argparse
import sys
from pathlib import Path

import img2pdf
from PIL import Image

DPI = 300
PAGE_IN = 8.25
PAGE_PX = round(PAGE_IN * DPI)  # 2475

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
OUT = ROOT / "right_here_with_you.pdf"


def check(paths):
    problems = []
    for p in paths:
        with Image.open(p) as im:
            if im.size != (PAGE_PX, PAGE_PX):
                problems.append(f"{p.name}: {im.size[0]}x{im.size[1]} px, needs {PAGE_PX}x{PAGE_PX}")
            if im.mode not in ("RGB", "RGBA", "P"):
                problems.append(f"{p.name}: color mode {im.mode}; export as sRGB RGB")
            if im.mode == "RGBA" and im.getchannel("A").getextrema()[0] < 255:
                problems.append(f"{p.name}: has transparent pixels; flatten onto white before export")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages", type=Path, default=PAGES)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    paths = sorted(args.pages.glob("*.png"))
    if not paths:
        sys.exit(f"No PNG pages found in {args.pages}")

    problems = check(paths)
    for msg in problems:
        print("PROBLEM:", msg)
    print(f"{len(paths)} pages checked, {len(problems)} problem(s).")
    if problems:
        sys.exit(1)
    if args.check_only:
        return

    # img2pdf rejects images with an alpha channel; flatten any fully opaque RGBA to RGB first.
    inputs = []
    for p in paths:
        with Image.open(p) as im:
            if im.mode != "RGB":
                tmp = args.out.parent / f".flat_{p.name}"
                im.convert("RGB").save(tmp, dpi=(DPI, DPI))
                inputs.append(str(tmp))
            else:
                inputs.append(str(p))

    size = (img2pdf.in_to_pt(PAGE_IN), img2pdf.in_to_pt(PAGE_IN))
    layout = img2pdf.get_layout_fun(size)
    args.out.write_bytes(img2pdf.convert(inputs, layout_fun=layout))
    for f in inputs:
        if Path(f).name.startswith(".flat_"):
            Path(f).unlink()
    print(f"Wrote {args.out} ({len(paths)} pages, {PAGE_IN} x {PAGE_IN} in each)")


if __name__ == "__main__":
    main()
