n = 4
m = 5
soma = 0
a = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())
        soma += a[i][j]

print(soma)