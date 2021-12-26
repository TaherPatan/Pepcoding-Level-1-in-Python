n = int(input())
lst = [int(input()) for i in range(n)]
d = int(input())
if d in lst:
    print(lst.index(d))
else:
    print(-1)