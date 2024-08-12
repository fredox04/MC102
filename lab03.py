###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Frederico Jon Campos
# RA: 243387
###################################################

# leitura de dados

dia_da_semana = int(input())
hora = int(input())
minuto = int(input())/60
estudante = str(input())
metodo_de_pagamento = str(input())
horario = hora + minuto

# valor do ingresso inteiro

if dia_da_semana == 1 or dia_da_semana == 4 and horario >= 18.50 or dia_da_semana == 5 and horario >= 18.50 or dia_da_semana == 7 and horario < 18.50:
    ingresso = 30.00
elif dia_da_semana == 2 and horario < 18.50 or dia_da_semana == 3 and horario < 18.50 or dia_da_semana == 4 and horario < 18.50:
    ingresso = 15.00
elif dia_da_semana == 5 and horario < 18.50 or dia_da_semana == 6 and horario < 18.50 or dia_da_semana == 2 and horario > 18.50 or dia_da_semana == 3 and horario > 18.50:
    ingresso = 20.00
else:
    ingresso = 40.00
    
# valor a pagar

if dia_da_semana == 1 or dia_da_semana == 6 and horario >18.50:
    desconto = 0.30
elif dia_da_semana == 7:
    desconto = 0.20
else:
    desconto = 0.50
    
if estudante == 'S':
    ingresso = ingresso/2

if metodo_de_pagamento == 'C' and estudante == 'N':
    ingresso = (1.00-desconto)*ingresso

# saída do valor do ingresso

print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))