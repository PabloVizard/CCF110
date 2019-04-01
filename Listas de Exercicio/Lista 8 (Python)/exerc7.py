n = int(input("Numeros de Cadastros: "))
from typing import NamedTuple
class cadastro (NamedTuple):
    nome = [0 for i in range(n)]
    telefone = [0 for i in range(n)]
    aniversario = [0 for i in range(n)]
    cidade = [0 for i in range(n)]
    estado = [0 for i in range(n)]

for i in range(n):
    cadastro.nome[i] = input("Nome: ")
    cadastro.telefone[i] = input("Telefone: ")
    cadastro.aniversario[i] = input("Aniversario: ")
    cadastro.cidade[i] = input("Cidade: ")
    cadastro.estado[i] = input("Estado: ")