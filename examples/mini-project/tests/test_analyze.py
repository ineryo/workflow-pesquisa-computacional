from __future__ import annotations

import csv
import math
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

import analyze  # noqa: E402


class AnalyzeTests(unittest.TestCase):
    def test_rmse_matches_known_value(self) -> None:
        rows = [
            {"analytical": 0.0, "numerical": 0.0},
            {"analytical": 0.0, "numerical": 3.0},
            {"analytical": 0.0, "numerical": 4.0},
        ]

        self.assertTrue(math.isclose(analyze.rmse(rows), 5 / math.sqrt(3)))

    def test_run_analysis_writes_expected_results(self) -> None:
        data = Path(__file__).resolve().parents[1] / "data" / "sample.csv"
        with tempfile.TemporaryDirectory() as temporary_directory:
            results = Path(temporary_directory) / "results"
            value = analyze.run_analysis(data, results)

            self.assertTrue(math.isclose(value, 0.0209, abs_tol=0.0001))
            self.assertTrue((results / "figures" / "comparison.png").is_file())
            self.assertGreater((results / "figures" / "comparison.png").stat().st_size, 0)

            with (results / "tables" / "summary.csv").open(encoding="utf-8") as f:
                self.assertEqual(
                    list(csv.DictReader(f)), [{"metric": "RMSE", "value": "0.0209"}]
                )
            self.assertIn(
                "| RMSE | 0.0209 |",
                (results / "tables" / "summary.md").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
