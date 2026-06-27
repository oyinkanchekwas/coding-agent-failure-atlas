from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable


def analyse_cases(cases: Iterable[dict[str, Any]]) -> dict[str, Any]:
    cases = list(cases)
    by_mode = Counter(case["primary_failure_mode"] for case in cases)
    by_split = Counter(case["split"] for case in cases)
    by_severity = Counter(case["severity"] for case in cases)
    by_detectability = Counter(case["detectability"] for case in cases)
    by_surface = Counter(case["risk_surface"] for case in cases)
    split_by_mode: dict[str, Counter[str]] = defaultdict(Counter)

    for case in cases:
        split_by_mode[case["primary_failure_mode"]][case["split"]] += 1

    return {
        "case_count": len(cases),
        "failure_mode_count": len(by_mode),
        "by_failure_mode": dict(sorted(by_mode.items())),
        "by_split": dict(sorted(by_split.items())),
        "by_severity": dict(sorted(by_severity.items())),
        "by_detectability": dict(sorted(by_detectability.items())),
        "by_risk_surface": dict(sorted(by_surface.items())),
        "split_by_failure_mode": {
            mode: dict(sorted(counts.items())) for mode, counts in sorted(split_by_mode.items())
        },
    }

