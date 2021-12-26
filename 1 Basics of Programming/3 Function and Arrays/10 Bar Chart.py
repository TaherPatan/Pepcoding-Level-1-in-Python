n = int(input())
lst = [int(input()) for i in range(n)]
for row in range(max(lst), 0, -1):
    for col in range(0, n):
        if row <= lst[col]:
            print('*', end='\t')
        else:
            print('', end='\t')
    print()
