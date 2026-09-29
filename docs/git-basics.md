# Git: o mínimo para começar

Git mantém o histórico de mudanças do projeto.

Para um aluno começando, isso já resolve um problema importante: **a versão não precisa morar no nome do arquivo**.

Em vez de:

```text
analise.py
analise_nova.py
analise_final.py
analise_final2.py
```

um único `analise.py` pode evoluir ao longo do histórico.

## Comandos suficientes para o primeiro contato

```bash
git status
git diff
git add <arquivo>
git commit -m "descreva brevemente a mudança"
git log
```

Se o projeto usa um repositório remoto, também aparecerão:

```bash
git pull
git push
```

Não é necessário dominar branches, rebases, hooks ou outros recursos avançados para começar a se beneficiar de controle de versão.

## Marcos importantes

Uma pesquisa raramente tem um único “final”. Há estados importantes:

- resultado apresentado em reunião;
- resumo submetido;
- artigo submetido;
- versão usada em uma defesa.

Git permite marcar estados relevantes do histórico. Esse recurso pode ser aprendido quando surgir a necessidade.

## Aprenda pela referência certa

Este projeto não pretende substituir bons cursos de Git.

Recomendação principal:

- **Software Carpentry — Version Control with Git**
  https://swcarpentry.github.io/git-novice/

Para entender por que versionamento importa especificamente em pesquisa:

- **The Turing Way — Version Control**
  https://book.the-turing-way.org/reproducible-research/vcs/
