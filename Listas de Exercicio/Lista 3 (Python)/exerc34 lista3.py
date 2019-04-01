i = 0
somamulher = 0
somahomem = 0
sim = 0
nao = 0

while i <= 2000:
    sexo = int(input())
    resposta = int(input())

    if sexo == 1:
        if resposta == 1:
            somamulher = somamulher + 1

    if sexo == 2:
        if resposta == 2:
            somahomem = somahomem + 1

    if resposta == 1:
        sim = sim + 1

    if resposta  == 2:
        nao = nao + 1

    i = i + 1

somamulher = (somamulher / i)*100
somahomem = (somahomem / i)*100

print("Porcentagem Sim Mulheres: {0: .2f}".format(somamulher))
print("POrcentagem Não Homens: {o: .2f}".format(somahomem))
print("Sim: {}".format(sim))
print("Não: {}".format(nao))