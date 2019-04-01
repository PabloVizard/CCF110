n = int(input())
soma = 0
i = 0

while n > 0:
    if n % 3 == 0:
        soma += n
        i += 1

    n = int(input())

media = soma/i

print("Média: ", media)