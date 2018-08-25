num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))

soma = num1 + num2

if soma > 20:
    soma = soma + 8
    print ("A soma se tornou: {}".format(soma))

else:
    soma = soma - 5
    print("Soma se tornou: {}".format(soma))