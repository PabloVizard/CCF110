s = 0

for i in range (0, 51):
    s = s + (pow(-1, i) / pow((i * 2 + 1), 3))
    a = pow(s*32, 1/3)

print(a)
