def binary_search_modified(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    ceil = 0
    floor = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
            floor = arr[mid]
        elif arr[mid] > n:
            high = mid - 1
            ceil = arr[mid]
        elif arr[mid] == n:
            return arr[mid], [mid]
    return floor, ceil


n = int(input())
a1 = [int(input()) for i in range(n)]
d = int(input())
fi, li = binary_search_modified(a1, d)
print(li)
print(fi)
