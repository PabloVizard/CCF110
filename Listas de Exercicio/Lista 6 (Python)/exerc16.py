n = int(input("Produtos a serem digitados: "))

preco = [0 for x in range(n)]
nome = [0 for x in range(n)]

for i in range(n):
    nome[i] = input()
    preco[i] = float(input())

for i in range(n):
    temp = preco[i]
    dolar = temp* 3.4840
    print("Produto:",nome[i], "\nValor R$",preco[i], "\nValor U${0:.2f}".format(dolar))