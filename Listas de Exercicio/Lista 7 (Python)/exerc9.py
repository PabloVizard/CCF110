n = 10
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

for i in range(n):
    for j in range(n):
        if i+j < n-1:
            print(a[i][j], end=" ")
print(" ")