# Markdown e renderização

```text
report.md  ──MyST──→ site / DOCX / PDF
slides.md  ──Marp──→ PDF / PPTX
```

Os documentos deste repositório são arquivos `.md`. Você pode lê-los e editá-los como texto; quando precisar compartilhar, pode gerar site, documento ou slides.

## Como navegar localmente pelo site

Para leitura e navegação, na raiz do repositório execute:

```bash
npx --yes mystmd@1.11.0 start
```

O MyST mostra um endereço local no terminal. Deixe esse comando em execução e abra o endereço no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

## Como validar a estrutura do site

```bash
npx --yes mystmd@1.11.0 build --site --strict
```

Esse comando gera e valida a estrutura e as referências internas do site. `_build/site/` contém os dados estruturados desse build.

## Como gerar um documento

O relatório do mini-projeto fica em `examples/mini-project/docs/report.md`.

Para gerar DOCX:

```bash
npx --yes mystmd@1.11.0 build examples/mini-project/docs/report.md --docx --strict
```

O arquivo é exportado para `exports/mini-project-report.docx`.

Para gerar PDF:

```bash
npx --yes mystmd@1.11.0 build examples/mini-project/docs/report.md --pdf --strict
```

O PDF deste exemplo requer tooling adicional de LaTeX. MyST também suporta fluxos baseados em Typst, mas eles exigem configuração própria e não fazem parte deste exemplo inicial.

[MyST](https://mystmd.org/) permite trabalhar com documentos científicos em Markdown, incluindo referências, equações, links e inclusão de resultados produzidos pela análise.

## Como gerar slides

O exemplo de apresentação está em `docs/slides-example.md`.

PDF:

```bash
npx --yes @marp-team/marp-cli@4.5.1 --theme-set styles/marp/research.css --allow-local-files --pdf --output exports/slides-example.pdf docs/slides-example.md
```

PPTX:

```bash
npx --yes @marp-team/marp-cli@4.5.1 --theme-set styles/marp/research.css --allow-local-files --pptx --output exports/slides-example.pptx docs/slides-example.md
```

A exportação de PDF ou PPTX pelo Marp requer Chrome, Chromium, Edge ou Firefox. Se o navegador não estiver na localização usual, indique-o com `CHROME_PATH`.

[Marp](https://marp.app/) transforma um arquivo Markdown com frontmatter em uma apresentação.

## Outra conversão quando necessário

[Pandoc](https://pandoc.org/) é útil quando você precisa converter um Markdown para outro formato:

```bash
pandoc documento.md -o documento.docx
```

Use a documentação da ferramenta escolhida quando o seu documento exigir recursos específicos.
