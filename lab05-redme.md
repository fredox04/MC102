# Jornada de Trabalho - MC102 Laboratório 5

Este programa calcula o total de horas trabalhadas e horas extras de um funcionário durante a semana, além de calcular o valor devido ao final do período. Ele considera limites diários e semanais para contabilizar horas extras.

---

## Funcionalidade

1. **Leitura de Dados**:
   - Valor da hora de trabalho.
   - Número de dias trabalhados na semana.
   - Períodos de trabalho em cada dia.

2. **Cálculo das Horas**:
   - Soma as horas trabalhadas em cada período de trabalho.
   - Identifica horas extras diárias (excedentes acima de 8 horas/dia).
   - Verifica se há horas extras semanais (excedentes acima de 44 horas/semana).

3. **Cálculo do Valor Devido**:
   - O valor devido inclui:
     - Horas normais.
     - Horas extras diárias e semanais, pagas com adicional de 50%.

4. **Resultado**:
   - Exibe o total de horas trabalhadas, horas extras e o valor devido.

---

## Entradas

1. **Valor da Hora**:
   - Um inteiro \( V \), representando o valor pago por hora trabalhada.

2. **Número de Dias Trabalhados**:
   - Um inteiro \( D \), indicando o número de dias trabalhados na semana.

3. **Períodos de Trabalho por Dia**:
   - Para cada dia, um número inteiro \( P \) indicando o número de períodos trabalhados.
   - Para cada período, os horários de início e fim (em horas inteiras).

**Exemplo de Entrada**:
```
20
5
2
8
12
13
17
1
9
18
2
8
12
13
18
1
8
12
```

---

## Saídas

1. **Horas Trabalhadas**:
   - Total de horas trabalhadas na semana.

2. **Horas Extras**:
   - Soma das horas extras diárias e semanais.

3. **Valor Devido**:
   - Valor total devido ao funcionário.

**Exemplo de Saída**:
```
Horas trabalhadas: 50 Horas extras: 6 Valor devido: R$ 1060.00
```
---

## Como o Programa Funciona

1. **Inicialização**:
   - Lê os dados básicos como valor da hora e número de dias trabalhados.

2. **Processamento Diário**:
   - Para cada dia, soma as horas trabalhadas nos períodos.
   - Calcula as horas extras diárias (se aplicável).

3. **Processamento Semanal**:
   - Soma todas as horas trabalhadas na semana.
   - Verifica e calcula horas extras semanais (se aplicável).

4. **Cálculo do Valor Total**:
   - Calcula o valor devido com base nas horas normais e no adicional de 50% para horas extras.

5. **Exibição do Resultado**:
   - Imprime as horas trabalhadas, horas extras e o valor devido.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, jornada_trabalho.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os dados no formato especificado:
    - Valor da hora.
    - Número de dias trabalhados.
    - Períodos de trabalho de cada dia.
4. Veja o total de horas trabalhadas, horas extras e o valor devido ao funcionário.
