---
name: wm-video-producer
description: Use after an approved creative direction / Content Master exists and the target medium includes video. Continue the project through Video Concept, Director Proposal, art-motion routing, production manifest, motion prototypes, narration timing, rough cut, QA and release candidate. Codex-first; generative video models are optional assets, not the default production engine.
---

# World Mechanism Video Producer

## Mission

Do not stop at “good idea”.

Turn an approved idea into a **resumable, coded, testable video production** while preserving the upstream mechanism and authorial decisions.

The default implementation base is:

> `renderers/art-motion/` + `third_party/huashu-art-motion`

The default producer is:

> **Codex / coding agent**

not an end-to-end generative-video model.

---

## When to activate

Activate when all are true:

1. a candidate has been marked `KEEP` or an approved Content Master already exists;
2. video is the chosen or requested medium;
3. there is enough upstream context to identify Must Preserve.

Do not activate for HOLD / REJECT candidates.

If Content Master / Video Concept / Director Proposal is missing, create the next missing layer rather than stopping.

---

## Continuation contract

Default flow:

```text
KEEP
→ Creative Blueprint
→ Research Pass B if required
→ Content Master
→ Video Concept
→ Director Proposal
→ Production Manifest
→ art-motion Style / Grammar Routing
→ Motion Plan
→ Keyframe Direction Gate
→ Motion Prototype Gate
→ Narration / Word Timing if needed
→ End-to-end Rough Cut
→ QA / Independent Review
→ Revision Loop
→ Release Candidate
→ Human Release Gate
→ Retrospective
```

After completing one layer, continue to the next mechanically derivable layer in the same execution whenever possible.

Do not end with “next we could make a storyboard” if enough information exists to make it now.

---

## Step 1 — Read upstream locks

Read:

- Creative Blueprint;
- Evidence Pack if factual;
- Content Master;
- Must Preserve;
- creator feedback.

Write a short production lock list.

The production layer may compress wording, reorder shots and change styles. It may not silently change the thesis or world rules.

---

## Step 2 — Build / verify Video Concept

Video Concept must define:

- Core Cognitive Turn;
- Visual Argument;
- Temporal Device;
- Sound Argument;
- Beat Map;
- Must Preserve.

Ask:

> What can picture, motion and sound prove that narration should not need to explain?

Do not translate paragraphs one-to-one into illustrations.

---

## Step 3 — Build / verify Director Proposal

Turn the Video Concept into:

- protagonist / subject strategy;
- camera grammar;
- sound grammar;
- sequence map;
- asset strategy;
- production risks;
- Locked / Flexible.

Then initialize:

`productions/<id>/production.yaml`

using `engine/production-orchestrator/template-production.yaml`.

---

## Step 4 — Art-motion routing

Read the upstream art-motion catalog before choosing styles.

At minimum inspect:

- `references/风格配方/INDEX.md`
- `references/09-视频动画语法.md`
- relevant style cards;
- relevant demos / clips.

Then choose one style-count strategy:

### A. Single Style
One style throughout.

Best when the film needs a strong unified world.

### B. Sectional Styles
A few styles mapped to argument sections.

Best when form changes correspond to mental-model changes.

### C. Parallel World Styles
Different styles coexist simultaneously.

Best for alternative worlds, viewpoints or simultaneous realities.

### D. Speedrun Styles
Many styles over a deliberately short passage.

Best only when variation itself is meaningful.

### E. Hybrid Assets
Code-drawn world + generated character/image assets.

Often best for human-led films.

**The correct number of styles is 1..N, not “as many as possible”.**

For every selected style record:

- where it appears;
- what job it performs;
- why a simpler single-style treatment is insufficient.

---

## Step 5 — Codex-first asset and renderer plan

Default to code for:

- scene structure;
- camera;
- transitions;
- layout;
- typography;
- diagrams / UI;
- multi-window systems;
- long-scroll systems;
- timing;
- compositing;
- audio cue timing;
- render/export;
- QA.

Use generated still images / sprites when they improve:

- human identity;
- difficult organic forms;
- painterly character fidelity;
- textures / background plates.

The image becomes a controlled asset inside code.

### Generative video exception

