n = 3
a = [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

for i in range(n):
    for j in range(n):
        if j == 0:
            print("%3d"%a[i][j],end="")

        else:
            print("%4d" % a[i][j], end="")
    print("")
print("")

for i in range(n):
    for j in range(n):
        if j == n-1:
            temp = a[i][j-(n-1)]
            a[i][j-(n-1)] = a[i][j]
            a[i][j] = temp

for i in range(n):
    for j in range(n):
        if i == n-1:
            temp = a[i-(n-1)]
            a[i-(n-1)] = a[i]
            a[i] = temp

for i in range(n):
    for j in range(n):
        if j == 0:
            print("%3d"%a[i][j],end="")

        else:
            print("%4d" % a[i][j], end="")
    print("")
print("")
