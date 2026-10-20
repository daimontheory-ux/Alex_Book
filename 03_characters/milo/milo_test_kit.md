# Milo Test Kit: poses, expressions, fade and glow

**Purpose:** develop and lock everything Milo needs for *Right Here With You* (bible v1.2), in a fixed order, before page art. Noah, Mom and Boris follow the same pattern next.

**Source of truth:** `00_story-bible.md` §3.2 (look), §5 (fade and glow), §7.5 (print). Page uses: `milo.md` → Page map (v1.0).

## How to run every prompt

- **Midjourney V7**, the proven recipe RC-A1: **Omni Reference** slot = `milo_front_LOCKED.png` (from the repo; or the "Milo Standing Neutral" image if it's still in your Midjourney uploads) at `--ow 100`; **Styles** slot = `STYLE_ANCHOR.png` at `--sw 60`.
- The prompts below are complete. Paste as-is; don't type `--sref` or `--oref` (the slots replace them).
- Run each prompt **once** (4 candidates). Reroll up to **3 times**. If none pass, stop and bring the best one here; we'll adjust the wording rather than burn rolls.
- Log every run in the Google Sheet "Alex Book – Midjourney Test Log" (Test Log tab): ID below, version, recipe, job URL, pass/fail per check.
- Save picks as `milo_<ID>_LOCKED.png` in `03_characters/milo/` (e.g. `milo_P-3d_LOCKED.png`).

## The pass checklist (every image)

- ☐ **Hair:** golden blond (not ginger), short clipped sides with **ears showing**, shaggy wavy top with a middle part.
- ☐ **Eyes:** clear whites and **black pupils** (no blue irises). If irises come out blue but all else passes, keep it; we recolor in GIMP as before.
- ☐ **Freckles** present.
- ☐ **Size:** small 7-year-old, about 3.5 heads tall.
- ☐ **Outfit:** all blue, no logos.
- ☐ **Style:** matches the anchor's line and pale wash.
- ☐ **Clean background:** plain white, no props unless the row says so, no signature marks.
- ☐ **Emotion:** reads at a glance as the row's target (the "Must read as" column).
- ☐ **No glow, rim light or see-through effects** baked in (those are added in GIMP).

## Stage A: the three critical poses (run first)

These carry the book's meaning (lonely, patient, noticing). If V7 can hold Milo through these, the rest will follow. **After Stage A, bring the picks here for review before Stage B.**

### P-3d: Alone under the tree (p. 10)
**Attach:** Omni Reference = `03_characters/milo/milo_front_LOCKED.png` (`--ow 100`); Styles = `03_characters/style-anchor/STYLE_ANCHOR.png` (`--sw 60`). Nothing else: the expression sheets carry ginger hair and blue irises, and head-only crops pull the framing to a close-up. Leaves are excluded because the anchor's leaf pile tends to appear under seated figures.
**Must read as:** Sad and small, never angry or sulking. No tears (hurt here is quiet). Room above his head for the text zone.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, sitting on the ground hugging his knees to his chest, chin resting on his knees, sad and lonely, eyes looking down, seen from his eye level, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, angry, crying, tears, autumn leaves, leaf pile
```

### P-3g: Lying on the rug (pp. 15–17)
**Must read as:** Eyes **open** and soft. Body flat and patient, not napping and not playful.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, eyes open, lying flat on his stomach on the floor, cheek resting on his folded hands, calm gentle eyes looking forward, very still and patient, seen from floor level, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, sleeping, closed eyes, pillow
```

### P-3h: Looking at his hand (pp. 18, 20)
**Must read as:** Curious and wondering, a little uncertain. The hand is clearly the focus of his gaze.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, sitting cross-legged, holding one open hand up in front of his face, studying his palm with a curious, wondering expression, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

**Optional method check (one run):** repeat P-3g on the **V8 Edit** path (delete `--v 7`, `--ow 100`; put the Milo reference in the Edit/reference slot, anchor in Styles). Lying-down poses are where Omni Reference drifts most, so this is the fairest comparison. Log it as P-3g-V8.

## Stage B: the remaining poses

Run in this order (most-used pages first).

### P-3a: At the piano (pp. 1, 26, 28)
**Must read as:** Hands at keyboard height. **No piano** (it comes from the setting). If the stool vanishes, delete `background scenery` from `--no` and reroll.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, sitting on a plain low wooden stool in three-quarter view, both hands raised forward as if playing piano keys, happy concentrated smile, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, piano
```

### P-3b: Shooting (pp. 4, 5, 24)
**Must read as:** Readable motion; ball in hand or just leaving it; **no hoop**.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, jumping to shoot a basketball, arms up over his head, ball leaving his hands, eyes on a hoop above, determined, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, hoop
```

### P-3h2: Looking at both hands (standing) (p. 20)
**Must read as:** The "noticing" moment: concern rising, not panic.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, standing, looking down at both open hands held in front of him, worried and surprised, noticing something, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### P-3i: The big breath (p. 22)
**Must read as:** Calm effort, not a tantrum and not holding his breath angrily.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, standing, eyes gently closed, cheeks puffed out, slowly letting out a big breath, shoulders dropping and relaxing, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### P-3f: Looking back (p. 14)
**Must read as:** The realization face: softening, not frowning.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, kneeling on the floor, half turned away, looking back over his shoulder with a soft, worried, thoughtful face, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### P-3e: Reaching under (pp. 12, 13)
**Must read as:** Arm clearly reaching low and forward; the couch comes from the setting.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, kneeling on the floor, reaching one arm forward and low as if under a couch, frowning, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, couch, furniture
```

### P-3c: Arms limp (p. 9)
**Must read as:** Deflated, small.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, standing alone, arms hanging limp at his sides, shoulders slumped, looking down at the ground, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### P-3j: Sitting, leaning back (p. 23)
**Must read as:** Relaxed and settled; color-back moment.

```
full body, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, sitting on the ground with his legs stretched out in front of him, leaning back on his hands, calm and settled, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

## Stage C: close-up expressions (head and shoulders)

For close-up insets and for faces to swap onto a pose in GIMP if a body is right but the face isn't. Sets 1–2 already cover grin, shout, worried, scowl, hopeful and content.

### E-1: Lonely (p. 10)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, sad and lonely, eyes looking down, mouth small, eyebrows tilted up in the middle, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery, angry, tears
```

### E-2: Wondering (pp. 18, 20)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, curious and wondering, eyes wide, eyebrows raised, mouth slightly open, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### E-3: Gentle whisper (p. 15)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, calm and gentle, soft eyes, mouth just open as if whispering, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### E-4: Big breath (p. 22)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, eyes gently closed, cheeks puffed out, letting out a long slow breath, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### E-5: Relieved (pp. 23, 24)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, relieved small smile, eyebrows relaxed, eyes soft, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

### E-6: Held (p. 27)
```
head and shoulders, the same small 7-year-old boy from the reference image, about three and a half heads tall, pale golden blond curtain haircut with short neatly clipped sides and back and ears showing, soft shaggy wavy hair on top parted down the middle, light freckles across his nose and cheeks, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, eyes closed, cheek pressed against something soft, peaceful contented small smile, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, long sides, teenager, tall, lanky, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

## Stage D: fade and glow test in GIMP

Do this as soon as **P-3d** and **P-3a** are locked (the book's G3 and G0 extremes). It sets the one glow strength for the whole book and proves the cut-outs are clean.

1. **Cut out** P-3a and P-3d per `docs/gimp-workflow.md` §3 (Foreground Select + layer mask, never Color to Alpha). Do the halo check over a dark layer.
2. **Build `build/glow_bloom.png`** (workflow §5): 1200 px, radial, `#F2C14E` → transparent.
3. **Test sheet:** new 2475 × 2475 px page, white. Place **four copies of P-3a** across the top row at **G0, G1, G2, G3** (layer opacity 100/75/50/30 %, Hue-Saturation saturation 0/−20/−45/−70). Place **P-3d at G3** on the bottom half over a light tree-trunk wash (any quick brush stroke), to see how the background shows through a faded figure.
4. **Glow on every copy:** scale the bloom to about 1.5× Milo's chest width, center on his heart, layer **above** the figure. Save the sheet three times with glow opacity **25%, 35% and 45%**.
5. **Print all three** at 100% scale.
6. **Judge on paper:**
   - ☐ G0: the glow feels like warmth, not a spotlight or a stain on the shirt.
   - ☐ G3: the glow is clearly the warmest thing about him.
   - ☐ The four steps are distinguishable side by side; G1 is subtle but visible.
   - ☐ G3 over the trunk still reads as Milo (figure not lost in the background).
   - ☐ No white halos around faded figures.
   - ☐ The glow doesn't look like a halo or a superpower.
7. **Record:** the chosen glow opacity and any step changes in bible §5.4 (Strength); close bible §9 item 2. Commit the test sheet as `build/tests/fade_glow_test_<opacity>.png`.

**If a step fails:** G1 invisible → raise its saturation cut to −30; G3 lost on backgrounds → G3 opacity 35%; glow too yellow on the blue shirt → shift the color toward `#F5D27A` (paler gold).

## What comes back to me after each stage
- **Stage A:** the picks (and any near misses) attached in chat, with the job URLs. I review against the checklist, recolor irises if needed, and lock them in `milo.md`.
- **Stage B and C:** same.
- **Stage D:** a phone photo of the three printed sheets and your pick.

## Then: Noah, Mom, Boris
Same structure: turnaround → critical poses (Noah #2 and #4; Boris #2; Mom #2 and the hug test) → remaining poses → a quick fade check on Noah and Boris at G2 (their glow appears only when faded).
