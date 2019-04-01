altura = [0 for x in range(10)]
soma = 0
cont = 0
cont1 = 0

for i in range(10):
    altura[i] = float(input())
    soma = soma + altura[i]

media1 = soma/10

for i in range(10):
    if altura[i] > media1:
        cont1 += 1

media = [0 for x in range(cont1)]

for i in range(10):
    if altura[i] > media1:
        media[cont] = altura[i]
        cont += 1

print(media)