x = float(input())

if x <= 4 and x >= -4:
    print("A função não tem raiz real!")

else:
    fx = (5*x + 3)/pow(pow(x, 2) - 16, (1/2))
    print("f(x) = ", fx)