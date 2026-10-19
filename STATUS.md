# Project Status: *Right Here With You* (working title)

**Read this first at the start of every working session.** Last updated 2026-10-19.

> **2026-10-19 pivot:** the plot moved from *The Happy Meter* to a Dr. Becky Kennedy "Deeply Feeling Kids" story. The old book is preserved in git branch `archive/happy-meter-v0.7`. Gates 1–3 are reopened as v1.0 drafts.

## Gate status
| Gate | Deliverable | Status |
|---|---|---|
| 1 | Story bible (`00_story-bible.md`) | 🟡 v1.2 draft, awaiting approval (2 open items, §9) |
| 2 | Beat sheet (`01_beat-sheet.md`) | 🟡 v1.1 draft, awaiting approval |
| 3 | Manuscript (`02_manuscript.md`) | 🟡 v1.1 draft, awaiting approval |
| 4 | Character references (`03_characters/`) | 🟡 In progress (repathed for v1.0) |
| 5 | Setting references (`04_settings/`) | ☐ Not started |
| 6 | Page art (`05_pages/`) | ☐ Not started |
| 7 | GIMP pages → PDF → proof copy (`build/`) | 🟡 Tools ready: page guides, `make_pdf.py`; target PrestoPhoto 8×8 hardcover |

## Gate 4 detail
| Asset | Status |
|---|---|
| Style anchor | ✅ `STYLE_ANCHOR.png` |
| Milo turnaround (+ front, 3/4 crops) | ✅ (carries over) |
| Milo expressions sets 1–2 | ✅ (carry over; remapped to v1.0 pages in `milo.md`) |
| Milo set 3: full-body poses 3a–3j | ☐ **Next.** Start with the critical ones: 3d, 3g, 3h |
| Boris turnaround + poses | ☐ Prompts ready (#2 peering is critical) |
| Noah turnaround + poses | ☐ Prompts ready (#2 hurt, #4 sitting on ball are critical) |
| Mom turnaround + poses + hug test | ☐ Prompts ready |
| Size lineup with glow marks (GIMP) | ☐ |
| ~~Nia, Owen + cat, Dad~~ | Retired (`03_characters/_retired/`) |

## House rules (locked)
- Style anchor in the **Styles** box on every prompt, with `--sw 60` and "soft, pale, muted, calm transparent watercolor."
- **Black pupils** on all human characters, never colored irises (Boris keeps green eyes).
- Character consistency: **V7 + Omni Reference**. **One character per generation**, always on white, composited in GIMP (now required, because fading and the glow are per-character layers).
- **Every character is generated at full color.** Fading, the glow, text and speech bubbles are all added in GIMP, never by AI. Prompts exclude `glow, glowing, light rays, transparency, ghost`.
- Kids about 3.5 heads tall; Mom lean, adult proportions, 2× Milo's height.
- Prompts describe the style. They never name a real artist.

## Production setup (2026-10-19)
- **Tool:** GIMP 3 for compositing, fade, glow and lettering (`docs/gimp-workflow.md`).
- **Printer:** PrestoPhoto 8×8 in hardcover from our own PDF (bible §7.5). Confirm page-count rules, paper, layflat option and cover template before ordering.
- **Page files:** 2475 × 2475 px, sRGB, text and faces inside the ¾ in safe area (`build/page_template_guides.png`).

## Open decisions (bible §9)
1. Hug image method for p. 27 (V8 Edit vs. composite): decide after a test. The hug is the book's peak.
2. Glow strength (one fixed value for the whole book): set in the GIMP test.

Resolved 2026-10-19: friend = **Noah**; Mom's line = refrain only; glow = always-on round bloom around Milo's heart, others only when faded.

## Next actions
1. Daimon reviews bible, beat sheet and manuscript v1.1.
2. Milo set 3 poses: 3d, 3g, 3h first (Prompt 3 in `milo.md`).
3. Boris → Noah → Mom (turnaround, then poses), then the hug test.
4. **GIMP fade/glow test** (`docs/gimp-workflow.md` §8): Milo at G0–G3 with the heart bloom at 25/35/45%; print and pick one strength.
5. Size lineup with glow marks → close Gate 4.
6. Gate 5: living room (piano, couch with dark gap, rug, lamp) and park (half-court, big tree).
