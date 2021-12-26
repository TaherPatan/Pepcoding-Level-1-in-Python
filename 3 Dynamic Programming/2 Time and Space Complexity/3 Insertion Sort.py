def swap(arr, i, j):
    print(f'Swapping {arr[i]} and {arr[j]}')
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def isGreater(arr,j,i):
    print(f'Comparing {arr[i]} and {arr[j]}')
    if arr[i] < arr[j]:
        return True
    else:
        return False


def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if not isGreater(arr, j, i):
                break
            swap(arr, j, i)
            i = j


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")
    print()


if __name__ == '__main__':
    arr = []
    n = int(input())
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    insertionSort(arr)
    printList(arr)
