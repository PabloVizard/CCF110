a1 = int(input("Termo a1: "))
r = float(input("Razão r: "))
n = int(input("Número de Termos: "))
a = 0

for i in range (1, n+1):
        a = a1 + (i-1)*r
        print(a)