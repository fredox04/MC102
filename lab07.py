###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# Leitura das tropas de defesa
defesa = []
quantidade_defesa = int(input())
for i in range(quantidade_defesa):
    defesa.append(int(input()))

# Leitura das tropas de ataque
ataque = []
quantidade_ataque = int(input())
for i in range(quantidade_ataque):
    ataque.append(int(input()))

# Processamento da guerra
inicio_defesa = 0
pontuação_ataque = 0
pontuação_defesa = 0
while pontuação_ataque <= pontuação_defesa and inicio_defesa + quantidade_ataque < quantidade_defesa:
    pontuação_ataque = 0
    pontuação_defesa = 0
    for i in range(quantidade_ataque):
        if defesa[inicio_defesa + i] > ataque[i]:
            pontuação_defesa += 1
        elif defesa[inicio_defesa + i] < ataque[i]:
            pontuação_ataque += 1
    inicio_defesa += 1
# Saída de dados
if pontuação_ataque > pontuação_defesa:
    print('Vitória posicionando as tropas a partir da posição', inicio_defesa)
else:
    print('Derrota')    
