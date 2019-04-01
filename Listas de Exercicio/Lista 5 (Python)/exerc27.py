massa = int(input("Massa em gramas: "))
tempo = 0

while massa >= 0.10:
    massa -= (massa*0.25)
    tempo += 30

print("Tempo para o processo: ", tempo, "segundos.")