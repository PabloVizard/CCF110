n = float(input("Digite o número: "))
maior = n
menor = n

for i in range (0, 5):
    i = float (input("Digite o número: "))

    if i > n :
        maior = i

    else:
        menor = i

print("O maior valor é: {}".format(maior))
print("O menor número é: {}".format(menor))