n = 10
m = 4
alunos = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            alunos[i][j] = int(input("Matricula: "))
        elif j == 1:
            alunos[i][j] = int(input("Sexo (0 para MUlher, 1 para Homem): "))
        elif j == 2:
            alunos[i][j] = input("Código curso: ")
        elif j == 3:
            alunos[i][j] = int(input("Coeficiente de Rendimento: "))

escolhido = input("Turma escolhida: ")
cont = 0
for i in range(n):
    for j in range(m):
        if j == 2:
            if cont == 0:
                temp = 1
                maior = alunos[i][3]
                cont += 1

            elif alunos[i][j] == escolhido:
                if alunos[i][3] >= maior:
                    temp = i
                    maior = alunos[i][j]

print("O aluno selecionado é: {} com CR: {}".format(alunos[temp][0], alunos[temp][3]))