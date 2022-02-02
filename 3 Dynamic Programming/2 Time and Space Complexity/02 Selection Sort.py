def swap(arr, i, j):
    print("Swapping",arr[i],"and",arr[j])
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def isSmaller(arr, i, j):
    print("Comparing", arr[i], "and", arr[j])
    if arr[i] < arr[j]:
        return True
    else:
        return False


def selectionSort(arr):
    for i in range(len(arr) - 1):
        small = i
        for j in range(i + 1, len(arr)):
            if isSmaller(arr, j, small):
                small = j
        swap(arr, i, small)


def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()


if __name__ == '__main__':
    arr = []
    n = int(input())
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    selectionSort(arr)
    printList(arr)