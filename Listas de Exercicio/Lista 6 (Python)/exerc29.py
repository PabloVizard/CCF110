m = int(input())
a = [0 for x in range(m)]
for i in range(m):
    a[i] = int(input())

for i in range(m):
    for j in range(i, m):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

c = [0 for x in range(m)]
for i in range(m):
    if i == 0:
        c[i] = a[i]

    elif a[i] != a[i-1]:
        c[i] = a[i]

n = int(input())
b = [0 for x in range(n)]
for i in range(n):
    b[i] = int(input())

for i in range(n):
    for j in range(i, n):
        if b[i] > b[j]:
            temp = b[i]
            b[i] = b[j]
            b[j] = temp

d = [0 for x in range(n)]
for i in range(n):
    if i == 0:
        d[i] = b[i]

    elif b[i] != b[i-1]:
        d[i] = b[i]

print("Novo Conjunto: ")
for i in range(n):
    if c[i] != 0:
        print(c[i], end=" ")
print("")

for i in range(n):
    if d[i] != 0:
        print(d[i], end=" ")
print("")