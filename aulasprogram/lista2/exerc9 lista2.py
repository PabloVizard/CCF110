contpar = 0
contimpar = 0

for i in range (0, 10):
    i = float (input("Digite o valor: "))
    rest = i % 2

    if rest == 0:
        contpar = contpar + 1

    else:
        contimpar = contimpar +1

print("Temos {} números pares!".format(contpar))
print("Temos {} números impares!".format(contimpar))