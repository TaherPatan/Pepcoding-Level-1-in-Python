n = int(input())
m = int(input())
a1 = [[int(input()) for j in range(m)] for i in range(n)]
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            print(a1[j][i])
    else:
        for j in range(n - 1, -1, -1):
            print(a1[j][i])
