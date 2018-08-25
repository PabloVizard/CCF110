a = float(input("Valor: "))
b = float(input("Valor: "))
c = float(input("Valor: "))

if a > b and a > c:
    if b > c:
        print("{},{},{}".format(a,b,c))

    elif c > b:
        print("{},{},{}".format(a,c,b))

    else:
        print("{},{}".format(a,b))

elif b > a and b > c:
    if a > c:
        print("{},{},{}".format(b,a,c))

    elif c > a:
        print("{},{},{}".format(b,c,a))

    else:
        print("{},{}".format(b,a))

elif c > a and c > b:
    if a > b:
        print("{},{},{}".format(c,a,b))

    elif b > a:
        print("{},{},{}".format(c,b,a))

    else:
        print("{},{}".format(c,a))