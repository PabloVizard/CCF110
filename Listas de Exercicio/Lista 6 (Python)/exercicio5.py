vetor = [0 for i in range(30)]
for i in range(30):
    vetor[i] = int(input())
a = int(input())
for i in range(30):
    conta = vetor[i] * a
    if conta % 2 == 0:
        print(conta, "Par")
    else:
        print(conta, "Impar")