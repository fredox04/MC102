# Disconnect - MC102 Laboratório 7

Este programa simula uma batalha entre tropas de defesa e tropas de ataque, verificando a melhor posição inicial para as tropas de ataque obterem uma vitória.

---

## Funcionalidade

1. **Leitura das Tropas**:
   - O programa lê as forças das tropas de defesa e ataque, que são valores inteiros.

2. **Simulação de Batalha**:
   - Para cada posição inicial possível das tropas de ataque em relação às tropas de defesa, o programa calcula o resultado da batalha:
     - **Ponto para a Defesa**: Quando a força da tropa de defesa é maior que a tropa de ataque correspondente.
     - **Ponto para o Ataque**: Quando a força da tropa de ataque é maior que a tropa de defesa correspondente.

3. **Condição de Vitória**:
   - O programa verifica se as tropas de ataque podem vencer, ajustando sua posição inicial na linha de defesa.

4. **Resultado**:
   - Se as tropas de ataque conseguem vencer em alguma posição inicial, a posição inicial vencedora é exibida.
   - Caso contrário, o programa declara derrota.

---

## Entradas

1. **Quantidade e Forças das Tropas de Defesa**:
   - Um inteiro \( n \), seguido por \( n \) inteiros representando as forças das tropas de defesa.

2. **Quantidade e Forças das Tropas de Ataque**:
   - Um inteiro \( m \), seguido por \( m \) inteiros representando as forças das tropas de ataque.

**Exemplo de Entrada**:
```
5
3
6
1
7
5
3
2
8
4
```

---

## Saídas

1. **Resultado da Batalha**:
   - Se as tropas de ataque vencerem, a posição inicial vencedora é exibida:
     ```
     Vitória posicionando as tropas a partir da posição <posição>
     ```
   - Se não houver vitória para o ataque:
     ```
     Derrota
     ```

**Exemplo de Saída**:
```
Vitória posicionando as tropas a partir da posição 2
```
---

## Como o Programa Funciona

1. **Inicialização**:
   - Lê as forças das tropas de defesa e ataque.

2. **Simulação da Guerra**:
   - Para cada posição inicial possível das tropas de ataque:
     - Compara as forças das tropas de ataque com as forças das tropas de defesa.
     - Conta os pontos para ataque e defesa.

3. **Condição de Parada**:
   - A simulação termina se o ataque obtiver mais pontos que a defesa em alguma posição inicial.

4. **Exibição do Resultado**:
   - Exibe a posição inicial vencedora do ataque ou declara derrota.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, disconnect.py.
2. Execute o programa em um terminal ou console Python.
3. Insira as quantidades e forças das tropas de defesa e ataque.
4. O programa exibirá se as tropas de ataque podem vencer e, se possível, a posição inicial vencedora.
   
