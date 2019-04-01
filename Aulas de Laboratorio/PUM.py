n = int(input())
linha = n*4

for i in range (1, (linha + 1)):
    if i % 4 == 0:
        print(i-3, i-2, i-1, "PUM")