n = int(input())
a1 = [[int(input()) for _ in range(n)] for _ in range(n)]
for gap in range(n):
    for i, j in zip(range(0, n), range(gap, n)):
        print(a1[i][j])