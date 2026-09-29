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
results/figures/comparison.svg
  ↓
docs/report.md e docs/slides-example.md
```

- `data/sample.csv` contém os dados sintéticos.
- `src/analyze.py` calcula o erro e produz uma tabela e uma figura.
- `results/` guarda os artefatos produzidos pela análise.
- `docs/report.md` usa a tabela e a figura no relatório.
- `docs/slides-example.md` reutiliza a figura em uma apresentação.

## Execute

Na pasta deste mini-projeto:

```bash
python src/analyze.py
```

Depois abra `docs/report.md` e `../../docs/slides-example.md` para ver duas formas de comunicar o mesmo resultado.

## Exporte o relatório

Para gerar DOCX:

```bash
npx --yes mystmd@latest build docs/report.md --docx
```

Para gerar PDF, use o mesmo comando com `--pdf`. A rota de PDF precisa de LaTeX ou Typst instalado localmente.

Os comandos para gerar slides estão em [`../../docs/markdown-rendering.md`](../../docs/markdown-rendering.md).
