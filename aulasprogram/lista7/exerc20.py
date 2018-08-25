n = 12
m = 4
venda = [[0 for i in range(m)]for j in range(n)]
vendatotal = 0
for i in range(n):
    for j in range(m):
        venda[i][j] = float(input())
        vendatotal += venda[i][j]

somames = [0 for i in range(n)]
for i in range(n):
    for j in range(m):
        somames[i] += venda[i][j]

for i in range(n):
    print("Venda do mes {}: {}".format(i+1, somames[i]))

for i in range(n):
    for j in range(m):
        print("Venda do mes {}, semana {}: {}".format(i+1, j+1, venda[i][j]))

print("Venda total do ano: ",vendatotal)