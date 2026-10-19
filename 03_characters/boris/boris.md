# Boris: Character Reference

**Source of truth:** story bible §3.4 (v1.0). The family's Russian Blue. In v1.0 he's no longer comic relief; he's **the mirror** for Milo in Episode 2 (pp. 11–18): scared of the vacuum, he fades, hides and hisses, and Milo learns to stay. He also bookends the book on the piano (pp. 1–3, 26–28).

## Locked description (paste-ready prompt fragment)
```
sleek Russian Blue cat, short dense silver blue-grey coat, bright green eyes, slender and elegant, expressive
```

## Prompt 1: Turnaround (unchanged)
```
character turnaround sheet for a children's picture book, a sleek Russian Blue cat shown three times: sitting front view, standing side view, sitting three-quarter view, short dense silver blue-grey coat, bright green eyes, slender and elegant, hand-inked with a fine sable brush, lively fluid lines that swell and taper, soft, pale, muted, calm transparent watercolor, plain white paper background --ar 3:2 --sref <SREF> --sw 60 --stylize 100 --no text, letters, words, collar, glow, glowing, transparency, ghost, speech bubbles, captions, border, frame, panel lines, background scenery
```

## Prompt 2: Action poses (v1.0)
Run **one pose per prompt** with the locked turnaround in **Omni Reference** and `STYLE_ANCHOR.png` in **Styles**. Replace `[POSE]`:
```
full body, the same sleek Russian Blue cat, [POSE], silver blue-grey coat, bright green eyes, hand-inked with a fine sable brush, lively fluid lines that swell and taper, soft, pale, muted, calm transparent watercolor, plain white background --ar 1:1 --sw 60 --ow 100 --v 7 --no text, letters, words, numbers, collar, glow, glowing, transparency, ghost, speech bubbles, captions, border, frame, panel lines, background scenery
```

| # | `[POSE]` | Pages | Priority |
|---|---|---|---|
| 1 | `startled, fur puffed up, back slightly arched, ears back, eyes huge and round` | 11 | High |
| 2 | `crouched flat and low, only the front half visible, peering forward with wide green eyes, ears back, trembling, as if hiding in a dark gap` | 12, 14, 15 | **Critical** |
| 3 | `mid-swat with one paw raised, ears flattened, mouth open in a hiss` | 13 | High |
| 4 | `creeping forward slowly and cautiously, low to the ground, one paw lifted` | 16 | High |
| 5 | `curled up contentedly, eyes closed, purring, relaxed` | 17, 18, 28 | High |
| 6 | `sitting tall and calm, tail hanging down, as if perched on top of a piano` | 1, 26 | Medium |
| 6b | `stepping forward and head-butting affectionately, eyes half-closed` | 3 | Medium |

**Watch-outs:**
- **#3 (the swat) must read as scared, not vicious.** Keep it small and defensive. If it looks attacking, add `frightened` at the front.
- **#2** is the book's key image of fear. The dark couch gap is a GIMP layer from the setting reference; Boris is composited into it.

## Acceptance checklist
- ☐ Unmistakably a **Russian Blue**: silver-blue (not grey-brown), **green** eyes, sleek build.
- ☐ Fear poses (#1–#4) read as **frightened**, never mean.
- ☐ No collar.
- ☐ Matches the style anchor.

## Lock record
| Asset | File | Prompt / version / job URL | Approved |
|---|---|---|---|
| Turnaround | `boris_turnaround_LOCKED.png` | | ☐ |
| Poses #1–#6b | `boris_pose_N_LOCKED.png` | | ☐ |
| `--oref` URL | | | |
