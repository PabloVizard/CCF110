x = int(input())
i = 1
soma = 0
n = 25

while i <= 25:
    soma = soma + ((pow(-1, (i-1))*(pow(x, n)/i)))

    i = i + 1
    n = n - 1

print(soma)