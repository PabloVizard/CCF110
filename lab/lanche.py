tabela = input().split(' ')
cod = int(tabela[0])
quant = int(tabela[1])

if cod == 1:
    valor = quant*4.00
    print("Total: R$ {0:.2f}".format(valor))

elif cod == 2:
    valor = quant*4.50
    print("Total: R$ {0:.2f}".format(valor))

elif cod == 3:
    valor = quant*5.00
    print("Total: R$ {0:.2f}".format(valor))

elif cod == 4:
    valor = quant*2.00
    print("Total: R$ {0:.2f}".format(valor))

elif cod == 5:
    valor = quant*1.50
    print("Total: R$ {0:.2f}".format(valor))

