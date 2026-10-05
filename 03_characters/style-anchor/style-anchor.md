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

## Round 1 results (2026-10-04)

Daimon's review of the first three generations, saved here as reference inputs:

| File | Keep | Reject |
|---|---|---|
| `ref_A_linework.png` | **Linework level and detail.** Light, economical, airy. | Ball-shaped head, dot eyes, stick-like hair, weak expression |
| `ref_B_face.png` | **Facial style.** Big eyes with whites, expressive brows, open grin, rosy cheeks. | Line too heavy and busy; jacket detail; chunky body |
| `ref_C_watercolor.png` | **Leaves and background.** Almost no outlines, all loose watercolor. | Busy plaid shirt; chunky body |

**Strategy:** no single image has everything, so we **blend them as weighted style references** and use words to steer what references can't fix (head shape, hair, outfit). See Prompt C.

## Prompt C: blended anchor (use this next)
Upload all three `ref_*.png` files to Midjourney first. Then paste this, replacing `<A>`, `<B>`, `<C>` with each image's URL. To get a URL, open the image on the Midjourney site and use "Copy image address."

```
classic newspaper comic strip style children's picture book illustration of a joyful 7-year-old boy leaping over a pile of autumn leaves, large head on a small slim body with thin arms and legs, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, small button nose, rosy cheeks, wide open-mouth grin, full voluminous blond hair parted in the middle with long wavy locks falling to each side of his face, hair drawn as a few bold flowing brush-stroke clumps, plain light blue t-shirt, blue jeans, blue sneakers, light economical hand-inked outlines on the boy only, the leaves and background painted in loose calm watercolor with almost no outlines, white paper showing through, mostly white background, lots of negative space --ar 1:1 --stylize 100 --sref <A>::2 <B>::1 <C>::1 --no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, hatching, cross-hatching, perfectly round ball-shaped head, dot eyes, stick-like hair, spiky hair, jacket, plaid, chubby body, anime, chibi, 3d, gradient background
```

### Reading the `--sref` weights
`::2` means "twice as much influence." Start at **A = 2, B = 1, C = 1**, then adjust one at a time:

| What you see | Change |
|---|---|
| Lines too heavy or busy | Raise **A** to 3 |
| Face too simple; eyes small again | Raise **B** to 2 |
| Leaves getting outlined | Raise **C** to 2 |
| Body too chunky | Add "skinny, lanky little kid" to the prompt |
| Hair spiky or stick-like | Add "soft rounded hair clumps, thick brush" to the prompt |

**Why words *and* references:** the style references control *how things are drawn* (line, wash, face rendering). They don't reliably control *what is drawn* (head shape, hair style, outfit). That's what the words are for, which is why the prompt describes the hair and body so specifically.

### Two ways to load the references
- **Simple (recommended first):** drag all three images into the **Style Reference** slot and **delete the whole `--sref <A>::2 <B>::1 <C>::1` text** from the prompt. The slot replaces it. The three blend equally, and you steer with words. Use `--sw` (style weight, default 100) to turn the overall style influence up (e.g. 200) or down (e.g. 50).
- **Weighted (only if needed):** remove the images from the slot. In your uploads, right-click each image → **Copy image address**, and paste each URL in place of `<A>`, `<B>`, `<C>`. Typed URLs with `::` weights are the only way to weight them individually.

## Prompt A: kid in motion (round 1, superseded by Prompt C)
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

## Anchor review (2026-10-04)
| Criterion | Result |
|---|---|
| Proportions: big head, slim body, thin limbs | ✅ Strong. The right silhouette. |
| Big expressive eyes, mobile brows | ✅ |
| Hand-inked, light, lively line on the figure | ✅ |
| Hair volume and brush clumps | ✅ volume / ⚠ **style is a swept-up quiff, not Milo's middle-part curtain.** Fix in Milo's prompts, not here. |
| Calm, delicate watercolor | ⚠ The leaf pile is denser and more saturated (red-orange, black accents, flame-like strokes) than "calm." Acceptable for a style anchor; watch for it in page art. |
| Mostly white paper | ✅ |

**Watch-outs when using this anchor:**
- If page art comes out too intense or too orange, lower `--sw` to 50–75, or add "soft, pale, muted watercolor" to the prompt.
- The quiff may bleed into Milo. His prompts now exclude it explicitly.

## Lock record
| Field | Value |
|---|---|
| Chosen file | `STYLE_ANCHOR.png` ✅ |
| Prompt used | Prompt C text (above), without the `--sref` chunk; refs A, B, C loaded via the Styles box, equal weight |
| Exact prompt | classic newspaper comic strip style children's picture book illustration of a joyful 7-year-old boy leaping over a pile of autumn leaves, large head on a small slim body with thin arms and legs, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, small button nose, rosy cheeks, wide open-mouth grin, full voluminous blond hair parted in the middle with long wavy locks falling to each side of his face, hair drawn as a few bold flowing brush-stroke clumps, plain light blue t-shirt, blue jeans, blue sneakers, light economical hand-inked outlines on the boy only, the leaves and background painted in loose calm watercolor with almost no outlines, white paper showing through, mostly white background, lots of negative space |
| Model version | V8.2 (default) |
| Upscale | Subtle |
| Midjourney job URL | https://www.midjourney.com/jobs/fbb1c4b5-aa29-4ef2-897f-bdd7bce556e6?index=0 |
| Approved by / date | Daimon, 2026-10-04 |
