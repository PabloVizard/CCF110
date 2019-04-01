n = int(input("Numero de alunos: "))
from typing import NamedTuple
class notas (NamedTuple):
    nome = [0 for i in range(n)]
    turma = [0 for i in range(n)]
    nota1 = [0 for i in range(n)]
    nota2 = [0 for i in range(n)]
    nota3 = [0 for i in range(n)]
    nota4 = [0 for i in range(n)]

for i in range(n):
    notas.nome[i] = input("Nome: ")
    notas.turma[i] = input("Turma: ")
    notas.nota1[i] = float(input("Nota1: "))
    notas.nota2[i] = float(input("Nota2: "))
    notas.nota3[i] = float(input("Nota3: "))
    notas.nota4[i] = float(input("Nota4: "))

print(notas.nome)
print(notas.nota1)
