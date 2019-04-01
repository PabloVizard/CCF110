quantcaixas = int(input("Quantidade Caixas: "))
precounid = float(input("Preço Kg: "))
pesocaixa = [0 for x in range(quantcaixas)]
soma = 0

for i in range(quantcaixas):
    pesocaixa[i] = float(input("Peso caixa: "))
    soma = soma + pesocaixa[i]

precomonetario = float(input("Preço Monetário Carga: "))
precocaixas = soma*precounid
print("Peso das Caixas: ", soma)

if precomonetario == precocaixas:
    print("Valor Correto!")

else:
    print("É necessário recalcular o valor da carga!")