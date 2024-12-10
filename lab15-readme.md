# Caça-Palavras - MC102 Laboratório 15

Este programa implementa uma solução básica para um problema de busca de palavras em um tabuleiro de letras. Ele verifica se cada letra de uma palavra pode ser encontrada no tabuleiro e informa se a palavra foi encontrada ou não.

---

## Funcionalidade

O programa realiza as seguintes ações:

1. **Entrada do Tabuleiro**: O tabuleiro é uma matriz de letras, onde cada linha é lida como uma sequência de caracteres. A leitura do tabuleiro termina quando o usuário insere o caractere `'0'`.

2. **Entrada de Palavras**: Após o tabuleiro ser inserido, o programa recebe palavras a serem buscadas. A leitura das palavras termina quando o usuário insere `'0'`.

3. **Busca de Palavras**: Para cada palavra inserida, o programa verifica se todas as suas letras podem ser encontradas no tabuleiro, independentemente da ordem e da posição.

4. **Resultado**:
   - Se todas as letras da palavra forem encontradas no tabuleiro, o programa imprime:
     ```
     Palavra <palavra>: encontrada
     ```
   - Caso contrário, imprime:
     ```
     Palavra <palavra>: nao encontrada
     ```

---

## Entradas

1. **Tabuleiro**: 
   - Uma sequência de linhas contendo letras em sequência.
   - Exemplo de entrada:
     ```
     abcde
     fghij
     klmno
     pqrst
     uvwxy
     0
     ```

2. **Palavras**:
   - Uma sequência de palavras a serem buscadas no tabuleiro, uma por vez.
   - Exemplo de entrada:
     ```
     gato
     rato
     casa
     0
     ```

---

## Saídas

Para cada palavra inserida, o programa indica se a palavra foi encontrada ou não no tabuleiro, como mostrado abaixo:

  - Exemplo de Saída:
     ```
     Palavra gato: nao encontrada
     Palavra rato: encontrada
     Palavra casa: nao encontrada
     ```


---

## Como o Programa Funciona

1. O tabuleiro é armazenado como uma lista de listas, onde cada linha do tabuleiro é uma sublista.
2. A função `caca_palavras` verifica se todas as letras da palavra inserida estão presentes no tabuleiro. Para cada letra da palavra:
   - Percorre todas as linhas e colunas do tabuleiro.
   - Conta o número de vezes que a letra aparece.
3. Se o número de letras encontradas no tabuleiro for igual ou maior que o número de letras da palavra, ela é considerada "encontrada".

---

## Limitações

- O programa não verifica a posição exata das letras no tabuleiro. Ele apenas verifica se todas as letras da palavra estão presentes no tabuleiro.
- Letras repetidas na palavra serão contadas, mas podem ser encontradas em qualquer linha ou coluna do tabuleiro.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, caca_palavras.py.
2. Execute o programa em um terminal ou console Python.
3. Insira o tabuleiro linha por linha, seguido por '0'.
4. Insira as palavras uma por vez, seguidas por '0'.
5. Veja o resultado das palavras no console.
