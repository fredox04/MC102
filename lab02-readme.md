# Rumo a Marte - MC102 Laboratório 2

Este programa compara o tempo necessário para duas espaçonaves concluírem suas viagens ao mesmo destino, considerando distâncias, velocidades e intervalos de espera entre os trajetos.

---

## Funcionalidade

1. **Leitura de Dados**:
   - Recebe as distâncias e velocidades das duas espaçonaves, além do tempo de espera (em dias) entre as etapas da viagem.

2. **Cálculo do Tempo Total de Viagem**:
   - Para cada espaçonave:
     - Calcula o tempo necessário para percorrer sua distância.
     - Considera o intervalo de espera para a segunda espaçonave.

3. **Comparação dos Tempos**:
   - Compara o tempo total gasto por ambas as espaçonaves e determina se a primeira é mais rápida que a segunda.

4. **Resultado**:
   - Exibe `True` se a primeira espaçonave é mais rápida.
   - Exibe `False` caso contrário.

---

## Entradas

1. **Distância da Primeira Espaçonave**:
   - Um inteiro \( D1 \), representando a distância a ser percorrida pela primeira espaçonave (em milhões de km).

2. **Velocidade da Primeira Espaçonave**:
   - Um inteiro \( V1 \), representando a velocidade da primeira espaçonave (em milhões de km/h).

3. **Tempo de Espera**:
   - Um inteiro \( T \), representando o tempo de espera entre os dois trechos da viagem (em dias).

4. **Distância da Segunda Espaçonave**:
   - Um inteiro \( D2 \), representando a distância a ser percorrida pela segunda espaçonave (em milhões de km).

5. **Velocidade da Segunda Espaçonave**:
   - Um inteiro \( V2 \), representando a velocidade da segunda espaçonave (em milhões de km/h).

**Exemplo de Entrada**:
```
384
8
1
750
10
```

---

## Saídas

1. **Resultado da Comparação**:
   - `True` se a primeira espaçonave é mais rápida.
   - `False` caso contrário.

**Exemplo de Saída**:
```
True
```

---

## Como o Programa Funciona

1. **Cálculo do Tempo Total para a Primeira Espaçonave**:
   - Divide a distância pela velocidade (\( T1 = D1 / V1 \)).

2. **Cálculo do Tempo Total para a Segunda Espaçonave**:
   - Divide a distância pela velocidade, somando o intervalo de espera em horas (\( T2 = (D2 / V2) + T \times 24 \)).

3. **Comparação dos Tempos**:
   - Compara \( T1 \) e \( T2 \) para determinar qual espaçonave é mais rápida.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, rumo_marte.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os valores no formato especificado:
    - Distâncias e velocidades das duas espaçonaves.
    - Tempo de espera em dias.
4. O programa exibirá True ou False, indicando se a primeira espaçonave é mais rápida.
