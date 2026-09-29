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
    "examples/mini-project/requirements.txt",
    "examples/mini-project/docs/report.md",
    "examples/mini-project/results/figures/comparison.png",
]

missing = [path for path in required if not (ROOT / path).exists()]
markdown_files = [
    path
    for path in ROOT.rglob("*.md")
    if "_build" not in path.parts and ".venv" not in path.parts
]
latest_references = [
    path.relative_to(ROOT)
    for path in markdown_files
    if "@latest" in path.read_text(encoding="utf-8")
]

if missing:
    print("Arquivos obrigatórios ausentes:")
    for path in missing:
        print(f"  - {path}")
    sys.exit(1)

if latest_references:
    print("Referências a @latest encontradas na documentação:")
    for path in latest_references:
        print(f"  - {path}")
    sys.exit(1)

print("Scaffold básico válido.")
