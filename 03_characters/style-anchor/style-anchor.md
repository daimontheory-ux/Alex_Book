# Style Anchor

The one image that defines how the whole book *feels*. It becomes `--sref` on every later prompt.

## What we're looking for
- **Cartoon proportions, not a ball head:** a **large head** (about 1/4 of body height, "four heads tall") with a **soft, slightly wide oval** shape, a rounded cheek and chin, and **real volume of hair** on top. *Not* a perfectly round, bald, ball-shaped head.
- **Big expressive eyes:** large eyes with clear whites and dark pupils, and **mobile eyebrows**. The eyes and mouth carry the emotion together.
- **Full, flowing hair:** drawn as **clumps of curved brush strokes** with weight and movement. *Not* thin spiky lines or stick-like strands.
- **Hand-inked line:** a lively **brush line that swells and tapers**, organic and slightly imperfect. Confident and sparse, but never thin or vector-clean. **No hatching or cross-hatching.**
- **Calm, delicate watercolor:** soft transparent washes, lightly applied, not fully filling the outlines, with white paper showing through.
- **Mostly white paper.** Scenery only suggested (a few strokes for grass, one tree).
- Soft, warm **autumn** palette: reds, oranges, mustard yellow, plus the blue of Milo's outfit.

## Vocabulary that drives the look
Midjourney responds to *descriptions of features*. These are the phrases doing the work:

| Goal | Phrases that work | Add to `--no` |
|---|---|---|
| Big head, right shape | `large head, cartoon proportions about four heads tall, soft wide oval head with rounded cheeks` | `perfectly round ball-shaped head, bald head, realistic proportions` |
| Big expressive eyes | `big expressive eyes with white highlights and dark pupils, expressive eyebrows` | `dot eyes, tiny eyes, anime eyes, eyelashes` |
| Full hair | `full voluminous hair drawn in flowing clumps of curved brush strokes, hair with weight and movement` | `spiky hair, stick-like hair, thin straight hair lines` |
| Hand-inked line | `hand-inked with a fine sable brush, lively fluid lines that swell and taper, organic hand-drawn imperfection, classic newspaper comic strip linework` | `hatching, cross-hatching, vector, thin uniform lines, digital lineart` |
| Calm watercolor | `calm delicate transparent watercolor washes, soft and lightly applied, white paper showing through` | `shading, gradients, airbrush, 3d, saturated colors` |

**Avoid** "chibi" and "anime" (huge sparkly eyes, Japanese style) and "round head" (pulls toward a bald, ball-headed comic look).

## Prompt A: kid in motion (recommended first try)
```
classic newspaper comic strip style children's picture book illustration of a joyful 7-year-old boy leaping through a pile of autumn leaves, large head with cartoon proportions about four heads tall, soft wide oval head with rounded cheeks, big expressive eyes with dark pupils, expressive eyebrows, big open-mouth grin, full voluminous blond hair drawn in flowing clumps of curved brush strokes with weight and movement, hand-inked with a fine sable brush, lively fluid lines that swell and taper, organic hand-drawn imperfection, calm delicate transparent watercolor washes, white paper showing through, mostly white background, scenery only suggested with a few strokes, soft warm autumn palette of red orange and mustard yellow, lots of negative space --ar 1:1 --stylize 125 --no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, hatching, cross-hatching, perfectly round ball-shaped head, bald head, dot eyes, spiky hair, stick-like hair, vector, thin uniform lines, anime, chibi, 3d, shading, gradient background
```

## Prompt B: quiet scene (tests restraint)
```
classic newspaper comic strip style children's picture book illustration of a small boy sitting alone under a big autumn tree with his chin in his hands, leaves drifting down, large head with cartoon proportions about four heads tall, soft wide oval head, big expressive thoughtful eyes, full voluminous hair drawn in flowing clumps of curved brush strokes, hand-inked with a fine sable brush, lively fluid lines that swell and taper, calm delicate transparent watercolor, almost entirely white paper, only the tree and a few leaves painted, soft muted warm palette, gentle mood, generous negative space --ar 1:1 --stylize 125 --no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, hatching, cross-hatching, perfectly round ball-shaped head, bald head, dot eyes, spiky hair, stick-like hair, vector, thin uniform lines, anime, chibi, 3d, shading, gradient background
```

## Tuning knobs
- **Head too small:** move the proportion phrases to the **front** of the prompt (Midjourney weights early words more).
- **Hair still stick-like:** don't use `--raw` or low `--stylize` (both strip out brushwork). Keep `--stylize` at 100–150. Add "thick ink brush strokes in the hair."
- **Lines too busy:** lower `--stylize` slightly (to about 100) and add "economical, confident linework." Avoid "few lines" and "minimal detail", which made the hair stick-like.
- **Best fix when one image is close:** use **Vary (Subtle)** on it rather than re-prompting. Or upload it as an **Image Prompt** to keep its proportions while you adjust the words.
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
