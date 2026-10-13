# Production Orchestrator

Production Orchestrator solves one recurring failure mode:

> a strong creative direction is generated, then the system stops and waits for the creator to manually restart a separate video-production conversation.

This layer turns an approved creative direction into a resumable production state machine.

## Entry condition

Start only when:

- Editorial / Creative Gate says `KEEP`;
- the chosen expression includes video;
- upstream Must Preserve is available;
- no unresolved factual contradiction blocks production.

If the candidate is `HOLD` or `REJECT`, do not create a production.

## State machine

```text
creative_keep
  ↓
blueprint_ready
  ↓
content_master_ready
  ↓
video_concept_ready
  ↓
director_proposal_ready
  ↓
production_initialized
  ↓
style_routed
  ↓
motion_plan_ready
  ↓
keyframe_gate
  ↓
prototype_gate
  ↓
timing_ready
  ↓
rough_cut
  ↓
qa_review
  ↺ revision_loop
  ↓
release_candidate
  ↓
human_release_gate
  ↓
released
  ↓
retrospective
```

Not every production requires fresh research, narration, generated characters or multiple styles. The state machine describes possible stages, not mandatory busywork.

## Auto-continue principle

After a state is complete, produce the next mechanically derivable artifact in the same work session whenever possible.

Examples:

- approved Content Master + video target → draft Video Concept;
- approved Video Concept → draft Director Proposal;
- approved Director Proposal → initialize Production Manifest and style routing;
- selected visual direction → build Motion Plan and smallest required prototypes;
- accepted prototypes + narration → bind word timestamps and render rough cut;
- rough cut → QA / revision loop.

Do not ask the creator “what next?” when the answer is already encoded in the workflow.

## Where human judgment is required

### Gate A — Creative selection
Choose KEEP / HOLD / REJECT.

### Gate B — Material visual direction
If two directions imply meaningfully different films, show 2–3 keyframes / short tests.

### Gate C — New mechanism prototype
If a new technical idea is central to the film, prove it with the smallest clip before scaling.

### Gate D — Release
Human approves the release candidate.

Routine engineering decisions stay with Codex / the production agent.

## Art-motion routing

`renderers/art-motion` is the default video production base.

For each sequence classify the cognitive job, then choose:

1. animation grammar;
2. style count strategy;
3. art style(s);
4. camera grammar;
5. transition grammar;
6. asset strategy;
7. sound behavior.

### Style-count strategies

#### `single_style`
One visual language for the whole film.

Use when consistency and immersion matter more than contrast.

#### `sectional_styles`
A small number of styles mapped to major conceptual sections.

Use when the argument has distinct modes.

#### `parallel_world_styles`
Different styles coexist inside a shared window / world system.

Use when simultaneity or alternative realities are themselves meaningful.

#### `speedrun_styles`
Fast controlled style changes over a short sequence.

Use only when variation itself is the point.

#### `hybrid_assets`
A code-drawn world with generated image/character assets.

This is often the best default for human subjects.

The system must evaluate the upstream style library even when it finally chooses only one style.

## Codex-first build strategy

Codex is the primary producer because the project values:

- deterministic motion;
- precise timing;
- reusable systems;
- frame-level revision;
- consistent characters and layout;
- reproducible QA;
- the ability to resume production from code and manifests.

A generative-video model is an optional shot generator, not the production graph.

## Production directory contract

```text
productions/<id>/
├── production.yaml           # state machine / source of truth
├── 00-source/
├── 01-motion-plan.yaml
├── 02-lookdev/
├── 03-prototypes/
├── 04-assets/
│   ├── characters/
│   ├── generated-images/
│   ├── optional-video-clips/
│   └── audio/
├── 05-code/
├── 06-renders/
│   ├── stills/
│   ├── clips/
│   ├── rough-cuts/
│   └── release-candidates/
├── 07-qa/
└── retrospective.md
```

## Production Manifest lifecycle

Create from `template-production.yaml`.

At minimum update after:

- direction selected;
- style routing locked;
- prototype gate passed/failed;
- narration timing ready;
- each rough-cut review;
- release candidate produced;
- release approved.

A new Codex session should be able to continue from the manifest without access to the originating chat.

## Failure escalation

If a downstream problem survives two materially different fixes, classify it:

- `asset_failure` → regenerate/rebuild asset;
- `renderer_failure` → improve reusable engine capability;
- `motion_plan_failure` → change sequence design;
- `director_failure` → return to Director Proposal;
- `concept_failure` → return to Video Concept;
- `content_failure` → return to Content Master / Blueprint.

Do not keep polishing a downstream layer when the root cause is upstream.
