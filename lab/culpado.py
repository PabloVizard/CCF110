n = int(input())

if n != 0:
    for i in range(n):
        aluno = input().split()
        alunos = [0 for x in range(n+1)]
        a = int(input())

        for i in range(1, n+1):
            alunos[i] = int(aluno.split(" ")[i-1])

        while True:
            if aluno[a] == a:
                print(aluno[a])
                break

            else:
                a = aluno[a]
