a1 = int(input("Termo a1: "))
q = float(input("Razão q: "))
n = int(input("Número de termos: "))
i = 1
a = 0

while i <= n:
    if i == 1:
        print(a1)
    else:
        a = a1 * pow(q, (i-1))
        print(a)

    i = i + 1