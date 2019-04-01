soma = 0
num = 1
denom = 1

for i in range(1, 51):
    soma = soma + (num/denom)
    num = num + 2
    denom = denom + 1

print("Soma: {}".format(soma))