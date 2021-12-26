def printlist(arr):
    for i in arr:
        print(i)


def swap(arr, i, j) :
    print("Swapping index", i, "and index", j)
    arr[i], arr[j] = arr[j], arr[i]


def sort012(arr):
    i, j, k = 0, 0, len(arr) - 1
    while i <= k:
        if arr[i] == 0:
            swap(arr, i, j)
            j += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            swap(arr, i, k)
            k -= 1


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    sort012(arr)
    printlist(arr)
