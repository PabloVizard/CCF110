n = int(input("Numero de Voos: "))
from typing import NamedTuple
class voo (NamedTuple):
    nvoo = [0 for i in range(n)]
    tipo = [0 for i in range(n)]
    preco = [0 for i in range(n)]
    lugares = [0 for i in range(n)]

for i in range(n):
    voo.nvoo[i] = input("Numero do Voo: ")
    voo.tipo[i] = input("Tipo de Voo: ")
    voo.preco[i] = float(input("Preço do Voo: "))
    voo.lugares[i] = int(input("Numero de Lugares: "))