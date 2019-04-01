horas = input().split(' ')
hora = float(horas[0])
minutos = float(horas[1])

minutos_dia = (hora * 60) + minutos

print("Minutos passados no dia: ", minutos_dia)