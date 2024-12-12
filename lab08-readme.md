# Wordle - MC102 Laboratório 8

Este programa implementa uma versão simplificada do jogo **Wordle**, onde o jogador tenta adivinhar uma palavra secreta em até 6 tentativas. Para cada tentativa, o programa fornece dicas indicando se uma letra está na posição correta, existe em outra posição ou não está presente na palavra.

---

## Funcionalidade

1. **Leitura da Palavra Secreta**:
   - O programa lê a palavra secreta que deve ser adivinhada.

2. **Leitura das Tentativas**:
   - O jogador insere uma palavra por tentativa.

3. **Feedback por Tentativa**:
   - Para cada letra na tentativa:
     - Se a letra está na posição correta, é exibida em **maiúscula**.
     - Se a letra está na palavra, mas em outra posição, é exibida em **minúscula**.
     - Se a letra não está na palavra, é substituída por `_`.

4. **Condição de Vitória**:
   - Se o jogador adivinhar a palavra secreta, a palavra inteira é exibida em maiúsculas e uma mensagem de "Resposta correta" é exibida.

5. **Condição de Derrota**:
   - Após 6 tentativas sem sucesso, o programa exibe a palavra correta.

---

## Entradas

1. **Palavra Secreta**:
   - Uma palavra de até 6 letras, que será a palavra secreta a ser adivinhada.

2. **Tentativas**:
   - Até 6 palavras de comprimento igual à palavra secreta.

**Exemplo de Entrada**:
```
campo
canpo
lampo
pomca
compo
campo
```

---

## Saídas

1. **Resultado de Cada Tentativa**:
   - Feedback indicando as letras na posição correta (maiúsculas), letras presentes na palavra (minúsculas) e letras ausentes (`_`).

2. **Mensagem Final**:
   - Em caso de acerto: `Resposta correta`.
   - Em caso de erro após 6 tentativas: `Palavra correta: <palavra>`.

**Exemplo de Saída**:
```
Ca__o
cAm_o
_lm_o
Po_c_
Campo
Resposta correta
```

---

## Como o Programa Funciona

1. **Feedback por Tentativa**:
   - Para cada letra na palavra de tentativa:
     - Se a letra coincide com a posição correspondente da palavra secreta:
       - Exibida em maiúscula.
     - Se a letra existe na palavra secreta, mas não na posição correta:
       - Exibida em minúscula.
     - Caso contrário:
       - Substituída por `_`.

2. **Contagem de Tentativas**:
   - O jogador pode realizar até 6 tentativas. Se a palavra correta não for encontrada, o programa exibe a palavra correta.

3. **Finalização**:
   - Se a palavra secreta for encontrada antes do limite de tentativas, o jogo termina com uma mensagem de vitória.

---

### Como executar

1. Salve o código em um arquivo chamado, por exemplo, wordle.py.
2. Execute o programa em um terminal ou console Python.
3. Insira a palavra secreta.
4. Insira as tentativas uma por vez.
5. O programa exibirá o feedback e o resultado final (vitória ou derrota).

