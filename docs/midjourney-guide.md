# Midjourney Quick-Start for This Book

For a first-time user. Everything happens on the **website** (midjourney.com). You don't need Discord, even though older tutorials use it. Midjourney changes its interface often, so if a button has moved, the concept will still be the same.

---

## Part 1: Account and plan (≈10 min)

1. **Go to** [midjourney.com](https://www.midjourney.com) and click **Sign Up / Log In**. Use your Google account; it's the simplest option.
2. **Subscribe.** There is **no free trial**. Plans as of 2026:

   | Plan | Monthly | Fast GPU time | Relax mode (unlimited, slower) | Stealth (private images) |
   |---|---|---|---|---|
   | Basic | $10 | 3.3 hrs | No | No |
   | **Standard** | **$30** | 15 hrs | **Yes** | No |
   | Pro | $60 | 30 hrs | Yes | Yes |

   **Recommendation: Standard, monthly, for 1–2 months, then cancel.** This book needs a few hundred generations once you count re-rolls. Basic might run out mid-project, while Standard's Relax mode is unlimited (each job just waits a little longer).

3. **Privacy note:** on Basic and Standard, your images are visible in Midjourney's public gallery. These are invented cartoon characters, so that's fine. **Never upload real photos of Alex or the family** as references; describe in words instead. If you want images to be private, that requires Pro.

---

## Part 2: The screen (the parts you'll use)

| Area | Where | What it does |
|---|---|---|
| **Create** page | left menu | Where you generate. Your results stream in below. |
| **Imagine bar** | top of Create | Type or paste the prompt and press Enter. |
| **Image icon** | left end of the Imagine bar | Opens your uploads. You drag images from here into reference slots. |
| **Settings icon** (sliders) | right end of the Imagine bar | Version, aspect ratio, stylize, Raw mode, Fast/Relax. |
| **Organize** page | left menu | All your images. Filter, select, and download from here. |

**Useful shortcut:** **Ctrl + Enter** (Cmd + Enter on a Mac) submits the prompt but **keeps the text** in the bar, so you can tweak it and re-run.

---

## Part 3: Your first run, the style anchor (≈20–30 min)

1. Open `03_characters/style-anchor/style-anchor.md` and copy **Prompt A** (everything inside the code block).
2. Paste it into the **Imagine bar** and press **Enter**.
3. You get **4 images** in about a minute. Hover over one to see the buttons:
   - **Vary (Subtle / Strong):** 4 new versions close to that image. Use this when you like it but want options.
   - **Upscale:** higher-resolution version. Do this for any keeper.
   - **Rerun:** a fresh set of 4 from the same prompt.
4. Repeat until **one** image captures the feel. Expect 5–15 rounds; that's normal.
5. **Save the winner:** upscale it, then click into it and **Download**. Rename it `STYLE_ANCHOR.png` and put it in `03_characters/style-anchor/` (or attach it in this chat).

---

## Part 4: Using references (this is how consistency works)

Our prompt files contain placeholders like `--sref <SREF>` and `--oref <MILO_OREF>`. On the website you **don't need to type URLs**. You drag images into slots instead.

1. Click the **image icon** in the Imagine bar and upload your saved image (e.g., `STYLE_ANCHOR.png`). It now sits in your uploads library.
2. **Drag** it into the Imagine bar. You'll see drop zones such as:
   - **Image Prompt:** uses the picture's content as a starting point. *We rarely use this.*
   - **Style Reference:** copies the *look* (line, wash, palette). **The style anchor always goes here.**
   - **Omni Reference** (V7) or **Edit / reference images** (V8): copies a *character*. **Locked character sheets go here.**
3. **Delete the placeholder text** (`--sref <SREF>`, `--oref <...>`, `--ow 100`) from the pasted prompt, since the slot replaces it. Keep everything else, including `--ar`, `--stylize`, `--no ...` and `--v 7` where shown.
4. **Version switching:** our prompts mark which ones need `--v 7` (those using Omni Reference). For everything else, leave the default (V8.2). You can also switch versions in **Settings**.

**If V7 + Omni Reference drifts** (Milo's hair changes, etc.), try the V8 path instead. Put the character sheet in the **Edit / reference** slot (up to 4 images) and write the prompt as an instruction, e.g. *"Draw this exact boy, shown in the reference, leaping across couch cushions..."*

---

## Part 5: Settings worth knowing

| Setting | Our default | When to change |
|---|---|---|
| Version | V8.2 (V7 for Omni Reference prompts) | — |
| Aspect ratio | Set by `--ar` in the prompt | — |
| Stylize | 100–150 | Lower (50) if images look too glossy or "AI"; higher if too plain |
| Raw mode | Off | **Turn on** if Midjourney keeps adding its own flourishes |
| Speed | Fast | Switch to **Relax** if fast hours run low (Standard plan) |

---

## Part 6: Review loop with me

1. Generate and pick your 1–2 favorite candidates per asset.
2. Download, name them per the convention (e.g. `milo_turnaround_cand1.png`), and **attach them in this chat**. Or commit them to the character's folder.
3. I review each against the checklist in the character file and suggest prompt tweaks for any misses.
4. You approve. I rename to `_LOCKED`, fill in the lock record, and commit.

## Common first-timer problems

| Problem | Fix |
|---|---|
| Random letters or gibberish text appear | Already in our `--no` list. If it persists, add `--raw` and reroll; small stray marks can be erased in Canva. |
| Too much background, not enough white | Add "vignette fading to white paper, unpainted edges" |
| Character looks too old or young | Add "small child", or the age, earlier in the prompt |
| Three views of the character look like different kids | Normal for turnarounds. Pick the best single view and use it as the reference, then regenerate the others from it. |
| Hands or fingers look odd | Reroll, or Vary (Subtle). Watercolor style hides a lot of this. |
