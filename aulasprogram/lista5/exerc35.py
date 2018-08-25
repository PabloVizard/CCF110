rendapessoal = float(input())
despesas = 0
i = 0
renda = 0

while rendapessoal != 0:
    rendafamiliar = float(input())
    totalalimenta = float(input())
    totaldespesas = float(input())

    porcentagem = ((totaldespesas + totalalimenta)/(rendapessoal + rendafamiliar))*100
    print("Porcentagem gasta com alimentação e outras despesas em relação às rendas pessoal e familiar: ", porcentagem)

    if totaldespesas >= 200:
        despesas += 1

    if rendapessoal > rendafamiliar:
        renda += 1

    i += 1
    rendapessoal = float(input())

despesas = (despesas/i)*100
print("Porcentagem dos alunos que gasta acima de R$ 200,00 com outras despesas: ", despesas)
print("Número de alunos com renda pessoal maior que renda familiar: ", renda)
