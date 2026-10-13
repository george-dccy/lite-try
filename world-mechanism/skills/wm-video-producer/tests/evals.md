# wm-video-producer Evals

## Eval 1 — One-style film is valid

Input:
- approved Content Master;
- quiet philosophical explainer;
- one coherent visual world is strongest.

Expected:
- inspect art-motion catalog;
- select `single_style` if appropriate;
- do **not** force multiple styles;
- initialize Production Manifest;
- continue to Motion Plan / lookdev.

Failure:
- “art-motion has 35 styles, therefore use many of them.”

## Eval 2 — Multi-style only when structurally meaningful

Input:
- several simultaneous alternate worlds are part of the thesis.

Expected:
- `parallel_world_styles` may be selected;
- each style has explicit cognitive/spatial rationale;
- shared window / timestamp / camera system preserves film unity.

Failure:
- showreel-like style switching with no narrative reason.

## Eval 3 — Codex-first, not whole-film video generation

Input:
- 120-second explainer with UI, typography, split screens, exact narration timing and recurring character assets.

Expected:
- code/compositing owns timeline, layout, camera, transitions, UI and render;
- image generation may supply character sprites;
- no end-to-end MiniMax H3 / text-to-video backbone.

Failure:
- produce a list of 12 video-model prompts as the primary production plan.

## Eval 4 — Local generative-video exception

Input:
- one 3-second organic cloth/water transformation is central and expensive to reproduce convincingly in code.

Expected:
- generative-video clip may be proposed as a bounded optional asset;
- record why code is inferior, provider/model/settings, in/out boundary and replacement plan;
- integrate through the main code/edit pipeline.

Failure:
- expand the exception into the default method for adjacent scenes.

## Eval 5 — Creative KEEP auto-continues

Input:
- Creative Director returns KEEP;
- video is the selected medium;
- Blueprint and Content Master are available.

Expected:
- continue to Video Concept;
- continue to Director Proposal;
- initialize `production.yaml`;
- route art-motion;
- create Motion Plan / next actions;
- stop only at a real human gate or execution boundary.

Failure:
- end with “we can make the video next if you want.”

## Eval 6 — Resume after chat loss

Input:
- existing production directory with `production.yaml`, Motion Plan and latest QA log;
- no prior conversation context.

Expected:
- read manifest first;
- load linked upstream artifacts;
- execute `codex.next_actions`;
- preserve locked decisions.

Failure:
- restart creative exploration or ask the creator to restate the project.

## Eval 7 — Prototype before scale

Input:
- film depends on a novel recursive split-screen mechanic.

Expected:
- build the smallest representative prototype first;
- pass/fail Prototype Gate;
- only then implement across whole film.

Failure:
- build 2 minutes of scene code before testing the core mechanic.
