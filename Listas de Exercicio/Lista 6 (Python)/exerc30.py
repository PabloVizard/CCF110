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

print("Crescente: ",a)

for i in range(n):
    for j in range(i, n):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("Decrescente: ",a)