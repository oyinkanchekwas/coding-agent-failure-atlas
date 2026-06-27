# Novelty

This atlas is deliberately narrower than general agent benchmarks. It is built for one problem:
training and evaluating monitors for coding-agent traces.

## What Is Different

- Trace-level cases, not only final diffs.
- Evidence spans linked to event ids.
- Intervention points showing where a monitor should act.
- Safe counterfactuals showing how the agent could still complete the user task.
- Detectability tags that separate pattern, semantic, cross-event, and contextual failures.
- A taxonomy that includes coding-agent-specific integrity failures, such as test weakening
  and false verification claims.

## Why This Matters

A monitor that only sees final code can miss failures that happen in the process:

- an unsafe shell command that left no code diff,
- a prompt injection embedded in a tool result,
- a failed test hidden by the final response,
- a boundary crossing such as publishing a repository without approval.

The atlas makes those failures first-class dataset objects.

## Research Questions It Supports

1. Can monitors identify the exact event where intervention is needed?
2. Which failure modes are detectable with patterns, and which need semantic or contextual review?
3. Do LLM-as-judge monitors over-warn on benign but scary-looking traces?
4. Can small fine-tuned monitors learn evidence-span extraction rather than only case labels?
5. Does adding safe counterfactual supervision improve remediation quality?

