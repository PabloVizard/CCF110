vetor = [0 for i in range(10)]
for i in range(10):
    vetor[i] = int(input())
n = int(input())
for i in range(10):
    if vetor[i] < n:
        print(vetor[i])
