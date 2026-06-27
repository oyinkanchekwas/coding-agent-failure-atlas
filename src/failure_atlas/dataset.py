from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from failure_atlas.taxonomy import DETECTABILITY, FAILURE_MODES, SEVERITIES, SPLITS


REQUIRED_CASE_FIELDS = {
    "case_id",
    "title",
    "split",
    "primary_failure_mode",
    "severity",
    "task_family",
    "risk_surface",
    "lifecycle_stage",
    "detectability",
    "trace",
    "evidence",
    "intervention_point",
    "safe_counterfactual",
    "monitor_targets",
}

REQUIRED_EVENT_FIELDS = {"event_id", "actor", "action", "content"}
REQUIRED_EVIDENCE_FIELDS = {"event_id", "excerpt", "rationale"}


def load_cases(path: str | Path) -> list[dict[str, Any]]:
    dataset_path = Path(path)
    cases: list[dict[str, Any]] = []
    with dataset_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                case = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{dataset_path}:{line_number}: invalid JSON: {exc}") from exc
            case["_line_number"] = line_number
            cases.append(case)
    return cases


def validate_cases(cases: Iterable[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for case in cases:
        errors.extend(validate_case(case))
        case_id = str(case.get("case_id", "<missing>"))
        if case_id in seen_ids:
            errors.append(f"{case_id}: duplicate case_id")
        seen_ids.add(case_id)
    return errors


def validate_case(case: dict[str, Any]) -> list[str]:
    case_id = str(case.get("case_id", f"line-{case.get('_line_number', '?')}"))
    errors: list[str] = []
    missing = REQUIRED_CASE_FIELDS - set(case)
    if missing:
        errors.append(f"{case_id}: missing fields {sorted(missing)}")

    mode = case.get("primary_failure_mode")
    if mode not in FAILURE_MODES:
        errors.append(f"{case_id}: unknown primary_failure_mode {mode!r}")

    if case.get("severity") not in SEVERITIES:
        errors.append(f"{case_id}: invalid severity {case.get('severity')!r}")
    if case.get("split") not in SPLITS:
        errors.append(f"{case_id}: invalid split {case.get('split')!r}")
    if case.get("detectability") not in DETECTABILITY:
        errors.append(f"{case_id}: invalid detectability {case.get('detectability')!r}")

    trace = case.get("trace")
    if not isinstance(trace, list) or len(trace) < 3:
        errors.append(f"{case_id}: trace must contain at least three events")
        trace = []

    event_ids = set()
    for event in trace:
        if not isinstance(event, dict):
            errors.append(f"{case_id}: trace event is not an object")
            continue
        missing_event = REQUIRED_EVENT_FIELDS - set(event)
        if missing_event:
            errors.append(f"{case_id}: event missing fields {sorted(missing_event)}")
        event_id = event.get("event_id")
        if event_id in event_ids:
            errors.append(f"{case_id}: duplicate event_id {event_id!r}")
        event_ids.add(event_id)

    evidence = case.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append(f"{case_id}: evidence must be a non-empty list")
        evidence = []

    for item in evidence:
        if not isinstance(item, dict):
            errors.append(f"{case_id}: evidence item is not an object")
            continue
        missing_evidence = REQUIRED_EVIDENCE_FIELDS - set(item)
        if missing_evidence:
            errors.append(f"{case_id}: evidence missing fields {sorted(missing_evidence)}")
        if item.get("event_id") not in event_ids:
            errors.append(f"{case_id}: evidence references unknown event {item.get('event_id')!r}")

    if case.get("intervention_point") not in event_ids:
        errors.append(f"{case_id}: intervention_point does not reference a trace event")

    if not isinstance(case.get("monitor_targets"), list) or not case.get("monitor_targets"):
        errors.append(f"{case_id}: monitor_targets must be a non-empty list")
    if not str(case.get("safe_counterfactual", "")).strip():
        errors.append(f"{case_id}: safe_counterfactual is empty")

    return errors

