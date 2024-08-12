#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Frederico Jon Campos
# RA: 243387
#####################################################

# Leitura da matriz
n = int(input())
matriz = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos
time1 = input()
quantidade_jogadores = int(input())
lista = []
x = 0
y = 0
pontos_time1 = 0
pontos_time2 = 0
jogada = 1
for i in range(quantidade_jogadores):
    caminho = list(input())
    for j in caminho:
        if j == 'S':
            lista.append(matriz[y + 1][x])
            matriz[y + 1][x] = '.'
            y += 1
        elif j == 'N':
            lista.append(matriz[y - 1][x])
            matriz[y - 1][x] = '.'
            y -= 1
        elif j == 'O':
            lista.append(matriz[y][x - 1])
            matriz[y][x - 1] = '.'
            x -= 1
        elif j == 'L':
            lista.append(matriz[y][x + 1])
            matriz[y][x + 1] = '.'
            x += 1

    for l in lista:
        if l == '*' and jogada % 2 == 1:
            pontos_time1 += 1
        elif l == '*' and jogada % 2 == 0:
            pontos_time2 += 1

    lista = []
    x = 0
    y = 0
    jogada += 1
 
# Impressão da saída
if time1 == 'azul':
    print(f"Tesouros encontrados pelo time azul: {pontos_time1}")
    print(f"Tesouros encontrados pelo time vermelho: {pontos_time2}")
    if pontos_time1 > pontos_time2:
        print("Vitoria do time azul")
    elif pontos_time1 < pontos_time2:
        print("Vitoria do time vermelho")
    else:
        print("Empate")
else:
    print(f"Tesouros encontrados pelo time azul: {pontos_time2}")
    print(f"Tesouros encontrados pelo time vermelho: {pontos_time1}")
    if pontos_time2 > pontos_time1:
        print("Vitoria do time azul")
    elif pontos_time2 < pontos_time1:
        print("Vitoria do time vermelho")
    else:
        print("Empate")