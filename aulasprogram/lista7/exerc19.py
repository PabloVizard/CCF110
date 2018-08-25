n = 5
m = 11
altura = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            altura[i][j] = input("Delegação: ")

        else:
            altura[i][j] = float(input("Altura: "))

for i in range(n):
    maior = 0
    for j in range(m):
        if j >= 1:
            if j == 1:
                maior = altura[i][j]

            elif altura[i][j] >= maior:
                maior = altura[i][j]
    print("Maior altura da delegação {}: {}".format(altura[i][0], maior))