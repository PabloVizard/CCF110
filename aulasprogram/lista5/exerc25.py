PA = 5000000
PB = 7000000
G1 = 3
G2 = 2
tempo = 0

while PA <= PB:
    PA = PA + (PA * (G1 / 100))
    PB = PB + (PB * (G2 / 100))
    tempo += 1

print("Anos necessários: ", tempo)