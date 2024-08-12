###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# Leitura da palavra
palavra = input()

# Leitura dos palpites e impressão do resultado para cada palpite
resposta = []
j = 1
tentativa = input()

while tentativa != palavra and j < 6:
    for i in range(len(palavra)):
        if palavra[i] == tentativa[i]:
            resposta.append(tentativa[i].capitalize())
        elif palavra[i] != tentativa[i]:
            if tentativa[i] in palavra:
                resposta.append(tentativa[i])
            else:
                resposta.append('_')
    str_resp = ''.join(resposta)
    print(str_resp)
    resposta = []
    tentativa = input()
    j += 1

# Impressão da linha final
if tentativa == palavra:
    print(palavra.upper())
    print("Resposta correta")
elif tentativa != palavra:
        for i in range(len(palavra)):
            if palavra[i] == tentativa[i]:
                resposta.append(tentativa[i].capitalize())
            elif palavra[i] != tentativa[i]:
                if tentativa[i] in palavra:
                    resposta.append(tentativa[i])
                else:
                    resposta.append('_')
        str_resp = ''.join(resposta)
        print(str_resp)
        print("Palavra correta:", palavra)