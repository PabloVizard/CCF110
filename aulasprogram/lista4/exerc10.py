produto = float(input("Valor produto: "))

desconto = produto * 0.09
total = produto + desconto

print("Desconto: {0: .2f}".format(desconto))
print("Total Final: {0: .2f}".format(total))