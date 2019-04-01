c = int(input("Indice A"))
d = int(input("Indice A"))

e = int(input("Indice B"))
f = int(input("Indice B"))

if d != e:
    print("Não é possivel fazer o produto")
else:
    a = [[0 for i in range(d)]for j in range(c)]
    for i in range(c):
        for j in range(d):
            a[i][j] = float(input())

    b = [[0 for i in range(f)] for j in range(e)]
    for i in range(e):
        for j in range(f):
            b[i][j] = float(input())

    g = [[0 for i in range(f)] for j in range(c)]
    for i in range(c):
        for j in range(f):
            for k in range(d):
                g[i][j] += a[i][k] * b[k][j]

    print(g)