altura1 = float(input("Digite a altura: "))
sexo = int(input("Digite 1 para homem e 2 para mulher: "))
maior = altura1
menor = altura1
alturas = 0
alturas1 = 0
contmulher = 0

for i in range (1, 50):
    altura = float(input("Digite a altura: "))
    sexo = int(input("Digite 1 para homem e 2 para mulher: "))

    if sexo == 2:
        alturas = alturas + altura
        contmulher = contmulher + 1

    elif sexo == 1:
        alturas1 = alturas1 + altura

    if altura > altura1:
        maior = altura

    else:
        menor = altura

    media = alturas / contmulher
    medias = (alturas + alturas1)/50

print("Maior altura: {}".format(maior))
print("Menor altura: {}".format(menor))
print("Média altura meninas: {}".format(media))
print("Média alturas turma: {}".format(medias))
