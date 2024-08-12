###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Caça-Palavras
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

def caca_palavras(m, tabuleiro):
    m = list(m)
    pontos = 0
    for i in m:
        for j in range(len(tabuleiro)):
            for k in tabuleiro[j]:
                if i == k:
                    pontos += 1
    if pontos >= len(m):
        return True
    else:
        return False


letras = []
a = []
leitura = input()

while leitura != '0':
    a = list(leitura)
    letras.append(a)
    a =[]
    leitura = input()


palavra = input()
while palavra != '0':
    if caca_palavras(palavra, letras) == True:
        print(f"Palavra {palavra}: encontrada")
    else:
        print(f"Palavra {palavra}: nao encontrada")
    palavra = input()
