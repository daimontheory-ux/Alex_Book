# Milo: Character Reference

**Source of truth:** story bible §3.2 (v1.0). Put `STYLE_ANCHOR.png` in the Styles box (or replace `<SREF>` with its URL) and `<MILO_OREF>` with the locked turnaround URL once it exists.

## Locked description (paste-ready prompt fragment)
```
7-year-old boy, small short 7-year-old about three and a half heads tall, large head on a small slim body with short thin arms and short legs, blond curtain haircut with short neatly clipped sides and back and ears showing, longer shaggy wavy hair on top parted down the middle, wavy bangs falling to either side of his forehead, drawn in a few flowing brush-stroke clumps, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, big elastic mouth, plain light blue t-shirt, blue jeans, blue sneakers
```

## Prompt 1: Turnaround
```
character turnaround sheet for a children's picture book, small short 7-year-old boy about three and a half heads tall, blond curtain haircut with short neatly clipped sides and back and ears showing, longer shaggy wavy hair on top parted down the middle, wavy bangs falling to either side of his forehead, classic newspaper comic strip style, large head on a small slim body with short thin arms and short legs, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, wide happy grin, shown three times standing side by side: front view, three-quarter view, side view, full body, plain light blue t-shirt, blue jeans, blue sneakers, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white paper background --ar 3:2 --sref <SREF> --sw 60 --stylize 100 --no blue eyes, colored irises, tall, lanky, teenager, long legs, long hair, hair covering ears, mullet, quiff, pompadour, side-swept hair, hair swept up, hatching, cross-hatching, perfectly round ball-shaped head, dot eyes, stick-like hair, vector, realistic proportions, anime, text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, background scenery
```

## Prompt 2: Expression sheet
Milo's expressions are the emotional engine of the book. Each one maps to specific pages.

```
expression sheet for a children's picture book character, the same small 7-year-old boy shown six times, head and shoulders: huge open-mouth joyful grin; furious shouting with scrunched eyes and clenched fists; frozen wide-eyed surprise; narrowed eyes and tongue poking out in concentration; sheepish embarrassed small smile; wry knowing half-smile, blond curtain haircut with short clipped sides, shaggy wavy hair on top parted down the middle, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background --ar 3:2 --sref <SREF> --sw 60 --oref <MILO_OREF> --ow 100 --v 7 --no blue eyes, colored irises, long hair, quiff, pompadour, hatching, cross-hatching, perfectly round ball-shaped head, dot eyes, stick-like hair, vector, realistic proportions, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines
```

> Page numbers in this section and in the reviews below refer to the retired *Happy Meter* book. The current page map is in **Page map (v1.0)** further down.

**Two ways to run this (the version test):**
- **V7 path:** keep `--v 7`; drag `milo_front_LOCKED.png` into the **Omni Reference** slot and `STYLE_ANCHOR.png` into **Styles**; delete the `--sref <SREF>` and `--oref <MILO_OREF> --ow 100` text.
- **V8 path:** delete `--v 7`; drag `milo_front_LOCKED.png` into the **Edit / reference images** slot and `STYLE_ANCHOR.png` into **Styles**; delete the `--sref`/`--oref`/`--ow` text. Optionally start the prompt with "Draw this exact boy from the reference image as an expression sheet: ..."
- Whichever keeps the hair, eyes, freckles and shirt more faithful becomes the method for all page art.

