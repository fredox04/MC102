# Controle de Estoque - MC102 Laboratório 4

Este programa realiza o controle de estoque de um produto, registrando compras, vendas e validando a disponibilidade do estoque para as operações de venda. Ao final, exibe o número total de vendas realizadas e a quantidade final em estoque.

---

## Funcionalidade

1. **Leitura de Operações**:
   - O programa lê uma sequência de operações de ajuste no estoque:
     - Valores positivos indicam compras (incremento no estoque).
     - Valores negativos indicam vendas (decremento no estoque).

2. **Validação de Estoque**:
   - Antes de registrar uma venda, verifica se há estoque suficiente para atender a operação.
   - Caso o estoque seja insuficiente, exibe uma mensagem de erro.

3. **Cálculo dos Resultados**:
   - Soma o número de vendas realizadas.
   - Calcula o estoque final após todas as operações.

4. **Resultado**:
   - Exibe o número total de vendas realizadas e o estoque final.

---

## Entradas

1. **Operações**:
   - Sequência de inteiros representando ajustes no estoque:
     - Valores positivos indicam compras.
     - Valores negativos indicam vendas.
   - A entrada termina com o valor `0`.

**Exemplo de Entrada**:
```
10
-5
-8
15
-12
0
```

---

## Saídas

1. **Resultados do Controle de Estoque**:
   - Mensagens de erro para vendas não atendidas por falta de estoque.
   - Quantidade de vendas realizadas.
   - Estoque final.

**Exemplo de Saída**:
```
Quantidade indisponível para a venda de 8 unidades.
Quantidade indisponível para a venda de 12 unidades.
Quantidade de vendas realizadas: 1
Quantidade em estoque: 20
```

---

## Como o Programa Funciona

1. **Inicialização**:
   - Começa com o estoque inicial igual a 0.
   - Lê os ajustes de estoque (compras e vendas).

2. **Validação de Vendas**:
   - Para cada valor negativo (venda), verifica se há estoque suficiente:
     - Se houver, decremente o estoque e registre a venda.
     - Caso contrário, exiba uma mensagem de erro.

3. **Registro de Compras**:
   - Para valores positivos, incrementa o estoque.

4. **Finalização**:
   - Exibe o total de vendas realizadas e a quantidade final em estoque.

---

### Como Executar
1. Salve o código em um arquivo chamado, por exemplo, controle_estoque.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os valores de ajuste de estoque:
    - Valores positivos para compras.
    - Valores negativos para vendas.
    - Finalize a sequência com 0.
4. O programa exibirá as mensagens de erro para vendas não atendidas, o número de vendas realizadas e o estoque final.
5. 
