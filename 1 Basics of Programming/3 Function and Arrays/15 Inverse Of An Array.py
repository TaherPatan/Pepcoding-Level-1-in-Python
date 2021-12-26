n = int(input())
a1 = [int(input()) for i in range(n)]
temp = [0] * n
for i in range(n):
    temp[a1[i]] = i
for i in temp:
    print(i)
