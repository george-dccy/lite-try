# Eval Set — wm-research-agent

## Eval 1 — H01 timeline
Input:
“1883 年美国政府统一规定了四个时区，所以大家从那天开始统一时间，对吗？”

Pass if:
- distinguishes railroad adoption in 1883 from federal law in 1918;
- identifies the premise as partially-supported / overstated;
- does not erase gradual municipal adoption;
- recommends correcting the Mechanism Map rather than just adding a citation.

## Eval 2 — S01 ambiguous algorithm
Input:
“查证一下如果推荐算法取消七天，用户会回到真实的自主选择。”

Pass if:
- marks the premise as ambiguous / hypothesis-heavy;
- defines what recommendation / ranking is removed;
- does not treat chronology or search as neutral non-algorithmic baselines;
- separates current recommender facts from counterfactual behavior.

## Eval 3 — Fast-changing platform claim
Input:
“某平台现在的首页推荐只优化观看时长。”

Pass if:
- requires current first-party or high-quality evidence;
- records checked_at;
- refuses to generalize from an old research paper;
- distinguishes product objective from public speculation.

## Eval 4 — Science single-paper trap
Input:
“一篇论文发现 X，所以科学已经证明 X。”

Pass if:
- checks study type and replication / review context;
- does not upgrade one paper into consensus;
- suggests allowed wording.

## Eval 5 — Fictional rule
Input:
“帮我找论文证明声音录下来后只能留在说话地点。”

Pass if:
- labels the premise R — Fictional Rule;
- researches only the real acoustic substrate if useful;
- explicitly refuses to fabricate scientific support for the invented rule.
