num_conta = int(input())
nome = input()
saldo = float(input())
soma = 0
soma1 = 0
i = 0

while num_conta != -999 or i != 5:
    i = i + 1

    if saldo < 0:
        print("Negativo")
    else:
        print("Positivo")

    num_conta =int(input())
    nome = input()
    saldo = float(input())

    if saldo < 0:
        soma = soma + 1

    else:
        soma1 = soma1 + 1

print("Temos {} clientes postivios!".format(soma1))
print("Temos {} clientes negativos!".format(soma))