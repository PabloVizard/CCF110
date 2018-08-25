n = 3
m = 5
a = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())

soma = [0 for i in range(n)]
for i in range(n):
    for j in range(m):
        soma[i] += a[i][j]

for i in range(n):
    print("Soma da linha {}: {}".format(i+1, soma[i]))
