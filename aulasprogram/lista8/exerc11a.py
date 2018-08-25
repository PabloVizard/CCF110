from typing import NamedTuple
n = 30
class reg (NamedTuple):
    ins = [0 for i in range(n)]
    nome = [0 for i in range(n)]
    altura = [0 for i in range(n)]
    peso = [0 for i in range(n)]
    natural = [ 0 for i in range(n)]
    estado = [0 for i in range(n)]

for i in range(n):
    reg.ins[i] = int(input())
    reg.nome[i] = input()
    reg.altura[i] = float(input())
    reg.peso[i] = float(input())
    reg.natural[i] = input()
    reg.estado[i] = input()