A text/image-to-video model may generate a replaceable clip only if:

- the desired organic motion is genuinely hard to implement well with code + sprite/image assets;
- frame-perfect determinism is not central;
- the clip has clear in/out boundaries;
- continuity can be controlled in edit.

Record the reason and provenance in `production.yaml`.

Do not make a provider such as MiniMax H3 the default full-film renderer.

---

## Step 6 — Keyframe Direction Gate

Before full implementation, produce 2–3 materially different visual directions **only when direction is still genuinely open**.

Each direction should show the same representative moment so comparison is meaningful.

Judge:

- author fit;
- mechanism fit;
- character / world credibility;
- style function;
- production feasibility.

If the direction is already locked from a prior approved production or strong reference, skip redundant alternatives.

---

## Step 7 — Prototype Gate

Identify the 1–3 hardest or most novel motion ideas.

Prototype those first.

Examples:

- recursive split-screen;
- long-scroll world traversal;
- style morph transition;
- interactive-looking diagram;
- character sprite + camera composite;
- a sound-dependent reveal.

A prototype should be the smallest clip that can fail for the right reason.

If the prototype fails, do not scale it to the full film.

---

## Step 8 — Motion Plan

For every sequence / narration block write:

```yaml
start:
end:
spoken_text:
cognitive_job:
scene:
grammar:
style:
camera:
action:
transition:
audio_cue:
subtitle_safe_zone:
asset_dependencies:
```

If the film has narration, bind animation to word-level timestamps when timing matters.

Do not hardcode every cue before narration timing exists.

---

## Step 9 — Rough cut before polish

Build an end-to-end skeleton early.

Rough cut priorities:

1. cognitive sequence;
2. timing;
3. picture argument;
4. sound argument;
5. continuity;
6. only then visual polish.

Do not spend hours polishing a character hand before learning that the entire sequence is structurally unnecessary.

---

## Step 10 — QA and revision loop

Run applicable upstream QA and inspect actual frames.

Review separately:

### Mechanism QA
Did production preserve the intended cognitive turn?

### Motion QA
Does each scene move according to its grammar rather than merely zooming a still image?

### Style QA
Are style changes intentional and legible?

### Camera QA
Are framing, movement and safe zones correct through transitions?

### Audio QA
Can the sound structure be understood without relying on music to manufacture meaning?

### Continuity QA
Are recurring people / worlds / objects stable where stability matters?

### Independent review
A reviewer not involved in implementation watches the film first, then reports timecoded issues.

Log:

> timecode → symptom → root cause → change → recheck

---

## Step 11 — Resume protocol

If entering an existing production, read in this order:

1. `production.yaml`;
2. Content Master;
3. Video Concept;
4. Director Proposal;
5. Motion Plan;
6. latest QA log;
7. current code.

Then execute `codex.next_actions`.

Do not restart ideation unless the manifest records an upstream failure.

---

## Output contract

A completed production pass should leave some or all of:

1. `production.yaml`
2. Video Concept
3. Director Proposal
4. art-motion routing decision
5. Motion Plan
6. look-development frames
7. prototype clips
8. narration + word timestamps if applicable
9. rough cut
10. QA log
11. release candidate
12. retrospective

The key requirement is **continuation state**, not a one-off answer.

---

## Failure modes

- creative stops after candidate generation;
- storyboard stops without runnable production state;
- using many art styles merely to show capability;
- choosing style before understanding cognitive job;
- whole-film prompt-to-video dependence;
- letting video-model accidents rewrite the story;
- polishing before prototype validation;
- rebuilding animation infrastructure already present in art-motion;
- no manifest, so the next Codex session restarts from memory;
- asking the creator for routine decisions the production system can make itself.

---

## Completion test

- Can a new Codex session resume from files alone?
- Is art-motion evaluated and deliberately routed?
- Is the selected style count justified, whether one or many?
- Is code/compositing the backbone of the film?
- Are any generative-video clips optional, bounded and replaceable?
- Did the hard motion ideas pass prototypes before scaling?
- Is there an end-to-end rough cut before final polish?
- Did QA test the actual cognitive and viewing result, not just technical validity?
- Is final release still a human decision?
