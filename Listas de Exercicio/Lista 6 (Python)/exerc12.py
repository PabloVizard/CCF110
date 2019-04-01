a = [0 for x in range(10)]
b = [0 for x in range(10)]
cont = 9

for i in range(10):
    a[i] = int(input())

for i in range(10):
    b[i] = a[cont]
    cont -= 1

print(a)
print(b)