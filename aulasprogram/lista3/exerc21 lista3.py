alunos = int(input())
soma = 0

for i in range(1, (alunos+1)):
    nome = input("Nome: ")
    prova1 = float(input("Prova1: "))
    prova2 = float(input("Prova2: "))
    prova3 = float(input("Prova3: "))
    prova4 = float(input("Prova4: "))
    prova5 = float(input("Prova5: "))

    if prova1 >= 7 and prova2 >= 7 and prova3 >= 7 and prova4 >= 7 and prova5 >= 7:
        print("{} APROVADO EM TODAS AS MATERIAS".format(nome))

    if prova1 >= 7 and prova4 >= 7:
        print("{} APROVADO NAS MATERIAS 1 E 4".format(nome))

    if prova3 >= 7:
        soma = soma + 1

porcento = (soma / alunos)*100
print("PORCENTAGEM DE ALUNOS APROVADOS NA MATERIA 3: {}".format(porcento))