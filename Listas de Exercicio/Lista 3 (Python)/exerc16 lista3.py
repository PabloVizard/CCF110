mult = 0

for a in range(0, 20):
    n = int(input("Valor: "))

    for i in range (1, (n+1)):
        mult = i * n
        print("{} x {} = {}".format(i, n, mult))