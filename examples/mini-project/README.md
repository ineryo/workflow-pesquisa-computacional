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

Este exemplo requer Python 3.11 ou superior. Na pasta deste mini-projeto, crie e ative um ambiente virtual antes de instalar a dependência.

No Windows com PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/analyze.py
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/analyze.py
```

Depois abra `docs/report.md` e `../../docs/slides-example.md` para ver duas formas de comunicar o mesmo resultado.

## Exporte o relatório

Os comandos e requisitos para gerar DOCX, PDF ou slides estão em [`../../docs/markdown-rendering.md`](../../docs/markdown-rendering.md).
