# Milo: Character Reference

**Source of truth:** story bible §3.2. Put `STYLE_ANCHOR.png` in the Styles box (or replace `<SREF>` with its URL) and `<MILO_OREF>` with the locked turnaround URL once it exists.

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

| # | Expression | Used on |
|---|---|---|
| 1 | Joyful grin | pp. 1, 4, 24, 25, 26 |
| 2 | Furious NO shout | pp. 2, 6, 14 |
| 3 | Frozen, wide-eyed | pp. 7, 14, 27 |
| 4 | Concentrating "scientist" | pp. 10–12 |
| 5 | Sheepish | p. 3 |
| 6 | Wry half-smile | p. 28 |
| + | Eyes squeezed shut, cheeks puffed (holding the NO) | pp. 22–23 (generate separately if needed) |

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
| Expressions set 2 | `milo_expressions_set2_LOCKED.png` | Prompt 2b | ☐ |
| `--oref` URL | | | |
