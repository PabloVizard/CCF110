n = 2
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
        a[i][j] = a[i][j]/n

print(a)