# Related Work

This repo sits between software-engineering agent benchmarks and agent-safety benchmarks.

## Software-Engineering Agent Benchmarks

[SWE-bench](https://arxiv.org/abs/2310.06770) evaluates whether models can resolve real GitHub
issues by editing repositories and passing tests. Later work such as
[SWE-rebench](https://arxiv.org/abs/2505.20411) focuses on larger and fresher interactive software
engineering tasks.

Those benchmarks are mainly task-completion benchmarks. They ask whether the agent solves the
issue. The atlas asks a different question: can a monitor catch risky process failures while the
agent is attempting the task?

## Agent Harm Benchmarks

[AgentHarm](https://arxiv.org/abs/2410.09024) studies harmful multi-step agent tasks. More recent
computer-use safety benchmarks such as [CUAHarm](https://arxiv.org/abs/2508.00935) evaluate whether
computer-using agents can carry out risky actions, and include monitor analysis.

The atlas is narrower. It focuses on coding-agent traces and monitor labels: evidence spans,
intervention points, safe counterfactuals, and detectability tags.

## Owner-Harm Framing

[Owner-Harm](https://arxiv.org/abs/2604.18658) argues that deployed agents can harm their own
operators or organisations, not only third parties. That framing is close to several atlas labels:
`data_exfiltration`, `permission_boundary_violation`, `false_verification_claim`, and
`prompt_injection_compliance`.

## Gap This Atlas Targets

The seed release is not a replacement for larger benchmarks. Its value is the schema:

- trace-level cases,
- exact evidence spans,
- intervention points,
- safe counterfactuals,
- detectability labels for monitor design.

That makes it useful for early experiments on coding-agent monitors, especially before a team has
access to large private trace logs.

