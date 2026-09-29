# Mini-projeto de exemplo

Este exemplo mostra uma análise pequena. Ele não é um curso de Python.

## O que entra e o que sai

```text
data/sample.csv
  ↓
src/analyze.py
  ↓
results/tables/summary.csv
results/tables/summary.md
results/figures/comparison.png
  ↓
docs/report.md e ../../docs/slides-example.md
```

- `data/sample.csv` contém os dados sintéticos.
- `src/analyze.py` calcula o erro e produz uma tabela e uma figura.
- `results/` guarda os artefatos produzidos pela análise.
- `docs/report.md` usa a tabela e a figura no relatório.
- `../../docs/slides-example.md` reutiliza a figura em uma apresentação.

## Execute

Este exemplo requer Python 3.11 ou superior. O ambiente `.venv` mantém a dependência isolada e não precisa ser ativado.

No Windows com PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\analyze.py
```

No Linux ou macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python src/analyze.py
```

Depois abra `docs/report.md` e `../../docs/slides-example.md` para ver duas formas de comunicar o mesmo resultado.

## Exporte o relatório

Os comandos e requisitos para gerar DOCX, PDF ou slides estão em [`../../docs/markdown-rendering.md`](../../docs/markdown-rendering.md).