## Note from the style anchor
The anchor's boy has the right face and proportions, but his hair is a **swept-up quiff**. Milo's cut is a **short-sided curtain cut**: sides and back clipped short (a #4 clipper guard, about ½ inch), ears showing, with longer **shaggy, wavy hair on top, parted down the middle**, and wavy bangs falling to either side of the forehead. Midjourney doesn't know clipper guard numbers, so the prompts describe the shape instead. If the hair grows long again, move the hair phrase to the **front** of the prompt.

**Height:** Milo is small, about 3.5 heads tall. Turnaround sheets tend to stretch figures, so the prompts say "small short" and exclude "tall, lanky, long legs." 

## Turnaround review (2026-10-04)
- ✅ Consistent across all three views. ✅ Small (about 3.5 heads tall). ✅ Big eyes with whites, expressive brows, grin. ✅ All-blue outfit. ✅ Ears showing; shaggy wavy top.
- ⚠ The middle part is soft rather than crisp, and the back reads slightly longer than a #4 cut. Both are accepted as-is; re-check on close-ups.
- ➕ **Freckles** appeared (light, across nose and cheeks). They're now **canon**: keep them on every page.

## Expressions set 1 review (2026-10-04, V7)
| Face (left→right, top row then bottom) | Reads as | Use for |
|---|---|---|
| 1 | Joyful grin ✅ | pp. 1, 4, 24–26 |
| 2 | Furious shout ✅ (the strongest "NO" face) | pp. 2, 6, 14 |
| 3 | Uneasy, arms crossed | p. 15 (the grudging "FINE") |
| 4 | Whiny yell, eyes narrowed | p. 6 alternate |
| 5 | Wince / alarmed yell | not needed; reads as pain or fear |

**Missing:** concentrating (tongue out), sheepish, wry half-smile, and "holding the NO." These come in set 2.
**Drift to watch:** the hair went **ginger/orange and spikier** than the turnaround's golden blond; **blue irises** appeared (the turnaround has black pupils); and skin is warmer. Two small fake "signatures" also appeared (bottom left, mid right). Erase them in Canva.

## Prompt 2b: Expressions set 2 (the missing faces)
```
expression sheet for a children's picture book character, the same small 7-year-old boy shown four times, head and shoulders: eyes narrowed and tongue poking out of the corner of his mouth in concentration; sheepish embarrassed small smile with eyes looking down; wry knowing half-smile with one eyebrow raised; eyes squeezed shut and cheeks puffed out holding his breath, pale golden blond curtain haircut with short clipped sides, soft shaggy wavy hair on top parted down the middle, light freckles, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, light blue t-shirt, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background --ar 3:2 --sref <SREF> --sw 60 --oref <MILO_OREF> --ow 150 --v 7 --no blue eyes, colored irises, red hair, ginger hair, orange hair, spiky hair, long hair, quiff, pompadour, signature, hatching, cross-hatching, dot eyes, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines
```
Changes from Prompt 2: four faces instead of six (fewer faces = more consistency), `--ow 150` (stronger character lock), and the hair color and texture pinned down ("pale golden blond," "soft") with ginger, orange, and spiky excluded.

## Expressions set 2 review (2026-10-05, V7 + Omni at `--ow 100`, recipe RC-A1)
Delivered as four single head-and-shoulders images rather than one 4-up sheet. File names describe what each face reads as; Daimon's upload names are in brackets.

| File | Reads as | Pupils | Use for | Status |
|---|---|---|---|---|
| `milo_expr2_hopeful.png` [Milo_Hopeful] | Hopeful, eyes up, warm smile | ✅ black | pp. 24–26 calm-happy beats | Keep |
| `milo_expr2_content_lookup.png` [Milo_Sheepish] | Content / daydreaming, eyes up | ✅ black | Daimon accepts as the sheepish face | ✅ Keep |
| `milo_expr2_scowl_sideeye.png` [Milo_Concentration] | Grumpy defiant side-eye, not concentration (no tongue) | ❌ blue irises | Strong oppositional face: pp. 2, 6, 15. Daimon accepts as the concentration face | ✅ Use `_fixed` (irises recolored black) |
| `milo_expr2_worried.png` [Milo_Worried] | Worried / unsure, eyes up | ❌ blue irises | pp. 7, 14, 27 (the "frozen" beats, softer version) | ✅ Use `_fixed` (irises recolored black) |

**Improved over set 1:** hair is golden blond (no ginger), freckles present on all four, no fake signatures, line and wash match the anchor.
**Still drifting:** blue irises on 2 of 4; side hair longer and shaggier than the clipped curtain cut (ears show, but sides aren't short); skin slightly warmer/orange than the turnaround.
**Pupil fix (2026-10-05):** blue irises on the scowl and worried faces were recolored to black in code (eye areas only; the rest of each drawing is untouched). The `_fixed` files are the ones to use; the originals stay as the raw Midjourney output.
**Still missing (set 3):** wry half-smile with raised eyebrow, and holding the NO (eyes squeezed shut, cheeks puffed). Daimon counts concentration and sheepish as covered by set 2.

## Page map (v1.0, *Right Here With You*)
Locked faces from sets 1–2 that carry over, and where they're used now:

| Asset | Reads as | v1.0 pages |
|---|---|---|
| Set 1 #1 | Joyful grin | 1, 3, 4 |
| Set 1 #2 | Furious shout | 7 (GO AWAY), 21 (GO—, mid-stop) |
| `milo_expr2_worried_fixed` | Worried / unsure | 2, 5, 8 |
| `milo_expr2_scowl_sideeye_fixed` | Grumpy, frustrated | 6, 13 |
| `milo_expr2_hopeful` | Hopeful | 19 |
| `milo_expr2_content_lookup` | Content, sheepish | 24, 25, 26 |
| Set 3 (below) | Full-body poses | everything else |

The old "wry half-smile" and "holding the NO" faces are **no longer needed**.

## Prompt 3: Set 3, full-body poses (v1.0)
v1.0 needs Milo's **body** more than new faces: lying on the rug, hugging his knees, looking at his hands. Run **one pose per prompt** (proven most consistent), on white, at full color. Fading and the glow are added in Canva.

**Template** (V7 path: `milo_front_LOCKED.png` or the "Milo Standing Neutral" image in **Omni Reference**, `STYLE_ANCHOR.png` in **Styles**). Replace `[POSE]`:
```
full body, the same small 7-year-old boy, [POSE], pale golden blond curtain haircut with short clipped sides, soft shaggy wavy hair on top parted down the middle, light freckles, big expressive eyes with clear whites and black pupils, thick expressive eyebrows, plain light blue t-shirt, blue jeans, blue sneakers, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, red hair, ginger hair, spiky hair, long hair, glow, glowing, light rays, transparency, ghost, signature, hatching, cross-hatching, vector, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines, background scenery
```

| # | `[POSE]` | Pages | Priority |
|---|---|---|---|
| 3a | `sitting on a small wooden bench in three-quarter view, both hands raised forward playing piano keys, happy concentrated smile` | 1, 26, 28 | High |
| 3b | `jumping to shoot a basketball, arms up, eyes on the hoop, determined` | 4, 5, 24 | High |
| 3c | `standing alone with arms hanging limp at his sides, shoulders slumped, looking down` | 9 | Medium |
| 3d | `sitting on the ground hugging his knees to his chest, chin on his knees, sad and lonely, eyes looking down` | 10 | **Critical** |
| 3e | `kneeling on the floor reaching one arm forward and low, under something, frowning` | 12, 13 | Medium |
| 3f | `kneeling, half turned away, looking back over his shoulder with a soft worried, thoughtful face` | 14 | High |
| 3g | `lying flat on his stomach on the floor, cheek resting on his folded hands, calm gentle eyes, very still and patient` | 15, 16, 17 | **Critical** |
| 3h | `sitting cross-legged, holding one open hand up in front of his face, studying it with a curious, wondering expression` | 18, 20 (standing variant: `standing, looking down at both open hands`) | **Critical** |
| 3i | `standing, eyes gently closed, cheeks puffed out, slowly letting out a big breath, shoulders relaxing` | 22 | High |
| 3j | `sitting on the ground with his legs stretched out, leaning back on his hands, calm` | 23 | Low |

**Pose-specific watch-outs:**
- **3g (lying down):** Midjourney often turns this into a sleeping pose. If the eyes close, add `eyes open` at the front and `sleeping` to `--no`.
- **3d and 3h** carry the book's meaning. Re-roll until the face is gentle and sad or curious, never angry.
- Keep the camera at Milo's eye level on 3d and 3g, so the reader is "down there with him."

## Acceptance checklist
- ☐ Hair: **blond**, **short clipped sides and back** with ears showing; **shaggy wavy top parted down the middle**; wavy bangs to either side. Not long, not a quiff, not a bowl cut.
- ☐ **Small**: about 3.5 heads tall; reads as a little 7-year-old, not a lanky tween.
- ☐ Outfit is **all blue**: light-blue tee, jeans, sneakers. No logos or stripes.
- ☐ Reads as about **7**, not a toddler and not a tween.
- ☐ Face is expressive in the comic way: big mouth shapes, readable eyebrows.
- ☐ Line and watercolor match the style anchor.
- ☐ **Does not look like Alex** beyond energy, hairstyle, and expression (story bible P1).

## Lock record
| Asset | File | Prompt / version / job URL | Approved |
|---|---|---|---|
| Turnaround | `milo_turnaround_LOCKED.png` | Prompt 1 (as above, `--sref` via Styles box, `--sw 60`); V8.2; https://cdn.midjourney.com/0a2b04ed-3069-4f16-9417-93be82f266a8/0_0.png | ✅ Daimon 2026-10-04 |
| Front (cropped from turnaround) | `milo_front_LOCKED.png` | cropped from turnaround | ✅ |
| Three-quarter (cropped) | `milo_threequarter_LOCKED.png` | cropped from turnaround | ✅ |
| Expressions set 1 | `milo_expressions_set1_LOCKED.png` | Prompt 2, V7 + Omni Reference (milo_front) + Styles (anchor), `--sw 60`; https://cdn.midjourney.com/089680b2-212f-460b-a946-18329799d49f/0_0.png | ✅ Daimon 2026-10-04 (see review) |
| Expressions set 2 (4 singles) | `milo_expr2_hopeful.png`, `milo_expr2_content_lookup.png`, `milo_expr2_scowl_sideeye.png`, `milo_expr2_worried.png` | Prompt 2b revised (Test Log R-001 to R-004), V7 + Omni (Milo Standing Neutral, `--ow 100`) + Styles (anchor, `--sw 60`); job URLs pending | ✅ Daimon 2026-10-05; scowl and worried use the `_fixed` black-pupil versions |
| Set 3 poses (3a–3j) | `milo_pose_3a_LOCKED.png` … | Prompt 3 template, one pose per run | ☐ |
| `--oref` URL | | | |
