# Workflow de Pesquisa Computacional

Um ponto de partida leve para alunos e pesquisadores que usam programação para investigar problemas científicos. O objetivo é ajudar você a organizar dados, código, resultados e documentos desde o começo, sem exigir formação prévia em desenvolvimento de software.

Muitas dificuldades aparecem tarde: scripts duplicados, arquivos chamados `final2`, figuras sem origem clara e análises difíceis de retomar. Algumas práticas simples evitam boa parte desse trabalho.

## Comece pelo mini-projeto

O [mini-projeto executável](examples/mini-project/README.md) mostra uma análise sintética completa:

```text
dados
  ↓
código ou modelo
  ↓
resultados persistidos
  ↓
relatório e apresentação
```

1. Abra [`examples/mini-project/README.md`](examples/mini-project/README.md).
2. Execute o comando indicado.
3. Veja os arquivos produzidos em `results/`.
4. Abra o relatório em Markdown em `docs/report.md`.

## Uma estrutura pequena

Comece separando as partes do trabalho:

```text
meu-projeto/
├── README.md       # o que é o projeto e como executá-lo
├── data/           # entradas apropriadas para o repositório
├── src/            # código, modelos ou scripts
├── results/        # tabelas e figuras produzidas
└── docs/           # relatórios, notas e apresentações
```

A estrutura não é uma regra rígida. Ela só ajuda a localizar cada coisa quando o projeto cresce.

- Guarde dados ou entradas em `data/` quando puderem ser versionados e compartilhados.
- Execute o código em `src/` para gerar tabelas e figuras em `results/`.
- Use esses resultados em relatórios e apresentações em `docs/`.
- Registre no `README.md` como executar a análise principal e onde encontrar os resultados.

## Poucas práticas para começar

- Use Git cedo para preservar o histórico sem criar várias cópias do mesmo arquivo. Veja [Git: o mínimo para começar](docs/git-basics.md).
- Escreva relatórios e slides em Markdown `.md`. Você pode lê-los como texto e renderizá-los quando precisar compartilhar. Veja [Markdown e renderização](docs/markdown-rendering.md).
- Gere tabelas e figuras a partir do código sempre que possível. Se não for possível, registre a origem.
- Introduza novas ferramentas só quando aparecer um problema concreto. Os nomes e caminhos ficam em [ferramentas opcionais](docs/extras/tooling-landscape.md).

## Markdown para comunicar resultados

O mesmo conteúdo em `.md` pode servir a mais de uma forma de comunicação:

- use [MyST](https://mystmd.org/) para visualizar o site ou gerar documentos;
- use [Marp](https://marp.app/) para gerar slides a partir de Markdown;
- recorra ao [Pandoc](https://pandoc.org/) quando precisar converter um documento para outro formato.

Os comandos e requisitos de cada rota estão em [Markdown e renderização](docs/markdown-rendering.md).

## Dados protegidos

Dados proprietários, pessoais, confidenciais ou sujeitos a contrato devem ficar em armazenamento autorizado separado do projeto de desenvolvimento. Resultados derivados também podem ter restrições.

```text
workspace/
├── research-project/
└── protected-data/
```

Mantenha no repositório apenas dados, código, documentação e resultados apropriados para versionamento e compartilhamento. Para exemplos e testes, prefira dados públicos ou sintéticos.

## Para aprofundar

- [Começando um projeto](docs/quickstart.md): primeiro ciclo de trabalho.
- [Git: o mínimo para começar](docs/git-basics.md): histórico de versões sem transformar o arquivo em `final3`.
- [Markdown e renderização](docs/markdown-rendering.md): site, documento e slides.
- [Referências e caminhos de estudo](docs/references.md): fontes e materiais de aprofundamento.
- [Ferramentas e caminhos para explorar](docs/extras/tooling-landscape.md): opções para problemas que apareçam mais tarde.

As práticas deste repositório se apoiam em trabalhos como *Good Enough Practices in Scientific Computing*, *The Turing Way*, Software Carpentry e o [Kit de sobrevivência digital para cientistas](https://github.com/compgeolab/kit), do CompGeoLab/IAG-USP. Veja as referências completas em [docs/references.md](docs/references.md).

As decisões de manutenção, limites do escopo e alternativas consideradas estão no [ADR-0001](docs/decisions/ADR-0001-markdown-first-research-workflow.md).
