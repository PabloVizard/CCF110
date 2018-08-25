#coding: utf-8
tempo = int (input ("Digite o tempo gasto na viagem: "))
velocidade = int(input("Digite a velocidade média: "))
distancia = tempo * velocidade
litros = distancia/12
print ("A distancia percorrida é de: ", velocidade)
print ("Os litros gastos são: ", litros)