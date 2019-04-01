alunos = int(input("Número de alunos: "))
nota = [0 for x in range(4)]
maior = [0 for x in range(4)]
menor = [0 for x in range(4)]
melhor = [0 for x in range(4)]
pior = [0 for x in range(4)]

for n in range(alunos):
    aluno = input()
    for i in range(4):
        nota[i] = int(input())

        if nota[i] >= maior[i]:
            maior[i] = nota[i]
            melhor[i] = aluno

        if nota[i] <= menor[i]:
            menor[i] = nota[i]
            pior[i] = aluno

    if n == 0:
        for i in range(4):
            menor[i] = nota[i]

print("Melhores notas: ", maior, "dos alunos: ", melhor)
print("Piores notas: ", menor, "dos alunos: ", pior)