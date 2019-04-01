n = int(input("Numeros de Cadastros: "))
from typing import NamedTuple
class medico (NamedTuple):
    matricula = [0 for i in range(n)]
    nome = [0 for i in range(n)]
    inicio = [0 for i in range(n)]
    fim = [0 for i in range(n)]
    especialidade = [0 for i in range(n)]

for i in range(n):
    medico.matricula[i] = input("Matricula: ")
    medico.nome[i] = input("Nome: ")
    medico.inicio[i] = input("Harario de Entrada: ")
    medico.fim[i] = input("Horario de Saida: ")
    medico.especialidade[i] = input("Especialidade: ")