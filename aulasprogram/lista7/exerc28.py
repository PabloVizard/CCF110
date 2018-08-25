n = int(input())
m = int(input())

if n != m:
    print("A matriz não é anti - simetrica!")

else:
    a = [[0 for i in range(m)]for j in range(m)]
    b = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = int(input())

    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != 0:
                    print("Não é Annti Simetrica!")
                    break

    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]

    for i in range(n):
        for j in range(m):
            if a[i][j] != -b[i][j]:
                print("Não é Anti simetrica!")
                cont = 0
                break
            else:
                cont = 1

    if cont == 1:
        print("É anti simetrica!")