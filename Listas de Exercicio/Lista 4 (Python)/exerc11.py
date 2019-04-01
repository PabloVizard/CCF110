valor_aula = float(input("Valor Aula: "))
num_aulas = float(input("Número de aulas: "))

salario = (valor_aula * num_aulas)

if salario <= 1317.07:
    salario_liquido = salario - (salario * 0.08)

elif salario >= 1317.08 and salario <= 2195.12:
    salario_liquido = salario - (salario * 0.09)

elif salario >= 2195.13 and salario <= 4390.24:
    salario_liquido = salario - (salario * 0.11)

print("Salário Liquido: {0: .2f}".format(salario_liquido))