T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Processamento
n = 0
pontos1 = 0
pontos2 = 0
pontos3 = 0
pontos4 = 0
col_tabuleiro = len(tabuleiro[0])
col_peca = len(peca[0])


def rotacionar90(matriz):
    quant_colunas = len(matriz[0])
    nova_linha = []
    nova_peca = []
    for j in range(quant_colunas):
        for i in range(P):
            nova_linha.append(matriz[-1-i][j])
        nova_peca.append(nova_linha)
        nova_linha = []
    matriz = nova_peca.copy()
    return matriz


def verificacao(linha,coluna,x):
    a = 0
    b = P * col_peca
    for i in range(P):
        for j in range(col_peca):
            if (peca[i][j] != tabuleiro [i + linha][j + coluna]) or (peca[i][j] == "." and tabuleiro [i + linha][j + coluna] == "."):
                a += 1
    if a == b:
        x += 1
    return x


for k in range(4):
    for i in range(T - P + 1):
        for j in range(col_tabuleiro - col_peca + 1):
            if k == 0:
                pontos1 += verificacao(i,j,n)
            elif k == 1:
                pontos2 += verificacao(i,j,n)
            elif k == 2:
                pontos3 += verificacao(i,j,n)
            elif k == 3:
                pontos4 += verificacao(i,j,n)
    peca = rotacionar90(peca)
    P = len(peca)
    col_peca = len(peca[0])

#Impressão do resultado
print(f"{pontos1},{pontos2},{pontos3},{pontos4}")
