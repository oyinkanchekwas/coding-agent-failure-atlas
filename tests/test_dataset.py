import unittest
from pathlib import Path

from failure_atlas.analysis import analyse_cases
from failure_atlas.dataset import load_cases, validate_cases


ROOT = Path(__file__).resolve().parents[1]


class DatasetTests(unittest.TestCase):
    def test_seed_dataset_validates(self) -> None:
        cases = load_cases(ROOT / "data/cases.jsonl")
        errors = validate_cases(cases)

        self.assertEqual(errors, [])

    def test_seed_dataset_has_expected_shape(self) -> None:
        cases = load_cases(ROOT / "data/cases.jsonl")
        summary = analyse_cases(cases)

        self.assertEqual(summary["case_count"], 120)
        self.assertEqual(summary["failure_mode_count"], 12)
        self.assertEqual(summary["by_split"], {"dev": 24, "test": 24, "train": 72})
        self.assertTrue(all(count == 10 for count in summary["by_failure_mode"].values()))


if __name__ == "__main__":
    unittest.main()

