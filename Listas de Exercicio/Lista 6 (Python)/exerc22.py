n = 121
temp = [0 for x in range(n)]
soma = 0

for i in range(n):
    temp[i] = int(input())
    soma = soma + temp[i]

    if i == 0:
        maiortemp = temp[i]
        menortemp = temp[i]

    if temp[i] >= maiortemp:
        maiortemp = temp[i]

    if temp[i] <= menortemp:
        menortemp = temp[i]

media = soma/n
cont = 0

for i in range(n):
    if temp[i] > media:
        cont += 1

dias = [0 for x in range(cont)]
cont1 = 0
for i in range(n):
    if temp[i] > media:
        dias[cont1] = i
        cont1 += 1

print("Maior Temperatura:",maiortemp,"\nMenor Temperatura:",menortemp)
print("Média de Temperatura:",media)
print("Dias acima da média:",dias)