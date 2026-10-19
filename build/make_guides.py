"""Draw the page-template guide overlay for GIMP.

Produces build/page_template_guides.png: a 2475 x 2475 px (8.25 x 8.25 in at
300 dpi) transparent PNG with the bleed, trim, safe area, text zones and a
center cross marked. Open it in GIMP with File > Open as Layers on top of a
page, keep it visible while composing, and hide it before exporting.

Spec source: 00_story-bible.md section 7.5.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DPI = 300
TRIM_IN = 8.0
BLEED_IN = 0.125
SAFE_IN = 0.75  # from trim edge, for text and faces

SIZE = round((TRIM_IN + 2 * BLEED_IN) * DPI)  # 2475
TRIM = round(BLEED_IN * DPI)  # 38 (37.5 rounded)
SAFE = math.ceil((BLEED_IN + SAFE_IN) * DPI)  # 263 (262.5 rounded inward)
SAFE_END = SIZE - SAFE  # 2212
MID = SIZE // 2

RED = (220, 40, 40, 255)
BLUE = (30, 110, 220, 255)
GREEN = (20, 150, 70, 255)
ZONE_FILL = (30, 110, 220, 28)
GREY = (120, 120, 120, 200)


def dashed_rect(draw, box, color, width, dash=40, gap=24):
    x0, y0, x1, y1 = box
    for a, b, fixed, horizontal in (
        (x0, x1, y0, True), (x0, x1, y1, True), (y0, y1, x0, False), (y0, y1, x1, False)
    ):
        pos = a
        while pos < b:
            end = min(pos + dash, b)
            if horizontal:
                draw.line([(pos, fixed), (end, fixed)], fill=color, width=width)
            else:
                draw.line([(fixed, pos), (fixed, end)], fill=color, width=width)
            pos = end + gap


def main():
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 34)
    except OSError:
        font = ImageFont.load_default()

    # Text zones: upper half of the safe area, left and right halves.
    gutter = 40
    left_zone = (SAFE, SAFE, MID - gutter, MID)
    right_zone = (MID + gutter, SAFE, SAFE_END, MID)
    for zone, label in ((left_zone, "TEXT ZONE L"), (right_zone, "TEXT ZONE R")):
        d.rectangle(zone, fill=ZONE_FILL, outline=BLUE, width=3)
        d.text((zone[0] + 20, zone[1] + 16), label, fill=BLUE, font=font)

    d.rectangle((TRIM, TRIM, SIZE - TRIM, SIZE - TRIM), outline=RED, width=4)
    d.text((TRIM + 14, SIZE - TRIM - 50), "TRIM 8 x 8 in (outside = bleed, cut off)", fill=RED, font=font)

    dashed_rect(d, (SAFE, SAFE, SAFE_END, SAFE_END), GREEN, 4)
    d.text((SAFE + 14, SAFE_END - 50), "SAFE: text and faces inside", fill=GREEN, font=font)

    d.line([(MID - 30, MID), (MID + 30, MID)], fill=GREY, width=2)
    d.line([(MID, MID - 30), (MID, MID + 30)], fill=GREY, width=2)

    out = Path(__file__).with_name("page_template_guides.png")
    img.save(out, dpi=(DPI, DPI))
    print(f"{out} {SIZE}x{SIZE}px trim@{TRIM}px safe {SAFE}-{SAFE_END}px")


if __name__ == "__main__":
    main()
