# Começando um projeto

Esta página apresenta apenas o necessário para começar.

Uma estrutura inicial pode ser:

```text
meu-projeto/
├── README.md
├── data/
├── src/
├── results/
└── docs/
```

Ela não é uma taxonomia obrigatória. A ideia é apenas separar, de forma previsível:

- **entradas**;
- **métodos/código**;
- **resultados produzidos**;
- **documentação e comunicação**.

Essa separação é compatível com a ideia de *research compendium* discutida pelo *Turing Way* e com recomendações de organização apresentadas por Wilson et al. (2017).

## Um fluxo simples

```text
data/
  ↓
src/
  ↓
results/
  ↓
docs/
```

Se um script ou simulador produz uma tabela ou figura, prefira salvar esse resultado em `results/` e fazer o documento consumi-lo, em vez de manter cópias independentes espalhadas.

## README

O `README.md` deve responder, pelo menos:

- o que é este projeto;
- por onde começar;
- como executar a análise principal;
- onde estão os resultados.

Ele serve tanto para colaboradores quanto para você mesmo no futuro.

## Git

Use Git desde o começo para manter histórico de mudanças.

O objetivo inicial não é dominar Git. É deixar de depender de nomes como:

```text
modelo_final.py
modelo_final2.py
modelo_final_corrigido.py
```

Veja [`git-basics.md`](git-basics.md).

## Dados protegidos

Dados restritos ou protegidos podem ficar fora do projeto:

```text
workspace/
├── meu-projeto/
└── dados-protegidos/
```

O código pode receber a localização dos dados durante a execução.

O projeto pode usar dados públicos ou sintéticos em exemplos, documentação e testes.

Dados derivados também podem continuar sujeitos às mesmas restrições da fonte original; isso deve ser avaliado no contexto do projeto.

## Resultados e figuras

Quando possível:

- gere resultados a partir do código;
- mantenha a origem de uma figura reconhecível;
- use formatos vetoriais para gráficos quando forem adequados;
- use HTML quando a interatividade realmente agregar valor.

Para aprofundar visualização científica, veja as referências em [`references.md`](references.md).

## Quando complicar?

Somente quando surgir uma necessidade concreta.

Exemplos:

```text
“Não sei mais qual script executar primeiro.”
→ procure Make ou Snakemake.

“Meus dados são grandes demais para o fluxo normal de Git.”
→ procure DVC, Git LFS ou soluções institucionais.

“Quero um paper computacional totalmente reconstruível.”
→ conheça showyourwork!.

“Meu deck Marp vive ficando desatualizado.”
→ conheça sincronização de artefatos e MAU.
```

Essas ferramentas existem. Você não precisa aprendê-las antes de precisar delas.
