salario = float(input("Salario Minimo: "))
quilowatt = float(input("Quilowatts gastos: "))

valor_quilowatt = (salario/7)/100
valor_conta = valor_quilowatt*quilowatt
desconto = valor_conta - (valor_conta*0.1)

print("Valor Quilowatt: R${0: .2f}".format(valor_quilowatt))
print("Valor Conta: R${0: .2f}".format(valor_conta))
print("Valor Conta com Desconto: R${0: .2f}".format(desconto))

