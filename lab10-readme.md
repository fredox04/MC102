# Caça ao Tesouro - MC102 Laboratório 10

Este programa simula uma caça ao tesouro em um tabuleiro representado como uma matriz. Dois times (azul e vermelho) se alternam para seguir caminhos pré-definidos, buscando tesouros marcados no tabuleiro. O programa calcula os tesouros coletados por cada time e determina o vencedor.

---

## Funcionalidade

1. **Leitura do Tabuleiro**:
   - O tabuleiro é uma matriz \( n \times n \) onde cada célula pode conter um tesouro (`*`) ou estar vazia (`.`).

2. **Leitura dos Caminhos**:
   - Para cada jogador, o programa lê um caminho composto por movimentos (`N` para norte, `S` para sul, `L` para leste e `O` para oeste).

3. **Movimentação e Coleta de Tesouros**:
   - Cada jogador segue o caminho fornecido, coletando tesouros (`*`) ao longo do percurso.
   - Os tesouros coletados são contabilizados para o time correspondente (azul ou vermelho).

4. **Resultado**:
   - O programa exibe os tesouros encontrados por cada time e declara o vencedor (ou empate).

---

## Entradas

1. **Tamanho do Tabuleiro**:
   - Um inteiro \( n \), indicando o número de linhas e colunas do tabuleiro.

2. **Tabuleiro**:
   - \( n \) linhas contendo \( n \) elementos cada, representando o estado inicial do tabuleiro.

3. **Time Inicial**:
   - Uma string (`"azul"` ou `"vermelho"`) indicando qual time começa jogando.

4. **Quantidade de Jogadores**:
   - Um inteiro \( q \), representando o número de jogadores.

5. **Caminhos dos Jogadores**:
   - \( q \) linhas, cada uma contendo uma sequência de movimentos (`N`, `S`, `L`, `O`) que o jogador seguirá no tabuleiro.

**Exemplo de Entrada**:
```
5
. * . . .
. . * * .
. . . . *
. * . . .
. . . * .
azul
3
SSSS
LLOO
NNNN
```

---

## Saídas

1. **Tesouros Encontrados**:
   - O número de tesouros coletados por cada time.

2. **Resultado da Partida**:
   - O programa declara o vencedor ou indica empate.

**Exemplo de Saída**:
```
Tesouros encontrados pelo time azul: 2
Tesouros encontrados pelo time vermelho: 3
Vitoria do time vermelho
```
---

## Como o Programa Funciona

1. **Leitura do Tabuleiro e Caminhos**:
   - Lê o tamanho do tabuleiro, a matriz inicial, o time que começa jogando, o número de jogadores e os caminhos.

2. **Processamento das Movimentações**:
   - Cada jogador segue o caminho fornecido, coletando tesouros ao longo do percurso.
   - O tabuleiro é atualizado para refletir as células já visitadas.

3. **Contagem de Tesouros**:
   - Os tesouros encontrados são atribuídos ao time ativo, alternando entre os times a cada jogada.

4. **Determinação do Resultado**:
   - Compara os tesouros coletados pelos times e declara o vencedor ou empate.

---
### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, caca_tesouro.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os dados de entrada conforme o formato especificado:
    - Tamanho do tabuleiro.
    - Matriz representando o tabuleiro.
    - Time inicial.
    - Quantidade de jogadores.
    - Caminhos de cada jogador.
4. Veja os resultados da coleta de tesouros e o time vencedor no console.
