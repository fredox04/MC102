##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Frederico Jon Campos
# RA: 243387
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
torre2 = [int(panqueca) for panqueca in torre]
M = int(input())
torre_final = [int(panqueca) for panqueca in torre]
while M != 0:
    for i in range(M):
        torre_final[i] = torre[M - 1 - i]
    for i in range(M,len(torre)):
        torre_final[i] = torre[i]
    torre = [int(panqueca) for panqueca in torre_final]
    M = int(input())

# Impressão da saída
torre2.sort()
if torre_final == torre2:
    print("Torre estavel")
else:
    print("Torre instavel")