n = int(input())
soma = 0

vetor = [0 for x in range(n)]
for i in range(n):
    vetor[i] = int(input())

for i in range(n):
    if i % 2 == 0:
        soma = soma + vetor[i]

print("Soma: ", soma)