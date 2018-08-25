n = int(input())
i = 0

while n >= 0:
    if n == 2:
        i += 1

    elif n % 2 != 0:
        i += 1
    n = int(input())
print("Primos: ", i)