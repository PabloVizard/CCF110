num = 480
denom = 10
soma = 0

for i in range (0, 30):
    soma = soma + (((-1) ^ i) * num) / denom
    denom = denom + 1
    num = num - 5

print("O resultado da soma é: {}".format(soma))