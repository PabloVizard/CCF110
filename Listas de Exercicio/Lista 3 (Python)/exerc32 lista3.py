itens = int(input())
valor = 0
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0

for i in range(1,(itens+1)):
    codigo = int(input())
    quant = float(input())

    if codigo == 1:
        valor = 3.00 * quant

    if codigo == 2:
        valor1 = 2.50 * quant

    if codigo == 3:
        valor2 = 2.50 * quant

    if codigo == 4:
        valor3 = 1.00 * quant

    if codigo == 5:
        valor4 = 3.00 * quant

    soma = valor + valor1 + valor2 + valor3 + valor4
print("Valor: {}".format(soma))

