n = 100
preco = [0 for x in range(n)]
for i in range(n):
    print("Registro do produto ",i+1)
    preco[i] = float(input("Preço produto: "))

soma = 0
venda = int(input("Número de Produtos Vendidos no Mês: "))
for i in range(venda):
    cod = int(input("Código: "))
    quant = int(input("Quantidade: "))
    soma += preco[cod-1] * quant

print("Faturamento do mês: {0:.2f}".format(soma))