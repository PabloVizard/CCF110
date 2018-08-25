n = int (input("Digite o valor de n fatorial: "))
fat = 0

for i in range (0, (n+1)):
    if i == 0:
        fat = 1

    else:
        fat = fat * i

print(fat)