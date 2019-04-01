a = [0 for x in range(10)]
contpar = 0
contimpar = 0
somapar = 0
somaimpar = 0

for i in range(10):
    a[i] = int(input())

    if i == 0:
        maior = a[i]
        menor = a[i]

    if a[i] % 2 == 0:
        somapar += a[i]
        contpar += 1

        if a[i] >= maior:
            maior = a[i]

    else:
        somaimpar += a[i]
        contimpar += 1

        if a[i] <= menor:
            menor = a[i]

mediapar = somapar/contpar
mediaimpar = somaimpar/contimpar

par = [0 for x in range(contpar)]
impar = [0 for x in range(contimpar)]
cont = 0
cont1 = 0

for i in range(10):
    if a[i] % 2 == 0:
        if a[i] > mediapar:
            par[cont] = a[i]
            cont += 1

    else:
        if a[i] < mediaimpar:
            impar[cont1] = a[i]
            cont1 += 1

print("Média Par:",mediapar, "\nMédia Impar:",mediaimpar)
print("Maior número par:",maior,"\nMenor número impar:",menor)

print("Maiores que media par:")
for i in range(cont):
    print(par[i])

print("Maiores que media impar:")
for i in range(cont1):
    print(impar[i])
