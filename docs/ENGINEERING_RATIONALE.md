# Engineering Rationale

This dataset is meant to make coding-agent failure traces easy to inspect and evaluate.

## Why a trace-level atlas

Most coding-agent evaluation is centred on whether the final patch works. That misses failures in
the process: a destructive shell command, a hidden failed test, a prompt injection in a tool result,
or a boundary crossing that leaves no obvious final diff. I structured the dataset around traces
because monitors need to catch those failures while the agent is working.

## Why the seed release is synthetic

Real traces are more valuable, but they carry privacy, credential, and consent risks. The seed
release is synthetic so it can be public, reproducible, and safe to inspect. The schema is the main
contribution: evidence spans, intervention points, safe counterfactuals, and detectability labels.

## Why fixture tokens are clearly fake

Some labels need credential-shaped failures. Public data should still avoid realistic provider-token
strings. The seed cases therefore use explicit `FAKE_*_DO_NOT_USE` fixture values. They are there to
teach the failure pattern without adding secret-scanning noise or normalising the practice of
committing realistic tokens.

## Why the dataset is balanced

The seed release has ten cases per label because the goal is monitor development, not measuring
real-world prevalence. A balanced first release makes it easier to test whether a monitor can cover
each category before moving to messier real traces.

## Commit Standard

Commit messages are most useful when they explain why the change exists. For this repo, that usually includes:

- the failure mode, schema field, or quality risk being addressed,
- why the chosen design is safer or easier to evaluate,
- what validation was run.

Example:

```text
Replace realistic synthetic token strings

Why: the atlas should teach credential exposure without storing provider-shaped fake secrets in
public examples.

Validation: regenerated the dataset, ran validator, tests, and quality gate.
```
