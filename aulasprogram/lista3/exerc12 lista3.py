contpar = 0
contimpar = 0
somapar = 0
somaimpar = 0
maior = 0
menor = 0

for i in range(0, 40000000):
    n = int(input("Valor: "))

    if n < 0:
        break

    if contpar == 0 and n % 2 == 0:
        maior = n

    if contimpar == 0 and n % 2 != 0:
        menor = n

    if n % 2 == 0:
        contpar = contpar + 1
        somapar = somapar + n

        if n > maior:
            maior = n

    else:
        contimpar = contimpar + 1
        somaimpar = somaimpar + n

        if n < menor:
            menor = n

mediapar = somapar / contpar
mediaimpa = somaimpar / contimpar

print("Média pares: {}".format(mediapar))
print("Média impares: {}".format(mediaimpa))
print("Maior par: {}".format(maior))
print("Menor impar: {}".format(menor))