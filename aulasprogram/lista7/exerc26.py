n = int(input())
m = int(input())
a = [[0 for i in range(m)]for j in range(n)]
b = [[0 for i in range(n)]for j in range(m)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())

for i in range(m):
    for j in range(n):
        b[i][j] = a[j][i]

print(b)