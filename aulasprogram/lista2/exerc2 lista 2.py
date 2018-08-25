caixa = float(input("Digite o valor em caixa: "))
bola = float(input("Digite o número da bola sorteada: "))

if bola == 0 or bola == 5:
    premio = caixa * 0.05
    print("O prêmio é de R${}".format(premio))

elif bola == 1:
    premio = caixa * 0.25
    print("O prêmio é de R${}".format(premio))

elif bola == 2 or bola == 9:
    premio = caixa * 0.1
    print("O prêmio é de R${}".format(premio))

elif bola == 3:
    premio = caixa * 0.07
    print("O prêmio é de R${}".format(premio))

elif bola == 4:
    premio = caixa * 0.08
    print("O prêmio é de R${}".format(premio))

elif bola == 6:
    premio = caixa * 0.15
    print("O prêmio é de R${}".format(premio))

elif bola == 7:
    premio= caixa * 0.12
    print("O prêmio é de R${}".format(premio))

elif bola == 8:
    premio = caixa * 0.03
    print("O prêmio é de R${}".format(premio))

else:
    print("Número de bola inválido!")