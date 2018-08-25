valor = float(input("Valor deposito: "))
taxa = float(input("Taxa de Rendimento: "))

taxa = (taxa/100)*valor
valor = valor + taxa

print("Rendimento: {0: .2f}".format(taxa))
print("Valor Total: {0: .2f}".format(valor))