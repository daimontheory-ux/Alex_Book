# Milo: Character Reference

**Source of truth:** story bible §3.2. Replace `<SREF>` with the style anchor URL and `<MILO_OREF>` with the locked turnaround URL once it exists.

## Locked description (paste-ready prompt fragment)
```
7-year-old boy, full voluminous blond hair in a messy middle-part curtain cut, long wavy locks drawn in flowing clumps of curved brush strokes falling to each side of his face, big expressive eyes, expressive eyebrows, big elastic mouth, plain light blue t-shirt, blue jeans, blue sneakers
```

## Prompt 1: Turnaround
```
character turnaround sheet for a children's picture book, classic newspaper comic strip style, large head with cartoon proportions about four heads tall, soft wide oval head, big expressive eyes with dark pupils, hand-inked with a fine sable brush, lively fluid lines that swell and taper, 7-year-old boy shown three times standing side by side: front view, three-quarter view, side view, full body, full voluminous blond hair in a messy middle-part curtain cut, long wavy locks drawn in flowing clumps of curved brush strokes falling to each side of his face, wide happy grin, plain light blue t-shirt, blue jeans, blue sneakers, calm delicate transparent watercolor, plain white paper background --ar 3:2 --sref <SREF> --stylize 100 --no hatching, cross-hatching, perfectly round ball-shaped head, dot eyes, stick-like hair, vector, realistic proportions, anime, text, letters, words, speech bubbles, captions, signature, border, frame, panel lines, background scenery
```

## Prompt 2: Expression sheet
Milo's expressions are the emotional engine of the book. Each one maps to specific pages.

```
expression sheet for a children's picture book character, the same 7-year-old boy shown six times, head and shoulders: (1) huge open-mouth joyful grin, (2) furious shouting with scrunched eyes and clenched fists, (3) frozen wide-eyed surprise, (4) narrowed eyes and tongue poking out in concentration, (5) sheepish embarrassed small smile, (6) wry knowing half-smile, full voluminous blond messy middle-part curtain hair with long wavy locks in flowing brush-stroke clumps, light blue t-shirt, hand-inked with a fine sable brush, lively fluid lines that swell and taper, calm delicate transparent watercolor, plain white background --ar 3:2 --sref <SREF> --oref <MILO_OREF> --ow 100 --v 7 --no hatching, cross-hatching, perfectly round ball-shaped head, dot eyes, stick-like hair, vector, realistic proportions, anime, text, letters, words, numbers, speech bubbles, captions, border, frame, panel lines
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

**Note:** Midjourney may draw the numbers into the image even with `--no numbers`. If it does, drop the "(1)…(6)" markers and list the expressions in plain commas.

## Acceptance checklist
- ☐ Hair is clearly **blond**, **middle part**, **long wavy locks** framing the face (not a bowl cut, not short).
- ☐ Outfit is **all blue**: light-blue tee, jeans, sneakers. No logos or stripes.
- ☐ Reads as about **7**, not a toddler and not a tween.
- ☐ Face is expressive in the comic way: big mouth shapes, readable eyebrows.
- ☐ Line and watercolor match the style anchor.
- ☐ **Does not look like Alex** beyond energy, hairstyle, and expression (story bible P1).

## Lock record
| Asset | File | Prompt / version / job URL | Approved |
|---|---|---|---|
| Turnaround | `milo_turnaround_LOCKED.png` | | ☐ |
| Front (cropped from turnaround) | `milo_front_LOCKED.png` | | ☐ |
| Expression sheet | `milo_expressions_LOCKED.png` | | ☐ |
| `--oref` URL | | | |
