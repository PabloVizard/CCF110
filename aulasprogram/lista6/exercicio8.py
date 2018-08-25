id = [0 for i in range(100)]
valor = [0 for i in range(100)]
cont = 0

id[cont] = int(input())
while id[cont] > 0:
    valor[cont] = float(input())
    cont += 1
    id[cont] = int(input())

cont1 = 0
while cont1 != cont:
    print("ID: {} Valor a pagar = R$ {}".format(id[cont1],valor[cont1]))
    cont1 += 1

cont1 = 0
conta = 0
while cont1 != cont:
    conta += valor[cont1]
    cont1 += 1

print("Valor total do Caixa = R$",conta)