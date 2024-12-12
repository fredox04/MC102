# Ingresso do Cinema - MC102 Laboratório 3

Este programa calcula o valor de um ingresso de cinema com base no dia da semana, horário da sessão, status de estudante e método de pagamento. Ele aplica descontos específicos de acordo com as condições fornecidas.

---

## Funcionalidade

1. **Leitura de Dados**:
   - Dia da semana (1 a 7).
   - Horário da sessão (hora e minuto).
   - Status de estudante (`S` para sim, `N` para não).
   - Método de pagamento (`C` para cartão de crédito, outro para dinheiro).

2. **Cálculo do Valor do Ingresso**:
   - O valor base do ingresso é definido de acordo com o dia da semana e horário.
   - Descontos são aplicados dependendo do dia, horário, status de estudante e método de pagamento.

3. **Resultado**:
   - Exibe o valor final do ingresso, formatado para duas casas decimais e no formato brasileiro (vírgula como separador decimal).

---

## Entradas

1. **Dia da Semana**:
   - Um inteiro de 1 a 7 (1 para segunda-feira, 7 para domingo).

2. **Horário da Sessão**:
   - Dois inteiros representando hora e minuto.

3. **Status de Estudante**:
   - Uma string (`S` para sim, `N` para não).

4. **Método de Pagamento**:
   - Uma string (`C` para cartão de crédito ou outro para dinheiro).

**Exemplo de Entrada**:
```
5
18
30
N
C
```

---

## Saídas

1. **Valor do Ingresso**:
   - O valor final do ingresso, formatado no estilo brasileiro.

**Exemplo de Saída**:
```
Valor do ingresso: R$ 28,00
```

---

## Como o Programa Funciona

1. **Cálculo do Valor Base do Ingresso**:
   - Determina o valor do ingresso com base no dia da semana e no horário da sessão.

2. **Aplicação de Descontos**:
   - Descontos são aplicados em duas etapas:
     - Desconto de 50% para estudantes.
     - Desconto adicional para pagamento com cartão de crédito, dependendo do dia e horário.

3. **Exibição do Resultado**:
   - Imprime o valor final do ingresso.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, ingresso_cinema.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os dados no formato especificado:
    - Dia da semana.
    - Hora e minuto da sessão.
    - Status de estudante.
    - Método de pagamento.
4. O programa exibirá o valor final do ingresso.
