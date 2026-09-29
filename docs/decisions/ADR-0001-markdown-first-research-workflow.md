# ADR-0001 — Workflow científico Markdown-first

- **Status:** Aceito para a arquitetura inicial
- **Data:** 2026-09-28
- **Escopo:** estrutura do projeto de referência e princípios de onboarding
- **Nome do projeto:** Workflow de Pesquisa Computacional

## Contexto

Pesquisadores e alunos de iniciação científica frequentemente passam a depender de programação para resolver problemas de engenharia e outras ciências sem que desenvolvimento de software seja sua área principal.

Nesse contexto, práticas elementares de organização e rastreabilidade podem ser tratadas como conhecimento implícito e só serem descobertas depois que o projeto já acumulou:

- múltiplas cópias de scripts;
- arquivos chamados “final” em várias versões;
- resultados cuja origem é difícil de reconstruir;
- apresentações e relatórios que divergem do estado do código;
- dificuldade para retomar projetos antigos.

Esse problema não é novo. Wilson et al. (2017), *The Turing Way*, Software Carpentry e iniciativas brasileiras como o **Kit de sobrevivência digital para cientistas** já oferecem boas práticas, cursos e referências relevantes.

O gap que este projeto pretende ocupar é mais específico: oferecer um **starter/reference repository pequeno, em português brasileiro, independente de linguagem de programação, que aplique algumas dessas práticas desde o primeiro dia sem exigir que o aluno estude uma stack de engenharia de software antes de começar a pesquisa**.

## Forças de projeto

As decisões devem equilibrar:

1. baixa barreira de entrada;
2. rastreabilidade suficiente para evitar os erros mais caros;
3. independência de linguagem e domínio científico;
4. portabilidade do conteúdo;
5. proteção de dados restritos;
6. possibilidade de crescimento para workflows avançados;
7. reutilização de ferramentas existentes em vez de criação de infraestrutura própria.

## Decisão

### 1. Markdown `.md` é a fonte humana canônica

Arquivos humanos de documentação, relatórios e apresentações devem permanecer em `.md` sempre que razoável.

Motivações:

- formato textual simples;
- leitura direta sem renderer;
- histórico e revisão por diff;
- compatibilidade com diversos editores e plataformas;
- menor acoplamento a uma ferramenta de publicação.

A arquitetura não exige que todos os documentos sejam Markdown puro sem extensões. Recursos específicos de renderizadores podem ser usados progressivamente quando agregarem valor, mantendo `.md` como arquivo de origem.

### 2. Renderer e formato canônico são conceitos separados

O projeto não será definido por MyST, Marp, Pandoc ou outro renderer.

A implementação de referência adota:

- **MyST** para documentos científicos e long-form;
- **Marp** para apresentações;
- **Pandoc** para interoperabilidade e fallback.

Essas escolhas podem mudar futuramente sem alterar o princípio Markdown-first.

### 3. MyST é backend recomendado, não identidade do projeto

Foi considerada a possibilidade de estruturar o projeto diretamente em torno do ecossistema MyST.

Essa alternativa **não é adotada como requisito arquitetural**.

MyST permanece como implementação de referência recomendada porque trabalha diretamente com `.md` e oferece recursos úteis de publicação científica. Entretanto, o protocolo não deve depender de MyST para definir a estrutura ou a identidade do conteúdo.

Recursos específicos de MyST podem ser introduzidos progressivamente quando necessários.

### 4. O repositório deve ser um exemplo vivo

A documentação e os exemplos devem usar as práticas recomendadas.

O scaffold inclui:

- documentos `.md`;
- configuração MyST separada;
- deck Marp real em `.md`;
- estilo Marp simples separado do conteúdo;
- mini-projeto executável;
- resultados persistidos;
- referências e decisões versionadas.

O repositório deve demonstrar o workflow em vez de apenas descrevê-lo.

### 5. A estrutura inicial é mínima e expansível

Estrutura recomendada para projetos de pesquisa:

```text
project/
├── README.md
├── data/
├── src/
├── results/
└── docs/
```

Essa estrutura é uma convenção de partida, não uma taxonomia rígida.

Novas pastas e ferramentas surgem conforme necessidades reais.

### 6. Git entra cedo, mas o onboarding é pequeno

O projeto recomenda Git desde o início porque histórico de mudanças elimina grande parte da necessidade de múltiplas cópias “final”.

O onboarding não exige domínio completo de Git.

Conceitos avançados ficam em referências ou material opcional.

### 7. Dados restritos podem ficar fora do projeto de desenvolvimento

Dados proprietários, pessoais, confidenciais ou protegidos por contrato podem e frequentemente devem permanecer em armazenamento separado e autorizado.

Exemplo:

```text
workspace/
├── research-project/
└── protected-data/
```

O código acessa os dados quando necessário.

O projeto de referência deve funcionar com dados públicos ou sintéticos, permitindo documentação, testes e automação sem acesso à fonte protegida.

Não se presume que resultados derivados sejam automaticamente públicos; as restrições do projeto devem ser respeitadas.

### 8. Resultados persistidos fazem a ponte entre computação e comunicação

O padrão recomendado é:

```text
entrada → computação → resultados persistidos → comunicação
```

A computação pode ser Python, MATLAB, C++, Julia, R, simuladores ou outra ferramenta.

A comunicação não deve depender de a análise estar embutida no documento.

### 9. Visualização recebe referências e poucos exemplos

O projeto não criará inicialmente uma biblioteca própria de plotting.

A documentação deve apresentar poucas recomendações práticas e apontar para referências consolidadas.

