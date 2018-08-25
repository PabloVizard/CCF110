n = 37
soma = 0

for i in range (1, 38, 1):
    soma = soma + ((n * (n+1))/i)
    n = n - 1

print("A soma é: {}".format(soma))