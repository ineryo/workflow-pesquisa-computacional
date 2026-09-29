# Experimente este repositório

Este guia executa o exemplo que já vem no repositório. Para aplicar as ideias na sua própria pesquisa, adapte a estrutura e as práticas ao seu contexto; você não precisa usar este repositório inteiro como base.

## O que você precisa

Para executar o mini-projeto, use Git para clonar o repositório e Python 3 para executar a análise. Para renderizar site, documento ou slides, você também precisará de Node.js com npm. Confira se essas ferramentas estão disponíveis:

```bash
git --version
python3 --version
node --version
npm --version
```

## 1. Clone o repositório

```bash
git clone https://github.com/ineryo/workflow-pesquisa-computacional.git
cd workflow-pesquisa-computacional
```

## 2. Execute o mini-projeto

Na pasta do mini-projeto, crie um ambiente virtual, instale a dependência e execute a análise:

```bash
cd examples/mini-project
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --requirement requirements.txt
python src/analyze.py
```

O script lê `data/sample.csv` e produz:

```text
results/tables/summary.csv
results/tables/summary.md
results/figures/comparison.png
```

## 3. Leia o relatório em Markdown

Abra `docs/report.md` no editor, no GitHub ou em qualquer visualizador de Markdown. O relatório usa a tabela e a figura que o script acabou de gerar.

## 4. Veja o site local

Volte para a raiz do repositório e inicie o site:

```bash
cd ../..
npx --yes mystmd@1.11.0 start
```

O MyST mostra um endereço local no terminal. Deixe esse comando em execução e abra o endereço no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

## 5. Gere um primeiro documento

Para gerar uma cópia DOCX do relatório:

```bash
npx --yes mystmd@1.11.0 build examples/mini-project/docs/report.md --docx --strict
```

O arquivo gerado fica em `exports/mini-project-report.docx`.

## Opcional: experimente os slides

O deck reutiliza a figura produzida pelo mini-projeto. Os comandos para gerar PDF ou PPTX, e os requisitos de navegador, estão em [Markdown e renderização](markdown-rendering.md).

## Leve as ideias para sua pesquisa

Quando quiser começar um projeto próprio, crie uma estrutura pequena com `data/`, `src/`, `results/`, `docs/` e um `README.md`. Adapte os nomes ao seu domínio, registre como executar a análise e mantenha resultados protegidos fora do repositório quando necessário.

Veja [Git: o mínimo para começar](git-basics.md) e [ferramentas e caminhos para explorar](extras/tooling-landscape.md) quando aparecer uma necessidade concreta.
