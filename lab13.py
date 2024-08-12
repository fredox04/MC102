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
