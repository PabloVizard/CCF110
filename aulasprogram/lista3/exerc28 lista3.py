num_conta = int(input())
saldo = float(input())
soma = 0
soma1 = 0
i = 0

while num_conta > 0:
    i = i + 1

    if saldo < 0:
        print("Negativo")
    else:
        print("Positivo")

    num_conta =int(input())
    saldo = float(input())

    if saldo < 0:
        soma = soma + 1


if i != 0:
    percentual =  (soma / i) * 100
    print("Temos {} clientes negativos!".format(percentual))