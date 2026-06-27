from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from failure_atlas.analysis import analyse_cases
from failure_atlas.dataset import load_cases, validate_cases
from failure_atlas.taxonomy import taxonomy_as_dict


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "validate":
        return _validate(args)
    if args.command == "analyse":
        return _analyse(args)
    if args.command == "taxonomy":
        return _taxonomy(args)
    parser.print_help()
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="failure-atlas",
        description="Validate and analyse the Coding Agent Failure Atlas dataset.",
    )
    subparsers = parser.add_subparsers(dest="command")

    validate = subparsers.add_parser("validate", help="Validate dataset JSONL.")
    validate.add_argument("dataset", type=Path)

    analyse = subparsers.add_parser("analyse", help="Produce dataset summary counts.")
    analyse.add_argument("dataset", type=Path)
    analyse.add_argument("--out", type=Path)
    analyse.add_argument("--pretty", action="store_true")

    taxonomy = subparsers.add_parser("taxonomy", help="Print the failure-mode taxonomy.")
    taxonomy.add_argument("--out", type=Path)
    taxonomy.add_argument("--pretty", action="store_true")

    return parser


def _validate(args: argparse.Namespace) -> int:
    cases = load_cases(args.dataset)
    errors = validate_cases(cases)
    if errors:
        for error in errors:
            sys.stderr.write(error + "\n")
        return 1
    sys.stdout.write(f"Validated {len(cases)} cases.\n")
    return 0


def _analyse(args: argparse.Namespace) -> int:
    cases = load_cases(args.dataset)
    errors = validate_cases(cases)
    if errors:
        for error in errors:
            sys.stderr.write(error + "\n")
        return 1
    _emit_json(analyse_cases(cases), args.out, pretty=args.pretty)
    return 0


def _taxonomy(args: argparse.Namespace) -> int:
    _emit_json(taxonomy_as_dict(), args.out, pretty=args.pretty)
    return 0


def _emit_json(payload: object, out: Path | None, *, pretty: bool) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=True)
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")

