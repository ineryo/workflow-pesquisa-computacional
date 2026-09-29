from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

import analyze  # noqa: E402


class AnalyzeTests(unittest.TestCase):
    def test_rmse_rejects_empty_rows(self) -> None:
        with self.assertRaisesRegex(ValueError, "ao menos uma linha"):
            analyze.rmse([])

    def test_write_summary_uses_lf_line_endings(self) -> None:
        rows = [{"analytical": 0.0, "numerical": 0.02}]
        original_tables = analyze.TABLES
        try:
            with tempfile.TemporaryDirectory() as temporary_directory:
                analyze.TABLES = Path(temporary_directory)
                analyze.write_summary(rows)
                self.assertEqual(
                    (analyze.TABLES / "summary.csv").read_bytes(),
                    b"metric,value\nRMSE,0.0200\n",
                )
        finally:
            analyze.TABLES = original_tables


if __name__ == "__main__":
    unittest.main()
