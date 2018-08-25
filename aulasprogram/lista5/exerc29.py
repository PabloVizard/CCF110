n = int(input())
somapar = 0
multimpar = 1

while n != 0:
    if n % 2 == 0:
        somapar += n

    elif n % 2 != 0:
        multimpar *= n

    n = int(input())

print("Soma par: ", somapar, "\nProduto Impar: ",multimpar)
