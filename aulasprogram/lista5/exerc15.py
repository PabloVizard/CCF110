n = int(input())
a = 0

for i in range (1, (n+1)):
    if i != 0:
        if n % i == 0:
            print(i, "é divisor de ", n)