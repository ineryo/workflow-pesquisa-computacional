# Experimente este repositório

Este guia executa o exemplo que já vem no repositório. Para aplicar as ideias na sua própria pesquisa, adapte a estrutura e as práticas ao seu contexto; você não precisa usar este repositório inteiro como base.

## O que você precisa

Confira as ferramentas disponíveis:

```bash
git --version
python --version
node --version
npm --version
```

O mini-projeto usa apenas a biblioteca padrão do Python, portanto não precisa de `requirements.txt` nem de ambiente virtual. Node.js e npm são usados para executar MyST e Marp com `npx`, sem instalação global dessas ferramentas.

## 1. Clone o repositório

```bash
git clone https://github.com/ineryo/workflow-pesquisa-computacional.git
cd workflow-pesquisa-computacional
```

## 2. Execute o mini-projeto

```bash
cd examples/mini-project
python src/analyze.py
```

O script lê `data/sample.csv` e produz:

```text
results/tables/summary.csv
results/tables/summary.md
results/figures/comparison.svg
```

## 3. Leia o relatório em Markdown

Abra `docs/report.md` no editor, no GitHub ou em qualquer visualizador de Markdown. O relatório usa a tabela e a figura que o script acabou de gerar.

## 4. Veja o site local

Volte para a raiz do repositório e inicie o site:

```bash
cd ../..
npx --yes mystmd@latest start
```

O MyST mostra um endereço local no terminal. Deixe esse comando em execução e abra o endereço no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

## 5. Gere um primeiro documento

Para gerar uma cópia DOCX do relatório:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --docx --strict
```

O arquivo gerado fica em `exports/mini-project-report.docx`. A figura é SVG; se ImageMagick não estiver instalado, o MyST pode avisar que a conversão da imagem precisa ser conferida no documento final.

## Opcional: experimente os slides

O deck reutiliza a figura produzida pelo mini-projeto. Os comandos para gerar PDF ou PPTX, e os requisitos de navegador, estão em [Markdown e renderização](markdown-rendering.md).

## Leve as ideias para sua pesquisa

Quando quiser começar um projeto próprio, crie uma estrutura pequena com `data/`, `src/`, `results/`, `docs/` e um `README.md`. Adapte os nomes ao seu domínio, registre como executar a análise e mantenha resultados protegidos fora do repositório quando necessário.

Veja [Git: o mínimo para começar](git-basics.md) e [ferramentas e caminhos para explorar](extras/tooling-landscape.md) quando aparecer uma necessidade concreta.
