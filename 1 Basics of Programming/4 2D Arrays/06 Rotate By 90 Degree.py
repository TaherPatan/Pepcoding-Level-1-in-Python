n = int(input())
a1 = [[int(input()) for _ in range(n)] for _ in range(n)]
for row in range(n // 2):
    for col in range(n):
        a1[row][col], a1[n - 1 - row][col] = a1[n - 1 - row][col], a1[row][col]
for row in range(n):
    for col in range(row, n):
        a1[row][col], a1[col][row] = a1[col][row], a1[row][col]
for row in a1:
    for col in row:
        print(col, end=' ')
    print()
