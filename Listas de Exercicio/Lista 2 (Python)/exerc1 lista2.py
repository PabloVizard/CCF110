idade = float (input("Digite a idade do paciente: "))
peso = float (input("Digite o peso do paciente: "))
ml = 20
mg = 500

if idade >= 12 and peso > 60:
    mg = 1000 / mg
    ml = mg * ml
    print ("O paciente deve tomar {} gotas".format(ml))

elif idade >= 12 and peso < 60:
    mg = 875 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))

elif idade < 12 and 5 < peso < 9:
    mg = 125 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))

elif idade < 12 and 9 < peso < 16:
    mg = 250 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))

elif idade < 12 and 16 < peso < 24:
    mg = 275 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))

elif idade < 12 and 24 < peso < 30:
    mg = 500 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))

elif idade < 12 and peso > 30:
    mg = 750 / mg
    ml = mg * ml
    print("O paciente deve tomar {} gotas".format(ml))