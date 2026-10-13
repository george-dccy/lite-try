# Production Continuation Contract

## Trigger

Continue into video production when:

- candidate status = `KEEP`, or an approved Content Master exists;
- target medium includes video;
- Must Preserve can be identified.

## Mandatory continuation behavior

Do not stop at the first artifact below if its successor can be derived:

```text
Content Master
→ Video Concept
→ Director Proposal
→ Production Manifest
→ art-motion Routing
→ Motion Plan
→ Lookdev / Prototype
→ Timing
→ Rough Cut
→ QA / Revision
→ Release Candidate
```

## Default production mode

`codex_first`

This means the production graph is code-driven and deterministic where practical.

## art-motion evaluation requirement

Every new video production must evaluate the art-motion style and grammar library before locking its renderer strategy.

Evaluation does **not** require using multiple styles.

Valid outcomes include:
- one selected style;
- a few section styles;
- parallel-world styles;
- short controlled style speedrun;
- code world + generated image/sprite assets.

## Generative-video boundary

End-to-end generative video is not the default renderer.

Any generated-video clip must be:
- locally justified;
- bounded by explicit in/out points;
- replaceable;
- documented in `production.yaml`;
- integrated by the main code/edit pipeline.

## Resume guarantee

A production is not considered correctly initialized until a new Codex session can resume from:

`productions/<id>/production.yaml`

without access to the originating chat.
