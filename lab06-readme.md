# Torre de Panquecas - MC102 Laboratório 6

Este programa simula a organização de uma torre de panquecas. O objetivo é realizar uma série de movimentos para reorganizar a torre e verificar se ela está ordenada de forma crescente.

---

## Funcionalidade

1. **Leitura da Torre de Panquecas**:
   - O programa recebe uma lista de números inteiros representando as alturas das panquecas em uma torre.

2. **Movimentos para Reorganizar**:
   - Cada movimento é representado por um número \( M \), que indica que as primeiras \( M \) panquecas da torre devem ser invertidas.

3. **Verificação da Torre**:
   - Após todos os movimentos, o programa verifica se a torre está ordenada de forma crescente.

4. **Resultado**:
   - Exibe `Torre estavel` se a torre está ordenada.
   - Exibe `Torre instavel` caso contrário.

---

## Entradas

1. **Torre de Panquecas**:
   - Uma linha contendo \( n \) inteiros representando as alturas das panquecas.

2. **Movimentos**:
   - Vários inteiros \( M \), indicando o número de panquecas a serem invertidas no movimento.
   - A entrada termina com \( M = 0 \).

**Exemplo de Entrada**:
```
4 3 2 1
3
2
0
```

---

## Saídas

1. **Resultado da Organização**:
   - `Torre estavel` se a torre está ordenada de forma crescente.
   - `Torre instavel` caso contrário.

**Exemplo de Saída**:
```
Torre estavel
```

---

## Como o Programa Funciona

1. **Inicialização**:
   - Lê a torre inicial e cria uma cópia ordenada dela para comparação posterior.

2. **Execução dos Movimentos**:
   - Para cada \( M \):
     - Inverte as primeiras \( M \) panquecas da torre.
   - Atualiza a torre após cada movimento.

3. **Verificação da Torre**:
   - Compara a torre final com a versão ordenada.
   - Exibe o resultado.

---
### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, torre_panquecas.py.
2. Execute o programa em um terminal ou console Python.
3. Insira a lista de alturas das panquecas.
4. Insira os movimentos 𝑀 até finalizar com 𝑀 = 0.
5. O programa exibirá se a torre está estável (ordenada) ou instável.
   
