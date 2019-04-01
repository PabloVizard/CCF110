for i in range (0,5):
    pares = input().split(" ")
    a = int(pares[0])
    b = int(pares[1])

    if a < b:
        for n in range(a, (b+1)):
            if n % 2 == 0:
                print("Par: {}".format(n))

    else:
        print("A não é maior que B!")