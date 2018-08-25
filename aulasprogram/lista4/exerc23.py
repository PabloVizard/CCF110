peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (pow(altura,2))

if imc < 20:
    print("Abaixo do peso!")

elif imc >= 20 and imc < 25:
    print("Peso normal!")

elif imc >=25 and imc < 30:
    print("Sobre peso!")

elif imc >= 30 and imc < 40:
    print("Obeso!")

elif imc >= 40:
    print("Obesidade Morbida!")