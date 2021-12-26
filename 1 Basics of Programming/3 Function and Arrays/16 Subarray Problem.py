n = int(input())
a1 = [int(input()) for i in range(n)]
temp = a1.copy()
while True:
    if temp:
        for i in range(1, len(temp) + 1):
            for j in range(i):
                print(temp[j], end='\t')
            print()
        temp.pop(0)
    else:
        break
