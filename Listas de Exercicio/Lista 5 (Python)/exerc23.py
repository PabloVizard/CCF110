n = int(input())
maior = n
menor = n

while n != -1:
    if n > maior:
        maior = n

    elif menor > n:
        menor = n

    n = int(input())

print("Maior: ", maior, "\nMenor: ", menor)