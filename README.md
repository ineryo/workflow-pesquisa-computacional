# Workflow científico computacional leve

> **Nome do projeto: ainda em aberto.**
>
> “A boring research workflow is a good research workflow” é uma possível chamada editorial para uma futura postagem no Medium, não o nome definido deste repositório.

Este repositório é uma **implementação de referência** para começar projetos de pesquisa computacional de forma simples, legível e rastreável.

Ele foi pensado especialmente para alunos e pesquisadores de engenharia e outras ciências que usam programação como **meio para investigar um problema científico**, e não necessariamente como área principal de formação.

## Por que isto existe

Muitas práticas elementares de desenvolvimento acabam sendo tratadas como conhecimento implícito em ambientes de inovação tecnológica. Para quem está entrando em iniciação científica, isso pode significar descobrir tarde demais conceitos simples de versionamento, organização, documentação e rastreabilidade.

O custo aparece meses ou anos depois: scripts duplicados, arquivos chamados `final`, `final2` e `final_agora`, figuras cuja origem já não é clara e projetos antigos que nem o próprio autor consegue reconstruir com confiança.

A motivação deste projeto é simples: **este é o tipo de ponto de partida que gostaríamos de ter recebido no início da pesquisa computacional**.

A literatura já discute amplamente práticas de pesquisa computacional reprodutível. Este projeto não tenta reinventá-las. Ele seleciona um conjunto pequeno e aplicável desde cedo, apoiando-se em referências como:

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

O caminho principal é curto:

1. leia este `README`;
2. veja [`docs/quickstart.md`](docs/quickstart.md);
3. use [`docs/git-basics.md`](docs/git-basics.md) apenas se Git ainda for novo;
4. consulte os extras somente quando surgir necessidade.

## Exemplo vivo

[`examples/mini-project`](examples/mini-project/) demonstra uma pequena pesquisa sintética:

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

Com MyST instalado:

```bash
myst start
```

Para exportar um documento específico:

```bash
myst build examples/mini-project/docs/report.md --pdf
```

Slides podem continuar como Markdown comum com frontmatter Marp:

```bash
npx @marp-team/marp-cli@latest \
  --theme-set styles/marp \
  docs/slides-example.md \
  --pdf
```

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

## Status

A arquitetura inicial está registrada em:

[`docs/decisions/ADR-0001-markdown-first-research-workflow.md`](docs/decisions/ADR-0001-markdown-first-research-workflow.md)

O nome definitivo do projeto e targets institucionais específicos permanecem em aberto.
