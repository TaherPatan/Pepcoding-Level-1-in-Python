n = int(input())
m = int(input())
a1 = [[int(input()) for j in range(m)] for i in range(n)]
for i in a1:
    for j in i:
        print(j, end=' ')
    print()
