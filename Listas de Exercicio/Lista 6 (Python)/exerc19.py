vetorraiz = [0 for i in range(15)]

for i in range(15):
    n = int(input())

    if n >= 0:
        vetorraiz[i] = pow(n,(1/2))

    else:
        vetorraiz[i] = -1

print(vetorraiz)