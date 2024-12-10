# Controle de Estoque 2.0 - MC102 Laboratório 9

Este programa gerencia o estoque de produtos em uma loja, permitindo registrar compras e vendas. Ele calcula e exibe o estoque final, o número de pedidos de compra e o número de pedidos de venda de cada produto.

---

## Funcionalidade

1. **Entrada de Dados**:
   - O programa lê entradas no formato:
     ```
     <produto> : <quantidade>
     ```
   - Quantidades positivas indicam compras.
   - Quantidades negativas indicam vendas.
   - A entrada termina com a palavra `"FIM"`.

2. **Gerenciamento de Estoque**:
   - Atualiza o estoque com base nas entradas.
   - Verifica se há quantidade suficiente no estoque para atender vendas.
   - Registra o número de pedidos de compra e venda.

3. **Saída dos Resultados**:
   - Exibe as informações de cada produto:
     - Nome do produto.
     - Quantidade em estoque.
     - Número de pedidos de compra.
     - Número de pedidos de venda.

---

## Entradas

1. **Formato da Entrada**:
   - Cada linha contém o nome do produto e a quantidade no formato `<produto> : <quantidade>`.
   - Quantidades negativas indicam vendas e positivas indicam compras.
   - A entrada termina com `"FIM"`.

**Exemplo de Entrada**:
```
maçã : 10
banana : 5
maçã : -4
banana : -6
laranja : -2
FIM
```

---

## Saídas

1. **Informações do Estoque**:
   - Para cada produto, exibe:
     ```
     Produto: <nome_do_produto>
     Quantidade em Estoque: <quantidade>
     Pedidos de Compra: <num_compras>
     Pedidos de Venda: <num_vendas>
     ```

**Exemplo de Saída**:
```
Quantidade indisponivel para a venda de 6 unidade(s) do produto banana.
Quantidade indisponivel para a venda de 2 unidade(s) do produto laranja.
Produto: banana
Quantidade em Estoque: 5
Pedidos de Compra: 1
Pedidos de Venda: 1
Produto: maçã
Quantidade em Estoque: 6
Pedidos de Compra: 1
Pedidos de Venda: 1
```
---

## Como o Programa Funciona

1. **Verificação Inicial**:
   - Se uma venda é registrada para um produto inexistente no estoque, o programa exibe uma mensagem de erro e ignora a entrada.

2. **Atualização de Estoque**:
   - Para produtos existentes, o programa verifica se há estoque suficiente para atender vendas.
   - Em caso de estoque insuficiente, uma mensagem de erro é exibida.

3. **Registro de Pedidos**:
   - Compras e vendas são contadas separadamente.
   - Cada registro de compra ou venda incrementa o contador do produto correspondente.

4. **Exibição dos Resultados**:
   - Após a entrada `"FIM"`, o programa ordena os produtos alfabeticamente e exibe as informações de estoque, pedidos de compra e pedidos de venda.

---
###Como Executar
1. Salve o código em um arquivo chamado, por exemplo, controle_estoque.py.
2. Execute o programa em um terminal ou console Python.
3. Insira os dados no formato especificado até a entrada "FIM".
4. Veja o relatório do estoque e pedidos no console.
