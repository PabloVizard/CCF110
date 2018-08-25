a = [0 for i in range(5)]
b = [0 for i in range(5)]
c = [0 for i in range(5)]

for i in range(5):
    a[i] = int(input())
    b[i] = int(input())
    soma = a[i] + b[i]
    c[i] = soma

print(c)