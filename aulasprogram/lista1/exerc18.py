a = float(input("Digite o valor a ser analizado: "))
b = float(input("Digite o valor para analisar como multiplo: "))

div = a % b

if div == 0:
    print("O número {} é multiplo de {}".format(a, b))

else:
    print("O número {} não é multiplo de {}".format(a, b))