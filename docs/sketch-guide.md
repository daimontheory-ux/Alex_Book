# Composition Sketches: How to Use Them Without Causing Drift

Rough stick-figure sketches of key pages are worth doing. They answer **where things go**, which is the question words alone handle worst. Used the wrong way, though, they can pull Midjourney toward stick-figure drawing. The rule:

> **Sketches control composition. References control the characters and the style. Never let a sketch do the references' job.**

## Which pages to sketch
These pages are composition-critical: framing or placement *is* the storytelling.

| Page | Why it needs a sketch |
|---|---|
| 7 | First meter. Placement of Noah walking away vs. Milo; lots of white space |
| 11 | Ghosted Boris overlapping present-moment Boris |
| 18 | Puddle reflection: the meter appears only in the reflection |
| 22–23 | Holding the NO; the bubble pushing up from his chest |
| 26 | Piano-panel reflection (must mirror p. 18's framing) |
| 27 | Nia and Milo on the bench, the mystery beat |
| 28 | Bathroom mirror, final image |

Single-character action pages (p. 1, 5, 12…) usually don't need one. The beat sheet's description is enough.

## How to draw them
- One 8×8 square per page. Pencil or marker on paper; phone photo is fine.
- **Heads as big circles** at roughly the right proportions (kids 3.5 heads tall, parents 2× Milo). Even a stick figure should carry the book's proportions.
- **Box the text zone** (upper L or R) and **mark the meter zone** above heads with a dashed line.
- Label figures with initials (M, N, Ni, O, B) and add arrows for gaze or motion.
- Keep it *crude*. Detail in a sketch is just more for Midjourney to copy.

## How each sketch is used (two routes, chosen per page)
1. **Canva route (default, zero drift):** the sketch is the **layout plan**. Characters are generated separately on white with their references, then placed in Canva to match the sketch. Midjourney never sees the sketch.
2. **Image Prompt route (only for single-image scenes such as the puddle or mirror):** add the sketch photo in the **Image Prompt** slot with a **low image weight, `--iw 0.25` to `0.5`**. At that weight it guides layout and camera angle while the style and character references still control how everything looks. If stick-figure qualities start appearing (thin limbs, flat shading), lower `--iw` or switch to the Canva route.

## Workflow
Photograph the sketches and attach them in chat (or commit them to `05_pages/sketches/page_NN.jpg`). Claude turns each one into that page's prompt, its route (Canva or Image Prompt), and a Canva layout note in `05_pages/page_NN.md`.
