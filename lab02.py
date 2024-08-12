###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# Leitura de dados

D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())

# Cálculo do tempo total gasto por cada espaçonave 

T1 = D1/V1 
T2 = (D2/V2) + (T*24)

# Impressão da resposta
if (T1 < T2):
    print("True")
else:
    print("False")