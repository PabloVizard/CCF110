n = int(input("Números que serão digitados: "))
num = float(input("Valor: "))
maior = num

for i in range(1, n):
    num1 = float(input("Valor: "))

    if num1 > maior:
        maior = num1

print("Maior valor é: {}".format(maior))