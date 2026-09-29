# Ferramentas e caminhos para explorar

Esta página é opcional. Use-a quando um problema aparecer; você não precisa aprender estas ferramentas antes de começar.

## Preciso gerar um artigo, relatório ou outro formato

- **MyST** trabalha com documentos científicos em Markdown, referências, equações e exports. Veja <https://mystmd.org/>.
- **Quarto** é uma opção de publicação científica e técnica, especialmente em trabalhos que combinam execução e documento. Veja <https://quarto.org/>.
- **Pandoc** converte documentos entre formatos. Veja <https://pandoc.org/>.
- **Manubot** ajuda a manter manuscritos científicos colaborativos com Markdown, Git e automação. Veja <https://manubot.org/>.

Comece com a ferramenta que já resolve o seu caso. Você não precisa adotar um sistema completo para escrever o primeiro relatório.

## Minha execução virou um pipeline difícil de repetir

- **Make** ajuda quando poucos comandos já têm dependências claras.
- **Snakemake** organiza pipelines científicos mais extensos. Veja <https://snakemake.readthedocs.io/>.
- **showyourwork!** é voltado a artigos computacionais que precisam reconstruir paper, scripts, figuras e dependências. Veja <https://show-your.work/>.

Olhe para essas opções quando a ordem dos scripts ou a repetição do pipeline começar a causar erros.

## Meus dados ficaram grandes demais para o fluxo normal de Git

- **DVC** oferece versionamento e pipelines voltados a dados e experimentos. Veja <https://dvc.org/>.
- **Git LFS** e soluções institucionais também podem ser adequados, conforme o tamanho dos dados e as restrições de acesso.

Dados protegidos exigem armazenamento autorizado, independentemente da ferramenta de versionamento escolhida.

## Quero explorar dados em notebook

- **Jupyter** é útil para exploração, estudo e prototipagem.
- **Jupytext** representa notebooks também em formatos textuais, o que pode facilitar revisão e versionamento. Veja <https://jupytext.readthedocs.io/>.

Use notebooks para explorar. Quando um resultado precisar ser reproduzido, deixe claro qual código e quais entradas o produzem.

## Quero figuras interativas ou visualização especializada

- **Matplotlib** é uma base consolidada para figuras científicas estáticas em Python. Veja <https://matplotlib.org/>.
- **Plotly** permite gráficos interativos e exportação para HTML. Veja <https://plotly.com/python/>.
- **Altair / Vega-Lite** oferece visualização declarativa. Veja <https://altair-viz.github.io/>.
- **ParaView** e **PyVista** são opções para meshes, elementos finitos, CFD e visualização 3D. Veja <https://www.paraview.org/> e <https://pyvista.org/>.

Interatividade vale a pena quando ajuda a responder uma pergunta; uma figura estática costuma bastar para comunicar um resultado estável.

## Meu relatório e meus slides vivem desatualizados

Primeiro, mantenha tabelas e figuras como artefatos produzidos pelo código e reutilize-os nos documentos. Se isso não resolver um problema recorrente, conheça o Markdown Artifact Updater (MAU), uma ferramenta experimental para atualizar regiões explícitas de documentos Markdown ou Marp a partir de artefatos externos.

O MAU não é necessário no começo. Avalie-o apenas quando uma necessidade real não for atendida por uma solução simples.
