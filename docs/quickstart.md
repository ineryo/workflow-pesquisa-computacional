# Experimente este repositório

Este guia executa o exemplo que já vem no repositório. Para aplicar as ideias na sua própria pesquisa, adapte a estrutura e as práticas ao seu contexto; você não precisa usar este repositório inteiro como base.

## 1. Obtenha o projeto

Para clonar o repositório, você precisa de [Git](https://git-scm.com/downloads). Se Git ainda é novo para você, veja [Git: o mínimo para começar](git-basics.md):

```bash
git --version
git clone https://github.com/ineryo/workflow-pesquisa-computacional.git
cd workflow-pesquisa-computacional
```

## 2. Execute o mini-projeto

Para executar a análise, você precisa de [Python](https://www.python.org/downloads/) 3.11 ou superior.

No Windows com PowerShell:

```powershell
py --version
cd examples/mini-project
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\analyze.py
```

No Linux ou macOS:

```bash
python3 --version
cd examples/mini-project
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python src/analyze.py
```

O ambiente `.venv` mantém a dependência do exemplo isolada do restante do sistema. Não é necessário ativá-lo: os comandos usam diretamente o Python desse ambiente.

O script lê `data/sample.csv` e produz:

```text
results/tables/summary.csv
results/tables/summary.md
results/figures/comparison.png
```

## 3. Leia o relatório em Markdown

Abra `docs/report.md` para ver o documento-fonte. A figura usa Markdown comum; a tabela é incluída a partir do arquivo gerado quando o documento é processado pelo MyST.

## 4. Renderize a documentação e os slides

Para renderizar, você precisa de [Node.js](https://nodejs.org/en/download) em uma versão LTS atualmente suportada, com npm:

```bash
node --version
npm --version
```

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
