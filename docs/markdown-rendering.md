# Markdown e renderização

A decisão central deste projeto é manter o conteúdo humano em arquivos `.md`.

Isso permite que o texto permaneça:

- legível diretamente;
- versionável como texto;
- utilizável em GitHub, VS Code, Obsidian e outros editores;
- relativamente independente de uma ferramenta específica de publicação.

## MyST como implementação de referência

MyST é usado como backend recomendado para documentos científicos.

Exemplo:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --pdf
```

ou:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --docx
```

O mini-projeto declara esses exports no frontmatter do próprio relatório. PDF requer uma instalação local de LaTeX ou Typst; DOCX pode ser usado quando esse renderer ainda não estiver disponível.

O projeto não é “um projeto MyST”. MyST é um renderer recomendado.

Recursos específicos de MyST podem ser introduzidos quando forem úteis, como referências cruzadas ou inclusão de conteúdo, mantendo o arquivo com extensão `.md`.

Documentação:

https://mystmd.org/

## Marp para apresentações

Marp permite que uma apresentação continue sendo um `.md`. Para exportar o exemplo deste repositório:

```bash
npx --yes @marp-team/marp-cli@latest \
  --theme-set styles/marp/research.css \
  --pdf --output exports/slides-example.pdf \
  docs/slides-example.md
```

A exportação PDF requer Chrome, Chromium, Edge ou Firefox disponível no sistema (ou indicado por `CHROME_PATH`).

Um arquivo simples:

```markdown
---
marp: true
theme: research
paginate: true
---

# Título

Conteúdo.

---

## Próximo slide

Mais conteúdo.
```

pode ser exportado para formatos de apresentação.

Documentação:

https://marp.app/

## Pandoc como interoperabilidade

Pandoc pode converter Markdown para diversos formatos.

Exemplo:

```bash
pandoc documento.md -o documento.docx
```

Ele é tratado aqui como uma ferramenta de interoperabilidade e fallback, não como a interface que todo iniciante precisa aprender.

Documentação:

https://pandoc.org/

## Portabilidade não significa identidade perfeita

Nem todo recurso avançado de um renderer possui equivalente direto em outro.

A decisão Markdown-first busca preservar o **conteúdo e a legibilidade**, não prometer que um PDF, um DOCX e um deck terão comportamento idêntico em todos os backends.
