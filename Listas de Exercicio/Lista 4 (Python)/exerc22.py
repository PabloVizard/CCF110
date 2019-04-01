x = float(input("Valor: "))
y = float(input("Valor: "))

if x > y:
    y = pow(y, 2)

    if x >= 0:
        x = pow(x, (1/2))
        print("Quadrado menor: {} \n Raiz do Maior: {}".format(y,x))

    elif x < 0:
        print("Quadrado menor: {} \n Não tem raiz real o maior!".format(y))

elif  x < y:
    x = pow(x, 2)

    if y >= 0:
        y = pow(y, (1 / 2))
        print("Quadrado menor: {} \n Raiz do Maior: {}".format(x, y))

    elif y < 0:
        print("Quadrado menor: {} \n Não tem raiz real o maior!".format(x))