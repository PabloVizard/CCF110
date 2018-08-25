salario = float(input("Salário: "))
prest = float(input("Valor Prestação: "))

salario = salario*0.3

if prest/salario <= 1:
    print("O empréstimo pode ser concedido!")

else:
    print("O empréstimo não pode ser concedido!")