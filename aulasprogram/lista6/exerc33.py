n = int(input())
a = [0 for x in range(n)]
for i in range(n):
    a[i] = int(input())

k = int(input())
if k <= n:
    print("Elemento K em A: ",a[k])

else:
    print("Valor inválido!")

for i in range(n):
    for j in range(i, n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Ordenação: ", a)