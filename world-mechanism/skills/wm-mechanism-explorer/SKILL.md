---
name: wm-mechanism-explorer
description: Use when a user wants to understand why a phenomenon happens, uncover a system's underlying mechanism, deepen a content idea before writing, stress-test a world rule, or turn a promising creative seed into a mechanism map. Do not use as a shortcut to directly produce scripts, titles, storyboards, or videos.
---

# World Mechanism Explorer

## Core contract

Help the creator **understand before expressing**.

The skill does not optimize for fast content generation. It turns a question, observation, historical detail, current phenomenon, knowledge point, or creative seed into a clearer model of how a system works, what is known, what is uncertain, and which counterfactuals reveal the mechanism.

A successful run should leave the creator with at least one of these:
- a sharper question;
- a mechanism they did not see before;
- a causal distinction that changes their view;
- a productive uncertainty worth researching;
- a counterfactual that exposes the mechanism.

If none happens, the run is not successful even if the output looks complete.

## Two valid entry routes

### Question-first
Question → Operationalize → Question Ladder → Mechanism Candidates → Evidence Gaps → Mechanism Map → Counterfactuals

### Spark-first
Creative Seed → Protect the seed → Behavior changes → Real mechanism it may expose → Mechanism Map → Stress test

Do not force a creative seed to pretend it began as research. Do not let a vivid seed bypass mechanism exploration entirely.

## Scope gate

Infer the user's intended scope:

- **Explore only**
- **Explore for creation**
- **Evaluate an existing premise**
- **Research-backed exploration**

If already supplied, do not re-ask. If broad, default to **Explore for creation** while keeping output pre-script.

## Workflow

### 1. Preserve the creator's starting point
Record:
- what they noticed;
- what feels strange or interesting;
- their current intuition;
- why they care, if known.

Do not replace their question with a fashionable content angle.

### 2. Operationalize ambiguous concepts

Before mechanism analysis, ask internally:

- What exactly counts as the thing being changed?
- What remains unchanged?
- What time / place / population does the claim cover?
- Does the question contain a false binary or undefined baseline?

Examples:
- “algorithm disappears” is unusable until the system states which ranking / personalization is removed and what alternatives remain;
- “people used local time” needs date and geography before historical inference.

If a factual premise is load-bearing, perform or request **Research Pass A** before continuing.

### 3. Build a short Question Ladder
Read references/question-ladder.md.

Use only layers that add understanding:
- phenomenon;
- causality;
- incentives;
- system;
- information;
- time;
- human behavior;
- author perspective.

Select the 5–10 highest-value questions. Do not mechanically fill every category.

### 4. Generate competing mechanism candidates

Produce 2–4 plausible candidates when uncertainty exists.

Prefer this structure:
- **Core mechanism**
- **Supporting pressures**
- **System consequences**
- **Competing explanation / boundary**

For each candidate:
- what it explains;
- what it misses;
- what evidence would distinguish it.

Never collapse correlation, incentive, and causation into one claim.

### 5. Separate evidence states

- **F — Fact**
- **I — Interpretation**
- **H — Hypothesis**
- **R — Fictional Rule**

If a factual claim matters and is not established, mark a research gap. Do not fill it with confident prose.

### 6. Build the Mechanism Map
Read references/mechanism-map-template.md.

Include only relevant:
- actors;
- incentives;
- constraints;
- flows;
- feedback loops;
- thresholds;
- time scales;
- path dependence;
- information asymmetry;
- institutional / physical substrate.

Finish with a **one-sentence model** that is accurate rather than clever.

### 7. Stress-test with counterfactuals
Read references/counterfactual-protocol.md.

Use at least three structurally different transformations where useful:
- Remove;
- Expose;
- Amplify;
- Delay / Accelerate;
- Localize;
- Invert.

For high-uncertainty social systems, prefer **branching scenarios** over a single deterministic timeline.

### 8. Return authorship to the human

Always include a short **Creator Gate**:

- What surprised you?
- Which explanation feels correct but uninteresting?
- Which uncertainty do you personally want to pursue?
- What would you refuse to simplify?
- What question would you actually want to discuss with your child, friend, or reader?

Do not answer these on the creator's behalf unless they explicitly ask for candidate answers.

### 9. Stop before production

If the user asked only for mechanism exploration, stop.

If the user wants to continue toward creation, output 2–4 **creative hypotheses** at most. Each must state:
- what real mechanism it exposes;
- what rule / perspective changes;
- what behavior it would generate;
- whether story is actually the best form.

Do not silently advance to screenplay, storyboard, renderer, or video prompts.

## Output contract

Read references/output-contract.md.

Default sections:
1. Starting Point
2. Operational Definition / Scope
3. Core Question
4. Question Ladder
5. Mechanism Candidates
6. Mechanism Map
7. Evidence Ledger
8. Counterfactuals
9. Creator Gate
10. Optional Creative Hypotheses
11. Status: candidate, needs-research, or ready-for-editorial-gate

## Failure modes

- **Title-first thinking**
- **Three-truth compression**
- **Moral-first analysis**
- **Mechanism = theme**
- **Single-cause confidence**
- **Undefined counterfactual**
- **Deterministic social forecasting**
- **Counterfactual spectacle**
- **Research dumping**
- **Creator erasure**

## Completion test

- Did the core question become more precise?
- Are ambiguous terms operationalized?
- Is the one-sentence mechanism causal or structural?
- Are F / I / H / R clearly separated?
- Is there at least one alternative explanation or boundary condition?
- Does the counterfactual expose a mechanism rather than decorate it?
- Are uncertain social adaptations branched / conditional rather than asserted?
- Is there a real human decision still left for the creator?
- Have you stopped before production unless explicitly asked to continue?
