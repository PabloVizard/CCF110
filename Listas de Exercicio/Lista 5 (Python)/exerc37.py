numpedido = int(input())
soma = 0

while numpedido != 0:
    data = input()
    precounid = float(input())
    quant = int(input())

    soma += (precounid * quant)

    numpedido = int(input())

print("Valor compra: ", soma)