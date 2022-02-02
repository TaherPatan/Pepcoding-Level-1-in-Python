def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    print("Merging these two arrays ")
    print("left array -> ", end="")
    for i in range(0, n1):
        L[i] = arr[l + i]
    printList(L)
    print("right array -> ", end="")
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    printList(R)
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l == r:
        return [arr[l]]
    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    mergeSort(arr, 0, n - 1)
    print("Sorted Array -> ", end="")
    printList(arr)
