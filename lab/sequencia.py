values = input().split(' ')
x = int(values[0])
y = int(values[1])
cont = 1


for i in range(1, y+1):
    if i % x != 0:
        print(i, end=" ", flush=True)

    elif i % x == 0:
        print(i, end="")
        print("")

if y % x != 0:
    print(" ")
