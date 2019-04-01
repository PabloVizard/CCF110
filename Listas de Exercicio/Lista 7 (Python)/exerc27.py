n = int(input())
m = int(input())
a = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())

print(a)

if n == m:
    print("Matriz Simetrica!")
else:
    print("A matriz não é simetrica!")