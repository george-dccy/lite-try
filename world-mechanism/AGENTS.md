# AGENTS.md — World Mechanism Story Engine

This repository is designed to be produced primarily by **Codex / coding agents**.

The project is not a prompt collection and not a generative-video workflow. The default production method is:

> **understand → design → compile → code → render → inspect → revise**

not:

> write prompt → send whole scene to a video model → accept whatever returns.

## 1. Source-of-truth hierarchy

When instructions conflict, prefer in this order:

1. Human-approved `Must Preserve` / explicit creator feedback
2. Approved `Content Master`
3. Approved `Video Concept`
4. Approved `Director Proposal`
5. `Production Manifest` / `Motion Plan`
6. Renderer / art-style implementation convenience
7. Current model/tool capability

Production tools may change expression. They may not silently rewrite the mechanism.

## 2. Default video engine: art-motion

For video work, always evaluate `renderers/art-motion/` first.

Its upstream engine is pinned at:

`third_party/huashu-art-motion`

The engine contains reusable art styles, animation grammars, long-scroll mechanics, camera systems, compositing, transitions and QA.

### Style selection is content-driven, deliberate, not maximal

The project has **no universal house style** that every production should inherit.

Read `docs/style-routing-principle.md` before locking a visual direction.

A production may use:

- **one style for the entire film**;
- **one style per major section**;
- **different styles for simultaneously existing worlds**;
- **a short multi-style speedrun**;
- **realistic / photographic treatment**;
- **collage / archive / whiteboard / diagrammatic / UI-led treatment**;
- **Chinese ink or another culturally grounded visual language**;
- or a hybrid of art-motion code and generated character/image/video assets.

Never inherit a previous production's style merely because that pipeline already works.

Never use every available style merely because it exists.

For every chosen style, be able to answer:

> What cognitive, spatial, temporal, dramatic or emotional job does this style perform for this specific content?

If there is no answer, remove the style switch or choose a simpler visual system.

Before inventing a renderer from scratch, inspect:

- `third_party/huashu-art-motion/references/风格配方/INDEX.md`
- `third_party/huashu-art-motion/references/09-视频动画语法.md`
- the nearest style/grammar card
- existing demos / clips / long-scroll skeleton

Then adapt rather than rebuilding common animation infrastructure.

## 3. Codex-first production policy

### Primary method

Codex should own the production graph:

- scene code;
- Canvas / SVG / DOM / compositing logic;
- camera movement;
- timing;
- transitions;
- typography;
- multi-window systems;
- long-scroll systems;
- image/sprite compositing;
- audio timing and FFmpeg assembly;
- deterministic rendering;
- QA scripts;
- regression fixes.

### Image generation is an asset source

Image generation may create:

- character keyframes / sprites;
- difficult organic subjects;
- textures;
- background plates;
- visual references.

Generated assets should be placed under the production asset tree and then controlled by code.

### Generative video models are secondary, not the backbone

Tools such as MiniMax H3 or other text/image-to-video models may be used only when a shot genuinely benefits from non-programmatic organic motion that would be disproportionately expensive to code.

They are **not** the default method for:

- the whole film;
- scene continuity;
- camera grammar;
- timing-critical explanation;
- repeatable transitions;
- typography / UI / diagrams;
- multi-window logic;
- long-scroll logic;
- shots that must be frame-accurate or deterministic.

If a generative-video clip is used:

1. explain why code/compositing is inferior for this shot;
2. isolate it as a replaceable asset;
3. record prompt/model/settings/source in the production manifest;
4. trim and integrate it through the code/edit pipeline;
5. do not let its visual accidents rewrite upstream creative decisions.

## 4. Creative-to-production continuation

A video project should not stop when a creative candidate is generated.

When an Editorial / Creative Gate marks a candidate **KEEP** and the chosen medium includes video, continue through the production state machine unless a hard human gate is reached.

Default continuation:

```text
KEEP candidate
→ Creative Blueprint
→ Research Pass B if needed
→ Content Master
→ Video Concept
→ Director Proposal
→ Production Manifest
→ Style / Grammar Routing
→ Motion Plan
→ Keyframe Gate
→ Motion Prototype Gate
→ Narration / word timing
→ Rough Cut
→ QA + independent review
→ Revision loop
→ Release Candidate
→ Human Release Gate
→ Final + Retrospective
```

Do not stop after Video Concept or Director Proposal merely to ask what to do next when the next artifact is mechanically derivable.

## 5. Hard human gates

Default automation may continue until one of these gates genuinely needs creator judgment:

### Creative Gate
Which candidate is KEEP / HOLD / REJECT?

### Direction Gate
When there are materially different visual directions, present 2–3 strong directions / keyframes. Do not render a full film before direction selection.

### Prototype Gate
For a new production mechanism, test the smallest clips that validate it before full-film implementation.

### Release Gate
The creator approves the final release candidate.

Do not invent additional approval gates for routine implementation decisions.

## 6. Production Manifest is the state machine

Every video production should have:

`productions/<id>/production.yaml`

It records:

- current stage;
- source artifacts;
- locked decisions;
- selected art-motion styles / grammars;
- renderer strategy;
- Codex tasks;
- generated assets and provenance;
- optional video-model assets and justification;
- prototype results;
- render candidates;
- QA status;
- next actions.

Update it whenever a production passes a gate.

The manifest exists so another Codex session can resume without reconstructing the conversation.

## 7. Build in vertical slices

Do not build the whole film before proving the hard mechanisms.

Preferred order:

1. keyframe / look test;
2. one hard motion prototype;
3. one transition prototype;
4. one representative audio section;
5. rough end-to-end skeleton;
6. polish by sequence.

For multi-style productions, test style compatibility in the same frame/window system before producing many scenes.

## 8. Code architecture rules

Prefer reusable production primitives over one-off hacks:

- shared timeline/cue helpers;
- camera abstraction;
- scene interface;
- transition registry;
- style adapters;
- sprite / generated-frame loader;
- sound cue map;
- subtitle safe-zone overlay;
- deterministic random seed;
- frame capture / compare helpers.

If an upstream huashu component nearly fits, wrap or extend it. Do not fork large blocks unnecessarily.

Keep project-specific creative logic in `productions/<id>/` and reusable production capability in `renderers/art-motion/` or shared engine code.

## 9. Rendering and QA

Before calling a video done:

- render deterministic test frames;
- inspect key timestamps;
- render representative clips;
- run upstream QA where applicable;
- inspect subtitle safe zones;
- verify no clipped text / limbs / important action;
- verify transitions at actual frame boundaries;
- listen to the sound argument separately from the picture;
- have an independent reviewer / agent watch the output without implementation context;
- log timecode → symptom → root cause → change → recheck.

A high QA score is not the goal. Fix the actual viewing problem.

## 10. When resuming an existing production

Read, in order:

1. `productions/<id>/production.yaml`
2. linked Content Master
3. linked Video Concept
4. linked Director Proposal
5. current Motion Plan
6. latest retrospective / QA log
7. only then inspect scene code

Resume from `next_actions` in the manifest.

Do not restart creative exploration unless a logged upstream failure explicitly requires it.
