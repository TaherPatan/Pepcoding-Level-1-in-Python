def swap(arr, i, j):
    print("Swapping", arr[i], "and", arr[j])
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, pivot):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= pivot:
            swap(arr, i, j)
            j += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    pivot = int(input())
    partition(arr, pivot)
    printList(arr)
