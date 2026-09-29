# Como contribuir

Contribua com casos que você realmente usaria ou já utilizou. O objetivo é manter um caminho inicial simples para alunos e pesquisadores que usam código, modelos ou simulações.

As contribuições mais úteis tendem a ser novos exemplos e novos estilos ou targets. Mudanças no núcleo também são bem-vindas quando resolvem um problema observado.

## Novos exemplos

`examples/` pode reunir exemplos pequenos e autocontidos de diferentes domínios e linguagens. Um bom exemplo:

- parte de um caso real ou plausível;
- é compreensível isoladamente;
- executa ou informa claramente seus requisitos;
- não inclui dados restritos;
- mostra uma prática útil sem tentar mostrar tudo de uma vez.

Use a estrutura que fizer sentido. Como referência, um exemplo pode conter:

```text
examples/<nome>/
├── README.md
├── data/
├── src/
├── results/
└── docs/
```

Não é necessário criar todas essas pastas quando elas não ajudam o caso.

## Novos estilos ou targets

Contribua com um estilo ou target quando houver uma necessidade concreta de comunicação ou publicação. Antes de abrir a contribuição:

- use uma fonte ou template oficial quando houver;
- confirme a licença e registre ano ou versão quando isso importar;
- mantenha conteúdo científico e apresentação separados;
- documente requisitos específicos do renderer;
- inclua um exemplo mínimo que possa ser renderizado.

Não reproduza templates oficiais apenas de memória.

## Mudanças no núcleo

Prefira mudanças que resolvam um problema observado, preservem a baixa barreira de entrada e mantenham a apresentação gradual de ferramentas. Antes de criar infraestrutura própria, considere se uma ferramenta existente já resolve o caso.

## Processo

1. Abra uma issue ou discussão apenas se a mudança for grande ou o escopo estiver incerto.
2. Crie uma branch para a mudança.
3. Mantenha o diff pequeno e direcionado.
4. Execute o check mínimo com o interpretador Python ativo no seu ambiente:

   ```bash
   python scripts/check_scaffold.py
   ```

   Se alterou um exemplo, execute também os testes e a geração desse exemplo. Se alterou documentação ou estilo, valide o output correspondente quando aplicável.
5. Abra um pull request explicando o problema ou caso, a solução e como ela foi validada.
