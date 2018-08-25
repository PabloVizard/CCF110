for i in range (1, 11):
    n = int(input())

    if i == 1:
        maior = n

    if i == 2:
        maior1 = n

    if maior < n:
        maior1 = maior
        maior = n

print("Maior: ",maior, "\nSegundo Maior: ",maior1)