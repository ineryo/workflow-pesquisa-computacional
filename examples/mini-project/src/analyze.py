from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample.csv"
RESULTS = ROOT / "results"


def load_rows(data_path: Path) -> list[dict[str, float]]:
    with data_path.open(encoding="utf-8") as f:
        return [
            {
                "x": float(row["x"]),
                "analytical": float(row["analytical"]),
                "numerical": float(row["numerical"]),
            }
            for row in csv.DictReader(f)
        ]


def rmse(rows: list[dict[str, float]]) -> float:
    if not rows:
        raise ValueError("É necessária ao menos uma linha para calcular o RMSE.")
    return math.sqrt(
        sum((row["numerical"] - row["analytical"]) ** 2 for row in rows) / len(rows)
    )


def write_summary(rows: list[dict[str, float]], tables: Path) -> float:
    tables.mkdir(parents=True, exist_ok=True)
    value = rmse(rows)

    with (tables / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerow(["RMSE", f"{value:.4f}"])

    (tables / "summary.md").write_text(
        "| Métrica | Valor |\n"
        "|---|---:|\n"
        f"| RMSE | {value:.4f} |\n",
        encoding="utf-8",
    )
    return value


def write_figure(rows: list[dict[str, float]], figure_path: Path) -> None:
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    x_values = [row["x"] for row in rows]
    analytical = [row["analytical"] for row in rows]
    numerical = [row["numerical"] for row in rows]

    figure, axis = plt.subplots(figsize=(7.2, 3.8), layout="constrained")
    axis.plot(x_values, analytical, color="black", label="solução analítica")
    axis.plot(
        x_values,
        numerical,
        color="gray",
        linestyle="--",
        label="solução numérica",
    )
    axis.set(xlabel="x", ylabel="resposta")
    axis.legend()
    figure.savefig(figure_path, dpi=160)
    plt.close(figure)


def run_analysis(data_path: Path, results: Path) -> float:
    rows = load_rows(data_path)
    value = write_summary(rows, results / "tables")
    write_figure(rows, results / "figures" / "comparison.png")
    return value


def main() -> None:
    run_analysis(DATA, RESULTS)
    print("Resultados gerados em results/.")


if __name__ == "__main__":
    main()
