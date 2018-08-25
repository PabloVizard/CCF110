soma = 0
for i in range (0, 4000000):
    n = int(input("Valor: "))

    if n == 0:
        break

    if n < 0:
        soma = soma + n

print("Soma dos negativos: {}".format(soma))