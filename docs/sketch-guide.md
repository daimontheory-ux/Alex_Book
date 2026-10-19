# Composition Sketches: How to Use Them Without Causing Drift

Rough stick-figure sketches of key pages are worth doing. They answer **where things go**, which is the question words alone handle worst. Used the wrong way, though, they can pull Midjourney toward stick-figure drawing. The rule:

> **Sketches control composition. References control the characters and the style. Never let a sketch do the references' job.**

## Which pages to sketch
These pages are composition-critical: framing or placement *is* the storytelling.

| Page | Why it needs a sketch |
|---|---|
| 7 | GO AWAY: faint Milo plus a big shout bubble; balance the two |
| 9 | Noah walking away vs. small, faint Milo; lots of white space |
| 10 | Alone under the tree; the glow should be the focal point |
| 14 | Milo looking back over his shoulder; Boris in the couch gap |
| 15–17 | Same camera on the rug across three pages, so the color returning reads as time passing |
| 20–22 | Noticing → GO— → breath: keep Milo in the same spot so only his face and color change |
| 27–28 | The hug and the final dusk image with two glows |

Single-character action pages (p. 1, 5, 12…) usually don't need one. The beat sheet's description is enough.

## How to draw them
- One 8×8 square per page. Pencil or marker on paper; phone photo is fine.
- **Heads as big circles** at roughly the right proportions (kids 3.5 heads tall, parents 2× Milo). Even a stick figure should carry the book's proportions.
- **Box the text zone** (upper L or R) and **mark each glow position** (center of chest) with a small circle.
- Label figures with initials (M, N, B, Mom) and add arrows for gaze or motion.
- Keep it *crude*. Detail in a sketch is just more for Midjourney to copy.

## How each sketch is used (two routes, chosen per page)
1. **Canva route (default, zero drift):** the sketch is the **layout plan**. Characters are generated separately on white with their references, then placed in Canva to match the sketch. Midjourney never sees the sketch.
2. **Image Prompt route (only for single-image scenes such as the puddle or mirror):** add the sketch photo in the **Image Prompt** slot with a **low image weight, `--iw 0.25` to `0.5`**. At that weight it guides layout and camera angle while the style and character references still control how everything looks. If stick-figure qualities start appearing (thin limbs, flat shading), lower `--iw` or switch to the Canva route.

## Workflow
Photograph the sketches and attach them in chat (or commit them to `05_pages/sketches/page_NN.jpg`). Claude turns each one into that page's prompt, its route (Canva or Image Prompt), and a Canva layout note in `05_pages/page_NN.md`.
