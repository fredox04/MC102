# Verificação de Posições e Rotação de Peças em um Tabuleiro - MC102 Laboratório 15

Este programa implementa a verificação de ocorrências de uma peça dentro de um tabuleiro, considerando a peça em sua forma original e em suas três rotações de 90°, 180° e 270°. Ele conta o número de correspondências exatas para cada rotação e exibe os resultados.

---

## Funcionalidade

1. **Leitura do Tabuleiro**:
   - O programa lê um tabuleiro \( T \times T \) representado como uma matriz.

2. **Leitura da Peça**:
   - Lê uma peça \( P \times Q \) (matriz de tamanho arbitrário) que será verificada no tabuleiro.

3. **Verificação e Rotação**:
   - A peça é comparada ao tabuleiro, verificando correspondências em todas as posições possíveis.
   - A peça é rotacionada 90° três vezes, contabilizando ocorrências para cada rotação.

4. **Saída**:
   - O programa imprime o número de correspondências para a peça em cada uma de suas quatro orientações: 0°, 90°, 180°, 270°.

---

## Entradas

1. **Dimensão do Tabuleiro**:
   - Um inteiro \( T \), indicando o número de linhas (e colunas) do tabuleiro.

2. **Tabuleiro**:
   - \( T \) linhas com \( T \) elementos cada, representando os valores do tabuleiro.

3. **Dimensão da Peça**:
   - Um inteiro \( P \), indicando o número de linhas da peça.

4. **Peça**:
   - \( P \) linhas com \( Q \) elementos cada, representando os valores da peça.

- Exemplo de Entrada:
```
5
A A A A A
A . A . A
A A A A A
A . A . A
A A A A A
3
A A A
. A .
A A A
```

---

## Saídas

1. **Contagem de Ocorrências**:
   - O programa imprime quatro números inteiros, separados por vírgulas, representando o número de correspondências para as rotações de 0°, 90°, 180° e 270°.

- Exemplo de Saída:
```
4,4,4,4
```

---

## Como o Programa Funciona

1. **Função `verificacao`**:
   - Verifica se a peça corresponde exatamente ao tabuleiro, respeitando as regras:
     - Cada célula da peça deve coincidir com a célula do tabuleiro.
     - Posições marcadas como `.` na peça são ignoradas.
   - Incrementa a contagem se uma correspondência é encontrada.

2. **Função `rotacionar90`**:
   - Rotaciona a peça em 90° no sentido horário, criando uma nova matriz.

3. **Processamento**:
   - Para cada rotação da peça:
     - Verifica todas as posições possíveis no tabuleiro onde a peça pode caber.
     - Conta as correspondências exatas.
     - Rotaciona a peça em 90°.

4. **Saída dos Resultados**:
   - Exibe os contadores de correspondências para as orientações de 0°, 90°, 180° e 270°.

---

## Limitações

- O programa assume que o tabuleiro e a peça são fornecidos com as dimensões corretas.
- O caractere `.` na peça é tratado como uma célula "coringa", que sempre coincide com qualquer valor.

---
###Como Executar
1. Salve o código em um arquivo chamado, por exemplo, tabuleiro_peca.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os valores do tabuleiro e da peça, conforme o formato especificado nas entradas.
4. Veja os resultados no formato pontos1, pontos2, pontos3, pontos4, indicando o número de correspondências para cada rotação.
