n = 5
m = 4
manicure = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            manicure[i][j] = input("Manicure: ")
        elif j == 1:
            manicure[i][j] = int(input("Pés Feitos: "))
        elif j == 2:
            manicure[i][j] = int(input("Mãos Feitas: "))
        elif j == 3:
            manicure[i][j] = int(input("Serviço Podologico Feito: "))

for i in range(n):
    salario = 0
    for j in range(m):
        if j >= 1:
            if j == 1:
                salario += manicure[i][j]*10
            elif j == 2:
                salario += manicure[i][j]*15
            elif j == 3:
                salario += manicure[i][j]*30
    print("Manicure {} tem salario: {}".format(manicure[i][0], salario*0.5))