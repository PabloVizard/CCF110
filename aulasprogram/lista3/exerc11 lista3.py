for i in range (1, 4000000000):
    n = float(input("Valor: "))
    n = n * n
    num = n % 6

    if num == 0:
        print("Quadrado de multiplo de 6: {}".format(n))
        break

    else:
        print("Quadrado: {}".format(n))