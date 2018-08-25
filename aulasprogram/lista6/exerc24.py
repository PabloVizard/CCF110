n = 100
a = [0 for x in range(n)]
for i in range(n):
    a[i] = int(input())

soma = 0
cont = n-1
for i in range(n//2):
    soma += pow((a[i] - a[cont]), 3)
    n -= 1

print(soma)