for i in range (1, 40000000):
    num = float(input("Digite o número: "))
    if num == -999:
        break
    else:
        num = num * 3
        print("O triplo é: {}".format(num))

