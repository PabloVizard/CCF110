saldo = float(input("Saldo Médio: "))

if saldo >= 0 and saldo <= 500:
    print("Não tem direito a Crédito!")

elif saldo >= 501 and saldo <= 1000:
    credito = saldo*0.3
    print("Saldo Médio: {0: .2f}".format(saldo))
    print("Crédito: {0: .2f}".format(credito))

elif saldo >= 1001 and saldo <= 3000:
    credito = saldo*0.4
    print("Saldo Médio: {0: .2f}".format(saldo))
    print("Crédito: {0: .2f}".format(credito))

elif saldo >= 3001:
    credito = saldo*0.5
    print("Saldo Médio: {0: .2f}".format(saldo))
    print("Crédito: {0: .2f}".format(credito))