Exemplos podem mostrar:

- figura vetorial estática;
- HTML interativo;
- ferramentas como Matplotlib e Plotly.

### 10. Progressive disclosure é regra editorial

O manual principal não deve se tornar um catálogo de “boas práticas a dominar antes de pesquisar”.

Uma recomendação deve entrar no onboarding quando:

1. previne um erro comum e caro;
2. é útil já nas primeiras semanas;
3. pode ser explicada sem introduzir infraestrutura desnecessária.

Ferramentas e práticas avançadas aparecem em material opcional, preferencialmente organizadas pelo problema que resolvem.

### 11. Preferir adoção e contribuição a software novo

Antes de implementar:

1. buscar projeto mantido existente;
2. avaliar configuração/template/extensão;
3. avaliar contribuição upstream;
4. criar código próprio somente quando o gap estiver demonstrado.

A ausência de software novo é um resultado arquitetural válido.

### 12. MAU não faz parte do núcleo

O Markdown Artifact Updater pode continuar como ferramenta experimental ou opção para workflows Marp/Markdown que sofram com sincronização de artefatos.

Ele não será expandido ou incorporado ao core por inércia.

Novo desenvolvimento precisa ser sustentado por casos reais não resolvidos adequadamente por soluções existentes.

## Não objetivos

Este projeto não pretende:

- criar um novo formato de documento;
- substituir Git;
- substituir MyST, Marp ou Pandoc;
- criar um workflow engine;
- impor uma estrutura rígida de pastas;
- ser específico de Python;
- ensinar engenharia de software completa;
- exigir CI, containers, DVC ou Snakemake;
- criar uma framework de visualização;
- resolver sozinho governança institucional de dados protegidos.

## Alternativas consideradas

### Quarto como núcleo

Quarto oferece excelente infraestrutura de publicação e formatos institucionais.

Não foi escolhido como base canônica porque o caminho completo do ecossistema utiliza `.qmd`, enquanto este projeto prioriza `.md` como contrato humano estável.

Quarto permanece uma alternativa relevante em `docs/extras/`.

### Pandoc puro como interface principal

Pandoc é extremamente flexível, mas expõe mais detalhes de conversão, templates e filtros do que o necessário para o onboarding.

Permanece como infraestrutura/fallback.

### MyST como camada central de autoria

Não adotado como requisito arquitetural.

MyST é backend recomendado, não o formato ou a identidade do projeto.

### MAU como sincronizador central

Não adotado.

O valor precisa ser demonstrado por um problema recorrente que não seja melhor resolvido por ferramentas existentes.

### Framework próprio de artefatos científicos

Não adotado.

O projeto prefere composição de ferramentas existentes e convenções simples.

## Prior art e relação com projetos existentes

### Good enough practices in scientific computing

Wilson et al. (2017) é a principal base conceitual geral. O artigo se dirige justamente a pesquisadores que dependem de computação sem necessariamente terem formação formal equivalente em práticas de software e dados.

### The Turing Way

A ideia de *research compendium* fornece um enquadramento direto para organizar dados, métodos, textos e outputs de pesquisa.

### Software Carpentry

Serve como referência de ensino de Git e outras habilidades computacionais para pesquisadores.

### Kit de sobrevivência digital para cientistas — CompGeoLab/IAG-USP

É um prior art brasileiro especialmente relevante.

O curso cobre Bash, Git/GitHub, Make, LaTeX e ciência aberta, com foco em cientistas que trabalham com dados e precisam de workflows documentados e reproduzíveis.

Este projeto não pretende substituí-lo. O escopo é diferente:

- o Kit é um curso de ferramentas;
- este projeto busca ser um starter/reference repository pequeno, utilizável desde o primeiro projeto;
- o Kit ensina Make e LaTeX como parte central do workflow;
- aqui, automação avançada é opcional e Markdown `.md` é a fonte humana canônica.

## Consequências

### Positivas

- baixa barreira de entrada;
- arquivos humanos simples e portáveis;
- possibilidade de trocar renderizadores;
- melhor adequação a alunos que usam computação como ferramenta;
- exemplos podem servir diretamente para onboarding;
- reduz risco de inventar infraestrutura que já existe.

### Custos e limitações

- recursos avançados podem ter portabilidade imperfeita entre renderizadores;
- targets institucionais exigirão manutenção específica;
- reprodutibilidade completa de ambientes e dados está fora do núcleo;
- a qualidade do projeto depende fortemente de documentação editorialmente enxuta;
- manter `.md` como fonte pode exigir compromissos em ferramentas cuja experiência principal usa outra extensão.

## Critérios de sucesso

A implementação inicial será considerada bem-sucedida se um aluno conseguir, sem estudar uma stack extensa:

1. compreender a estrutura recomendada;
2. executar o mini-projeto;
3. reconhecer de onde vêm os resultados;
4. entender por que Git substitui cópias “final”;
5. editar um `.md` e gerar ao menos um output renderizado;
6. reconhecer como dados protegidos podem permanecer fora do projeto;
7. encontrar caminhos de aprofundamento sem que eles pareçam pré-requisitos.

## Decisões ainda abertas

- nome definitivo do projeto;
- forma de distribuição: template, starter repository ou pacote complementar;
- identidade visual padrão;
- primeiro target institucional a ser implementado;
- necessidade real de qualquer camada adicional de sincronização de artefatos.

## Próximos passos

A implementação deve seguir `AGENTS.md`.

Antes de adicionar features, validar o scaffold existente e o fluxo Markdown → output em ambiente real.
