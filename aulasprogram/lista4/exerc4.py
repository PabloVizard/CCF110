ak = int(input("Termo a1: "))
q = float(input("Razão q: "))
n = int(input("Número de termos: "))
k = int(input("Termo k: "))
i = 1
a = 0

while i <= q:
    a = a + (ak * pow(q, (n-k)))
    print(a)
    i = i + 1