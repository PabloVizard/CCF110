a = [0 for x in range(30)]
b = [0 for x in range(30)]

for i in range(30):
    a = int(input())
    b = int(input())

x = int(input())

for i in range(30):
    if a[i] == x:
        print("Elemento: ",b[i])

