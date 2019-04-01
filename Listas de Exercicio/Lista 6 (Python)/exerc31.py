n = int(input())
a = [0 for x in range(n)]
for i in range(n):
    a[i] = int(input())

for i in range(n):
    for j in range(i, n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Vetor Ordenado: ", a)

c = [0 for x in range(n)]
for i in range(n):
    for j in range(i, n):
        if a[j] == a[i]:
            if c[i] != 0:
                c[i] += 1
            else:
                c[i] += 1

d = [0 for x in range(n)]
for i in range(n):
    if i == 0:
        d[i] = a[i]

    elif a[i] != a[i-1]:
        d[i] = a[i]

for i in range(n):
    if d[i] != 0:
        print ("O número", d[i], "se repete",c[i], "vezes")