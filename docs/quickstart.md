# Começando um projeto

Use este guia quando estiver iniciando uma pesquisa computacional e quiser montar um primeiro ciclo de trabalho.

## 1. Crie uma estrutura mínima

```text
meu-projeto/
├── README.md
├── data/
├── src/
├── results/
└── docs/
```

- `data/`: entradas que podem ficar no repositório.
- `src/`: scripts, modelos ou arquivos do simulador.
- `results/`: tabelas e figuras produzidas pela análise.
- `docs/`: relatório, notas e apresentação.
- `README.md`: o que o projeto investiga, como executar a análise e onde estão os resultados.

Adapte os nomes se o seu domínio pedir outra organização. O importante é conseguir localizar entradas, método, resultados e comunicação.

## 2. Faça o primeiro ciclo

1. Coloque um conjunto pequeno de dados ou uma entrada sintética em `data/`.
2. Escreva ou adapte o código em `src/`.
3. Execute a análise e salve as tabelas e figuras em `results/`.
4. Use os arquivos de `results/` no relatório ou apresentação em `docs/`.
5. Atualize o `README.md` com o comando principal.

Evite copiar uma tabela para o relatório e depois manter duas versões. Se o código gera a tabela, salve-a em `results/` e use esse arquivo no documento.

## 3. Registre o histórico

Use Git desde o começo. Você não precisa aprender tudo agora; comece por:

```bash
git status
git diff
git add <arquivo>
git commit -m "descreva brevemente a mudança"
git log
```

Veja [Git: o mínimo para começar](git-basics.md).

## 4. Escreva enquanto trabalha

Registre decisões, hipóteses, comandos importantes e resultados próximos do trabalho. Um arquivo `.md` em `docs/` já resolve muito. Quando precisar entregar um relatório ou uma apresentação, veja [Markdown e renderização](markdown-rendering.md).

## 5. Separe dados protegidos

Dados restritos podem ficar fora do projeto:

```text
workspace/
├── meu-projeto/
└── dados-protegidos/
```

O código recebe o caminho autorizado durante a execução. Exemplos, testes e documentação podem usar dados públicos ou sintéticos. Resultados derivados também podem estar sujeitos às restrições da fonte.

## Quando surgir um problema maior

- Se você não souber mais a ordem de execução dos scripts, conheça Make ou Snakemake.
- Se os dados ficarem grandes demais para o fluxo normal de Git, conheça DVC, Git LFS ou soluções institucionais.
- Se precisar de um paper computacional totalmente reconstruível, conheça showyourwork!.

Os links e um pouco de contexto ficam em [ferramentas e caminhos para explorar](extras/tooling-landscape.md).
