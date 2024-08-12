#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Frederico Jon Campos
# RA: 243387
#####################################################

def caminho(tabuleiro, x1, y1, x2, y2,cor1, cor2):
    t = int((x1**2)**(1/2) - (x2**2)**(1/2)) + ((y1**2)**(1/2) + (y2**2)**(1/2))
    if t%2 == 0 and cor1 == cor2: return True
    elif t%2 == 1 and cor1 != cor2: return True
    return False
# Leitura dos dados

L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

# Verificação se existe um caminho

cor1 = tabuleiro[l1][c1]
cor2 = tabuleiro[l2][c2]
if caminho(tabuleiro, l1, c1, l2, c2, cor1, cor2) == True:
    print("caminho encontrado")
else:
    print("caminho nao encontrado")
  
  