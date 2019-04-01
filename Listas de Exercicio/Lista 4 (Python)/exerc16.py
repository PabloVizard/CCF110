x = float(input("Valor: "))

if x >= 0:
    x = pow(x, (1/2))
    print("Raiz Quadrada: {0: .2f}".format(x))

else:
    x = pow(x, 2)
    print("Quadrado: {0: .2f}".format(x))