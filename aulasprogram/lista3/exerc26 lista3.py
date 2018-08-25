soma = 0
soma1 = 0

for i in range(1, 11):
    n = int(input())

    if 10 <= n and n >= 20:
        soma = soma + 1

    else:
        soma1 = soma1 + 1

print("{} estão no intervalo [10,20]".format(soma))
print("{} não estão no intervalo [10,20]".format(soma1))