###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Fredrico Jon Campos
# RA: 243387
###################################################
objeto_quantidade = []
estoque = {}
compras = {}
vendas = {}
j = []
while objeto_quantidade == []:
    informacao = input()
    objeto_quantidade = informacao.split(" : ")
    if int(objeto_quantidade[1]) < 0:
        a = int(objeto_quantidade[1]) * -1
        print("Quantidade indisponivel para a venda de " + str(a) + " unidade(s) do produto " + objeto_quantidade[0] + ".")
        objeto_quantidade = []
     
while informacao != 'FIM':
    if objeto_quantidade[0] in estoque.keys():
        if int(estoque[objeto_quantidade[0]]) + int(objeto_quantidade[1]) >= 0:
            estoque[objeto_quantidade[0]] = int(estoque[objeto_quantidade[0]]) + int(objeto_quantidade[1])
            if int(objeto_quantidade[1]) > 0:
                compras[objeto_quantidade[0]] += 1
            elif int(objeto_quantidade[1]) < 0:
                if objeto_quantidade[0] in vendas.keys():
                    vendas[objeto_quantidade[0]] += 1
                else:
                    vendas[objeto_quantidade[0]] = 1
        else:
            a = int(objeto_quantidade[1]) * -1
            print("Quantidade indisponivel para a venda de " + str(a) + " unidade(s) do produto " + objeto_quantidade[0] + ".")
    else:
        estoque[objeto_quantidade[0]] = objeto_quantidade[1]
        if int(objeto_quantidade[1]) > 0:
            compras[objeto_quantidade[0]] = 1
    objeto_quantidade = []

    while objeto_quantidade == []:
        informacao = input()
        if informacao != 'FIM':
            objeto_quantidade = informacao.split(" : ")
            if int(objeto_quantidade[1]) < 0 and objeto_quantidade[0] not in estoque.keys():
                a = int(objeto_quantidade[1]) * -1
                print("Quantidade indisponivel para a venda de " + str(a) + " unidade(s) do produto " + objeto_quantidade[0] + ".")
                objeto_quantidade = []
        else:
            for i in estoque.keys():
                if i not in vendas:
                    vendas[i] = 0
            e = sorted(estoque.items())
            c = sorted(compras.items())
            v = sorted(vendas.items())
            a = 0
            for i in e:
                print("Produto: " + i[0])
                print("Quantidade em Estoque: " + str(i[1]))
                print("Pedidos de Compra: " + str(c[a][1]))
                print("Pedidos de Venda: " + str(v[a][1]))
                a += 1
            exit()