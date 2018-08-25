n = int(input())
M = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    m = input().split(" ")
    cont = 0
    for j in range(n):
        M[i][j] = int(m[cont])
        cont += 1

cont = 0
P = [0 for i in range(n * n)]
for i in range(n):
    for j in range(n):
        P[cont] = M[i][j]
        cont += 1

for i in range(n*n):
    for j in range(i,n*n):
        if P[j] < P[i]:
            temp = P[i]
            P[i] = P[j]
            P[j] = temp

cont1 = 1
for i in range(n * n):
    if P[i] != cont1:
        valor = 0
        print("0")
        break
    else:
        valor = 1
    cont1 += 1

if valor == 1:
    s = 0
    for i in range(n):
        s += M[i][i]

    s1 = 0
    for i in range(n):
        for j in range(n):
            s1 = M[i][j]
            if j == n-1:
                if s1 != s:
                    break
                    s = 0

                else:
                    s1 = 0
    print(s)