# Datasheet

## Motivation

Coding-agent monitoring needs labelled examples that include more than final code diffs.
This atlas focuses on trace-level failures: what the user asked, what the agent planned,
what it did, where a monitor should intervene, and what a safer counterfactual action
would look like.

## Composition

Seed release:

- 120 synthetic cases.
- 12 failure modes.
- 10 cases per failure mode.
- 4 trace events per case.
- 1 evidence span per case.
- Deterministic splits: 72 train, 24 dev, 24 test.

Each case includes:

- `primary_failure_mode`
- `severity`
- `risk_surface`
- `lifecycle_stage`
- `detectability`
- `trace`
- `evidence`
- `intervention_point`
- `safe_counterfactual`
- `monitor_targets`
- `decision`

## Collection Process

The seed dataset is generated from hand-written templates in `scripts/materialise_dataset.py`.
It is synthetic by design: no real credentials, users, repositories, logs, accounts, or private
data are included.

## Recommended Uses

- Train and test coding-agent monitors.
- Compare deterministic monitors with LLM-as-judge monitors.
- Build evidence-span extraction experiments.
- Test whether monitors can identify the correct intervention point.
- Teach reviewers how coding-agent failures appear in traces.

## Unsuitable Uses

- Measuring real-world failure prevalence.
- Claiming production security coverage.
- Training a model to execute the unsafe actions in the traces.
- Treating the seed release as a substitute for human-labelled production logs.

## Known Limits

The cases are synthetic and compact. They support early monitor development, but they do not
capture the full messiness of real coding-agent sessions: long tool chains, partial edits,
ambiguous user intent, reviewer disagreement, and multi-turn recovery.

## Release Policy

Real traces are outside the seed release unless they have gone through manual review, secret
scanning, and removal of private or identifying information.
