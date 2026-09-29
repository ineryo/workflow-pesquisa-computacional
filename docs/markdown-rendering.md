# Markdown e renderização

```text
report.md  ──MyST──→ site / DOCX / PDF
slides.md  ──Marp──→ PDF / PPTX
```

Os documentos deste repositório são arquivos `.md`. Você pode lê-los e editá-los como texto; quando precisar compartilhar, pode gerar site, documento ou slides.

## Como ler ou gerar o site

Para navegar localmente pelo site, na raiz do repositório execute:

```bash
npx --yes mystmd@latest start
```

O MyST mostra um endereço local no terminal. Deixe esse comando em execução e abra o endereço no navegador. Para encerrar o servidor, pressione `Ctrl+C`.

Para gerar e validar o site, execute:

```bash
npx --yes mystmd@latest build --site --strict
```

Esse comando constrói o site e interrompe o build se encontrar referências internas inválidas. Os arquivos gerados ficam em `_build/site/`.

## Como gerar um documento

O relatório do mini-projeto fica em `examples/mini-project/docs/report.md`.

Para gerar DOCX:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --docx --strict
```

O arquivo é exportado para `exports/mini-project-report.docx`. Como o relatório usa uma figura SVG, o MyST pode avisar que ImageMagick é necessário para convertê-la; confira o documento gerado se essa ferramenta não estiver instalada.

Para gerar PDF:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --pdf --strict
```

PDF requer tooling adicional, como LaTeX ou Typst instalado localmente. Se ainda não tiver um desses renderizadores, use o DOCX ou o site para começar.

[MyST](https://mystmd.org/) permite trabalhar com documentos científicos em Markdown, incluindo referências, equações, links e inclusão de resultados produzidos pela análise.

## Como gerar slides

O exemplo de apresentação está em `docs/slides-example.md`.

PDF:

```bash
npx --yes @marp-team/marp-cli@latest --theme-set styles/marp/research.css --allow-local-files --pdf --output exports/slides-example.pdf docs/slides-example.md
```

PPTX:

```bash
npx --yes @marp-team/marp-cli@latest --theme-set styles/marp/research.css --allow-local-files --pptx --output exports/slides-example.pptx docs/slides-example.md
```

A exportação de PDF ou PPTX pelo Marp requer Chrome, Chromium, Edge ou Firefox. Se o navegador não estiver na localização usual, indique-o com `CHROME_PATH`.

[Marp](https://marp.app/) transforma um arquivo Markdown com frontmatter em uma apresentação.

## Outra conversão quando necessário

[Pandoc](https://pandoc.org/) é útil quando você precisa converter um Markdown para outro formato:

```bash
pandoc documento.md -o documento.docx
```

Use a documentação da ferramenta escolhida quando o seu documento exigir recursos específicos.
