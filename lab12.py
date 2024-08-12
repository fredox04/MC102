###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    imagem = []
    q, p, r = 0, 0, 0
    for i in range(2*n-1):
        linha = []
        for j in range(2*m-1):
            if i % 2 == 0 and j % 2 == 0:
                linha.append(imagem_original[q][p])
                p += 1
                if p == m:
                    p = 0
                    q += 1
            else:
                linha.append(-1)
        imagem.append(linha)
    for i in range(len(imagem)):
        while r < len(imagem[0]):
            if imagem[i][r] == -1:
                imagem[i][r] = (imagem[i-1][r] + imagem[i+1][r])/2
            r += 2
        r = 0
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == -1:
                imagem[i][j] = (imagem[i][j-1] + imagem[i][j+1])/2
    return imagem

def retracao(imagem_original):
    imagem = []
    a, b = 0, 0
    if n % 2 == 0:
        for i in range(int(n/2)):
            linha = []
            if m % 2 == 0:
                for j in range(int(m/2)):
                    linha.append(-1)
            else:
                for j in range(int((m+1)/2)):
                    linha.append(-1)
            imagem.append(linha)

    else:
        for i in range(int((n+1)/2)):
            linha = []
            if n % 2 == 0:
                for j in range(int(m/2)):
                    linha.append(-1)
            else:
                for j in range(int((m+1)/2)):
                    linha.append(-1)
            imagem.append(linha)

    for i in range(int(n/2)):
        b = 0
        for j in range(int(m/2)):
            imagem[i][j] = (imagem_original[a][b] + imagem_original[a][b+1] + imagem_original[a+1][b] + imagem_original[a+1][b+1])/4
            b += 2
        a += 2

    if m % 2 == 1 and n % 2 == 1:
        if n % 2 == 1:
            a = 0
            for i in range(len(imagem)-1):
                imagem[i][-1] = (imagem_original[a][-1] + imagem_original[a+1][-1])/2
                a += 2
        if m % 2 == 1:
            b = 0
            for i in range(len(imagem[0])-1):
                imagem[-1][i] = (imagem_original[-1][b] + imagem_original[-1][b+1])/2
                b += 2
    
        imagem[-1][-1] = imagem_original[-1][-1]

    elif n % 2 == 1:
        a = 0
        for i in range(len(imagem[0])):
            imagem[-1][i] = (imagem_original[-1][a] + imagem_original[-1][a+1])/2
            a += 2

    elif m % 2 == 1:
        b = 0
        for i in range(len(imagem)):
            imagem[i][-1] = (imagem_original[b][-1] + imagem_original[b+1][-1])/2
            b += 2
    return imagem

# leitura da imagem
_ = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento
redimensionamento = input()
if redimensionamento == 'expansao':
    x = expansao(imagem_original)
else:
    x = retracao(imagem_original)
# impressão da imagem final
imprimir_imagem(x)