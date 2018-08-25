n = int(input())
a = [0 for x in range(n)]
b = [0 for x in range(n)]
c = [0 for x in range(n*2)]
cont = 0
cont1 = 0

for i in range(n):
    a[i] = int(input())

for i in range(n):
    b[i] = int(input())

for i in range(n*2):
    if i % 2 == 0:
        c[i] = a[cont1]
        cont1 += 1

    else:
        c[i] = b[cont]
        cont += 1

print(a)
print(b)
print(c)