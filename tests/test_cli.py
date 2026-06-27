import json
import tempfile
import unittest
from pathlib import Path

from failure_atlas.cli import main


ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def test_analyse_writes_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "summary.json"
            code = main(["analyse", str(ROOT / "data/cases.jsonl"), "--out", str(out), "--pretty"])
            summary = json.loads(out.read_text(encoding="utf-8"))

        self.assertEqual(code, 0)
        self.assertEqual(summary["case_count"], 120)


if __name__ == "__main__":
    unittest.main()

