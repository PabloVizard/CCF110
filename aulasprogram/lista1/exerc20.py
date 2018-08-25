idade = float(input("Digite a idade: "))

if idade <= 16:
    print ("Você não é eleitor!")

elif 18 <= idade <= 65:
    print("Você é eleitor Obrigátorio!")

else:
    print ("Você é eleitor facultativo!")