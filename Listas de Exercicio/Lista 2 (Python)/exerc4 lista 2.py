mes = int(input("Digite o número do mês: "))

if mes == 1 or mes == 2 or mes == 3:
    print("Esse mês pertence ao 1 trimestre do ano!")

elif mes == 4 or mes == 5 or mes == 6:
    print("Esse mês pertence ao 2 trimestre do ano!")

elif mes == 7 or mes == 8 or mes == 9:
    print("Esse mês pertence ao 3 trimestre do ano!")

elif mes == 10 or mes == 11 or mes == 12:
    print("Esse mês pertence ao 4 trimestre do ano!")

else:
    print("Mês inválido!")