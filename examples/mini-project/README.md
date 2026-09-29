# Mini-projeto de exemplo

Este exemplo existe para mostrar o fluxo, não para ensinar Python.

```text
data/sample.csv
      ↓
src/analyze.py
      ↓
results/
      ↓
docs/report.md
```

Execute:

```bash
python src/analyze.py
```

Depois abra `docs/report.md`.

Com MyST instalado, por exemplo:

```bash
npx --yes mystmd@latest build docs/report.md --pdf --docx
```

O PDF requer LaTeX ou Typst instalado localmente; o DOCX pode ser gerado sem esse requisito.
