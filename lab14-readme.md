# Caminho Binário Alternado - MC102 Laboratório 14

Este programa determina se existe um caminho alternado entre duas posições em um tabuleiro binário. Um caminho alternado é definido pelas seguintes condições:
- A distância entre as posições é ímpar, e as cores das casas são diferentes.
- A distância entre as posições é par, e as cores das casas são iguais.

---

## Funcionalidade

1. **Entrada do Tabuleiro**:
   - Um tabuleiro de tamanho \( L \times L \), onde cada célula possui uma cor representada como uma string ("0" ou "1").
   
2. **Entrada das Coordenadas**:
   - Duas posições no tabuleiro, dadas por suas coordenadas \( (l1, c1) \) e \( (l2, c2) \).
   
3. **Verificação do Caminho**:
   - O programa calcula a distância entre as posições e verifica se a sequência de cores atende às condições de um caminho alternado.

4. **Saída**:
   - Exibe se existe ou não um caminho alternado entre as duas posições.

---

## Entradas

1. **Tamanho do Tabuleiro**:
   - Um número inteiro \( L \), representando o número de linhas e colunas do tabuleiro.
   
2. **Tabuleiro**:
   - \( L \) linhas, cada uma contendo \( L \) elementos separados por espaços, representando as cores das casas do tabuleiro.

3. **Coordenadas**:
   - Quatro números inteiros \( l1, c1, l2, c2 \), indicando as posições iniciais e finais no tabuleiro.

- Exemplo de Entrada:
```
3
0 1 0
1 0 1
0 1 0
0 0 2 2
```

---

## Saídas

1. **Caminho Encontrado**:
   - Se existe um caminho alternado, o programa imprime:
     ```
     caminho encontrado
     ```

2. **Caminho Não Encontrado**:
   - Caso contrário, o programa imprime:
     ```
     caminho nao encontrado
     ```

- Exemplo de Saída:
```
caminho encontrado
```

---

## Como o Programa Funciona

1. **Função `caminho`**:
   - Calcula a distância entre as duas posições \( (x1, y1) \) e \( (x2, y2) \) como a soma das diferenças absolutas das coordenadas.
   - Verifica se a distância é par ou ímpar e compara as cores das casas.
   - Retorna `True` se o caminho alternado é válido, ou `False` caso contrário.

2. **Leitura do Tabuleiro e Coordenadas**:
   - O tabuleiro é lido e armazenado como uma lista de listas.
   - As coordenadas \( l1, c1, l2, c2 \) são lidas como inteiros.

3. **Verificação do Caminho**:
   - Compara as cores das casas nas posições inicial e final.
   - Usa a função `caminho` para determinar se o caminho alternado existe.

4. **Saída dos Resultados**:
   - Exibe uma mensagem indicando se o caminho foi encontrado.

---

## Limitações

- Não considera validação para entradas fora do intervalo do tabuleiro.
- Assume que o tabuleiro é sempre quadrado e bem formatado.

---

