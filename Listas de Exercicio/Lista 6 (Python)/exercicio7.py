vetor = [0 for i in range(20)]
for i in range(20):
    vetor[i] = int(input())
print(vetor)
cont = 19
troca = 0
for i in range(10):
    troca = vetor[i]
    vetor[i] = vetor[cont]
    vetor[cont] = troca
    cont -= 1
print(vetor)