n = int(input())
a1 = [int(input()) for i in range(n)]
k = int(input()) % n
front = a1[0:-k:1]
back = a1[-k:]
arr = back + front
for i in arr:
    print(i, end=' ')