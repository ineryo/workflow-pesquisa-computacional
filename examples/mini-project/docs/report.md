---
title: Comparação entre uma solução analítica e uma solução numérica
authors:
  - name: Exemplo sintético
exports:
  - format: pdf
    output: ../../../exports/mini-project-report.pdf
  - format: docx
    output: ../../../exports/mini-project-report.docx
---

# Comparação entre uma solução analítica e uma solução numérica

Os dados de exemplo estão em `../data/sample.csv`. O script `../src/analyze.py` produz a tabela e a figura em `../results/`.

## Resultado

![Comparação entre as soluções](../results/figures/comparison.svg)

A tabela abaixo vem do arquivo gerado pela análise:

```{include} ../results/tables/summary.md
```

A figura e a tabela podem ser reutilizadas no relatório e em uma apresentação sem copiar os valores para outro arquivo.
