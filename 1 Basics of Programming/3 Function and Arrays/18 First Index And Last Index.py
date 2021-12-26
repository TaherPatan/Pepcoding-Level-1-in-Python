def binary_search_modified(arr, n):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > n:
            high = mid - 1
        elif arr[mid] < n:
            low = mid + 1
        elif arr[mid] == n:
            fi = mid
            li = mid
            while (fi - 1 >= 0 and arr[fi - 1] == n) or (li + 1 < len(arr) and arr[li + 1] == n):
                if arr[fi - 1] == n:
                    fi -= 1
                if arr[li + 1] == n:
                    li += 1
            return fi, li
    return -1, -1


n = int(input())
a1 = [int(input()) for i in range(n)]
d = int(input())
fi, li = binary_search_modified(a1, d)
print(fi)
print(li)
