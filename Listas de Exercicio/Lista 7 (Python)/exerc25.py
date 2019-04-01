n = 2
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

sub1 = 1
sub2 = 1
for i in range(n):
    for j in range(n):
        if i == j:
            sub1 *= a[i][j]

        if i+j == n-1:
            sub2 *= a[i][j]

det = sub1 - sub2
print("Determinante: ", det)