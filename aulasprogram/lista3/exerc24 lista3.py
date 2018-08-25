idade = float(input())
soma21 = 0
soma50 = 0

while idade > 0:
    if idade < 21:
        soma21 = soma21 + 1

    if idade > 50:
        soma50 = soma50 + 1

    idade = int(input())

print("Tem {} com menos de 21 anos".format(soma21))
print("Tem {} com mais de 50 anos".format(soma50))