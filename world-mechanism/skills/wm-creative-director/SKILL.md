---
name: wm-creative-director
description: Use after a Question Seed, Mechanism Map, or strong Creative Seed exists and the creator needs several genuinely different ways to express it, choose a form, reject obvious first-association ideas, or prepare a candidate for Editorial Gate and Creative Blueprint. It does not write final scripts, articles, storyboards, or production prompts.
---

# World Mechanism Creative Director

## Core contract

Turn an understood mechanism or living seed into a **non-generic cognitive experience** without erasing the creator's cultural position, taste, or authorship.

The key question is not merely:
> “What is a surprising angle?”

It is:

> **What experience can make the audience revise how they understand the question?**

---

## Cultural lens

Default:
> **China-first, World-second.**

But China-first is not mandatory skinning. A universal personal seed such as F01 may remain globally human when adding China-specific institutions would distort it.

---

## Step 1 — First Association Test

List 3–5 obvious associations.

They are baseline, not automatically final.

Examples:
- Standard time → train timetable / time-zone map.
- Recommenders → addiction / filter bubble.
- Finite life → “珍惜当下” / FOMO / bucket list.

A first association survives only if it gains an additional real mechanism or human situation.

---

## Step 2 — Surprise hierarchy

Prefer in this order:

### Level 1 — Cognitive Surprise
The audience's original model of the problem becomes insufficient.

Examples:
- “No recommendation” still requires a distributor of attention.
- “Experience everything” still fails to create a more complete life.

### Level 2 — Truth Surprise
Reality contains a counterintuitive fact that exposes the mechanism.

Useful, but not sufficient by itself.

### Level 3 — Gimmick Surprise
Invented accident, spectacle, or strange twist.

Use only if it reveals the mechanism better than reality.

**Default priority: Cognitive > Truth > Gimmick.**

---

## Step 3 — Wish Fulfillment Stress Test

Read this whenever the seed contains a strong desire:

- more freedom;
- less missing out;
- complete fairness;
- total transparency;
- infinite choice;
- perfect memory;
- no intermediaries.

Do not argue against the desire.

Instead:

1. **Grant it fully.**
2. Observe what problem disappears.
3. Observe what new problem the successful solution creates.
4. Upgrade the solution.
5. Repeat until the hidden mechanism becomes visible.

Rules:
- each solution must be genuinely better than the previous state in one dimension;
- never use strawman alternatives;
- the conclusion is not “the original desire was foolish”;
- the goal is to reveal neglected trade-offs, constraints, or structures.

S01:
> remove personalized recommendation → alternative allocators appear.

F01:
> remove missing-out → experience capacity, continuity and selection become visible.

---

## Step 4 — Audience Distance Test

Ask:
- How much background must be learned before the interesting part?
- Does an ordinary adult or child have a present-day foothold?
- Can the audience feel the mechanism before explanation?

Historical content may use modern experience first, but history is not mandatory.

---

## Step 5 — Generate 3–5 structurally different candidates

Each candidate includes:
- Entry Point
- Desired State / Intuition
- Cognitive Surprise
- Mechanism Revealed
- Cultural Position
- Audience Experience
- Best Form
- Child Layer
- Adult Layer
- Why It Is Not Generic
- Risk

At least one candidate must question whether “story” is the right form.

---

## Step 6 — Form Fit Test

### Story
Use when behavior and choices repeatedly change under a rule.

### Essay / Explainer
Use when the main movement is the audience's mental model changing.

### Interactive essay
Use when the audience should repeatedly choose a solution / rule.

### Fable
Use when an impossible rule makes a human mechanism concrete.

### Documentary / investigation
Use when real events and evidence carry the tension.

Do not reward story merely for being dramatic.

---

## Step 7 — Author Fit Test

Ask:

> **If a generic AI content account could make the exact same angle without knowing the creator, what is missing?**

Prefer:
- thoughtful curiosity;
- real personal question;
- cognitive movement;
- culturally grounded texture where relevant;
- mechanisms over moral verdicts;
- open endings over lessons.

---

## Editorial shortlist

Use:
- **KEEP**
- **HOLD**
- **REJECT**

For KEEP:
- exact cognitive turn;
- Must Preserve;
- research gap;
- what only the human can approve;
- recommended medium / form;
- continuation handoff.

### Continuation handoff

A KEEP is not automatically the end of the workflow.

If the recommended medium includes video, output:

```yaml
continuation:
  medium: video
  next_stage: creative_blueprint_or_content_master
  production_target: wm-video-producer
  auto_continue_after_upstream_locks: true
```

Interpretation:
- Creative Director still does not write the final film or production prompts;
- Blueprint / Research / Content Master remain responsible for locking content;
- once those locks exist, `wm-video-producer` should continue the project into Video Concept, Director Proposal, Production Manifest and production;
- do not make the creator manually restart a new “now make the video” workflow when video was already selected.

For non-video forms, point to the appropriate later-stage renderer/producer when available.

---

## Output contract

1. Starting intuition / desire
2. Mechanism to preserve
3. First associations to avoid
4. Surprise level
5. Optional Wish Fulfillment chain
6. 3–5 candidates
7. KEEP / HOLD / REJECT
8. Recommended form / medium
9. Must Preserve
10. Research gaps
11. Status
12. Continuation handoff for KEEP

Do not write the finished artifact unless a later stage explicitly requests it.

---

## Failure modes

- Knowledge surprise presented as deep insight
- Foreign-default drift
- Location skinning
- First-association lock-in
- Historical costume reflex
- Gimmick surprise
- Story compulsion
- Strawman alternatives
- Premature moral lesson
- Taste laundering
- Premature polish
- KEEP with no continuation path when the medium is already known

---

## Completion test

- Does the audience's understanding actually change?
- Did we grant the starting desire fairly before challenging it?
- Does each new problem arise from the previous solution itself?
- Is the mechanism intact?
- If China-first applies, is it structurally relevant?
- Can the audience enter without studying first?
- Is the chosen form cognitively appropriate?
- Is final approval still human?
- If the candidate is KEEP and video is selected, is the handoff to continued production explicit?
