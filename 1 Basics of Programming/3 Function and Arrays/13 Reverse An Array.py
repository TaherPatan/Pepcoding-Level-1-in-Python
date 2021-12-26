n = int(input())
arr_a = [int(input()) for i in range(n)]
left, right = 0, len(arr_a) - 1
while left < right:
    arr_a[left], arr_a[right] = arr_a[right], arr_a[left]
    left += 1
    right -= 1
for i in arr_a:
    print(i, end=' ')
