n = int(input())
m = int(input())
a1 = [[int(input()) for _ in range(m)] for _ in range(n)]
minr, minc, maxr, maxc, count = 0, 0, len(a1) - 1, len(a1[0]) - 1, 0
while count < n * m:
    for i, j in zip(range(minr, maxr + 1), range(count, n * m)):
        print(a1[i][minc])
        count += 1
    minc += 1
    for i, j in zip(range(minc, maxc + 1), range(count, n * m)):
        print(a1[maxr][i])
        count += 1
    maxr -= 1
    for i, j in zip(range(maxr, minr - 1, -1), range(count, n * m)):
        print(a1[i][maxc])
        count += 1
    maxc -= 1
    for i, j in zip(range(maxc, minc - 1, -1), range(count, n * m)):
        print(a1[minr][i])
        count += 1
    minr += 1
