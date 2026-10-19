# GIMP Page Workflow

How each page is assembled in GIMP 3 from the locked Midjourney pieces. Spec source: story bible §5.4 (fade and glow) and §7.5 (print and file spec). The bible wins any conflict.

## 1. Page setup (once per page)
1. **File → New:** 2475 × 2475 px, 300 ppi, sRGB, fill **white**. (8 × 8 in trim + ⅛ in bleed all round.)
2. **File → Open as Layers →** `build/page_template_guides.png`. Keep it on top while composing; hide it before export.
3. Save as `05_pages/page_NN.xcf`. The XCF is the working file; the PNG export is what prints.

## 2. Layer stack (top to bottom)
| Layer | Notes |
|---|---|
| `guides` | Hidden before export |
| `text` + `bubbles` | Lettering (section 6) |
| `glow_milo`, `glow_noah`, `glow_boris` | Above the figures; Milo's on every page, others only when faded |
| `milo`, `noah`, `mom`, `boris` | One cut-out figure per layer, each with its fade step |
| `setting` | Hoop, tree, piano, couch: 1–3 props, light |
| `background` | White paper (the default fill) |

## 3. Cutting characters out of their white backgrounds
- **Don't use Color to Alpha** on the figures. It turns the pale watercolor washes partly transparent, so the figure would look faded even at full color.
- Use **Foreground Select** (or Fuzzy Select on the white, then Select → Invert), **Select → Grow 1–2 px**, then add a **layer mask** from the selection. Masks keep the original pixels if an edge needs fixing.
- **Halo check:** temporarily put a dark layer under the figure and look at 100% zoom. Any white fringe will show up badly once the figure is faded; clean it now.
- Save each clean cut-out as `05_pages/cutouts/<character>_<pose>.png` so it can be reused on other pages.

## 4. Sizing and upscaling
- Scale every figure to the size lineup (`03_characters/lineup/`) so Mom ≈ 2× Milo and Noah = Milo on every page.
- A figure needs about **300 px per printed inch**. A Milo printed 4 in tall needs ≥1200 px of real detail.
- Midjourney images are usually smaller than a full page. Up to about 1.5× enlargement in GIMP (**Image → Scale**, interpolation **NoHalo**) is usually fine for watercolor. Beyond that, upscale first (Midjourney's Upscale, or a dedicated upscaler) and check at 100% zoom.

## 5. Fade and glow
**Fade step** on a figure layer: set **layer opacity**, then add **Colors → Hue-Saturation** as a non-destructive filter on the layer (GIMP 3), so the step can be changed later.

| Step | Layer opacity | Saturation |
|---|---|---|
| G0 | 100% | 0 |
| G1 | 75% | −20 |
| G2 | 50% | −45 |
| G3 | 30% | −70 |

**Glow (built once):**
1. New transparent image 1200 × 1200 px.
2. Foreground color warm gold, starting value `#F2C14E`.
3. **Gradient tool:** gradient **FG to Transparent**, shape **Radial**. Drag from the exact center to the edge.
4. Export as `build/glow_bloom.png`.

**On each page:** **File → Open as Layers →** `glow_bloom.png`; **Layer → Scale Layer** to about 1.5× the character's chest width; center it on the heart; place it **above** that character's figure; set its **opacity to the book's single glow value** (from the test below). Never change it page to page.

## 6. Lettering
- Install the two chosen fonts (dialogue and narration) and use them on every page.
- **Text stays inside the safe area** and in the page's text zone (L or R in the beat sheet).
- **Speech bubbles:** Ellipse Select → fill white → **Edit → Stroke Selection** (about 5 px, ink color) → tail with Free Select, filled and stroked the same way. Build one of each bubble type (round, small, thought cloud, jagged GO AWAY, the soft "Right here with you" bubble) in `build/bubbles.xcf` and copy them from there so they match on every page.

## 7. Export and build the PDF
1. Hide `guides`. Check that the page has no transparent areas (the white background layer must be visible).
2. **File → Export As →** `build/pages/page_NN.png` (PNG, keep the 300 ppi resolution). Name the title page `page_00_title.png` so it sorts first.
3. When all pages are exported, from the repo root:
   ```
   pip install img2pdf pillow
   python build/make_pdf.py --check-only   # checks every page is 2475 x 2475 and opaque
   python build/make_pdf.py                # writes build/right_here_with_you.pdf
   ```
4. Upload the PDF to the print service and order **one proof copy** first.

## 8. The fade and glow test (do this before any page art)
1. New page per section 1. Place `milo_front_LOCKED.png` four times in a row, set to G0, G1, G2 and G3.
2. Add the glow to each at the same opacity. Try three versions of the page: glow at **25%, 35% and 45%**.
3. Print at 100% scale on a home printer (a rough check; the real proof comes later).
4. Pick the strength that feels like warmth at G0 and still clearly stands out at G3. Record it in the bible (§5.4 Strength) and close bible §9 item 2.
