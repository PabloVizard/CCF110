corredor = [0 for x in range(10)]
tempo = [0 for x in range(10)]
for i in range(10):
    corredor[i] = int(input("Corredor: "))
    tempo[i] = float(input("Tempo: "))

for i in range(10):
    for j in range(i,10):
        if tempo[i] > tempo[j]:
            temp = tempo[i]
            tempo[i] = tempo[j]
            tempo[j] = temp

            temp1 = corredor[i]
            corredor[i] = corredor[j]
            corredor[j] = temp1

for i in range(10):
    print(i+1, "colocado:",corredor[i], "no tempo:", tempo[i])