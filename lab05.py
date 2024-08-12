##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Frederico Jon Campos
# RA: 243387
##################################################

# Leitura do valor da hora
V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
i = 1
j = 1
horas_trabalhadas = 0
horas_trabalhadas_no_dia = 0
horas_extras = 0
horas_extras_diarias = 0
horas_extras_semanais = 0
while j <= D:
    periodos = int(input())
    while i <= periodos:
        inicio_do_periodo = int(input())
        fim_do_periodo = int(input())
        horas_trabalhadas_no_dia = horas_trabalhadas_no_dia + fim_do_periodo - inicio_do_periodo
        i += 1
    if horas_trabalhadas_no_dia > 8:
        horas_extras_diarias = horas_extras_diarias + horas_trabalhadas_no_dia - 8
    horas_trabalhadas += horas_trabalhadas_no_dia
    j += 1
    i = 1
    horas_trabalhadas_no_dia = 0
if horas_trabalhadas - horas_extras_diarias > 44:
    horas_extras_semanais = horas_trabalhadas - horas_extras_diarias - 44
horas_extras = horas_extras_diarias + horas_extras_semanais

# Calculo do valor devido ao funcionário
valor = V * horas_trabalhadas + V/2 * horas_extras_diarias + V/2 * horas_extras_semanais

# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
