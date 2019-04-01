a = [0 for x in range(15)]

for i in range(15):
    a[i] = int(input())

for i in range(15):
    for j in range(i, 15):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)