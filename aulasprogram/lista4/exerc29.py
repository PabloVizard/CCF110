caloria = 0
prato = int(input("Digite 1 para Vegetariano, 2 para Peixe, 3 para Frango e 4 para Carne: "))

if prato == 1:
    caloria = caloria + 180

elif prato == 2:
    caloria = caloria + 230

elif prato == 3:
    caloria = caloria + 250

elif prato == 4:
    caloria = caloria + 350

sobremesa = int(input("Digite 1 para Abacaxi, 2 para Sorvete Diet, 3 para Mousse Diet, 4 para Mousse Chocolate: "))

if sobremesa == 1:
    caloria = caloria + 75

elif sobremesa == 2:
    caloria = caloria + 110

elif sobremesa == 3:
    caloria = caloria + 170

elif sobremesa == 4:
    caloria = caloria + 200

bebida = int(input("Digite 1 para Chá, 2 para Suco de Laranja, 3 para Suco de Melão e 4 para Refrigerante Diet: "))

if bebida == 1:
    caloria = caloria + 20

elif bebida == 2:
    caloria = caloria + 70

elif bebida == 3:
    caloria = caloria + 100

elif bebida == 4:
    caloria = caloria + 65

print("Calorias: ",caloria)