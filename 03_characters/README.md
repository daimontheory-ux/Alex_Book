# Gate 4: Character Reference Sheets

**Status:** IN PROGRESS. Prompts drafted; awaiting generation.
**Goal:** one locked set of reference images per character. Every page prompt in Gate 6 reuses these, so the characters look the same on page 1 and page 28.

---

## The tool setup (Midjourney, as of Oct 2026)

Midjourney's current default model is **V8.2**. The two features that matter for this book work differently by version, so we use each where it's strongest:

| Need | Feature | Version | How we use it |
|---|---|---|---|
| Same **look and feel** on every image | **Style Reference** `--sref <url>` (+ `--sw` weight) | V7 and V8 | The approved style anchor image (Step 0) goes on **every** prompt. |
| Same **character** on every image | **Omni Reference** `--oref <url>` (+ `--ow` weight) | **V7 only** | Add `--v 7` to the prompt. One character reference per prompt. |
| Same character, V8 quality | **Edit model** with up to 4 reference images | V8.x | Alternative path. Try it if V7 + oref drifts. |

**Rule of thumb:** generate **style anchor and character sheets in V8.2** for the best quality. Then generate **page art in V7 with `--oref` + `--sref`**, or with V8's Edit model if that holds the characters better. Midjourney changes often, so the first test generations will tell us which path wins.

### The single biggest consistency trick: composite in Canva
The art is **mostly white paper**, so you rarely need the AI to put three kids in one image. For multi-character pages (pp. 20, 25, etc.), generate **each character separately on white**, using that character's `--oref`. Then arrange them in Canva. Watercolor edges on white blend almost seamlessly. One character per generation is also where Omni Reference is most reliable.

---

## Workflow

**New to Midjourney?** Start with `docs/midjourney-guide.md`.

### Step 0: Style anchor (do this first)
Prompts are in `style-anchor/style-anchor.md`. Generate, pick **one** image whose *feel* you love (line, wash, white space, palette), and save it as `style-anchor/STYLE_ANCHOR.png`. Upload it to Midjourney and keep its URL. That URL becomes `--sref` on every prompt that follows.

### Step 1: Character sheets
For each character file (`milo/milo.md` etc.):
1. Run the **turnaround** prompt (front, three-quarter, side). Re-roll until one set matches the spec.
2. Run the **expression sheet** prompt with the chosen turnaround as `--oref`.
3. Save picks using the naming below. Fill in the **Lock record** at the bottom of the character file.

### Step 2: Size lineup
Run the lineup prompt in `lineup/lineup.md` to confirm relative heights (Owen > Nia > Milo ≈ Diego). Composite it in Canva if needed.

### Step 3: Review and lock
Drop picks into the folder (or attach them in this chat). I'll review each against the checklist in its file, and you approve. Once a character is locked, **its reference images never change**.

---

## Conventions
- **File names:** `<character>_<view>_LOCKED.png` for approved refs (e.g. `milo_front_LOCKED.png`). Candidates under review use `_cand1`, `_cand2`. Delete rejected candidates; don't commit them.
- **Prompts never name a real artist or comic strip.** The style is described, not borrowed.
- **Every prompt ends with:** `--no text, letters, words, speech bubbles, captions, signature, border, frame, panel lines` (Midjourney sometimes invents lettering; we letter in Canva).
- **Aspect ratio:** `--ar 3:2` for turnaround and expression sheets (wide), `--ar 1:1` for single figures and all page art.
- **Record everything:** for each locked image, note the full prompt, model version, and Midjourney job URL in the character file's Lock record, so we can regenerate or extend later.

## Character checklist status

| Character | Turnaround | Expressions | Locked |
|---|---|---|---|
| Style anchor | — | — | ☐ |
| Milo | ☐ | ☐ | ☐ |
| Diego | ☐ | ☐ | ☐ |
| Nia | ☐ | ☐ | ☐ |
| Owen + B&W cat | ☐ | ☐ | ☐ |
| Boris | ☐ | ☐ | ☐ |
| Mom & Dad | ☐ | ☐ | ☐ |
| Size lineup | — | — | ☐ |
