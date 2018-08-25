a = 1
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
total = 0

for i in range(0, 20):
    voto = int(input())

    if voto == 1:
        soma1 = soma1 + 1

    if voto == 2:
        soma2 = soma2 + 1

    if voto == 3:
        soma3 = soma3 + 1

    if voto == 4:
        soma4 = soma4 + 1

    if voto == 5:
        soma5 = soma5 + 1

    if voto == 6:
        soma6 = soma6 + 1

print("Votos Candidatos 1: {}".format(soma1))
print("Votos Candidatos 2: {}".format(soma2))
print("Votos Candidatos 3: {}".format(soma3))
print("Votos Candidatos 4: {}".format(soma4))
print("Votos Nulos: {}".format(soma5))
print("Votos Brancos: {}".format(soma6))

total = ((soma5 + soma6)/i)*100
print("Percentual Nulos e Brancos: {0: .2f}".format(total))