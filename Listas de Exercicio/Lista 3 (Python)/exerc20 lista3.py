X = int(input())
Z = int(input())

if X < Z:
    for i in range(X, (Z+1)):
        print(i)

else:
    for i in range(Z, (X+1)):
        print(i)