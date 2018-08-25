dividendo = int(input())
divisor = int(input())
quociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print("Quociente: ", quociente)
