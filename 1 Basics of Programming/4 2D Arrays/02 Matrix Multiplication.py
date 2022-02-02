n1, m1 = int(input()), int(input())
one = [[int(input()) for _ in range(m1)] for _ in range(n1)]
n2, m2 = int(input()), int(input())
two = [[int(input()) for _ in range(m2)] for _ in range(n2)]
if m1 != n2:
    print("Invalid input")
    quit()
prd = [[0 for _ in range(m2)] for _ in range(n1)]
for i in range(len(prd)):
    for j in range(len(prd[0])):
        val = 0
        for k in range(m1):
            val += one[i][k] * two[k][j]
        prd[i][j] = val
for i in prd:
    for j in i:
        print(j, end=' ')
    print()
