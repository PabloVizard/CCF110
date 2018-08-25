menor = [0 for x in range(3)]
empregado = [0 for x in range(3)]
for i in range(300):
    empg = int(input("Número Empregdo: "))

    if empg == 00:
        break

    meses = int(input("Meses Trabalhados: "))

    if i == 0:
        menor[0] = meses
        empregado[0] = empg

    if meses <= menor[0]:
        menor[2] = menor[1]
        empregado[2] = empregado[1]
        menor[1] = menor[0]
        empregado[1] = empregado[0]
        menor[0] = meses
        empregado[0] = empg

for i in range(3):
    print(i+1, "Menor: ", menor[i], "do empregado: ", empregado[i])