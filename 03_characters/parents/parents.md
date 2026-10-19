# Mom (and retired Dad): Character Reference

**Source of truth:** story bible §3.5 (v1.0). **Dad is retired** in v1.0; his design and prompts are kept below for reference only. **Mom** appears on pp. 3 (offscreen voice), 11 (vacuuming) and 26–28 (the PS). She is the book's sturdy presence: she sits, stays, hugs, and says only the refrain.

## Locked design (2026-10-04)
- **Build:** lean, like the kids, but with **more realistic adult head-to-body proportions** (about six heads tall instead of the kids' 3.5).
- **Height:** about **2× Milo's height**.
- **Eyes:** big expressive eyes with **black pupils** (house rule for all characters).
- **Dad:** brown hair with gray highlights, light stubble, blue button-down shirt, jeans.
- **Mom:** brown hair in a ponytail, big eyes, purple sweater set, black capris.

## Locked descriptions (paste-ready prompt fragments)
**Dad**
```
lean friendly father, more realistic adult proportions about six heads tall, short brown hair with gray highlights, light stubble on his jaw, kind smile, big expressive eyes with clear whites and black pupils, blue button-down shirt with sleeves rolled up, jeans
```
**Mom**
```
lean friendly mother, more realistic adult proportions about six heads tall, brown hair pulled back in a ponytail, big expressive eyes with clear whites and black pupils, warm smile, purple sweater set with a cardigan over a matching top, black capri pants
```

## Prompt 1: Dad turnaround (RETIRED, not used)
```
character turnaround sheet for a children's picture book, lean friendly father shown three times standing side by side: front view, three-quarter view, side view, full body, more realistic adult proportions about six heads tall, short brown hair with gray highlights, light stubble on his jaw, kind smile, big expressive eyes with clear whites and black pupils, blue button-down shirt with sleeves rolled up, jeans, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white paper background --ar 3:2 --sref <SREF> --sw 60 --stylize 100 --no blue eyes, colored irises, heavy beard, muscular, chubby, hatching, cross-hatching, vector, anime, text, letters, words, signature, speech bubbles, captions, border, frame, panel lines, background scenery
```

## Prompt 2: Mom turnaround
```
character turnaround sheet for a children's picture book, lean friendly mother shown three times standing side by side: front view, three-quarter view, side view, full body, more realistic adult proportions about six heads tall, brown hair pulled back in a ponytail, big expressive eyes with clear whites and black pupils, warm smile, purple sweater set with a cardigan over a matching top, black capri pants, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white paper background --ar 3:2 --sref <SREF> --sw 60 --stylize 100 --no blue eyes, colored irises, loose hair, chubby, hatching, cross-hatching, vector, anime, text, letters, words, signature, speech bubbles, captions, border, frame, panel lines, background scenery
```

## Mom page poses (v1.0)
Run after `mom_turnaround_LOCKED.png` exists. One pose per prompt; Mom's front view in **Omni Reference**, `STYLE_ANCHOR.png` in **Styles**. Replace `[POSE]`:
```
full body, the same lean friendly mother, [POSE], brown hair pulled back in a ponytail, big expressive eyes with clear whites and black pupils, purple sweater set with a cardigan, black capri pants, classic newspaper comic strip style, hand-inked light lively brush lines, soft, pale, muted, calm transparent watercolor, plain white background, no other characters --ar 1:1 --sw 60 --ow 100 --v 7 --no blue eyes, colored irises, loose hair, glow, glowing, transparency, ghost, hatching, cross-hatching, vector, anime, text, letters, words, signature, speech bubbles, captions, border, frame, panel lines, background scenery
```

| # | `[POSE]` | Pages | Priority |
|---|---|---|---|
| 1 | `pushing an upright vacuum cleaner, cheerful, unaware, seen from the side` | 11 (small, in the background) | Medium |
| 2 | `sitting sideways on a low bench, hands resting in her lap, turned slightly toward someone beside her, quietly listening, soft warm face` | 26 | **Critical** |
| 3 | Hug with Milo: see **Hug test** below | 27 | **Critical** |
| 4 | `sitting on a low bench, head tilted down and to the side as if resting her cheek on a child's head, eyes closed, peaceful` | 28 | High |

**Mom must never look stern, worried, or "about to talk."** Pose #2 is the whole of Kennedy's sturdy presence in one image: close, calm, quiet.

### Hug test (p. 27; bible §9 item 2)
Omni Reference holds only one character per image, so try in this order:
1. **V8 Edit path:** drop `mom_front_LOCKED.png` and `milo_front_LOCKED.png` in as reference images and `STYLE_ANCHOR.png` in **Styles**. Prompt: `the mother from the first reference image sitting on a low bench and hugging the small boy from the second reference image, his face pressed against her purple sweater, her eyes closed, warm and calm, [style fragment]`.
2. **Composite fallback:** generate Mom with arms in an open hugging shape (`arms wrapped around as if holding a child`) and Milo leaning in with his face turned away (`leaning forward, face hidden, arms reaching around someone`), then overlap them in Canva with Mom's arms on top.
Log both attempts in the Test Log; whichever wins becomes the method for p. 28.

## Acceptance checklist
- ☐ **Lean** builds, matching the kids' slim style, but with **adult proportions** (not big-headed like the kids).
- ☐ About **2× Milo's height** (check in the size lineup).
- ☐ **Black pupils**, big expressive eyes.
- ☐ Dad: brown hair with **gray highlights**, **light stubble** (not a full beard), blue button-down, jeans.
- ☐ Mom: brown **ponytail**, **purple sweater set**, **black capris**.
- ☐ Read as the boys' parents. The boys' blond hair can be read as coming from lighter childhood hair, which is common.
- ☐ Matches the style anchor.

## Lock record
| Asset | File | Prompt / version / job URL | Approved |
|---|---|---|---|
| ~~Dad turnaround~~ | retired | | — |
| Mom turnaround | `mom_turnaround_LOCKED.png` | | ☐ |
| Mom poses #1, #2, #4 | `mom_pose_N_LOCKED.png` | | ☐ |
| Hug (p. 27) | `mom_milo_hug_LOCKED.png` | | ☐ |
