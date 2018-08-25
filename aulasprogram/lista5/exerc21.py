n = int(input())
soma = 0

while n != -1:
    if n >= 0:
        soma += n

    n = int(input())

print("Soma: ", soma)