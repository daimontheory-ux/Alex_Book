# Style Anchor

The one image that defines how the whole book *feels*. It becomes `--sref` on every later prompt.

## What we're looking for
- **Cartoon proportions:** an **oversized round head** (about 1/3 of total body height, "3 heads tall"), a small compact body, and short limbs. Big hands and feet are fine.
- **Simple face:** small oval eyes with dot pupils, a tiny simple nose (or none), and a **big, elastic mouth** that carries the emotion. Expression comes from the mouth and eyebrows, not from detail.
- **Economical linework:** few lines, each one confident. A brush-ink contour with thick-to-thin variation. **No hatching, cross-hatching, or texture lines.** Clothing folds are suggested with one or two strokes.
- **Transparent watercolor** washes, lightly applied, that don't fully fill the outlines (some white showing through).
- **Mostly white paper.** Scenery only suggested (a few strokes for grass, one tree).
- Soft, warm **autumn** palette: reds, oranges, mustard yellow, plus the blue of Milo's outfit.
- Calm overall. Nothing busy, nothing glossy, no 3D or digital shading.

## Vocabulary that drives the look
Midjourney responds to *descriptions of features*. These are the phrases doing the work:

| Goal | Phrases that work | Add to `--no` |
|---|---|---|
| Big head | `oversized round head, big head small body, cartoon proportions three heads tall, short stubby limbs` | `realistic proportions, tall, lanky` |
| Simple face | `simple oval eyes with dot pupils, tiny simple nose, big expressive mouth, minimal facial detail` | `detailed eyes, eyelashes, anime eyes` |
| Simple lines | `clean economical brush-ink outlines, bold confident contour lines, few lines, minimal detail, newspaper comic strip drawing` | `hatching, cross-hatching, sketchy lines, texture, detailed rendering` |
| Light color | `flat light watercolor tint, color lightly washed inside the lines, white paper showing through` | `shading, gradients, airbrush, 3d` |

**Avoid** "chibi" and "anime." They also make big heads, but they pull toward a Japanese style with huge sparkly eyes. "Newspaper comic strip" pulls in the right direction.

## Prompt A: kid in motion (recommended first try)
```
newspaper comic strip style children's picture book illustration of a joyful 7-year-old boy leaping through a pile of autumn leaves, oversized round head, big head small body, cartoon proportions three heads tall, short stubby limbs, simple oval eyes with dot pupils, big open-mouth grin, minimal facial detail, clean economical brush-ink outlines with thick-to-thin line variation, few lines, flat light watercolor tint washed inside the lines, white paper showing through, mostly white background, scenery only suggested with a few strokes, soft warm autumn palette of red orange and mustard yellow, lots of negative space --ar 1:1 --stylize 75 --raw --no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, hatching, cross-hatching, realistic proportions, detailed eyes, anime, chibi, 3d, shading, gradient background
```

## Prompt B: quiet scene (tests restraint)
```
newspaper comic strip style children's picture book illustration of a small boy sitting alone under a big autumn tree with his chin in his hands, leaves drifting down, oversized round head, small body, cartoon proportions three heads tall, simple oval eyes with dot pupils, minimal facial detail, clean economical brush-ink outlines, few lines, flat light watercolor tint, almost entirely white paper, only the tree and a few leaves painted, soft muted warm palette, gentle mood, generous negative space --ar 1:1 --stylize 75 --raw --no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, hatching, cross-hatching, realistic proportions, detailed eyes, anime, chibi, 3d, shading, gradient background
```

## Tuning knobs
- **Head still too small:** move the proportion phrases to the **front** of the prompt (Midjourney weights early words more). Or add "head as wide as his shoulders".
- **Lines too busy or sketchy:** lower `--stylize` to 25–50 and keep `--raw` on. Add "drawn with a single brush, minimal strokes."
- **Too plain or stiff:** raise `--stylize` to 100–150 and add "dynamic action pose, lively."
- **Not enough white:** add "vignette fading to white paper, unpainted edges."
- **Colors too saturated:** add "muted, faded, light watercolor tint."
- **Strongest fix of all, a sketch of your own:** draw a quick stick-figure-with-a-big-circle-head pose on paper, photograph it, and add it as an **Image Prompt** (the first reference slot). Midjourney will borrow the proportions. Your sketch doesn't need to be good; the shapes are what matter.

Once one image nails the look, it becomes the style reference, and **every later prompt inherits the proportions and line quality automatically.** That's why this step gets the most re-rolls.

## Lock record
| Field | Value |
|---|---|
| Chosen file | `STYLE_ANCHOR.png` |
| Prompt used | |
| Model version | |
| Midjourney job URL | |
| `--sref` URL | |
| Approved by / date | |
