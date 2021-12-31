def findpivot(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1
    return arr[high]


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    pivot = findpivot(arr)
    print(pivot)
