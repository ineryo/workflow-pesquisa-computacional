from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample.csv"
TABLES = ROOT / "results" / "tables"
FIGURES = ROOT / "results" / "figures"


def load_rows():
    with DATA.open(encoding="utf-8") as f:
        return [
            {
                "x": float(row["x"]),
                "analytical": float(row["analytical"]),
                "numerical": float(row["numerical"]),
            }
            for row in csv.DictReader(f)
        ]


def rmse(rows):
    if not rows:
        raise ValueError("É necessária ao menos uma linha para calcular o RMSE.")
    return math.sqrt(
        sum((r["numerical"] - r["analytical"]) ** 2 for r in rows) / len(rows)
    )


def write_summary(rows):
    TABLES.mkdir(parents=True, exist_ok=True)
    value = rmse(rows)

    with (TABLES / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerow(["RMSE", f"{value:.4f}"])

    (TABLES / "summary.md").write_text(
        "| Métrica | Valor |\n"
        "|---|---:|\n"
        f"| RMSE | {value:.4f} |\n",
        encoding="utf-8",
    )


def write_svg(rows):
    FIGURES.mkdir(parents=True, exist_ok=True)

    width, height = 720, 380
    left, right, top, bottom = 70, 30, 30, 55
    xmin, xmax = min(r["x"] for r in rows), max(r["x"] for r in rows)
    ymin, ymax = -0.05, 1.05

    def sx(x):
        return left + (x - xmin) / (xmax - xmin) * (width - left - right)

    def sy(y):
        return top + (ymax - y) / (ymax - ymin) * (height - top - bottom)

    def polyline(key):
        return " ".join(f"{sx(r['x']):.1f},{sy(r[key]):.1f}" for r in rows)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  <line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="black"/>
  <line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="black"/>
  <polyline points="{polyline('analytical')}" fill="none" stroke="black" stroke-width="2"/>
  <polyline points="{polyline('numerical')}" fill="none" stroke="gray" stroke-width="2" stroke-dasharray="7 5"/>
  <text x="{width/2}" y="{height-12}" text-anchor="middle" font-family="sans-serif" font-size="16">x</text>
  <text x="18" y="{height/2}" transform="rotate(-90 18 {height/2})" text-anchor="middle" font-family="sans-serif" font-size="16">resposta</text>
  <text x="{width-210}" y="32" font-family="sans-serif" font-size="14">solução analítica</text>
  <text x="{width-210}" y="54" font-family="sans-serif" font-size="14">solução numérica</text>
</svg>"""
    (FIGURES / "comparison.svg").write_text(svg, encoding="utf-8")


def main():
    rows = load_rows()
    write_summary(rows)
    write_svg(rows)
    print("Resultados gerados em results/.")


if __name__ == "__main__":
    main()
