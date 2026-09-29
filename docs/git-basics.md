# Git: o mínimo para começar

Git guarda o histórico de mudanças do projeto. Assim, a versão não precisa morar no nome do arquivo.

Em vez de:

```text
analise.py
analise_nova.py
analise_final.py
analise_final2.py
```

mantenha um único `analise.py` e registre as mudanças no histórico.

## Primeiro uso

Se você está começando um projeto próprio, entre na pasta dele e crie o repositório uma vez:

```bash
git init
```

Depois, use:

```bash
git status
git diff
git add <arquivo>
git commit -m "descreva brevemente a mudança"
git log
```

- `git status` mostra o que mudou.
- `git diff` mostra as alterações antes do registro.
- `git add` escolhe os arquivos que entram no próximo registro.
- `git commit` salva um ponto do histórico com uma mensagem curta.
- `git log` mostra os registros anteriores.

Se você usar um repositório remoto, também verá `git pull` e `git push`.

## Registre marcos reais

Uma pesquisa pode ter versões usadas em reunião, em um resumo submetido, em um artigo ou em uma defesa. Faça um commit quando uma mudança tiver um propósito claro. Você pode aprender a marcar versões formais quando precisar disso.

## Continue aprendendo

- [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/) oferece um tutorial prático para pesquisadores.
- [The Turing Way: Version Control](https://book.the-turing-way.org/reproducible-research/vcs/) explica por que o versionamento é útil em pesquisa.
