n = int(input("Numeros de Cadastros: "))
from typing import NamedTuple
class filmes (NamedTuple):
    titulo = [0 for i in range(n)]
    duracao = [0 for i in range(n)]
    sessoes = [0 for i in range(n)]

for i in range(n):
    filmes.titulo[i] = input("Titulo: ")
    filmes.duracao[i] = int(input("Duração: "))
    filmes.sessoes[i] = input("Sessões: ")