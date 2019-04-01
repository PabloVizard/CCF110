n = 3
a = [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

for i in range(n):
    for j in range(n):
        if j == n-1:
            temp = a[i][j-(n-1)]
            a[i][j-(n-1)] = a[i][j]
            a[i][j] = temp

for i in range(n-1):
    for j in range(n-1):
        temp = a[i][j]
        a[i][j] = a[n-1-j][n-1-i]
        a[n-1-j][n-1-i] = temp

print(a)