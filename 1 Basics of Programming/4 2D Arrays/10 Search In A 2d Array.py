n = int(input())
arr1 = [[int(input()) for _ in range(n)] for _ in range(n)]
x = int(input())
i = 0
j = len(arr1[0]) - 1
while i < len(arr1) and j >= 0:
    if x > arr1[i][j]:
        i += 1
    elif x < arr1[i][j]:
        j -= 1
    else:
        print(i)
        print(j)
        exit()
print("Not Found")