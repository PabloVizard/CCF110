n = int(input())
serie = 0

for i in range (1, (n+1)):
    serie += (1/ pow(i,i))

print(serie)