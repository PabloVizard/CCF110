peso = float(input("Peso: "))
print("Digite 1 - Mércurio \n 2 - Vênus \n 3 - Marte \n 4 - Júpiter \n 5 - Saturno \n 6 - Urano")
cod = int(input())

if cod == 1:
    peso *= 0.37

elif cod == 2:
    peso *= 0.88

elif cod == 3:
    peso *= 0.38

elif cod == 4:
    peso *= 2.64

elif cod == 5:
    peso *= 1.15

elif cod == 6:
    peso *= 1.17

print("Peso: ",peso)