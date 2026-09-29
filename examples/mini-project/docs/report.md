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

Este documento é deliberadamente pequeno. Ele demonstra a separação entre:

- dados;
- código;
- resultados;
- comunicação.

Os dados de exemplo estão em `../data/sample.csv`. O script `../src/analyze.py` gera os artefatos em `../results/`.

## Resultado

A figura abaixo é produzida pelo script:

![Comparação entre as soluções](../results/figures/comparison.svg)

A tabela abaixo também é gerada pelo script. O bloco a seguir usa uma diretiva MyST opcional para incluir o arquivo Markdown produzido pela análise:

```{include} ../results/tables/summary.md
```

O arquivo continua sendo `.md`. A diretiva é um exemplo de extensão progressiva: ela é útil aqui, mas não é uma exigência do protocolo.
