.PHONY: data validate analyse test

data:
	PYTHONPATH=src python3 scripts/materialise_dataset.py

validate:
	PYTHONPATH=src python3 -m failure_atlas validate data/cases.jsonl

analyse:
	PYTHONPATH=src python3 -m failure_atlas analyse data/cases.jsonl --out reports/dataset_summary.json

test:
	PYTHONPATH=src python3 -m unittest discover -s tests -v

quality:
	PYTHONPATH=src python3 scripts/quality_gate.py
