n = int(input())
arr1 = [[int(input()) for _ in range(n)] for _ in range(n)]
i = 0
j = 0
while i < n:
    min_idx = 0
    for j in range(n):
        if arr1[i][j] < arr1[i][min_idx]:
            min_idx = j
    for row in range(n):
        flag = True
        if arr1[row][min_idx] > arr1[i][min_idx]:
            flag = False
            break
    if flag:
        print(arr1[i][min_idx])
        break
    i += 1
if not flag:
    print("Invalid input")
