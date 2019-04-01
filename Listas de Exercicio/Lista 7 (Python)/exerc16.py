n = 3
m = 3
estoque = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            estoque[i][j] = input("Planta: ")

        if j == 1:
            estoque[i][j] = int(input("Estoque Ideal: "))

        if j == 2:
            estoque[i][j] = int(input("Estoque Atual: "))

for i in range(n):
    for j in range(m):
        if j == 2:
            if estoque[i][j] <= estoque[i][j-1]:
                compra = estoque[i][j-1] - estoque[i][j]
                if compra != 0:
                    print("É necesário comprar {} de {}".format(compra, estoque[i][0]))