n = 5
notas = [0 for x in range(n)]
for i in range(n):
    notas[i] = int(input())

c = [0 for x in range(n)]
for i in range(n):
    for j in range(i, n):
        if notas[j] == notas[i]:
            if c[i] != 0:
                c[i] += 1
            else:
                c[i] += 1


d = [0 for x in range(n)]
for i in range(n):
    if i == 0:
        d[i] = notas[i]

    elif notas[i] != notas[i-1]:
        d[i] = notas[i]

for i in range(n):
    if d[i] != 0:
            print ("A nota ", d[i], "tem frequência absoluta de: ",c[i])
            print("E tem frequẽncia relativa de: {0:.2f}".format(c[i]/n))