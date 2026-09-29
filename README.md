# Workflow de Pesquisa Computacional

Uma introdução leve a conceitos e práticas básicas de pesquisa computacional, pensada para alunos de iniciação científica e para apoiar projetos científicos mais organizados e eficientes.

Este repositório é uma implementação de referência: mostra um caminho pequeno para separar dados, código, resultados e documentação, sem exigir uma formação prévia em desenvolvimento de software.

> “A boring research workflow is a good research workflow” é uma possível chamada editorial para uma futura postagem no Medium. Não é o nome nem a identidade principal do projeto.

## Comece pelo exemplo

O [`mini-projeto`](examples/mini-project/README.md) já está completo e executável. Ele mostra o percurso que este repositório recomenda:

```text
data pública/sintética
      ↓
código, modelo ou simulador
      ↓
resultados persistidos
      ↓
Markdown
      ↓
documento ou apresentação
```

Depois, siga o caminho curto:

1. leia [`docs/quickstart.md`](docs/quickstart.md);
2. execute o mini-projeto;
3. use [`docs/git-basics.md`](docs/git-basics.md) se Git ainda for novo;
4. consulte os extras somente quando surgir uma necessidade concreta.

## Por que isto existe

Muitas práticas simples de desenvolvimento aparecem tarde para quem começa uma iniciação científica: versionamento, organização, documentação e rastreabilidade. O custo costuma surgir meses depois, em scripts duplicados, arquivos chamados `final`, `final2` e `final_agora`, figuras sem origem clara e projetos difíceis de retomar.

Este projeto reúne um conjunto pequeno de práticas já discutidas na literatura e em iniciativas de ensino. Não pretende reinventá-las. As referências incluem:

- Wilson et al. (2017), *Good enough practices in scientific computing*;
- *The Turing Way*, especialmente a ideia de *research compendium*;
- Software Carpentry, para introdução prática a Git;
- iniciativas brasileiras como o **Kit de sobrevivência digital para cientistas**, do CompGeoLab/IAG-USP.

Veja [`docs/references.md`](docs/references.md).

## O que este projeto propõe

O núcleo pode ser resumido em:

```text
dados/entradas
      ↓
código, modelo ou simulador
      ↓
resultados persistidos
      ↓
documentação e comunicação em Markdown
```

E em algumas convenções:

- arquivos humanos principais permanecem em **Markdown `.md`**;
- resultados devem, quando possível, ser regeneráveis a partir do código ou ter sua origem documentada;
- Git entra cedo, mas apenas no nível necessário para começar;
- dados restritos ou protegidos ficam fora do projeto de desenvolvimento;
- ferramentas avançadas são apresentadas quando resolvem um problema real, não como pré-requisito;
- o próprio repositório deve demonstrar o workflow que recomenda.

## Markdown é a fonte; renderizadores são ferramentas

O projeto não adota um formato proprietário de autoria.

```text
                    arquivos .md
                         │
            ┌────────────┼────────────┐
            │            │            │
          MyST          Marp        Pandoc
            │            │            │
      docs científicos  slides   interoperabilidade
```

A implementação de referência usa:

- **MyST** para documentos científicos e documentação;
- **Marp** para apresentações;
- **Pandoc** como conversor e rota de interoperabilidade.

Essas ferramentas **não definem a identidade do projeto**. O contrato principal é manter o conteúdo humano em `.md`.

## Estrutura deste repositório

```text
.
├── README.md
├── myst.yml
├── references.bib
├── docs/
│   ├── quickstart.md
│   ├── markdown-rendering.md
│   ├── git-basics.md
│   ├── references.md
│   ├── decisions/
│   │   └── ADR-0001-markdown-first-research-workflow.md
│   └── extras/
│       └── tooling-landscape.md
├── styles/
│   └── marp/
│       └── research.css
└── examples/
    └── mini-project/
```

## Exemplo vivo

[`examples/mini-project/README.md`](examples/mini-project/README.md) demonstra uma pequena pesquisa sintética:

```text
data/sample.csv
      ↓
src/analyze.py
      ↓
results/tables/summary.csv
results/tables/summary.md
results/figures/comparison.svg
      ↓
docs/report.md
```

O exemplo usa Python apenas por conveniência. O protocolo não é Python-first: o mesmo papel poderia ser exercido por MATLAB, C++, Julia, R, um simulador numérico ou outro software científico.

## Renderização

Para construir o site local e reportar links quebrados:

```bash
npx --yes mystmd@latest build --site --strict
```

Para exportar o documento do mini-projeto:

```bash
npx --yes mystmd@latest build examples/mini-project/docs/report.md --pdf --docx --strict
```

A exportação PDF requer uma instalação local de LaTeX ou Typst. A exportação DOCX não depende desse requisito.

Slides podem continuar como Markdown comum com frontmatter Marp:

```bash
npx --yes @marp-team/marp-cli@latest \
  --theme-set styles/marp/research.css \
  --pdf \
  --output exports/slides-example.pdf \
  docs/slides-example.md
```

A exportação PDF do Marp requer Chrome, Chromium, Edge ou Firefox disponível no sistema (ou indicado por `CHROME_PATH`).

Pandoc permanece disponível quando um caso de interoperabilidade justificar:

```bash
pandoc docs/quickstart.md -o quickstart.docx
```

Veja [`docs/markdown-rendering.md`](docs/markdown-rendering.md).

## Dados protegidos

Nem todo dado de pesquisa pertence ao projeto de desenvolvimento.

Quando os dados forem proprietários, pessoais, confidenciais ou protegidos por contrato, uma organização simples pode ser:

```text
workspace/
├── research-project/
└── protected-data/
```

O projeto contém código, documentação e resultados que podem ser mantidos com segurança. Os dados protegidos permanecem no armazenamento autorizado e são acessados apenas quando necessário.

Sempre que possível, exemplos e testes devem usar dados públicos ou sintéticos.

## O que este projeto não pretende ser

Este repositório não pretende:

- criar um novo formato de documento;
- transformar um aluno de IC em engenheiro de software;
- impor uma estrutura grande de pastas;
- exigir CI, containers, DVC, Snakemake ou outras ferramentas avançadas;
- criar uma nova biblioteca de gráficos;
- substituir MyST, Marp, Pandoc, Git ou ferramentas científicas existentes.

A regra é deliberadamente simples:

> **Uma recomendação deve resolver um problema provável antes de introduzir um novo conceito.**

## Decisão arquitetural

A decisão Markdown-first, os limites do escopo e as alternativas consideradas estão registrados em [`docs/decisions/ADR-0001-markdown-first-research-workflow.md`](docs/decisions/ADR-0001-markdown-first-research-workflow.md).
