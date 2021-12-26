n = int(input())
a1 = [int(input()) for i in range(n)]
for row in range(1, max(a1) + 1):
    for col in range(0, n):
        if a1[col] > 0:
            print('*', end='\t')
            a1[col] -= 1
        else:
            print('', end='\t')
    print()
