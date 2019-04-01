ak = int(input("Termo ak: "))
r = float(input("Razão r: "))
n = int(input("Número de Termos: "))
k = int(input("Termo k: "))
i = 1
a = 0

while i <= n:
    a = a + (ak + (n-k)*r)
    print(a)
    i = i + 1