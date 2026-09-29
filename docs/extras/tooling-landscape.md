# Ferramentas e caminhos para explorar

Esta página não é um checklist de ferramentas a dominar.

Ela existe para que, quando um problema aparecer, o aluno reconheça alguns nomes e saiba por onde começar a procurar.

## Escrita e publicação

### MyST

Documentos científicos baseados em Markdown, referências cruzadas, equações e exportação para diferentes formatos.

https://mystmd.org/

### Quarto

Ecossistema amplo de publicação científica e técnica, especialmente útil em workflows que combinam execução computacional e documentos.

https://quarto.org/

### Pandoc

Conversor universal de documentos e base de muitos outros sistemas de publicação.

https://pandoc.org/

### Marp

Apresentações baseadas em Markdown.

https://marp.app/

### Manubot

Workflow colaborativo para manuscritos científicos com Markdown, Git e automação.

https://manubot.org/

## Automação e reprodutibilidade

### Make

Útil quando um conjunto pequeno de comandos já possui dependências claras.

### Snakemake

Workflow engine para pipelines científicos mais complexos.

https://snakemake.readthedocs.io/

### showyourwork!

Workflow para artigos científicos computacionais reproduzíveis, integrando paper, scripts, figuras e dependências.

https://show-your.work/

### DVC

Versionamento e pipelines voltados a dados e experimentos.

https://dvc.org/

## Notebooks

### Jupyter

Excelente para exploração, estudo e prototipagem.

### Jupytext

Permite representar notebooks também em formatos textuais, o que pode ajudar em versionamento e revisão.

https://jupytext.readthedocs.io/

## Visualização

### Matplotlib

Base consolidada para figuras científicas estáticas em Python.

https://matplotlib.org/

### Plotly

Visualização interativa e exportação para HTML, além de imagens estáticas.

https://plotly.com/python/

### Altair / Vega-Lite

Abordagem declarativa para visualização.

https://altair-viz.github.io/

### ParaView e PyVista

Opções relevantes para meshes, elementos finitos, CFD e visualização 3D científica.

## Sincronização de artefatos

### Markdown Artifact Updater (MAU)

Ferramenta experimental para atualizar regiões explícitas de documentos Markdown/Marp a partir de código e artefatos externos.

Pode ser útil quando decks ou documentos ficam repetidamente desatualizados em relação aos resultados.

Não faz parte do núcleo deste projeto. O desenvolvimento adicional deve ser justificado por casos reais não atendidos satisfatoriamente por ferramentas existentes.

## Como escolher

Evite escolher ferramentas por popularidade ou completude.

Uma heurística melhor é:

```text
problema percebido
      ↓
solução mais simples suficiente
      ↓
ferramenta adicional somente se necessário
```
