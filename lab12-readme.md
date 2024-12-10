# Redimensionamento de Imagens - MC102 Laboratório 12

Este programa implementa funções para redimensionar imagens no formato PGM (Portable Graymap). Ele permite duas operações principais:
1. **Expansão**: Amplia a imagem, duplicando as dimensões e interpolando os valores ausentes.
2. **Retração**: Reduz a imagem pela metade, calculando a média dos valores de pixels adjacentes.

---

## Funcionalidade

1. **Leitura da Imagem**:
   - O programa lê uma imagem no formato PGM com as seguintes especificações:
     - Tipo: `P2` (imagem em tons de cinza).
     - Largura e altura da imagem.
     - Valor máximo da escala de cinza (sempre 255).
     - Matriz de valores representando os pixels da imagem.

2. **Redimensionamento**:
   - Expansão:
     - Dobra as dimensões da imagem.
     - Preenche os valores intermediários por interpolação linear.
   - Retração:
     - Reduz as dimensões da imagem pela metade.
     - Calcula a média dos pixels em blocos \(2 \times 2\).
     - Trata adequadamente casos onde a largura ou altura são ímpares.

3. **Saída da Imagem**:
   - Imprime a imagem redimensionada no formato PGM.

---

## Entradas

1. **Cabeçalho da Imagem**:
   - Tipo do arquivo PGM (linha ignorada pelo programa).
   - Largura e altura da imagem (número de colunas e linhas).
   - Valor máximo da escala de cinza (linha ignorada pelo programa).

2. **Matriz da Imagem**:
   - Matriz \(n \times m\) de inteiros representando os valores dos pixels.

3. **Tipo de Redimensionamento**:
   - `expansao`: para ampliar a imagem.
   - `retracao`: para reduzir a imagem.

- Exemplo de Entrada:
```
P2
3 2
255
12 34 56
78 90 12
expansao
```

---

## Saídas

1. **Cabeçalho da Imagem Redimensionada**:
   - Tipo do arquivo (`P2`).
   - Largura e altura da imagem redimensionada.
   - Valor máximo da escala de cinza (sempre `255`).

2. **Matriz Redimensionada**:
   - Os valores dos pixels após o redimensionamento.

- Exemplo de Saída (para o exemplo acima):
```
P2
5 3
255
12 23 34 45 56
45 56 67 78 89
78 84 90 51 12
```

---

## Como o Programa Funciona

1. **Leitura da Imagem**:
   - Lê a largura e altura da imagem.
   - Lê a matriz de pixels linha por linha.

2. **Função de Expansão**:
   - Cria uma nova matriz com dimensões \( (2n-1) \times (2m-1) \).
   - Preenche os valores originais e interpola os valores intermediários.

3. **Função de Retração**:
   - Cria uma nova matriz com dimensões reduzidas (\(n/2\) ou \((n+1)/2\) dependendo da paridade).
   - Calcula a média dos valores em blocos \(2 \times 2\) para preencher os novos valores.

4. **Saída da Imagem**:
   - Imprime a imagem redimensionada no formato PGM.

---

## Limitações

- Apenas suporta imagens no formato PGM do tipo `P2`.
- Supõe que as entradas estejam bem formatadas.
- A interpolação na expansão é linear, sem considerar outras técnicas mais avançadas.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, redimensionamento.py.
2. Execute o programa em um terminal ou console Python.
3. Insira as informações da imagem no formato PGM.
4. Escolha o tipo de redimensionamento: expansao ou retracao.
5. Veja a saída da imagem redimensionada no console.
