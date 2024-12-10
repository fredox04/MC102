# Eleições 2022 - MC102 Laboratório 13

Este programa processa votos recebidos em uma eleição simulada, calcula a quantidade de votos válidos e inválidos (nulos e brancos) e exibe os resultados ordenados por quantidade de votos em ordem decrescente.

---

## Funcionalidade

O programa realiza as seguintes ações:

1. **Entrada de Votos**:
   - Os votos são lidos continuamente até que o caractere `'0'` seja inserido.
   - Cada voto pode ser:
     - O nome de um candidato.
     - `"Branco"` para votos em branco.
     - `"Nulo"` para votos inválidos.

2. **Processamento dos Votos**:
   - Contabiliza os votos para cada candidato.
   - Conta separadamente os votos brancos e nulos.
   - Ordena os candidatos pela quantidade de votos em ordem decrescente.

3. **Saída dos Resultados**:
   - Exibe o nome de cada candidato e sua respectiva quantidade de votos.
   - Exibe a quantidade de votos brancos e nulos.

---

## Entradas

1. **Votos**:
   - Sequência de strings representando o nome do candidato ou as palavras `"Branco"` e `"Nulo"`.
   - A leitura termina quando o caractere `'0'` é inserido.

- Exemplo de Entrada:
```
Joao
Maria
Branco
Joao
Nulo
Maria
Maria
Branco
0
```

---

## Saídas

O programa exibe os resultados no seguinte formato:

1. **Candidatos**: Nome seguido pelo número de votos.
2. **Votos Brancos e Nulos**: Tipo de voto seguido pela quantidade.

- Exemplo de Saída:
```
Maria 3
Joao 2
Brancos 2
Nulos 1
```

---

## Como o Programa Funciona

1. **Leitura dos Votos**:
   - Os votos são armazenados em um dicionário chamado `eleicao`, onde a chave é o nome do candidato e o valor é a quantidade de votos.
   - Os votos brancos e nulos são contabilizados separadamente no dicionário `nulos_brancos`.

2. **Ordenação dos Resultados**:
   - Os candidatos no dicionário `eleicao` são ordenados pela quantidade de votos em ordem decrescente e transferidos para o dicionário `eleicao_ordenada`.

3. **Exibição dos Resultados**:
   - Primeiro, os resultados dos candidatos são exibidos.
   - Em seguida, os votos brancos e nulos são apresentados.

---

## Limitações

- O programa não trata empates entre candidatos. Caso dois candidatos tenham a mesma quantidade de votos, a ordem de exibição pode variar.
- Não considera validação para tipos de entrada inválidos.

---

## Código

```python
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# Leitura de dados
voto = input()
eleicao = {}
nulos_brancos = {'Brancos': 0, 'Nulos': 0}
while voto != '0':
    if voto == 'Branco':
        nulos_brancos['Brancos'] += 1
    elif voto == 'Nulo':
        nulos_brancos['Nulos'] += 1
    elif voto not in eleicao.keys():
        eleicao[voto] = 1
    else:
        eleicao[voto] += 1
    voto = input()

# Saída de dados
eleicao_ordenada = {}
for _ in range(len(eleicao)):
    menor_valor = list(eleicao.values())[0]
    menor_chave = list(eleicao.keys())[0]
    for i in eleicao.keys():
        if menor_valor < eleicao[i]:
            eleicao[menor_chave] = menor_valor
            menor_chave = i
            menor_valor = eleicao[menor_chave]
    eleicao.pop(menor_chave)
    eleicao_ordenada[menor_chave] = menor_valor

for i in eleicao_ordenada:
    print(i, eleicao_ordenada[i]) 

for i in nulos_brancos:
    print(i, nulos_brancos[i])
```
