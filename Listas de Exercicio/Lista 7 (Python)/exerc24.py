n = 10
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

for i in range(n):
    for j in range(n):
        if i == 7:
            temp = a[i][j]
            a[i][j] = a[1][j]
            a[1][j] = temp

for i in range(n):
    for j in range(n):
        if j == 9:
            temp = a[i][j]
            a[i][j] = a[i][3]
            a[i][3] = temp

for i in range(n):
    for j in range(n):
        if i+j == n-1:
            temp = a[i][j]
            a[i][j] = a[i][i]
            a[i][i] = temp

print(a)