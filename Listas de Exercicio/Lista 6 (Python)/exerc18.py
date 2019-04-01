a = [0 for x in range(10)]
b = [0 for x in range(10)]

for i in range(10):
    a[i] = int(input())
    b[i] = pow(a[i],2)

print(a)
print(b)