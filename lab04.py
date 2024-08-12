###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# leitura da sequência de compras e vendas
estoque = 0
numero_de_vendas = 0
ajuste = int(input())

while ajuste != 0:
    if ajuste < 0:
        Y = ajuste * (-1)
        if Y > estoque:
            print(f"Quantidade indisponível para a venda de {Y} unidades.")
        else:
            estoque = estoque - Y
            numero_de_vendas += 1
    else:
        X = ajuste
        estoque = estoque + X
    ajuste = int(input())
    
# impressão da saída
print (f"Quantidade de vendas realizadas: {numero_de_vendas}")
print (f"Quantidade em estoque: {estoque}")