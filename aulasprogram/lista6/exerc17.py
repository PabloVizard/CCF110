vetor = [0 for i in range(20)]
contvetor = 1
impares = [0 for i in range(10)]
cont = 0

for i in range(20):
    vetor[i] = contvetor

    if contvetor % 2 != 0:
        temp = pow(vetor[i], 2)
        impares[cont] = temp
        cont += 1

    contvetor += 1

print(impares)
print(vetor)