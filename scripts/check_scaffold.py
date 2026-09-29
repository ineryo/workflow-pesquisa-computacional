from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "myst.yml",
    "docs/quickstart.md",
    "docs/git-basics.md",
    "docs/markdown-rendering.md",
    "docs/decisions/ADR-0001-markdown-first-research-workflow.md",
    "examples/mini-project/docs/report.md",
    "examples/mini-project/results/figures/comparison.svg",
]

missing = [path for path in required if not (ROOT / path).exists()]
qmd_files = list(ROOT.rglob("*.qmd"))

if missing:
    print("Arquivos obrigatórios ausentes:")
    for path in missing:
        print(f"  - {path}")
    sys.exit(1)

if qmd_files:
    print("Foram encontrados arquivos .qmd, contrariando a decisão Markdown-first:")
    for path in qmd_files:
        print(f"  - {path.relative_to(ROOT)}")
    sys.exit(1)

print("Scaffold básico válido.")
